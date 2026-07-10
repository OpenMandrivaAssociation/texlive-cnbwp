%global tl_name cnbwp
%global tl_revision 69910

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2024.02
Release:	%{tl_revision}.1
Summary:	Typeset working papers of the Czech National Bank
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cnbwp
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cnbwp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cnbwp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports proper formatting of Working Papers of the Czech
National Bank (WP CNB). The package was developed for CNB but it is also
intended for authors from outside CNB.

