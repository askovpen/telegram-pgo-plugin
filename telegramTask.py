import telegram
import pprint
from pokemongo_bot.base_task import BaseTask

class telegramTask(BaseTask):
  SUPPORTED_TASK_API_VERSION = 1
  update_id=None
  tbot=None

  def __init__(self, bot, config):
    super(telegramTask, self).__init__(bot, config)

  def initialize(self):
    print("init")
    api_key=self.config.get('api_key')
    if api_key==None:
      self.emit_event(
        'config_error',
        formatted='api_key not defined.'
      )
      return
    self.tbot = telegram.Bot(api_key)
    try:
      self.update_id = self.tbot.getUpdates()[0].update_id
    except IndexError:
      self.update_id = None

  def work(self):
    for update in self.tbot.getUpdates(offset=self.update_id, timeout=10):
      self.update_id=update.update_id+1
      if update.message:
        if update.message.text=="/info":
          stats=self._get_player_stats()
          with self.bot.database as conn:
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT COUNT(encounter_id) FROM catch_log WHERE dated >= datetime('now','-1 day')")
            catch_day=cur.fetchone()[0]
            cur.execute("SELECT DISTINCT COUNT(pokestop) FROM pokestop_log WHERE dated >= datetime('now','-1 day')")
            ps_day=cur.fetchone()[0]
          res=(
            "_Level:_ "+str(stats["level"]),
            "_XP:_ "+str(stats["experience"])+"/"+str(stats["next_level_xp"]),
            "_Pokemons Captured:_ "+str(stats["pokemons_captured"])+" ("+str(catch_day)+" _today_)",
            "_Poke Stop Visits:_ "+str(stats["poke_stop_visits"])+" ("+str(ps_day)+" _today_)",
            "_KM Walked:_ "+str(stats["km_walked"])
          )
          self.tbot.sendMessage(chat_id=update.message.chat_id, parse_mode='Markdown', text="\n".join(res))

  def _get_player_stats(self):
    """
    Helper method parsing the bot inventory object and returning the player stats object.
    :return: The player stats object.
    :rtype: dict
    """
    # TODO : find a better solution than calling the api
    inventory_items = self.bot.api.get_inventory() \
      .get('responses', {}) \
      .get('GET_INVENTORY', {}) \
      .get('inventory_delta', {}) \
      .get('inventory_items', {})
    return next((x["inventory_item_data"]["player_stats"]
        for x in inventory_items
        if x.get("inventory_item_data", {}).get("player_stats", {})),
      None)
