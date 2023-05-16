import configparser
import pytest


def pytest_collection_modifyitems(items):

   for item in items:
      item.name = item.name.encode('utf-8').decode('unicode_escape')
      item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


@pytest.fixture()
def logindata():

   config = configparser.ConfigParser()
   config.read('d://study/pythonProject/testcases/config.ini')
   loginData = []
   print(config.sections(),config.default_section,config.has_section("default"))
   for key in config["test"]:

      if key == "url":
         url = config["test"].get(key)
         loginData.append(url)
      elif key == "user":
         user = config["test"].get(key)
         loginData.append(user)
      elif key == "passwd":
         passwd = config["test"].get(key)
         loginData.append(passwd)


   return loginData