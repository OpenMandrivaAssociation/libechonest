%define oname	echonest
%define major	2.0
%define libname %mklibname %{oname} %{major}
%define devname %mklibname -d %{oname}

Summary:	Qt library for communicating with The Echo Nest
Name:		libechonest
Version:	2.0.1
Release:	4
License:	GPLv2
Group:		System/Libraries
Url:		https://projects.kde.org/projects/playground/libs/libechonest/
Source0:	http://pwsp.cleinias.com/%{name}-%{version}.tar.bz2
Patch0:		libechonest-2.0.1-werror.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtTest)

%description
Qt library for communicating with The Echo Nest.
It currently supports almost all of the features of the Echo Nest API,
including all API functions.

%package -n %{libname}
Summary:	libechonest core library
Group:		System/Libraries
Obsoletes:	%{_lib}echonest2 < 2.0.1-4

%description -n %{libname}
A c++/qt library to access the APIs provided by The Echo Nest.

%package -n %{devname}
Summary:	%{name} development files
Group:		Development/C++
Provides:	%{oname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}

%prep
%setup -q
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libechonest.so.%{major}*

%files -n %{devname}
%{_includedir}/%{oname}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
