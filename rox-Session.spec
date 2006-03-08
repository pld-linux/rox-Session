%define _name ROX-Session
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Session is a really simple session manager
Summary(pl):	ROX-Session jest naprawdê prostym zarz±dc± sesji
Name:		rox-Session
Version:	0.27
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/rox-session-%{version}.tar.bz2
# Source0-md5:	15cb41c0bf8104a6a90021b1762b5712
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

%description -l pl
ROX-Session jest prostym w obs³udze zarz±dc± sesji. Jest to czê¶æ
projektu ROX, ale mo¿e byæ u¿ywany osobno. Gdy logujesz siê ustawia on
twoje biurko i uruchamia programy, o które zostanie poproszony.
ROX-Session pozwala skonfigurowaæ ró¿ne ustawienia, takie jak domy¶lna
czcionka, miganie kursora, czy zachowanie myszy. Pozwala on tak¿e na
wybranie zarz±dcy okien i na zmianê programu zarz±dzaj±cego oknami bez
wylogowywania siê.

%prep
%setup -q -n rox-session-%{version}

%build

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
%{_roxdir}/%{_name}/*.py[c,o]
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
