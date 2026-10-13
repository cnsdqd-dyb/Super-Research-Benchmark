# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** afff7992 | **Time:** 192.85s | **Cost:** $0.03511
--------------------------------------------------------------------------------

# How is the Balance Between Physical Realism and Artistic Expressiveness Achieved in Digital Animation Rhythm Design?

## Abstract

The pursuit of achieving a harmonious balance between physical realism and artistic expressiveness represents one of the most fundamental challenges in digital animation rhythm design. This research report examines the theoretical foundations, methodological approaches, and practical techniques that enable animators and researchers to navigate this complex creative and technical landscape. Through an analysis of contemporary research in computer graphics, kinematic modeling, procedural animation, and style transfer, this report identifies key frameworks for understanding how rhythm design serves as the critical interface between physical plausibility and artistic intent. The findings reveal that successful balance is achieved through sophisticated timing curves derived from Newtonian physics, constraint-based motion adaptation, parameterizable animation systems, and the strategic application of animation principles that have evolved over decades of artistic practice. This report synthesizes insights from academic research and industry practice to provide a comprehensive understanding of the mechanisms by which digital animation achieves its dual mandate of believability and expressiveness.

## 1. Introduction

Digital animation occupies a unique position at the intersection of technical computation and artistic expression, requiring practitioners to reconcile the deterministic nature of computer systems with the inherently subjective and emotionally resonant qualities of human movement. The challenge of achieving balance between physical realism and artistic expressiveness in animation rhythm design is not merely a technical problem to be solved through algorithmic optimization; rather, it represents an ongoing dialogue between the laws of physics as we understand them and the perceptual and emotional needs of audiences who consume animated content.

The fundamental tension arises from the observation that purely physically realistic motion often lacks the emotional impact and narrative clarity that audiences expect from animated storytelling. Conversely, motion that prioritizes expressiveness over physical plausibility risks appearing arbitrary, confusing, or disconnected from the viewer's intuitive understanding of how objects and characters should move through space and time. This report investigates how digital animation has developed sophisticated mechanisms for navigating this tension, with particular emphasis on rhythm design as the primary vehicle for achieving balance.

Rhythm in animation encompasses the temporal organization of movement, including the timing of actions, the spacing between poses, and the acceleration and deceleration patterns that give movement its characteristic feel. As noted by professional studios engaged in character animation, "combining these two principles correctly transforms movement into a story" [4]. The right animation workflow does not focus exclusively on poses or keyframes but pays careful attention to ease-in and ease-out, to arcs, to how distance and rhythm interact to create realistic movement that resonates emotionally with viewers.

The research context for this report draws upon multiple streams of academic investigation and industry practice. Computer graphics research has produced increasingly sophisticated models for generating and modifying motion that balance physical correctness with artistic control. Animation theory has articulated principles that guide practitioners in creating movement that is both believable and expressive. Industry practice has refined tools and workflows that enable artists to achieve these goals efficiently while maintaining creative control over the final output.

## 2. Theoretical Foundations

### 2.1 The Physical Basis of Motion

Understanding physical realism in animation requires grounding in the fundamental principles of mechanics as they apply to moving objects and characters. The Newtonian framework provides the foundation for physically-based animation, describing how forces produce acceleration, how objects respond to impacts and constraints, and how energy is conserved or dissipated during motion. Research in computer graphics has extensively explored how these physical principles can be translated into computational models that generate realistic motion [2].

A particularly significant contribution to this field involves the development of timing curves that capture essential physical phenomena such as inertia, anticipation, and overshoot. These motion characteristics, which experienced animators intuitively incorporate into their work, can be formalized through mathematical models derived from solving "the basic physics of motion for inertia and restoring forces and applying normalizing boundary conditions" [2]. The resulting models produce motion that is "physically plausible, and thus realistic" while remaining computationally tractable and artistically controllable.

The physical basis for animation extends beyond simple particle dynamics to encompass the complex musculoskeletal structures of characters. Research in character animation emphasizes that "the motion of a character with many degrees of freedom needs to be consistent with the laws of physics" and that "in order for the motion to look realistic, the entire musculoskeletal structure must be taken into account" [11]. This holistic approach to physical realism recognizes that individual body parts do not move independently but are connected through anatomical and mechanical relationships that constrain and influence their collective motion.

### 2.2 The Expressive Imperative

While physical realism provides a foundation of believability, animation as an art form must also serve expressive and communicative purposes that may legitimately depart from strict physical accuracy. The tradition of animation has developed a rich vocabulary of expressive techniques that enhance emotional clarity, narrative emphasis, and aesthetic appeal. These techniques include exaggeration, anticipation, follow-through, squash and stretch, and secondary action, among others [10].

The principle of squash and stretch illustrates how expressiveness can enhance rather than undermine believability. In character animation, "squash and stretch are used not only to add realism to physical actions but also to enhance emotional expressiveness" [10]. When a character is surprised or frightened, exaggerated stretching can make the reaction "more dramatic and easily readable to the audience," while controlled squash during impact "gives the audience a tangible sense of the character's lightness and flexibility." This example demonstrates that expressiveness and physical plausibility are not opposing forces but complementary aspects of effective animation.

The concept of arcs provides another lens through which to understand the relationship between realism and expressiveness. "Since arcs are inherently smooth, they help create a seamless flow from one movement to the next, making the action feel cohesive" [10]. However, "applying them effectively requires a balance between realism and stylization. Too rigid an adherence to natural arcs might result in movements that are predictable or dull, while overly exaggerated arcs can break the illusion of reality." Skilled animators manipulate arcs "to enhance the storytelling without losing the sense of believability."

### 2.3 Rhythm as the Balancing Mechanism

Rhythm emerges as the critical mechanism through which physical realism and artistic expressiveness are reconciled in digital animation. Rhythm encompasses both timing, which determines when movements occur, and spacing, which determines how far objects move between temporal markers. As practitioners explain, "timing is the rhythm—the beats that decide when things happen," while "spacing is the choreography—how far something moves between those beats" [4]. When animators blend both with intention, even simple gestures become "emotionally rich and physically convincing."

The interdependence of timing and spacing creates opportunities for nuanced control over the balance between realism and expressiveness. A slow blink with wide spacing can express calm or sadness, while a quick blink with tight spacing might show surprise [4]. Similarly, a character running with uneven timing but perfect spacing "still looks off—because both elements must support each other to build a believable 3D animation flow." This interdependence means that rhythm design provides multiple degrees of freedom for adjusting the character of movement without sacrificing either physical plausibility or emotional impact.

## 3. Methodological Approaches

### 3.1 Kinematic Timing Curves and Physics-Based Models

One of the most significant methodological advances in achieving balance between realism and expressiveness involves the development of parameterized timing curves derived from physical principles. These curves provide closed-form solutions for animation effects that would be challenging to reproduce manually but for which full physics simulation would be excessive [2]. The approach involves "solving the basic physics of motion for inertia and restoring forces and applying normalizing boundary conditions" to create models with "manageable parameters that can express these behaviors."

The timing curve model extends the standard no-parameter timing curve with "three easy-to-visualize parameters: anticipation, midpoint, and bounces" [2]. These parameters can give rise to "a wide variety of expressive behaviors" while maintaining physical plausibility because the model is "derived from Newtonian physics." The anticipation parameter controls the preparatory motion before a primary action, the midpoint parameter influences the character of motion through the central portion of a movement, and the bounces parameter governs oscillatory behavior at the conclusion of motion.

The elegance of this approach lies in its ability to provide "a simple expression that reproduces these effects and smoothly blends between them while maintaining physical realism" [2]. The model is "controlled by three intuitive parameters" that "allow users to define physically correct procedural motions while maintaining a high degree of control." This combination of physical grounding and intuitive control exemplifies the balance that effective animation systems must achieve.

### 3.2 Motion Adaptation and Constraint-Based Methods

Motion adaptation methods provide another powerful framework for balancing physical realism and artistic expressiveness. These approaches take existing motion data, whether captured from real performers or generated through other means, and transform it to satisfy new constraints while preserving the essential qualities of the original motion [3]. The fundamental insight is that "motion for a model consists of signals (a signal being the time-varying data for a single parameter) that are represented by a set of samples that are potentially sparse."

The constraint-based approach allows animators to specify high-level goals, such as the timing and placement of specific actions, while the system automatically generates motion that satisfies these constraints while maintaining physical plausibility. For example, an animator might provide a jumping motion and specify that "the character touches a particular point at a particular time" [3]. The system then modifies the motion to satisfy this constraint while preserving the natural feel of the original animation.

This methodology can be understood through a common framework where "some previous motion adaptation methods can be viewed under a common framework and controlled using constraint techniques" [3]. Extensions to these methods "provide additional flexibility in the types of control" through a variety of applicable constraints. The constraint-based approach thus provides a structured way to introduce artistic intent into physically-based motion while maintaining the coherence and plausibility that physical constraints enforce.

### 3.3 Procedural Animation Systems

Procedural animation represents a paradigm where motion is generated algorithmically based on rules and parameters rather than through direct manipulation of keyframes or motion capture data. This approach offers significant advantages for balancing realism and expressiveness because it can incorporate physical simulation while providing artists with controllable parameters that influence the character of motion [7].

The design and implementation of physics-based simulations for procedural animation are "rather more complex compared to standard character- and key-frame animations," requiring substantial computational resources [7]. However, when properly implemented, procedural animation can "provide the field of character animation with fruitful results by animating complicated details" that would be difficult to achieve through manual animation alone. The complexity of procedural animation means that "there is little cohesive practice and no guidelines for a common studio practice," but the potential benefits for achieving realistic yet expressive motion make continued development worthwhile.

Modern procedural animation systems often integrate machine learning approaches that learn motion patterns from data and generate new motion that reflects those patterns. In this emerging paradigm, "the role of our animators is no longer to draw animation curves, creating state transitions, or blending clips. They're here to train agents" [9]. Animators "direct the feeling and intent of the final movement, rather than moving each leg themselves," while the system generates motion that balances physical realism with the desired expressive character.

### 3.4 Style Transfer and Temporal Consistency

The application of artistic styles to animated sequences presents unique challenges for maintaining both visual style and temporal coherence. While physical models can achieve realistic simulation of artistic media such as watercolor, oil paint, or pastel, "those techniques do not deal with the issue of preserving temporal consistency in animation" [1]. This limitation is particularly significant for rhythm design because temporal inconsistencies can disrupt the perceived physicality and emotional impact of motion.

Example-based style transfer to video sequences has advanced significantly, with improvements in both visual quality and computational efficiency [1]. Unlike still images, "when stylizing a video, one needs to take temporal continuity into account." The inputs to such systems typically include style exemplar sequences captured perpendicular to a canvas, binary masks denoting the presence of artistic media, and target masks defining placement in the output animation. These systems must balance the artistic goals of style transfer with the physical requirement of temporal coherence.

The challenge of temporal consistency extends beyond visual style to encompass the rhythm and timing of motion itself. Systems that successfully transfer artistic styles while maintaining temporal consistency enable animators to achieve distinctive visual aesthetics without sacrificing the physical believability that rhythm design establishes. This integration of style and timing represents an important frontier in the ongoing effort to balance realism and expressiveness in digital animation.

## 4. Practical Techniques and Tools

### 4.1 Timing and Spacing in Professional Workflows

Professional animation studios have developed refined workflows for achieving balance between physical realism and artistic expressiveness through careful attention to timing and spacing. The workflow typically begins with rough blocking to establish the overall timing, followed by frame-by-frame refinement of spacing to shape the performance's rhythm [4]. This staged approach allows animators to establish the broad strokes of physical motion before refining the expressive details.

Graph editors and timing charts serve as essential tools for fine-tuning the harmony between timing and spacing. These tools allow animators to visualize and manipulate the curves that govern motion over time, adjusting acceleration, deceleration, and other temporal characteristics [4]. The ability to see motion represented as curves makes it possible to achieve the precise balance between physical behavior and expressive intent that professional animation requires.

The principle of slow in and slow out, one of the foundational techniques of animation, exemplifies how timing can balance realism and expressiveness. Most objects in nature do not begin or end movement instantaneously but accelerate and decelerate gradually due to physical forces. By incorporating slow in and slow out, animators create motion that feels physically grounded while also providing visual emphasis and clarity to the beginning and end of actions [10].

### 4.2 Rigging and Control Systems

Rigging tools provide the technical infrastructure through which animators exercise control over character motion. These tools "allow animators to build control systems for characters, as if they were a virtual puppet, to ensure that they move naturally within a scene" [5]. The sophistication of rigging systems directly impacts the ability to achieve balance between physical realism and artistic expressiveness.

Industry-standard tools like Autodesk Maya, Blender, Houdini, and others provide increasingly powerful capabilities for creating and manipulating animation controls [5]. These tools enable animators to create rigs that embody physical constraints while providing artistic control over the timing and character of motion. The choice of rigging approach and the design of control systems significantly influence the range of expressive possibilities available to animators.

Procedural rigging and animation systems extend these capabilities by incorporating algorithmic generation of motion based on physical principles and artistic parameters. Research in this area has explored how "physics-based control models, such as the inverted pendulum, have supported stable and realistic locomotion across animated characters" [6]. These systems can generate motion that respects physical constraints while allowing artists to specify high-level parameters that influence the expressive character of movement.

### 4.3 The Twelve Principles as a Framework

The twelve principles of animation, developed through decades of artistic practice and codified for digital application, provide a comprehensive framework for balancing physical realism and artistic expressiveness. These principles, including squash and stretch, anticipation, staging, straight ahead action versus pose-to-pose, follow through and overlapping action, slow in and slow out, arcs, secondary action, timing, exaggeration, solid drawing, and appeal, offer specific techniques for achieving particular effects [10].

The principle of follow through and overlapping action articulates how different parts of a body or object move at different speeds, creating realistic and expressive motion. "Follow through refers to the action that occurs after a character or object comes to a stop, accounting for parts of the body that continue to move after the main action has finished" [10]. This principle "adds realism by mimicking the physical laws of motion and helps convey weight and inertia." Overlapping action, where "parts of a character or object move at different rates or times," adds "depth and complexity to animations by demonstrating that various elements react to motion independently."

The choice between straight ahead and pose-to-pose approaches represents another dimension of the balance between realism and expressiveness. "Straight ahead means drawing the animation frame-by-frame from beginning to end. This approach is often used for fast, unpredictable, or fluid movements (like fire, water, or or hair) because it creates natural, spontaneous motion" [10]. In contrast, "pose-to-pose means drawing a few key frames and then filling in the intervals. This method is used for more planned-out, controlled animations, such as character acting or complex movements. It helps maintain consistency in size, proportion, and timing."

## 5. Advanced Approaches and Emerging Techniques

### 5.1 Sketch-Based and Stroke-Centric Animation

Recent advances in sketch-based animation tools have expanded the possibilities for achieving balance between physical realism and artistic expressiveness. These tools "progressively reduce manual workload while maintaining creative control, incrementally automating the animation process, from physical effects and gesture replication to texture generation, semantic interpretation, and procedural motion" [6]. The evolution of these tools has moved "from assisting traditional animation to creating dynamic, adaptable animations with minimal artist input."

A significant advancement in this area enables artists to "embed continuous, coordinated motions into static sketches using motion handles and kinetic textures," enabling "dynamic environmental effects" [6]. These techniques preserve the expressive qualities of hand-drawn illustration while introducing physical motion that enhances believability. The integration of motion handles and kinetic textures demonstrates how physical motion can be added to stylistically distinctive artwork without overwhelming the artistic character of the original.

Stroke-centric and sketch-guided techniques now offer "powerful tools for direct, intuitive control while embedding data-driven intelligence for automated motion inference" [6]. These approaches allow artists to specify motion in terms that feel natural and expressive while the system generates motion that respects physical constraints. The balance between artistic control and physical realism is achieved through interfaces that translate artistic intent into motion parameters that the system can interpret and implement.

### 5.2 Machine Learning and Data-Driven Approaches

Machine learning has emerged as a powerful tool for achieving balance between physical realism and artistic expressiveness in animation. These approaches can learn motion patterns from large datasets and generate new motion that reflects those patterns while satisfying specified constraints. The integration of machine learning with animation workflows represents a significant shift in how animators conceptualize and execute their creative vision [9].

Data-assisted systems like Tracemove offer "frame-by-frame animation" capabilities that combine the precision of computational methods with the expressiveness of artistic input [6]. These systems can learn from examples of motion and apply that learning to new situations, generating motion that balances physical plausibility with the stylistic characteristics of the training data. The ability to transfer motion from video or example-based style propagation provides new avenues for achieving expressive motion that remains grounded in physical reality.

The application of machine learning to animation requires careful attention to the balance between automated generation and artistic control. As practitioners note, "introducing new procedural tools requires acceptance and a change of mindset" [9]. Teaching animators "how to best use machine learning and what you can and can't use it for is an ongoing effort." Successful integration requires collaboration between technical and artistic perspectives to ensure that the generated motion serves both physical and expressive goals.

### 5.3 Physics-Based Control for Character Animation

Physics-based character control methods generate motions with physical realism and environmental interactions, addressing the fundamental challenge of creating movement that respects the laws of physics while serving expressive purposes. The key challenge is "the design or learning of robust controllers with which to drive simulated characters" [11]. Research in this area has produced significant advances in synthesizing motion controllers for a wide range of motor tasks.

Manually-designed controllers have achieved notable success for locomotion and other fundamental movements [11]. These controllers encode physical principles and motion characteristics in rules that govern how characters respond to their environments and user inputs. The design of these controllers requires deep understanding of both the physical principles that govern realistic motion and the expressive qualities that make animation compelling.

Trajectory optimization methods and deep reinforcement learning represent more recent approaches to physics-based character control [11]. These methods can discover motion strategies that satisfy physical constraints while achieving specified goals, potentially revealing unexpected but effective approaches to movement. The integration of these methods with artistic control interfaces represents an important direction for achieving balance between physical realism and expressiveness.

## 6. Discussion

### 6.1 The Complementary Nature of Realism and Expressiveness

The evidence examined in this report suggests that physical realism and artistic expressiveness should be understood not as opposing forces in tension but as complementary aspects of effective animation that can be mutually reinforcing. The timing curves derived from Newtonian physics produce motion that is "physically plausible, and thus realistic" while also being capable of generating "a wide variety of expressive behaviors" through intuitive parameter control [2]. Similarly, squash and stretch adds both "realism to physical actions" and "enhances emotional expressiveness" [10].

This complementary relationship emerges from the recognition that physical principles themselves contain inherent expressive potential. The anticipation, midpoint, and bounces parameters of physics-based timing curves are not arbitrary artistic choices but reflect genuine physical phenomena that audiences intuitively recognize and respond to. By making these parameters explicit and controllable, animation systems enable artists to emphasize or modulate the physical character of motion to serve expressive purposes.

The principle of arcs illustrates this complementarity particularly clearly. Natural arcs arise from physical constraints on movement, yet "too rigid an adherence to natural arcs might result in movements that are predictable or dull" [10]. Skilled animators manipulate arcs to enhance storytelling while maintaining believability, finding the point where physical grounding serves expressive purposes rather than constraining them.

### 6.2 The Role of Constraint in Creative Motion

Constraint-based approaches to animation reveal how physical and artistic goals can be reconciled through the specification of constraints that must be satisfied. Motion adaptation methods take existing motion and transform it to satisfy new constraints while preserving essential qualities [3]. This approach acknowledges that both physical realism and artistic expressiveness can be formulated as constraints that the final motion must satisfy.

The constraint-based paradigm shifts the focus from generating motion from scratch to modifying motion to meet specified goals. An animator might specify that a character "touches a particular point at a particular time" [3], and the system generates motion that satisfies this constraint while maintaining physical plausibility. The constraint provides the artistic direction, while the system ensures that the resulting motion respects physical principles.

This approach has important implications for the balance between realism and expressiveness. Constraints can be formulated at multiple levels of abstraction, from low-level physical constraints like ground contact to high-level expressive constraints like the emotional quality of a movement. The system then finds motion that satisfies all applicable constraints, potentially discovering solutions that balance physical and artistic goals in ways that might not be obvious to human animators.

### 6.3 Workflow and Tool Design

The practical achievement of balance between physical realism and artistic expressiveness depends critically on the design of workflows and tools that enable animators to exercise appropriate control. Professional workflows that separate timing establishment from spacing refinement allow animators to address physical grounding before expressive refinement [4]. This staged approach acknowledges that physical and expressive considerations may require different types of attention at different stages of the animation process.

The development of graph editors and timing charts provides visual interfaces for manipulating the temporal characteristics of motion [4]. These tools make abstract concepts like acceleration and deceleration visible and manipulable, enabling animators to achieve precise control over the rhythm of movement. The effectiveness of these tools demonstrates how interface design can support the integration of physical and expressive considerations.

Rigging systems provide the underlying infrastructure for animation control, with more sophisticated rigs enabling more nuanced control over the balance between physical and expressive elements [5]. The choice of rigging approach and the design of control systems significantly influence the range of possibilities available to animators. Tools that embody physical constraints while providing artistic control over parameters enable animators to achieve balance without having to manually enforce physical correctness at every step.

## 7. Conclusion

The balance between physical realism and artistic expressiveness in digital animation rhythm design is achieved through a sophisticated integration of physical principles, mathematical models, artistic principles, and computational tools. This integration is not a one-time achievement but an ongoing process of refinement as new techniques and tools emerge. The research examined in this report reveals several key insights that guide effective practice in this area.

First, physical principles provide a foundation of believability that can coexist with and support expressive goals. Timing curves derived from Newtonian physics produce motion that is both physically plausible and capable of generating a wide range of expressive behaviors [2]. The key is to make physical parameters explicit and controllable, enabling artists to emphasize or modulate physical characteristics as needed.

Second, constraint-based approaches provide a framework for reconciling physical and artistic goals by formulating both as constraints that motion must satisfy. This approach acknowledges that balance is not a fixed point but a negotiated outcome that depends on the specific requirements of each animation [3]. Systems that can satisfy multiple constraints simultaneously enable animators to achieve balance without having to choose between physical correctness and expressive intent.

Third, the twelve principles of animation provide a time-tested vocabulary for achieving specific effects that balance realism and expressiveness. These principles, developed through decades of artistic practice, offer specific techniques for addressing common animation challenges [10]. Their application in digital contexts demonstrates their continued relevance and adaptability.

Fourth, workflow and tool design significantly impact the ability to achieve balance. Professional workflows that separate timing and spacing, interfaces that make temporal characteristics visible and manipulable, and rigging systems that embody physical constraints while providing artistic control all contribute to effective practice [4][5].

Finally, emerging techniques including sketch-based animation, machine learning, and physics-based control continue to expand the possibilities for achieving balance between physical realism and artistic expressiveness [6][9][11]. These approaches offer new ways to integrate physical simulation with artistic control, potentially revealing new strategies for balancing competing goals.

The ongoing development of techniques and tools for digital animation rhythm design reflects the fundamental importance of achieving balance between physical realism and artistic expressiveness. As computational capabilities increase and artistic understanding deepens, new opportunities will emerge for creating animation that is both believable and compelling. The principles and methods examined in this report provide a foundation for understanding and participating in this ongoing creative and technical endeavor.

## References

[1] Platkevic, J. et al. (2021). Style Transfer for Video Sequences. *Computer Graphics Technical Report*. Czech Technical University in Prague. https://dcgi.fel.cvut.cz/~sykorad/Platkevic21-PG.pdf

[2] Kinematic Timing Curves: Cartoon Physics with Ease. (2022). *Journal of Computer Graphics Techniques*, 11(3). https://jcgt.org/published/0011/03/02/paper.pdf

[3] Gleicher, M. (1998). Motion Adaptation for Computer Animation. *University of Wisconsin Graphics Lab*. https://graphics.cs.wisc.edu/Papers/1998/GL98/adapt.pdf

[4] Whizzy Studios. (2024). Timing and Spacing: The Secret Formula Behind Smooth 3D Animation. https://www.whizzystudios.com/post/timing-and-spacing-the-secret-formula-behind-smooth-3d-animation

[5] TESSR. (2024). 7 Digital Tools Necessary for Animators. https://www.tessr.us/post/7-digital-tools-necessary-for-animators

[6] arXiv. (2025). Sketch Animation Tools and Procedural Motion. https://arxiv.org/html/2510.10218v1

[7] Isikguner, B. (2014). Procedural Animation in Character Animation. *NTU Research Archive*. https://irep.ntu.ac.uk/id/eprint/310/1/220423_Baris_Isikguner_September2014_excl.3rdpartymaterial.pdf

[8] YouTube. (2024). Procedural Animation Tutorial. https://www.youtube.com/watch?v=A3y58qEUBu0

[9] Embark Studios. (2024). Transforming Animation with Machine Learning. https://medium.com/embarkstudios/transforming-animation-with-machine-learning-27ac694590c

[10] CGSpectrum. (2024). 12 Principles of Animation. https://www.cgspectrum.com/blog/12-principles-of-animation

[11] Zurich, E. (2023). Kinematic and Physics-Based Character Animation. *SFU Summit*. https://summit.sfu.ca/_flysystem/fedora/2023-04/etd22376.pdf

[12] Disney Research. Interactive Design of Stylized Walking Gaits for Robotic Characters. https://la.disneyresearch.com/wp-content/uploads/Interactive_Design_of_Stylized_Walking_Gaits_for_Robotic_Characters-5.pdf

## Annotations


## Sources
[1] https://arxiv.org/html/2510.10218v1
[2] https://cgl.ethz.ch/Downloads/Publications/Dissertations/Schm12.pdf
[3] https://dcgi.fel.cvut.cz/~sykorad/Platkevic21-PG.pdf
[4] https://graphics.cs.wisc.edu/Papers/1998/GL98/adapt.pdf
[5] https://homes.cs.washington.edu/~zoran/sigg99/preprint.pdf
[6] https://irep.ntu.ac.uk/id/eprint/310/1/220423_Baris_Isikguner_September2014_excl.3rdpartymaterial.pdf
[7] https://jcgt.org/published/0011/03/02/paper.pdf
[8] https://la.disneyresearch.com/wp-content/uploads/Interactive_Design_of_Stylized_Walking_Gaits_for_Robotic_Characters-5.pdf
[9] https://medium.com/embarkstudios/transforming-animation-with-machine-learning-27ac694590c
[10] https://summit.sfu.ca/_flysystem/fedora/2023-04/etd22376.pdf
[11] https://www.cgspectrum.com/blog/12-principles-of-animation
[12] https://www.linkedin.com/pulse/6-animation-techniques-frank-govaere-xyhaf
[13] https://www.tessr.us/post/7-digital-tools-necessary-for-animators
[14] https://www.whizzystudios.com/post/timing-and-spacing-the-secret-formula-behind-smooth-3d-animation
[15] https://www.youtube.com/watch?v=A3y58qEUBu0