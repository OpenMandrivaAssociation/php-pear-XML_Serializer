%define		_class		XML
%define		_subclass	Serializer
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.20.2
Release:	1
Summary:	Class to build XML documents from data structures
License:	BSD
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_Serializer/
Source0:	http://download.pear.php.net/package/XML_Serializer-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
%{upstream_name} serializes complex data structures like arrays or objects
as XML documents. This class helps you generating any XML document you
require without the need for DOM.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.19.2-6mdv2011.0
+ Revision: 667695
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19.2-5mdv2011.0
+ Revision: 607168
- rebuild

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.2-4mdv2010.1
+ Revision: 464963
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.19.2-3mdv2010.0
+ Revision: 426676
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.19.2-2mdv2009.1
+ Revision: 368304
- Rebuild
- Update license
- Update php pear XML_Serializer to 0.19.2 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.18.0-6mdv2009.1
+ Revision: 321939
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.18.0-5mdv2009.0
+ Revision: 224894
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.18.0-4mdv2008.1
+ Revision: 178564
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.18.0-3mdv2008.0
+ Revision: 64200
- rebuild


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.18.0-2mdv2007.0
+ Revision: 81271
- Import php-pear-XML_Serializer

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.18.0-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 0.18.0-1mdk
- 0.18.0
- fix deps

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-2mdk
- rebuild

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-1mdk
- 0.15.0
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 0.14.1-2mdk
- Updated

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 0.14.1-1mdk
- First mdk package


