Summary:	Prints a Linux system's font configuration
Summary(pl.UTF-8):	Wypisywanie konfiguracji fontów systemowych pod Linuksem
Name:		font-config-info
Version:	0.2
Release:	1
License:	ASL 2.0
Group:		Applications
Source0:	https://github.com/derat/font-config-info/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	e0e1bc3d2bf7fd3dca530e599c5037aa
URL:		https://github.com/derat/font-config-info
BuildRequires:	fontconfig-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
font-config-info is a tiny program that queries and prints a Linux
system's font configuration. It is intended to produce brief reports
that users can send to developers to aid in debugging font rendering
issues.

%description -l pl.UTF-8
font-config-info to mały program odpytujący i wypisujący konfigurację
fontów systemowych pod Linuksem. Ma za zadanie tworzyć krótkie
raporty, które użytkownicy mogą wysyłać programistom w celu pomocy
przy diagnostyce problemów z renderowaniem fontów.

%prep
%setup -qc
mv %{name}-*/* .

%{__sed} -i -e 's/gcc -Wall/%{__cc} %{rpmcflags}/' Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/font-config-info
