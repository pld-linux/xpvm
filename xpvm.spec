Summary:	TCL/TK graphical frontend to monitor and manage a PVM cluster
Summary(pl):	Graficzny frontend TCL/TK do monitorowania i zarz±dzania klastrem PVM
Name:		xpvm
Version:	1.2.5
Release:	6
License:	Free
Group:		X11/Development/Tools
Source0:	http://www.netlib.org/pvm3/xpvm/XPVM.src.%{version}.tgz
# Source0-md5:	7b20143cb2ff61e3cb28baf8f9cb2770
Patch0:		%{name}.patch
Patch1:		%{name}-help-path.patch
Patch2:		%{name}-noenv.patch
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pvm-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:	pvm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pvm-gui

%define 	_xpvm_root	%{_datadir}/xpvm

%description
Xpvm is a TCL/TK based tool that allows full manageability of the PVM
cluster as well as the ability to monitor cluster performance.

%description -l pl
Xpvm to bazuj±ce na TCL/TK narzêdzie pozwalaj±ce zarz±dzaæ klastrem
PVM, a tak¿e monitorowaæ jego wydajno¶æ.

%prep
%setup -q -n xpvm
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
XPCFLOPTS="%{rpmcflags} -DXPVMROOT=\\\"%{_xpvm_root}\\\""

XPVM_ROOT=`pwd` \
%{__make} \
	CFLOPTS="$XPCFLOPTS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xpvm_root},%{_bindir}}

%ifarch alpha
install src/LINUXALPHA/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch ppc
install src/LINUXPPC/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch sparc sparc64 sparcv9
install src/LINUXSPARC/xpvm $RPM_BUILD_ROOT%{_bindir}
%endif
%ifnarch alpha ppc sparc sparc64 sparcv9
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
