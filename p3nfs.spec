Summary:	A program for mount Symbian OS file system using Bluetooth, IrDA and NFS
Summary(pl):	Program do montowania systemu plik�w Symbian OS poprzez Blootooth, IrDA i NFS
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

%description -l pl
P3nfsd to program do komunikacji mi�dzy Symbianem (Psion/Nokia/Sony
Ericsson itp.) a Uniksem/Linuksem. Pozwala montowa� systemy plik�w
telefon�w lub PDA na maszynie uniksowej. Oznacza to, �e wszystkie
systemy plik�w telefon�w/PDA wida� jako systemy plik�w na maszynie
uniksowej i mo�na kopiowa� i modyfikowa� dowolny plik na telefonie/PDA
przy u�yciu swoich ulubionych narz�dzi na maszynie uniksowej.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
