Name:		texlive-cnbwp
Version:	32550
Release:	1
Summary:	Typeset working papers of the Czech National Bank
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cnbwp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnbwp.r32550.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnbwp.doc.r32550.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports proper formatting of Working Papers of the
Czech National Bank (WP CNB). The package was developed for CNB
but it is also intended for authors from outside CNB.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cnbwp/abbrvcnb.bst
%{_texmfdistdir}/makeindex/cnbwp/cnbindex.ist
%{_texmfdistdir}/tex/latex/cnbwp/cnbwp-manual.sty
%{_texmfdistdir}/tex/latex/cnbwp/cnbwp.cls
%{_texmfdistdir}/tex/latex/cnbwp/cnbwpsizes.clo
%doc %{_texmfdistdir}/doc/latex/cnbwp/README
%doc %{_texmfdistdir}/doc/latex/cnbwp/biblio.tex
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbpaper.pdf
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbpaper.tex
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbsample.bib
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbwp-manual-cs.pdf
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbwp-manual-cs.tex
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbwp-manual-en.pdf
%doc %{_texmfdistdir}/doc/latex/cnbwp/cnbwp-manual-en.tex
%doc %{_texmfdistdir}/doc/latex/cnbwp/graph18.eps
%doc %{_texmfdistdir}/doc/latex/cnbwp/graph18.gif
%doc %{_texmfdistdir}/doc/latex/cnbwp/graph18.jpg
%doc %{_texmfdistdir}/doc/latex/cnbwp/graph18.pdf
%doc %{_texmfdistdir}/doc/latex/cnbwp/graph18.png
%doc %{_texmfdistdir}/doc/latex/cnbwp/numtable.tex
%doc %{_texmfdistdir}/doc/latex/cnbwp/widematrix.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc %{buildroot}%{_texmfdistdir}
