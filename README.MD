## Reference NOTES
Running commands in the container
This is an example commmand
Project is the name of the servicedocker-compose run --rm app sh -c "django-admin startproject project ."
```docker-compose run --rm project sh -c "django-admin startproject project ." ```
To stop all running containers.
This command lists them and then stops them
```docker stop $(docker ps -q)```