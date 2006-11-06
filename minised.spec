# TODO: optflags
Summary:	minised - a smaller, cheaper, faster sed implementation
Summary(pl):	minised - mniejsza, tañsza, szybsza implementacja seda
Name:		minised
Version:	1.12
Release:	0.1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.exactcode.de/oss/minised/%{name}-%{version}.tar.gz
# Source0-md5:	ea532e8cb043618be69fd3e7fb9a36f3
URL:		http://www.exactcode.de/oss/minised/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
minised is a minimalistic and fast sed implementation for small
systems and embedded use.

%description -l pl
minised jest minimalistyczn± i szybk± implementacj± seda dla ma³ych
systemów i zastosowañ w systemach osadzonych.

%prep
%setup -q

%build
%{__make}

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
