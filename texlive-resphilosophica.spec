# revision 32874
# category Package
# catalog-ctan /macros/latex/contrib/resphilosophica
# catalog-date 2014-02-05 19:42:21 +0100
# catalog-license lppl1.3
# catalog-version 1.19
Name:		texlive-resphilosophica
Version:	1.31
Release:	1
Summary:	Typeset articles for the journal Res Philosophica
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/resphilosophica
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Th bundle provides a class for typesetting articles for the
journal Res Philosophica. Development was commissioned by Saint
Louis University.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/resphilosophica/resphilosophica.bst
%{_texmfdistdir}/tex/latex/resphilosophica/resphilosophica.cls
%doc %{_texmfdistdir}/doc/latex/resphilosophica/Makefile
%doc %{_texmfdistdir}/doc/latex/resphilosophica/README
%doc %{_texmfdistdir}/doc/latex/resphilosophica/resphilosophica.bib
%doc %{_texmfdistdir}/doc/latex/resphilosophica/resphilosophica.pdf
%doc %{_texmfdistdir}/doc/latex/resphilosophica/rpsample.bib
%doc %{_texmfdistdir}/doc/latex/resphilosophica/rpsample.pdf
%doc %{_texmfdistdir}/doc/latex/resphilosophica/rpsample.tex
#- source
%doc %{_texmfdistdir}/source/latex/resphilosophica/resphilosophica.dtx
%doc %{_texmfdistdir}/source/latex/resphilosophica/resphilosophica.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
