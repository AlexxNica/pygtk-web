WEBDIR = ${HOME}/www/pygtk-web
IMGDIR = ${HOME}/www/pygtk-web/img
TUTDIRS = ${HOME}/www/pygtk-web/pygtktutorial \
		${HOME}/www/pygtk-web/pygtk2tutorial \
		${HOME}/www/pygtk-web/pygtk2tutorial-lgs
REFDIRS = ${HOME}/www/pygtk-web/pygtk2reference

PYTHON = python2
PROCESSOR = ${PYTHON} stp.py

SRC_PAGES = index.src about.src screenshots.src news.src downloads.src \
		 feedback.src applications.src people.src articles.src \
		tutorial.src reference.src
HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src
CSS_FILES = default.css

all: dirs ${HTML_PAGES}

dirs: ${WEBDIR} ${IMGDIR} ${TUTDIRS} ${REFDIRS}

${WEBDIR}:
	mkdir -p ${WEBDIR}
	cp ${CSS_FILES} ${WEBDIR}

${IMGDIR}:
	mkdir -p ${IMGDIR}
	cp img/*.png ${IMGDIR}

${TUTDIRS}:
	mkdir -p ${TUTDIRS}

${REFDIRS}:
	mkdir -p ${REFDIRS}

${HTML_PAGES}: ${SRC_PAGES} ${COMMON_PAGES}

${WEBDIR}/%.html: %.src
	${PROCESSOR} $< > $@

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs
