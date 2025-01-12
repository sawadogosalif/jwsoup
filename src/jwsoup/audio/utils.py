import urllib
def extract_audio_identifier(url):
    """
    Génère un identifiant unique pour un fichier audio basé sur l'URL.
    """
    parts = url.strip('/').split('/')
    return urllib.parse.unquote(parts[-2]), parts[-1]
