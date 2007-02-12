Summary:	Tcl/Tk graphical frontend to monitor and manage a PVM cluster
Summary(pl.UTF-8):	Graficzny frontend Tcl/Tk do monitorowania i zarządzania klastrem PVM
Name:		xpvm
Version:	1.2.5
Release:	7
License:	Free
Group:		X11/Development/Tools
Source0:	http://www.netlib.org/pvm3/xpvm/XPVM.src.%{version}.tgz
# Source0-md5:	7b20143cb2ff61e3cb28baf8f9cb2770
Patch0:		%{name}.patch
Patch1:		%{name}-help-path.patch
Patch2:		%{name}-noenv.patch
URL:		http://www.netlib.org/pvm3/xpvm/
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pvm-devel
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:	pvm
Obsoletes:	pvm-gui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_xpvm_root	%{_datadir}/xpvm

%description
Xpvm is a Tcl/Tk based tool that allows full manageability of the PVM
cluster as well as the ability to monitor cluster performance.

%description -l pl.UTF-8
Xpvm to bazujące na Tcl/Tk narzędzie pozwalające zarządzać klastrem
PVM, a także monitorować jego wydajność.

%prep
%setup -q -n xpvm
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
XPCFLOPTS="%{rpmcflags} -DXPVMROOT=\\\"%{_xpvm_root}\\\""

XPVM_ROOT=`pwd` \
%{__make} \
	CFLOPTS="$XPCFLOPTS" \
	XLIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xpvm_root},%{_bindir}}

%ifarch alpha
install src/LINUXALPHA/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch %{x8664}
install src/LINUX64/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch ppc
install src/LINUXPPC/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch sparc sparc64 sparcv9
install src/LINUXSPARC/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifnarch alpha %{x8664} ppc sparc sparc64 sparcv9
install src/LINUX/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
install *.tcl $RPM_BUILD_ROOT%{_xpvm_root}
sed -e "s!@XPVMROOT@!%{_xpvm_root}!" xpvm.tcl >$RPM_BUILD_ROOT%{_xpvm_root}/xpvm.tcl
cp -rf src/xbm $RPM_BUILD_ROOT%{_xpvm_root}
cp -rf src/help $RPM_BUILD_ROOT%{_xpvm_root}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xpvm
%{_xpvm_root}
