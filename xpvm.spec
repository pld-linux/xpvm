Summary:	TCL/TK graphical frontend to monitor and manage a PVM cluster.
Name:		xpvm
Version:	1.2.5
Release:	1
Copyright:	free
Group:		X11/Development/Libraries
Source0:	http://www.netlib.org/pvm3/xpvm/XPVM.src.%{version}.tgz
Patch0:		xpvm.patch
Patch1:		xpvm-help-path.patch
Patch2:		xpvm-noenv.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	pvm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	XFree86-devel
Requires:	pvm
Obsoletes:	pvm-gui

%define _xpvm_root	%{_prefix}/X11R6/share/xpvm
%define _xbindir	%{_prefix}/X11R6/bin

%description
Xpvm is a TCL/TK based tool that allows full manageability of the PVM cluster
as well as the ability to monitor cluster performance.

%prep 
%setup -q -n xpvm
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
XPCFLOPTS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"
XPCFLOPTS="$XPCFLOPTS -DXPVMROOT=\\\"%{_xpvm_root}\\\""

XPVM_ROOT=`pwd` make CFLOPTS="$XPCFLOPTS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_xpvm_root} $RPM_BUILD_ROOT%{_xbindir}

# xpvm
install src/LINUX/xpvm $RPM_BUILD_ROOT%{_xbindir}
install *.tcl $RPM_BUILD_ROOT%{_xpvm_root}
sed -e "s!@XPVMROOT@!%{_xpvm_root}!" xpvm.tcl >$RPM_BUILD_ROOT%{_xpvm_root}/xpvm.tcl
cp -rf src/xbm $RPM_BUILD_ROOT%{_xpvm_root}
cp -rf src/help $RPM_BUILD_ROOT%{_xpvm_root}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/xpvm
%{_xpvm_root}
