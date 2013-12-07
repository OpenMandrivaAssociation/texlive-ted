# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ted
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-ted
Version:	1.06
Release:	6
Summary:	A (primitive) token list editor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ted
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ted.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Just like sed is a stream editor, ted is a token list editor.
Actually, it is not as powerfull as sed, but its main feature
is that it really works with tokens, not only characters. The
ted package provides two user macros: \Substitute and
\ShowTokens. The first is maybe the most useful: it performs
substitutions in token lists (even inside braces). The second
displays each token of the list (one per line) with its catcode
(in the list, not just the current one), and can be useful for
debugging or for TeX learners. Ted is designed to work well
even if strange tokens (that is, unusual {charcode, catcode}
pairs or tokens with a confusing meaning) occur in the list.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ted/ted.sty
%doc %{_texmfdistdir}/doc/latex/ted/README
%doc %{_texmfdistdir}/doc/latex/ted/ted-fr.pdf
%doc %{_texmfdistdir}/doc/latex/ted/ted.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ted/ted.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.06-2
+ Revision: 756551
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.06-1
+ Revision: 719664
- texlive-ted
- texlive-ted
- texlive-ted

