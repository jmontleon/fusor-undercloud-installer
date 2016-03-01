Name: 		fusor-undercloud-installer
Version: 	1.0
Release:	1%{?dist}
Summary: 	Scripts to configure and install an OpenStack Undercloud instance.

Group:		Development/Python
License: 	GPLv3+
URL: 		https://github.com/fusor/fusor-undercloud-installer
Source0: 

Requires: python(abi) = 2.7
Requires: ruby193-rubygem-egon
Requires: python-ipaddress
Requires: python-netifaces
BuildArch noarch

%description
Fusor Undercloud Installer

%prep
%setup -q


%build
#don't really need to build anything

%install
install -d -m0755 %{buildroot}%{_sbindir}
cp bin/fusor-undercloud-installer %{buildroot}%{_sbindir}/fusor-undercloud-installer
cp bin/fusor-undercloud-configurator %{buildroot}%{_sbindir}/fusor-undercloud-configurator

%files
%doc LICENSE
%defattr(755, root, root)
%{_sbindir}/fusor-undercloud-installer
%{_sbindir}/fusor-undercloud-configurator


%changelog

