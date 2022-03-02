%{?nodejs_find_provides_and_requires}
Name:                nodejs-has-symbols
Version:             1.0.0
Release:             2
Summary:             Determine if the JS environment has Symbol support
License:             MIT
URL:                 https://www.npmjs.com/package/has-symbols
Source0:             https://registry.npmjs.org/has-symbols/-/has-symbols-%{version}.tgz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(tape)
%description
Determine if the JS environment has Symbol support. Supports spec, or shams.

%prep
%autosetup -n package
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/has-symbols
cp -pr package.json index.js shams.js %{buildroot}%{nodejs_sitelib}/has-symbols
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%__nodejs test
%__nodejs --harmony  test
%__nodejs test/shams/get-own-property-symbols.js
%__nodejs test/shams/core-js.js

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{nodejs_sitelib}/has-symbols

%changelog
* Thu Mar 01 2022 Yongqing chen <chenyongqingdl@gmail.com> - 1.0.0-2
- Delete --es-staging option 

* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.0.0-1
- Package init

