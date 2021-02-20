#!/usr/bin/env python3

# Модули / Modules
from subprocess import call
from os import listdir
from sys import platform

# Сборка mkv. Требуется утилита FFmpeg / Build mkv. Requires utility FFmpeg.
# Аргументы: / Arguments:
# original - оригинальный файл / original file.
# voiceover - русская озвучка / russian voiceover.
# captions - надписи.
# subtitles - субтитры.
# release_name - название релиза.
# serial_number - номер серии.
# quality - качество.
# resolution - разрешение.
# dir_fonts - папка со шрифтами.
# ffmpeg - путь к утилите FFmpeg / FFmpeg utility path
def mkvmerge(original,
             voiceover,
             captions,
             subtitles,
             release_name,
             serial_number,
             quality,
             resolution,
             dir_fonts=None,
             ffmpeg=None):
    
    # Сборка команды для FFmpeg / Build command for FFmpeg.
    # Позиция потоков и метаданные сделаны по стандартам AniLibria.TV / Placements and metadata are made according to AniLibria.TV standards.
    
    # Проверка, указан ли путь к утилите FFmpeg / Checking if the path to FFmpeg is specified.
    if not ffmpeg:
        command = ['ffmpeg']
    else:
        command = [ffmpeg]
    
    command += [
               
               # Входные файлы / Input files
               '-i', original,
               '-i', voiceover,
               '-i', captions,
               '-i', subtitles,
               
               # Позиции потоков. 0(номер файла):0(номер потока файла) / Positions of streams. 0(file number):0(file stream number).
               '-map', '0:0',
               '-map', '1',
               '-map', '0:1',
               '-map', '2',
               '-map', '3',
               
               # Метаданные по стандартам AniLibria.TV. s:0(номер потока выходного файла).
               # Metadata according to AniLibria.TV standards. s:0(stream number of the output file).
               # language - язык потока.
               # title - название потока.
               '-metadata:s:0', 'language=jpn',
               '-metadata:s:0', 'title=' + release_name + ' - ' + serial_number,
               '-metadata:s:1', 'language=rus',
               '-metadata:s:1', 'title=AniLibria.TV',
               '-metadata:s:2', 'language=jpn',
               '-metadata:s:2', 'title=Оригинал',
               '-metadata:s:3', 'language=rus',
               '-metadata:s:3', 'title=Надписи',
               '-metadata:s:4', 'language=rus',
               '-metadata:s:4', 'title=Субтитры',
               
               # Потоки воспроизводимые по умолчанию / Streams playable by default.
               '-disposition:s:0', 'default',
               '-disposition:s:1', 'default',
               '-disposition:s:3', 'default']
    
    # Проверка наличия шрифтов и подключение их, если они есть / Checking for Fonts and connect them, if any.
    if dir_fonts:
        
        if platform == 'win32':
            if dir_fonts[-1] != '\\':
                dir_fonts += '\\'
        else:
            if dir_fonts[-1] != '/':
                dir_fonts += '/'
                
        fonts = listdir(dir_fonts)
        
        for font in fonts:
            command += ['-attach',
                        dir_fonts+font,
                        '-metadata:s:t:' + str(fonts.index(font)),
                        'mimetype=application/x-truetype-font']
    
    # Завершающий этап сборки команды / The final stage of command building.
    # Название готового mkv файла будет назван по стандартам AniLibria.TV.
    # The name of the finished mkv file will be named according to AniLibria.TV standards.
    command += ['-c', 'copy',
                
                release_name.replace(' ', '_') +
                '_[' +
                serial_number +
                ']_[AniLibria_TV]_[' +
                quality + '_' + resolution +
                '].mkv']
    
    # Запуск утилиты из собранной команды / Running the utility from the assembled command.
    # Возвращает статус код процесса / Returns the status code of the process.
    return call(command)

# Если был запущен скрипт / If the script was run
if __name__ == '__main__':
    
    # Импорт модулей и обработка входных аргументов / Importing Modules and Handling Input Arguments.
    # Для получения справки, необходимо задать аргумент -h или --help / To get help, you need to set the argument -h or --help.
    # Необязательные аргументы помечены квадратными скобками / Optional arguments are marked with square brackets.
    from argparse import ArgumentParser
    from locale import getdefaultlocale
    
    # Локализация
    lang = getdefaultlocale()[0][:2]
    
    localization = { 'ru' : {
        
                        'help' : {
                            'original_video' : 'Путь к оригинальному видео файлу',
                            'voiceover'      : 'Путь к файлу с озвучкой',
                            'captions'       : 'Путь к файлу с надписями',
                            'subtitles'      : 'Путь к файлу с субтитрами',
                            'fonts'          : 'Путь к директории со шрифтами (необязательно)',
                            'ffmpeg'         : 'Путь к утилите FFmpeg (необязательно, если утилита прописана в переменное окружение PATH)',
                            'release_name'   : 'Название релиза',
                            'serial_number'  : 'Номер серии',
                            'quality'        : 'Качество видео файла',
                            'resolution'     : 'Разрешение видео файла' },
                        
                        'interrupt' : 'Прервано пользователем!' },
                     
                     'en' : {
                         
                        'help' : {
                            'original_video' : 'Path to a original video file',
                            'voiceover'      : 'Path to a file of voice acting',
                            'captions'       : 'Path to a file with captions',
                            'subtitles'      : 'Path to a file with subtitles',
                            'fonts'          : 'Path to a directory with fonts (Optional)',
                            'ffmpeg'         : 'FFmpeg utility path (Optional, if the utility is registered in the PATH environment variable)'
                            'release_name'   : 'Release name',
                            'serial_number'  : 'Serial number',
                            'quality'        : 'Quality of video file',
                            'resolution'     : 'Resolution of video file' },
                         
                        'interrupt' : 'Interrupted by user!' }
                    }

    arguments_parser = ArgumentParser()

    arguments_parser.add_argument('-o', '--original-video', type=str, required=True, help=localization[lang]['help']['original_video'])
    arguments_parser.add_argument('-v', '--voiceover', type=str, required=True, help=localization[lang]['help']['voiceover'])
    arguments_parser.add_argument('-c', '--captions', type=str, required=True, help=localization[lang]['help']['captions'])
    arguments_parser.add_argument('-s', '--subtitles', type=str, required=True, help=localization[lang]['help']['subtitles'])
    arguments_parser.add_argument('-f', '--fonts', type=str, default=None, help=localization[lang]['help']['fonts'])
    arguments_parser.add_argument('-ff', '--ffmpeg', type=str, default=None, help=localization[lang]['help']['ffmpeg'])
    arguments_parser.add_argument('release_name', type=str, help=localization[lang]['help']['release_name'])
    arguments_parser.add_argument('serial_number', type=str, help=localization[lang]['help']['serial_number'])
    arguments_parser.add_argument('quality', type=str, help=localization[lang]['help']['quality'])
    arguments_parser.add_argument('resolution', type=str, help=localization[lang]['help']['resolution'])

    argv = arguments_parser.parse_args()
    
    argv = [argv.original_video,
            argv.voiceover,
            argv.captions,
            argv.subtitles,
            argv.release_name,
            argv.serial_number,
            argv.quality,
            argv.resolution,
            argv.fonts,
            argv.ffmpeg]
        
    if platform == 'win32':
        for arg in argv:
            if arg:
                argv[argv.index(arg)] = arg.replace('\\', '\\\\')
    
    try:
       mkvmerge(*argv)
    except KeyboardInterrupt:
        print('\n' + localization[lang]['interrupt'])
