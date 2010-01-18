# TODO:
# - make use of eclipse-swt package

%define		ver_major	3.5
%define		buildid	20090920-1017
Summary:	Eclipse - an open extensible IDE
Summary(pl.UTF-8):	Eclipse - otwarte, rozszerzalne środowisko programistyczne
Name:		eclipse-bin
Version:	%{ver_major}
Release:	2
License:	EPL v1.0
Group:		Development/Tools
Source0:	ftp://eclipse.bluage.com/technologySR1/eclipse-jee-galileo-SR1-linux-gtk.tar.gz
# NoSource0-md5:	8c1e4f8cc967cfc847ddd8150407d8cd
Source1:	ftp://eclipse.bluage.com/technologySR1/eclipse-jee-galileo-SR1-linux-gtk-x86_64.tar.gz
# NoSource1-md5:	f7a468512be47b9119ce1b92d25d9c7e
NoSource:	0
NoSource:	1
URL:		http://www.eclipse.org/
BuildRequires:	ant >= 1.6.1
BuildRequires:	ant-apache-regexp
BuildRequires:	jdk >= 1.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
Requires:	ant
Requires:	jdk >= 1.4
Obsoletes:	eclipse-SDK
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
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
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

cp -a eclipse ${_libdir}/eclipse
ln -s ${_libdir}/eclipse/eclipse $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/eclipse
%attr(755,root,root) %{_bindir}/eclipse
