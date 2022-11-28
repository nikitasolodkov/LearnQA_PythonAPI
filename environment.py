import os

# export MY_VAR="123"
# set MY_VAR="123"

class Environment:

    DEV = 'dev'
    PROD = 'prod'
    FIRST = 'first'
    SECOND = 'second'

    URLS = {
        DEV: "https://playground.learnqa.ru/ajax/api/dev",
        PROD: "https://playground.learnqa.ru/ajax/api",
        FIRST: "https://playground.learnqa.ru/api",
        SECOND: "https://playground.learnqa.ru/api/dev",
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")

ENV_OBJECT = Environment()