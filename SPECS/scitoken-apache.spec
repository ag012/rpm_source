#spec file for the apache-scitoken module
Summary: Authentication module for Apache httpd with Scitoken.
Name: apache-scitokens2
Version: 0.1
Release: 1
License: Apache-2.0
Source: https://github.com/scitokens/apache-scitokens

%description
Authentication module for Apache httpd with Scitoken.

%prep
rm -rf apache-scitokens && tar -xvzf apache-scitokens.tar.gz
%install
make
%files
/apache-scitokens
