## Reference NOTES
Running commands in the container
This is an example commmand
```docker-compose run --rm app sh -c "django-admin startproject app ." ```
To stop all running containers.
This command lists them and then stops them
```docker stop $(docker ps -q)```