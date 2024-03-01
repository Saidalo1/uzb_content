from re import findall

from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()


@register.filter('custom_title', is_safe=True)
@stringfilter
def custom_title(value):
    """Convert a string into titlecase."""

    def capitalize_word(word_value):
        if word_value.startswith("o'"):
            return word_value[:2].capitalize() + word_value[2:]
        else:
            return word_value.capitalize()

    pattern = r"[\w']+"
    words = findall(pattern, value)

    titled_words = []
    for word in words:
        if "'" in word:
            parts = word.split("'")
            titled_parts = [capitalize_word(part) for part in parts]
            titled_word = "'".join(titled_parts)
            titled_words.append(titled_word)
        else:
            titled_words.append(capitalize_word(word))

    return ' '.join(titled_words)
