# 图床

使用方法
```bash
$ git clone https://github.com/MarkusJoe/avatar.git
$ cd avatar
$ pip3 install -r requirements.txt
$ uvicorn main:app
```


上传图片测试
```python
import requests

def test_upload():
    url = 'http://127.0.0.1:8000/upload'
    files = {'file': open('test.jpg', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

if __name__ == '__main__':
    test_upload()
```