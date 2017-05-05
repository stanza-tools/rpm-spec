%global uversion 0_11_10
%global sname lstanza
%global stanza_data %{_datadir}/%{name}/%{uversion}
%global stanza_libs %{_libdir}/%{name}/%{uversion}

Name:    lbstanza
Version: 0.11.10
Release: 0.1%{?dist}
Summary: L.B. Stanza Programming Language 
URL:     http://lbstanza.org
License: BSD
Source0: http://lbstanza.org/resources/stanza/%{sname}_%{uversion}.zip 

%description
L.B. Stanza (Stanza for short) is an optionally-typed general-purpose language. 

%prep
%autosetup -c %{sname}_%{uversion}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{stanza_data}/{compiler,core,runtime}
mkdir -p %{buildroot}%{stanza_libs}/{pkgs,fast-pkgs}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d

install -p -m 755 pkgs/*      %{buildroot}/%{stanza_libs}/pkgs
install -p -m 755 fast-pkgs/* %{buildroot}/%{stanza_libs}/fast-pkgs
install -p -m 755 compiler/*  %{buildroot}/%{stanza_data}/compiler
install -p -m 755 core/*      %{buildroot}/%{stanza_data}/core
install -p -m 755 runtime/*   %{buildroot}/%{stanza_data}/runtime
install -p -m 555 License.txt %{buildroot}/%{stanza_data}/
install -p -m 755 stanza      %{buildroot}%{_bindir}

# Write the config file to the conventional location
cat << EOF > %{buildroot}%{_sysconfdir}/.stanza
install-dir = "%{stanza_data}"
platform = linux
pkg-dirs = ("%{stanza_libs}/pkgs")
fast-pkg-dirs = ("%{stanza_libs}/fast-pkgs")
EOF

# Add the needed environment variable and a few extra
cat << EOF > %{buildroot}%{_sysconfdir}/profile.d/stanza.sh
export STANZA_CONFIG=%{_sysconfdir}
export STANZA_FILE=$STANZA_CONFIG/.stanza
export STANZA_PKGS=%{stanza_libs}/pkgs
export STANZA_FAST_PKGS=%{stanza_libs}/fast-pkgs
EOF

# Clean out some random backup files
find %{buildroot} -name '*~' -exec rm {} \;

%check
%{buildroot}%{_bindir}/stanza version

%files
%doc               examples/calculus.stanza
%doc               examples/helloworld.stanza
%doc               examples/sort.stanza
%doc               examples/triforce.stanza
%license           License.txt
%config(noreplace) %{_sysconfdir}/.stanza
%config(noreplace) %{_sysconfdir}/profile.d/stanza.sh
                   %{_bindir}/*
                   %{_datadir}/*
                   %{_libdir}/*


%changelog
* Fri May 05 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.10-0.1
- Another assumed bugfix of 0.11.8
* Fri May 05 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.9-0.1
- Update to latest experimental release
- Unknown changes though expected to be a bugfix of 0.11.8
* Sun Apr 16 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.8-0.1
- A fairly major restructuring of the mid-end to allow for more aggressive inlining optimizations
* Sun Apr 16 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-3
- Separate data and libs into per-version folders
* Sun Apr 16 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-2
- Refactor installation
- Add more environment variables
- Add some comments
* Sat Feb 18 2017 Jake Russo <madcap.russo@gmail.com> - 0.11.7-1
- Initial rpm build


