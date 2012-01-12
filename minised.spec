Summary:	minised - a smaller, cheaper, faster sed implementation
Summary(pl.UTF-8):	minised - mniejsza, tańsza, szybsza implementacja seda
Name:		minised
Version:	1.13
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.exactcode.de/oss/minised/%{name}-%{version}.tar.gz
# Source0-md5:	2a43b1bbf1654ef7fab9d8c4f6c979a1
URL:		http://www.exactcode.de/site/open_source/minised/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
minised is a minimalistic and fast sed implementation for small
systems and embedded use.

%description -l pl.UTF-8
minised jest minimalistyczną i szybką implementacją seda dla małych
systemów i zastosowań w systemach osadzonych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{,%{_bindir},%{_mandir}/man1}

install minised $RPM_BUILD_ROOT%{_bindir}
install minised.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
