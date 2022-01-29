#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .
#=/_×÷_
from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()


APP_ID = 3281305
API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
BOT_TOKEN = "5189545644:AAEDeiJaXwmpeGwmIr6CQZXLA0ge6ZTFyLg" 

OWNER = "1666551439"
FFMPEG = "ffmpeg -i '''{}''' -preset fast -c:v libx264 -crf 28 -map 0:v -c:a libopus -ab 32k -s 800x400 -map 0:a -c:s copy -map 0:s? '''{}''' -y"
THUMB = "https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
