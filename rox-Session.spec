%define _name ROX-Session
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Session is a really simple session manager
Summary(pl):	ROX-Session jest naprawd� prostym zarz�dc� sesji
Name:		rox-Session
Version:	0.1.25
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
# Source0-md5:	49c5ddeabdda9aa7c344bb260b0e73dd
URL:		http://rox.sourceforge.net/phpwiki/index.php/ROX-Session
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	python-dbus
Requires:	rox >= 2.2.0-2
Requires:	rox-Lib2 >= 1.9.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Session is a simple and easy to use session manager. It is part of
the ROX project, but can also be used on its own. It sets up your
desktop when you log in, and starts any applications you ask it to.
ROX-Session allows you to set various settings, such as the default
font, cursor blinking and mouse behaviour. It also allows you to
choose a window manager, and change between window managers without
logging out.

%description -l pl
ROX-Session jest prostym w obs�udze zarz�dc� sesji. Jest to cz��
projektu ROX, ale mo�e by� u�ywany osobno. Gdy logujesz si� ustawia on
twoje biurko i uruchamia programy, o kt�re zostanie poproszony.
ROX-Session pozwala skonfigurowa� r�ne ustawienia, takie jak domy�lna
czcionka, miganie kursora, czy zachowanie myszy. Pozwala on tak�e na
wybranie zarz�dcy okien i na zmian� programu zarz�dzaj�cego oknami bez
wylogowywania si�.

%prep
%setup -q -n %{_name}-%{version}

%build
%{_name}/AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,images,%{_platform},Messages}

cd %{_name}
install App* Login Options.xml RunROX SetupPanel Styles findrox.py interactive.py logout.py setup.py \
	$RPM_BUILD_ROOT%{_appsdir}/%{_name}

install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install images/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/images
install %{_platform}/%{_name} $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install Messages/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/{Changes,README}
%dir %{_appsdir}/%{_name}
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/Login
%attr(755,root,root) %{_appsdir}/%{_name}/RunROX
%attr(755,root,root) %{_appsdir}/%{_name}/SetupPanel
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%attr(755,root,root) %{_appsdir}/%{_name}/interactive.py
%attr(755,root,root) %{_appsdir}/%{_name}/setup.py
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Options.xml
%{_appsdir}/%{_name}/Styles
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/images
%{_appsdir}/%{_name}/Messages
%{_appsdir}/%{_name}/findrox.py
%{_appsdir}/%{_name}/logout.py
