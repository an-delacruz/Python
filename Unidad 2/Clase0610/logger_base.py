import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s:%(levelname)s [%(filename)s]: %(lineno)s %(message)s",
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('./Unidad 2/Clase0610/capa_datos.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug("Mensaje Debug")