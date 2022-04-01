from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

DEBUG = True


class ENV():
    _instance = None
    _loaded = False
    _env = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(ENV, self).__new__(self)
        return self._instance

    def load(self, env):
        if env != self._env:
            self._env = env
            self._loaded = False
        if not self._loaded:
            path = join(dirname(__file__), env)
            if DEBUG:
                print(f'Loading {path}')
            load_dotenv(path)
            self._loaded = True
        return environ

    def get(self, env, key):
        return self.load(env).get(key)


print(ENV().get('.env', 'DB_USER'))
print(ENV().get('.env', 'DB_Pass'))
