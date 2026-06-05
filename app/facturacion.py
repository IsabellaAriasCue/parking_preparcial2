from math import ceil

TARIFA_HORA = 500
MINUTOS_GRATIS = 30
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20


def calcular_tarifa(minutos, vip=False):

    if minutos <= MINUTOS_GRATIS:
        return 0

    horas = ceil((minutos - MINUTOS_GRATIS) / 60)

    total = horas * TARIFA_HORA

    if vip:
        total *= (1 - DESCUENTO_VIP)

    total = min(total, TOPE_DIARIO)

    return int(total)