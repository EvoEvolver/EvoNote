import{_ as a,r as n,o as i,c as s,a as e,b as t,d as h,e as r}from"./app-1ed94c4d.js";const d={},c=r('<h1 id="method-of-loci" tabindex="-1"><a class="header-anchor" href="#method-of-loci" aria-hidden="true">#</a> Method of Loci</h1><p>Method of Loci, also known as memory palace, is a method to memorize things by associating them with a place. It is a very old method and has been used for thousands of years. It is also a very effective method.</p><p>When you try to memorize a list of things, you can just imagine a place you are familiar with and put the things in the place. When you want to recall the things, you can just imagine the place and the things will come to your mind.</p><h2 id="why-is-the-method-good" tabindex="-1"><a class="header-anchor" href="#why-is-the-method-good" aria-hidden="true">#</a> Why is the method good?</h2><p>Why this method is efficient? Here is the claim:</p><div class="custom-container tip"><p class="custom-container-title">Claim</p><p>Method of Loci is efficient because it creates a graph of knowledge with each node has only limited number of edges. That is, it is a sparse graph.</p></div><p>Here, in the graph of knowledge, the nodes are the context (situation) and the edges leads to the memory or another situation. The whole point of method of loci is to turn a list of things, which is densely indexed, into a sparsely connected structure.</p><h2 id="why-sparse-graph-is-good" tabindex="-1"><a class="header-anchor" href="#why-sparse-graph-is-good" aria-hidden="true">#</a> Why sparse graph is good?</h2><p>Here is the claim:</p><div class="custom-container tip"><p class="custom-container-title">Claim</p><p>Sparse graph performs better because it fits in context window of human brain better.</p></div><p>Thinking with a sparse graph limits the number of things you need to think about at one time. In this meantime, because the knowledge are still interconnected, you can still think about the whole knowledge.</p><h2 id="what-does-it-mean-to-llm" tabindex="-1"><a class="header-anchor" href="#what-does-it-mean-to-llm" aria-hidden="true">#</a> What does it mean to LLM?</h2>',12),l={href:"https://arxiv.org/abs/2307.03172",target:"_blank",rel:"noopener noreferrer"},p=e("p",null,"Maybe it can be improved in the future, but I strongly don't believe that will happen very fast. We can use the sparsity of the graph to decrease the number of things LLM needs to think about at one time and enhance the performance.",-1),u=e("h2",{id:"how-about-evonote",tabindex:"-1"},[e("a",{class:"header-anchor",href:"#how-about-evonote","aria-hidden":"true"},"#"),t(" How about EvoNote?")],-1),m=e("p",null,"EvoNote uses the tree structure to index the knowledge. It has a natural advantage to make the connection at each node (note) sparse. Compared to the approaches that use a flat list (e.g., chunks) or a dense graph (e.g., knowledge graph) to index the knowledge, it is more efficient.",-1),f=e("h2",{id:"how-about-docinpy",tabindex:"-1"},[e("a",{class:"header-anchor",href:"#how-about-docinpy","aria-hidden":"true"},"#"),t(" How about DocInPy")],-1),g=e("p",null,"DocInPy provides a way to add sections to your Python codes to separate the functions and classes for arranging them into a tree structure. It makes it possible to make the tree sparse.",-1),y=e("p",null,"There are a lot of Python projects put a tons of functions in one file. This have put a barrier for both human and LLM to understand the code for a long time. DocInPy can help to solve this problem.",-1);function b(w,_){const o=n("ExternalLinkIcon");return i(),s("div",null,[c,e("p",null,[t("LLM also has a limited number of token in the context window. Current technology still struggles to make the context window large. When it seems to be large, the performance is usually not good. (See "),e("a",l,[t("Lost in the Middle: How Language Models Use Long Contexts"),h(o)]),t(")")]),p,u,m,f,g,y])}const v=a(d,[["render",b],["__file","2.1 Method of Loci and sparsity.html.vue"]]);export{v as default};
