# DataBasis
DataBasis is a work-in-process with a few goals in mind

- help document tables and fields in a database
- define company metrics (or key performance indicators)
- define, share, and comment on database queries
- show links between queries, tables, and metrics
- show performance metrics for queries

## Development
Below are steps to get started developing this project.

### Prerequisites
Please make sure to install a recent version of [Python](https://www.python.org/) 3.x and the [Poetry package manager](https://python-poetry.org/).

### Create virtual environment
From within this **source-code folder**, use the following commands to create a virtual environment and install dependencies.

Activate virtual environment:
```
poetry shell
```

### Install dependencies:
```
poetry install
```

### Re-activating the virtual environment
When developing the project, you only need to install the virtual environment and dependencies when things change. Mostly, you will just re-activate the existing virtual environment when developing.

Activate the existing virtual environment:
```
poetry shell
```

### Change to project directory
Once the virtual environment is activated, you can move into the **project directory** (which is in a sub-folder of the source-code folder).

```
cd databasis
```

### Run database migrations
Make sure the database tables are created and have the proper structure.

```
python manage.py migrate
```

### Create a superuser
Create a superuser that you can use to log in and access the admin interface.

```
python manage.py createsuperuser
```

### Run the project
Start the server.

```
python manage.py runserver
```

### Access the project
With the above commands complete, you should now be able to access the server.

Front-end:
http://localhost:8000

Admin section:
http://localhost:8000/admin
