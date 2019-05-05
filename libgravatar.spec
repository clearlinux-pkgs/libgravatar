#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libgravatar
Version  : 19.04.0
Release  : 6
URL      : https://download.kde.org/stable/applications/19.04.0/src/libgravatar-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/libgravatar-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/libgravatar-19.04.0.tar.xz.sig
Summary  : KDE PIM library providing Gravatar support
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libgravatar-data = %{version}-%{release}
Requires: libgravatar-lib = %{version}-%{release}
Requires: libgravatar-license = %{version}-%{release}
Requires: libgravatar-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the libgravatar package.
Group: Data

%description data
data components for the libgravatar package.


%package dev
Summary: dev components for the libgravatar package.
Group: Development
Requires: libgravatar-lib = %{version}-%{release}
Requires: libgravatar-data = %{version}-%{release}
Provides: libgravatar-devel = %{version}-%{release}
Requires: libgravatar = %{version}-%{release}

%description dev
dev components for the libgravatar package.


%package lib
Summary: lib components for the libgravatar package.
Group: Libraries
Requires: libgravatar-data = %{version}-%{release}
Requires: libgravatar-license = %{version}-%{release}

%description lib
lib components for the libgravatar package.


%package license
Summary: license components for the libgravatar package.
Group: Default

%description license
license components for the libgravatar package.


%package locales
Summary: locales components for the libgravatar package.
Group: Default

%description locales
locales components for the libgravatar package.


%prep
%setup -q -n libgravatar-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557038593
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557038593
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgravatar
cp COPYING %{buildroot}/usr/share/package-licenses/libgravatar/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libgravatar/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libgravatar

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/libgravatar.categories
/usr/share/xdg/libgravatar.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Gravatar/GravatarCache
/usr/include/KF5/Gravatar/GravatarConfigWidget
/usr/include/KF5/Gravatar/GravatarConfigureSettingsDialog
/usr/include/KF5/Gravatar/GravatarConfigureSettingsWidget
/usr/include/KF5/Gravatar/GravatarDownloadPixmapWidget
/usr/include/KF5/Gravatar/GravatarResolvUrlJob
/usr/include/KF5/gravatar/gravatar_export.h
/usr/include/KF5/gravatar/gravatarcache.h
/usr/include/KF5/gravatar/gravatarconfiguresettingsdialog.h
/usr/include/KF5/gravatar/gravatarconfiguresettingswidget.h
/usr/include/KF5/gravatar/gravatarconfigwidget.h
/usr/include/KF5/gravatar/gravatardownloadpixmapwidget.h
/usr/include/KF5/gravatar/gravatarresolvurljob.h
/usr/include/KF5/gravatar/gravatarsettings.h
/usr/include/KF5/gravatar_version.h
/usr/lib64/cmake/KF5Gravatar/KF5GravatarConfig.cmake
/usr/lib64/cmake/KF5Gravatar/KF5GravatarConfigVersion.cmake
/usr/lib64/cmake/KF5Gravatar/KF5GravatarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Gravatar/KF5GravatarTargets.cmake
/usr/lib64/libKF5Gravatar.so
/usr/lib64/qt5/mkspecs/modules/qt_Gravatar.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Gravatar.so.5
/usr/lib64/libKF5Gravatar.so.5.11.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgravatar/COPYING
/usr/share/package-licenses/libgravatar/COPYING.LIB

%files locales -f libgravatar.lang
%defattr(-,root,root,-)

