#Uso

```
from dvyt import DVYT

def progress(d,args):
    hola = args[0]
    adios = args[1]
    print(f"Progreso: {d['downloaded_bytes'] / d['total_bytes'] * 100:.2f}%")
    

url = "https://youtu.be/uzqvqugF1LA?si=fhI5qffv0GHhRZ0g"

dl = DVYT(path='')
formatos = dl.get_formats(url)
for format in formatos:
    print(format)

format = input("id ")

dl.download(url,format,progress=progress,args=("Hola","Adios"))
```