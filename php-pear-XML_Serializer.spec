%define	_class	XML
%define	_subclass	Serializer
%define	modname	%{_class}_%{_subclass}

Summary:	Class to build XML documents from data structures
Name:		php-pear-%{modname}
Version:	0.21.0
Release:	2
License:	BSD
Group:		Development/PHP
Url:		http://pear.php.net/package/XML_Serializer/
Source0:	http://download.pear.php.net/package/XML_Serializer-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
%{modname} serializes complex data structures like arrays or objects
as XML documents. This class helps you generating any XML document you
require without the need for DOM.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/doc
%doc %{modname}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/doc/XML_Serializer/*
%{_datadir}/pear/test/XML_Serializer/tests/*
