# full-stack-testing ![Cool Coverage](https://img.shields.io/badge/coverage-94.87%25-red) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
> this project want to do some automated testing stuff including api, browser and mobile device

### slides in Hackmd.io
* https://hackmd.io/@m_DutsiYQdSG0m1spz8yIQ/H1pLeRiQI

### hi, newbies 💂🏻
* [Mom, I'm here](doc/Newbie.md)

- - -

### setup venv ⚙️
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

### setup project interpreter (options, ide only)

### pip install
```
(venv) $ pip3 install -r requirements.txt
 or
(venv) $ pip3 install pytest
(venv) $ pip3 install urllib3
(venv) $ pip3 install selenium
(venv) $ pip3 install Appium-Python-Client
(venv) $ pip3 install allure-pytest
```
* after installed new library, you need to update requirements.txt
```
(venv) $ pip3 freeze | tee requirements.txt
```

### run test 🧙‍♂️
```
(venv) $ pytest -v -s
(venv) $ pytest -v -s tests/api/demo/get_test.py
(venv) $ pytest -v -s tests/api/
(venv) $ pytest -v -s tests/api/ --alluredir=build/allure_results
```

### unzip allure/allure-commandline-2.13.1.zip

### run allure server to see the report 👀
```
$ ./allure/allure-2.13.1/bin/allure serve build/allure_results
```

- - -

### more information about pytest
* https://docs.pytest.org/en/latest/reference.html

### more information about python selenium
* https://selenium-python.readthedocs.io/installation.html

### more information about python appium
* https://github.com/appium/python-client
