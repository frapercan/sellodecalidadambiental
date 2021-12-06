import requests

def extraer_datos(paises,mediciones):

    print('-----------------------------------------------------------------------')

    # Set download url
    url_servicio = "http://discomap.eea.europa.eu/map/fme/latest"

    # Countries to download
    # Note: List is not complete


    # Pollutant to be downloaded

    for pais in paises:
        for medicion in mediciones:
            nombre_fichero = "%s_%s.csv" % (pais, medicion)
            descarga_fichero = '%s/%s_%s.csv' % (url_servicio, pais, medicion)
            # Download and save to local path
            print('Downloading: %s' % descarga_fichero)
            file = requests.get(descarga_fichero).content
            output = open(nombre_fichero, 'wb')
            output.write(file)
            output.close()
            print('Saved locally as: %s ' % nombre_fichero)
            print('-----')
        print('Download finished')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extraer_datos()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
