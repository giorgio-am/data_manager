import logging as log
#revisar documentacion de logger en python
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('procesos.log'),
                    log.StreamHandler()
                ])




if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('mensaje a nivel de info')
    log.warning('mensaje a nivel de warning')
    log.error('mensaje a nivel de error')
    log.critical('mensaje a nivel critico')