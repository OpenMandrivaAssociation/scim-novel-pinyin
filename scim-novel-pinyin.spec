%define oname novel-pinyin

Name:           scim-%{oname}
BuildRequires:  gtk2-devel scim-devel intltool gcc-c++ 
BuildRequires:  db-devel
Summary:        Novel Pinyin
Version:        0.2.4
Release:        %mkrel 3
License:        GPLv2+
Group:          System/Internationalization
Url:            http://novel-pinyin.sourceforge.net
Source0:        http://kent.dl.sourceforge.net/sourceforge/novel-pinyin/novel-pinyin-%{version}.tar.gz
Requires:	scim-client = %{scim_api}
Provides:	%{oname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A Simplified Chinese Sentence-Based Pinyin Input Method Engine Based On Markov Model. 

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/IMEngine/novel_pinyin.*a
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/SetupUI/novel-pinyin-imengine-setup.*a

%find_lang %oname

%files -f %oname.lang
%defattr(-, root, root)
%{scim_plugins_dir}/IMEngine/novel_pinyin.so
%{scim_plugins_dir}/SetupUI/novel-pinyin-imengine-setup.so
%{_datadir}/scim/icons/novel-pinyin.png
%dir %{_datadir}/scim/novel-pinyin
%{_datadir}/scim/novel-pinyin/bigram.db
%{_datadir}/scim/novel-pinyin/gb_char.bin
%{_datadir}/scim/novel-pinyin/gbk_char.bin
%{_datadir}/scim/novel-pinyin/pinyin_index.bin
%{_datadir}/scim/novel-pinyin/special_table
