import requests


def extraer_datos(paises, mediciones):
    print('-----------------------------------------------------------------------')

    url_servicio = "http://discomap.eea.europa.eu/map/fme/latest"

    for pais in paises:
        for medicion in mediciones:
            nombre_fichero = "%s_%s.csv" % (pais, medicion)
            descarga_fichero = '%s/%s_%s.csv' % (url_servicio, pais, medicion)

            print('Descargando: %s' % descarga_fichero)
            file = requests.get(descarga_fichero).content
            output = open(nombre_fichero, 'wb')
            output.write(file)
            output.close()
            print('Guardado localmente como: %s ' % nombre_fichero)
            print('-----')
        print('Descarga finalizada')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paises = ['ES']
    mediciones = ['C6H6', 'PM10', 'CO', 'NO2', 'SO2', 'O3', 'PM2.5']
    extraer_datos(paises, mediciones)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
