from threading import Thread
import requests


class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/' + 1)]
        resp = requests.get(self.url)
        with open('~/' + filename, 'wb') as f:
            f.write(resp.content)


class GetHttp(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        print(resp.content)


def main():
    qqnum = '1342009839'
    url = 'https://api.muxiaoguo.cn/api/QqInfo?qq=' + qqnum
    resp = GetHttp(url).start()


if __name__ == '__main__':
    main()
