Name:		texlive-resphilosophica
Version:	75163
Release:	1
Summary:	Typeset articles for the journal Res Philosophica
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/resphilosophica
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/resphilosophica
%{_texmfdistdir}/tex/latex/resphilosophica
%doc %{_texmfdistdir}/doc/latex/resphilosophica
#- source
%doc %{_texmfdistdir}/source/latex/resphilosophica

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
