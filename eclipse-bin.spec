
%bcond_without	ix86	# don't download ix86 source
%bcond_without	x86_64	# don't download x86_64 source

Summary:	Eclipse - an open extensible IDE
Summary(pl.UTF-8):	Eclipse - otwarte, rozszerzalne środowisko programistyczne
Name:		eclipse-bin
Version:	3.5.1
Release:	2
License:	EPL v1.0
Group:		Development/Tools
%if %{with ix86}
Source0:	ftp://eclipse.bluage.com/technologySR1/eclipse-jee-galileo-SR1-linux-gtk.tar.gz
# Source0-md5:	8c1e4f8cc967cfc847ddd8150407d8cd
%endif
%if %{with x86_64}
Source1:	ftp://eclipse.bluage.com/technologySR1/eclipse-jee-galileo-SR1-linux-gtk-x86_64.tar.gz
# Source1-md5:	f7a468512be47b9119ce1b92d25d9c7e
%endif
Source2:	eclipse.desktop
Source3:	eclipse.ini
URL:		http://www.eclipse.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	ant
Requires:	jdk >= 1.4
Obsoletes:	eclipse-SDK
Obsoletes:	eclipse
Provides:	eclipse = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86\\|athlon\\|pentium/x86/;s/amd64/x86_64/')
%define		no_install_post_chrpath		1

# list of script capabilities (regexps) not to be used in Provides
%define		_noautoprov			libcairo.so.2

%description
Eclipse is a kind of universal tool platform - an open extensible IDE
for anything and nothing in particular.

%description -l pl.UTF-8
Eclipse to rodzaj uniwersalnej platformy narzędziowej - otwarte,
rozszerzalne IDE (zintegrowane środowisko programistyczne) do
wszystkiego i niczego w szczególności.

%prep
%ifarch %{ix86}
%setup -q -T -c -a0
%endif
%ifarch %{x8664}
%setup -q -T -c -a1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/eclipse,%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}/eclipse}

cd eclipse
cp -a features p2 configuration plugins \
      libcairo-swt.so eclipse \
      $RPM_BUILD_ROOT%{_libdir}/eclipse

install -p icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/eclipse-icon.xpm

install -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/eclipse.ini

ln -s %{_libdir}/eclipse/eclipse $RPM_BUILD_ROOT%{_bindir}
ln -s %{_sysconfdir}/eclipse/eclipse.ini $RPM_BUILD_ROOT%{_libdir}/eclipse/eclipse.ini

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc eclipse/{about_files,readme,*html}
%dir %{_libdir}/eclipse
%{_libdir}/eclipse/features
%{_libdir}/eclipse/p2
%{_libdir}/eclipse/configuration
%{_libdir}/eclipse/plugins
%{_libdir}/eclipse/eclipse.ini
%{_desktopdir}/eclipse.desktop
%{_pixmapsdir}/eclipse-icon.xpm
%config(noreplace) %verify(not md5 mtime size) %attr(644,root,root) %{_sysconfdir}/eclipse
%attr(755,root,root) %{_libdir}/eclipse/libcairo-swt.so
%attr(755,root,root) %{_libdir}/eclipse/eclipse
%attr(755,root,root) %{_bindir}/eclipse
