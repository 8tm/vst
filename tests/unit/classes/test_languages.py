import pytest

from mts.classes.languages import LanguageToLanguageTag  # type: ignore

languages_tags = [
    ('English', 'en-GB'),
    ('German', 'de-DE'),
    ('Polish', 'pl-PL'),
]
languages_names = (f'Checking {language} language' for language, _ in languages_tags)


@pytest.mark.parametrize('language, tag', languages_tags, ids=languages_names)
def test_language(language: str, tag: str) -> None:
    result = LanguageToLanguageTag(language_name=language)
    assert result.selected_language == language


languages_names = (f'{language} language has "{tag}" tag' for language, tag in languages_tags)


@pytest.mark.parametrize('language, tag', languages_tags, ids=languages_names)
def test_language_tag(language: str, tag: str) -> None:
    language = LanguageToLanguageTag(language_name=language)
    result = str(language)
    assert result == tag


def test_not_existing_language() -> None:
    language = LanguageToLanguageTag(language_name='UFO')
    result = str(language)
    assert result == 'pl-PL'

