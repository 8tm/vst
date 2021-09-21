# MTS (MekaTron Scripts)

## Instalation

```shell
git clone https://github.com/8tm/mts.git
cd mts
pip install .
```

# Usage
**Those scripts hasn't been tested on the following operating systems: Windows, MacOS !!!**

## Script: mts_audio_to_wav
This script was created to convert audio files to WAV format (mono, 22050 Hz).

The script searches for files with the following extensions and converts them to wav format:
 - .aac
 - .ac3
 - .aiff
 - .ape
 - .flac
 - .m4a
 - .mp2
 - .mp3
 - .mp4
 - .ogg
 - .ogx
 - .opus
 - .ts
 - .wav
 - .wma
 - .wv 

### Help
```shell
mts_audio_to_wav -h
mts_audio_to_wav --help
```

### mts_audio_to_wav usage
```shell
mts_audio_to_wav -i input_folder_path -o output_folder_path -v -r -t
mts_audio_to_wav -i wav/ -o . -r
mts_audio_to_wav -i . -o ../output -t
```

### Params:
### Params:
#### -i / --input
Description: Path to folder with audio files.<br>
Required: Yes<br>

```
/path/to/folder/
path/to/folder
folder_name
.
```

#### -o / --output
Description: Path to folder where wav files will be saved.<br>
Required: Yes<br>

```
/path/to/folder/
path/to/folder
folder_name
.
```

#### -r / --recursive
Description: Find files also in subdirectories of input path<br>
Required: No<br>
Default: off<br>

#### -t / --truncate
Description: Truncate the silence<br>
Required: No<br>
Default: off<br>

#### -v / --verbose
Description: Show information while the script is running.<br> 
Required: No<br>
Default: off<br>


## Script: mts_wav_to_text
This script is designed to create training and validation files from words spoken in WAV files.<br>
For many reasons, it is not able to read the words perfectly.<br>
Sometimes it will lose or misspell some words.<br>
In most of cases it relieves the user in tedious work.<br>
It is required to check and correct the files again.<br>

### Help
```shell
mts_wav_to_text -h
mts_wav_to_text --help
```

### mts_wav_to_text usage
```shell
mts_wav_to_text -i input_folder_path -o output_folder_path --language Polish -v -p 13
mts_wav_to_text -i wav/ -o . --language English -p 15
mts_wav_to_text -i . -o ../
```

### Params:
#### -i / --input
Description: Path to folder with wav files.<br>
Required: Yes<br>

```
/path/to/folder/
path/to/folder
folder_name
.
```

#### -o / --output
Description: Path to folder where training.txt and validation.txt files will be saved.<br>
Required: Yes<br>

```
/path/to/folder/
path/to/folder
folder_name
.
```

#### -r / --recursive
Description: Find files also in subdirectories of input path<br>
Required: No<br>
Default: off<br>

#### -l / --language
Description: Language name.<br>
Required: No<br>
default: Polish<br>

Currently supported languages:
- Polish
- English
- German

#### -p / --percent
Description: Set validation percentage (1-99 percent) to change number of lines which will moved from training file to validation file.<br> 
Required: No<br>
Default: 5%<br>

#### -v / --verbose
Description: Show information while the script is running.<br> 
Required: No<br>
Default: off<br>



### Training/Validation file content
Used input path will be used as a path in created file.
So when you use `-i wav/` it will create content like this:

```
wav/bchlml_beachvi_d_S_POL.27.wav|dalej ruszaj.
wav/bchlml_beachvi_d_S_POL.29.wav|Dlaczego nadajnika nieaktywowany wcześniej.
(...)
```

When you use `-i .` it will create content like this:
```
bchlml_beachvi_d_S_POL.27.wav|dalej ruszaj.
bchlml_beachvi_d_S_POL.29.wav|Dlaczego nadajnika nieaktywowany wcześniej.
(...)
```

When you use `-i /path/to/folder/with/wav/files/` it will create content like this:
```
/path/to/folder/with/wav/files/bchlml_beachvi_d_S_POL.27.wav|dalej ruszaj.
/path/to/folder/with/wav/files/bchlml_beachvi_d_S_POL.29.wav|Dlaczego nadajnika nieaktywowany wcześniej.
(...)
```

