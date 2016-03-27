# docker-microservice-demo
Playing with Ideas of Multiple Python Flask Micro-Services, utilizing MongoDB, etcd, nginx, and RabbitMQ/NSQ

## Idea's built into this project

    Purpose of this is to demonstrate service discovery/registration, and multiple "micro" services.
    Unittests are not being performed
    Code is in no way production quality

### Service Names and their purpose

 - mongo - Database, simple, effective, not doing much with it.
 - data - REST API for accessing data from Mongo (Remove Mongo Dependency from other services)
 - app - Application, pulling Data from Data Layer
 - web - Nginx Load Balancer
 - etcd - etcd container for service discovery
   registrator - Service Discovery for registering services on the host
