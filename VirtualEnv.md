# Creating your Virtual Env

Create a Virtual Environment... WHY?

```
You want to save your packages and be able to transfer them over to 
other machines
```

Here's how to do it: 

1. Open a command line
2. Go into this folder
3. Look for an `.env` folder using `ls`

```commandline
python -m venv env
```

# Virtual Env Configuration

## Activating your virtual env
```commandline
. ./env/bin/activate
```

## Deactivating your virtual env
```commandline
deactivate
```

# Package Management

## Install packages from a requirement.txt file

```commandline
pip install -r requirements.txt
```
x
## Installing Individual Packages

You can find package names at the following website
[pypi](https://pypi.org/)

** Warning don't just go installing any packages. Please google/reddit packages before installing **

```commandline
pip install <package-name>
pip install pandas
pip install requests
```


## Saving your packages

Whenever you add new packages using `pip install`
you need to save your packages using the following in the terminal:
```commandline
pip freeze > requirements.txt
```

# Setting up this project on a new machine

A shortcut has been created for you to setup quickly. Run the following:

```commandline
./bootstrap
```