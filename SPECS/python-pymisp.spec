Name:		python-pymisp
Version:	2.4.90
Release:	2%{?dist}
Summary:    Python interface to MISP

Group:		Development/Languages
License:	PyMISP-License
URL:		https://github.com/MISP/PyMISP
Source0:	fake-tgz.tgz

BuildArch:  noarch
BuildRequires:	python-devel, python-setuptools, git
BuildRequires:  python-pip
Requires:	python, python-pip, python-requests

%description
Python interface to MISP

%prep
%setup -q -n fake-tgz

%build
# intentianally left empty

%install
git clone https://github.com/MISP/PyMISP.git
cd PyMISP
git submodule update --init
pip install --install-option='--prefix=$RPM_BUILD_ROOT/usr' -I .

%files
/usr/lib/python2.7/site-packages/*
/usr/bin/*

%changelog
* Wed Aug 25 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.4.90
- update to version 2.4.90

* Fri Mar 30 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.4.82-2
- update to version 2.4.82-2

* Fri Jan 12 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.4.82
- update to version 2.4.82

* Tue Oct 17 2017 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.4.81
- first version
