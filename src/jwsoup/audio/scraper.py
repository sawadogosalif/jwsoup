from loguru import logger
from jwsoup.audio import download_audio, extract_mp3_link, extract_audio_identifier



def download_audios(start_url, output_dir, max_pages=5):
    """
    Télécharge les fichiers audio sur plusieurs pages, en commençant par une URL donnée.
    """
    current_url = start_url
    i = 0

    while current_url and i < max_pages:
        logger.info(f"Traitement de la page : {current_url}")
        audio_link, next_page_link = extract_mp3_link(current_url)

        if audio_link:
            chapter_id, page_id = extract_audio_identifier(current_url)
            download_audio(audio_link, output_dir, chapter_id, page_id)

        current_url = next_page_link
        i += 1
    
    logger.info(f"Téléchargement terminé. Nombre de pages traitées : {i}")
