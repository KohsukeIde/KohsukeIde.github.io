---
title: "Intelligence Learns How to Find Out"
subtitle: "Perception, action, and the making of evidence."
author: "Kohsuke Ide"
lang: en
---

# Intelligence Learns How to Find Out

*Perception, action, and the making of evidence.*

> The world hands out outcomes, not lessons.  
> Turning one into the other is the work I want the learner to own.

In [*Where Do Good Vision Targets Come From?*](https://kohsukeide.github.io/blog/posts/where-good-vision-targets-come-from/), I argued that the bottleneck can lie in the observations from which we build learning targets, not just in the loss used to learn from them. In [*Plato Is Not a Space*](https://kohsukeide.github.io/blog/posts/plato-is-not-a-space/), I argued that visual knowledge should be understood through the predictions about change it supports, not only through the similarity of internal spaces.

The two positions meet at a practical requirement. Testing a prediction requires observations that can support or challenge it. When the evidence at hand leaves competing predictions unresolved, another view or a revealing action can make their consequences distinguishable. **Can a visual learner arrange those observations for itself?**

This brings us back to an unresolved difficulty in the first blog. An agent might collect its own experience, but a kitchen does not come with a scoring function.[^targets] In a predefined task, we specify what to measure and how a result counts as success or error. Those choices are not automatically supplied for each new question about a kitchen.

It is tempting to make the problem disappear by saying that the world grades our predictions. Predict that a cup will tip, push it, and see what happens. But the world supplies an outcome, not an explanation of what the outcome establishes. The cup might leave the camera’s view. The push might differ from the one intended. A single outcome consistent with the prediction might still leave several explanations intact.

Turning what happens into something we can learn from is already work.

My position is that more of that work should belong to the learner. A general visual intelligence should not only improve its answers from the evidence it receives. It should learn how to obtain and interpret evidence for questions that matter and expand the range of questions it can investigate.

## 1. An outcome is not yet a learning signal

Suppose a robot wants to know whether two parts are rigidly attached. It pushes them, and both move. That observation does not settle the question. Contact and friction might have carried them together.

The robot could try to hold one part still while moving the other. It might first need a better view of the joint, a more reliable grip, or a way to distinguish the object’s motion from the camera’s. The relevant achievement is not merely executing an action. It is selecting an action and a viewpoint that make competing predictions distinguishable in the observations.

I use *evidence* here to mean an observation interpreted in relation to a question and to how it was obtained. It may change the support for a prediction without settling it. Obtaining useful evidence therefore requires linking a question to an action or observation and a measurement that bears on that question. None of these is guaranteed merely by putting a camera on a robot.

Even then, a gentle pull that produces no visible relative motion need not establish rigid attachment. Friction or motion below the camera’s resolution could produce the same observation. The result is evidence under particular conditions, not a complete explanation of the mechanism. Learning includes recognizing what remains unresolved.

![Three stages: an outcome, evidence for a question, and knowledge worth learning. Question and measurement connect the first two; purposes and future use connect the last two.](assets/figure-1-en-desktop.svg)

*Figure 1. From an outcome to something worth learning. A measurement bears on a question under stated conditions; it need not settle the question. Whether learning from it is worthwhile also depends on purposes and future use. The arrows identify work for the learner, not automatic implications.*

This is also work that a dataset’s creators may already have done by choosing a view, recording an action, or retaining the frames that reveal a change. A recorded interaction can support learning without being repeated. A dataset of recorded observations is not outside the world; it preserves selected observations of it.

**What agency adds is the ability to influence which observations the learner acquires next.**

## 2. A new skill can be a new way of knowing

Once a learner can obtain evidence for one question, what does it retain that could help it investigate another? I care about visual knowledge through the predictions it supports about what will remain stable, what will change, and what would follow under different conditions.[^interfaces]

Such knowledge need not be verbal, or stored as a collection of explicit propositions. A broadly useful visual representation may support a new question through a task-specific readout learned after pretraining. The concern here is what happens when the available observation, or the learner’s way of using it, is insufficient.

Return to the robot and the two parts. Learning to hold one part steady might look like a manipulation skill. It can also make previously ambiguous motion informative. Learning to rotate an object can reveal surfaces that the original camera never saw. Learning to use a mirror can make a new line of sight available.

In each case, an ability changes not only what the agent can accomplish, but what the world can teach it.

A new view may resolve the current uncertainty without improving the system’s ability to learn in a new situation. For the process to become developmental, the system must retain something reusable, such as a relation it discovered, a better way of measuring, or a way to arrange a revealing situation. A motor skill opens access; learning from the resulting evidence is a further achievement.

That is the developmental loop I want to build. Knowledge enables action, action can make informative observations accessible, and interpreting them can support further knowledge. Crucially, what is retained should help the system obtain or interpret evidence in another situation, rather than just repeat the original task.

![A cycle links what the system knows, what it can do, what evidence it can reach, and what it can learn next. Its focus is learning new ways to acquire evidence, not repeating a fixed loop.](assets/figure-2-en-desktop.svg)

*Figure 2. A skill can open a new route to evidence. A skill can make an informative observation accessible. The loop develops only when interpreting that observation leaves knowledge or a way of investigating that can be reused. This is a developmental possibility, not a guarantee of unlimited growth.*

The goal is not to challenge every prediction indiscriminately. It is to learn how to identify predictions that fail or remain underdetermined, including those the model initially made with confidence.

<details>
<summary>Side note · One representation, many questions</summary>

A broadly reusable encoder and a system that actively seeks evidence are complementary. A representation may already contain what a new question requires; the next step can be a different readout, not another experiment.

Steerable Visual Representations provides a concrete example of conditioning a visual encoder on supplied text to emphasize different concepts in the same image.[^steer] Such conditioning changes how available information is used. A prompt can also supply prior knowledge or a task description, but steering alone is not a new measurement of the pictured scene. Changing the question, acquiring evidence, and updating knowledge are different operations.

</details>

**Learning changes what can be learned.**

## 3. Not everything checkable is worth learning

Giving the learner a role in choosing its questions also allows it to choose badly. It could become excellent at generating easy questions, predicting irrelevant regularities, and repeatedly confirming what it already knows. High accuracy on self-generated tasks would not establish that the system had learned anything useful beyond those tasks.

The issue is not peculiar to vision. In discussions of AI-assisted mathematics, formal verification is distinguished from checking whether the formal statement captures the intended claim; a correct result is also distinguished from an intellectually valuable one.[^tao] Applied here, these are two separate requirements. Evidence must bear on the question actually being asked. Answering that question must also be worth the learner’s effort.

To say why a distinction is worth learning, we first need to say what the distinction amounts to. Calling the parts “rigidly attached” should make a difference to predictions about how their relative position changes under an applied force. Merely assigning a different label would not supply that content.

This is where pragmatism enters the argument. In *How to Make Our Ideas Clear*, Charles S. Peirce proposes clarifying a concept through the practical consequences it could conceivably have.[^peirce] I take this as a way to connect a representation to predictions that can be tested. What would be different, under what conditions, if the distinction were correct?

That is a claim about meaning, not yet about which questions deserve attention. A distinction can have clear consequences and still be irrelevant to the learner’s purposes. Whether it matters also depends on the system’s goals, available sensory and action capabilities, and resources, a relationship emphasized by the Umwelt Representation Hypothesis.[^urh] None of this makes convenience a test of truth. A prediction that seems useful can still be wrong.

Consider the two-part assembly again. Suppose a visible indicator stays on independently of the connection. The same recorded interaction lets the learner check a prediction about the light and a prediction about the parts’ relative motion. Only the latter helps distinguish the connection in this example. Checkability alone does not determine which target is worth learning.

![Two prediction targets use the same recorded interaction. Under the goal of learning how parts are connected, predicting a constant independent indicator is verifiable but uninformative about the connection. Predicting relative motion is also verifiable and may inform the connection. Transfer to another assembly remains an open question.](assets/figure-3-en-desktop.svg)

*Figure 3. Verifiable predictions can differ in learning value. Illustrative comparison, not measured model performance. The indicator is assumed independent of the connection. Both targets can be checked from the same interaction; their relevance differs under the stated goal. Colour could matter for another task. Reuse on unfamiliar assemblies is a possibility to test, not a result established by this example.*

My additional step is to include future learning among the consequences that make knowledge valuable. Knowing how to hold a part can make a joint observable; understanding that joint may help the learner inspect an unfamiliar mechanism. The immediate answer is only part of the return. If a way of investigating transfers, its value can extend beyond the task that first made it useful.

This gives the developmental loop a purpose without reducing it to today’s reward. The aim is not to collect every possible distinction, but to acquire knowledge that improves decisions or opens worthwhile paths of inquiry, under the learner’s purposes and constraints.

**Some of the value of knowledge lies in what it makes possible to learn next.**

## 4. World models for exploration and training

The learner now needs to choose an action or viewpoint likely to provide useful evidence. It can learn how to make that choice directly from experience, or use predictions to compare candidate actions. The second route gives a *world model* a concrete role. Here, a world model is a learned predictive model of how the environment and its observations may change, including under candidate actions.

Considering possible consequences before acting can support action selection.[^hoki] Here, the choice includes actions whose immediate purpose is to learn. The model need not already know the answer; it needs to help identify an observation for which different possible answers predict different outcomes.

For the two parts, it might predict one motion pattern if the joint is rigid and another if contact alone carries them together. That comparison could suggest holding one part while watching their relative motion. The result still has to be interpreted under the measurement limits discussed earlier. If the real mechanism was absent from the imagined alternatives, observation must be allowed to revise the alternatives too.

The same model can also generate simulated experience for training. Rather than only selecting the next action in the real environment, a controllable world model can generate variations of a situation in which the agent learns or evaluates its behavior. This is the promise of using world models as resources for training and evaluation.[^christian] Knowledge then becomes part of the infrastructure for acquiring more knowledge.

But learning from simulated experience and obtaining new evidence from the current environment serve different roles. Simulation can expose implications of the model’s assumptions and support learning behavior under those assumptions. Generating more samples from the same model does not establish that it accurately describes the scene outside it. Improvements within the simulation still need to transfer to the real environment.

![A world model generates candidate outcomes and simulated experience. Proposed actions lead to interaction with the real environment. Observations return from that interaction and can update predictions. A boundary separates model-generated outcomes from independently acquired observations.](assets/figure-4-en-desktop.svg)

*Figure 4. Model predictions guide interaction; observations can update the model. A world model can compare candidate actions and generate simulated experience for training. A new observation can test a prediction only if it measures a relevant difference. Model-generated experience is not an independent measurement of the real environment.*

<details>
<summary>Side note · Thinking longer, seeing something new</summary>

If a maze is fully visible, more computation may reveal a route already determined by the evidence. If a door’s state is hidden and no available clue settles it, drawing a detailed future does not reveal its actual state. A prior may favor one possibility without providing a new observation of that door.

Generated alternatives can still identify a useful next observation. Their vividness is not the criterion; their contribution to finding out is. This distinction does not depend on a particular generation architecture.

</details>

This separates two timescales rather than two fixed modules. Within a single interaction, the learner uses perception to select an action. Over repeated interactions, learning new actions and interpreting their outcomes can expand the observations it can acquire and interpret.

**Within a decision, perception may precede action. Across learning, action can change what perception becomes capable of.**

## 5. Generality beyond pretraining

For generality, I want both the ability to apply pretrained knowledge to new tasks and the ability to adapt through new experience when that knowledge is insufficient. Generalization from existing knowledge and adaptation through new observations are distinct capabilities. A useful pretrained representation supports the first and provides a starting point for the second.

Still, suppose two situations produce the same available observations but require different answers. Those observations alone cannot identify which situation the learner faces. Prior knowledge can make one answer more plausible, and more computation can extract overlooked implications; neither is a new observation of the unresolved difference. This is a limit of the evidence for that question, not a universal ceiling on passive learning.

When informative observations are accessible, the next challenge is acquiring and interpreting them without requiring us to redesign the data collection and learning targets for every new task. That extends the goal beyond answering unfamiliar questions from pretrained knowledge. The learner must also adapt how it acquires knowledge when that knowledge is insufficient.

Our contribution to *Visual General Intelligence: A White Paper* describes visual general intelligence (VGI) in terms of acquiring usable world structure from partial visual experience and applying it to new tasks.[^vgi] This blog extends that acquisition process beyond experiences already prepared for the learner, to conditions it can learn to arrange for itself.

<details>
<summary>Side note · Limits and lineage</summary>

This is a research stance, not a guarantee that every question becomes answerable. Sensors, resources, safety constraints, and the world impose limits. An autonomous learner should discover useful intermediate questions while remaining accountable to the purposes and constraints it was given, rather than replacing them with whatever is easiest to measure.

Curiosity-driven developmental learning already studies how acquired skills become stepping stones for further learning.[^development] The perception–action perspective likewise places autonomous experience collection inside the learning problem.[^vincent] The commitment here is to make obtaining and interpreting useful evidence a transferable capability.

The argument requires neither a single internal representation nor a rendered video before every action. A learned way of acquiring evidence need not be represented as an explicit procedure. What matters is whether it helps the system learn from another situation.

</details>

My bet is that **the ability to find out should itself transfer.**

Transfer would mean more than executing the same successful motion on a new object. A learner should be able to adapt a way of revealing, isolating, comparing, or testing so that an unfamiliar situation becomes informative. The new task need not have been anticipated when that way of investigating was learned.

I expect this reusable ability to become a major source of generality in sustained physical interaction. For systems already equipped with broad pretrained visual knowledge, the stronger expectation is that improving how they acquire missing evidence will matter more for unfamiliar physical situations than simply accumulating more comparable passive observations. That priority is a further claim to test; it does not follow merely from the fact that active observation can help.

If each new family of questions still requires us to invent a fresh dataset, specify a fresh target, and build a fresh way to interpret success, then we have retained a substantial part of the learning process outside the agent.

Conversely, if newly learned ways of obtaining evidence remain useful only for their original tasks, the developmental loop I am betting on is much weaker than I hope.

The goal is not a machine that has already seen everything. It is a machine that can use what it knows to find out what it does not, then turn what it finds out into further capacity to learn.

**The bet**

> **Generality in vision will come less from what a system has seen than from what it has learned how to find out.**

## References

[^targets]: Kohsuke Ide. [Where Do Good Vision Targets Come From?](https://kohsukeide.github.io/blog/posts/where-good-vision-targets-come-from/). The starting question: where learning targets come from, and the difficulty of interpreting feedback outside a prepared task.

[^interfaces]: Kohsuke Ide. [Plato Is Not a Space](https://kohsukeide.github.io/blog/posts/plato-is-not-a-space/). Visual knowledge considered through the predictions and responses a representation supports, rather than a prescribed internal geometry.

[^steer]: Jona Ruthardt, Manu Gaur, Deva Ramanan, Makarand Tapaswi & Yuki M. Asano · 2026. [Steerable Visual Representations](https://arxiv.org/abs/2604.02327). A concrete example of conditioning visual computation on a supplied question or concept; distinct from obtaining new sensory evidence.

[^tao]: Tanya Klowden & Terence Tao · 2026. [Mathematical methods and human thought in the age of AI](https://arxiv.org/abs/2603.26524). §4.4 separates formal correctness from fidelity to an intended mathematical statement; §§4.6–4.7 separate correctness from broader understanding and value. The application to visual learning here is an analogy, not a claim proved in that paper.

[^peirce]: Charles S. Peirce · 1878. [How to Make Our Ideas Clear](https://www.peirce.org/writings/p119.html). A method for clarifying conceptual meaning through conceivable practical consequences. The further claim that knowledge can be valuable for enabling future learning is the position developed in this blog, not a consequence established by the maxim.

[^urh]: Victoria Bosch, Rowan Sommers, Adrien Doerig & Tim C. Kietzmann · 2026. [The Umwelt Representation Hypothesis: Rethinking Universality](https://arxiv.org/abs/2604.17960). Box 1 and §2 connect useful distinctions and representational alignment to goals, sensing and action capabilities, and resource constraints.

[^hoki]: Hokin Deng. [Coding Is All You Need? Why We Need a World Model!](https://hokindeng.com/coding-is-all-you-need-why-we-need-a-world-model/). Considering consequences before acting; the companion blog discusses deliberation during video generation. See also [Schrödinger’s Cat in Video Models](https://hokindeng.com/schrodingers-cat-in-video-models/).

[^christian]: Christian Rupprecht · 2026. [World Models at Third Dimension AI](https://thirddimension.ai/blog/posts/world-models-at-third-dimension-ai). World models as controllable resources for training and evaluation, including the difficulty of generalizing beyond their own training data. The blog uses that role, not a guarantee that simulated experience transfers to reality.

[^vgi]: Hirokatsu Kataoka et al. · 2026. [Visual General Intelligence: A White Paper](https://arxiv.org/html/2608.25924#S2.SS10). §2.10: usable knowledge acquired from partial visual experience and applied to prediction, imagination, reconstruction, and new tasks.

[^development]: Sébastien Forestier, Rémy Portelas, Yoan Mollard & Pierre-Yves Oudeyer · 2017 / JMLR 2022. [Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning](https://arxiv.org/abs/1708.02190). Autonomous goal exploration and skills that become stepping stones for further learning.

[^vincent]: Vincent Sitzmann · 2026. [The flavor of the bitter lesson for computer vision](https://www.vincentsitzmann.com/blog/bitter_lesson_of_cv/). The perception–action loop and the problem of acquiring experience autonomously.

