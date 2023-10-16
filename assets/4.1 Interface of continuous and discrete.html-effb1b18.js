import{_ as a,r as o,o as i,c as s,a as e,b as t,d as r,e as c}from"./app-1ed94c4d.js";const h={},d=c('<h1 id="interface-of-continuous-and-discrete" tabindex="-1"><a class="header-anchor" href="#interface-of-continuous-and-discrete" aria-hidden="true">#</a> Interface of continuous and discrete</h1><h2 id="heap-attack" tabindex="-1"><a class="header-anchor" href="#heap-attack" aria-hidden="true">#</a> Heap attack</h2><h3 id="paradox-of-the-heap" tabindex="-1"><a class="header-anchor" href="#paradox-of-the-heap" aria-hidden="true">#</a> Paradox of the heap</h3><div class="custom-container tip"><p class="custom-container-title">Story</p><p>If you remove one grain of sand from a heap of sand, it is still a heap. If you keep removing grains of sand, eventually you will have only one grain of sand left. Is it still a heap?</p></div><p>The key point of this paradox lies in the continuous nature of the concept - <code>heap</code>. The concept <code>heap</code>, is actually never well-defined when we use it as natural language. It also does not have a formal definition in any way. You knowledge about the heap might vary infinitesimally.</p><div class="custom-container tip"><p class="custom-container-title">Observation</p><p>For a same object, you might think that is a heap this second and not a heap in the next second. However, you do not think your knowledge about the heap is changing even you give different answer. This proves that the concept <code>heap</code> is continuous because infinitesimal variation does not matter.</p></div><h3 id="attack-to-any-continuous-concept" tabindex="-1"><a class="header-anchor" href="#attack-to-any-continuous-concept" aria-hidden="true">#</a> Attack to any continuous concept</h3><p>For any continuous concept that does not have a clear definition. You can always attack it by the following way:</p><div class="custom-container tip"><p class="custom-container-title">Protocol</p><ul><li>Find an object that is an instance of the concept.</li><li>Find way to vary the object, so it is still an instance of the concept.</li><li>Show that along the way, the object will eventually not be an instance of the concept.</li><li>You know that along the way there must be a &quot;sweet point&quot;. However, the sweet point should not exist because infinitesimal variation should not change the concept, even on the sweet point. Therefore, the concept is not well-defined.</li></ul></div><p>For example, you can attack the concept <code>machine learning</code> by the following way:</p><div class="custom-container tip"><p class="custom-container-title">Example</p><ul><li>Optimizing neural network on machines is an instance of <code>machine learning</code>.</li><li>You can adjust the process by replacing some of the learning steps with human-made steps. It is still an instance of <code>machine learning</code>.</li><li>You can adjust the process by replacing all the learning steps with human-made step except for one machine-made noise step. It is ridiculous if there are 100000 human-made steps and 1 useless machine-made step. However, it is still an instance of <code>machine learning</code>.</li></ul></div><p>Importantly, nearly all the big concepts are continuous, including <code>philosophy</code>, <code>science</code>, <code>understanding</code>, <code>knowledge</code>, <code>freedom</code>, <code>democracy</code>, etc. They are all vulnerable to this attack. Though they are useful concepts, people should keep in mind that they can never have a clear definition. This impossibility of this has been proved by the history.</p><h2 id="mixture-of-continuous-and-discrete" tabindex="-1"><a class="header-anchor" href="#mixture-of-continuous-and-discrete" aria-hidden="true">#</a> Mixture of continuous and discrete</h2><p>There are knowledge that is neither continuous nor discrete. They are mixture of both. For example, though I claimed that neural networks mainly carry continuous knowledge, they also carry discrete knowledge by its network structure. The network structure is discrete and the weights are continuous.</p><p>The tree of knowledge in EvoNote is the same. The tree structure is discrete and the knowledge in the nodes are continuous because they are natural language.</p><h3 id="machine-learning-engineers" tabindex="-1"><a class="header-anchor" href="#machine-learning-engineers" aria-hidden="true">#</a> Machine learning engineers</h3><p>Machine learning engineers does a funny job. They design the discrete structure of the neural network and train the continuous weights. In this way, they mix the discrete and continuous knowledge together.</p><p>In this process, one interesting point is the roles of human and machine. The discrete structure is designed by human and the continuous weights are trained by machine. Therefore, machine only deals with continuous knowledge and the discrete knowledge are handled by human. This matches the performance of the model as products - they are good at continuous tasks and bad at discrete tasks.</p><blockquote><p>Network Architecture Search (NAS) is a process that tries to automate the design of the discrete structure. However, it failed heavily in the competition with the transformer structure. This proves that machine learning are not good at discrete tasks again.</p></blockquote><h2 id="math-that-bridges-continuous-and-discrete" tabindex="-1"><a class="header-anchor" href="#math-that-bridges-continuous-and-discrete" aria-hidden="true">#</a> Math that bridges continuous and discrete</h2><p>Math provides some concrete bridge between continuous and discrete. This kind of bridge is hard to find from daily life knowledge. This makes math beautiful and holy.</p><h3 id="group-theory" tabindex="-1"><a class="header-anchor" href="#group-theory" aria-hidden="true">#</a> Group theory</h3><p>The space where the continuous knowledge lives might have a symmetry described by a certain Lie group. Group theory offers a way to analyze these continuous knowledge by analyzing its Lie group. For example, the Lie group might have a countable number of generators, which gives a discrete way to analyze the continuous knowledge. We can also analyze the representation of the Lie group, which will make the representation of it more discrete if we can decompose it into irreducible representations.</p>',23),l={href:"https://arxiv.org/abs/2006.10503",target:"_blank",rel:"noopener noreferrer"},u=e("h3",{id:"topology",tabindex:"-1"},[e("a",{class:"header-anchor",href:"#topology","aria-hidden":"true"},"#"),t(" Topology")],-1),p=e("p",null,"Topology is an example where continuous entities can be unambiguously represented by discrete entities.",-1),m=e("p",null,"Condense matter physics loves topology very much. Part of the reason is the topological properties of condensed matter system nearly the only way to describe them in a discrete way.",-1);function g(f,y){const n=o("ExternalLinkIcon");return i(),s("div",null,[d,e("p",null,[t("Using the discrete knowledge found by group theory have been applied to neural network design. "),e("a",l,[t("Equivariant neural network"),r(n)]),t(" is one example.")]),u,p,m])}const b=a(h,[["render",g],["__file","4.1 Interface of continuous and discrete.html.vue"]]);export{b as default};
