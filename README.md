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

### 不要背景執行
```
python3 -m gunicorn --bind 0.0.0.0:5000 main:app
```

### 背景執行
```
python3 -m gunicorn --bind 0.0.0.0:5000 main:app --daemon
```

## oracle cloud 開啟防火牆對外port參考網頁

https://izo.tw/oracle-cloud-port/

### CLICK

http://\<Public IP address>:5000

### 刪除背景執行 

##### 停止所有 gunicorn 背景

```
pkill gunicorn
```

##### 查詢正在使用的 port
lsof -n -i:\<port>
kill -9 \<pid>