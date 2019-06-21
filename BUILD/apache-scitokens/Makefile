.PHONY: install

install: src/scitoken.c
	yum install httpd-devel #apt-get install apache2-dev
	rm -rf scitokens-cpp
	git clone https://github.com/scitokens/scitokens-cpp.git
	cd scitokens-cpp/src;\
	cp scitokens.h /usr/include;\
	mkdir build;\
	cd build;\
	git clone https://github.com/Thalhammer/jwt-cpp.git;\
	JWT_CPP_DIR = jwt-cpp cmake ..;\
	make;\
	echo "installing apache-scitoken"
	apxs -i -a -c src/scitoken.c -lSciTokens
