import requests
from multiprocessing.pool import Pool
from sys import argv

URL = 'http://alx.aleph:3000'
# URL = 'https://wmeloni-uat.herokuapp.com'


def do_get_request(url):
    return requests.get(url).status_code


def stress_the_melon(processes=10, times=500):
    print('Stress test working with '+str(processes)+' threads and '+str(times)+' requests\nURL: '+URL)
    pool = Pool(processes=int(processes))

    for i in range(0, int(times)):
        result = pool.apply_async(do_get_request, [URL, ])
        print(result.get())

    pool.terminate()


if __name__ == '__main__':
    print('Lets Stress that Melon!\nusage: python3 main.py <workers> <requests>')
    if len(argv) == 3:
        stress_the_melon(argv[1], argv[2])
    else:
        print('we need more params')
