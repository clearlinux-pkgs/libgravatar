#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libgravatar
Version  : 25.04.2
Release  : 83
URL      : https://download.kde.org/stable/release-service/25.04.2/src/libgravatar-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/libgravatar-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/libgravatar-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libgravatar-25.04.2
cd %{_builddir}/libgravatar-25.04.2
pushd ..
cp -a libgravatar-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749523849
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
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1749523849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgravatar
cp %{_builddir}/libgravatar-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libgravatar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libgravatar-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libgravatar-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libgravatar-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/libgravatar/83531e59fb16ef6f78484389fd0551b70a226866 || :
cp %{_builddir}/libgravatar-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/libgravatar-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/libgravatar/83531e59fb16ef6f78484389fd0551b70a226866 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libgravatar6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/libgravatar.categories
/usr/share/qlogging-categories6/libgravatar.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/Gravatar/Gravatar/GravatarCache
/usr/include/KPim6/Gravatar/Gravatar/GravatarConfigureSettingsDialog
/usr/include/KPim6/Gravatar/Gravatar/GravatarConfigureSettingsWidget
/usr/include/KPim6/Gravatar/Gravatar/GravatarDownloadPixmapWidget
/usr/include/KPim6/Gravatar/Gravatar/GravatarResolvUrlJob
/usr/include/KPim6/Gravatar/gravatar/gravatar_export.h
/usr/include/KPim6/Gravatar/gravatar/gravatarcache.h
/usr/include/KPim6/Gravatar/gravatar/gravatarconfiguresettingsdialog.h
/usr/include/KPim6/Gravatar/gravatar/gravatarconfiguresettingswidget.h
/usr/include/KPim6/Gravatar/gravatar/gravatardownloadpixmapwidget.h
/usr/include/KPim6/Gravatar/gravatar/gravatarresolvurljob.h
/usr/include/KPim6/Gravatar/gravatar/gravatarsettings.h
/usr/include/KPim6/Gravatar/gravatar_version.h
/usr/lib64/cmake/KPim6Gravatar/KPim6GravatarConfig.cmake
/usr/lib64/cmake/KPim6Gravatar/KPim6GravatarConfigVersion.cmake
/usr/lib64/cmake/KPim6Gravatar/KPim6GravatarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6Gravatar/KPim6GravatarTargets.cmake
/usr/lib64/libKPim6Gravatar.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6Gravatar.so.6.4.2
/usr/lib64/libKPim6Gravatar.so.6
/usr/lib64/libKPim6Gravatar.so.6.4.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgravatar/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libgravatar/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libgravatar/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libgravatar/83531e59fb16ef6f78484389fd0551b70a226866
/usr/share/package-licenses/libgravatar/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libgravatar6.lang
%defattr(-,root,root,-)

