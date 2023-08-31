#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-redis
Version  : 5.3.7
Release  : 56
URL      : https://pecl.php.net/get/redis-5.3.7.tgz
Source0  : https://pecl.php.net/get/redis-5.3.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-redis-lib = %{version}-%{release}
Requires: php-redis-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
DESCRIPTION
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small.

%package lib
Summary: lib components for the php-redis package.
Group: Libraries
Requires: php-redis-license = %{version}-%{release}

%description lib
lib components for the php-redis package.


%package license
Summary: license components for the php-redis package.
Group: Default

%description license
license components for the php-redis package.


%prep
%setup -q -n redis-5.3.7
cd %{_builddir}/redis-5.3.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-redis
cp %{_builddir}/redis-%{version}/COPYING %{buildroot}/usr/share/package-licenses/php-redis/e2815bf94c6ff64afbc20d3403dc45ea5c73c6f0
cp %{_builddir}/redis-%{version}/liblzf/LICENSE %{buildroot}/usr/share/package-licenses/php-redis/9a0e277bb547589f33bbd1fc939e6057703a95ae
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/redis.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-redis/9a0e277bb547589f33bbd1fc939e6057703a95ae
/usr/share/package-licenses/php-redis/e2815bf94c6ff64afbc20d3403dc45ea5c73c6f0
