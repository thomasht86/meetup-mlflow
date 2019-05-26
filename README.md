# Trondheim Machine Learning Meetup - MlFlow
This repo contains instructions and code to follow the demo presented 29-05-2019.

## Create an Azure subscription
If you already have access to an active Azure subscription, you can use this. 
Otherwise, you can create a free account with $200 of credits [here](https://azure.microsoft.com/en-us/free/).

## Set up environment
This is a guide to help you set up your development environment so that you can follow the demo on your own computer. (And use MlFlow for your own projects afterwards)
### Mac users
1. [Install Anaconda (Python 3.7 version)](https://www.anaconda.com/distribution/)
2. Optional: Install Visual Studio Code
3. Install Homebrew python.
From [MlFlow docs](https://mlflow.org/docs/latest/index.html):
You cannot install MLflow on the MacOS system installation of Python. We recommend installing Python 3 through the Homebrew package manager using brew install python.

### Windows 10 users
MlFlow does not support installation on Windows (yet). But I will describe one way that you can make it work anyway, that may also be useful for other development scenarios. This is only possible for windows 10. For users with earlier windows versions, I do not have a solution, unfortunately.

With Windows 10 came the opportunity to install Windows Subsystem for Linux (WSL). This enables us to access a full Linux environment without the overhead of a virtual machine. WSL is not enabled by default, but must be configured. Here is a straightforward recipe to achieve this. (Choose Ubuntu 18.04 as the Linux distribution from the Microsoft store)
1. Install Anaconda in WSL your Ubuntu 18.04 shell according to [these](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart) instructions.
2. Install [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/) (in Windows)
3. Install [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for Visual Studio Code
This allows us to access the Linux filesystem from VS Code.
4. Open the linux filesystem from VS Code 
A)
Open the Ubuntu 18.04 application. 
Run the command:

```code-insiders .```

Necessary components will be installed, and VS Code with access to the WSL file system will be launched.
OR
B) 
Open Visual Studio Code - Insiders, open the command palette (Ctrl+Shift+P) and choose "Remote WSL: New window".
You should now be able to open a folder on the Ubuntu filesystem from Visual Studio Code Insiders. 

### Linux users
1. [Install Anaconda (Python 3.7 version)](https://www.anaconda.com/distribution/)

Go to MlFlow installation.

## MlFlow installation
MlFlow 1.0 is [very close](https://mlflow.org/news/2019/05/22/1.0.0-release-candidate-1/index.html). They have published a release candidate version, and it is this one we will use for this workshop.
For all functions of the mlflow cli to work as expected, it is recommended to install MlFlow in the conda base environment (Not doing this requires additional workarounds). 
To install, run the following command (must be run from WSL bash for windows users):

```pip install https://mlflow-snapshots.s3-us-west-2.amazonaws.com/mlflow-1.0.0.rc0-1173.fb8a711-py2.py3-none-any.whl```

This will install the release candidate version. 

## Training 
- Demonstrate training+tracking on local computer
- Demonstrate training+tracking on Databricks

## Comparing
- Access results programmatically

## Serving
- Serving from local computer
- Serving from ACI


