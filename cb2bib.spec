Name:		cb2bib
Summary:	A tool for extracting bibliographic references
Version:	1.4.7
License:	GPL
Release:	1
Group:		Publishing	
Source0:	http://www.molspaces.com/dl/progs/%{name}-%{version}.tar.gz
Url:		http://www.molspaces.com/cb2bib
BuildRequires:	cmake

%description
From clipboard to BibTeX: A tool for rapidly extracting unformatted bibliographic
references from email alerts, journal web pages, and PDF files.

The cb2Bib facilitates the capture of single references from unformatted and non
standard sources. Output references are written in BibTeX. Article files can be
easily linked and renamed by dragging it onto the cb2Bib window. Additionally, it
permits editing and browsing BibTeX files, searching references and the contents
of linked files, and cite them into document editors.

%prep
%setup -q

%build
%cmake
%make

%install
cd build/
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
