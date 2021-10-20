%define		kdeplasmaver	5.23.1
%define		qtver		5.9.0
%define		kpname		plasma-phone-components
%define		kf5ver		5.39.0

Summary:	plasma-phone-components
Name:		kp5-%{kpname}
Version:	5.23.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	dd105ecb8aeb23bb41dd21eaed5dcfff
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.0
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.82
BuildRequires:	kf5-kwayland-devel >= 5.82
BuildRequires:	kf5-plasma-framework-devel >= 5.82
BuildRequires:	kp5-kwin-devel >= 5.23.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
UI components for Plasma Phone.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwinwrapper
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mobilehomescreencomponents
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%{_datadir}/knotifications5/plasma_phone_components.notifyrc
%{_datadir}/metainfo/org.kde.phone.activities.appdata.xml
%{_datadir}/metainfo/org.kde.phone.krunner.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phoneshell.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.activities
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.krunner
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%{_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_libdir}/qt5/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/mm/qmldir
%{_datadir}/plasma/quicksettings/org.kde.plasma.airplanemode
%{_datadir}/plasma/quicksettings/org.kde.plasma.nightcolor
