# 图床

部署

```bash
$ git clone https://github.com/MarkusJoe/avatar.git
$ cd avatar
$ pip3 install -r requirements.txt
$ uvicorn main:app
```

上传图片测试

```python
import hashlib
import requests
import webbrowser


def test_upload():
    url = 'http://127.0.0.1:8000/upload'
    files = {'file': open('test.jpg', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


if __name__ == '__main__':
    test_upload()
    md5 = hashlib.md5(open('test.jpg', 'rb').read()).hexdigest()
    webbrowser.open('http://127.0.0.1:8000/{}'.format(md5))
```