NAME=python-megacli
VERSION=1.0
FPM=/usr/lib/ruby/gems/1.8/bin/fpm
ifdef BUILD_VCS_NUMBER
    RELEASE=${BUILD_VCS_NUMBER}
else
    RELEASE=1
endif

OSREL:=$(shell lsb_release -sir | sed -e 's/ //' -e 's/Fedora/fc/' -e 's/CentOS/el/' -e 's/Scientific/el/' | cut -f1 -d'.')

all: rpm

clean:
	rm -f *.rpm

rpm:
	${FPM} -s python -t rpm -v ${VERSION} --iteration ${RELEASE}.${OSREL} -n ${NAME} .
