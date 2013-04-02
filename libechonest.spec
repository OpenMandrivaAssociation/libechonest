%define oname echonest

Summary:	Qt library for communicating with The Echo Nest
Name:		libechonest
Version:	2.0.1
Release:	3
License:	GPLv2
Group:		System/Libraries
Url:		https://projects.kde.org/projects/playground/libs/libechonest/
Source0:	http://pwsp.cleinias.com/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
Patch0:		libechonest-2.0.1-werror.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtTest)
BuildRequires:	doxygen

%description
Qt library for communicating with The Echo Nest.
It currently supports almost all of the features of the Echo Nest API,
including all API functions.

#--------------------------------------------------------------------

%define libechonest_major 2
%define libechonest %mklibname %{oname} %{libechonest_major}

%package -n %{libechonest}
Summary:	libechonest core library
Group:		System/Libraries

%description -n %{libechonest}
A c++/qt library to access the APIs provided by The Echo Nest.

%files -n %{libechonest}
%{_libdir}/libechonest.so.%{libechonest_major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %{oname}

%package -n %{develname}
Summary:	%{name} development files
URL:		http://pwsp.cleinias.com/libechonest_api/
Group:		Development/C++
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	lib%{oname}-devel = %{version}-%{release}
Requires:	%{libechonest} = %{version}-%{release}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}

%files -n %{develname}
%{_includedir}/%{oname}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

%changelog
* Thu Aug 02 2012 neoclust <neoclust> 2.0.1-1.mga3
+ Revision: 277767
- New version 2.0.1

* Fri Nov 25 2011 mikala <mikala> 1.2.1-1.mga2
+ Revision: 171851
- Update tarball to 1.2.1

  + tv <tv>
    - new release

* Sat Jul 16 2011 mikala <mikala> 1.1.8-2.mga2
+ Revision: 124625
- Add missing requires for -devel package
- Fix license

* Fri Jul 15 2011 mikala <mikala> 1.1.8-1.mga2
+ Revision: 124490
- Add lib%%{oname}-devel as Provides for devel package
- imported package libechonest

