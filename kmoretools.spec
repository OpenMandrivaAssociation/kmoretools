%define libname %mklibname KF6MoreTools
%define devname %mklibname KF6MoreTools -d
%define git 20230729

Name: kmoretools
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/libraries/kmoretools/-/archive/master/kmoretools-master.tar.bz2#/kmoretools-%{git}.tar.bz2
Summary: Support for downloading application assets from the network
URL: https://invent.kde.org/libraries/kmoretools
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6WidgetsAddons)
Requires: %{libname} = %{EVRD}
# Prevent the KF5 version from being pulled in
BuildRequires: plasma6-xdg-desktop-portal-kde

%description
Support for downloading application assets from the network

%package -n %{libname}
Summary: Support for downloading application assets from the network
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Support for downloading application assets from the network

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Support for downloading application assets from the network

%prep
%autosetup -p1 -n kmoretools-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html --with-man

%files -f %{name}.lang
%{_datadir}/kf6/kmoretools

%files -n %{devname}
%{_includedir}/KF6/KMoreTools
%{_includedir}/KF6/kmoretools_version.h
%{_libdir}/cmake/KF6MoreTools
%{_qtdir}/doc/KF6MoreTools.qch
%{_qtdir}/doc/KF6MoreTools.tags

%files -n %{libname}
%{_libdir}/libKF6MoreTools.so*
