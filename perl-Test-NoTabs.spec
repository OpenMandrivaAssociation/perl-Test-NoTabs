%define upstream_name    Test-NoTabs
%define upstream_version 1.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Check the presence of tabs in your project
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc) for the presence of tabs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 685626
- update to new version 1.1

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2
+ Revision: 656827
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 572833
- import perl-Test-NoTabs

