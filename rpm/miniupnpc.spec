# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       miniupnpc

# >> macros
# << macros

Summary:    an implementation of a UPnP IGD + NAT-PMP / PCP gateway
Version:    2.0.20170509
Release:    0
Group:      Applications/Internet
License:    BSD-3-Clause
URL:        http://miniupnp.tuxfamily.org/
Source0:    %{name}-%{version}.tar.gz
Source100:  miniupnpc.yaml
Source101:  miniupnpc-rpmlintrc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake

%description

%{summary}.

%if "%{?vendor}" == "chum"
PackageName: MiniUPnP
Type: console-application
PackagerName: nephros
DeveloperName: Thomas Bernard
Custom:
  Repo: https://github.com/nephros/transmission
Url:
  Homepage: %{url}
  Help: http://miniupnp.tuxfamily.org/forum/
  Bugtracker: https://github.com/miniupnp/miniupnp/issues
%endif


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.
%if "%{?vendor}" == "chum"
PackageName: %{name}
Type: console-application
PackagerName: nephros
DeveloperName: Thomas Bernard
Custom:
  Repo: https://github.com/nephros/transmission
Url:
  Homepage: %{url}
  Help: http://miniupnp.tuxfamily.org/forum/
  Bugtracker: https://github.com/miniupnp/miniupnp/issues
%endif


%prep
%setup -q -n %{name}-%{version}/%{name}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DUPNPC_BUILD_STATIC=FALSE \
    -DUPNPC_BUILD_TESTS=FALSE

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/*.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/*.so
%{_includedir}/*'
# << files devel
