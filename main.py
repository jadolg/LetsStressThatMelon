import datetime
import requests
import logging
from multiprocessing.pool import Pool
from sys import argv

URL = 'http://myurl.com'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def do_get_request(url):
    """
    :param url: the url you want to do a GET request 
    :return: an integer representing the HTTP response code
    """
    starts = datetime.datetime.now()
    try:
        code = requests.get(url).status_code
    except:
        code = -1
    ends = datetime.datetime.now()
    logging.debug('started @ '+str(starts)+' finished @ '+str(ends)+' response code '+str(code))
    return code


def stress_the_melon(processes=10, times=500, url=URL):
    """
    :param processes: ammount of processes running at the same time 
    :param times: how many requests you want to make (sum)
    :param url: the url you want to get
    """
    print('Stress test working with '+str(processes)+' threads and '+str(times)+' requests\nURL: '+URL)
    pool = Pool(processes=int(processes))

    for i in range(0, int(times)):
        result = pool.apply_async(do_get_request, [url, ])
        if result.get() != 200:
            print('OK, the Melon just died :(')

    pool.terminate()


if __name__ == '__main__':
    print('[Lets Stress that Melon!]\nusage: python3 main.py <workers> <requests> <?url>')
    if len(argv) == 3:
        stress_the_melon(argv[1], argv[2])
    elif len(argv) == 4:
        stress_the_melon(argv[1], argv[2], argv[3])
    else:
        print('we need more params')
