Summary:	HTML/XML templating system for Python
Name:		python-meld3
Version:	1.0.2
Release:	1

License:	BSD
Group:		Development/Python 
URL:		http://www.plope.com/software/meld3/
Source0:	http://pypi.python.org/packages/source/m/meld3/meld3-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	python-setuptools
BuildRequires:	python-devel


%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template
markup and dynamic rendering logic separate from one another. See
http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -q -n meld3-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

#%%check
#%%{__python} meld3/test_meld3.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt CHANGES.txt
%{python_sitelib}/*


%changelog
* Tue Nov 01 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 709297
- imported package python-meld3

