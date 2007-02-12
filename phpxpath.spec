Summary:	A PHP Xpath library
Summary(pl.UTF-8):   Biblioteka PHP Xpath
Name:		phpxpath
Version:	3.5
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://dl.sourceforge.net/phpxpath/PhpXPath-%{version}.zip
# Source0-md5:	44a433d971f51d3431f5abe98dfc703e
URL:		http://phpxpath.sourceforge.net/
BuildRequires:	unzip
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
A PHP class for searching an XML document using XPath, and making
modifications using a DOM style API. Does not require the DOM XML PHP
library.

%description -l pl.UTF-8
Klasa PHP służąca do przeszukiwania dokumentów XML przy użyciu XPath
i dokonywania modyfikacji korzystając z API w styli DOM. Nie wymaga
biblioteki PHP DOM XML.

%prep
%setup -q -c

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
