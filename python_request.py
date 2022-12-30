# email liuyibo906@163.com
# 时间 2022/12/30 22:43
import requests
def test_login():
    method='post'
    url='http://hrocloud.test.feihec.com/login'
    data={'username':'chenxiang',
        'password':'654321',
        'basecode':'sida01'
    }

    res = requests.request(method, url, data=data)
    print(res)
    print(res.text)
    print(res.content)
    print(res.status_code)
    print(res.headers)
    print(res.reason)
    print(res.cookies)
    print(res.json())
    print(res.request.url)
    print(res.request.headers)
    print(res.request.method)

if __name__ == '__main__':
    test_login()