WEBDIR ?= ${HOME}/www/pygtk-web
IMGDIR = ${WEBDIR}/img
DISTDIR = ${WEBDIR}/dist
ARTICLEDIR = ${WEBDIR}/articles

PYTHON = python2.2
PROCESSOR = ${PYTHON} stp.py

WGET = wget # XXX move to rsync
TARBALLS = http://www.moeraki.com/pygtkreference/pygtk2reference.tgz \
		   http://www.moeraki.com/pygtktutorial/pygtk2tutorial.tgz \
		   http://www.moeraki.com/pygtktutorial/pygtktutorial.tgz
		   # XXX: add lgs' spanish version

SRC_PAGES = index.src about.src screenshots.src news.src downloads.src \
			feedback.src applications.src people.src articles.src \
			tutorial.src reference.src newsitems.src developer.src

HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src
CSS_FILES = default.css

all: start_log dirs ${HTML_PAGES} extras finish_log

dirs: ${WEBDIR} ${IMGDIR} ${DISTDIR} ${ARTICLEDIR}

start_log:
	echo 'Starting to build the PyGTK web'

finish_log:
	echo 'PyGTK web finished'

${WEBDIR}:
	mkdir -p ${WEBDIR}

${IMGDIR}:
	mkdir -p ${IMGDIR}

${DISTDIR}:
	mkdir -p ${DISTDIR}

${ARTICLEDIR}:
	mkdir -p ${ARTICLEDIR}

${HTML_PAGES}: ${SRC_PAGES} ${COMMON_PAGES}

${WEBDIR}/%.html: %.src
	${PROCESSOR} $< > $@

extras: ${CSS_FILES} img/*.png
	cp -a articles/* ${ARTICLEDIR}
	cp ${CSS_FILES} ${WEBDIR}
	cp img/*.png ${IMGDIR}
	(cd ${DISTDIR}; ${WGET} -qc ${TARBALLS})
	(cd ${WEBDIR}; for f in ${DISTDIR}/*.tgz; do tar xfz $$f ; done)

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs extras
