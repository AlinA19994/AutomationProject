# Automation Project

## This Project will run an end-to-end automation test on the Homme Website

## 1. Installation

### 01.

Install Python & Pip on your workstation

### 02.

Install the following packages with pip, with the following command:

```
pip install selenium~=4.0 pytest webdriver-manager smart-assertions allure-pytest
```

### 03.

Download Allure from the following link:

```
https://github.com/allure-framework/allure2/releases
```

### 04.

add the Allure bin directory to the environment variable PATH in your machine

### for windows:

```
setx PATH "%PATH%;\path\to\allure-$VERSION\bin"
```

### for linux/macOS:

```
export PATH="$PATH:/path/to/allure-$VERSION/bin"
source ~/.bashrc   # or ~/.zshrc, ~/.bash_profile depending on your shell
```

## 2. Running the Tests

## 01.

Open a Powershell Terminal or a linux Terminal and run the following commands:

```
cd test_cases
pytest -s -v .\test_web.py --alluredir=../allure/allure-result
```

## 02.

To Run the allure server:

```
cd ..\allure
allure serve .\allure-result\
```
