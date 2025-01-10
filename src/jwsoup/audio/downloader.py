import os
import requests
from loguru import logger

def download_audio(mp3_url, output_dir, chapter_id, page_id):
    """
    Télécharge un fichier audio MP3 à partir de l'URL donnée et le sauvegarde dans un répertoire structuré.
    """
    try:
        output_dir = os.path.join(output_dir, chapter_id)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"page_{page_id}.mp3")
        
        response = requests.get(mp3_url)
        response.raise_for_status()
        
        with open(output_path, "wb") as file:
            file.write(response.content)
        
        logger.info(f"Audio téléchargé avec succès : {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Erreur lors du téléchargement de l'audio : {e}")
        return None

