import platform
import ctypes
import os

OS = platform.uname().system
if 'Linux' in OS:
	DLL = ctypes.CDLL
	OS = 'linux'
	klusolve = None
	opendssdirect = 'libOpenDSSDirect.so'
elif 'Darwin' in OS:
	DLL = ctypes.CDLL
	OS = 'darwin'
	klusolve = 'libklusolve.dylib'
	opendssdirect = 'libOpenDSSDirect.dylib'
else:
	DLL = ctypes.WinDLL
	OS = 'windows'
	klusolve = 'KLUSolve.dll'
	opendssdirect = 'OpenDSSDirect.dll'

CPU = platform.uname().machine
if 'x86_64' in CPU:
	CPU = 'x86_64'
elif 'x86' in CPU or 'i386' in CPU or 'i686' in CPU:
	CPU = 'x86_32'
elif 'arm' in CPU:
	CPU = CPU
else:
	CPU = None

if CPU is None:
	raise TypeError('Unsupported CPU {}'.format(platform.uname().machine))

print('super directors: {}'.format(os.listdir('..')))
print('library content: {}'.format(os.listdir('../_lib')))

if klusolve is not None:
	DLL('../_lib/{}-{}/{}'.format(CPU, OS, klusolve))

dss = DLL('../_lib/{}-{}/{}'.format(CPU, OS, opendssdirect))

print('{} -> Start({})'.format(dss, dss.DSSI(ctypes.c_int32(3), ctypes.c_int32(0)) == 1))
