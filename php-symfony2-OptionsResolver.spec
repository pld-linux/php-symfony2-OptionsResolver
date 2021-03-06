%define		package	OptionsResolver
%define		php_min_version 5.3.9
Summary:	Symfony2 OptionsResolver Component
Name:		php-symfony2-OptionsResolver
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	fd95e86294744a4d85321532a3b2d6ac
URL:		http://symfony.com/doc/2.7/components/options_resolver.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OptionsResolver Component helps you configure objects with option
arrays. It supports default values, option constraints and lazy
options.

%prep
%setup -q -n options-resolver-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/OptionsResolver
%{php_data_dir}/Symfony/Component/OptionsResolver/*.php
%{php_data_dir}/Symfony/Component/OptionsResolver/Exception
