import telegram
from pokemongo_bot.base_task import BaseTask


class telegramTask(BaseTask):
  SUPPORTED_TASK_API_VERSION = 1
  update_id=None
  tbot=None

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
    print(self.bot.metrics)
    for update in self.tbot.getUpdates(offset=self.update_id, timeout=10):
      if update.message:
        if update.message.text=="/info":
          res="test"
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
