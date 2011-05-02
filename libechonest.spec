%define major 1.1
%define libname %mklibname echonest %major
%define develname %mklibname -d echonest

Name: libechonest
Version: 1.1.1
Release: %mkrel 2
Summary: C++ wrapper for the Echo Nest API
Group: System/Libraries
License: GPLv2+
URL: https://projects.kde.org/projects/playground/libs/libechonest
Source0: http://pwsp.cleinias.com/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qjson-devel
BuildRequires: qt4-devel
BuildRequires: cmake

%description
libechonest is a collection of C++/Qt classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package -n %{libname}
Summary: Shared libraries files for %{name}
Group: System/Libraries

%description -n %{libname}
libechonest is a collection of C++/Qt classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}
Provides: echonest-devel = %{version}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake -DECHONEST_BUILD_TESTS=OFF
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/echonest
%{_libdir}/%{name}.so
