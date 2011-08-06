WEBDIR ?= ${HOME}/www/pygtk-web
IMGDIR = ${WEBDIR}/img
DISTDIR = ${WEBDIR}/dist
ARTICLEDIR = ${WEBDIR}/articles

#using python2.4 now (2007/04/19)
PYTHON = python
PROCESSOR = ${PYTHON} stp.py

WGET = wget
REFTARBALLS = \
	documentation/pygobject.tar.bz2	\
	documentation/pygtk.tar.bz2

TARBALLS = 								\
	http://www.moeraki.com/pygtktutorial/pygtk2tutorial.tgz 	\
	http://www.moeraki.com/pygtktutorial/pygtktutorial.tgz 		\
	http://www.moeraki.com/pygtktutorial/pygtk2-tut.pdf 		\
	http://www.sicem.biz/personal/lgs/docs/pygtk2tutorial-es.tgz 	\
	http://www.cornets.net/mige/pygtk2tutorial-id/pygtk2tutorial-id.tgz

LOCAL_TARBALLS =				\
	documentation/pygtkmozembed.tar.bz2	\
	documentation/pygtksourceview.tar.bz2	\
	documentation/pygtkspell.tar.bz2	\
	documentation/pygnomeprint.tar.bz2	\
	documentation/pygnomeprintui.tar.bz2	\
	documentation/pygnomevfs.tar.bz2

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
	reference.src 		\
	tutorial.src

HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src newsitems.py feed.py
CSS_FILES = default.css

all: start_log pages tarballs finish_log

html: ${HTML_PAGES}

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
	cp -fa articles/* ${ARTICLEDIR}
	cp ${CSS_FILES} ${WEBDIR}
	cp img/*.jpg ${IMGDIR}
	cp img/*.png ${IMGDIR}
	cp news.rss ${WEBDIR}
	cp .htaccess ${WEBDIR}/.htaccess

remote-tarballs:
	-(cd ${DISTDIR}; ${WGET} -KN ${TARBALLS})
	(cd ${WEBDIR}; for f in ${DISTDIR}/*.tgz; do tar xzf $$f; done)

reference-tarballs:
	rm -fr ${WEBDIR}/pygtk2reference
	ln -s ${WEBDIR}/docs/pygtk ${WEBDIR}/pygtk2reference 

	mkdir -p ${WEBDIR}/docs

	(srcdir=`pwd`; cd ${WEBDIR}/docs; for f in ${REFTARBALLS}; do bzip2 -dc $${srcdir}/$$f | tar x; done)

local-tarballs:
	cp ${LOCAL_TARBALLS} ${DISTDIR}
	(srcdir=`pwd`; cd ${WEBDIR}; for f in ${LOCAL_TARBALLS}; do bzip2 -dc $${srcdir}/$$f | tar x; done)

# The spanish and bahasa indonesia tutorials aren't utf-8, so we need to
# fix this them up in this hackish sort of way.
tarball-directory-fixups:
	cp .htaccess-latin1 ${WEBDIR}/pygtk2tutorial-es/.htaccess
	cp .htaccess-latin1 ${WEBDIR}/pygtk2tutorial-id/.htaccess

tarballs: local-tarballs remote-tarballs reference-tarballs tarball-directory-fixups

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs extras tarballs remote-tarballs local-tarballs tarball-directory-fixups \
		 		pages start_log finish_log reference-tarballs

