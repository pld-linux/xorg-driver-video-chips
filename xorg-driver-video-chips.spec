Summary:	X.org video driver for Chips and Technologies video processors
Summary(pl.UTF-8):	Sterownik obrazu X.org do układów graficznych Chips and Technologies
Name:		xorg-driver-video-chips
Version:	1.5.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.xz
# Source0-md5:	ecd6e9c98d57f1b866bbd3a11a42cf9b
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-chips < 1:7.0.0
Obsoletes:	XFree86-ChipsTechnologies < 4
Obsoletes:	XFree86-driver-chips < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Chips and Technologies video processors. It
supports video processors on most of the bus types currently
available. Supported chipsets fall into one of three architectural
classes:
- basic (ct65520, ct65525, ct65530, ct65535, ct65540, ct65545,
  ct65546, ct65548),
- WinGine (ct64200, ct64300)
- HiQV (ct65550, ct65554, ct65555, ct68554, ct69000, ct96030).

%description -l pl.UTF-8
Sterownik obrazu X.org do układów graficznych Chips and Technologies.
Obsluguje układy graficzne na większości z dostępnych teraz szyn.
Obsługiwane są układy z trzech klas architektur:
- basic (ct65520, ct65525, ct65530, ct65535, ct65540, ct65545,
  ct65546, ct65548),
- WinGine (ct64200, ct64300)
- HiQV (ct65550, ct65554, ct65555, ct68554, ct69000, ct96030).

%prep
%setup -q -n xf86-video-chips-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.4*
