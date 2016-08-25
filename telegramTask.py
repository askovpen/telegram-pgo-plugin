from pokemongo_bot.base_task import BaseTask

class Task(BaseTask):
  SUPPORTED_TASK_API_VERSION = 1
  api_key=""

  def initialize(self):
    print("init")
    self.api_key=self.config.get('api_key')
    if api_key==None:
      self.emit_event(
        'api_error',
        formatted='api_key not defined.'
      )

  def work(self):
    print(self.api_key)
