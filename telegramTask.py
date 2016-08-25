from pokemongo_bot.base_task import BaseTask

class Task(BaseTask):
  SUPPORTED_TASK_API_VERSION = 1
  api_key=""

  def setup(self):
    print("setup")
    self.api_key=self.config.get('api_key')

  def initialize(self):
    print("init")
    self.api_key=self.config.get('api_key')

  def work(self):
    print(self.api_key)
