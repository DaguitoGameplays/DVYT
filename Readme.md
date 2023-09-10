# Uso de la clase DVYT (Descargar Video de YouTube)


## Paso 1: Importar la clase DVYT

from dvyt import DVYT


## Paso 2: Crear una instancia de la clase DVYT

dvyt = DVYT(path='ruta_personalizada')

## Paso 3: Obtener los formatos disponibles para un video

Podemos utilizar el método get_formats para obtener los formatos disponibles. Este método recibe una URL de un video de YouTube como parámetro y devuelve una lista de formatos.

url = 'https://www.youtube.com/watch?v=video_id'

formatos = dvyt.get_formats(url)


## Paso 4: Descargar un video en un formato específico

Una vez que tengamos la lista de formatos disponibles, podemos utilizar el método download para descargar el video en un formato específico. Este método recibe la URL del video, el ID del formato deseado y dos parámetros opcionales: 'progress' y 'args'.

url = 'https://www.youtube.com/watch?v=video_id'

format_id = 'formato_id'

dvyt.download(url, format_id)


El parámetro format_id debe ser una cadena que contenga el ID del formato que deseamos descargar. Podemos obtener este ID de la lista de formatos disponibles obtenida en el paso anterior.

## Paso 5: Especificar una función de progreso durante la descarga

Si deseamos mostrar el progreso de la descarga del video, podemos proporcionar una función de progreso como parámetro opcional en el método download. Esta función se llamará durante el proceso de descarga y nos permitirá mostrar información de progreso al usuario.

def mostrar_progreso(d):

    print(f"Progreso: {d['downloaded_bytes'] / d['total_bytes'] * 100:.2f}%")

url = 'https://www.youtube.com/watch?v=video_id'

format_id = 'formato_id'

dvyt.download(url, format_id, progress=mostrar_progreso)

## Paso 6: Guardar el video en una ubicación personalizada

Si deseamos guardar el video descargado en una ubicación personalizada, podemos proporcionar una ruta como parámetro opcional en el constructor de la clase DVYT. El video se guardará en esta ruta especificada.

dvyt = DVYT(path='ruta_personalizada')

En el ejemplo anterior, debemos reemplazar 'ruta_personalizada' por la ruta real donde deseamos guardar los videos descargados.