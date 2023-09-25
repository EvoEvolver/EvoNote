sample_html=r"""
<!DOCTYPE html>
<html lang="en" dir="auto">

<head><meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="robots" content="index, follow">
<title>LLM Powered Autonomous Agents | Lil&#39;Log</title>
<meta name="keywords" content="nlp, language-model, agent, steerability, prompting" />
<meta name="description" content="Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
Agent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent&rsquo;s brain, complemented by several key components:">
<meta name="author" content="Lilian Weng">
<link rel="canonical" href="https://lilianweng.github.io/posts/2023-06-23-agent/" />
<link crossorigin="anonymous" href="/assets/css/stylesheet.min.67a6fb6e33089cb29e856bcc95d7aa39f70049a42b123105531265a0d9f1258b.css" integrity="sha256-Z6b7bjMInLKehWvMldeqOfcASaQrEjEFUxJloNnxJYs=" rel="preload stylesheet" as="style">
<script defer crossorigin="anonymous" src="/assets/js/highlight.min.7680afc38aa6b15ddf158a4f3780b7b1f7dde7e91d26f073e6229bb7a0793c92.js" integrity="sha256-doCvw4qmsV3fFYpPN4C3sffd5&#43;kdJvBz5iKbt6B5PJI="
    onload="hljs.initHighlightingOnLoad();"></script>
<link rel="icon" href="https://lilianweng.github.io/favicon_peach.ico">
<link rel="icon" type="image/png" sizes="16x16" href="https://lilianweng.github.io/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://lilianweng.github.io/favicon-32x32.png">
<link rel="apple-touch-icon" href="https://lilianweng.github.io/apple-touch-icon.png">
<link rel="mask-icon" href="https://lilianweng.github.io/safari-pinned-tab.svg">
<meta name="theme-color" content="#2e2e33">
<meta name="msapplication-TileColor" content="#2e2e33">
<noscript>
    <style>
        #theme-toggle,
        .top-link {
            display: none;
        }

    </style>
    <style>
        @media (prefers-color-scheme: dark) {
            :root {
                --theme: rgb(29, 30, 32);
                --entry: rgb(46, 46, 51);
                --primary: rgb(218, 218, 219);
                --secondary: rgb(155, 156, 157);
                --tertiary: rgb(65, 66, 68);
                --content: rgb(196, 196, 197);
                --hljs-bg: rgb(46, 46, 51);
                --code-bg: rgb(55, 56, 62);
                --border: rgb(51, 51, 51);
            }

            .list {
                background: var(--theme);
            }

            .list:not(.dark)::-webkit-scrollbar-track {
                background: 0 0;
            }

            .list:not(.dark)::-webkit-scrollbar-thumb {
                border-color: var(--theme);
            }
        }

    </style>
</noscript>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HFT45VFBX6"></script>
<script>
var doNotTrack = false;
if (!doNotTrack) {
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config', 'G-HFT45VFBX6', { 'anonymize_ip': false });
}
</script>
<meta property="og:title" content="LLM Powered Autonomous Agents" />
<meta property="og:description" content="Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
Agent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent&rsquo;s brain, complemented by several key components:" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://lilianweng.github.io/posts/2023-06-23-agent/" /><meta property="article:section" content="posts" />
<meta property="article:published_time" content="2023-06-23T00:00:00&#43;00:00" />
<meta property="article:modified_time" content="2023-06-23T00:00:00&#43;00:00" />

<meta name="twitter:card" content="summary"/>
<meta name="twitter:title" content="LLM Powered Autonomous Agents"/>
<meta name="twitter:description" content="Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
Agent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent&rsquo;s brain, complemented by several key components:"/>


<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position":  1 ,
      "name": "Posts",
      "item": "https://lilianweng.github.io/posts/"
    }, 
    {
      "@type": "ListItem",
      "position":  2 ,
      "name": "LLM Powered Autonomous Agents",
      "item": "https://lilianweng.github.io/posts/2023-06-23-agent/"
    }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "LLM Powered Autonomous Agents",
  "name": "LLM Powered Autonomous Agents",
  "description": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent\u0026rsquo;s brain, complemented by several key components:",
  "keywords": [
    "nlp", "language-model", "agent", "steerability", "prompting"
  ],
  "articleBody": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:\n Planning  Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks. Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results.   Memory  Short-term memory: I would consider all the in-context learning (See Prompt Engineering) as utilizing short-term memory of the model to learn. Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval.   Tool use  The agent learns to call external APIs for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources and more.    Fig. 1. Overview of a LLM-powered autonomous agent system. Component One: Planning A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.\nTree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like \"Steps for XYZ.\\n1.\", \"What are the subgoals for achieving XYZ?\", (2) by using task-specific instructions; e.g. \"Write a story outline.\" for writing a novel, or (3) with human inputs.\nAnother quite distinct approach, LLM+P (Liu et al. 2023), involves relying on an external classical planner to do long-horizon planning. This approach utilizes the Planning Domain Definition Language (PDDL) as an intermediate interface to describe the planning problem. In this process, LLM (1) translates the problem into “Problem PDDL”, then (2) requests a classical planner to generate a PDDL plan based on an existing “Domain PDDL”, and finally (3) translates the PDDL plan back into natural language. Essentially, the planning step is outsourced to an external tool, assuming the availability of domain-specific PDDL and a suitable planner which is common in certain robotic setups but not in many other domains.\nSelf-Reflection Self-reflection is a vital aspect that allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. It plays a crucial role in real-world tasks where trial and error are inevitable.\nReAct (Yao et al. 2023) integrates reasoning and acting within LLM by extending the action space to be a combination of task-specific discrete actions and the language space. The former enables LLM to interact with the environment (e.g. use Wikipedia search API), while the latter prompting LLM to generate reasoning traces in natural language.\nThe ReAct prompt template incorporates explicit steps for LLM to think, roughly formatted as:\nThought: ... Action: ... Observation: ... ... (Repeated many times) Fig. 2. Examples of reasoning trajectories for knowledge-intensive tasks (e.g. HotpotQA, FEVER) and decision-making tasks (e.g. AlfWorld Env, WebShop). (Image source: Yao et al. 2023). In both experiments on knowledge-intensive tasks and decision-making tasks, ReAct works better than the Act-only baseline where Thought: … step is removed.\nReflexion (Shinn \u0026 Labash 2023) is a framework to equips agents with dynamic memory and self-reflection capabilities to improve reasoning skills. Reflexion has a standard RL setup, in which the reward model provides a simple binary reward and the action space follows the setup in ReAct where the task-specific action space is augmented with language to enable complex reasoning steps. After each action $a_t$, the agent computes a heuristic $h_t$ and optionally may decide to reset the environment to start a new trial depending on the self-reflection results.\nFig. 3. Illustration of the Reflexion framework. (Image source: Shinn \u0026 Labash, 2023) The heuristic function determines when the trajectory is inefficient or contains hallucination and should be stopped. Inefficient planning refers to trajectories that take too long without success. Hallucination is defined as encountering a sequence of consecutive identical actions that lead to the same observation in the environment.\nSelf-reflection is created by showing two-shot examples to LLM and each example is a pair of (failed trajectory, ideal reflection for guiding future changes in the plan). Then reflections are added into the agent’s working memory, up to three, to be used as context for querying LLM.\nFig. 4. Experiments on AlfWorld Env and HotpotQA. Hallucination is a more common failure than inefficient planning in AlfWorld. (Image source: Shinn \u0026 Labash, 2023) Chain of Hindsight (CoH; Liu et al. 2023) encourages the model to improve on its own outputs by explicitly presenting it with a sequence of past outputs, each annotated with feedback. Human feedback data is a collection of $D_h = \\{(x, y_i , r_i , z_i)\\}_{i=1}^n$, where $x$ is the prompt, each $y_i$ is a model completion, $r_i$ is the human rating of $y_i$, and $z_i$ is the corresponding human-provided hindsight feedback. Assume the feedback tuples are ranked by reward, $r_n \\geq r_{n-1} \\geq \\dots \\geq r_1$ The process is supervised fine-tuning where the data is a sequence in the form of $\\tau_h = (x, z_i, y_i, z_j, y_j, \\dots, z_n, y_n)$, where $\\leq i \\leq j \\leq n$. The model is finetuned to only predict $y_n$ where conditioned on the sequence prefix, such that the model can self-reflect to produce better output based on the feedback sequence. The model can optionally receive multiple rounds of instructions with human annotators at test time.\nTo avoid overfitting, CoH adds a regularization term to maximize the log-likelihood of the pre-training dataset. To avoid shortcutting and copying (because there are many common words in feedback sequences), they randomly mask 0% - 5% of past tokens during training.\nThe training dataset in their experiments is a combination of WebGPT comparisons, summarization from human feedback and human preference dataset.\nFig. 5. After fine-tuning with CoH, the model can follow instructions to produce outputs with incremental improvement in a sequence. (Image source: Liu et al. 2023) The idea of CoH is to present a history of sequentially improved outputs in context and train the model to take on the trend to produce better outputs. Algorithm Distillation (AD; Laskin et al. 2023) applies the same idea to cross-episode trajectories in reinforcement learning tasks, where an algorithm is encapsulated in a long history-conditioned policy. Considering that an agent interacts with the environment many times and in each episode the agent gets a little better, AD concatenates this learning history and feeds that into the model. Hence we should expect the next predicted action to lead to better performance than previous trials. The goal is to learn the process of RL instead of training a task-specific policy itself.\nFig. 6. Illustration of how Algorithm Distillation (AD) works. (Image source: Laskin et al. 2023). The paper hypothesizes that any algorithm that generates a set of learning histories can be distilled into a neural network by performing behavioral cloning over actions. The history data is generated by a set of source policies, each trained for a specific task. At the training stage, during each RL run, a random task is sampled and a subsequence of multi-episode history is used for training, such that the learned policy is task-agnostic.\nIn reality, the model has limited context window length, so episodes should be short enough to construct multi-episode history. Multi-episodic contexts of 2-4 episodes are necessary to learn a near-optimal in-context RL algorithm. The emergence of in-context RL requires long enough context.\nIn comparison with three baselines, including ED (expert distillation, behavior cloning with expert trajectories instead of learning history), source policy (used for generating trajectories for distillation by UCB), RL^2 (Duan et al. 2017; used as upper bound since it needs online RL), AD demonstrates in-context RL with performance getting close to RL^2 despite only using offline RL and learns much faster than other baselines. When conditioned on partial training history of the source policy, AD also improves much faster than ED baseline.\nFig. 7. Comparison of AD, ED, source policy and RL^2 on environments that require memory and exploration. Only binary reward is assigned. The source policies are trained with A3C for \"dark\" environments and DQN for watermaze.(Image source: Laskin et al. 2023) Component Two: Memory (Big thank you to ChatGPT for helping me draft this section. I’ve learned a lot about the human brain and data structure for fast MIPS in my conversations with ChatGPT.)\nTypes of Memory Memory can be defined as the processes used to acquire, store, retain, and later retrieve information. There are several types of memory in human brains.\n  Sensory Memory: This is the earliest stage of memory, providing the ability to retain impressions of sensory information (visual, auditory, etc) after the original stimuli have ended. Sensory memory typically only lasts for up to a few seconds. Subcategories include iconic memory (visual), echoic memory (auditory), and haptic memory (touch).\n  Short-Term Memory (STM) or Working Memory: It stores information that we are currently aware of and needed to carry out complex cognitive tasks such as learning and reasoning. Short-term memory is believed to have the capacity of about 7 items (Miller 1956) and lasts for 20-30 seconds.\n  Long-Term Memory (LTM): Long-term memory can store information for a remarkably long time, ranging from a few days to decades, with an essentially unlimited storage capacity. There are two subtypes of LTM:\n Explicit / declarative memory: This is memory of facts and events, and refers to those memories that can be consciously recalled, including episodic memory (events and experiences) and semantic memory (facts and concepts). Implicit / procedural memory: This type of memory is unconscious and involves skills and routines that are performed automatically, like riding a bike or typing on a keyboard.    Fig. 8. Categorization of human memory. We can roughly consider the following mappings:\n Sensory memory as learning embedding representations for raw inputs, including text, image or other modalities; Short-term memory as in-context learning. It is short and finite, as it is restricted by the finite context window length of Transformer. Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval.  Maximum Inner Product Search (MIPS) The external memory can alleviate the restriction of finite attention span. A standard practice is to save the embedding representation of information into a vector store database that can support fast maximum inner-product search (MIPS). To optimize the retrieval speed, the common choice is the approximate nearest neighbors (ANN)​ algorithm to return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup.\nA couple common choices of ANN algorithms for fast MIPS:\n LSH (Locality-Sensitive Hashing): It introduces a hashing function such that similar input items are mapped to the same buckets with high probability, where the number of buckets is much smaller than the number of inputs. ANNOY (Approximate Nearest Neighbors Oh Yeah): The core data structure are random projection trees, a set of binary trees where each non-leaf node represents a hyperplane splitting the input space into half and each leaf stores one data point. Trees are built independently and at random, so to some extent, it mimics a hashing function. ANNOY search happens in all the trees to iteratively search through the half that is closest to the query and then aggregates the results. The idea is quite related to KD tree but a lot more scalable. HNSW (Hierarchical Navigable Small World): It is inspired by the idea of small world networks where most nodes can be reached by any other nodes within a small number of steps; e.g. “six degrees of separation” feature of social networks. HNSW builds hierarchical layers of these small-world graphs, where the bottom layers contain the actual data points. The layers in the middle create shortcuts to speed up search. When performing a search, HNSW starts from a random node in the top layer and navigates towards the target. When it can’t get any closer, it moves down to the next layer, until it reaches the bottom layer. Each move in the upper layers can potentially cover a large distance in the data space, and each move in the lower layers refines the search quality. FAISS (Facebook AI Similarity Search): It operates on the assumption that in high dimensional space, distances between nodes follow a Gaussian distribution and thus there should exist clustering of data points. FAISS applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters. Search first looks for cluster candidates with coarse quantization and then further looks into each cluster with finer quantization. ScaNN (Scalable Nearest Neighbors): The main innovation in ScaNN is anisotropic vector quantization. It quantizes a data point $x_i$ to $\\tilde{x}_i$ such that the inner product $\\langle q, x_i \\rangle$ is as similar to the original distance of $\\angle q, \\tilde{x}_i$ as possible, instead of picking the closet quantization centroid points.  Fig. 9. Comparison of MIPS algorithms, measured in recall@10. (Image source: Google Blog, 2020) Check more MIPS algorithms and performance comparison in ann-benchmarks.com.\nComponent Three: Tool Use Tool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities.\nFig. 10. A picture of a sea otter using rock to crack open a seashell, while floating in the water. While some other animals can use tools, the complexity is not comparable with humans. (Image source: Animals using tools) MRKL (Karpas et al. 2022), short for “Modular Reasoning, Knowledge and Language”, is a neuro-symbolic architecture for autonomous agents. A MRKL system is proposed to contain a collection of “expert” modules and the general-purpose LLM works as a router to route inquiries to the best suitable expert module. These modules can be neural (e.g. deep learning models) or symbolic (e.g. math calculator, currency converter, weather API).\nThey did an experiment on fine-tuning LLM to call a calculator, using arithmetic as a test case. Their experiments showed that it was harder to solve verbal math problems than explicitly stated math problems because LLMs (7B Jurassic1-large model) failed to extract the right arguments for the basic arithmetic reliably. The results highlight when the external symbolic tools can work reliably, knowing when to and how to use the tools are crucial, determined by the LLM capability.\nBoth TALM (Tool Augmented Language Models; Parisi et al. 2022) and Toolformer (Schick et al. 2023) fine-tune a LM to learn to use external tool APIs. The dataset is expanded based on whether a newly added API call annotation can improve the quality of model outputs. See more details in the “External APIs” section of Prompt Engineering.\nChatGPT Plugins and OpenAI API function calling are good examples of LLMs augmented with tool use capability working in practice. The collection of tool APIs can be provided by other developers (as in Plugins) or self-defined (as in function calls).\nHuggingGPT (Shen et al. 2023) is a framework to use ChatGPT as the task planner to select models available in HuggingFace platform according to the model descriptions and summarize the response based on the execution results.\nFig. 11. Illustration of how HuggingGPT works. (Image source: Shen et al. 2023) The system comprises of 4 stages:\n(1) Task planning: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.\nInstruction:\nThe AI assistant can parse user input to several tasks: [{\"task\": task, \"id\", task_id, \"dep\": dependency_task_ids, \"args\": {\"text\": text, \"image\": URL, \"audio\": URL, \"video\": URL}}]. The \"dep\" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag \"-task_id\" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can't be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.  (2) Model selection: LLM distributes the tasks to expert models, where the request is framed as a multiple-choice question. LLM is presented with a list of models to choose from. Due to the limited context length, task type based filtration is needed.\nInstruction:\nGiven the user request and the call command, the AI assistant helps the user to select a suitable model from a list of models to process the user request. The AI assistant merely outputs the model id of the most appropriate model. The output must be in a strict JSON format: \"id\": \"id\", \"reason\": \"your detail reason for the choice\". We have a list of models for you to choose from {{ Candidate Models }}. Please select one model from the list.  (3) Task execution: Expert models execute on the specific tasks and log results.\nInstruction:\nWith the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.  (4) Response generation: LLM receives the execution results and provides summarized results to users.\nTo put HuggingGPT into real world usage, a couple challenges need to solve: (1) Efficiency improvement is needed as both LLM inference rounds and interactions with other models slow down the process; (2) It relies on a long context window to communicate over complicated task content; (3) Stability improvement of LLM outputs and external model services.\nAPI-Bank (Li et al. 2023) is a benchmark for evaluating the performance of tool-augmented LLMs. It contains 53 commonly used API tools, a complete tool-augmented LLM workflow, and 264 annotated dialogues that involve 568 API calls. The selection of APIs is quite diverse, including search engines, calculator, calendar queries, smart home control, schedule management, health data management, account authentication workflow and more. Because there are a large number of APIs, LLM first has access to API search engine to find the right API to call and then uses the corresponding documentation to make a call.\nFig. 12. Pseudo code of how LLM makes an API call in API-Bank. (Image source: Li et al. 2023) In the API-Bank workflow, LLMs need to make a couple of decisions and at each step we can evaluate how accurate that decision is. Decisions include:\n Whether an API call is needed. Identify the right API to call: if not good enough, LLMs need to iteratively modify the API inputs (e.g. deciding search keywords for Search Engine API). Response based on the API results: the model can choose to refine and call again if results are not satisfied.  This benchmark evaluates the agent’s tool use capabilities at three levels:\n Level-1 evaluates the ability to call the API. Given an API’s description, the model needs to determine whether to call a given API, call it correctly, and respond properly to API returns. Level-2 examines the ability to retrieve the API. The model needs to search for possible APIs that may solve the user’s requirement and learn how to use them by reading documentation. Level-3 assesses the ability to plan API beyond retrieve and call. Given unclear user requests (e.g. schedule group meetings, book flight/hotel/restaurant for a trip), the model may have to conduct multiple API calls to solve it.  Case Studies Scientific Discovery Agent ChemCrow (Bran et al. 2023) is a domain-specific example in which LLM is augmented with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design. The workflow, implemented in LangChain, reflects what was previously described in the ReAct and MRKLs and combines CoT reasoning with tools relevant to the tasks:\n The LLM is provided with a list of tool names, descriptions of their utility, and details about the expected input/output. It is then instructed to answer a user-given prompt using the tools provided when necessary. The instruction suggests the model to follow the ReAct format - Thought, Action, Action Input, Observation.  One interesting observation is that while the LLM-based evaluation concluded that GPT-4 and ChemCrow perform nearly equivalently, human evaluations with experts oriented towards the completion and chemical correctness of the solutions showed that ChemCrow outperforms GPT-4 by a large margin. This indicates a potential problem with using LLM to evaluate its own performance on domains that requires deep expertise. The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.\nBoiko et al. (2023) also looked into LLM-empowered agents for scientific discovery, to handle autonomous design, planning, and performance of complex scientific experiments. This agent can use tools to browse the Internet, read documentation, execute code, call robotics experimentation APIs and leverage other LLMs.\nFor example, when requested to \"develop a novel anticancer drug\", the model came up with the following reasoning steps:\n inquired about current trends in anticancer drug discovery; selected a target; requested a scaffold targeting these compounds; Once the compound was identified, the model attempted its synthesis.  They also discussed the risks, especially with illicit drugs and bioweapons. They developed a test set containing a list of known chemical weapon agents and asked the agent to synthesize them. 4 out of 11 requests (36%) were accepted to obtain a synthesis solution and the agent attempted to consult documentation to execute the procedure. 7 out of 11 were rejected and among these 7 rejected cases, 5 happened after a Web search while 2 were rejected based on prompt only.\nGenerative Agents Simulation Generative Agents (Park, et al. 2023) is super fun experiment where 25 virtual characters, each controlled by a LLM-powered agent, are living and interacting in a sandbox environment, inspired by The Sims. Generative agents create believable simulacra of human behavior for interactive applications.\nThe design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.\n Memory stream: is a long-term memory module (external database) that records a comprehensive list of agents' experience in natural language.  Each element is an observation, an event directly provided by the agent. - Inter-agent communication can trigger new natural language statements.   Retrieval model: surfaces the context to inform the agent’s behavior, according to relevance, recency and importance.  Recency: recent events have higher scores Importance: distinguish mundane from core memories. Ask LM directly. Relevance: based on how related it is to the current situation / query.   Reflection mechanism: synthesizes memories into higher level inferences over time and guides the agent’s future behavior. They are higher-level summaries of past events (self-reflection above)  Prompt LM with 100 most recent observations and to generate 3 most salient high-level questions given a set of observations/statements. Then ask LM to answer those questions.   Planning \u0026 Reacting: translate the reflections and the environment information into actions  Planning is essentially in order to optimize believability at the moment vs in time. Prompt template: {Intro of an agent X}. Here is X's plan today in broad strokes: 1) Relationships between agents and observations of one agent by another are all taken into consideration for planning and reacting. Environment information is present in a tree structure.    Fig. 13. The generative agent architecture. (Image source: Park et al. 2023) This fun simulation results in emergent social behavior, such as information diffusion, relationship memory (e.g. two agents continuing the conversation topic) and coordination of social events (e.g. host a party and invite many others).\nProof-of-Concept Examples AutoGPT has drawn a lot of attention into the possibility of setting up autonomous agents with LLM as the main controller. It has quite a lot of reliability issues given the natural language interface, but nevertheless a cool proof-of-concept demo. A lot of code in AutoGPT is about format parsing.\nHere is the system message used by AutoGPT, where {{...}} are user inputs:\nYou are {{ai-name}}, {{user-provided AI bot description}}. Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications. GOALS: 1. {{user-provided goal 1}} 2. {{user-provided goal 2}} 3. ... 4. ... 5. ... Constraints: 1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files. 2. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember. 3. No user assistance 4. Exclusively use the commands listed in double quotes e.g. \"command name\" 5. Use subprocesses for commands that will not terminate within a few minutes Commands: 1. Google Search: \"google\", args: \"input\": \"\" 2. Browse Website: \"browse_website\", args: \"url\": \"\", \"question\": \"\" 3. Start GPT Agent: \"start_agent\", args: \"name\": \"\", \"task\": \"\", \"prompt\": \"\" 4. Message GPT Agent: \"message_agent\", args: \"key\": \"\", \"message\": \"\" 5. List GPT Agents: \"list_agents\", args: 6. Delete GPT Agent: \"delete_agent\", args: \"key\": \"\" 7. Clone Repository: \"clone_repository\", args: \"repository_url\": \"\", \"clone_path\": \"\" 8. Write to file: \"write_to_file\", args: \"file\": \"\", \"text\": \"\" 9. Read file: \"read_file\", args: \"file\": \"\" 10. Append to file: \"append_to_file\", args: \"file\": \"\", \"text\": \"\" 11. Delete file: \"delete_file\", args: \"file\": \"\" 12. Search Files: \"search_files\", args: \"directory\": \"\" 13. Analyze Code: \"analyze_code\", args: \"code\": \"\" 14. Get Improved Code: \"improve_code\", args: \"suggestions\": \"\", \"code\": \"\" 15. Write Tests: \"write_tests\", args: \"code\": \"\", \"focus\": \"\" 16. Execute Python File: \"execute_python_file\", args: \"file\": \"\" 17. Generate Image: \"generate_image\", args: \"prompt\": \"\" 18. Send Tweet: \"send_tweet\", args: \"text\": \"\" 19. Do Nothing: \"do_nothing\", args: 20. Task Complete (Shutdown): \"task_complete\", args: \"reason\": \"\" Resources: 1. Internet access for searches and information gathering. 2. Long Term memory management. 3. GPT-3.5 powered Agents for delegation of simple tasks. 4. File output. Performance Evaluation: 1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities. 2. Constructively self-criticize your big-picture behavior constantly. 3. Reflect on past decisions and strategies to refine your approach. 4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps. You should only respond in JSON format as described below Response Format: { \"thoughts\": { \"text\": \"thought\", \"reasoning\": \"reasoning\", \"plan\": \"- short bulleted\\n- list that conveys\\n- long-term plan\", \"criticism\": \"constructive self-criticism\", \"speak\": \"thoughts summary to say to user\" }, \"command\": { \"name\": \"command name\", \"args\": { \"arg name\": \"value\" } } } Ensure the response can be parsed by Python json.loads GPT-Engineer is another project to create a whole repository of code given a task specified in natural language. The GPT-Engineer is instructed to think over a list of smaller components to build and ask for user input to clarify questions as needed.\nHere are a sample conversation for task clarification sent to OpenAI ChatCompletion endpoint used by GPT-Engineer. The user inputs are wrapped in {{user input text}}.\n[ { \"role\": \"system\", \"content\": \"You will read instructions and not carry them out, only seek to clarify them.\\nSpecifically you will first summarise a list of super short bullets of areas that need clarification.\\nThen you will pick one clarifying question, and wait for an answer from the user.\\n\" }, { \"role\": \"user\", \"content\": \"We are writing {{a Super Mario game in python. MVC components split in separate files. Keyboard control.}}\\n\" }, { \"role\": \"assistant\", \"content\": \"Summary of areas that need clarification:\\n1. Specifics of the Super Mario game (e.g. level design, characters, gameplay mechanics)\\n2. Details about the MVC components (e.g. which components are in each file)\\n3. Keyboard control implementation (e.g. which keys to use, how to handle input)\\n\\nClarifying question:\\nCan you provide more details about the Super Mario game, such as level design, characters, and gameplay mechanics?\" }, { \"role\": \"user\", \"content\": \"{{There are 10 levels in total. The main character is a plumber named Mario, who can walk and jump. It is a classical platform game just like Super Mario. The main character moves from left to right, trying to get to the destination, where there are many obstacles and attacks from enemies in the process.}}\\n\\nIs anything else unclear? If yes, only answer in the form:\\n{remaining unclear areas} remaining questions.\\n{Next question}\\nIf everything is sufficiently clear, only answer \\\"Nothing more to clarify.\\\".\" }, { \"role\": \"assistant\", \"content\": \"Remaining unclear areas: 2 remaining questions.\\nCan you provide more information about how the MVC components are split into separate files?\" }, { \"role\": \"user\", \"content\": \"{{Make your own assumptions and state them explicitly before starting}}\" } ] Then after these clarification, the agent moved into the code writing mode with a different system message. System message:\nYou will get instructions for code to write. You will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code. Make sure that every detail of the architecture is, in the end, implemented as code. Think step by step and reason yourself to the right decisions to make sure we get it right. You will first lay out the names of the core classes, functions, methods that will be necessary, as well as a quick comment on their purpose.\nThen you will output the content of each file including ALL code. Each file must strictly follow a markdown code block format, where the following tokens must be replaced such that FILENAME is the lowercase file name including the file extension, LANG is the markup code block language for the code’s language, and CODE is the code:\nFILENAME\nCODE You will start with the “entrypoint” file, then go to the ones that are imported by that file, and so on. Please note that the code should be fully functional. No placeholders.\nFollow a language and framework appropriate best practice file naming convention. Make sure that files contain all imports, types etc. Make sure that code in different files are compatible with each other. Ensure to implement all code, if you are unsure, write a plausible implementation. Include module dependency or package manager dependency definition file. Before you finish, double check that all parts of the architecture is present in the files.\nUseful to know: You almost always put different classes in different files. For Python, you always create an appropriate requirements.txt file. For NodeJS, you always create an appropriate package.json file. You always add a comment briefly describing the purpose of the function definition. You try to add comments explaining very complex bits of logic. You always follow the best practices for the requested languages in terms of describing the code written as a defined package/project.\nPython toolbelt preferences:\n pytest dataclasses   Conversatin samples:\n[ { \"role\": \"system\", \"content\": \"You will get instructions for code to write.\\nYou will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.\\nMake sure that every detail of the architecture is, in the end, implemented as code.\\n\\nThink step by step and reason yourself to the right decisions to make sure we get it right.\\nYou will first lay out the names of the core classes, functions, methods that will be necessary, as well as a quick comment on their purpose.\\n\\nThen you will output the content of each file including ALL code.\\nEach file must strictly follow a markdown code block format, where the following tokens must be replaced such that\\nFILENAME is the lowercase file name including the file extension,\\nLANG is the markup code block language for the code's language, and CODE is the code:\\n\\nFILENAME\\n```LANG\\nCODE\\n```\\n\\nYou will start with the \\\"entrypoint\\\" file, then go to the ones that are imported by that file, and so on.\\nPlease note that the code should be fully functional. No placeholders.\\n\\nFollow a language and framework appropriate best practice file naming convention.\\nMake sure that files contain all imports, types etc. Make sure that code in different files are compatible with each other.\\nEnsure to implement all code, if you are unsure, write a plausible implementation.\\nInclude module dependency or package manager dependency definition file.\\nBefore you finish, double check that all parts of the architecture is present in the files.\\n\\nUseful to know:\\nYou almost always put different classes in different files.\\nFor Python, you always create an appropriate requirements.txt file.\\nFor NodeJS, you always create an appropriate package.json file.\\nYou always add a comment briefly describing the purpose of the function definition.\\nYou try to add comments explaining very complex bits of logic.\\nYou always follow the best practices for the requested languages in terms of describing the code written as a defined\\npackage/project.\\n\\n\\nPython toolbelt preferences:\\n- pytest\\n- dataclasses\\n\" }, # … same conversation as earlier, ended with \"Make your own assumptions and state them explicitly before starting\". { \"role\": \"assistant\", \"content\": \"Assumptions:\\n1. Model: The model will contain the game's data, such as level information, character states, and enemy positions.\\n2. View: The view will handle the game's visuals, including rendering the game objects, backgrounds, and updating the display.\\n3. Controller: The controller will manage user input, such as keyboard controls, and update the model accordingly.\\n\\nWith these assumptions in mind, is there any specific aspect of the keyboard control implementation you would like me to clarify?\" }, { \"role\": \"user\", \"content\": \"Please now remember the steps:\\n\\nThink step by step and reason yourself to the right decisions to make sure we get it right.\\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\\n\\nThen you will output the content of each file including ALL code.\\nEach file must strictly follow a markdown code block format, where the following tokens must be replaced such that\\nFILENAME is the lowercase file name including the file extension,\\nLANG is the markup code block language for the code's language, and CODE is the code:\\n\\nFILENAME\\n```LANG\\nCODE\\n```\\n\\nPlease note that the code should be fully functional. No placeholders.\\n\\nYou will start with the \\\"entrypoint\\\" file, then go to the ones that are imported by that file, and so on.\\nFollow a language and framework appropriate best practice file naming convention.\\nMake sure that files contain all imports, types etc. The code should be fully functional. Make sure that code in different files are compatible with each other.\\nBefore you finish, double check that all parts of the architecture is present in the files.\\n\" } ] Challenges After going through key ideas and demos of building LLM-centered agents, I start to see a couple common limitations:\n  Finite context length: The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention.\n  Challenges in long-term planning and task decomposition: Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.\n  Reliability of natural language interface: Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output.\n  Citation Cited as:\n Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents\". Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.\n Or\n@article{weng2023prompt, title = \"LLM-powered Autonomous Agents\"\", author = \"Weng, Lilian\", journal = \"lilianweng.github.io\", year = \"2023\", month = \"Jun\", url = \"https://lilianweng.github.io/posts/2023-06-23-agent/\" } References [1] Wei et al. “Chain of thought prompting elicits reasoning in large language models.\" NeurIPS 2022\n[2] Yao et al. “Tree of Thoughts: Dliberate Problem Solving with Large Language Models.\" arXiv preprint arXiv:2305.10601 (2023).\n[3] Liu et al. “Chain of Hindsight Aligns Language Models with Feedback “ arXiv preprint arXiv:2302.02676 (2023).\n[4] Liu et al. “LLM+P: Empowering Large Language Models with Optimal Planning Proficiency” arXiv preprint arXiv:2304.11477 (2023).\n[5] Yao et al. “ReAct: Synergizing reasoning and acting in language models.\" ICLR 2023.\n[6] Google Blog. “Announcing ScaNN: Efficient Vector Similarity Search” July 28, 2020.\n[7] https://chat.openai.com/share/46ff149e-a4c7-4dd7-a800-fc4a642ea389\n[8] Shinn \u0026 Labash. “Reflexion: an autonomous agent with dynamic memory and self-reflection” arXiv preprint arXiv:2303.11366 (2023).\n[9] Laskin et al. “In-context Reinforcement Learning with Algorithm Distillation” ICLR 2023.\n[10] Karpas et al. “MRKL Systems A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning.\" arXiv preprint arXiv:2205.00445 (2022).\n[11] Weaviate Blog. Why is Vector Search so fast? Sep 13, 2022.\n[12] Li et al. “API-Bank: A Benchmark for Tool-Augmented LLMs” arXiv preprint arXiv:2304.08244 (2023).\n[13] Shen et al. “HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace” arXiv preprint arXiv:2303.17580 (2023).\n[14] Bran et al. “ChemCrow: Augmenting large-language models with chemistry tools.\" arXiv preprint arXiv:2304.05376 (2023).\n[15] Boiko et al. “Emergent autonomous scientific research capabilities of large language models.\" arXiv preprint arXiv:2304.05332 (2023).\n[16] Joon Sung Park, et al. “Generative Agents: Interactive Simulacra of Human Behavior.\" arXiv preprint arXiv:2304.03442 (2023).\n[17] AutoGPT. https://github.com/Significant-Gravitas/Auto-GPT\n[18] GPT-Engineer. https://github.com/AntonOsika/gpt-engineer\n",
  "wordCount" : "6445",
  "inLanguage": "en",
  "datePublished": "2023-06-23T00:00:00Z",
  "dateModified": "2023-06-23T00:00:00Z",
  "author":{
    "@type": "Person",
    "name": "Lilian Weng"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://lilianweng.github.io/posts/2023-06-23-agent/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Lil'Log",
    "logo": {
      "@type": "ImageObject",
      "url": "https://lilianweng.github.io/favicon_peach.ico"
    }
  }
}
</script>
</head>

<body class="" id="top">
<script>
    if (localStorage.getItem("pref-theme") === "dark") {
        document.body.classList.add('dark');
    } else if (localStorage.getItem("pref-theme") === "light") {
        document.body.classList.remove('dark')
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark');
    }

</script>

<script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$','$$'], ['\\[', '\\]']],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
    }
  };

  window.addEventListener('load', (event) => {
      document.querySelectorAll("mjx-container").forEach(function(x){
        x.parentElement.classList += 'has-jax'})
    });

</script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<header class="header">
    <nav class="nav">
        <div class="logo">
            <a href="https://lilianweng.github.io/" accesskey="h" title="Lil&#39;Log (Alt + H)">Lil&#39;Log</a>
            <span class="logo-switches">
                <button id="theme-toggle" accesskey="t" title="(Alt + T)">
                    <svg id="moon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                    <svg id="sun" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                </button>
            </span>
        </div>
        <ul id="menu">
            <li>
                <a href="https://lilianweng.github.io/" title="Posts">
                    <span>Posts</span>
                </a>
            </li>
            <li>
                <a href="https://lilianweng.github.io/archives" title="Archive">
                    <span>Archive</span>
                </a>
            </li>
            <li>
                <a href="https://lilianweng.github.io/search/" title="Search (Alt &#43; /)" accesskey=/>
                    <span>Search</span>
                </a>
            </li>
            <li>
                <a href="https://lilianweng.github.io/tags/" title="Tags">
                    <span>Tags</span>
                </a>
            </li>
            <li>
                <a href="https://lilianweng.github.io/faq" title="FAQ">
                    <span>FAQ</span>
                </a>
            </li>
            <li>
                <a href="https://www.emojisearch.app/" title="emojisearch.app">
                    <span>emojisearch.app</span>
                </a>
            </li>
        </ul>
    </nav>
</header>
<main class="main">

<article class="post-single">
  <header class="post-header">
    
    <h1 class="post-title">
      LLM Powered Autonomous Agents
    </h1>
    <div class="post-meta"><span title='2023-06-23 00:00:00 +0000 UTC'>June 23, 2023</span>&nbsp;·&nbsp;31 min&nbsp;·&nbsp;Lilian Weng

</div>
  </header> <div class="toc">
    <details >
        <summary accesskey="c" title="(Alt + C)">
            <span class="details">Table of Contents</span>
        </summary>

        <div class="inner"><ul>
                <li>
                    <a href="#agent-system-overview" aria-label="Agent System Overview">Agent System Overview</a></li>
                <li>
                    <a href="#component-one-planning" aria-label="Component One: Planning">Component One: Planning</a><ul>
                        
                <li>
                    <a href="#task-decomposition" aria-label="Task Decomposition">Task Decomposition</a></li>
                <li>
                    <a href="#self-reflection" aria-label="Self-Reflection">Self-Reflection</a></li></ul>
                </li>
                <li>
                    <a href="#component-two-memory" aria-label="Component Two: Memory">Component Two: Memory</a><ul>
                        
                <li>
                    <a href="#types-of-memory" aria-label="Types of Memory">Types of Memory</a></li>
                <li>
                    <a href="#maximum-inner-product-search-mips" aria-label="Maximum Inner Product Search (MIPS)">Maximum Inner Product Search (MIPS)</a></li></ul>
                </li>
                <li>
                    <a href="#component-three-tool-use" aria-label="Component Three: Tool Use">Component Three: Tool Use</a></li>
                <li>
                    <a href="#case-studies" aria-label="Case Studies">Case Studies</a><ul>
                        
                <li>
                    <a href="#scientific-discovery-agent" aria-label="Scientific Discovery Agent">Scientific Discovery Agent</a></li>
                <li>
                    <a href="#generative-agents-simulation" aria-label="Generative Agents Simulation">Generative Agents Simulation</a></li>
                <li>
                    <a href="#proof-of-concept-examples" aria-label="Proof-of-Concept Examples">Proof-of-Concept Examples</a></li></ul>
                </li>
                <li>
                    <a href="#challenges" aria-label="Challenges">Challenges</a></li>
                <li>
                    <a href="#citation" aria-label="Citation">Citation</a></li>
                <li>
                    <a href="#references" aria-label="References">References</a>
                </li>
            </ul>
        </div>
    </details>
</div>

  <div class="post-content"><p>Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as <a href="https://github.com/Significant-Gravitas/Auto-GPT">AutoGPT</a>, <a href="https://github.com/AntonOsika/gpt-engineer">GPT-Engineer</a> and <a href="https://github.com/yoheinakajima/babyagi">BabyAGI</a>, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.</p>
<h1 id="agent-system-overview">Agent System Overview<a hidden class="anchor" aria-hidden="true" href="#agent-system-overview">#</a></h1>
<p>In a LLM-powered autonomous agent system, LLM functions as the agent&rsquo;s brain, complemented by several key components:</p>
<ul>
<li><strong>Planning</strong>
<ul>
<li>Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.</li>
<li>Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results.</li>
</ul>
</li>
<li><strong>Memory</strong>
<ul>
<li>Short-term memory: I would consider all the in-context learning (See <a href="https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/">Prompt Engineering</a>) as utilizing short-term memory of the model to learn.</li>
<li>Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval.</li>
</ul>
</li>
<li><strong>Tool use</strong>
<ul>
<li>The agent learns to call external APIs for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources and more.</li>
</ul>
</li>
</ul>
<img src="agent-overview.png" style="width: 100%;" class="center" />
<figcaption>Fig. 1. Overview of a LLM-powered autonomous agent system.</figcaption>
<h1 id="component-one-planning">Component One: Planning<a hidden class="anchor" aria-hidden="true" href="#component-one-planning">#</a></h1>
<p>A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.</p>
<h2 id="task-decomposition">Task Decomposition<a hidden class="anchor" aria-hidden="true" href="#task-decomposition">#</a></h2>
<p><a href="https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/#chain-of-thought-cot"><strong>Chain of thought</strong></a> (CoT; <a href="https://arxiv.org/abs/2201.11903">Wei et al. 2022</a>) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to &ldquo;think step by step&rdquo; to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model&rsquo;s thinking process.</p>
<p><strong>Tree of Thoughts</strong> (<a href="https://arxiv.org/abs/2305.10601">Yao et al. 2023</a>) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.</p>
<p>Task decomposition can be done (1) by LLM with simple prompting like <code>&quot;Steps for XYZ.\n1.&quot;</code>, <code>&quot;What are the subgoals for achieving XYZ?&quot;</code>, (2) by using task-specific instructions; e.g. <code>&quot;Write a story outline.&quot;</code> for writing a novel, or (3) with human inputs.</p>
<p>Another quite distinct approach, <strong>LLM+P</strong> (<a href="https://arxiv.org/abs/2304.11477">Liu et al. 2023</a>), involves relying on an external classical planner to do long-horizon planning. This approach utilizes the Planning Domain Definition Language (PDDL) as an intermediate interface to describe the planning problem. In this process, LLM (1) translates the problem into &ldquo;Problem PDDL&rdquo;, then (2) requests a classical planner to generate a PDDL plan based on an existing &ldquo;Domain PDDL&rdquo;, and finally (3) translates the PDDL plan back into natural language. Essentially, the planning step is outsourced to an external tool, assuming the availability of domain-specific PDDL and a suitable planner which is common in certain robotic setups but not in many other domains.</p>
<h2 id="self-reflection">Self-Reflection<a hidden class="anchor" aria-hidden="true" href="#self-reflection">#</a></h2>
<p>Self-reflection is a vital aspect that allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. It plays a crucial role in real-world tasks where trial and error are inevitable.</p>
<p><a name="react"></a><strong>ReAct</strong> (<a href="https://arxiv.org/abs/2210.03629">Yao et al. 2023</a>) integrates reasoning and acting within LLM by extending the action space to be a combination of task-specific discrete actions and the language space. The former enables LLM to interact with the environment (e.g. use Wikipedia search API), while the latter prompting LLM to generate reasoning traces in natural language.</p>
<p>The ReAct prompt template incorporates explicit steps for LLM to think, roughly formatted as:</p>
<pre tabindex="0"><code>Thought: ...
Action: ...
Observation: ...
... (Repeated many times)
</code></pre><img src="react.png" style="width: 100%;" class="center" />
<figcaption>Fig. 2.  Examples of reasoning trajectories for knowledge-intensive tasks (e.g. HotpotQA, FEVER) and decision-making tasks (e.g. AlfWorld Env, WebShop). (Image source: <a href="https://arxiv.org/abs/2210.03629" target="_blank">Yao et al. 2023</a>).</figcaption>
<p>In both experiments on knowledge-intensive tasks and decision-making tasks, <code>ReAct</code> works better than the <code>Act</code>-only baseline where <code>Thought: …</code> step is removed.</p>
<p><strong>Reflexion</strong> (<a href="https://arxiv.org/abs/2303.11366">Shinn &amp; Labash 2023</a>) is a framework to equips agents with dynamic memory and self-reflection capabilities to improve reasoning skills. Reflexion has a standard RL setup, in which the reward model provides a simple binary reward and the action space follows the setup in ReAct where the task-specific action space is augmented with language to enable complex reasoning steps. After each action $a_t$, the agent computes a heuristic $h_t$ and optionally may <em>decide to reset</em> the environment to start a new trial depending on the self-reflection results.</p>
<img src="reflexion.png" style="width: 80%;" class="center" />
<figcaption>Fig. 3. Illustration of the Reflexion framework. (Image source: <a href="https://arxiv.org/abs/2303.11366" target="_blank">Shinn & Labash, 2023</a>)</figcaption>
<p>The heuristic function determines when the trajectory is inefficient or contains hallucination and should be stopped. Inefficient planning refers to trajectories that take too long without success. Hallucination is defined as encountering a sequence of consecutive identical actions that lead to the same observation in the environment.</p>
<p>Self-reflection is created by showing two-shot examples to LLM and each example is a pair of (failed trajectory, ideal reflection for guiding future changes in the plan). Then reflections are added into the agent&rsquo;s working memory, up to three, to be used as context for querying LLM.</p>
<img src="reflexion-exp.png" style="width: 100%;" class="center" />
<figcaption>Fig. 4. Experiments on AlfWorld Env and HotpotQA. Hallucination is a more common failure than inefficient planning in AlfWorld. (Image source: <a href="https://arxiv.org/abs/2303.11366" target="_blank">Shinn & Labash, 2023</a>)</figcaption>
<p><strong>Chain of Hindsight</strong> (CoH; <a href="https://arxiv.org/abs/2302.02676">Liu et al. 2023</a>) encourages the model to improve on its own outputs by explicitly presenting it with a sequence of past outputs, each annotated with feedback. Human feedback data is a collection of $D_h = \{(x, y_i , r_i , z_i)\}_{i=1}^n$, where $x$ is the prompt, each $y_i$ is a model completion, $r_i$ is the human rating of $y_i$, and $z_i$ is the corresponding human-provided hindsight feedback. Assume the feedback tuples are ranked by reward, $r_n \geq r_{n-1} \geq \dots \geq r_1$ The process is supervised fine-tuning where the data is a sequence in the form of $\tau_h = (x, z_i, y_i, z_j, y_j, \dots, z_n, y_n)$, where $\leq i \leq j \leq n$. The model is finetuned to only predict $y_n$ where conditioned on the sequence prefix, such that the model can self-reflect to produce better output based on the feedback sequence. The model can optionally receive multiple rounds of instructions with human annotators at test time.</p>
<p>To avoid overfitting, CoH adds a regularization term to maximize the log-likelihood of the pre-training dataset. To avoid shortcutting and copying (because there are many common words in feedback sequences), they randomly mask 0% - 5% of past tokens during training.</p>
<p>The training dataset in their experiments is a combination of <a href="https://huggingface.co/datasets/openai/webgpt_comparisons">WebGPT comparisons</a>, <a href="https://github.com/openai/summarize-from-feedback">summarization from human feedback</a> and <a href="https://github.com/anthropics/hh-rlhf">human preference dataset</a>.</p>
<img src="CoH.png" style="width: 100%;" class="center" />
<figcaption>Fig. 5. After fine-tuning with CoH, the model can follow instructions to produce outputs with incremental improvement in a sequence. (Image source: <a href="https://arxiv.org/abs/2302.02676" target="_blank">Liu et al. 2023</a>)</figcaption>
<p>The idea of CoH is to present a history of sequentially improved outputs  in context and train the model to take on the trend to produce better outputs. <strong>Algorithm Distillation</strong> (AD; <a href="https://arxiv.org/abs/2210.14215">Laskin et al. 2023</a>) applies the same idea to cross-episode trajectories in reinforcement learning tasks, where an <em>algorithm</em> is encapsulated in a long history-conditioned policy. Considering that an agent interacts with the environment many times and in each episode the agent gets a little better, AD concatenates this learning history and feeds that into the model. Hence we should expect the next predicted action to lead to better performance than previous trials. The goal is to learn the process of RL instead of training a task-specific policy itself.</p>
<img src="algorithm-distillation.png" style="width: 85%;" class="center" />
<figcaption>Fig. 6. Illustration of how Algorithm Distillation (AD) works. <br/>(Image source: <a href="https://arxiv.org/abs/2210.14215" target="_blank">Laskin et al. 2023</a>).</figcaption>
<p>The paper hypothesizes that any algorithm that generates a set of learning histories can be distilled into a neural network by performing behavioral cloning over actions. The history data is generated by a set of source policies, each trained for a specific task. At the training stage, during each RL run, a random task is sampled and a subsequence of multi-episode history is used for training, such that the learned policy is task-agnostic.</p>
<p>In reality, the model has limited context window length, so episodes should be short enough to construct multi-episode history. Multi-episodic contexts of 2-4 episodes are necessary to learn a near-optimal in-context RL algorithm. The emergence of in-context RL requires long enough context.</p>
<p>In comparison with three baselines, including ED (expert distillation, behavior cloning with expert trajectories instead of learning history), source policy (used for generating trajectories for distillation by <a href="https://lilianweng.github.io/posts/2018-01-23-multi-armed-bandit/#upper-confidence-bounds">UCB</a>), RL^2 (<a href="https://arxiv.org/abs/1611.02779">Duan et al. 2017</a>; used as upper bound since it needs online RL), AD demonstrates in-context RL with performance getting close to RL^2 despite only using offline RL and learns much faster than other baselines. When conditioned on partial training history of the source policy, AD also improves much faster than ED baseline.</p>
<img src="algorithm-distillation-results.png" style="width: 100%;" class="center" />
<figcaption>Fig. 7. Comparison of AD, ED, source policy and RL^2 on environments that require memory and exploration. Only binary reward is assigned. The source policies are trained with <a href="https://lilianweng.github.io/posts/2018-04-08-policy-gradient/#a3c" target="_blank">A3C</a> for "dark" environments and <a href="http://lilianweng.github.io/posts/2018-02-19-rl-overview/#deep-q-network" target="_blank">DQN</a> for watermaze.<br/>(Image source: <a href="https://arxiv.org/abs/2210.14215" target="_blank">Laskin et al. 2023</a>)</figcaption>
<h1 id="component-two-memory">Component Two: Memory<a hidden class="anchor" aria-hidden="true" href="#component-two-memory">#</a></h1>
<p>(Big thank you to ChatGPT for helping me draft this section. I&rsquo;ve learned a lot about the human brain and data structure for fast MIPS in my <a href="https://chat.openai.com/share/46ff149e-a4c7-4dd7-a800-fc4a642ea389">conversations</a> with ChatGPT.)</p>
<h2 id="types-of-memory">Types of Memory<a hidden class="anchor" aria-hidden="true" href="#types-of-memory">#</a></h2>
<p>Memory can be defined as the processes used to acquire, store, retain, and later retrieve information. There are several types of memory in human brains.</p>
<ol>
<li>
<p><strong>Sensory Memory</strong>: This is the earliest stage of memory, providing the ability to retain impressions of sensory information (visual, auditory, etc) after the original stimuli have ended. Sensory memory typically only lasts for up to a few seconds. Subcategories include iconic memory (visual), echoic memory (auditory), and haptic memory (touch).</p>
</li>
<li>
<p><strong>Short-Term Memory</strong> (STM) or <strong>Working Memory</strong>: It stores information that we are currently aware of and needed to carry out complex cognitive tasks such as learning and reasoning. Short-term memory is believed to have the capacity of about 7 items (<a href="psychclassics.yorku.ca/Miller/">Miller 1956</a>) and lasts for 20-30 seconds.</p>
</li>
<li>
<p><strong>Long-Term Memory</strong> (LTM): Long-term memory can store information for a remarkably long time, ranging from a few days to decades, with an essentially unlimited storage capacity. There are two subtypes of LTM:</p>
<ul>
<li>Explicit / declarative memory: This is memory of facts and events, and refers to those memories that can be consciously recalled, including episodic memory (events and experiences) and semantic memory (facts and concepts).</li>
<li>Implicit / procedural memory: This type of memory is unconscious and involves skills and routines that are performed automatically, like riding a bike or typing on a keyboard.</li>
</ul>
</li>
</ol>
<img src="memory.png" style="width: 100%;" class="center" />
<figcaption>Fig. 8. Categorization of human memory.</figcaption>
<p>We can roughly consider the following mappings:</p>
<ul>
<li>Sensory memory as learning embedding representations for raw inputs, including text, image or other modalities;</li>
<li>Short-term memory as in-context learning. It is short and finite, as it is restricted by the finite context window length of Transformer.</li>
<li>Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval.</li>
</ul>
<h2 id="maximum-inner-product-search-mips">Maximum Inner Product Search (MIPS)<a hidden class="anchor" aria-hidden="true" href="#maximum-inner-product-search-mips">#</a></h2>
<p>The external memory can alleviate the restriction of finite attention span.  A standard practice is to save the embedding representation of information into a vector store database that can support fast maximum inner-product search (<a href="https://en.wikipedia.org/wiki/Maximum_inner-product_search">MIPS</a>). To optimize the retrieval speed, the common choice is the <em>approximate nearest neighbors (ANN)​</em> algorithm to return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup.</p>
<p>A couple common choices of ANN algorithms for fast MIPS:</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Locality-sensitive_hashing"><strong>LSH</strong></a> (Locality-Sensitive Hashing): It introduces a <em>hashing</em> function such that similar input items are mapped to the same buckets with high probability, where the number of buckets is much smaller than the number of inputs.</li>
<li><a href="https://github.com/spotify/annoy"><strong>ANNOY</strong></a> (Approximate Nearest Neighbors Oh Yeah): The core data structure are <em>random projection trees</em>, a set of binary trees where each non-leaf node represents a hyperplane splitting the input space into half and each leaf stores one data point. Trees are built independently and at random, so to some extent, it mimics a hashing function. ANNOY search happens in all the trees to iteratively search through the half that is closest to the query and then aggregates the results. The idea is quite related to KD tree but a lot more scalable.</li>
<li><a href="https://arxiv.org/abs/1603.09320"><strong>HNSW</strong></a> (Hierarchical Navigable Small World): It is inspired by the idea of <a href="https://en.wikipedia.org/wiki/Small-world_network">small world networks</a> where most nodes can be reached by any other nodes within a small number of steps; e.g. &ldquo;six degrees of separation&rdquo; feature of social networks. HNSW builds hierarchical layers of these small-world graphs, where the bottom layers contain the actual data points. The layers in the middle create shortcuts to speed up search. When performing a search, HNSW starts from a random node in the top layer and navigates towards the target. When it can&rsquo;t get any closer, it moves down to the next layer, until it reaches the bottom layer. Each move in the upper layers can potentially cover a large distance in the data space, and each move in the lower layers refines the search quality.</li>
<li><a href="https://github.com/facebookresearch/faiss"><strong>FAISS</strong></a> (Facebook AI Similarity Search): It operates on the assumption that in high dimensional space, distances between nodes follow a Gaussian distribution and thus there should exist <em>clustering</em> of data points. FAISS applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters. Search first looks for cluster candidates with coarse quantization and then further looks into each cluster with finer quantization.</li>
<li><a href="https://github.com/google-research/google-research/tree/master/scann"><strong>ScaNN</strong></a> (Scalable Nearest Neighbors): The main innovation in ScaNN is <em>anisotropic vector quantization</em>. It quantizes a data point $x_i$ to $\tilde{x}_i$ such that the inner product $\langle q, x_i \rangle$ is as similar to the original distance of $\angle q, \tilde{x}_i$ as possible, instead of picking the closet quantization centroid points.</li>
</ul>
<img src="mips.png" style="width: 80%;" class="center" />
<figcaption>Fig. 9. Comparison of MIPS algorithms, measured in recall@10. (Image source: <a href="https://ai.googleblog.com/2020/07/announcing-scann-efficient-vector.html" target="_blank">Google Blog, 2020</a>)</figcaption>
<p>Check more MIPS algorithms and performance comparison in <a href="https://ann-benchmarks.com/">ann-benchmarks.com</a>.</p>
<h1 id="component-three-tool-use">Component Three: Tool Use<a hidden class="anchor" aria-hidden="true" href="#component-three-tool-use">#</a></h1>
<p>Tool use is a remarkable and distinguishing characteristic of human beings. We create, modify and utilize external objects to do things that go beyond our physical and cognitive limits. Equipping LLMs with external tools can significantly extend the model capabilities.</p>
<img src="sea-otter.png" style="width: 500px;" class="center" />
<figcaption>Fig. 10. A picture of a sea otter using rock to crack open a seashell, while floating in the water. While some other animals can use tools, the complexity is not comparable with humans. (Image source: <a href="https://www.popularmechanics.com/science/animals/g39714258/animals-using-tools/" target="_blank">Animals using tools</a>)</figcaption>
<p><a name="mrkl"></a><strong>MRKL</strong> (<a href="https://arxiv.org/abs/2205.00445">Karpas et al. 2022</a>), short for &ldquo;Modular Reasoning, Knowledge and Language&rdquo;, is a neuro-symbolic architecture for autonomous agents. A MRKL system is proposed to contain a collection of &ldquo;expert&rdquo; modules and the general-purpose LLM works as a router to route inquiries to the best suitable expert module. These modules can be neural (e.g. deep learning models) or symbolic (e.g. math calculator, currency converter, weather API).</p>
<p>They did an experiment on fine-tuning LLM to call a calculator, using arithmetic as a test case. Their experiments showed that it was harder to solve verbal math problems than explicitly stated math problems because LLMs (7B Jurassic1-large model) failed to extract the right arguments for the basic arithmetic reliably. The results highlight when the external symbolic tools can work reliably, <em>knowing when to and how to use the tools are crucial</em>, determined by the LLM capability.</p>
<p>Both <strong>TALM</strong> (Tool Augmented Language Models; <a href="https://arxiv.org/abs/2205.12255">Parisi et al. 2022</a>) and <strong>Toolformer</strong> (<a href="https://arxiv.org/abs/2302.04761">Schick et al. 2023</a>) fine-tune a LM to learn to use external tool APIs. The dataset is expanded based on whether a newly added API call annotation can improve the quality of model outputs. See more details in the <a href="https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/#external-apis">&ldquo;External APIs&rdquo; section</a> of Prompt Engineering.</p>
<p>ChatGPT <a href="https://openai.com/blog/chatgpt-plugins">Plugins</a> and OpenAI API  <a href="https://platform.openai.com/docs/guides/gpt/function-calling">function calling</a> are good examples of LLMs augmented with tool use capability working in practice. The collection of tool APIs can be provided by other developers (as in Plugins) or self-defined (as in function calls).</p>
<p><strong>HuggingGPT</strong> (<a href="https://arxiv.org/abs/2303.17580">Shen et al. 2023</a>) is a framework to use ChatGPT as the task planner to select models available in HuggingFace platform according to the model descriptions and summarize the response based on the execution results.</p>
<img src="hugging-gpt.png" style="width: 100%;" class="center" />
<figcaption>Fig. 11. Illustration of how HuggingGPT works. (Image source: <a href="https://arxiv.org/abs/2303.17580" target="_blank">Shen et al. 2023</a>)</figcaption>
<p>The system comprises of 4 stages:</p>
<p><strong>(1) Task planning</strong>: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.</p>
<p>Instruction:</p>
<div class="prompt">
The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag "<resource>-task_id" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can't be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.
</div>
<p><strong>(2) Model selection</strong>: LLM distributes the tasks to expert models, where the request is framed as a multiple-choice question. LLM is presented with a list of models to choose from. Due to the limited context length, task type based filtration is needed.</p>
<p>Instruction:</p>
<div class="prompt">
Given the user request and the call command, the AI assistant helps the user to select a suitable model from a list of models to process the user request. The AI assistant merely outputs the model id of the most appropriate model. The output must be in a strict JSON format: "id": "id", "reason": "your detail reason for the choice". We have a list of models for you to choose from {{ Candidate Models }}. Please select one model from the list.
</div>
<p><strong>(3) Task execution</strong>: Expert models execute on the specific tasks and log results.</p>
<p>Instruction:</p>
<div class="prompt">
With the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.
</div>
<p><strong>(4) Response generation</strong>: LLM receives the execution results and provides summarized results to users.</p>
<p>To put HuggingGPT into real world usage, a couple challenges need to solve: (1) Efficiency improvement is needed as both LLM inference rounds and interactions with other models slow down the process; (2) It relies on a long context window to communicate over complicated task content; (3) Stability improvement of LLM outputs and external model services.</p>
<p><strong>API-Bank</strong> (<a href="https://arxiv.org/abs/2304.08244">Li et al. 2023</a>) is a benchmark for evaluating the performance of tool-augmented LLMs. It contains 53 commonly used API tools, a complete tool-augmented LLM workflow, and 264 annotated dialogues that involve 568 API calls. The selection of APIs is quite diverse, including search engines, calculator, calendar queries, smart home control, schedule management, health data management, account authentication workflow and more. Because there are a large number of APIs, LLM first has access to API search engine to find the right API to call and then uses the corresponding documentation to make a call.</p>
<img src="api-bank-process.png" style="width: 60%;" class="center" />
<figcaption>Fig. 12. Pseudo code of how LLM makes an API call in API-Bank. (Image source: <a href="https://arxiv.org/abs/2304.08244" target="_blank">Li et al. 2023</a>)</figcaption>
<p>In the API-Bank workflow, LLMs need to make a couple of decisions and at each step we can evaluate how accurate that decision is. Decisions include:</p>
<ol>
<li>Whether an API call is needed.</li>
<li>Identify the right API to call: if not good enough, LLMs need to iteratively modify the API inputs (e.g. deciding search keywords for Search Engine API).</li>
<li>Response based on the API results: the model can choose to refine and call again if results are not satisfied.</li>
</ol>
<p>This benchmark evaluates the agent&rsquo;s tool use capabilities at three levels:</p>
<ul>
<li>Level-1 evaluates the ability to <em>call the API</em>. Given an API&rsquo;s description, the model needs to determine whether to call a given API, call it correctly, and respond properly to API returns.</li>
<li>Level-2 examines the ability to <em>retrieve the API</em>. The model needs to search for possible APIs that may solve the user&rsquo;s requirement and learn how to use them by reading documentation.</li>
<li>Level-3 assesses the ability to <em>plan API beyond retrieve and call</em>. Given unclear user requests (e.g. schedule group meetings, book flight/hotel/restaurant for a trip), the model may have to conduct multiple API calls to solve it.</li>
</ul>
<h1 id="case-studies">Case Studies<a hidden class="anchor" aria-hidden="true" href="#case-studies">#</a></h1>
<h2 id="scientific-discovery-agent">Scientific Discovery Agent<a hidden class="anchor" aria-hidden="true" href="#scientific-discovery-agent">#</a></h2>
<p><strong>ChemCrow</strong> (<a href="https://arxiv.org/abs/2304.05376">Bran et al. 2023</a>) is a domain-specific example in which LLM is augmented with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design. The workflow, implemented in <a href="https://github.com/hwchase17/langchain">LangChain</a>, reflects what was previously described in the <a href="#react">ReAct</a> and <a href="#mrkl">MRKLs</a> and combines CoT reasoning with tools relevant to the tasks:</p>
<ul>
<li>The LLM is provided with a list of tool names, descriptions of their utility, and details about the expected input/output.</li>
<li>It is then instructed to answer a user-given prompt using the tools provided when necessary. The instruction suggests the model to follow the ReAct format - <code>Thought, Action, Action Input, Observation</code>.</li>
</ul>
<p>One interesting observation is that while the LLM-based evaluation concluded that GPT-4 and ChemCrow perform nearly equivalently, human evaluations with experts oriented towards the completion and chemical correctness of the solutions showed that ChemCrow outperforms GPT-4 by a large margin. This indicates a potential problem with using LLM to evaluate its own performance on domains that requires deep expertise. The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.</p>
<p><a href="https://arxiv.org/abs/2304.05332">Boiko et al. (2023)</a> also looked into LLM-empowered agents for scientific discovery, to handle autonomous design, planning, and performance of complex scientific experiments. This agent can use tools to browse the Internet, read documentation, execute code, call robotics experimentation APIs and leverage other LLMs.</p>
<p>For example, when requested to <code>&quot;develop a novel anticancer drug&quot;</code>, the model came up with the following reasoning steps:</p>
<ol>
<li>inquired about current trends in anticancer drug discovery;</li>
<li>selected a target;</li>
<li>requested a scaffold targeting these compounds;</li>
<li>Once the compound was identified, the model attempted its synthesis.</li>
</ol>
<p>They also discussed the risks, especially with illicit drugs and bioweapons. They developed a test set containing a list of known chemical weapon agents and asked the agent to synthesize them. 4 out of 11 requests (36%) were accepted to obtain a synthesis solution and the agent attempted to consult documentation to execute the procedure. 7 out of 11 were rejected and among these 7 rejected cases, 5 happened after a Web search while 2 were rejected based on prompt only.</p>
<h2 id="generative-agents-simulation">Generative Agents Simulation<a hidden class="anchor" aria-hidden="true" href="#generative-agents-simulation">#</a></h2>
<p><strong>Generative Agents</strong> (<a href="https://arxiv.org/abs/2304.03442">Park, et al. 2023</a>) is super fun experiment where 25 virtual characters, each controlled by a LLM-powered agent, are living and interacting in a sandbox environment, inspired by The Sims. Generative agents create believable simulacra of human behavior for interactive applications.</p>
<p>The design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.</p>
<ul>
<li><strong>Memory</strong> stream: is a long-term memory module (external database) that records a comprehensive list of agents' experience in natural language.
<ul>
<li>Each element is an <em>observation</em>, an event directly provided by the agent.
- Inter-agent communication can trigger new natural language statements.</li>
</ul>
</li>
<li><strong>Retrieval</strong> model: surfaces the context to inform the agent&rsquo;s behavior, according to relevance, recency and importance.
<ul>
<li>Recency: recent events have higher scores</li>
<li>Importance: distinguish mundane from core memories. Ask LM directly.</li>
<li>Relevance: based on how related it is to the current situation / query.</li>
</ul>
</li>
<li><strong>Reflection</strong> mechanism: synthesizes memories into higher level inferences over time and guides the agent&rsquo;s future behavior. They are <em>higher-level summaries of past events</em> (&lt;- note that this is a bit different from <a href="#self-reflection">self-reflection</a> above)
<ul>
<li>Prompt LM with 100 most recent observations and to generate 3 most salient high-level questions given a set of observations/statements. Then ask LM to answer those questions.</li>
</ul>
</li>
<li><strong>Planning &amp; Reacting</strong>: translate the reflections and the environment information into actions
<ul>
<li>Planning is essentially in order to optimize believability at the moment vs in time.</li>
<li>Prompt template: <code>{Intro of an agent X}. Here is X's plan today in broad strokes: 1)</code></li>
<li>Relationships between agents and observations of one agent by another are all taken into consideration for planning and reacting.</li>
<li>Environment information is present in a tree structure.</li>
</ul>
</li>
</ul>
<img src="generative-agents.png" style="width: 100%;" class="center" />
<figcaption>Fig. 13. The generative agent architecture. (Image source: <a href="https://arxiv.org/abs/2304.03442" target="_blank">Park et al. 2023</a>)</figcaption>
<p>This fun simulation results in emergent social behavior, such as information diffusion, relationship memory (e.g. two agents continuing the conversation topic) and coordination of social events (e.g. host a party and invite many others).</p>
<h2 id="proof-of-concept-examples">Proof-of-Concept Examples<a hidden class="anchor" aria-hidden="true" href="#proof-of-concept-examples">#</a></h2>
<p><a href="https://github.com/Significant-Gravitas/Auto-GPT">AutoGPT</a> has drawn a lot of attention into the possibility of setting up autonomous agents with LLM as the main controller. It has quite a lot of reliability issues given the natural language interface, but nevertheless a cool proof-of-concept demo. A lot of code in AutoGPT is about format parsing.</p>
<p>Here is the system message used by AutoGPT, where <code>{{...}}</code> are user inputs:</p>
<pre tabindex="0"><code>You are {{ai-name}}, {{user-provided AI bot description}}.
Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications.

GOALS:

1. {{user-provided goal 1}}
2. {{user-provided goal 2}}
3. ...
4. ...
5. ...

Constraints:
1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.
2. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.
3. No user assistance
4. Exclusively use the commands listed in double quotes e.g. &quot;command name&quot;
5. Use subprocesses for commands that will not terminate within a few minutes

Commands:
1. Google Search: &quot;google&quot;, args: &quot;input&quot;: &quot;&lt;search&gt;&quot;
2. Browse Website: &quot;browse_website&quot;, args: &quot;url&quot;: &quot;&lt;url&gt;&quot;, &quot;question&quot;: &quot;&lt;what_you_want_to_find_on_website&gt;&quot;
3. Start GPT Agent: &quot;start_agent&quot;, args: &quot;name&quot;: &quot;&lt;name&gt;&quot;, &quot;task&quot;: &quot;&lt;short_task_desc&gt;&quot;, &quot;prompt&quot;: &quot;&lt;prompt&gt;&quot;
4. Message GPT Agent: &quot;message_agent&quot;, args: &quot;key&quot;: &quot;&lt;key&gt;&quot;, &quot;message&quot;: &quot;&lt;message&gt;&quot;
5. List GPT Agents: &quot;list_agents&quot;, args:
6. Delete GPT Agent: &quot;delete_agent&quot;, args: &quot;key&quot;: &quot;&lt;key&gt;&quot;
7. Clone Repository: &quot;clone_repository&quot;, args: &quot;repository_url&quot;: &quot;&lt;url&gt;&quot;, &quot;clone_path&quot;: &quot;&lt;directory&gt;&quot;
8. Write to file: &quot;write_to_file&quot;, args: &quot;file&quot;: &quot;&lt;file&gt;&quot;, &quot;text&quot;: &quot;&lt;text&gt;&quot;
9. Read file: &quot;read_file&quot;, args: &quot;file&quot;: &quot;&lt;file&gt;&quot;
10. Append to file: &quot;append_to_file&quot;, args: &quot;file&quot;: &quot;&lt;file&gt;&quot;, &quot;text&quot;: &quot;&lt;text&gt;&quot;
11. Delete file: &quot;delete_file&quot;, args: &quot;file&quot;: &quot;&lt;file&gt;&quot;
12. Search Files: &quot;search_files&quot;, args: &quot;directory&quot;: &quot;&lt;directory&gt;&quot;
13. Analyze Code: &quot;analyze_code&quot;, args: &quot;code&quot;: &quot;&lt;full_code_string&gt;&quot;
14. Get Improved Code: &quot;improve_code&quot;, args: &quot;suggestions&quot;: &quot;&lt;list_of_suggestions&gt;&quot;, &quot;code&quot;: &quot;&lt;full_code_string&gt;&quot;
15. Write Tests: &quot;write_tests&quot;, args: &quot;code&quot;: &quot;&lt;full_code_string&gt;&quot;, &quot;focus&quot;: &quot;&lt;list_of_focus_areas&gt;&quot;
16. Execute Python File: &quot;execute_python_file&quot;, args: &quot;file&quot;: &quot;&lt;file&gt;&quot;
17. Generate Image: &quot;generate_image&quot;, args: &quot;prompt&quot;: &quot;&lt;prompt&gt;&quot;
18. Send Tweet: &quot;send_tweet&quot;, args: &quot;text&quot;: &quot;&lt;text&gt;&quot;
19. Do Nothing: &quot;do_nothing&quot;, args:
20. Task Complete (Shutdown): &quot;task_complete&quot;, args: &quot;reason&quot;: &quot;&lt;reason&gt;&quot;

Resources:
1. Internet access for searches and information gathering.
2. Long Term memory management.
3. GPT-3.5 powered Agents for delegation of simple tasks.
4. File output.

Performance Evaluation:
1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
2. Constructively self-criticize your big-picture behavior constantly.
3. Reflect on past decisions and strategies to refine your approach.
4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.

You should only respond in JSON format as described below
Response Format:
{
    &quot;thoughts&quot;: {
        &quot;text&quot;: &quot;thought&quot;,
        &quot;reasoning&quot;: &quot;reasoning&quot;,
        &quot;plan&quot;: &quot;- short bulleted\n- list that conveys\n- long-term plan&quot;,
        &quot;criticism&quot;: &quot;constructive self-criticism&quot;,
        &quot;speak&quot;: &quot;thoughts summary to say to user&quot;
    },
    &quot;command&quot;: {
        &quot;name&quot;: &quot;command name&quot;,
        &quot;args&quot;: {
            &quot;arg name&quot;: &quot;value&quot;
        }
    }
}
Ensure the response can be parsed by Python json.loads
</code></pre><p><a href="https://github.com/AntonOsika/gpt-engineer">GPT-Engineer</a> is another project to create a whole repository of code given a task specified in natural language. The GPT-Engineer is instructed to think over a list of smaller components to build and ask for user input to clarify questions as needed.</p>
<p>Here are a sample conversation for task clarification sent to OpenAI ChatCompletion endpoint used by GPT-Engineer. The user inputs are wrapped in <code>{{user input text}}</code>.</p>
<pre tabindex="0"><code>[
  {
    &quot;role&quot;: &quot;system&quot;,
    &quot;content&quot;: &quot;You will read instructions and not carry them out, only seek to clarify them.\nSpecifically you will first summarise a list of super short bullets of areas that need clarification.\nThen you will pick one clarifying question, and wait for an answer from the user.\n&quot;
  },
  {
    &quot;role&quot;: &quot;user&quot;,
    &quot;content&quot;: &quot;We are writing {{a Super Mario game in python. MVC components split in separate files. Keyboard control.}}\n&quot;
  },
  {
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: &quot;Summary of areas that need clarification:\n1. Specifics of the Super Mario game (e.g. level design, characters, gameplay mechanics)\n2. Details about the MVC components (e.g. which components are in each file)\n3. Keyboard control implementation (e.g. which keys to use, how to handle input)\n\nClarifying question:\nCan you provide more details about the Super Mario game, such as level design, characters, and gameplay mechanics?&quot;
  },
  {
    &quot;role&quot;: &quot;user&quot;,
    &quot;content&quot;: &quot;{{There are 10 levels in total. The main character is a plumber named Mario, who can walk and jump. It is a classical platform game just like Super Mario. The main character moves from left to right, trying to get to the destination, where there are many obstacles and attacks from enemies in the process.}}\n\nIs anything else unclear? If yes, only answer in the form:\n{remaining unclear areas} remaining questions.\n{Next question}\nIf everything is sufficiently clear, only answer \&quot;Nothing more to clarify.\&quot;.&quot;
  },
  {
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: &quot;Remaining unclear areas: 2 remaining questions.\nCan you provide more information about how the MVC components are split into separate files?&quot;
  },
  {
    &quot;role&quot;: &quot;user&quot;,
    &quot;content&quot;: &quot;{{Make your own assumptions and state them explicitly before starting}}&quot;
  }
]
</code></pre><p>Then after these clarification, the agent moved into the code writing mode with a different system message.
System message:</p>
<div class="prompt">
You will get instructions for code to write.
You will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.
Make sure that every detail of the architecture is, in the end, implemented as code.
<p>Think step by step and reason yourself to the right decisions to make sure we get it right.
You will first lay out the names of the core classes, functions, methods that will be necessary, as well as a quick comment on their purpose.</p>
<p>Then you will output the content of each file including ALL code.
Each file must strictly follow a markdown code block format, where the following tokens must be replaced such that
FILENAME is the lowercase file name including the file extension,
LANG is the markup code block language for the code&rsquo;s language, and CODE is the code:</p>
<p>FILENAME</p>
<pre tabindex="0"><code class="language-LANG" data-lang="LANG">CODE
</code></pre><p>You will start with the &ldquo;entrypoint&rdquo; file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.</p>
<p>Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc. Make sure that code in different files are compatible with each other.
Ensure to implement all code, if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.
Before you finish, double check that all parts of the architecture is present in the files.</p>
<p>Useful to know:
You almost always put different classes in different files.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
You always add a comment briefly describing the purpose of the function definition.
You try to add comments explaining very complex bits of logic.
You always follow the best practices for the requested languages in terms of describing the code written as a defined
package/project.</p>
<p>Python toolbelt preferences:</p>
<ul>
<li>pytest</li>
<li>dataclasses</li>
</ul>
</div>
<p>Conversatin samples:</p>
<pre tabindex="0"><code>[
  {
    &quot;role&quot;: &quot;system&quot;,
    &quot;content&quot;: &quot;You will get instructions for code to write.\nYou will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.\nMake sure that every detail of the architecture is, in the end, implemented as code.\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nYou will first lay out the names of the core classes, functions, methods that will be necessary, as well as a quick comment on their purpose.\n\nThen you will output the content of each file including ALL code.\nEach file must strictly follow a markdown code block format, where the following tokens must be replaced such that\nFILENAME is the lowercase file name including the file extension,\nLANG is the markup code block language for the code's language, and CODE is the code:\n\nFILENAME\n```LANG\nCODE\n```\n\nYou will start with the \&quot;entrypoint\&quot; file, then go to the ones that are imported by that file, and so on.\nPlease note that the code should be fully functional. No placeholders.\n\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc. Make sure that code in different files are compatible with each other.\nEnsure to implement all code, if you are unsure, write a plausible implementation.\nInclude module dependency or package manager dependency definition file.\nBefore you finish, double check that all parts of the architecture is present in the files.\n\nUseful to know:\nYou almost always put different classes in different files.\nFor Python, you always create an appropriate requirements.txt file.\nFor NodeJS, you always create an appropriate package.json file.\nYou always add a comment briefly describing the purpose of the function definition.\nYou try to add comments explaining very complex bits of logic.\nYou always follow the best practices for the requested languages in terms of describing the code written as a defined\npackage/project.\n\n\nPython toolbelt preferences:\n- pytest\n- dataclasses\n&quot;
  },
 #  … same conversation as earlier, ended with &quot;Make your own assumptions and state them explicitly before starting&quot;.
  {
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: &quot;Assumptions:\n1. Model: The model will contain the game's data, such as level information, character states, and enemy positions.\n2. View: The view will handle the game's visuals, including rendering the game objects, backgrounds, and updating the display.\n3. Controller: The controller will manage user input, such as keyboard controls, and update the model accordingly.\n\nWith these assumptions in mind, is there any specific aspect of the keyboard control implementation you would like me to clarify?&quot;
  },
  {
    &quot;role&quot;: &quot;user&quot;,
    &quot;content&quot;: &quot;Please now remember the steps:\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\n\nThen you will output the content of each file including ALL code.\nEach file must strictly follow a markdown code block format, where the following tokens must be replaced such that\nFILENAME is the lowercase file name including the file extension,\nLANG is the markup code block language for the code's language, and CODE is the code:\n\nFILENAME\n```LANG\nCODE\n```\n\nPlease note that the code should be fully functional. No placeholders.\n\nYou will start with the \&quot;entrypoint\&quot; file, then go to the ones that are imported by that file, and so on.\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc. The code should be fully functional. Make sure that code in different files are compatible with each other.\nBefore you finish, double check that all parts of the architecture is present in the files.\n&quot;
  }
]
</code></pre><h1 id="challenges">Challenges<a hidden class="anchor" aria-hidden="true" href="#challenges">#</a></h1>
<p>After going through key ideas and demos of building LLM-centered agents, I start to see a couple common limitations:</p>
<ul>
<li>
<p><strong>Finite context length</strong>: The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses. The design of the system has to work with this limited communication bandwidth, while mechanisms like self-reflection to learn from past mistakes would benefit a lot from long or infinite context windows. Although vector stores and retrieval can provide access to a larger knowledge pool, their representation power is not as powerful as full attention.</p>
</li>
<li>
<p><strong>Challenges in long-term planning and task decomposition</strong>: Planning over a lengthy history and effectively exploring the solution space remain challenging. LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.</p>
</li>
<li>
<p><strong>Reliability of natural language interface</strong>: Current agent system relies on natural language as an interface between LLMs and external components such as memory and tools. However, the reliability of model outputs is questionable, as LLMs may make formatting errors and occasionally exhibit rebellious behavior (e.g. refuse to follow an instruction). Consequently, much of the agent demo code focuses on parsing model output.</p>
</li>
</ul>
<h1 id="citation">Citation<a hidden class="anchor" aria-hidden="true" href="#citation">#</a></h1>
<p>Cited as:</p>
<blockquote>
<p>Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents&quot;. Lil&rsquo;Log. https://lilianweng.github.io/posts/2023-06-23-agent/.</p>
</blockquote>
<p>Or</p>
<pre tabindex="0"><code>@article{weng2023prompt,
  title   = &quot;LLM-powered Autonomous Agents&quot;&quot;,
  author  = &quot;Weng, Lilian&quot;,
  journal = &quot;lilianweng.github.io&quot;,
  year    = &quot;2023&quot;,
  month   = &quot;Jun&quot;,
  url     = &quot;https://lilianweng.github.io/posts/2023-06-23-agent/&quot;
}
</code></pre><h1 id="references">References<a hidden class="anchor" aria-hidden="true" href="#references">#</a></h1>
<p>[1] Wei et al. <a href="https://arxiv.org/abs/2201.11903">&ldquo;Chain of thought prompting elicits reasoning in large language models.&quot;</a> NeurIPS 2022</p>
<p>[2] Yao et al. <a href="https://arxiv.org/abs/2305.10601">&ldquo;Tree of Thoughts: Dliberate Problem Solving with Large Language Models.&quot;</a> arXiv preprint arXiv:2305.10601 (2023).</p>
<p>[3] Liu et al. <a href="https://arxiv.org/abs/2302.02676">&ldquo;Chain of Hindsight Aligns Language Models with Feedback
&ldquo;</a> arXiv preprint arXiv:2302.02676 (2023).</p>
<p>[4] Liu et al. <a href="https://arxiv.org/abs/2304.11477">&ldquo;LLM+P: Empowering Large Language Models with Optimal Planning Proficiency&rdquo;</a> arXiv preprint arXiv:2304.11477 (2023).</p>
<p>[5] Yao et al. <a href="https://arxiv.org/abs/2210.03629">&ldquo;ReAct: Synergizing reasoning and acting in language models.&quot;</a> ICLR 2023.</p>
<p>[6] Google Blog. <a href="https://ai.googleblog.com/2020/07/announcing-scann-efficient-vector.html">&ldquo;Announcing ScaNN: Efficient Vector Similarity Search&rdquo;</a> July 28, 2020.</p>
<p>[7] <a href="https://chat.openai.com/share/46ff149e-a4c7-4dd7-a800-fc4a642ea389">https://chat.openai.com/share/46ff149e-a4c7-4dd7-a800-fc4a642ea389</a></p>
<p>[8] Shinn &amp; Labash. <a href="https://arxiv.org/abs/2303.11366">&ldquo;Reflexion: an autonomous agent with dynamic memory and self-reflection&rdquo;</a> arXiv preprint arXiv:2303.11366 (2023).</p>
<p>[9] Laskin et al. <a href="https://arxiv.org/abs/2210.14215">&ldquo;In-context Reinforcement Learning with Algorithm Distillation&rdquo;</a> ICLR 2023.</p>
<p>[10] Karpas et al. <a href="https://arxiv.org/abs/2205.00445">&ldquo;MRKL Systems A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning.&quot;</a> arXiv preprint arXiv:2205.00445 (2022).</p>
<p>[11] Weaviate Blog. <a href="https://weaviate.io/blog/why-is-vector-search-so-fast">Why is Vector Search so fast?</a> Sep 13, 2022.</p>
<p>[12] Li et al. <a href="https://arxiv.org/abs/2304.08244">&ldquo;API-Bank: A Benchmark for Tool-Augmented LLMs&rdquo;</a> arXiv preprint arXiv:2304.08244 (2023).</p>
<p>[13] Shen et al. <a href="https://arxiv.org/abs/2303.17580">&ldquo;HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace&rdquo;</a> arXiv preprint arXiv:2303.17580 (2023).</p>
<p>[14] Bran et al. <a href="https://arxiv.org/abs/2304.05376">&ldquo;ChemCrow: Augmenting large-language models with chemistry tools.&quot;</a> arXiv preprint arXiv:2304.05376 (2023).</p>
<p>[15] Boiko et al. <a href="https://arxiv.org/abs/2304.05332">&ldquo;Emergent autonomous scientific research capabilities of large language models.&quot;</a> arXiv preprint arXiv:2304.05332 (2023).</p>
<p>[16] Joon Sung Park, et al. <a href="https://arxiv.org/abs/2304.03442">&ldquo;Generative Agents: Interactive Simulacra of Human Behavior.&quot;</a> arXiv preprint arXiv:2304.03442 (2023).</p>
<p>[17] AutoGPT. <a href="https://github.com/Significant-Gravitas/Auto-GPT">https://github.com/Significant-Gravitas/Auto-GPT</a></p>
<p>[18] GPT-Engineer. <a href="https://github.com/AntonOsika/gpt-engineer">https://github.com/AntonOsika/gpt-engineer</a></p>


  </div>

  <footer class="post-footer">
    <ul class="post-tags">
      <li><a href="https://lilianweng.github.io/tags/nlp/">nlp</a></li>
      <li><a href="https://lilianweng.github.io/tags/language-model/">language-model</a></li>
      <li><a href="https://lilianweng.github.io/tags/agent/">agent</a></li>
      <li><a href="https://lilianweng.github.io/tags/steerability/">steerability</a></li>
      <li><a href="https://lilianweng.github.io/tags/prompting/">prompting</a></li>
    </ul>
<nav class="paginav">
  <a class="next" href="https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/">
    <span class="title"> »</span>
    <br>
    <span>Prompt Engineering</span>
  </a>
</nav>


<div class="share-buttons">
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on twitter"
        href="https://twitter.com/intent/tweet/?text=LLM%20Powered%20Autonomous%20Agents&amp;url=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f&amp;hashtags=nlp%2clanguage-model%2cagent%2csteerability%2cprompting">
        <svg version="1.1" viewBox="0 0 512 512" xml:space="preserve">
            <path
                d="M449.446,0c34.525,0 62.554,28.03 62.554,62.554l0,386.892c0,34.524 -28.03,62.554 -62.554,62.554l-386.892,0c-34.524,0 -62.554,-28.03 -62.554,-62.554l0,-386.892c0,-34.524 28.029,-62.554 62.554,-62.554l386.892,0Zm-253.927,424.544c135.939,0 210.268,-112.643 210.268,-210.268c0,-3.218 0,-6.437 -0.153,-9.502c14.406,-10.421 26.973,-23.448 36.935,-38.314c-13.18,5.824 -27.433,9.809 -42.452,11.648c15.326,-9.196 26.973,-23.602 32.49,-40.92c-14.252,8.429 -30.038,14.56 -46.896,17.931c-13.487,-14.406 -32.644,-23.295 -53.946,-23.295c-40.767,0 -73.87,33.104 -73.87,73.87c0,5.824 0.613,11.494 1.992,16.858c-61.456,-3.065 -115.862,-32.49 -152.337,-77.241c-6.284,10.881 -9.962,23.601 -9.962,37.088c0,25.594 13.027,48.276 32.95,61.456c-12.107,-0.307 -23.448,-3.678 -33.41,-9.196l0,0.92c0,35.862 25.441,65.594 59.311,72.49c-6.13,1.686 -12.72,2.606 -19.464,2.606c-4.751,0 -9.348,-0.46 -13.946,-1.38c9.349,29.426 36.628,50.728 68.965,51.341c-25.287,19.771 -57.164,31.571 -91.8,31.571c-5.977,0 -11.801,-0.306 -17.625,-1.073c32.337,21.15 71.264,33.41 112.95,33.41Z" />
        </svg>
    </a>
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on linkedin"
        href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f&amp;title=LLM%20Powered%20Autonomous%20Agents&amp;summary=LLM%20Powered%20Autonomous%20Agents&amp;source=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f">
        <svg version="1.1" viewBox="0 0 512 512" xml:space="preserve">
            <path
                d="M449.446,0c34.525,0 62.554,28.03 62.554,62.554l0,386.892c0,34.524 -28.03,62.554 -62.554,62.554l-386.892,0c-34.524,0 -62.554,-28.03 -62.554,-62.554l0,-386.892c0,-34.524 28.029,-62.554 62.554,-62.554l386.892,0Zm-288.985,423.278l0,-225.717l-75.04,0l0,225.717l75.04,0Zm270.539,0l0,-129.439c0,-69.333 -37.018,-101.586 -86.381,-101.586c-39.804,0 -57.634,21.891 -67.617,37.266l0,-31.958l-75.021,0c0.995,21.181 0,225.717 0,225.717l75.02,0l0,-126.056c0,-6.748 0.486,-13.492 2.474,-18.315c5.414,-13.475 17.767,-27.434 38.494,-27.434c27.135,0 38.007,20.707 38.007,51.037l0,120.768l75.024,0Zm-307.552,-334.556c-25.674,0 -42.448,16.879 -42.448,39.002c0,21.658 16.264,39.002 41.455,39.002l0.484,0c26.165,0 42.452,-17.344 42.452,-39.002c-0.485,-22.092 -16.241,-38.954 -41.943,-39.002Z" />
        </svg>
    </a>
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on reddit"
        href="https://reddit.com/submit?url=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f&title=LLM%20Powered%20Autonomous%20Agents">
        <svg version="1.1" viewBox="0 0 512 512" xml:space="preserve">
            <path
                d="M449.446,0c34.525,0 62.554,28.03 62.554,62.554l0,386.892c0,34.524 -28.03,62.554 -62.554,62.554l-386.892,0c-34.524,0 -62.554,-28.03 -62.554,-62.554l0,-386.892c0,-34.524 28.029,-62.554 62.554,-62.554l386.892,0Zm-3.446,265.638c0,-22.964 -18.616,-41.58 -41.58,-41.58c-11.211,0 -21.361,4.457 -28.841,11.666c-28.424,-20.508 -67.586,-33.757 -111.204,-35.278l18.941,-89.121l61.884,13.157c0.756,15.734 13.642,28.29 29.56,28.29c16.407,0 29.706,-13.299 29.706,-29.701c0,-16.403 -13.299,-29.702 -29.706,-29.702c-11.666,0 -21.657,6.792 -26.515,16.578l-69.105,-14.69c-1.922,-0.418 -3.939,-0.042 -5.585,1.036c-1.658,1.073 -2.811,2.761 -3.224,4.686l-21.152,99.438c-44.258,1.228 -84.046,14.494 -112.837,35.232c-7.468,-7.164 -17.589,-11.591 -28.757,-11.591c-22.965,0 -41.585,18.616 -41.585,41.58c0,16.896 10.095,31.41 24.568,37.918c-0.639,4.135 -0.99,8.328 -0.99,12.576c0,63.977 74.469,115.836 166.33,115.836c91.861,0 166.334,-51.859 166.334,-115.836c0,-4.218 -0.347,-8.387 -0.977,-12.493c14.564,-6.47 24.735,-21.034 24.735,-38.001Zm-119.474,108.193c-20.27,20.241 -59.115,21.816 -70.534,21.816c-11.428,0 -50.277,-1.575 -70.522,-21.82c-3.007,-3.008 -3.007,-7.882 0,-10.889c3.003,-2.999 7.882,-3.003 10.885,0c12.777,12.781 40.11,17.317 59.637,17.317c19.522,0 46.86,-4.536 59.657,-17.321c3.016,-2.999 7.886,-2.995 10.885,0.008c3.008,3.011 3.003,7.882 -0.008,10.889Zm-5.23,-48.781c-16.373,0 -29.701,-13.324 -29.701,-29.698c0,-16.381 13.328,-29.714 29.701,-29.714c16.378,0 29.706,13.333 29.706,29.714c0,16.374 -13.328,29.698 -29.706,29.698Zm-160.386,-29.702c0,-16.381 13.328,-29.71 29.714,-29.71c16.369,0 29.689,13.329 29.689,29.71c0,16.373 -13.32,29.693 -29.689,29.693c-16.386,0 -29.714,-13.32 -29.714,-29.693Z" />
        </svg>
    </a>
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on facebook"
        href="https://facebook.com/sharer/sharer.php?u=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f">
        <svg version="1.1" viewBox="0 0 512 512" xml:space="preserve">
            <path
                d="M449.446,0c34.525,0 62.554,28.03 62.554,62.554l0,386.892c0,34.524 -28.03,62.554 -62.554,62.554l-106.468,0l0,-192.915l66.6,0l12.672,-82.621l-79.272,0l0,-53.617c0,-22.603 11.073,-44.636 46.58,-44.636l36.042,0l0,-70.34c0,0 -32.71,-5.582 -63.982,-5.582c-65.288,0 -107.96,39.569 -107.96,111.204l0,62.971l-72.573,0l0,82.621l72.573,0l0,192.915l-191.104,0c-34.524,0 -62.554,-28.03 -62.554,-62.554l0,-386.892c0,-34.524 28.029,-62.554 62.554,-62.554l386.892,0Z" />
        </svg>
    </a>
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on whatsapp"
        href="https://api.whatsapp.com/send?text=LLM%20Powered%20Autonomous%20Agents%20-%20https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f">
        <svg version="1.1" viewBox="0 0 512 512" xml:space="preserve">
            <path
                d="M449.446,0c34.525,0 62.554,28.03 62.554,62.554l0,386.892c0,34.524 -28.03,62.554 -62.554,62.554l-386.892,0c-34.524,0 -62.554,-28.03 -62.554,-62.554l0,-386.892c0,-34.524 28.029,-62.554 62.554,-62.554l386.892,0Zm-58.673,127.703c-33.842,-33.881 -78.847,-52.548 -126.798,-52.568c-98.799,0 -179.21,80.405 -179.249,179.234c-0.013,31.593 8.241,62.428 23.927,89.612l-25.429,92.884l95.021,-24.925c26.181,14.28 55.659,21.807 85.658,21.816l0.074,0c98.789,0 179.206,-80.413 179.247,-179.243c0.018,-47.895 -18.61,-92.93 -52.451,-126.81Zm-126.797,275.782l-0.06,0c-26.734,-0.01 -52.954,-7.193 -75.828,-20.767l-5.441,-3.229l-56.386,14.792l15.05,-54.977l-3.542,-5.637c-14.913,-23.72 -22.791,-51.136 -22.779,-79.287c0.033,-82.142 66.867,-148.971 149.046,-148.971c39.793,0.014 77.199,15.531 105.329,43.692c28.128,28.16 43.609,65.592 43.594,105.4c-0.034,82.149 -66.866,148.983 -148.983,148.984Zm81.721,-111.581c-4.479,-2.242 -26.499,-13.075 -30.604,-14.571c-4.105,-1.495 -7.091,-2.241 -10.077,2.241c-2.986,4.483 -11.569,14.572 -14.182,17.562c-2.612,2.988 -5.225,3.364 -9.703,1.12c-4.479,-2.241 -18.91,-6.97 -36.017,-22.23c-13.314,-11.876 -22.304,-26.542 -24.916,-31.026c-2.612,-4.484 -0.279,-6.908 1.963,-9.14c2.016,-2.007 4.48,-5.232 6.719,-7.847c2.24,-2.615 2.986,-4.484 4.479,-7.472c1.493,-2.99 0.747,-5.604 -0.374,-7.846c-1.119,-2.241 -10.077,-24.288 -13.809,-33.256c-3.635,-8.733 -7.327,-7.55 -10.077,-7.688c-2.609,-0.13 -5.598,-0.158 -8.583,-0.158c-2.986,0 -7.839,1.121 -11.944,5.604c-4.105,4.484 -15.675,15.32 -15.675,37.364c0,22.046 16.048,43.342 18.287,46.332c2.24,2.99 31.582,48.227 76.511,67.627c10.685,4.615 19.028,7.371 25.533,9.434c10.728,3.41 20.492,2.929 28.209,1.775c8.605,-1.285 26.499,-10.833 30.231,-21.295c3.732,-10.464 3.732,-19.431 2.612,-21.298c-1.119,-1.869 -4.105,-2.99 -8.583,-5.232Z" />
        </svg>
    </a>
    <a target="_blank" rel="noopener noreferrer" aria-label="share LLM Powered Autonomous Agents on telegram"
        href="https://telegram.me/share/url?text=LLM%20Powered%20Autonomous%20Agents&amp;url=https%3a%2f%2flilianweng.github.io%2fposts%2f2023-06-23-agent%2f">
        <svg version="1.1" xml:space="preserve" viewBox="2 2 28 28">
            <path
                d="M26.49,29.86H5.5a3.37,3.37,0,0,1-2.47-1,3.35,3.35,0,0,1-1-2.47V5.48A3.36,3.36,0,0,1,3,3,3.37,3.37,0,0,1,5.5,2h21A3.38,3.38,0,0,1,29,3a3.36,3.36,0,0,1,1,2.46V26.37a3.35,3.35,0,0,1-1,2.47A3.38,3.38,0,0,1,26.49,29.86Zm-5.38-6.71a.79.79,0,0,0,.85-.66L24.73,9.24a.55.55,0,0,0-.18-.46.62.62,0,0,0-.41-.17q-.08,0-16.53,6.11a.59.59,0,0,0-.41.59.57.57,0,0,0,.43.52l4,1.24,1.61,4.83a.62.62,0,0,0,.63.43.56.56,0,0,0,.4-.17L16.54,20l4.09,3A.9.9,0,0,0,21.11,23.15ZM13.8,20.71l-1.21-4q8.72-5.55,8.78-5.55c.15,0,.23,0,.23.16a.18.18,0,0,1,0,.06s-2.51,2.3-7.52,6.8Z" />
        </svg>
    </a>
</div>

  </footer>
</article>
    </main>
    
<footer class="footer">
    <span>&copy; 2023 <a href="https://lilianweng.github.io/">Lil&#39;Log</a></span>
    <span>
        Powered by
        <a href="https://gohugo.io/" rel="noopener noreferrer" target="_blank">Hugo</a> &
        <a href="https://git.io/hugopapermod" rel="noopener" target="_blank">PaperMod</a>
    </span>
</footer>
<a href="#top" aria-label="go to top" title="Go to Top (Alt + G)" class="top-link" id="top-link" accesskey="g">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 6" fill="currentColor">
        <path d="M12 6H0l6-6z" />
    </svg>
</a>

<script>
    let menu = document.getElementById('menu')
    if (menu) {
        menu.scrollLeft = localStorage.getItem("menu-scroll-position");
        menu.onscroll = function () {
            localStorage.setItem("menu-scroll-position", menu.scrollLeft);
        }
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            var id = this.getAttribute("href").substr(1);
            if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                document.querySelector(`[id='${decodeURIComponent(id)}']`).scrollIntoView({
                    behavior: "smooth"
                });
            } else {
                document.querySelector(`[id='${decodeURIComponent(id)}']`).scrollIntoView();
            }
            if (id === "top") {
                history.replaceState(null, null, " ");
            } else {
                history.pushState(null, null, `#${id}`);
            }
        });
    });

</script>
<script>
    var mybutton = document.getElementById("top-link");
    window.onscroll = function () {
        if (document.body.scrollTop > 800 || document.documentElement.scrollTop > 800) {
            mybutton.style.visibility = "visible";
            mybutton.style.opacity = "1";
        } else {
            mybutton.style.visibility = "hidden";
            mybutton.style.opacity = "0";
        }
    };

</script>
<script>
    document.getElementById("theme-toggle").addEventListener("click", () => {
        if (document.body.className.includes("dark")) {
            document.body.classList.remove('dark');
            localStorage.setItem("pref-theme", 'light');
        } else {
            document.body.classList.add('dark');
            localStorage.setItem("pref-theme", 'dark');
        }
    })

</script>
<script>
    document.querySelectorAll('pre > code').forEach((codeblock) => {
        const container = codeblock.parentNode.parentNode;

        const copybutton = document.createElement('button');
        copybutton.classList.add('copy-code');
        copybutton.innerText = 'copy';

        function copyingDone() {
            copybutton.innerText = 'copied!';
            setTimeout(() => {
                copybutton.innerText = 'copy';
            }, 2000);
        }

        copybutton.addEventListener('click', (cb) => {
            if ('clipboard' in navigator) {
                navigator.clipboard.writeText(codeblock.textContent);
                copyingDone();
                return;
            }

            const range = document.createRange();
            range.selectNodeContents(codeblock);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            try {
                document.execCommand('copy');
                copyingDone();
            } catch (e) { };
            selection.removeRange(range);
        });

        if (container.classList.contains("highlight")) {
            container.appendChild(copybutton);
        } else if (container.parentNode.firstChild == container) {
            
        } else if (codeblock.parentNode.parentNode.parentNode.parentNode.parentNode.nodeName == "TABLE") {
            
            codeblock.parentNode.parentNode.parentNode.parentNode.parentNode.appendChild(copybutton);
        } else {
            
            codeblock.parentNode.appendChild(copybutton);
        }
    });
</script>
</body>

</html>
"""