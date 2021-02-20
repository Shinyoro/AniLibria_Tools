# AniLibria.TV Tools
Набор скриптов написанные на языке Python 3, которые предназначены для работы над таймингом релиза и обработки видео по стандартам AniLibria.TV.
Некоторые из них требуют дополнительные программы для полной работы.

## Требования
  * [Python 3.X](https://www.python.org/downloads/)

### Дополнительные программы
  * [FFmpeg](https://ffmpeg.org/download.html)
  
## Готовый архив с исполняемыми файлами
  * [Windows](https://github.com/Shinyoro/AniLibria_Tools/releases/download/v1.0/anilibria-tools-windows.zip)
  * [GNU/Linux](https://github.com/Shinyoro/AniLibria_Tools/releases/download/v1.0/anilibria-tools-gnu-linux.tar.gz)
  
## Использование

### Способы использование скриптов
Есть несколько способов использовать скрипты по вашему удобству:

  * Использовать командную строку Windows или терминал GNU/Linux для прямого
  вызова скрипта, который находится в определенной директории с помощью команды `python` (`python3` на GNU/Linux)
  * Добавить скрипт/исполняемый файл в переменное окружение PATH, чтобы использовать его в любом месте.
  
### anilibria-mkvmerge.py
Скрипт для сборки mkv файла. Работает из командной строки Windows или из терминала GNU\Linux. Требуется установленная утилита FFmpeg.

Принимающие аргументы:

  * `-o`, `--original-video` - путь к оригинальному видео файлу.
  * `-v`, `--voiceover` - путь к файлу готовой русской озвучки.
  * `-c`, `--captions` - путь к файлу с надписями.
  * `-s`, `--subtitles` - путь к файлу с субтитрами.
  * `-f`, `--fonts` - путь к директории со шрифтами (необязательно).
  * `-ff`, `--ffmpeg` - путь к утилите FFmpeg (необязательно, если утилита прописана в переменное окружение PATH).
  * `release_name` - название релиза.
  * `serial_number` - номер серии.
  * `quality` - качество.
  * `resolution` - разрешение.
  
Запустится утилита FFmpeg, которая соберет готовый mkv файл с правильной расстановкой потоков,
с метаданными и с названием файла по стандартам AniLibria.TV.

#### Пример:
Windows:

`python anilibria-mkvmerge.py -o original_release.mp4 -v D:\russian_voice_anilibria.m4a -c sub\captions.ass -s subtitles.ass -f fonts\ 'Name of anime' 07 WEBRip 720p`

`anilibria-mkvmerge.exe -o original_release.mp4 -v D:\russian_voice_anilibria.m4a -c sub\captions.ass -s subtitles.ass -f fonts\ 'Name of anime' 07 WEBRip 720p`
    
GNU/Linux:

`python3 anilibria-mkvmerge.py -o original_release.mp4 -v ~/russian_voice_anilibria.m4a -c sub/captions.ass -s subtitles.ass -f fonts/ 'Name of anime' 07 WEBRip 720p`

`anilibria-mkvmerge -o original_release.mp4 -v ~/russian_voice_anilibria.m4a -c sub/captions.ass -s subtitles.ass -f fonts/ 'Name of anime' 07 WEBRip 720p`


  
