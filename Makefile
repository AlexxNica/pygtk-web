WEBDIR = ~/www/pygtk-web
PYTHON = /usr/bin/python2.2
PROCESSOR = ${PYTHON} stp.py

SRC_PAGES = index.src about.src screenshots.src news.src downloads.src \
		 feedback.src applications.src people.src articles.src
HTML_PAGES = $(patsubst %.src, ${WEBDIR}/%.html, ${SRC_PAGES})
COMMON_PAGES = head.src foot.src

all: dirs ${HTML_PAGES}

dirs: ${WEBDIR}

${WEBDIR}:
	mkdir -p ${WEBDIR}

${HTML_PAGES}: ${SRC_PAGES} ${COMMON_PAGES}

${WEBDIR}/%.html: %.src
	${PROCESSOR} $< > $@

clean:
	rm -f ${HTML_PAGES}

.PHONY:	all dirs
