import urllib3


def internet_on():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://216.58.192.142', timeout=5.5)
        return True
    except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError):
        return False
