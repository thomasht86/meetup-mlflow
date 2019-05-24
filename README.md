# meetup-mlflow
Trondheim Machine Learning Meetup - MlFlow

## Preparation
This is a guide to help you set up your development environment so that you can follow the demo on your own computer. (And use MlFlow for your own projects afterwards)
### Mac users
1. Install Anaconda
2. Install Visual Studio Code
3. Install MlFlow
You cannot install MLflow on the MacOS system installation of Python. We recommend installing Python 3 through the Homebrew package manager using brew install python. (In this case, installing MLflow is now pip3 install mlflow).

### Windows 10
MlFlow does not support installation on Windows (yet). But I will describe one way that you can make it work anyway, that may also be useful for other development scenarios. This is only possible for windows 10. For users with earlier windows versions, I do not have a solution, unfortunately.

With Windows 10 came the opportunity to install Windows Subsystem for Linux (WSL). This enables us to access a full Linux environment without the overhead of a virtual machine. WSL is not enabled by default, but must be configured. Here is a straightforward recipe to achieve this. (Choose Ubuntu 18.04 as the Linux distribution from the Microsoft store)
1. Install Anaconda in WSL your Ubuntu 18.04 shell according to these instructions
2. Install Visual Studio Code Insiders (in Windows)
3. Install Remote Development Extension Pack for Visual Studio Code
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

## Training 

## Comparing

## Serving

## Deploying


