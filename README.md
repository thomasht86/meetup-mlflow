# Trondheim Machine Learning Meetup - MlFlow
This repo contains instructions and code to follow the demo presented 29-05-2019.
The tutorial will demonstrate the lifecycle of a text classifier through the following phases:
1. Experimenting and EDA in jupyter notebook.
2. Script (with MlFlow) to run structured experiments (potentially in cloud)
3. Evaluating results of experiments and choosing a model to deploy.
4. Deploy the selected model to production in Azure. 
5. Making requests to the model. 

## Set up environment
This is a guide to help you set up your development environment if you want follow the demo on your own computer. (And use MlFlow for your own projects afterwards). 

If you don't manage to set this up, don't worry. Join the meetup and watch the big screen with a beer instead. :)

### Mac users
1. [Install Anaconda (Python 3.7 version)](https://www.anaconda.com/distribution/)
2. Optional: Install Visual Studio Code
3. Install Homebrew python.
From [MlFlow docs](https://mlflow.org/docs/latest/index.html):
You cannot install MLflow on the MacOS system installation of Python. We recommend installing Python 3 through the Homebrew package manager using brew install python.

### Windows 10 users
MlFlow does not support installation on Windows (yet). But I will describe one way that you can make it work anyway, that may also be useful for other development scenarios. This is only possible for windows 10. For users with earlier windows versions, I do not have a solution, unfortunately.

With Windows 10 came the opportunity to install Windows Subsystem for Linux (WSL). This enables us to access a full Linux environment without the overhead of a virtual machine. WSL is not enabled by default, but must be configured. 
1. Enable WSL and install Ubuntu 18.04 according to [these](https://docs.microsoft.com/en-us/windows/wsl/install-win10) instructions. (Choose Ubuntu 18.04 as the Linux distribution from the Microsoft store)
2. Install Anaconda in WSL your Ubuntu 18.04 shell:

    ```wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh```

    ```sh Anaconda3-2019.03-Linux-x86_64.sh```

    Answer "yes" to all prompts.
3. Install [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/) in Windows.
4. Install [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for Visual Studio Code
This allows us to access the Linux filesystem from VS Code.
5. Open the linux filesystem from VS Code 

Then do either A or B:

A)
Open the Ubuntu 18.04 application. 
Run the command:

    ```code-insiders .```

Necessary components will be installed, and VS Code with access to the WSL file system will be launched.

B) 
Open Visual Studio Code - Insiders, open the command palette (Ctrl+Shift+P) and choose "Remote WSL: New window".
You should now be able to open a folder on the Ubuntu filesystem from Visual Studio Code Insiders. 

### Linux users
1. Install Anaconda 

    ```wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh```

    ```sh Anaconda3-2019.03-Linux-x86_64.sh```

    Answer "yes" to all prompts.


## Create an Azure subscription
If you already have access to an active Azure subscription, you can use this. 
Otherwise, you can create a free account with $200 of credits [here](https://azure.microsoft.com/en-us/free/).

## Create and configure a github account
Can be done [here](www.github.com).

## MlFlow installation
MlFlow 1.0 is [very close](https://mlflow.org/news/2019/05/22/1.0.0-release-candidate-1/index.html). They have published a release candidate version, and it is this one we will use for this workshop.
For all functions of the mlflow cli to work as expected, it is recommended to install MlFlow in the conda base environment (Not doing this requires additional workarounds). 
To install, run the following command (must be run from WSL bash for windows users):

```pip install https://mlflow-snapshots.s3-us-west-2.amazonaws.com/mlflow-1.0.0.rc0-1173.fb8a711-py2.py3-none-any.whl```

This will install the release candidate version. 

## AzureML SDK installation
Also in conda "base" environment:

```pip install azureml-sdk```

If you made it through, well done! If not, we will spend some time in the beginning of the meetup to try to get as many as possible set up. You will also hopefully learn something from just watching the demo.


