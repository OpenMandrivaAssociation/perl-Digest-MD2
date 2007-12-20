%define	name	perl-Digest-MD2
%define	real_name Digest-MD2
%define	version	2.03
%define	release	%mkrel 4

Summary:	Perl interface to the MD2 Algorithm	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/GAAS/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Provides:	perl-MD2
Requires:	perl

%description
Digest-MD2 module for perl.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto


