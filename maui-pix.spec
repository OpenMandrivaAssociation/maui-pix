#define snapshot 20220107

Name:		maui-pix
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Image gallery manager for Plasma Mobile
Url:      https://invent.kde.org/maui/pix/
Source0:	https://invent.kde.org/maui/pix/-/archive/%{?snapshot:master/maui-pix-master.tar.bz2#/pix-%{snapshot}}%{!?snapshot:v%{version}/maui-pix-v%{version}}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitImageTools4)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Threads)
BuildRequires:  pkgconfig(exiv2)

%description
Image gallery manager for Plasma Mobile

%prep
%autosetup -p1 -n maui-pix-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang pix

%files -f pix.lang
%{_bindir}/pix
%{_datadir}/applications/org.kde.pix.desktop
%{_datadir}/icons/hicolor/scalable/apps/pix.svg
%{_datadir}/metainfo/org.kde.pix.appdata.xml
