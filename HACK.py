import piexif
from PIL import Image
from datetime import datetime


import os

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

for name in onlyfiles :
	if(name[len(name) - 4 : len(name)] == '.JPG' or name[len(name) - 4 : len(name)] == '.jpg' ):
		year = int(name[0:4]);
		month = int(name[4:6]);
		day = int(name[6:8]);
		hour = int(name[9:11]);
		minute = int(name[11:13]);
		second  = int(name[13:15]);
		# print("PhotoName: " + str(name) + " -> Year: " + str(year) + " Month: " + str(month) + " Day: " + str(day) + " Hour: " +str(hour) + " Minute: " + str(minute)) 
		try:
			filename = name
			exif_dict = piexif.load(filename)
			
			exif_dict['Exif'] = { piexif.ExifIFD.DateTimeOriginal: datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S") }
			
			exif_bytes = piexif.dump(exif_dict)
			piexif.insert(exif_bytes, filename)
		except:
		  print("Cannot set this image: " + name)
	if(name[len(name) - 4 : len(name)] == '.PNG'):
		print("This is a png file, skipping | " + name);
		# Convert to PNG
		filename = name
		im = Image.open(filename)
		rgb_im = im.convert('RGB')
		rgb_im.save( filename[0: ( len(filename) - 4) ] + '.JPG')
		
		name = filename[0: ( len(filename) - 4) ] + '.JPG';
		year = int(name[0:4]);
		month = int(name[4:6]);
		day = int(name[6:8]);
		hour = int(name[9:11]);
		minute = int(name[11:13]);
		second  = int(name[13:15]);
		# print("PhotoName: " + str(name) + " -> Year: " + str(year) + " Month: " + str(month) + " Day: " + str(day) + " Hour: " +str(hour) + " Minute: " + str(minute)) 
		try:
			filename = name
			exif_dict = piexif.load(filename)
			
			exif_dict['Exif'] = { piexif.ExifIFD.DateTimeOriginal: datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S") }
			
			exif_bytes = piexif.dump(exif_dict)
			piexif.insert(exif_bytes, filename)
		except:
		  print("Cannot set this image: " + name)
	


