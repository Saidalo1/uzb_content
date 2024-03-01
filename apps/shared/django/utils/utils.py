def audio_upload_path(instance, filename):
    language = instance.language.language_code if instance.language else 'unknown'
    return f'audios/{language}/{filename}'
