import os
import mmap
import struct


#file = os.open(unicode('IoAAOLICameraCameraFrame'),os.O_RDWR)
import mmap
tag = "#vvvv"
byteSize = 256
fpx = mmap.mmap (-1,byteSize,tag)
print(fpx.read())
print(struct.unpack('64f', fpx))

#first allocate memory from vvvv with Writer (sharememory)
vvvvTag = "#python"
mm =mmap.mmap( 0,length=256, tagname=vvvvTag)
mm.flush()
string = "Hello vvvv this is python Speaking"
mm.write(string.encode())
mm.close()