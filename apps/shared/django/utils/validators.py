import filetype
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _


@deconstructible
class AudioValidator:
    def __call__(self, value):
        """
        :param value: Here is the **value** of the same file that we receive and we want to perform the validation
        operation
        """
        # get audio file
        file = value.file
        # get audio file temporary path saved django
        try:
            file_path = TemporaryUploadedFile.temporary_file_path(file)
        except AttributeError:
            raise ValidationError(_("Invalid format of audiofile. Please, upload a valid audio file!"))
        # We check the file type is audio type
        is_audio = filetype.is_audio(file_path)
        # We check the extension file is audio
        # file_extension = filetype.guess_extension(file_path)
        # get the file type use filetype library
        # file_type = filetype.guess(file_path)

        # check if file is audio
        if is_audio:
            pass
        else:
            raise ValidationError(
                f"please upload a valid audio file, your file: {file.name}"
            )
