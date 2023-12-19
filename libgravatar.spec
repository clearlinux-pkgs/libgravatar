#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libgravatar
Version  : 23.08.4
Release  : 61
URL      : https://download.kde.org/stable/release-service/23.08.4/src/libgravatar-23.08.4.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.4/src/libgravatar-23.08.4.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.4/src/libgravatar-23.08.4.tar.xz.sig
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
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
BuildRequires : pimcommon-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
%setup -q -n libgravatar-23.08.4
cd %{_builddir}/libgravatar-23.08.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702992376
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702992376
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgravatar
cp %{_builddir}/libgravatar-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libgravatar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libgravatar-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libgravatar-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libgravatar-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/libgravatar/83531e59fb16ef6f78484389fd0551b70a226866 || :
cp %{_builddir}/libgravatar-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libgravatar
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/libgravatar.categories
/usr/share/qlogging-categories5/libgravatar.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/Gravatar/Gravatar/GravatarCache
/usr/include/KPim5/Gravatar/Gravatar/GravatarConfigureSettingsDialog
/usr/include/KPim5/Gravatar/Gravatar/GravatarConfigureSettingsWidget
/usr/include/KPim5/Gravatar/Gravatar/GravatarDownloadPixmapWidget
/usr/include/KPim5/Gravatar/Gravatar/GravatarResolvUrlJob
/usr/include/KPim5/Gravatar/gravatar/gravatar_export.h
/usr/include/KPim5/Gravatar/gravatar/gravatarcache.h
/usr/include/KPim5/Gravatar/gravatar/gravatarconfiguresettingsdialog.h
/usr/include/KPim5/Gravatar/gravatar/gravatarconfiguresettingswidget.h
/usr/include/KPim5/Gravatar/gravatar/gravatardownloadpixmapwidget.h
/usr/include/KPim5/Gravatar/gravatar/gravatarresolvurljob.h
/usr/include/KPim5/Gravatar/gravatar/gravatarsettings.h
/usr/include/KPim5/Gravatar/gravatar_version.h
/usr/lib64/cmake/KPim5Gravatar/KPim5GravatarConfig.cmake
/usr/lib64/cmake/KPim5Gravatar/KPim5GravatarConfigVersion.cmake
/usr/lib64/cmake/KPim5Gravatar/KPim5GravatarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Gravatar/KPim5GravatarTargets.cmake
/usr/lib64/libKPim5Gravatar.so
/usr/lib64/qt5/mkspecs/modules/qt_Gravatar.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Gravatar.so.5.24.4
/usr/lib64/libKPim5Gravatar.so.5
/usr/lib64/libKPim5Gravatar.so.5.24.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libgravatar/83531e59fb16ef6f78484389fd0551b70a226866
/usr/share/package-licenses/libgravatar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libgravatar.lang
%defattr(-,root,root,-)

