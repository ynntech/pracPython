# pracPython
Pythonの練習。
実行は
```shell
$PRM_FILE=taco_burrito.prm gunicorn --access-logfile - -w 4 --preload wsgi:app
```

POSTは別のターミナルで
```shell 
http --form post :8000 img@~/Desktop/demo/pracPython/360.jpg 
```
