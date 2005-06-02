WEBDIR ?= ${HOME}/www/pygtk-web
IMGDIR = ${WEBDIR}/img
DISTDIR = ${WEBDIR}/dist
ARTICLEDIR = ${WEBDIR}/articles

PYTHON = python2.2
PROCESSOR = ${PYTHON} stp.py

WGET = wget
TARBALLS = 								\
	http://www.moeraki.com/pygtkreference/pygtk2reference.tgz 	\
	http://www.moeraki.com/pygtkreference/pygtk2reference.tbz2 	\
	http://www.moeraki.com/pygtktutorial/pygtk2tutorial.tgz 	\
	http://www.moeraki.com/pygtktutorial/pygtktutorial.tgz 		\
	http://www.moeraki.com/pygtktutorial/pygtk2-tut.pdf 		\
	http://www.sicem.biz/personal/lgs/docs/pygtk2tutorial-es.tgz 	\
	http://www.cornets.net/mige/pygtk2tutorial-id/pygtk2tutorial-id.tgz

LOCAL_TARBALLS =				\
	documentation/pygtkmozembed.tar.bz2	\
	documentation/pygtksourceview.tar.bz2	\
	documentation/pygtkspell.tar.bz2	\
	documentation/pygnomeprint.tar.bz2

SRC_PAGES = 			\
	about.src 		\
	applications.src 	\
	articles.src 		\
	consulting.src		\
	developer.src 		\
	downloads.src 		\
	feedback.src 		\
	index.src 		\
	news.src 		\
	people.src 		\
	reference.src 		\
	screenshots.src 	\
	tutorial.src

HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src newsitems.py feed.py
CSS_FILES = default.css

all: start_log pages tarballs finish_log

pages: dirs news.rss ${HTML_PAGES} extras 

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

news.rss: newsitems.py feed.py
	${PYTHON} feed.py

extras: ${CSS_FILES} img/*.png
	cp -a articles/* ${ARTICLEDIR}
	cp ${CSS_FILES} ${WEBDIR}
	cp img/*.png ${IMGDIR}
	cp news.rss ${WEBDIR}
	cp .htaccess ${WEBDIR}/.htaccess

remote-tarballs:
	-(cd ${DISTDIR}; ${WGET} -KN ${TARBALLS})
	(cd ${WEBDIR}; for f in ${DISTDIR}/*.tgz; do tar xzf $$f; done)

local-tarballs:
	cp ${LOCAL_TARBALLS} ${DISTDIR}
	(srcdir=`pwd`; cd ${WEBDIR}; for f in ${LOCAL_TARBALLS}; do bzip2 -dc $${srcdir}/$$f | tar x; done)

tarballs: local-tarballs remote-tarballs

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs extras tarballs pages start_log finish_log
