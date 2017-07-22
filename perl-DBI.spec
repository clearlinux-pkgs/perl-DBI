#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBI
Version  : 1.636
Release  : 15
URL      : http://www.cpan.org/CPAN/authors/id/T/TI/TIMB/DBI-1.636.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/T/TI/TIMB/DBI-1.636.tar.gz
Summary  : 'Database independent interface for Perl'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-DBI-bin
Requires: perl-DBI-lib
Requires: perl-DBI-doc

%description
# DBI - The Perl Database Interface.
[![Build Status](https://secure.travis-ci.org/perl5-dbi/dbi.png)](http://travis-ci.org/perl5-dbi/dbi/)

%package bin
Summary: bin components for the perl-DBI package.
Group: Binaries

%description bin
bin components for the perl-DBI package.


%package doc
Summary: doc components for the perl-DBI package.
Group: Documentation

%description doc
doc components for the perl-DBI package.


%package lib
Summary: lib components for the perl-DBI package.
Group: Libraries

%description lib
lib components for the perl-DBI package.


%prep
%setup -q -n DBI-1.636

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/Bundle/DBI.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/DBM.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/ExampleP.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/File.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/File/Developers.pod
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/File/HowTo.pod
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/File/Roadmap.pod
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Policy/Base.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Policy/classic.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Policy/pedantic.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Policy/rush.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Transport/Base.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Transport/corostream.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Transport/null.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Transport/pipeone.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Gofer/Transport/stream.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/NullP.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Proxy.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBD/Sponge.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Changes.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Const/GetInfo/ANSI.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Const/GetInfo/ODBC.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Const/GetInfoReturn.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Const/GetInfoType.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/DBD.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/DBD/Metadata.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/DBD/SqlEngine.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/DBD/SqlEngine/Developers.pod
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/DBD/SqlEngine/HowTo.pod
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Execute.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Request.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Response.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Serializer/Base.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Serializer/DataDumper.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Serializer/Storable.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Transport/Base.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Transport/pipeone.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Gofer/Transport/stream.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Profile.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/ProfileData.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/ProfileDumper.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/ProfileDumper/Apache.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/ProfileSubs.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/ProxyServer.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/PurePerl.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/SQL/Nano.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Util/CacheMemory.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/Util/_accessor.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DBI/W32ODBC.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/Win32/DBIODBC.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/DBIXS.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/Driver.xst
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/Driver_xst.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/dbd_xsh.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/dbi_sql.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/dbipport.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/dbivport.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/dbixs_rev.h
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/dbixs_rev.pl

%files bin
%defattr(-,root,root,-)
/usr/bin/dbilogstrip
/usr/bin/dbiprof
/usr/bin/dbiproxy

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DBI/DBI.so
