#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgravatar
Version  : 21.12.0
Release  : 34
URL      : https://download.kde.org/stable/release-service/21.12.0/src/libgravatar-21.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.0/src/libgravatar-21.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
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
%setup -q -n libgravatar-21.12.0
cd %{_builddir}/libgravatar-21.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639688778
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639688778
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgravatar
cp %{_builddir}/libgravatar-21.12.0/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libgravatar/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/libgravatar-21.12.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/libgravatar-21.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/libgravatar-21.12.0/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
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
/usr/lib64/libKF5Gravatar.so.5.19.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libgravatar/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123

%files locales -f libgravatar.lang
%defattr(-,root,root,-)

