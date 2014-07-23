Summary:	HTML/XML templating system for Python
Name:		python-meld3
Version:	1.0.0
Release:	1

License:	ZPLv2.1
Group:		Development/Python 
URL:		http://www.plope.com/software/meld3/
Source0:	http://pypi.python.org/packages/source/m/meld3/meld3-%{version}.tar.gz
Patch0:		python-meld3-0.6.7-missing-src-file.patch

BuildRequires:	python-celementtree
Requires:	python-celementtree
BuildRequires:	python-devel


%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template
markup and dynamic rendering logic separate from one another. See
http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -q -n meld3-%{version}
%patch0 -p1 -b .missing-src-file

%build
export USE_MELD3_EXTENSION_MODULES=True
CFLAGS="%{optflags}" python setup.py build

%install
export USE_MELD3_EXTENSION_MODULES=True
python setup.py install --skip-build --root %{buildroot}
sed -i s'/^#!.*//' $( find %{buildroot}/%{python_sitearch}/meld3/ -type f)
chmod 0755 %{buildroot}/%{py_platsitedir}/meld3/cmeld3.so

%check
python meld3/test_meld3.py

%clean

%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt CHANGES.txt
%{py_platsitedir}/*
