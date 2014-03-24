#
# spec file for package 
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define app_name {{name}}
Name:           erlang-%{app_name}
Version:        {{version}}
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Release:        0
License:        {{license}}
Summary:        {{summary}}
Url:            {{url}}
Group:          Development/Libraries/Other
Source:         %{app_name}-%{version}.tar.bz2
Requires:       erlang
BuildRequires:  erlang erlang-rebar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
{{description}}

%prep
%setup -q -n %{app_name}-%{version}

%build
%rebar compile

%install
for dir in ebin include priv ; do
	mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}
	cp -r ${dir}/* %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}/
done

%check
%rebar eunit

%files
%defattr(-,root,root)
%doc {{doc}}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/include
%{erlang_libdir}/%{app_name}-%{app_ver}/include/*.hrl
%{erlang_libdir}/%{app_name}-%{app_ver}/priv

%changelog
