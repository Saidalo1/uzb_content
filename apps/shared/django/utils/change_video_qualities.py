from os import makedirs
from os.path import exists, dirname

from django.utils.translation import gettext_lazy as _
from ffmpeg import input

from root.celery import app
from root.settings import BASE_DIR, MEDIA_URL, qualities


@app.task(bind=True, name=_('Split and sort video files into different qualities'))
def transcode_video(self, object_pk):
    self.update_state(state='RUNNING')
    from apps.content.models import Products
    video = Products.objects.get(pk=object_pk)
    input_file_path = video.video_original.path
    if not exists(input_file_path):
        return f"The video file for object '{video.title}' does not exist!"

    video_qualities = {}
    video_name = video.video_original.name

    for quality, resolution in qualities.items():
        file_path = f"videos/{quality}/{video_name[7:]}"
        output_file_path = f"{BASE_DIR}/{MEDIA_URL}{file_path}"
        output_directory = dirname(output_file_path)
        if not exists(output_directory):
            makedirs(output_directory)
        if not exists(output_file_path):
            input(input_file_path).output(output_file_path,
                                          vf=f'scale={resolution["width"]}:{resolution["height"]}').run()

            setattr(video, f'video_{quality}', output_file_path)
        video_qualities[quality] = file_path
    Products.objects.filter(pk=video.pk).update(video_original=video.video_original, video_1080=video_qualities['1080p'], video_720=video_qualities['720p'],
                                                video_480=video_qualities['480p'])
    return f"The video file '{video_name}' has been successfully divided and sorted by different quality!"
