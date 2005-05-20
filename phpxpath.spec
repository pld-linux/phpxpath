Summary:	A PHP Xpath library
Summary(pl):	Biblioteka PHP Xpath
Name:		phpxpath
Version:	3.5
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://dl.sourceforge.net/phpxpath/PhpXPath-%{version}.zip
# Source0-md5:	44a433d971f51d3431f5abe98dfc703e
URL:		http://phpxpath.sourceforge.net/
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
A php class for searching an XML document using XPath, and making
modifications using a DOM style API. Does not require the DOM XML PHP
library.

%description -l pl
Clasa php s³u¿±ca do szukania dokumentów XML korzystaj±c z XPath i
tworz±c modyfikacje korzystaj±c z API w styli DOM. Nie wymaga
biblioteki DOM XML PHP.

%prep
%setup  -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_phpsharedir}/%{name}
