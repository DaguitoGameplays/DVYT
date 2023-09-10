import yt_dlp
import os

class DVYT(object):
    def __init__(self,path=''):
        self.url = ''
        self.progress = ''
        self.args = ''
        self.path = path
        
        if self.path != '':
            isExist = os.path.exists(self.path)
            if not isExist:
                os.makedirs(self.path)
        
    def get_formats(self,url):
        ydl = yt_dlp.YoutubeDL({})
        info = ydl.extract_info(url, download=False)
        formats = info["formats"]
        for format in formats:
            print(format["format_id"], format["ext"], format["resolution"])
        return formats
        
    def download(self,url, format_id, progress=None, args=None):
        ydl_opts = {
        'format': format_id,
        'outtmpl': self.path + '%(title)s.%(ext)s', 
        }
        if progress:
            ydl_opts = {
            'format': format_id,
            'outtmpl': self.path + '%(title)s.%(ext)s', 
            'progress_hooks': [lambda d: progress(d, args)],
            }
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        ydl.download([url])