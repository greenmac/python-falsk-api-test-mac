# 指令順序

## 參考網頁
https://stackoverflow.com/questions/54794217/opening-port-80-on-oracle-cloud-infrastructure-compute-node/54835902#54835902

```
sudo apt install firewalld
```

```
sudo firewall-cmd --zone=public --permanent --add-port=5000/tcp
```

```
sudo firewall-cmd --reload
```

```
pip3 install -r requirements.txt
```

```
python3 -m gunicorn --workers 4 --bind 0.0.0.0:5000 main:app
```

## oracle cloud 開啟防火牆對外port參考網頁

https://izo.tw/oracle-cloud-port/

### CLICK

http://{Public IP address}:5000