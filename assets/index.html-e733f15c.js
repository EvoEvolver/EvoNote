import{_ as i,r as o,o as d,c,a as n,b as e,d as s,w as l,e as r}from"./app-1ed94c4d.js";const u={},p=n("h1",{id:"docinpy-documentation-just-in-your-python-code",tabindex:"-1"},[n("a",{class:"header-anchor",href:"#docinpy-documentation-just-in-your-python-code","aria-hidden":"true"},"#"),e(" DocInPy - Documentation just in your Python code")],-1),v=n("p",null,"DocInPy is a standard for putting documentation just in your Python code. It is proposed to provide another option other than the current standard of putting documentation in a separate file. Though it is not new to mix documentation with code, in DocInPy, you can also do",-1),m=n("ul",null,[n("li",null,"Adding sections to your functions and classes"),n("li",null,"Adding examples to your functions and classes")],-1),h=n("p",null,"We believe in this way we can provide much more context information to new contributors who are not familiar with the codebase. It is also important for AI-based agents to understand the codebase and develop it.",-1),b=n("h2",{id:"evonote",tabindex:"-1"},[n("a",{class:"header-anchor",href:"#evonote","aria-hidden":"true"},"#"),e(" EvoNote")],-1),k={href:"https://evonote.org/html/project_tree.html",target:"_blank",rel:"noopener noreferrer"},f=r(`<h2 id="how-to-use" tabindex="-1"><a class="header-anchor" href="#how-to-use" aria-hidden="true">#</a> How to use</h2><h3 id="sections" tabindex="-1"><a class="header-anchor" href="#sections" aria-hidden="true">#</a> Sections</h3><p>Putting sections in DocInPy is as easy as putting sections in Markdown. You just need to put a <code>#</code> before your section title in a comment environment starting with <code>&quot;&quot;&quot;</code>. For example,</p><div class="language-python line-numbers-mode" data-ext="py"><pre class="language-python"><code><span class="token triple-quoted-string string">&quot;&quot;&quot;
# Section 1
The following is a function.
&quot;&quot;&quot;</span>


<span class="token keyword">def</span> <span class="token function">foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">pass</span>


<span class="token triple-quoted-string string">&quot;&quot;&quot;
# Section 2
The following is another function.
&quot;&quot;&quot;</span>


<span class="token keyword">def</span> <span class="token function">bar</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">pass</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>In this way, <code>foo()</code> and <code>bar()</code> will have sections <code>Section 1</code> and <code>Section 2</code> respectively. The sections will also contain the comments under them.</p><p>Your section can also contain classes add levels. For example,</p><div class="language-python line-numbers-mode" data-ext="py"><pre class="language-python"><code><span class="token triple-quoted-string string">&quot;&quot;&quot;
# Top Section
## Section 1
&quot;&quot;&quot;</span>


<span class="token keyword">class</span> <span class="token class-name">Foo</span><span class="token punctuation">:</span>
    <span class="token triple-quoted-string string">&quot;&quot;&quot;
    # Section 1
    The following is a function.
    &quot;&quot;&quot;</span>

    <span class="token keyword">def</span> <span class="token function">foo</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">pass</span>

    <span class="token triple-quoted-string string">&quot;&quot;&quot;
    # Section 2
    The following is another function.
    &quot;&quot;&quot;</span>

    <span class="token keyword">def</span> <span class="token function">bar</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">pass</span>


<span class="token triple-quoted-string string">&quot;&quot;&quot;
## Section 2
&quot;&quot;&quot;</span>


<span class="token keyword">def</span> <span class="token function">baz</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">pass</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="section-in-folder" tabindex="-1"><a class="header-anchor" href="#section-in-folder" aria-hidden="true">#</a> Section in folder</h3><p>You add <code>.tree.yml</code> file in a folder to add sections in it. For example, in the following folder</p><div class="language-text line-numbers-mode" data-ext="text"><pre class="language-text"><code>a_folder
- __init__.py
- a.py
- b.py
- c.py
- .tree.yml
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>You can put <code>a</code>,<code>b</code> in a section by putting</p><div class="language-yaml line-numbers-mode" data-ext="yml"><pre class="language-yaml"><code><span class="token key atrule">sections</span><span class="token punctuation">:</span>
 <span class="token key atrule">your section title</span><span class="token punctuation">:</span>
   <span class="token punctuation">-</span> a
   <span class="token punctuation">-</span> b
<span class="token key atrule">default section</span><span class="token punctuation">:</span> you default section title
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>Then <code>a</code> and <code>b</code> will be in the section <code>your section title</code> and <code>c</code> will be in the section <code>you default section title</code>.</p><h3 id="mark-examples" tabindex="-1"><a class="header-anchor" href="#mark-examples" aria-hidden="true">#</a> Mark examples</h3><p>You can also add examples to your functions and classes. Just use the <code>@example</code> decorator. For example,</p><div class="language-python line-numbers-mode" data-ext="py"><pre class="language-python"><code><span class="token keyword">from</span> docinpy<span class="token punctuation">.</span>decorator <span class="token keyword">import</span> example


<span class="token decorator annotation punctuation">@example</span>
<span class="token keyword">def</span> <span class="token function">how_to_use_foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token triple-quoted-string string">&quot;&quot;&quot;
    # Example
    The following is an example of using \`foo()\`.
    &quot;&quot;&quot;</span>
    foo<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="mark-todos" tabindex="-1"><a class="header-anchor" href="#mark-todos" aria-hidden="true">#</a> Mark todos</h3><p>In a similar way, you can also mark todos in your code. Just use the <code>@todo</code> decorator. For example,</p><div class="language-python line-numbers-mode" data-ext="py"><pre class="language-python"><code><span class="token keyword">from</span> docinpy<span class="token punctuation">.</span>decorator <span class="token keyword">import</span> todo

<span class="token decorator annotation punctuation">@todo</span>
<span class="token keyword">def</span> <span class="token function">todo_foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token triple-quoted-string string">&quot;&quot;&quot;
    # Todo
    The following is a todo.
    &quot;&quot;&quot;</span>
    foo<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token decorator annotation punctuation">@todo</span><span class="token punctuation">(</span><span class="token string">&quot;This function is buggy. Fix it.&quot;</span><span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">buggy_foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    foo<span class="token punctuation">(</span>a<span class="token operator">=</span>b<span class="token punctuation">)</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="philosophy-behind-docinpy" tabindex="-1"><a class="header-anchor" href="#philosophy-behind-docinpy" aria-hidden="true">#</a> Philosophy behind DocInPy</h2><h3 id="literate-programming" tabindex="-1"><a class="header-anchor" href="#literate-programming" aria-hidden="true">#</a> Literate programming</h3>`,21),g={href:"https://guides.nyu.edu/datascience/literate-prog",target:"_blank",rel:"noopener noreferrer"},y=n("h3",{id:"sparse-tree-structure",tabindex:"-1"},[n("a",{class:"header-anchor",href:"#sparse-tree-structure","aria-hidden":"true"},"#"),e(" Sparse tree structure")],-1),q=n("p",null,"All the programming languages encourage the programmers to put their code in the tree structure. For example, you can put your functions in difference classes, in different files and put the files in different folders. However, it is still very common to put a lot of functions in a single file, in which the codes are arranged in an almost flat structure.",-1);function w(_,x){const a=o("ExternalLinkIcon"),t=o("RouterLink");return d(),c("div",null,[p,v,m,h,b,n("p",null,[e("EvoNote is using DocInPy to document its codebase. You can have a good visualization of EvoNote's codebase by running "),n("a",k,[e("EvoNote visualization"),s(a)]),e(".")]),f,n("p",null,[e("DocInPy can be regarded as an effort toward the idea - "),n("a",g,[e("literate programming"),s(a)]),e(". We think literate programming gets even more important in the era of AI for it provides more context information for AI-based agents to understand the codebase.")]),y,q,n("p",null,[e("DocInPy helps this by adding a zero-cost way to add sections to your functions and classes. It makes another step towards a more tree-like structure of the codebase. We believe this will help the programmers to understand the codebase better. See "),s(t,{to:"/writings/2.1%20Method%20of%20Loci%20and%20sparsity.html"},{default:l(()=>[e("Method of Loci")]),_:1}),e(" for more details.")])])}const S=i(u,[["render",w],["__file","index.html.vue"]]);export{S as default};
