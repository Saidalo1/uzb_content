from os import makedirs
from os.path import exists, dirname

from ffmpeg import input

from root.settings import BASE_DIR, MEDIA_URL, qualities


def transcode_video(object_pk):
    from apps.content.models import Video
    video = Video.objects.get(pk=object_pk)
    input_file_path = video.video_original.path
    video_qualities = {}

    for quality, resolution in qualities.items():
        file_path = f"videos/{quality}/{video.video_original.name[7:]}"
        output_file_path = f"{BASE_DIR}/{MEDIA_URL}{file_path}"
        output_directory = dirname(output_file_path)
        if not exists(output_directory):
            makedirs(output_directory)
        print(file_path, output_file_path)
        if not exists(output_file_path):
            input(input_file_path).output(output_file_path,
                                          vf=f'scale={resolution["width"]}:{resolution["height"]}').run()

            setattr(video, f'video_{quality}', output_file_path)
        video_qualities[quality] = file_path
    Video.objects.filter(pk=video.pk).update(video_1080=video_qualities['1080p'], video_720=video_qualities['720p'],
                                             video_480=video_qualities['480p'])
