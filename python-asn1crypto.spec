%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%global python3_pkgversion %{nil}

# Created by pyp2rpm-3.2.2
%global pypi_name asn1crypto

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.2.0
Release:        4%{?dist}
Summary:        Fast Python ASN.1 parser and serializer

License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rpm-macros


%description
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# asn1crypto source distribution doesn't come with tests
# {__python3} setup.py test
%{?scl:EOF}

%files
%doc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue Feb 04 2020 Lumír Balhar <lbalhar@redhat.com> - 1.2.0-4
- Import from the python38 module and modified for rh-python38 RHSCL
Resolves: rhbz#1671025

* Fri Dec 13 2019 Tomas Orsava <torsava@redhat.com> - 1.2.0-3
- Exclude unsupported i686 arch

* Wed Nov 20 2019 Lumír Balhar <lbalhar@redhat.com> - 1.2.0-2
- Adjusted for Python 3.8 module in RHEL 8

* Mon Nov 18 2019 Lumír Balhar <lbalhar@redhat.com> - 1.2.0-1
- New upstream version 1.2.0 (#1758089)

* Sat Oct 12 2019 Christian Heimes <cheimes@redhat.com> - 0.24.0-10
- Drop Python 2 package
- Resolves: rhbz#1761084

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Christian Heimes <cheimes@redhat.com> - 0.24.0-3
- Build Python 2 package conditionally

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.24.0-2
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Christian Heimes <cheimes@redhat.com> - 0.24.0-1
- New upstream release 0.24.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Christian Heimes <cheimes@redhat.com> - 0.23-1
- New upstream release 0.23.0

* Fri Aug 04 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-5
- Use python2-setuptools, add with_python3

* Thu Aug 03 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-4
- Modernize spec

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-2
- Address rpmlint issues

* Tue Jun 27 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-1
- Initial package.