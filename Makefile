WEBDIR ?= ${HOME}/www/pygtk-web
IMGDIR = ${WEBDIR}/img
DISTDIR = ${WEBDIR}/dist
ARTICLEDIR = ${WEBDIR}/articles

PYTHON = python2.2
PROCESSOR = ${PYTHON} stp.py

WGET = wget
TARBALLS = http://www.moeraki.com/pygtkreference/pygtk2reference.tgz \
		   http://www.moeraki.com/pygtktutorial/pygtk2tutorial.tgz \
		   http://www.moeraki.com/pygtktutorial/pygtktutorial.tgz \
		   http://www.sicem.biz/personal/lgs/docs/pygtk2tutorial-es.tgz \
		   http://www.cornets.net/mige/pygtk2tutorial-id/pygtk2tutorial-id.tgz

SRC_PAGES = index.src about.src screenshots.src news.src downloads.src \
			feedback.src applications.src people.src articles.src \
			tutorial.src reference.src newsitems.src developer.src

HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src
CSS_FILES = default.css

all: start_log pages tarballs finish_log

pages: dirs ${HTML_PAGES} extras 

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

tarballs:
	-(cd ${DISTDIR}; ${WGET} -KN ${TARBALLS})
	(cd ${WEBDIR}; for f in ${DISTDIR}/*.tgz; do tar xzf $$f; done)

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs extras tarballs pages start_log finish_log
