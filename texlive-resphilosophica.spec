%global tl_name resphilosophica
%global tl_revision 79936
%global tl_version 1.40

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Typeset articles for the journal Res Philosophica
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/resphilosophica
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resphilosophica.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides a class for typesetting articles for the journal Res
Philosophica. This work was commissioned by the Saint Louis University.

