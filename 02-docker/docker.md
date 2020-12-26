# Docker

- [Docker](#docker)
  - [DB Install](#db-install)
    - [MYSQL](#mysql)
    - [mongo](#mongo)
    - [redis](#redis)

## DB Install



### MYSQL

```shell
sudo docker run -d -p 3306:3306 --name mysql57 \
-v /home/reddy/docker_mapping/mysql/conf:/etc/mysql/mysql.conf.d  \
-v /home/reddy/docker_mapping/mysql/data:/var/lib/mysql  \
-e MYSQL_ROOT_PASSWORD=Reddyfan2020@  \
mysql:5.7
```



### mongo

```shell
sudo docker run -itd --name mongo \
-v  /home/reddy/docker_mapping/mongo/data/db:/data/db \
-p 27017:27017 mongo --auth
```



### redis

~~~shell
sudo docker run -itd -p 6379:6379  \
 -v /home/reddy/docker_mapping/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf \
 -v /home/reddy/docker_mapping/redis/data:/data  \
 --name  redis-server  redis:latest
~~~



```
 sudo docker exec -it redis-server /bin/bash
```

```
redis-cli -h 127.0.0.1 -p 6379
```

