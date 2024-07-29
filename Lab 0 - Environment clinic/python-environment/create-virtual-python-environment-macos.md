# Create Virtual Python Environment
Python applications import multiple libraries, and oftentimes, conflicts can occur between different versions of required libraries.  However your app may require a specific library version due to a bug fix.  The solution is to create a virtual environment, a self-contained suite of libraries for a specific Python installation.

We will use Python's built-in virtual environment functionality which was introduced in Python version 3.3 and provides [a built-in environments module called venv](https://docs.python.org/3/tutorial/venv.html). 

While creating your virtual Python environment below, you will also be installing all the libraries required to complete this Boot Camp including:
1. Jupyter Notebook
2. Watson Machine Learning Python SDK
3. LangChain.
4. Milvus

### 1.  Upgrade to Python v3.11 to Avoid Any Conflicts
Upgrading Python versions can be complicated so don't be afraid to ask for help during this process.  We have documented best practices to assist you.  You may have no issues using Python 3.8 plus, but recall that even Python 3.9 is 2.5 years old.  [Follow these best practices to upgrade to Python 3.11](upgrade-python.md).

### 2. Create your Python virtual environment
Create a folder where you will create and store your Python virtual environment.  Then open a terminal/console window and enter the commands below to create a Python environment called `genai`. The new virtual environment will result in a local directory by the same name.
```
cd <directory to store your Python environment>
python -m venv genai
```

### 3. Download requirements_venv.txt
Download [requirements_venv.txt](./requirements_venv.txt) which contains the list of initial packages to install in your environment.  Move the requirements.txt file to the folder that you created for your Python environments.

### 4. Activate your Python virtual environment
Execute these commands:
```
source genai/bin/activate
python -m pip install -r requirements_venv.txt
```

You can validate that your environment is active by looking at the start of the prompt line in your terminal/console window.  As shown below, the start of the prompt changes to show (genai).

<img width="532" alt="image" src="https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2024/assets/68722344/0a0ae2df-2949-48cb-83e7-f9ff347fc660">

Note: If you are a Windows user, instead of running the command `source genai/bin/activate`, follow the steps in [Setting-up-Python-Virtual-Environment-in-Windows.docx](https://github.com/Client-Engineering-Indonesia/watsonx-incubation-2024/blob/main/Lab%200%20-%20Environment%20clinic/python-environment/create-virtual-python-environment-windows.md). 


### 5. Dectivate your Python virtual environment
If you need to change to a different environment, you can deactivate your current environment using the command below:
```
deactivate
```
