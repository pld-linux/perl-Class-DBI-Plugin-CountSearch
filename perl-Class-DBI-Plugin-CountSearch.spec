#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-Plugin-CountSearch
Summary:	Class::DBI::Plugin::CountSearch - get COUNT(*) results from the database with search functionality
Summary(pl):	Class::DBI::Plugin::CountSearch - pobieranie wynik�w COUNT(*) z bazy danych z mo�liwo�ci� wyszukiwania
Name:		perl-Class-DBI-Plugin-CountSearch
Version:	1.02
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	f030e7d98161a4f9c05bf53a36d9eb3b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds support for COUNT(*) results directly from the
database without having to load the records into an iterator or array.
It provides 'count_search' and 'count_search_like' which take
arguments exactly like Class::DBI::search().

%description -l pl
Ta wtyczka dodaje obs�ug� wynik�w COUNT(*) bezpo�rednio z bazy danych
bez potrzeby wczytywania rekord�w do iteratora lub tablicy. Udost�pnia
'count_search' i 'count_search_like' przyjmuj�ce dok�adnie takie
argumenty, jak Class::DBI::search().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/Plugin/CountSearch.pm
%{_mandir}/man3/*
