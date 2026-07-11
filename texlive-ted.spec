%global tl_name ted
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.06
Release:	%{tl_revision}.1
Summary:	A (primitive) token list editor
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ted
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Just like sed is a stream editor, ted is a token list editor. Actually,
it is not as powerful as sed, but its main feature is that it really
works with tokens, not only characters. The ted package provides two
user macros: \Substitute and \ShowTokens. The first is maybe the most
useful: it performs substitutions in token lists (even inside braces).
The second displays each token of the list (one per line) with its
catcode (in the list, not just the current one), and can be useful for
debugging or for TeX learners. Ted is designed to work well even if
strange tokens (that is, unusual {charcode, catcode} pairs or tokens
with a confusing meaning) occur in the list.

