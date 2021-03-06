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

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='''ffmpeg -i "{}" -pix_fmt yuv420p10le -r 24000/1001 -s 1920x1080 -preset slow -c:v libx265 -crf 21.4 -x265-params deblock=0:-1:no-sao:psy-rd=1.20:psy-rdoq=2.00:aq-mode=3:aq-strength=0.90:frame-threads=4:no-info=1 -map 0:v -c:a libopus -b:a 96k -map 0:a -c:s copy -map 0:s? "{}"''',
    )
    THUMB = config(
        "THUMBNAIL", default="www.google.com" 
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
