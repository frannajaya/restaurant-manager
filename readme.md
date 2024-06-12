# Restaurant Service

Monolith service of restaurant, this Backend system contains all the system that we need to serve customer. Start from
system table, system kitchen, system admin, to system serving, build in python.

## How to Run

And then, after you clone the project, make sure your computer has python (`version 3.9`) in it. Then first you need to
create virtual environment to working on it.

```commandline
python -m venv .venv 
```

Next, after you have the virtual environment, you need to install all the dependency needed to run this project.

```commandline
source .venv/bin/activate

pip install -r requirements.txt
```

After that, you can try run it by running

```commandline
fastapi dev main.py
```