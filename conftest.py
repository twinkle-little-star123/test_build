import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def brower():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument('--start-maximized')

    global driver

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.close()
    return driver





@pytest.fixture(scope='session',autouse=True)
def session():
    print('before session......')
    yield
    print('after session......')


@pytest.fixture(scope='module',autouse=True)
def session():
    print('before module......')
    yield
    print('after module......')


@pytest.fixture(scope='class',autouse=True)
def session():
    print('before class......')
    yield
    print('after class......')


@pytest.fixture(scope='function',autouse=True)
def session():
    print('before function......')
    yield
    print('after function......')