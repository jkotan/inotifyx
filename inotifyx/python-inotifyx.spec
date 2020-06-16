%global lib_name inotifyx

Name:           python-inotifyx
Version:        0.2.2
Release:        3%{?dist}
Summary:        Simple Python binding to the Linux inotify API.

License:        MIT
URL:            https://launchpad.net/inotifyx
Source0:        https://launchpad.net/%{lib_name}/dev/v%{version}/+download/%{lib_name}-%{version}.tar.gz
Patch0:         0001-python3-compatibility.patch
Patch1:         0002-update-C-binding-for-python3.patch

ExclusiveArch:  %{ix86} x86_64
#BuildRequires:  pkgconfig(python2)
#BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python3-devel

%description
Simple Python binding to the Linux inotify file system event monitoring API.


%package -n python2-%{lib_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{lib_name}
%{description}


%package -n python3-%{lib_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{lib_name}
%{description}

%prep
%autosetup -n %{lib_name}-%{version} -p1


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install
# Remove references to buildroot to fix check-buildroot
sed -e 's:%{buildroot}::g' -i %{buildroot}%{python2_sitearch}/inotifyx/distinfo.py
sed -e 's:%{buildroot}::g' -i %{buildroot}%{python3_sitearch}/inotifyx/distinfo.py


%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-%{lib_name}
%license COPYING
%doc AUTHORS NEWS README
%{python2_sitearch}/*

%files -n python3-%{lib_name}
%license COPYING
%doc AUTHORS NEWS README
%{python3_sitearch}/*


%changelog
* Tue Jun 16 2020 Manuela Kuhn <manuela.kuhn@desy.de> - 0.2.2-3
- Add python3 package
* Tue Jun 16 2020 Manuela Kuhn <manuela.kuhn@desy.de> - 0.2.2-2
- Use python build and install tools directly
* Sat Mar 12 2016 Dylan Smith <dyskette@gmail.com> - 0.2.2-1
- First package
