%global uversion 0_11_7
%global lstz lstanza

Name:    lbstanza
Version: 0.11.7
Release: 1%{?dist}
Summary: L.B. Stanza Programming Language 
URL:     http://lbstanza.org
License: BSD
Source0: http://lbstanza.org/resources/stanza/%{lstz}_%{uversion}.zip 

%description
L.B. Stanza (Stanza for short) is an optionally-typed general-purpose language. 

%prep
%autosetup -c %{lstz}_%{uversion}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

mv pkgs fast-pkgs %{buildroot}%{_libdir}/%{name}/
mv compiler core runtime %{buildroot}%{_datadir}/%{name}/
mv stanza %{buildroot}%{_bindir}
cp License.txt %{buildroot}%{_datadir}/%{name}/

cat << EOF > %{buildroot}%{_sysconfdir}/.stanza
install-dir = "%{_datadir}/%{name}"
platform = linux
pkg-dirs = ("%{_libdir}/%{name}/pkgs")
fast-pkg-dirs = ("%{_libdir}/%{name}/fast-pkgs")
EOF

cat << EOF > %{buildroot}%{_sysconfdir}/profile.d/stanza.sh
export STANZA_CONFIG=%{_sysconfdir}
export STANZA_FILE=%{_sysconfdir}/.stanza
EOF

find %{buildroot} -name '*~' -exec rm {} \;

%check
%{buildroot}%{_bindir}/stanza version

%files
%doc               examples/calculus.stanza
%doc               examples/fibers.stanza
%doc               examples/helloworld.stanza
%doc               examples/sort.stanza
%doc               examples/table.stanza
%doc               examples/triforce.stanza
%license           License.txt
%config(noreplace) %{_sysconfdir}/.stanza
%config(noreplace) %{_sysconfdir}/profile.d/stanza.sh
                   %{_bindir}/*
                   %{_datadir}/*
                   %{_libdir}/*


%changelog
* Sat Feb 18 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-1
- Initial rpm build


