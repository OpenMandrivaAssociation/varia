Summary:	 Download manager based on aria2 
Name:		varia
Version:	2024.2.6
Release:	1
Group:		Networking/File transfer
License:	GPL
Url:		https://github.com/giantpinkrobots/varia
Source0:	https://github.com/giantpinkrobots/varia/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: python3dist(setuptools)

Requires:	aria2
Requires: aria2p
Requires: python

%description
Varia is a simple download manager that conforms to the latest Libadwaita design guidelines, integrating nicely with GNOME. 
It uses the amazing aria2 to handle the downloads.
It supports basic functionality like continuing incomplete downloads from the previous session upon startup, 
pausing/cancelling all downloads at once, setting a speed limit, authentication with a username/password, 
setting the simultaneous download amount and setting the download directory.

#--------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
# TODO
