%define	upstream_name    Digest-MD2
%define	upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl interface to the MD2 Algorithm	
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-MD2
Requires:	perl

%description
Digest-MD2 module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto
