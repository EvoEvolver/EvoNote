sample_paper= r"""
\title{On scientific understanding with artificial intelligence}

\begin{abstract}
Imagine an oracle that correctly predicts the outcome of every particle physics experiment, the products of every chemical reaction, or the function of every protein. Such an oracle would revolutionize science and technology as we know them. However, as scientists, we would not be satisfied with the oracle itself. We want more. We want to comprehend how the oracle conceived these predictions. This feat, denoted as scientific understanding, has frequently been recognized as the essential aim of science. Now, the ever-growing power of computers and artificial intelligence poses one ultimate question: How can advanced artificial systems contribute to scientific understanding or achieve it autonomously?

We are convinced that this is not a mere technical question but lies at the core of science. Therefore, here we set out to answer where we are and where we can go from here. We first seek advice from the philosophy of science to \textit{understand scientific understanding}. Then we review the current state of the art, both from literature and by collecting dozens of anecdotes from scientists about how they acquired new conceptual understanding with the help of computers. Those combined insights help us to define three dimensions of android-assisted scientific understanding: The android as a I) computational microscope, II) resource of inspiration and the ultimate, not yet existent III) agent of understanding. For each dimension, we explain new avenues to push beyond the status quo and unleash the full power of artificial intelligence's contribution to the central aim of science. We hope our perspective inspires and focuses research towards androids that get new scientific understanding and ultimately bring us closer to true artificial scientists.
\end{abstract}


\section{Introduction}
Artificial Intelligence (A.I.) has recently been called a ``new tool in the box for scientists"\cite{zdeborova2017new} and that ``machine learning with artificial networks is revolutionizing science``\cite{fosel2018reinforcement}. Additionally, it has been conjectured ``that machines could have a significantly more creative role in future research." \cite{melnikov2018active}. For instance, it has even been postulated that ``[t]he new goal of theoretical chemistry should be that of providing access to a chemical 'oracle': an A.I. environment which can help humans solve problems, associated with the fundamental chemical questions of the fourth industrial revolution [...], in a way such that the human cannot distinguish between this and communicating with a human expert" \cite{aspuru2018matter}.

However, this excitement has not been shared among all scientists. Specifically, it has been questioned whether advanced computational approaches can go beyond \textit{numerics} \cite{hoffmann2020simulationA, hoffmann2020simulationB, hoffmann2020simulationC, marcus2020next,thaler2021} and contribute fundamentally to one of the essential aims of science, that is, gaining of new scientific understanding \cite{potochnik2015diverse,potochnik2017idealization,de2017understanding}.

In this work, we address how artificial systems can contribute to scientific understanding -- specifically, what is the state-of-the-art and how we can push further. Besides a thorough literature review, we surveyed dozens of scientists at the interface of biology, chemistry or physics on the one hand, and artificial intelligence and advanced computational methods. These personal narratives focus on the concrete discovery process of ideas and are a vital augmentation to the scientific literature. We put the literature and personal accounts in the context of a philosophical theory of \textit{Scientific Understanding} recently developed by Dennis Dieks and Henk de Regt \cite{de2005contextual,de2017understanding}, who was awarded the Lakatos Award in 2019 for the development of this theory. We thereby introduce three fundamental dimensions for scientific androids\footnote{We encapsulate all advanced artificial computational systems under \textit{androids}, independent of their working principles. In this way, we are focusing on the operational objective rather than the methodology.} contribution towards new scientific understanding: 
\begin{enumerate}[I)]
\item Androids acting as a microscope in the responses, i.e., akin to an instrument revealing properties of a physical system that are otherwise difficult or even impossible to probe. Humans then lift these insights to scientific understanding.
\item Androids acting as muses, i.e., sources of inspiration for new concepts and ideas that are subsequently understood and generalized by human scientists.
\item Lastly, in an ultimate dimension of android-assisted scientific understanding, computers are the agents of understanding. While we have not found any evidence of computers acting as true agents of understanding in science yet, we outline important characteristics of such an artificial system of the future and potential ways to achieve it.
\end{enumerate}
In the first two dimensions, the android enables humans to gain new scientific understanding while in the last one the machine gains understanding itself. These classes enable us to layout a vibrant and mostly unexplored field of research, which will hopefully manifest itself as a guiding star for future developments of artificial intelligence in the natural sciences.

The goal of this perspective is to put \textit{Scientific Understanding} back to the limelight -- where we are convinced it belongs. We hope to inspire physicists, chemists and biologists and A.I. researchers to go beyond the status quo, focus on these central aims of science, and revolutionize computer-assisted scientific understanding. In that way, we believe that androids will become true agents of understanding that contribute to science in a fundamental and creative way.




\section{Scientific Understanding}
Let us imagine an oracle providing non-trivial predictions that are always true. While such a hypothetical system would have a very significant scientific impact, scientists would not be satisfied. We want ``\textit{to be able to grasp how the predictions are generated, and to develop a feeling for the consequences in concrete situations}" \cite{de2005contextual}. Colloquially, we refer to this goal as ``understanding" -- But what does that really mean? Can we find criteria for scientific understanding? To do that, we seek guidance from the field of philosophy of science. Notably, while hardly any scientist would argue against ``understanding" as an essential aim of science (next to explanation, description and prediction \cite{de2020understanding}), this view was not always accepted by philosophers. Specifically, Carl Hempel, who made foundational contributions clarifying the meaning of \textit{scientific explanation}, argued that ``understanding" is subjective and merely a psychological by-product of scientific activity and is therefore not relevant for the philosophy of science \cite{hempel1965aspects}. Other philosophers criticized these rather unsatisfying conclusions, and they tried to formalize what \textit{scientific understanding} means. Proposals include that understanding is connected to the ability to build causal models (Lord Kelvin said ``It seems to me that the test of 'Do we or not understand a particular subject in physics?' is, 'Can we make a mechanical model of it?' "\cite{de2005contextual}), connected to providing visualizations (or \textit{Anschaulichkeit}, as its strong proponent Erwin Schr\"odinger called it\cite{schrodinger1996nature,de2014visualization}) or that understanding corresponds to providing unification \cite{friedman1974explanation, kitcher1981explanatory}.

In recent years, Henk de Regt and Dennis Dieks have developed a new theory of scientific understanding, which is both contextual and pragmatic \cite{de2005contextual,de2017understanding,de2020understanding}. Importantly, they find that techniques such as visualization or unification are ``tools for understanding", thereby unifying previous ideas in one general framework. Their theory is agnostic to the specific ``tool" being used, making it particularly useful for application in scientific disciplines. They extend crucial insights by Werner Heisenberg \cite{heisenberg1927} and rather than introducing mere theoretical or hypothetical ideas, the main motivation behind their theory is that a ``\textit{satisfactory conception of scientific understanding should reflect the actual (contemporary and historical) practice of Science}". Put simply, they argue that:
\begingroup
\addtolength\leftmargini{-0.1in}
\begin{quote}
A phenomenon P can be understood if there exists an intelligible theory T of P such that scientists can recognise qualitatively characteristic consequences of T without performing exact calculations \cite{de2005contextual,de2017understanding}.
%\end{displayquote}
\end{quote}
\endgroup

Concretely, de Regt and Dieks define two interlinked criteria:
\begin{enumerate}
\item \textbf{Criterion of Understanding Phenomena}: A phenomenon P can be understood if a theory T of P exists that is intelligible.
\item \textbf{Criterion for the Intelligibility of Theories}: A scientific theory T is intelligible for scientists (in context C) if they can recognise qualitatively characteristic consequences of T without performing exact calculations.
\end{enumerate}
%}

We decided to use this specific theory because of one particular strength: We can use it experimentally to evaluate whether scientists have \textit{understood} new concepts or ideas, rather than by inspecting their methodology, by simply looking at the scientific outcome and the consequences. This also coincides with Angelika Potochnik's argument that ``\textit{understanding requires successful mastery, in some sense, of the target of understanding}"\cite{potochnik2017idealization}. We will follow this approach and, consequently, here explore its relationship to the role of A.I. in science. Accordingly, we believe we can significantly advance A.I.'s contribution to this central aim of Science if we have a clear picture of how scientists gain conceptual understanding, and instil it to artificial systems afterwards. We approach this goal by applying ideas of de Regt and Dieks directly to android assisted science (and ultimately, to android scientists themselves).

\section{What is next?}

\subsection{Beyond \textit{Re}-Discovery}
In recent years, scientists at the interface between A.I. and the natural sciences tried to rediscover scientific laws or concepts with machines. The question is, however, whether an android is capable of contributing to new scientific understanding if it can \textit{re}discovers physical laws and concepts, such as the heliocentric world view \cite{iten2020discovering}, the arrow of time \cite{seif2020machine} or mechanical equations of motions \cite{udrescu2020ai}? We believe that this is not guaranteed. The human creators of these androids know what they are looking for in these case studies. Therefore, it is unclear how both conscious and unconscious biases (in the broadest sense, e.g., by choosing particular representations) in the code or the data analysis can be prevented. Consequently, even if an algorithm can rediscover interesting physical phenomena, we cannot know whether and how they can be used to advance Science by helping to uncover new scientific understanding.

Hence, we believe we need to go beyond rediscovery tasks. Therefore we focus explicitly on the question of how to get \textit{new} scientific understanding.

\subsection{Beyond Discovery}
Importantly, other central aims of science such as prediction and discovery can lead to scientific and technological disruptions while not directly contributing to scientific understanding as discussed above \cite{de2020understanding,potochnik2017idealization}. For instance, imagine the hypothetical discovery of the \textit{hitherto} best material for energy storage that could revolutionize batteries. However, this game-changing discovery would not qualify as understanding if chemists could not use the underlying principles fruitfully in other contexts (without computation).

Similarly, the recent breakthrough in protein folding will undoubtedly change the landscape of biochemistry. However, so far, AlphaFold is a black box -- an oracle\cite{jumper2021highly,tunyasuvunakool2021highly}. As such it does not directly provide new scientific understanding in the sense of de Regt and Dieks (but could of course in the future enable humans to gain new scientific understanding). Hence, we believe we must go beyond artificial discoveries in science.

\subsection{Where to go from here?}
The ultimate goal is to get new \textit{understanding} from androids. Loosely speaking, we want to find new ideas or concepts that we can apply and use in different situations without (complete) computations.

This article aims to explain precisely what such a goal requires, what previous approaches have achieved, and how we can go further. We want to clearly lay out this underappreciated but essential research question and thereby give a clear goal for the future of A.I. in the natural sciences.


\begin{figure*}[ht]
\centering
\includegraphics[width=0.85\textwidth]{AndroidsFancyDreamsFig2.pdf}
\caption{\textbf{The future computational microscope.} We envision two types of advances in the next-generation computational microscopes which aim to advance genuine scientific understanding. First (left), larger and more complex computations will allow the computational observation of phenomena not accessible so far. There, new computational paradigms will play a significant role, such as Graphical Processor Units (GPU), Tensor Processor Units (TPU), Optical Processor Units (OPU) and -- ultimately -- quantum computers. Second (right), new ways to represent the highly complex data will advance our ability to sense structure and recognize underlying patterns. The involvement of all our senses could, for sensing computer-generated data, be an exciting pathway to advanced understanding.}
\label{fig:flowofargument2}
\end{figure*}



\section{Three dimensions of computer-assisted understanding}\label{sec:III}
We use scientific literature and personal anecdotes of dozens of scientists, and the context of the philosophy of science, to introduce a new classification of androids contribution to scientific understanding\footnote{We call the classification \textit{dimensions}, as they are independent and non-exclusive.}. It helps to see diverse unexplored journeys that can be investigated in the future.

An android can act
\begin{enumerate}[I)]
\item as a \textbf{computational microscope}, providing information not (yet) attainable by experiment

\item as a \textbf{resource of inspiration} or an \textit{artificial muse}, expanding the scope of human imagination and creativity.
\end{enumerate}

In those two classes, the human scientist is essential to take the new insight and inspiration and develop it to full understanding. Finally, an android can be

\begin{enumerate}[I)]
\setcounter{enumi}{2}
\item an \textbf{agent of understanding}, replacing the human in generalizing observations and transferring scientific concepts to new phenomena. 
\end{enumerate}

We stress that these three classes should not be understood dogmatically but rather guide future possibilities. In the following sections, based on concrete examples, we discuss each class in more detail and propose avenues for pushing the boundaries of the current computational faculties. 


\subsection{Computational microscope for scientific understanding}
Microscopes are devices that enable us to investigate objects and phenomena imperceptible to the naked eye. In a similar way, \textit{computational microscopes} enable the investigation of objects or processes that we cannot visualize or probe in any other way. One main objective is to simulate biological, chemical or physical processes that happen at length and time scales not perceivable by experiment.

As we are interested in understanding, the new computer-generated data needs to be generalized to other contexts without complete computation\cite{de2005contextual}. We show now two concrete examples.

The first example is molecular dynamics simulations of the SARS-CoV-2. The authors uncovered new biological functions that show different behaviours in the open and closed conformations of the spike protein. This explanation changed the view upon glycans in biological systems and inspired new ways to analyze these systems without the need to perform full computations \cite{casalino2020beyond}.

In the second example, the authors describe how molecular dynamics simulations helped to uncover fundamental patterns called \textit{glycoblocks}. The systematic use of glycoblocks can both be used to understand sequence-structure-property relationships of biomolecules and can also inform the design of synthetic structures with desired functions without the need for simulating the entire system \cite{fogarty2020and}.



\subsubsection*{The next computational microscope}\label{NextCMicroscope}
A computational microscope aims to provide data via computation that are not (yet) accessible by experiments that humans can understand. How could we make computational microscopes even more insightful and make it easier for human scientists to use this data to gain scientific understanding? There are two vibrant directions going forwards. First, more advanced computational systems will allow to analyze of more complex physical systems. Second, representing the information in a more interpretable way will help to lift the indications from computers to true scientific understanding.

\subsubsubsection{More Complex Systems} One obvious but nevertheless important research direction is increasing the complexity as well as the accuracy of computer simulations\cite{friederich2021machine}. For example, increasing the size of the systems, the time-scale of the simulations, the number of interactions that can be modelled will significantly increase the applicability in complex dynamic systems. In general, this can be achieved by either algorithmic improvements or hardware improvements, or both. In that regard, we expect that modern neural network technologies together with advanced hardware such as GPUs, TPUs or even OPUs \cite{gigan2020artificial,xu202111} will have an enormous impact. Furthermore, the recent progress in experimental quantum computing for quantum chemistry \cite{google2020hartree} and physics\cite{zhang2017observation, schweizer2019floquet, martinez2016real} promises that entirely new algorithms, based on quantum mechanics itself, will play an important role in this area \cite{cao2019quantum,gross2017quantum}. Algorithmic improvements could involve adaptive and intelligent resolution during simulation and advanced visualization methods\cite{de2005contextual}, which directly leads to the second future techniques:

\subsubsubsection{Full spectrum of senses}  We believe that human scientists can get more out of data if the full capabilities of all our senses are addressed. At the moment, we analyze data largely in (potentially animated) 2-dimensional pictures. As a first step, we believe that real 3D environments (realized either via virtual or augmented reality glasses, or holography) will significantly help in understanding complex systems or complex data. Initial advances in that regard have been demonstrated in the domain of chemistry \cite{o2018sampling, probst2018exploring, schmid2020structural}, and we expect this to become a standard tool for scientists to advance scientific understanding. In addition, we expect that going beyond the visual sense can open entirely new ways to experience scientific data. For example, the auditory sense is excellent in detecting structure or symmetries in (periodic) time-dependent data \cite{castelvecchi2021sound}. Furthermore, including the sense of touch, smell and taste could further expand the horizon of experiences. We expect that in order to realize that, physical scientists need to work closely together with psychologists and neurologists (and potentially even with artists), to develop suitable data representations that can be efficiently recognized by scientists with all their senses. An ultimate, admittedly futuristic version of a computational microscope could circumvent the receptors of human senses and instead use a computer-brain interface to enhance further experiencing computed data.

\subsubsubsection{Resource of inspiration for scientific understanding}
Surprising and creative ideas are the foundation of Science. Computer algorithms are a means to provoke such ideas systematically, thereby significantly accelerating scientific and technological progress. Already 70 years ago,  Alan Turing realized that computers could surprise their human creators: \textit{``Machines take me by surprise with great frequency. This is largely because I do not do sufficient calculation to decide what to expect them to do, or rather because, although I do a calculation, I do it in a hurried, slipshod fashion, taking risks."} and \textit{"Naturally I am often wrong, and the result is a surprise for me for by the time the experiment is done these assumptions have been forgotten``}\cite{turing1950computing}.

A much more recent study provides stories by dozens of researchers of artificial life and evolution. They demonstrate in an impressive way how computer algorithms can surprise their human creators and lead to behaviour that the authors \textit{would denote as creative}\cite{lehman2020surprising}. Accordingly, we believe that androids can be artificial muses of Science in a metaphorical sense.


Those examples demonstrate that computers can indeed be used as a source of surprises. But what are the most general ways to get inspirations from computers? And how can they be lifted by humans to true scientific understanding? We will outline a number of ways to develop ways to provoke surprising behaviours of algorithms and use their solutions, internal or external states as a source of inspiration for new scientific ideas.

\begin{figure*}[ht]
\centering
\includegraphics[width=0.85\textwidth]{AndroidsFancyDreamsFig3.pdf}
\caption{\textbf{The future \textit{re}-source of inspiration: } An android could act as a computational muse and inspire the human scientist by (A) identifying surprises in data, (B) identifying surprises in the scientific literature, (C) finding surprising concepts by inspecting models or (D) by probing the behaviour of artificial agents or (E) my finding new concepts from interpretable solutions.}
\label{fig:flowofargument3}
\end{figure*}


\subsubsection*{The future resource of inspiration}
\subsubsubsection{Identifying surprises in data} Exceptional data points or unexpected regularities obtained from experiments or simulations can surprise human scientists and inspire new ideas and concepts. Our survey shows that these exceptional points are usually identified by humans, such as the following two examples, which use high-throughput computations in chemistry \cite{pickard2011ab} and quantum optics \cite{krenn2016automated,krenn2020computer}.

The first example deals with a surprising phase of crystal structures in high-pressure physics. There, the authors found an unexpected stable configurations of alternating \ce{NH2} and \ce{NH4} layers, rather than a dense \ce{NH3} phase. The authors conceptualized this phenomenon as spontaneous ionization, a common process in acid-base chemistry, which is now a widely accepted phenomenon in the high-pressure phase diagram of \ce{NH3}. Spontaneous ionization in the high-pressure behaviour of matter has become a more general principle that can be used without performing any simulations \cite{pickard2008highly}.

In the second example, a search for new quantum experiments uncovered a solution with considerable larger quantum entanglement than expected. The authors understood the underlying principles and thereby discovered a new concept of entanglement generation \cite{krenn2017entanglement, krenn2017quantum}. The principle can be used without any computation and, for example, acts now as a new representation in more advanced artificial intelligence systems for quantum physics \cite{krenn2020conceptual}, demonstrating the application of the computer-inspired idea in more general different contexts.

In contrast to these examples and many others from literature and from personal accounts, the anomalies could manifest themselves in a more involved combination of variables, which might be very difficult for humans to grasp. Accordingly, applying advanced statistical methods and machine learning algorithms (e.g., see reference \cite{malhotra2015long}) to this type of problem will be an important future research direction. Exciting works into the direction of autonomous anomaly detection have been applied on scientific data from the Large Hadron Collider (LHC) at CERN \cite{aad2020dijet, tonon2021probing, park2021quasi}. Such techniques have the potential to identify new physics signatures, which can then be conceptualized and understood by human physicists \cite{schwartz2021modern,kasieczka2021lhc}. Neural networks that autonomously discover symmetries could become an efficient discovery tool for outliers in scientific data where the underlying rules might not be known beforehand \cite{yu2018group,dehmamy2021automatic}.

Estimating the confidence of predictions will be one method to directly search for anomalies in data \cite{nigam2021assigning}. The ability to uncover hidden regularities was very recently demonstrated in mathematics, where an A.I. hinted on relations between previously unconnected invariants in knot theory, which allowed mathematicians to conjecture and prove new theorems \cite{davies2021advancing}. Alternatively, an A.I. capable of constructing new scientific hypotheses could uncover outliers or unexpected patterns that are not discernible with standard statistical methods. 

It would be truly exciting to see an A.I. uncover hidden patterns or irregularities in scientific data previously overlooked by humans, which leads to new ideas and, ultimately, to new conceptual understanding. As of now, we are not aware of cases like that.


The data points for these systems could be obtained from computational methods (involving those described in section \ref{NextCMicroscope}), with exciting opportunities for mathematics or theoretical physics \cite{douglas2022machine}. Alternatively, the data could be obtained directly from experiments. Here we can imagine a closed-loop approach where an algorithm tries to explore the environment and steer the exploration into unexpected regions. If the data-source is an experiment, this future system will require access to complex lab automation with large parameter spaces to explore, as demonstrated recently in biology \cite{king2009automation}, chemistry \cite{bedard2018reconfigurable, steiner2019organic, coley2019robotic, burger2020mobile, chatterjee2020automated, grizou2020curious} or physics \cite{moon2020machine,dalgaard2020global}.

\subsubsubsection{Identifying surprises in the scientific literature } The number of scientific papers in essentially every scientific domain is growing enormously\cite{larsen2010rate}. Consequently, researchers have to specialise in narrow subdisciplines, which makes finding new interdisciplinary ideas difficult. In the future, we believe that computers will be able to use the scientific literature in an automated way\cite{evans2011metaknowledge,clauset2017data,fortunato2018science,wang2021science} and identify exceptional and surprising phenomena for further investigation. While the large-scale automated analysis of the scientific literature, to our knowledge, has not yet been able to induce new scientific understanding, there is significant progress in the field. One promising approach towards this goal is unsupervised word embedding of a large corpus of scientific papers. In that technique, the content of the scientific literature is transformed into a high-dimensional vector space. Recently, this technique has been applied in the domain of material science \cite{tshitoyan2019unsupervised} and rediscovered central scientific concepts such as the periodic table of the elements. Additionally, the results also suggested the existence of previously undiscovered structure-property relationships. Examples include new candidates for thermoelectric materials. Moreover, several other advanced computational techniques are being developed in material science to extract knowledge from the scientific literature and investigate it systematically by A.I. technologies\cite{olivetti2020data}, and can lead to complex scientific conclusions as demonstrated for instance on zeolite transformations \cite{schwalbe2019graph}.

An alternative approach aims to build semantic knowledge networks from large bodies of scientific literature. In these networks, scientific concepts are nodes, and edges carry relational information. In the simplest case, that means two scientific concepts are mentioned in the same scientific paper \cite{rzhetsky2015choosing,krenn2020predicting}. Thus, scientific knowledge is represented as an evolving network, which can be used to identify both islands and unexplored regions of the scientific literature. This type of network was used in biochemistry to identify efficient global research strategies \cite{rzhetsky2015choosing} and in quantum physics to predict and suggest future research directions \cite{krenn2020predicting}. Advances in A.I. technology could improve this type of system significantly. For example, natural language processing architectures such as BERT \cite{devlin2018bert}, or GPT3 \cite{brown2020language} could help extract more scientific knowledge from research papers, and large graph-based neural networks could improve the prediction of new research topics from semantic networks \cite{hamilton2017inductive}. 

\subsubsubsection{Surprising concepts by inspecting models} We also expect considerable progress by rationalising what A.I. algorithms have learned in order to solve a specific problem, i.e., explainable or interpretable A.I. \cite{montavon2018methods,samek2019explainable,roscher2020explainable,lundberg2020local}. One idea towards this goal is inspired by DeepDreaming, a method first used in computer vision \cite{mahendran2015understanding,mordvintsev2015inceptionism}. Put simply, the idea is to invert a neural network and probe its behaviour. Recently, this approach has been applied to rediscover thermodynamical properties \cite{seif2020machine}, and design principles for functional molecules \cite{shen2020deep}. An alternative and remarkable application is the \textit{disentanglement of variables} in neural networks \cite{burgess2018understanding}. The goal is to understand the internal representation the neural network has learned. Recently, astronomical data, represented in geocentric coordinates, was used to train a neural network and disentanglement of variables enabled the rediscovery of heliocentric coordinates via the internal representation of the model \cite{iten2020discovering}. In a related study, using gradient boosting with decision trees, feature importance has been used to explain properties of molecules, and quantum optics circuits \cite{friederich2021scientific}. Related to this is a study where the internal representation of an unsupervised deep generative model for quantum experiments has been inspected to understand the model's internal worldview\cite{flam2021learning}. In the chemical domain, counterfactual explanations for machine learning models have been demonstrated to produce rationale behind a model's prediction. Counterfactual explanations illustrate what differences to an event or instance would generate a change in an outcome. Wellawatte et al. \cite{wellawatte2022model} showed how this can be achieved in a model-independent way (it has been demonstrated for random forest, sequence models and graph neural networks), indicating great future potentials for opening the black-box of AI in science. Albeit not in science, recent work has investigated what the chess-playing A.I AlphaZero has learned about chess and how human-like knowledge is encoded in the internal representation \cite{mcgrath2021acquisition}. The concepts rediscovered in all of those works were not new, and thus the most important challenge for the future is to learn how to extract previously unknown concepts. Progress towards resolving that challenge will be essential in the near future to inspire new scientific ideas. 


\subsubsubsection{New concepts from interpretable solutions} Rather than getting inspirations from the A.I. algorithms themselves, scientists can also be surprised by the corresponding solutions. When solutions are represented in an interpretable way, they can provoke new ideas and lead to new concepts. An example of interpretable representations is a mathematical formula. Thus, scientists can inspect formulae derived by computer algorithms to solve mathematical problems directly and derive more general solution strategies. Several publications demonstrated extracting symbolic models from experimental data of mechanical systems \cite{schmidt2009distilling, udrescu2020ai}, of quantum systems \cite{gentile2021learning} and in astronomy \cite{cranmer2020discovering}. It will be exciting to see how these approaches, e.g., combined with methods such as causal inference \cite{cranmer2020frontier}, can be improved to propose reasonable physical models of unknown systems that advance scientific understanding. Altogether, exciting advances have been achieved in the field of mathematics\cite{raayoni2021generating,wagner2021constructions}, and we foresee similar approaches making a significant impact in the physical sciences as well. 

One concrete, recent example in astronomy is the rediscovery of Newton's law of gravitation from real-world observational data of planets and moons in our solar system from the last 30 years \cite{lemos2022rediscovering}. The application of graph neural networks allowed for the high-quality prediction of the object's motion. Furthermore, a symbolic regression technique called PySR (introduced in \cite{cranmer2020discovering}) was able to extract reasonable mathematical expressions for the learned behaviour. Interestingly, besides the equations of motions, the method simultaneously predicts the masses of the planetary objects correctly. The technique required the assumption of several symmetries and other physical laws. It will be interesting to see whether these prerequisites can be reduced further and how related approaches can be applied to modern physics questions.

Another concrete example of this methodology has been showcased in the field of quantum optics \cite{krenn2020conceptual}. There, an A.I. algorithm with a graph-theoretical representation of quantum optical setups designs configurations for previously unknown quantum systems. The final solutions were represented in a physically-interpretable graph-theoretical representation. From there, human scientists can quickly interpret the underlying reasons why the solutions work and apply it in other contexts without further computation. Accordingly, developing interpretable representations and methods to extract underlying concepts in other domains will be an important future research direction.


\subsubsubsection{Probing the behaviour of artificial agents} Another only rarely explored opportunity is interpreting the behaviour of machines when tasked to solve a scientific problem \cite{rahwan2019machine}. Algorithms that take actions such as genetic algorithms or reinforcement learning agents adopt policies to navigate the problem space. Human scientists can observe how they navigate this space. Instead of following a strict external reward, e.g., maximise a specific property of a physical system, intrinsic rewards such as artificial curiosity can be implemented \cite{schmidhuber2008driven,pathak2017curiosity}. Instead of maximizing directly some functions, the artificial agent tries to learn and predict the behaviour of the environment. It then chooses actions that lead to situations it cannot predict well, thus maximizing its own understanding of the environment. It has been shown using curious agents in simulated virtual universes \cite{thiede2020curiosity} and robot agents in real laboratories \cite{grizou2020curious} that curiosity is an efficient exploration strategy. Alternative intrinsic rewards for artificial agents are \textit{computational creativity}\cite{varshney2020explaining,varshney2019big} and \textit{surprise} \cite{itti2009bayesian}. These intrinsic rewards can produce exceptional and unexpected solutions, ultimately inspiring human scientists.



\subsection{Agent of Understanding}
The third and final class we consider are algorithms that can autonomously acquire new scientific understanding, a feat that has neither been described by the respondents of our survey nor in the scientific literature. Therefore, we will approach this class by listing the requirements of these agents, proposing tests to detect their successful realization and speculating what such computer programs could look like.

First, it is important to realize that finding \textit{new} scientific understanding is context-dependent. What is new depends on whether we consider an individual scientist and their field of expertise, a scientific domain, the whole scientific community or even the entire scientific endeavour throughout history. Hence, true agents of understanding must be able to evaluate whether an insight is new, at least in the context of a specific scientific domain that requires access to the knowledge of a scientific field.

Secondly, de Regt emphasized the importance of underlying scientific theories that allow us to recognize qualitatively characteristic consequences \cite{de2017understanding}. It is not enough to simply interpolate data points or predict new ones using advanced statistical methods such as machine learning. Thus, even though such methods can approximate complex and expensive computations, na\"ive applications of neural networks cannot be agents of understanding. Scientific understanding requires more than mere calculation. To illustrate this point even further, let us consider one concrete example in quantum physics from the literature: A computational method solved an open question about the generation of important resource states for quantum computing. Then it extracted the conceptual core of the solution in the form of a new quantum interference effect in such a fashion that human scientists can both understand the results and apply the acquired understanding in different contexts \cite{krenn2020conceptual}. Even if the computer itself was able to apply the conceptual core to other situations, it would not be \textit{a priori} clear whether the computer truly acquired scientific understanding. What is still missing is an explanation of the discovered technique in the context of a scientific theory. In this particular example, the android and the human scientist would need to recognize the underlying quantum interference in the context of the theory of quantum physics. Thus, we can propose the first sufficient condition for agents of understanding:


\begin{quote}
\textbf{Condition for Scientific Understanding I:}
\textit{An android gained scientific understanding if it can recognize qualitatively characteristic consequences of a theory without performing exact computations and use them in a new context}.
\end{quote}



This condition closely follows the ideas of de Regt and Dieks \cite{de2005contextual}. Let us go one step further and imagine that there is an android capable of explaining discoveries in the context of scientific theories. How could human scientists recognize that the machine acquired new scientific understanding? We argue that human scientists would do it in the exact same way they can recognize that other human scientists acquired new scientific understanding. That is, let the other human scientists transfer the newly acquired understanding to themselves. This allows us to propose the second sufficient condition for agents of understanding:


\begin{quote}
\textbf{Condition for Scientific Understanding II:}
\textit{An android gained scientific understanding if it can transfer its understanding to a human expert}.
\end{quote}

We argue that one can only recognize indirectly whether a computer (or human) has gained scientific understanding. Therefore, finally, we propose a test in the spirit of the Turing test \cite{turing1950computing} or the Feigenbaum test\cite{feigenbaum2003some} (or adaptations thereof in the natural sciences such as the Chemical Turing Test or the Feynman Test \cite{aspuru2018matter}):

\begingroup

\begin{quote}
\textbf{The Scientific Understanding Test:}

\textit{A human (the student) interacts with a teacher, either a human or an android scientist. The teacher's goal is to explain a scientific theory and its qualitative, characteristic consequences to the student. Another human (the referee) tests both the student and the teacher independently\footnote{In principle, there is no reason for the student or the referee not to be androids. However, to keep the test as simple as possible, we want to keep the number of possible variations small.}. If the referee cannot distinguish between the qualities of their non-trivial explanations in various contexts, we argue that the teacher has scientific understanding.}
\end{quote}
\endgroup


This implies that \textit{humans} need to understand the new concepts that androids devised. If a machine truly understands something, it will be able to explain it and transfer the understanding to someone else.\footnote{We leave aside the question whether the explanation of the android is true or false. It has been argued that also false theories can lead to genuine understanding \cite{de2017false}.} We believe that this should always be possible, even if the understanding is far beyond what human experts know at this point. We envision that computers will use advanced human-computer interaction techniques together with the tools we described for (future) computational microscopes.

Additionally, scientific discussions between a human and a computer could be realized using advanced queries in natural language processing tools such as BIRD \cite{devlin2018bert} or GPT-3 \cite{brown2020language}. That way, the scientist could probe the computer with scientific questions. Suppose the scientist gains new scientific understanding by communicating with the algorithm, as judged by our scientific understanding test. In that case, they can confirm that the computer truly acquired understanding.\footnote{We would like to point out that our test, like the ones originated by Turing and Feigenbaum, are not clear-cut, leaving room for situations that do not allow a clear judgement.} We are optimistic that more efforts will be directed at developing the necessary technologies, which will lead to ever more convincing demonstrations of android scientists acting as true agents of understanding in the future. 


\section{Conclusion}
Undoubtedly, advanced computational methods in general and artificial intelligence specifically will further revolutionize how scientists investigate the secrets of our world. We outline how these new methods can directly contribute to one of the main aims of science, namely acquiring new scientific understanding. We suspect that significant future progress in the use of androids to acquire scientific understanding will require multidisciplinary collaborations between natural scientists, computer scientists and philosophers of science. Thus, we firmly believe that these research efforts can -- within our lifetimes -- transform androids into true agents of understanding that will directly contribute to one of the most essential aims of science, namely Scientific Understanding.


"""

sample_paper_2 = r'''
\title{Lost in the Middle: How Language Models Use Long Contexts}


\author{Nelson F. Liu$^{1*}$ \tab Kevin Lin\affb \tab John Hewitt\affa \tab Ashwin Paranjape\affc \\ \quad {\bf Michele Bevilacqua}\affc \tab  {\bf Fabio Petroni}\affc \tab {\bf Percy Liang}\affa \\
  \affa Stanford University \tab \affb University of California, Berkeley \tab \affc Samaya AI \\
  \eml{nfliu@cs.stanford.edu}
}

\begin{document}

\maketitle
\blankfootnote{\llap{\textsuperscript{*}}Work partially completed as an intern at Samaya AI.}
\begin{abstract}
While recent language models have the ability to take long contexts as input, relatively little is known about how well the language models \textit{use} longer context.
We analyze language model performance on two tasks that require identifying relevant information within their input contexts: multi-document question answering and key-value retrieval.
We find that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts.
Furthermore, performance substantially decreases as the input context grows longer, even for explicitly long-context models.
Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context models.
\end{abstract}

\section{Introduction}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{./figures/figure1.pdf}
\caption{Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model's input context results in a U-shaped performance curve---models are better at using relevant information that occurs at the very beginning or end of its input context, and performance degrades significantly when models must access and use information located in the middle of its input context. For example, \gptturbo's open-book performance on the multi-document question task when relevant information is placed in the middle of its input context is lower than its performance when predicting \emph{without any documents} (i.e., the closed-book setting; 56.1\%).
See Figure~\ref{fig:qa_results} for full results.}\label{fig:figure1}
\end{figure}

Language models have become an important and flexible building block in a variety of user-facing language technologies, including conversational interfaces, search and summarization, and collaborative writing.
These models perform downstream tasks primarily via prompting: all relevant task specification and data to process is formatted as a textual context, and the model returns a generated text completion.
These input contexts can contain thousands of tokens, especially when using language models on lengthy inputs (e.g., legal or scientific documents, conversation histories, etc.) or augmenting them with external information (e.g., relevant documents from a search engine, database query results, etc; \citealp[\emph{inter alia}]{petroni2020context,ram2023incontext,shi2023replug,mallen2023trust,schick2023toolformer}).

Handling these use-cases requires language models to successfully operate over long sequences.
Language models are generally implemented with Transformers, which scale poorly to long sequences (e.g., since self-attention complexity is quadratic with the input sequence length).
As a result, language models are typically trained with relatively small context windows.
Recent improvements in hardware (e.g., faster GPUs with more memory) and algorithms \citep[\emph{inter alia}]{dai-etal-2019-transformer,dao2022flashattention,poli2023hyena,rubin2023longrange} have resulted in language models with larger context windows, but it remains unclear how these extended-context language models make use their input contexts when performing downstream tasks.

We empirically investigate this question via controlled experiments with a variety of state-of-the-art open (\mptinstruct, \longchat) and closed (OpenAI's \gptturbo and Anthropic's \claude) language models in settings that require accessing and using information within an input context. We first experiment with multi-document question answering, which requires models to reason over provided documents to find relevant information and use it to answer a given question; this task mimics the retrieval-augmented generation setup underlying many commercial generative search and question answering applications (e.g., Bing Chat).
We make controlled changes to the input context size and the position of the relevant information within the input context and study their effects on model performance. In particular, we can increase the input context length by adding more documents to the input context (akin to retrieving more documents in retrieval-augmented generation), and modify the position of the relevant information within the context by changing the order of the documents in the input context to place the relevant document at the beginning, middle or end of the context.


We observe a distinctive U-shaped performance, which can be clearly visualized in Figure \ref{fig:figure1},  as we vary the position of the relevant information ---language model performance is highest when relevant information occurs at the very beginning or end of its input context, and performance significantly degrades when models must access and use information in the middle of their input context (\S\ref{sec:qa_results}). For example, when relevant information is placed in the middle of its input context, \gptturbo's performance on the multi-document question task is lower than its performance when predicting \emph{without any documents} (i.e., the closed-book setting; 56.1\%).
In addition, we find that model performance steadily degrades on longer contexts (\S\ref{sec:qa_results}), and that extended-context models are not necessarily better at using their input context (\S\ref{sec:qa_results}).

Given that language models struggle to retrieve and use relevant information in the multi-document question answering task, to what extent can language models even \emph{retrieve} from their input contexts? We study this question with a synthetic key-value retrieval task, which is designed to be a minimal testbed for the basic ability to retrieve matching tokens from the input context. In this task, models are given a collection of JSON-formatted key-value pairs, and must return the value associated with a specific key. Similar to the multi-document QA task, the key-value retrieval task also admits controlled changes to the input context length (adding more key-value pairs) and the position of relevant information. We observe a similar U-shaped performance curve in this setting; many models struggle to simply retrieve matching tokens that occur in the middle of their input context.

To better understand why language models struggle to access and use information in the middle of their input contexts, we conduct preliminary investigations into the role of model architecture (decoder-only vs. encoder-decoder), query-aware contextualization, and instruction fine-tuning (\S\ref{sec:why_u_shape}).
We find that encoder-decoder models are relatively robust to changes in the position of relevant information within their input context when evaluated on sequences within its training-time sequence length, but they show a U-shaped curve when evaluated on sequences longer than those seen during training (\S\ref{sec:architecture}). In addition, query-aware contextualization (placing the query before \emph{and} after the documents or key-value pairs) enables models to perform the synthetic key-value task perfectly, but minimally changes trends in multi-document QA (\S\ref{sec:pre_conditioning}).
Finally, even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context.


Lastly, we perform a case study with retriever-reader models on open-domain question answering to better understand the trade-off between adding more information to an input context and increasing the amount of content that the model must reason over (\S\ref{sec:odqa_case_study})---in contrast to our controlled multi-document QA task, where the context always contains exactly one document that answers the question, none or many of the top $k$ documents may contain the answer in the open-domain QA settting.
When retrieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model performance saturates long before retriever recall levels off, indicating that models fail to effectively use additional retrieved documents---using more than 20 retrieved documents only marginally improves performance ($\sim$1.5\% for \gptturbo and $\sim$1\% for claude-1.3).


Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future long-context models. To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data at \href{https://nelsonliu.me/papers/lost-in-the-middle}{nelsonliu.me/papers/lost-in-the-middle}.

\section{Language Models}

We study language models as functions that take a textual input context and return a textual output.
Modern language models are most commonly implemented with Transformers \citep{10.5555/3295222.3295349}.
Transformer language models encode input contexts with self-attention, whose time and memory complexity is quadratic in the length of the input, limiting their application to very long sequences.
As a result, language models are generally pre-trained with relatively small amount of prior context (its \emph{context window}), which accordingly also limits the maximum length of their input contexts.

\paragraph{Increasing language model maximum context length.} Recent advances in hardware (e.g., faster GPUs with more memory) and algorithms (e.g., FlashAttention; \citealp[]{dao2022flashattention}) have driven a rapid increase in language model maximum context length.
OpenAI's \gptfour model (released in March 2023) has a maximum context window of 32K tokens; in May 2023, Claude's context window was expanded from 8K tokens to 100K tokens. In June 2023, OpenAI announced an extended-context version of its \gptturbo model, increasing its context from 4K to 16K tokens. A variety of open-source long context language models have also been recently released: MPT-30B has a maximum context length of 8K tokens, and LongChat-7B has a maximum context length of 16K tokens.
Finally, a variety of recently-proposed architectures model sequences with millions of tokens, raising the potential of further dramatic increases in language model maximum context length \citep[\emph{inter alia}]{gu2022efficiently,fu2023hungry,poli2023hyena,yu2023megabyte}.


\begin{figure*}[t]
\centering
\includegraphics[width=0.9\textwidth]{./figures/qa_example.pdf}
\caption{Example of the multi-document question answering task, with an input context and the desired model answer. The relevant document for correctly answering the request is bolded within the input context.
}\label{fig:qa_example}
\end{figure*}

\begin{figure}[t]
\centering
\includegraphics[width=0.9\columnwidth]{./figures/qa_changing_length.pdf}
\caption{Modulating the input context length of the multi-document question answering example presented in Figure~\ref{fig:qa_example}. Adding additional documents that do not contain the answer increases the length of the input context, but does not affect the desired output. 
The relevant document pair for correctly answering the request is bolded within the input context. 
}\label{fig:qa_changing_length}
\end{figure}

\begin{figure}[t]
\centering
\includegraphics[width=0.9\columnwidth]{./figures/qa_changing_position.pdf}
\caption{Modulating the position of relevant information within the input context for the multi-document question answering example presented in Figure~\ref{fig:qa_example}. Re-ordering the documents in the input context does not affect the desired output. The relevant document for correctly answering the request is bolded within the input context.}\label{fig:qa_changing_position}
\end{figure}

\section{Multi-Document Question Answering}\label{sec:qa}

Our goal is to better understand how language models use their input context.
To this end, we analyze model performance on multi-document question answering, which requires models to find relevant information within an input context and using it to answer the question.
In particular, we make controlled changes to the length of the input context and the position of the relevant information and measure changes in task performance.

\subsection{Experimental Setup}

Our multi-document question answering task closely parallels the retrieval-augmented generation setup underlying commercial search and question answering applications (e.g., Bing Chat).
In these experiments, the model inputs are (i)~a question to answer and (ii)~$k$ documents (e.g., passages from Wikipedia), where \emph{exactly one} the documents contains the answer to the question and $k - 1$ ``distractor'' documents do not. Performing this task requires the model to access the document that contains the answer within its input context and use it to answer the question. 
Figure~\ref{fig:qa_example} presents an example.


\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{./figures/qa.pdf}
\caption{The effect of changing the position of relevant information (document containing the answer) on multi-document question answering performance. Lower positions are closer to the start of the input context. Performance is generally highest when relevant information is positioned at the very start or very end of the context, and rapidly degrades when models must reason over information in the middle of their input context.
}\label{fig:qa_results}
\end{figure*}

We instantiate this task with data from the NaturalQuestions benchmark \citep{kwiatkowski-etal-2019-natural}, which contains historical queries issued to the Google search engine and human-annotated answers extracted from Wikipedia. Specifically, we first take queries from NaturalQuestions-Open \citep{lee-etal-2019-latent}, an open domain question answering benchmark that is derived from NaturalQuestions.
Use use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts.
For each of these queries, we need a document that contains the answer and $k-1$ distractor documents that do not contain the answer.
To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations.
To collect $k-1$ distractor documents that do not contain the answer, we use the Contriever retrieval system \citep{izacard2021contriever} to retrieve the $k-1$ Wikipedia chunks that are most relevant to the question and do not contain any of the NaturalQuestions-annotated answers.\footnote{Ambiguity in NaturalQuestions-Open means that a small number of distractor passages may contain a reasonable answer. We additionally run experiments on subset of unambiguous questions, finding similar results and conclusions; see Appendix~\ref{sec:ambiguity}.} In the input context, the distractor documents are presented in order of decreasing relevance.\footnote{Since there might be a prior over ``search results'' appearing in ranked order, we explored randomly ordering the $k-1$ distractor documents and mentioning that the documents are randomly ordered in the task description, but found the same trends. See Appendix~\ref{sec:qa_random_order} for more details.}

Following \citet{kandpal2022large} and \citet{mallen2023trust}, we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.

To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure~\ref{fig:qa_changing_length}). To modulate the position of relevant information within the input context, we adjust the order of the documents in the input context to change the position of the document that contains the answer (Figure~\ref{fig:qa_changing_position}).

\subsection{Models}\label{sec:models}

We analyze several state-of-the-art open and closed models. We use greedy decoding when generating outputs and leave exploration of other decoding methods to future work. We use a standard set of prompts for each model (depicted in Figure~\ref{fig:qa_example}).

\paragraph{Open models.} We experiment with \mptinstruct, which has a maximum context length of 8192 tokens. The model was initially pre-trained on 1 trilion tokens using 2048-token sequences, followed by an additional sequence length adaptation pre-training phase on 50B tokens using 8192-token sequences.
We also evaluate \longchat \citep{longchat2023}, which builds on LLaMA-13B (original maximum context window from 2048; \citealp{touvron2023llama}) and extends its context window to 16384 by using condensed rotary embeddings before fine-tuning with 16384-token sequences.

\paragraph{Closed models.} We use the OpenAI API to experiment with \gptturbo and \gptturboextended.\footnote{We use the \texttt{0613} model revisions for all OpenAI API experiments.}
\gptturbo has a maximum context length of 4K tokens, and \gptturboextended is a version with an extended maximum context length of 16K tokens.
We evaluate claude-1.3 and claude-1.3-100k with the Anthropic API; claude-1.3 has a maximum context length of 8K tokens, and claude-1.3-100k has an extended context length of 100K tokens.\footnote{We also use the OpenAI API to evaluate \gptfour on a subset of multi-document QA experiments, finding similar results and trends as other models (though with higher absolute performance). Evaluating \gptfour on the full multi-document QA and key-value retrieval experiments would cost upwards of \$6000. See Appendix~\ref{sec:gpt4} for results and discussion.}

\subsection{Results and Discussion}\label{sec:qa_results}
We experiment with input contexts containing 10, 20, and 30 documents (2.7K examples each).
Figure~\ref{fig:qa_results} presents multi-document question answering performance when the position of relevant information within the input context.
To better understand the realistic lower- and upper-bounds on performance, we also evaluate performance on the closed-book and oracle settings.
In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer.
On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question.
\gptturbo and \gptturboextended have the highest closed-book (55\%) and oracle (88\%) performance; see Appendix~\ref{sec:closedbook_oracle} for full closed-book and oracle results on all models.

\paragraph{Model performance is highest when relevant information occurs at the beginning or end of its input context.} As the position of relevant information is changed, we see a distinctive U-shaped curve in model performance---models are much better at identifying and using relevant information that occurs at the very beginning and very end of contexts, and suffer degraded performance when forced to use information within the middle of its input context. For example, \gptturbo's multi-document QA performance can drop by more than 20\%---at its nadir, performance in 20- and 30-document settings is lower than performance without \emph{any} input documents (i.e., closed-book performance; 56.1\%).
These results indicate that current models cannot effectively reason over their entire context window when performing downstream tasks, and that models have an easier time retrieving and using information at the very start or end of their input contexts.


\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{./figures/qa_context_length.pdf}
\caption{Language model performance (averaged across position of relevant information) on the multi-document question answering task decreases as the input context grows longer.}\label{fig:qa_context_length_results}
\end{figure}

\paragraph{Model performance substantially decreases as input contexts grow longer.} On both tasks, model performance degrades as the contexts grow longer, indicating that models struggle to retrieve and use relevant information from long input contexts (Figure~\ref{fig:qa_context_length_results}).

\begin{figure*}[t]
\centering
\includegraphics[width=0.9\textwidth]{./figures/kv_retrieval_example.pdf}
\caption{Example of the key-value retrieval task, with an input context and the desired model output. All keys and values are 128-bit UUIDs, and the goal of the task is to return the value associated with the specified key. The relevant key-value pair for correctly answering the request is bolded within the input context.
}\label{fig:kv_retrieval_example}
\end{figure*}

\begin{figure}[t]
\centering
\includegraphics[width=0.9\columnwidth]{./figures/kv_retrieval_changing_length.pdf}
\caption{Modulating the input context length of the key-value retrieval example presented in Figure~\ref{fig:kv_retrieval_example}. Adding random key-value pairs (128-bit UUIDs) increases length of the input context, but does not affect the desired output. The relevant key-value pair for correctly answering the request is bolded within the input context.
}\label{fig:kv_retrieval_changing_length}
\end{figure}

\begin{figure}[ht]
\centering
\includegraphics[width=0.9\columnwidth]{./figures/kv_retrieval_changing_position.pdf}
\caption{Modulating the position of relevant information within the input context for the key-value retrieval example presented in Figure~\ref{fig:kv_retrieval_example}. Re-ordering the key-value pairs does not affect the desired output. All keys and values are random 128-bit UUIDs. The relevant key-value pair for correctly answering the request is bolded within the input context.}\label{fig:kv_retrieval_changing_position}
\end{figure}

This trend continues when comparing models with their corresponding extended-context versions. For example, \gptturbo's lowest performance in the 20-document setting is 52.9\% (when the document containing the answer is positioned 10th out of 20). The input contexts of the 30-document setting are too long for \gptturbo, but using its extended-context counterpart \gptturboextended also results in performance decrease (49.5\% when the relevant document is positioned 10th out of 30)---although extended-context models can process longer input contexts, they may not be better at reasoning over the information within its context window.

\paragraph{Extended-context models are not necessarily better at using input context.}
In settings where the input context fits in the context window of both a model and its extended-context counterpart, we see that performance between them is nearly identical. For example, the results for \gptturbo and \gptturboextended are nearly superimposed (solid green series and dashed red series, respectively).
These results indicate that models with longer maximum context windows are not necessarily better at using this extended context.

\section{How Well Can Language Models Retrieve From Input Contexts?}\label{sec:kv}

Given that language models struggle to retrieve and use information from the middle of their input contexts in the multi-document question answering task, to what extent can they simply \emph{retrieve} from input contexts?
We study this question with a synthetic key-value retrieval task to isolate and study the basic ability of matching and retrieving relevant information from input contexts.

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{./figures/kv_records.pdf}
\caption{The effect of changing the input context length and the position of relevant information on key-value retrieval performance. Lower positions are closer to the start of the input context. Although some models are largely perfect on this synthetic task (e.g., claude-1.3 and claude-1.3), we see again that performance is often highest when relevant information is occurs at the very start or very end of the context, and rapidly degrades when models must retrieve from the middle of the input context. \longchat in the 140 key-value setting is a notable outlier; when the relevant information is at the start of the input context, it tends to generate code to retrieve the key, rather than outputting the value itself.
}\label{fig:kv_results}
\end{figure*}

\subsection{Experimental Setup}

In our synthetic key-value retrieval task, the inputs are (i)~a string-serialized JSON object with $k$ key-value pairs, where each of the keys and values are unique, randomly-generated UUIDs and (ii)~a particular key within the aforementioned JSON object.
The goal is to return the value associated with the specified key.
Thus, each JSON object contains one relevant key-value pair (where the value is to be retrieved), and $k-1$ irrelevant ``distractor'' key-value pairs.
Figure~\ref{fig:kv_retrieval_example} provides an example input context and its corresponding desired output.
We use accuracy as our evaluation metric, assessing whether the correct value appears in the predicted output.

Our synthetic key-value retrieval task is designed to provide a minimal testbed for the basic ability to retrieve matching tokens from an input context.
This task shares similar goals with the Little Retrieval Test of \citet{littleretrievaltest} and the closely-related fine-grained line retrieval task of \citet{longchat2023}, but we explicitly seek to distill and simplify the task by removing as much natural language semantics as possible (using random UUIDs instead), since language features may present potential confounders (e.g., because Transformer language models may have varying sensitivity to different linguistic features in their input context; \citealp{oconnor-andreas-2021-context}).

To modulate the input context length in this task, we change the number of input JSON key-value pairs $k$ by adding or removing random keys, changing the number of distractor key-value pairs (Figure~\ref{fig:kv_retrieval_changing_length}). To modulate the position of relevant information within the input context, we change the position of the key to retrieve within the serialized JSON object (Figure~\ref{fig:kv_retrieval_changing_position}).


\subsection{Results and Discussion}\label{sec:kv_results}

Figure~\ref{fig:kv_results} presents key-value retrieval performance; We experiment with input contexts containing 75, 140, and 300 key-value pairs (500 examples each). We use the same set of models as the multi-document question answering experiments, see \S\ref{sec:models} for more details.

Although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance---claude-1.3 and claude-1.3-100k do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when retrieving keys from 140 or more key-value pairs.

The results on the key-value retrieval task have largely similar trends to the results on the multi-document question-answering task (excepting models with perfect performance on the key-value retrieval task). In particular, we see the U-shaped performance curve again; model performance is lowest when they must access key-value pairs in the middle of their input context. Furthermore, model performance in this setting generally also decreases on longer input contexts.
\longchat in the 140 key-value setting is a notable outlier; when the relevant information is at the start of the input context, it tends to generate code to retrieve the key, rather than outputting the value itself.

\section{Why Do Language Models Struggle To Use Their Entire Input Context?}\label{sec:why_u_shape}

Our multi-document question answering and key-value retrieval results show that language model performance degrades significantly when they must access relevant information in the middle of long input contexts. To better understand why, we perform some preliminary investigations into the role of model architecture (e.g., decoder-only vs. encoder-decoder), query-aware contextualization, and the effects of instruction fine-tuning.

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/qa_decoder_only_vs_encoder_decoder.pdf}
\caption{Encoder-decoder models (\flanultwo and \flantfive) are relatively robust to changes in the position of relevant information within their input context when evaluated on sequences that are shorter than their encoder's training-time maximum sequence length (2048 and 512 tokens, respectively). However, when these models are evaluated on sequences longer than those seen during training (20- and 30-document settings), they also exhibit a U-shaped performance curve, where performance is much higher when the relevant information occurs at the beginning or end of the input context as opposed to the middle.
}\label{fig:qa_model_architecture}
\end{figure*}

\subsection{Effect of Model Architecture}\label{sec:architecture}

The open models we evaluate in \S\ref{sec:qa} and \S\ref{sec:kv} are all decoder-only models---at each timestep, they may only attend to prior tokens.
To better understand the potential effects of model architecture on how language model use context, we compare decoder-only and encoder-decoder language models.

We experiment with Flan-T5-XXL \citep{JMLR:v21:20-074,chung2022scaling} and Flan-UL2 \citep{tay2023ul2}. Flan-T5-XXL is trained with a sequences of 512 tokens (encoder and decoder). Flan-UL2 is initially trained with sequences of 512 tokens (encoder and decoder), but is then pre-trained for an extra 100K steps with 1024 tokens (encoder and decoder), before instruction-tuning on sequences with 2048 tokens in the encoder and 512 tokens in the decoder.
However, since these models use relative positional embeddings, they can (in principle) extrapolate beyond these maximum context lengths; \citet{shaham2023zeroscrolls} find that both models can perform well with sequences of 8K tokens.

Figure~\ref{fig:qa_model_architecture} juxtaposes the performance of decoder-only and encoder-decoder models. When Flan-UL2 is evaluated on sequences within its 2048 training-time context window, its performance is relatively robust to changes in the position of relevant information within the input context. When evaluated on settings with sequences longer than 2048 tokens, Flan-UL2 performance begins to degrade when relevant information is place in the middle.
Flan-T5-XXL shows a similar trend, where longer input contexts result in a greater performance degradation when placing relevant information in the middle of the input context.

We speculate that encoder-decoder models may make better use of their context windows because their bidirectional encoder allows processing each document in the context of future documents, potentially enhancing relative importance estimation between documents.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/20_total_documents_precondition_with_question.pdf}
\caption{Query-aware contextualization (i.e., placing the question before \emph{and} after the documents in the input context) improves multi-document QA performance when relevant information occurs at the very beginning, but slightly decreases performance otherwise.
}\label{fig:qa_query_preconditioning}
\end{figure}

\subsection{Effect of Query-Aware Contextualization}\label{sec:pre_conditioning}

Our experiments in \S\ref{sec:qa} and \S\ref{sec:kv} place the query (i.e., question to answer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or key-value pairs, since the query only appears at the end of the prompt and decoder-only models can only attend to prior tokens at each timestep. On the other hand, encoder-decoder models use a bidirectional encoder to contextualize input contexts, and seem to be more robust to changes in the position of relevant information in their input context---can use this intuition to also improve the performance of decoder-only models by placing the query before \emph{and} after the data, enabling query-aware contextualization of documents (or key-value pairs)?

We find that query-aware contextualization dramatically improves performance on the key-value retrieval task. For example, \gptturboextended (with query-aware contextualization) achieves perfect performance when evaluated with 300 key-value pairs. In contrast, without query-aware contextualization, it achieves a lowest performance of 45.6\% in the same setting (Figure~\ref{fig:kv_results}).

In contrast, query-aware contextualization minimally affects performance trends in the multi-document question answering task. In particular, it improves performance when the relevant information is located at the very beginning of the input context, but slightly decreases performance in other settings.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/base_vs_instruction_tuned.pdf}
\caption{Multi-document QA performance of \mptinstruct compared against its base model (i.e., before instruction fine-tuning) \mpt.
Both models have a U-shaped performance curve, where performance is much higher when relevant information occurs at the start or end of the input context, indicating that the instruction tuning process itself is not necessarily responsible for these performance trends.
}\label{fig:qa_base_vs_instruction_tuned}
\end{figure}

\subsection{Effect of Instruction-Tuning}\label{sec:instruction_tuning}

All of the models that we evaluated in \S\ref{sec:qa} and \S\ref{sec:kv} are instruction-tuned---after their initial pre-training, they undergo supervised fine-tuning on a dataset of instructions and responses.
In this supervised instruction-tuning data, the task specification and/or instruction is commonly placed at the beginning of the input context, which might lead instruction-tuned language models to place more weight on the start of the input context.

To better understand the potential effects of instruction-tuning on how language models use long input contexts, we compare the multi-document question answering performance of \mptinstruct against its base model (i.e., before instruction fine-tuning) \mpt. We use the same experimental setup as \S\ref{sec:qa}.

Figure~\ref{fig:qa_base_vs_instruction_tuned} compares the multi-document QA performance of \mpt and \mptinstruct as a function of the position of the relevant information in the input context. Surprisingly, we see that both \mpt and \mptinstruct exhibit a U-shaped performance curve, where performance is highest when relevant information occurs at the very beginning or very end of the context. Although the absolute performance of \mptinstruct is uniformly higher than that of \mpt, their overall performance trends are quite similar.

These observations complement prior work, which found that language models are biased towards recent tokens (i.e., the end of the input context; \citealp{khandelwal-etal-2018-sharp,press-etal-2021-shortformer}). This recency bias is generally shown in the context of next-word prediction on contiguous text, where language models minimally benefit from long-range information \citep{sun-etal-2021-long}. In contrast, our results show that language models are capable of using longer-range information (i.e., the beginning of the input context) when prompted with instruction-formatted data. We hypothesize that language models learn to use these contexts from similarly-formatted data that may occur in webtext seen during pre-training, e.g., StackOverflow questions and answers.




\section{Is More Context Is Always Better? A~Case Study With Open-Domain QA}\label{sec:odqa_case_study}

In practical settings, there is often a trade-off with increased the input context length---providing the instruction-tuned language model with more information may help improve downstream task performance, but also increases the amount of content that the model must reason over. Even if a language model can take in 16K tokens, is it actually beneficial to provide 16K tokens of context? The answer to this question is downstream task-specific since it depends on the marginal value of the added context and the model's ability to effectively use long input contexts, but we perform a case study with open-domain question answering on NaturalQuestions-Open to better understand this trade-off.

We use models in a standard retriever-reader setup. A retrieval system (Contriever, fine-tuned on MS-MARCO) takes an input query from NaturalQuestions-Open and returns $k$ documents from Wikipedia. To condition instruction-tuned language models on these retrieved documents, we simply include them in the prompt. We evaluate retriever recall and reader accuracy (whether any of the annotated answers appear in the predicted output) as a function of the number of retrieved documents $k$. We use a subset of NaturalQuestions-Open where the long answer is a paragraph (as opposed to a table or a list).

Figure~\ref{fig:odqa_results} presents open-domain QA results. We see that reader model performance saturates long before retriever performance levels off, indicating that readers are not effectively using the extra context. Using more than 20 retrieved documents only marginally improves reader performance ($\sim$1.5\% for \gptturbo and $\sim$1\% for \claude), while significantly increasing the input context length (and thus latency and cost).
These results, coupled with the observation that models are better at retrieving and using information at the start or end of the input contexts, suggest that effective reranking of retrieved documents (pushing relevant information closer to the start of the input context) or ranked list truncation (returning fewer documents when necessary; \citealp{arampatzis2009stop}) may be promising directions for improving how language-model-based readers use retrieved context.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{./figures/odqa.pdf}
\caption{Retriever recall and model performance as a function of the number of retrieved documents. Model performance saturates long before retriever recall saturates, indicating that the models have difficulty making use of the extra retrieved documents.}\label{fig:odqa_results}
\end{figure}

\section{Related Work}

\subsection{Long-context language models}

There is a rich line of work in designing performant language models with cheaper scaling than Transformers in the context length. 
Many lines of work pursue Transformer variants with attention modifications like recurrence \cite{dai-etal-2019-transformer}, factorizing attention into computationally less intensive approximations \cite{beltagy2020longformer,zaheer2020big}, or low-rank approximations \cite{Wang2020LinformerSW,peng2021random}; see \citet{tay2022efficient} for a comprehensive overview.
\citet{dao2022flashattention} instead provide a faster exact attention by a carefully-crafted IO-aware CUDA kernel.
Separately, there are attempts to do away with attention entire to remove quadratic sequence length complexity, often through convolution and/or linear RNNs, e.g., in RWKV \cite{PENG_RWKV-LM_2021}, S4 \cite{gu2022efficiently}, or Hyena \cite{poli2023hyena}.
Many efforts evaluate perplexity on a diverse web corpus as a proxy for the ability to process long contexts; this work shows that precise knowledge access on long contexts may be an added challenge.

\subsection{How do language models use context?}

The pioneering work of \citet{khandelwal-etal-2018-sharp} showed that small LSTM language models make increasingly coarse use of longer-term context; \citet{sankar2019neural} found similar results in dialogue models. \citet{petroni2020context} were among the first to demonstrate the potential of combining context from an information retrieval system with a pretrained language models for unsupervised question answering.
\citet{oconnor-andreas-2021-context} found that many information-destroying operations had marginal effects on Transformer LMs' predictions.
\citet{krishna2022rankgen} found that long-context neural generation in modestly-sized Transformer language models degenerates because models fail to properly condition on long context.
Finally, studying long-context models, \citet{sun-etal-2021-long} found that longer contexts improves prediction of only a few tokens, an empirical finding consistent with the theory of \citet{sharan2018prediction}, who showed that sequence distributions with bounded mutual information necessarily lead to marginal \textit{average} prediction benefits from increasingly long context.


\subsection{The serial-position effect}
The U-shaped curve we observe in this work has a connection in psychology known as the \textit{serial-position effect} \cite{ebbinghaus1913memory,murdock1962serial}, that states that in free-association recall of elements from a list, humans tend to best remember the first and last elements of the list.
The serial-position effect plays a role in understanding how humans develop short- and long-term memory.
Observing a serial-position-like effect in LLMs is perhaps surprising, since the self-attention mechanisms underlying Transformer LLMs being technically equally capable of retrieving any token from their contexts.

\section{Conclusion}

We empirically study how language models use long input contexts via a series of controlled experiments on two tasks that require identifying and using relevant information in-context: multi-document question answering and key-value retrieval. We find that language models often struggle to use information in the middle of long input contexts, and that performance decreases as the input context grows longer.
We conduct a preliminary investigation of the role of (i)~model architecture, (ii)~query-aware contextualization, and (iii)~instruction-tuning to better understand how each of these factors might affect how language models use context.
Finally, we conclude with a practical case study of open-domain question answering, finding that the performance of language model readers saturates far before retriever recall.
Our results and analysis provide a better understanding of how language models use their input context and provides new evaluation protocols for future long-context models.
de academic access program.

\bibliography{custom}
\bibliographystyle{acl_natbib}

\clearpage

\appendix

\section{Ambiguity in Multi-Document QA Distractor Documents}\label{sec:ambiguity}

Following a variety of past work on NaturalQuestions-Open \citep[\emph{inter alia}]{izacard2021contriever,izacard-grave-2021-leveraging}, we use a standard Wikipedia dump from late 2018 as our retrieval corpus. However, this standard Wikipedia dump has a small amount of temporal mismatch with the data in NaturalQuestions.

For example, consider the question ``what nfl team does robert griffin iii play for''. The NaturalQuestions annotated answer is ``currently a free agent''. However, the Wikipedia retrieval corpus contains the information that he plays for the ``Baltimore Ravens'', since he was released from the team between the Wikipedia dump's timestamp and the NaturalQuestions annotation process.

We use the ambiguity annotations of \citet{min-etal-2020-ambigqa} to create a subset unambiguous questions. Experiments on this unambiguous subset of the data show similar results and conclusions as the experiments on the full questions collection (Figure~\ref{fig:qa_nonambiguous}).

\begin{figure}[h]
\centering
\includegraphics[width=\columnwidth]{figures/20_total_documents_nonambiguous.pdf}
\caption{Language model performance on a unambiguous subset of questions.
}\label{fig:qa_nonambiguous}
\end{figure}


\section{Randomizing Distractor Order in Multi-Document QA}
\label{sec:qa_random_order}

Our prompt instructs the language model to use the provided search results to answer the question. There may be a prior in the pre-training or instruction-tuning data to treat search results as sorted by decreasing relevance (i.e., the documents near the beginning of the input context are more likely to be useful than those at the end). To validate that our conclusions are not simply a byproduct of this bias, we run experiments the modified instruction ``Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). The search results are ordered randomly.''
In addition, we randomly shuffle the $k-1$ distractor documents.

Figure~\ref{fig:qa_random_order} presents the results of this experiment.
We continue to see a U-shaped performance curve, with performance degrading when language models must use information in the middle of their input contexts.
Comparing the results in \S\ref{sec:qa_results} with those when randomizing the distractor order and mentioning such in the prompt, we see that randomization slightly decrases performance when the relevant information is at the very beginning of the context, and slightly increases performance when using information in the middle and end of the context.


\begin{figure}[h]
\centering
\includegraphics[width=\columnwidth]{./figures/20_total_documents_prompt_mention_random_ordering-use_random_ordering.pdf}
\caption{Language model performance when randomizing the order of the distractors (rather than presenting them in order of decreasing relevance) and mentioning as such in the prompt.
}\label{fig:qa_random_order}
\end{figure}

\newpage

\section{\gptfour Performance}
\label{sec:gpt4}

We evaluate \gptfour on a subset of 500 random examples (Figure~\ref{fig:gpt4}). GPT-4 achieves higher absolute performance than any other language model, but still shows a U-shaped performance curve---its performance is highest when relevant information occurs at the very start or end of the context, and performance degrades when it must use information in the middle of its input context.

\begin{figure}[h]
\centering
\includegraphics[width=\columnwidth]{figures/20_total_documents_500_examples.pdf}
\caption{Although \gptfour has higher absolute performance than other models, its performance still degrades when relevant information occurs in the middle of the input context.
}\label{fig:gpt4}
\end{figure}

\section{Closed-book and Oracle Performance}\label{sec:closedbook_oracle}

Table~\ref{tab:closedbook_and_oracle} presents language model performance on the closed-book and oracle settings for multi-document question answering.
In the closed-book setting, language models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer.
In the oracle setting, language models are given the single document that contains the answer, and must use it to answer the question. This represents an upper-bound on task performance.

\begin{table}[h]
    \footnotesize
    \centering
    \begin{tabular}{@{}lrr@{}}
\toprule
Model & Closed-Book & Oracle  \\
\midrule
    \longchat & 35.0\% & 83.35\% \\
    \mptinstruct & 31.5\% & 81.9\% \\
    \gptturbo & 56.1\% & 88.3 \\
    \gptturboextended & 56.0\% & 88.6 \\
    \claude & 48.3\% & 76.1\% \\
    \claudeextended & 48.2\% & 76.4\% \\
    \bottomrule
    \end{tabular}
    \caption{Closed-book and oracle accuracy of language models on the multi-document question answering task.}
    \label{tab:closedbook_and_oracle}
\end{table}
 
'''