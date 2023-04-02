# Django API Course

### Requirements
* Docker

### Project architecture
In the project we are using an MVC architecture since it is better suited to the way of working of Django

~~~~shell
├── api
│   ├── courses # 
│   │   ├── controllers # Data control flow
│   │   ├── models # Business models and rules
│   │   └── views # Views to present the data
└── └── project # Settings for Django project
~~~~

### Commands

Build docker images
~~~~shell
$ make build
~~~~

Run server
~~~~shell
$ make up
~~~~

Run migrations
~~~~shell
$ make migrate
~~~~

Populate DB
~~~~shell
$ make data
~~~~