%global uversion 0_11_7
%global lstz lstanza

Name:    lbstanza
Version: 0.11.7
Release: 2%{?dist}
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
mkdir -p %{buildroot}%{_libdir}/%{name}/pkgs
mkdir -p %{buildroot}%{_libdir}/%{name}/fast-pkgs
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

install -p -m 755 pkgs/* %{buildroot}%{_libdir}/%{name}/pkgs
install -p -m 755 fast-pkgs/* %{buildroot}%{_libdir}/%{name}/fast-pkgs
install -p -m 755 compiler/* %{buildroot}%{_datadir}/%{name}/compiler
install -p -m 755 core/* %{buildroot}%{_datadir}/%{name}/core
install -p -m 755 runtime/* %{buildroot}%{_datadir}/%{name}/runtime
install -p -m 755 stanza %{buildroot}%{_bindir}
install -p -m 555 License.txt %{buildroot}%{_datadir}/%{name}/

# Write the config file to the conventional location
cat << EOF > %{buildroot}%{_sysconfdir}/.stanza
install-dir = "%{_datadir}/%{name}"
platform = linux
pkg-dirs = ("%{_libdir}/%{name}/pkgs")
fast-pkg-dirs = ("%{_libdir}/%{name}/fast-pkgs")
EOF

# Add the needed environment variable and a few extra
cat << EOF > %{buildroot}%{_sysconfdir}/profile.d/stanza.sh
export STANZA_CONFIG=%{_sysconfdir}
export STANZA_FILE=$STANZA_CONFIG/.stanza
export STANZA_PKGS=%{_libdir}/%{name}/pkgs
export STANZA_FAST_PKGS=%{_libdir}/%{name}/fast-pkgs
EOF

# Clean out some random backup files
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
* Sun Apr 16 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-2
- Refactor installation
- Add more environment variables
- Add some comments
* Sat Feb 18 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-1
- Initial rpm build


