'''from pydub import lakshya.mp3
sound=AudioSegment.from_lakshya.mp3("lakshya.mp3")
AudioSegment.converter="ffmpeg.exe"
AudioSegment.ffmpeg="ffmpeg.exe"
AudioSegment.ffprobe="ffprobe.exe"

StartMin=0
StartSec=0

EndMin=0
EndSec=0.5

StartTime=StartMin*60*1000+StartSec*1000
EndTime=EndMin*60*1000+EndSec*1000

extract=sound[StartTime:EndTime]
extract.export("new file.mp3",format="mp3")'''





from pydub import AudioSegment


#importing file from location by giving its path
sound = AudioSegment.from_mp3(file="lakshya.mp3")

#Selecting Portion we want to cut
StrtMin = 0
StrtSec = 8

EndMin = 0
EndSec = 22

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("lakshya1.mp3", format="mp3")

# new file portion.mp3 is saved at required location


