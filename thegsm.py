import requests


def test(id):
    data = {"id" : id}
    r = requests.post("http://10.183.235.231:3000/api/post_test",json=data)
    
    return r.content