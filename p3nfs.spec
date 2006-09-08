Summary:	Symbian to UNIX/Linux communication program
Name:		p3nfs
Version:	5.19
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.koeniglich.de/packages/%{name}-%{version}.tar.gz
# Source0-md5:	15ac5e1b44a7c7f53369846c3cfe4de4
URL:		http://www.koeniglich.de/p3nfs.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
P3nfsd is a Symbian (Psion/Nokia/Sony-Ericsson/etc) to UNIX/Linux
communication program. It allows you to mount the file systems of the
Phone/PDA on your UNIX machine. This means that you see all the
filesystems of the Phone/PDA as a filesystem on your UNIX machine, and
you can copy/backup/edit any file on the Phone/PDA with your preferred
tools on the UNIX machine.

%prep
%setup -q

%build
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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
