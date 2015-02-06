# This spec is based on GvM work in MIB

%define		oversion	2g

Name:		dikt
Version:	2.0g
Release:	2
Summary:	A KDE client for the Dict network dictionary protocol
License:	BSD-like
Group:		Networking/Other
URL:		http://dikt.99k.org/
Source0:	%{name}-%{oversion}.xz
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	phonon-devel

%description
Dikt is a dictionary that implements the client side of Dict protocol for
KDE. It is a network application: it looks up words on dict servers; so you
don't need to install any dictionaries and only need a connection to
the Internet. It is very similar to web browsers but has the advantage that
is much smaller and faster than a real web browser.

%prep
%setup -q -n %{name}-%{oversion}
# The LICENSE file has wrong permissions and
# result unalterable later
%__chmod +w LICENSE

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_kde_bindir}/%{name}
%{_kde_datadir}/apps/%{name}/*
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_services}/dict.protocol
%{_kde_iconsdir}/hicolor/128x128/apps/%{name}.png



%changelog
* Wed Feb 22 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0g-1mdv2011.0
+ Revision: 779181
- Update URL
- imported package dikt

