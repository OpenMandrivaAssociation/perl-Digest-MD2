%define	upstream_name    Digest-MD2
%define	upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-5mdv2012.0
+ Revision: 765187
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-4
+ Revision: 763703
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-3
+ Revision: 676525
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 555242
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.0
+ Revision: 407000
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.03-7mdv2009.0
+ Revision: 256681
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.03-5mdv2008.1
+ Revision: 152064
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 2.03-4mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 15 2007 Olivier Thauvin <nanardon@mandriva.org> 2.03-4mdv2007.0
+ Revision: 109319
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Digest-MD2

* Fri Jan 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-3mdk
- Rebuild

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.03-2mdk
- rebuild for new perl, clean up spec

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.03-1mdk
- 2.03.

