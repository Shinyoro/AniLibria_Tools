# AniLibria.TV Tools
Набор скриптов написанные на языке Python 3, которые предназначены для работы над таймингом релиза и обработки видео по стандартам AniLibria.TV.
Некоторые из них требуют дополнительные программы для полной работы.

## Требования
  * [Python 3.X](https://www.python.org/downloads/)

### Дополнительные программы
  * [FFmpeg](https://ffmpeg.org/download.html)

  Утилита должна быть заранее прописана в переменное окружение PATH.
  
## Использование

### Способы использование скриптов
Есть несколько способов использовать скрипты по вашему удобству:

  * Использовать командную строку Windows или терминал GNU/Linux для прямого
  вызова скрипта, который находится в определенной директории с помощью команды `python` (`python3` на GNU/Linux)
  * Добавить скрипт в переменное окружение PATH, чтобы использовать его в любом месте.
  
### anilibria-mkvmerge.py
Скрипт для сборки mkv файла. Требуется установленная утилита FFmpeg.
Принимающие аргументы:

  * `-o` - путь к оригинальному видео файлу.
  * `-v` - путь к файлу готовой русской озвучки.
  * `-c` - путь к файлу с надписями.
  * `-s` - путь к файлу с субтитрами.
  * `-f` - путь к директории со шрифтами (опционально).
  * `release_name` - название релиза
  * `serial_number` - номер серии
  * `quality` - качество
  * `resolution` - разрешение
  
Запустится утилита FFmpeg, которая соберет готовый mkv файл с правильной расстановкой потоков,
с метаданными и с названием файла по стандартам AniLibria.TV.

#### Пример:
Windows:

`python anilibria-mkvmerge.py -o original_release.mp4 -v D:\russian_voice_anilibria.m4a -c sub\captions.ass -s subtitles.ass -f fonts\ 'Name of anime' 07 WEBRip 720p`
    
GNU/Linux:

`python3 anilibria-mkvmerge.py -o original_release.mp4 -v ~/russian_voice_anilibria.m4a -c sub/captions.ass -s subtitles.ass -f fonts/ 'Name of anime' 07 WEBRip 720p`


  
