#define snapshot 20220107

Name:		maui-pix
Version:	2.2.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Image gallery manager for Plasma Mobile
Source0:	https://invent.kde.org/maui/pix/-/archive/%{?snapshot:master/pix-master.tar.bz2#/pix-%{snapshot}}%{!?snapshot:v%{version}/pix-v%{version}}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(MauiKit)
BuildRequires:  cmake(MauiKitFileBrowsing)
BuildRequires:  cmake(MauiKitImageTools)
BuildRequires:  cmake(MauiKitImageTools)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Threads)
BuildRequires:  pkgconfig(exiv2)

%description
Image gallery manager for Plasma Mobile

%prep
%autosetup -p1 -n pix-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/pix
%{_datadir}/applications/org.kde.pix.desktop
%{_datadir}/icons/hicolor/scalable/apps/pix.svg
%{_datadir}/metainfo/org.kde.pix.appdata.xml
