#!/usr/bin/env python3

# Модули / Modules
from subprocess import call
from os import listdir
from sys import platform

# Сборка mkv. Требуется консольная утилита mkvmerge из набора инструментов mkvtoolnix. 
# Build mkv. Requires the mkvmerge console utility from the mkvtoolnix toolbox.

# Аргументы: / Arguments:
# original - оригинальный файл / original file.
# voiceover - русская озвучка / russian voiceover.
# captions - надписи.
# subtitles - субтитры.
# release_name - название релиза.
# serial_number - номер серии.
# quality - качество.
# resolution - разрешение.
# dir_fonts - папка со шрифтами (необязательно) / (optional).
# original_raw - название оригинального Raw для метаданных (необязательно) / Original name Raw for metadata (optional).
# mkvmerge - путь к утилите mkvmerge (необязательно) / mkvmerge utility path (optional).
def mkvmerge(original,
             voiceover,
             captions,
             subtitles,
             release_name,
             serial_number,
             quality,
             resolution,
             dir_fonts=None,
             original_raw=None,
             mkvmerge=None):
    
    # Сборка команды для mkvmerge / Build command for mkvmerge.
    # Позиция потоков и метаданные сделаны по стандартам AniLibria.TV / Placements and metadata are made according to AniLibria.TV standards.
    
    # Проверка, указан ли путь к утилите mkvmerge / Checking if the path to mkvmerge is specified.
    if not mkvmerge:
        command = ['mkvmerge']
    else:
        command = [mkvmerge]
    
    # Проверка, указано ли название оригинального Raw / Checking if the name of the original Raw is specified.
    if not original_raw:
        original_raw = 'Original'
    else:
        original_raw = 'Original [' + original_raw + ']'
    
    command += [
               
               # Входные файлы / Input files.
               
               # Метаданные по стандартам AniLibria.TV. <метаданные> <поток исходного файла>:<значение>.
               # Metadata according to AniLibria.TV standards. <metadata> <source file stream>: <value>.
               # --default-track - поток воспроизводимый по умолчанию.
               # --forced-track - принудительно воспроизводить поток.
               # --language - язык.
               # --track-name - заголовок потока / Stream title.
               '--default-track', '0:yes',
               '--forced-track',  '0:yes',
               '--language',      '0:jpn',
               '--language',      '1:jpn',
               '--track-name',    '0:' + original_raw,
               '--track-name',    '1:' + original_raw,
               original,
               
               '--default-track', '0:yes',
               '--forced-track',  '0:yes',
               '--language',      '0:rus',
               '--track-name',    '0:AniLibria.TV',
               voiceover,
               
               '--default-track', '0:yes',
               '--forced-track',  '0:yes',
               '--language',      '0:rus',
               '--track-name',    '0:Надписи [AniLibria.TV]',
               captions,
               
               '--language',      '0:rus',
               '--track-name',    '0:Полные [AniLibria.TV]',
               subtitles,
               
               # Позиции потоков / Positions of streams.
               # --track-order <номер исходного файла>:<номер потока>,... / --track-order <source file number>:<stream number>, ...
               '--track-order', '0:0,1:0,0:1,2:0,3:0']
    
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
            command += ['--attachment-mime-type', 'application/x-truetype-font',
                        '--attach-file', dir_fonts+font,]
    
    # Завершающий этап сборки команды / The final stage of command building.
    # Название готового mkv файла будет назван по стандартам AniLibria.TV.
    # The name of the finished mkv file will be named according to AniLibria.TV standards.
    command += ['-o',
                
                release_name.replace(' ', '_') +
                '_[' +
                serial_number +
                ']_[AniLibria_TV]_[' +
                quality + '_' + resolution +
                '].mkv']
    
    # Запуск утилиты из собранной команды / Running the utility from the assembled command.
    # Возвращает статус код процесса / Returns the status code of the process.
    return call(command)

# Если был запущен скрипт / If the script was run.
if __name__ == '__main__':
    
    # Импорт модулей и обработка входных аргументов / Importing Modules and Handling Input Arguments.
    # Для получения справки, необходимо задать аргумент -h или --help / To get help, you need to set the argument -h or --help.
    # Необязательные аргументы помечены квадратными скобками / Optional arguments are marked with square brackets.
    from argparse import ArgumentParser
    from locale import getdefaultlocale
    
    # Локализация.
    lang = getdefaultlocale()[0][:2]
    
    localization = { 'ru' : {
        
                        'help' : {
                            'original_video' : 'Путь к оригинальному видеофайлу.',
                            'original_raw'   : 'Название оригинального Raw для метаданных.',
                            'voiceover'      : 'Путь к файлу с озвучкой.',
                            'captions'       : 'Путь к файлу с надписями.',
                            'subtitles'      : 'Путь к файлу с субтитрами.',
                            'fonts'          : 'Путь к директории со шрифтами (необязательно).',
                            'mkvmerge'       : 'Путь к утилите mkvmerge (необязательно, если утилита прописана в переменное окружение PATH).',
                            'release_name'   : 'Название релиза.',
                            'serial_number'  : 'Номер серии.',
                            'quality'        : 'Качество видеофайла.',
                            'resolution'     : 'Разрешение видеофайла.' },
                        
                        'interrupt' : 'Прервано пользователем!' },
                     
                     'en' : {
                         
                        'help' : {
                            'original_video' : 'Path to a original videofile.',
                            'original_raw'   : 'Original Raw name for metadata.',
                            'voiceover'      : 'Path to a file of voice acting.',
                            'captions'       : 'Path to a file with captions.',
                            'subtitles'      : 'Path to a file with subtitles.',
                            'fonts'          : 'Path to a directory with fonts (Optional).',
                            'mkvmerge'       : 'mkvmerge utility path (Optional, if the utility is registered in the PATH environment variable).',
                            'release_name'   : 'Release name.',
                            'serial_number'  : 'Serial number.',
                            'quality'        : 'Quality of videofile.',
                            'resolution'     : 'Resolution of videofile.' },
                         
                        'interrupt' : 'Interrupted by user!' }
                    }

    arguments_parser = ArgumentParser()

    arguments_parser.add_argument('-o', '--original-video', type=str, required=True, help=localization[lang]['help']['original_video'])
    arguments_parser.add_argument('-r', '--original-raw', type=str, default=None, help=localization[lang]['help']['original_raw'])
    arguments_parser.add_argument('-v', '--voiceover', type=str, required=True, help=localization[lang]['help']['voiceover'])
    arguments_parser.add_argument('-c', '--captions', type=str, required=True, help=localization[lang]['help']['captions'])
    arguments_parser.add_argument('-s', '--subtitles', type=str, required=True, help=localization[lang]['help']['subtitles'])
    arguments_parser.add_argument('-f', '--fonts', type=str, default=None, help=localization[lang]['help']['fonts'])
    arguments_parser.add_argument('-m', '--mkvmerge', type=str, default=None, help=localization[lang]['help']['mkvmerge'])
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
            argv.original_raw,
            argv.mkvmerge]
        
    if platform == 'win32':
        for idx, arg in enumerate(argv):
            if arg:
                argv[idx] = arg.replace('\\', '\\\\')
    
    try:
       mkvmerge(*argv)
    except KeyboardInterrupt:
        print('\n' + localization[lang]['interrupt'])
