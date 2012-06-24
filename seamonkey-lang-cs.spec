Summary:	Czech resources for SeaMonkey
Summary(pl):	Czeskie pliki j�zykowe dla SeaMonkeya
Name:		seamonkey-lang-cs
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.cs-CZ.langpack.xpi
# Source0-md5:	a1369d8f008ab942e829e1b63d6c520b
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-cs-CZ-0.9x.xpi
# Source1-md5:	062b8ff76ffea50045aa00c92c83b496
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Czech resources for SeaMonkey.

%description -l pl
Czeskie pliki j�zykowe dla SeaMonkeya.

%prep
%setup -q -c
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{CZ,cs-CZ,cs-unix}.jar \
	> lang-cs-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-cs-CZ.jar \
	>> lang-cs-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{CZ,cs-CZ,cs-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-cs-CZ.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-cs-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{defaults,searchplugins} $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/CZ.jar
%{_chromedir}/cs-CZ.jar
%{_chromedir}/cs-unix.jar
%{_chromedir}/enigmail-cs-CZ.jar
%{_chromedir}/lang-cs-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/CZ
%{_datadir}/seamonkey/defaults/pref/all-cs.js
%{_datadir}/seamonkey/defaults/profile/CZ
