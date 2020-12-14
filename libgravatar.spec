#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libgravatar
Version  : 20.12.0
Release  : 25
URL      : https://download.kde.org/stable/release-service/20.12.0/src/libgravatar-20.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.0/src/libgravatar-20.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.0/src/libgravatar-20.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: libgravatar-data = %{version}-%{release}
Requires: libgravatar-lib = %{version}-%{release}
Requires: libgravatar-license = %{version}-%{release}
Requires: libgravatar-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev

%description
# Gravatar
Online avatar lookup library.
Allows to retrieve avatar images based on a hash from a person's email address, as well
as local caching to avoid unnecessary network operations. Use Gravatar::GravatarResolvUrlJob
for this.

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
%setup -q -n libgravatar-20.12.0
cd %{_builddir}/libgravatar-20.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607914767
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607914767
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgravatar
cp %{_builddir}/libgravatar-20.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang libgravatar

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/libgravatar.categories
/usr/share/qlogging-categories5/libgravatar.renamecategories

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
/usr/lib64/libKF5Gravatar.so.5.16.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a

%files locales -f libgravatar.lang
%defattr(-,root,root,-)

