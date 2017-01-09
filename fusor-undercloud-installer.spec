Name:       fusor-undercloud-installer
Version:    1.1.0
Release:    0%{?dist}
Summary:    Scripts to configure and install an OpenStack Undercloud instance.

Group:      Development/Python
License:    GPLv3+
URL:        https://github.com/fusor/fusor-undercloud-installer
Source0:    %{name}-%{version}.tar.gz

BuildRequires: asciidoc

Requires: python(abi) = 2.7
Requires: tfm-rubygem-egon
Requires: python-ipaddress
Requires: python-netifaces
BuildArch: noarch

%description
Fusor Undercloud Installer

%prep
%setup -q


%build
a2x -d manpage -f manpage fusor-undercloud-installer.8.asciidoc
a2x -d manpage -f manpage fusor-undercloud-configurator.8.asciidoc
a2x -d manpage -f manpage fusor-undercloud-installer.answers.yaml.5.asciidoc

%install
install -d -m0755 %{buildroot}%{_sbindir}
cp bin/fusor-undercloud-installer %{buildroot}%{_sbindir}/fusor-undercloud-installer
cp bin/fusor-undercloud-configurator %{buildroot}%{_sbindir}/fusor-undercloud-configurator
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__mkdir_p} %{buildroot}%{_mandir}/man8
%{__mkdir_p} %{buildroot}%{_datarootdir}/%{name}
cp -a fusor-undercloud-installer.answers.yaml.5 %{buildroot}/%{_mandir}/man5/
cp -a fusor-undercloud-installer.8 %{buildroot}/%{_mandir}/man8/
cp -a fusor-undercloud-configurator.8 %{buildroot}/%{_mandir}/man8/
cp -a disable-docker-registry.yaml %{buildroot}%{_datarootdir}/%{name}/

%files
%doc LICENSE
%defattr(755, root, root)
%{_sbindir}/fusor-undercloud-installer
%{_sbindir}/fusor-undercloud-configurator
%{_datarootdir}/%{name}/disable-docker-registry.yaml
%doc %{_mandir}/man5/fusor-undercloud-installer.answers.yaml.5*
%doc %{_mandir}/man8/fusor-undercloud-installer.8*
%doc %{_mandir}/man8/fusor-undercloud-configurator.8*


%changelog

