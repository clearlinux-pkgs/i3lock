#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4E7160ED4AC8EE1D (michael@stapelberg.de)
#
Name     : i3lock
Version  : 2.13
Release  : 10
URL      : https://i3wm.org/i3lock/i3lock-2.13.tar.bz2
Source0  : https://i3wm.org/i3lock/i3lock-2.13.tar.bz2
Source1  : https://i3wm.org/i3lock/i3lock-2.13.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: i3lock-bin = %{version}-%{release}
Requires: i3lock-data = %{version}-%{release}
Requires: i3lock-license = %{version}-%{release}
Requires: i3lock-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libev-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-atom)
BuildRequires : pkgconfig(xcb-event)
BuildRequires : pkgconfig(xcb-image)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xcb-util)
BuildRequires : pkgconfig(xcb-xinerama)
BuildRequires : pkgconfig(xcb-xkb)
BuildRequires : pkgconfig(xcb-xrm)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xkbcommon-x11)
Patch1: 0001-fix-include-libev.patch
Patch2: 0002-Use-gdm-password-derived-PAM-config-instead.patch

%description
i3lock - improved screen locker
===============================
[i3lock](https://i3wm.org/i3lock/)> is a simple screen locker like slock.
After starting it, you will see a white screen (you can configure the
color/an image). You can return to your screen by entering your password.

%package bin
Summary: bin components for the i3lock package.
Group: Binaries
Requires: i3lock-data = %{version}-%{release}
Requires: i3lock-license = %{version}-%{release}

%description bin
bin components for the i3lock package.


%package data
Summary: data components for the i3lock package.
Group: Data

%description data
data components for the i3lock package.


%package license
Summary: license components for the i3lock package.
Group: Default

%description license
license components for the i3lock package.


%package man
Summary: man components for the i3lock package.
Group: Default

%description man
man components for the i3lock package.


%prep
%setup -q -n i3lock-2.13
cd %{_builddir}/i3lock-2.13
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603928420
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1603928420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/i3lock
cp %{_builddir}/i3lock-2.13/LICENSE %{buildroot}/usr/share/package-licenses/i3lock/5cd63d8ad7ba3d702c355805f41914b9a5dd640f
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/pam.d
mv %{buildroot}/etc/pam.d/*  %{buildroot}/usr/share/pam.d
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/i3lock

%files data
%defattr(-,root,root,-)
/usr/share/pam.d/i3lock

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/i3lock/5cd63d8ad7ba3d702c355805f41914b9a5dd640f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/i3lock.1
