import argparse
import tempfile
from pathlib import Path
from typing import Dict, List, Tuple

import speech_recognition as sr  # type: ignore
from pydub import AudioSegment  # type: ignore
from vst.classes.languages import LanguageToLanguageTag  # type: ignore
from vst.classes.shell import Shell  # type: ignore


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '--input', action='store', required=True, type=Path,
        help='Path to folder with WAVs files',
    )
    parser.add_argument(
        '-l', '--language', action='store', required=False, type=str, default='Polish',
        help='Language name. Read README.md file to know all languages',
    )
    parser.add_argument(
        '-o', '--output', action='store', required=True, type=Path,
        help='Path to the folder where training and validation files will be saved',
    )
    parser.add_argument(
        '-p', '--percent', action='store', required=False, type=int, default=5,
        help='Path to folder with WAVs files',
    )
    parser.add_argument(
        '-r', '--recursive', action='store_true', required=False,
        help='Find files also in subdirectories of input path',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', required=False,
        help='Show information while the script is running',
    )
    return parser.parse_args()


def split_files_for_training_and_validation(files: List[Path], percent: int) -> Tuple[List[Path], List[Path]]:
    list_of_files = list(files)
    number_of_files = int((len(list_of_files) / 100) * percent + 0.5)
    number_of_validation_files = number_of_files if number_of_files > 2 else 2
    return list_of_files[number_of_validation_files:len(list_of_files)], list_of_files[:number_of_validation_files]


def get_text_from_wav_file(path: Path, language: str) -> str:
    r = sr.Recognizer()
    language_tag = str(LanguageToLanguageTag(language))
    silence = AudioSegment.silent(duration=1000)
    wav_content = AudioSegment.from_wav(path)
    new_content = silence + wav_content + silence
    path_to_temporary_file = Path(tempfile.gettempdir()) / 'temporary_wav_file.wav'
    new_content.export(path_to_temporary_file, format='wav')

    with sr.AudioFile(str(path_to_temporary_file)) as file:
        audio = r.record(file)
        try:
            text = r.recognize_google(audio, language=language_tag)
        except sr.UnknownValueError:
            text = f"<< Text wasn't recognized! Are you sure that the language used in the wav file is {language} ? >>"

    path_to_temporary_file.unlink()
    return text


def get_dialogs_from_files(paths: List[Path], language: str, verbose: bool = False) -> Dict[Path, str]:
    dialogs = {}
    for index, path in enumerate(paths, start=1):
        text = get_text_from_wav_file(Path(path), language)
        if verbose:
            print(f'{index:5}: {Path(path).name:50} {text}')
        dialogs[Path(path)] = text
    return dialogs


def convert_dialogs_to_file_content(dialogs: Dict[Path, str]) -> str:
    content = ''
    for dialog in dialogs:
        content += f'{dialog}|{dialogs[dialog]}.\n'
    return content


def save_content_to_file(path: Path, content: str) -> None:
    with open(path, 'w', encoding='utf8') as file:
        file.write(content)


def wav_to_text() -> None:
    arguments = parse_arguments()
    if arguments.percent < 1 or arguments.percent > 99:
        print('The value of param "percent" should be between 1 and 99 percent')
        exit(1)

    shell = Shell()
    wav_files_paths = shell.get_files_by_extensions(arguments.input, ['wav'], arguments.recursive)
    training_files, validation_files = split_files_for_training_and_validation(wav_files_paths, arguments.percent)

    operations = {
        'training': training_files,
        'validation': validation_files,
    }

    if arguments.verbose:
        message = f'''
        \r    Number of wav files: {len(training_files) + len(validation_files)}
        \r         Training files: {len(training_files)}
        \r       Validation files: {len(validation_files)}
        \r         Using language: {LanguageToLanguageTag(arguments.language).selected_language}
        \r              Recursive: {'Yes' if arguments.recursive else 'No'}'''
        print(message)

    for operation in operations:
        files = operations[operation]
        if arguments.verbose:
            print(f'\n => Converting {operation} files ({len(files)} files)')
        dialogs = get_dialogs_from_files(files, arguments.language, arguments.verbose)
        file_content = convert_dialogs_to_file_content(dialogs)
        save_content_to_file(Path(arguments.output) / f'{operation}.txt', file_content)


def main() -> None:
    try:
        wav_to_text()
    except KeyboardInterrupt:
        print(' <= Application terminated by the user\n')
        exit(0)


if __name__ == '__main__':
    main()