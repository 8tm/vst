# MTS (MekaTron Scripts)



## Instalation

```shell
git clone https://github.com/8tm/mts.git
cd mts
pip install .
```

# Usage

## mts_wav_to_text
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

On Linux:<br>
```
/path/to/folder/
path/to/folder
folder_name
.
```

#### -o / --output
Description: Path to folder where training.txt and validation.txt files will be saved.<br>
Required: Yes<br>

On Linux:
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
Description: Set validation percentage (1-99 percent) to change number of lines which will moved from training file to validation file. 
Required: No
Default: 5%

#### -v / --verbose
Description: Print information for user.<br> 
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

