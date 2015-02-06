Summary:	HTML/XML templating system for Python
Name:		python-meld3
Version:	0.6.7
Release:	2

License:	ZPLv2.1
Group:		Development/Python 
URL:		http://www.plope.com/software/meld3/
Source0:	http://pypi.python.org/packages/source/m/meld3/meld3-%{version}.tar.gz
Patch0:		python-meld3-0.6.7-missing-src-file.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
export USE_MELD3_EXTENSION_MODULES=True
%{__python} setup.py install --skip-build --root %{buildroot}
sed -i s'/^#!.*//' $( find %{buildroot}/%{python_sitearch}/meld3/ -type f)
chmod 0755 %{buildroot}/%{python_sitearch}/meld3/cmeld3.so

%check
%{__python} meld3/test_meld3.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt CHANGES.txt
%{python_sitearch}/*


%changelog
* Tue Nov 01 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 709297
- imported package python-meld3

