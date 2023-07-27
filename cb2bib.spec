%undefine _debugsource_packages

Name:		cb2bib
Summary:	A tool for extracting bibliographic references
Version:	2.0.1
License:	GPL
Release:	1
Group:		Publishing	
Source0:	http://www.molspaces.com/dl/progs/%{name}-%{version}.tar.gz
Url:		http://www.molspaces.com/cb2bib
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	qmake5
BuildRequires:	make
BuildRequires:	pkgconfig(liblz4)

%description
From clipboard to BibTeX: A tool for rapidly extracting unformatted bibliographic
references from email alerts, journal web pages, and PDF files.

The cb2Bib facilitates the capture of single references from unformatted and non
standard sources. Output references are written in BibTeX. Article files can be
easily linked and renamed by dragging it onto the cb2Bib window. Additionally, it
permits editing and browsing BibTeX files, searching references and the contents
of linked files, and cite them into document editors.

%prep
%autosetup -p1
# Looks like autoconf, but isn't -- it's actually a qmake wrapper
./configure \
	--prefix %{_prefix} \
	--enable-lz4

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
