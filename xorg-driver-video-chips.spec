Summary:	X.org video driver for Chips and Technologies video processors
Summary(pl):	Sterownik obrazu X.org do uk³adów graficznych Chips and Technologies
Name:		xorg-driver-video-chips
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-chips-%{version}.tar.bz2
# Source0-md5:	3182d43439ca4cbf08ff9aa76990bba3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Chips and Technologies video processors. It
supports video processors on most of the bus types currently
available. Supported chipsets fall into one of three architectural
classes: basic (ct65520, ct65525, ct65530, ct65535, ct65540, ct65545,
ct65546, ct65548), WinGine (ct64200, ct64300) and HiQV (ct65550,
ct65554, ct65555, ct68554, ct69000, ct96030).

%description -l pl
Sterownik obrazu X.org do uk³adów graficznych Chips and Technologies.
Obsluguje uk³ady graficzne na wiêkszo¶ci z dostêpnych teraz szyn.
Obs³ugiwane s± uk³ady z trzech klas architektur: basic (ct65520,
ct65525, ct65530, ct65535, ct65540, ct65545, ct65546, ct65548),
WinGine (ct64200, ct64300) oraz HiQV (ct65550, ct65554, ct65555,
ct68554, ct69000, ct96030).

%prep
%setup -q -n xf86-video-chips-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.4*
