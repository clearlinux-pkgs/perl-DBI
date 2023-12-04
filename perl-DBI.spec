#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBI
Version  : 1.643
Release  : 52
URL      : https://cpan.metacpan.org/authors/id/T/TI/TIMB/DBI-1.643.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TIMB/DBI-1.643.tar.gz
Summary  : 'Database independent interface for Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DBI-bin = %{version}-%{release}
Requires: perl-DBI-license = %{version}-%{release}
Requires: perl-DBI-man = %{version}-%{release}
Requires: perl-DBI-perl = %{version}-%{release}
Requires: perl(Params::Validate)
Requires: perl(RPC::PlClient)
Requires: perl(RPC::PlServer)
BuildRequires : buildreq-cpan

%description
# DBI - The Perl Database Interface.
[![Build Status](https://secure.travis-ci.org/perl5-dbi/dbi.png)](http://travis-ci.org/perl5-dbi/dbi/)

%package bin
Summary: bin components for the perl-DBI package.
Group: Binaries
Requires: perl-DBI-license = %{version}-%{release}

%description bin
bin components for the perl-DBI package.


%package dev
Summary: dev components for the perl-DBI package.
Group: Development
Requires: perl-DBI-bin = %{version}-%{release}
Provides: perl-DBI-devel = %{version}-%{release}
Requires: perl-DBI = %{version}-%{release}

%description dev
dev components for the perl-DBI package.


%package license
Summary: license components for the perl-DBI package.
Group: Default

%description license
license components for the perl-DBI package.


%package man
Summary: man components for the perl-DBI package.
Group: Default

%description man
man components for the perl-DBI package.


%package perl
Summary: perl components for the perl-DBI package.
Group: Default
Requires: perl-DBI = %{version}-%{release}

%description perl
perl components for the perl-DBI package.


%prep
%setup -q -n DBI-1.643
cd %{_builddir}/DBI-1.643

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBI
cp %{_builddir}/DBI-1.643/LICENSE %{buildroot}/usr/share/package-licenses/perl-DBI/63f2a1de14ec3f52b5ad62ffae99e3638db33472
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dbilogstrip
/usr/bin/dbiprof
/usr/bin/dbiproxy

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Bundle::DBI.3
/usr/share/man/man3/DBD::DBM.3
/usr/share/man/man3/DBD::File.3
/usr/share/man/man3/DBD::File::Developers.3
/usr/share/man/man3/DBD::File::HowTo.3
/usr/share/man/man3/DBD::File::Roadmap.3
/usr/share/man/man3/DBD::Gofer.3
/usr/share/man/man3/DBD::Gofer::Policy::Base.3
/usr/share/man/man3/DBD::Gofer::Policy::classic.3
/usr/share/man/man3/DBD::Gofer::Policy::pedantic.3
/usr/share/man/man3/DBD::Gofer::Policy::rush.3
/usr/share/man/man3/DBD::Gofer::Transport::Base.3
/usr/share/man/man3/DBD::Gofer::Transport::corostream.3
/usr/share/man/man3/DBD::Gofer::Transport::null.3
/usr/share/man/man3/DBD::Gofer::Transport::pipeone.3
/usr/share/man/man3/DBD::Gofer::Transport::stream.3
/usr/share/man/man3/DBD::Mem.3
/usr/share/man/man3/DBD::Proxy.3
/usr/share/man/man3/DBD::Sponge.3
/usr/share/man/man3/DBI.3
/usr/share/man/man3/DBI::Const::GetInfo::ANSI.3
/usr/share/man/man3/DBI::Const::GetInfo::ODBC.3
/usr/share/man/man3/DBI::Const::GetInfoReturn.3
/usr/share/man/man3/DBI::Const::GetInfoType.3
/usr/share/man/man3/DBI::DBD.3
/usr/share/man/man3/DBI::DBD::Metadata.3
/usr/share/man/man3/DBI::DBD::SqlEngine.3
/usr/share/man/man3/DBI::DBD::SqlEngine::Developers.3
/usr/share/man/man3/DBI::DBD::SqlEngine::HowTo.3
/usr/share/man/man3/DBI::Gofer::Execute.3
/usr/share/man/man3/DBI::Gofer::Request.3
/usr/share/man/man3/DBI::Gofer::Response.3
/usr/share/man/man3/DBI::Gofer::Serializer::Base.3
/usr/share/man/man3/DBI::Gofer::Serializer::DataDumper.3
/usr/share/man/man3/DBI::Gofer::Serializer::Storable.3
/usr/share/man/man3/DBI::Gofer::Transport::Base.3
/usr/share/man/man3/DBI::Gofer::Transport::pipeone.3
/usr/share/man/man3/DBI::Gofer::Transport::stream.3
/usr/share/man/man3/DBI::Profile.3
/usr/share/man/man3/DBI::ProfileData.3
/usr/share/man/man3/DBI::ProfileDumper.3
/usr/share/man/man3/DBI::ProfileDumper::Apache.3
/usr/share/man/man3/DBI::ProfileSubs.3
/usr/share/man/man3/DBI::ProxyServer.3
/usr/share/man/man3/DBI::PurePerl.3
/usr/share/man/man3/DBI::SQL::Nano.3
/usr/share/man/man3/DBI::Util::CacheMemory.3
/usr/share/man/man3/DBI::W32ODBC.3
/usr/share/man/man3/Win32::DBIODBC.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBI/63f2a1de14ec3f52b5ad62ffae99e3638db33472

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dbilogstrip.1
/usr/share/man/man1/dbiprof.1
/usr/share/man/man1/dbiproxy.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
