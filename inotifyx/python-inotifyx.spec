%global lib_name inotifyx

Name:           python-inotifyx
Version:        0.2.2
Release:        2%{?dist}
Summary:        Simple Python binding to the Linux inotify API.

License:        MIT
URL:            https://launchpad.net/inotifyx
Source0:        https://launchpad.net/%{lib_name}/dev/v%{version}/+download/%{lib_name}-%{version}.tar.gz
Patch0:         0001-python3-compatibility.patch
Patch1:         0002-update-C-binding-for-python3.patch

ExclusiveArch:  %{ix86} x86_64
BuildRequires:  pkgconfig(python2)
BuildRequires:  python-setuptools

%description
Simple Python binding to the Linux inotify file system event monitoring API.


%prep
%autosetup -n %{lib_name}-%{version} -p1


%build
%py2_build


%install
%py2_install
# Remove references to buildroot to fix check-buildroot
sed -e 's:%{buildroot}::g' -i %{buildroot}%{python2_sitearch}/inotifyx/distinfo.py


%check
%{__python2} setup.py test


%files
%license COPYING
%doc AUTHORS NEWS README
%{python2_sitearch}/*


%changelog
* Tue Jun 16 2020 Manuela Kuhn <manuela.kuhn@desy.de> - 0.2.2-2
- Use python build and install tools directly
* Sat Mar 12 2016 Dylan Smith <dyskette@gmail.com> - 0.2.2-1
- First package
