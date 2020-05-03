DESTHOST = rpi2-01.local
DESTDIR = /home/rnslucas/pythonprojects/gimbal

# List the current target directory
ls : 
	/usr/bin/ssh ${DESTHOST} 'ls -l ${DESTDIR}'

deploy :
	/usr/bin/scp *.* ${DESTHOST}:${DESTDIR}
	/usr/bin/scp -r static ${DESTHOST}:${DESTDIR}
	/usr/bin/scp -r templates ${DESTHOST}:${DESTDIR}
	/usr/bin/scp -r libs ${DESTHOST}:${DESTDIR}

