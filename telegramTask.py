import telegram
from pokemongo_bot.base_task import BaseTask


class telegramTask(BaseTask):
  SUPPORTED_TASK_API_VERSION = 1
  update_id=None
  bot=None

  def initialize(self):
    print("init")
    api_key=self.config.get('api_key')
    if api_key==None:
      self.emit_event(
        'config_error',
        formatted='api_key not defined.'
      )
      return
    self.bot = telegram.Bot(api_key)

  def work(self):
    for update in self.bot.getUpdates(offset=self.update_id, timeout=10):
      if update.message:
        print(update.message.text)
