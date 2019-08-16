# pracPython
Pythonの練習。
実行は
```shell
$PRM_FILE=taco_burrito.prm gunicorn --access-logfile - -w 4 --preload wsgi:app
```

POSTは別のターミナルで
```shell 
http --form post :8000 img@パス/360.jpg 
```


docker build
```
 docker build -t tako-burrito-api .
```

docker run
```
docker run -it --rm -p 8080:8080 tako-burrito-api:latest
```

