%define upstream_name Digest-MD2
%define upstream_version 2.03

Summary:	Perl interface to the MD2 Algorithm	
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	20
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
Provides:	perl-MD2

%description
Digest-MD2 module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto

