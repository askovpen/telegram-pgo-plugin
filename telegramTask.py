from pokemongo_bot.base_task import BaseTask

class Task(BaseTask)
  SUPPORTED_TASK_API_VERSION = 1

  def initialize(self):
    print("init")
    self.api.key=self.config.get('api_key')

  def work(self):
    print(self.api.key)
