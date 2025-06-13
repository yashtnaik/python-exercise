import logging

logging.basicConfig(filename='DebugLogs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(num):
    logging.debug('start of factoral (%s)' % (num))
    total=1
    for i in range (num + 1):
        total *= i
        logging.info('i is %s and total is %s' % (i, total) )
    print(total)
    logging.warning('Total is %s' % total)

factorial(5)

# logging.debug()
# logging.info()
# logging.Warning()
# logging.error()
# logging.critical()