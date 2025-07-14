Summary:	A program for mount Symbian OS file system using Bluetooth, IrDA and NFS
Summary(pl.UTF-8):	Program do montowania systemu plików Symbian OS poprzez Blootooth, IrDA i NFS
Name:		p3nfs
Version:	5.19
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.koeniglich.de/packages/%{name}-%{version}.tar.gz
# Source0-md5:	15ac5e1b44a7c7f53369846c3cfe4de4
Patch0:		%{name}-configure.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.koeniglich.de/p3nfs.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
P3nfsd is a Symbian (Psion/Nokia/Sony-Ericsson/etc) to UNIX/Linux
communication program. It allows you to mount the file systems of the
Phone/PDA on your UNIX machine. This means that you see all the
filesystems of the Phone/PDA as a filesystem on your UNIX machine, and
you can copy/backup/edit any file on the Phone/PDA with your preferred
tools on the UNIX machine.

%description -l pl.UTF-8
P3nfsd to program do komunikacji między Symbianem (Psion/Nokia/Sony
Ericsson itp.) a Uniksem/Linuksem. Pozwala montować systemy plików
telefonów lub PDA na maszynie uniksowej. Oznacza to, że wszystkie
systemy plików telefonów/PDA widać jako systemy plików na maszynie
uniksowej i można kopiować i modyfikować dowolny plik na telefonie/PDA
przy użyciu swoich ulubionych narzędzi na maszynie uniksowej.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_sbindir}/p3nfsd
%{_mandir}/p3nfsd.1*
