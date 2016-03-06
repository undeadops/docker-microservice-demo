# docker-microservice-demo
Playing with Ideas of a Python Flask Micro-Services, utilizing MongoDB, etcd, nginx, and multiple REST API's


## Idea's built into this project

 - Unittests are not being performed
 - Code is in no way production quality
 - purpose of this is to demonstrate service discovery/registration, and multiple "micro" services.


### Service Names and their purpose

 - mongo - Database, simple, effective, not doing much with it.
 - data - REST API for accessing data from Mongo (Remove Mongo Dependency from other services)
 - app - Application, pulling Data from Data Layer
 - web - Nginx Load Balancer
 - grandcentral - etcd container for service discovery


