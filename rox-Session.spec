%define _name ROX-Session
Summary:	ROX-Session - a really simple session manager
Summary(pl.UTF-8):   ROX-Session - naprawdę prosty zarządca sesji
Name:		rox-Session
Version:	0.28
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://heanet.dl.sourceforge.net/rox/rox-session-%{version}.tar.bz2
# Source0-md5:	d984f83c01f545d0d3d233de3cdf3ea2
URL:		http://rox.sourceforge.net/desktop/ROX-Session
Requires:	dbus >= 0.33
Requires:	python-dbus >= 0.33
Requires:	rox >= 2.3
Requires:	rox-Lib2 >= 1.9.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Session is a simple and easy to use session manager. It is part of
the ROX project, but can also be used on its own. It sets up your
desktop when you log in, and starts any applications you ask it to.
ROX-Session allows you to set various settings, such as the default
font, cursor blinking and mouse behaviour. It also allows you to
choose a window manager, and change between window managers without
logging out.

%description -l pl.UTF-8
ROX-Session jest prostym w obsłudze zarządcą sesji. Jest to część
projektu ROX, ale może być używany osobno. Gdy logujesz się ustawia on
twoje biurko i uruchamia programy, o które zostanie poproszony.
ROX-Session pozwala skonfigurować różne ustawienia, takie jak domyślna
czcionka, miganie kursora, czy zachowanie myszy. Pozwala on także na
wybranie zarządcy okien i na zmianę programu zarządzającego oknami bez
wylogowywania się.

%prep
%setup -q -n rox-session-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Messages,images}

cd %{_name}
install images/*.png $RPM_BUILD_ROOT%{_roxdir}/%{_name}/images
install Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages
install .DirIcon AppRun RunROX Login SetupPanel Styles browser $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install *.py *.xml $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/{Changes,DBUS-API,README}
%dir %{_roxdir}/%{_name}
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%attr(755,root,root) %{_roxdir}/%{_name}/Login
%attr(755,root,root) %{_roxdir}/%{_name}/RunROX
%attr(755,root,root) %{_roxdir}/%{_name}/SetupPanel
%attr(755,root,root) %{_roxdir}/%{_name}/browser
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/Styles
%{_roxdir}/%{_name}/*.py[co]
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/images
%dir %{_roxdir}/%{_name}/Messages
%lang(da) %{_roxdir}/%{_name}/Messages/da.gmo
%lang(de) %{_roxdir}/%{_name}/Messages/de.gmo
%lang(es) %{_roxdir}/%{_name}/Messages/es.gmo
%lang(fr) %{_roxdir}/%{_name}/Messages/fr.gmo
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%lang(ja) %{_roxdir}/%{_name}/Messages/ja.gmo
%lang(lt) %{_roxdir}/%{_name}/Messages/lt.gmo
%lang(nl) %{_roxdir}/%{_name}/Messages/nl.gmo
%lang(pt_BR) %{_roxdir}/%{_name}/Messages/pt_BR.gmo
%lang(ru) %{_roxdir}/%{_name}/Messages/ru.gmo
%lang(zh_CN) %{_roxdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_roxdir}/%{_name}/Messages/zh_TW.gmo
