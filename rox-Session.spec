%define _name ROX-Session
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Session is a really simple session manager
Summary(pl):	ROX-Session jest naprawdê prostym zarz±dc± sesji
Name:		rox-Session
Version:	0.1.24
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
# Source0-md5:	2eb49f8458c776b450d4ff0714efcd0b
URL:		http://rox.sourceforge.net/rox_session.php3
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _appsdir  %{_libdir}/ROX-apps

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
%setup -q -n %{_name}-%{version}

%build
%{_name}/AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform},Messages}

cd %{_name}
install App* Login *.sh Options.xml Styles \
	$RPM_BUILD_ROOT%{_appsdir}/%{_name}

install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/%{_name} $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install Messages/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/Login
%attr(755,root,root) %{_appsdir}/%{_name}/*sh
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Options.xml
%{_appsdir}/%{_name}/Styles
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/Messages
%dir %{_appsdir}/%{_name}
