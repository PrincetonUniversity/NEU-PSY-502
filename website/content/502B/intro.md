# Syllabus

NEU 502B<br>
Princeton University, Spring 2025<br>
**Time:** Tu/W 2:00–5:00 pm<br>
**Location:** PNI A03<br>
**Instructor:** Sam Nastase ([snastase@princeton.edu](snastase@princeton.edu))<br>
**AIs:** Kirsten Ziman ([kz0108@princeton.edu](kz0108@princeton.edu)), Ariadne Letrou ([ariadne@princeton.edu](ariadne@princeton.edu))<br>
**Syllabus:** [`Syllabus`](https://docs.google.com/document/d/1l-3O_eeZp_msTFY76TnRhKqZ37gdc1U860aRqd41988/edit?usp=sharing)<br>
**GitHub:** [`GitHub`](https://github.com/NEU502B/neu502b-2025)<br>
**Scratch:** [`Scratch`](https://docs.google.com/document/d/1q_i1X60_9cj2wMTuAFuuP6raWhcAJ_cwRK4qkR0IZAk/edit?usp=sharing)

---

This lab course closely accompanies NEU 502A and surveys the methodological landscape of cognitive computational neuroscience research. Students will learn the fundamentals of experimental design, data collection, preprocessing, and statistical analysis for fMRI and EEG/MEG, with an emphasis on best practices in reproducible neuroscience. Lectures will set the conceptual foundation for interactive, hands-on lab work using Jupyter notebooks. Advanced topics include multivariate pattern analysis (MVPA), representational similarity analysis (RSA), and regularized encoding models. This year, we're experimenting with a new format that will interleave two threads: empirical (*E*) classes focused on fMRI and MEG projects, and computational (*C*) classes focused on modeling and neural networks. *E* classes will provide the empirical backbone of the course, while *C* classes (typically on Wednesdays) will focus on interactive modeling exercises paralleling the topics discussed in 502A. These two threads will converge over the course of the term. Students will be expected to design, analyze, and write up both an fMRI experiment and an OPM-MEG experiment as graded projects.

---
### Lecture schedule

| Date | Topic | Slides/code                                                                                                                                                                           | Optional reading |
| --- | --- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- |
| Tu 1/28 (*E*) | Introduction and computing; MR physics and BOLD biology | [`Slides`](https://docs.google.com/presentation/d/1RZmTeYgUvjGUuW5EAkIRovwMJHa9K4kbODAjthHzVZw/edit?usp=sharing) [`Code`](https://github.com/NEU502B/neu502b-2025/tree/master/fmri-1) | [`Logothetis et al., 2001`](https://doi.org/10.1038/35084005) [`Kriegeskorte & Douglas, 2018`](https://doi.org/10.1038/s41593-018-0210-5) [`Richards et al., 2019`](https://doi.org/10.1038/s41593-019-0520-2) |
| W 1/29 (*E*) | fMRI design, preprocessing, and subject-level modeling (GLM) | [`Slides`](https://docs.google.com/presentation/d/1UyRfx_L24U0_7E0Pc1OnZZlkiz-yPOIxNmSsuBUecgA/edit?usp=sharing) [`Code`](https://github.com/NEU502B/neu502b-2025/tree/master/fmri-2) | [`Friston et al., 1994`](https://doi.org/10.1002/hbm.460020402) [`Power et al., 2012`](https://doi.org/10.1016/j.neuroimage.2011.10.018) [`Esteban et al., 2019`](https://doi.org/10.1038/s41592-018-0235-4) |
| Tu 2/4 (*E*) | fMRI group-level analysis and correction for multiple tests |                                                                                                                                                                                       | [`Nichols & Holmes, 2002`](https://doi.org/10.1002/hbm.1058) [`Eklund et al., 2016`](https://doi.org/10.1073/pnas.1602413113)
| W 2/5 (*C*) | Dynamics in perception | [`Code`](Computation/Dynamics%20in%20Perception/intro.md)                                                                                                                             | [`Hopfield et al., 1982`](https://doi.org/10.1073/pnas.79.8.2554) |
| Tu 2/11 (*E*) | Multivariate pattern analysis (MVPA)<br>fMRI project group formation and brainstorming |                                                                                                                                                                                       | [`Haxby et al., 2001`](https://doi.org/10.1126/science.1063736) [`Norman et al., 2006`](https://doi.org/10.1016/j.tics.2006.07.005) |
| W 2/12 (*C*) | Decision making | [`Code`](Computation/Decision%20Making/intro.md)                                                                                                                                      | [`Bogacz et al., 2006`](https://doi.org/10.1037/0033-295X.113.4.700) |
| Tu 2/18 (*E*) | Representational similarity analysis (RSA) and searchlights<br>fMRI project proposal presentations |                                                                                                                                                                                       | [`Edelman, 1998`](https://doi.org/10.1017/S0140525X98001253) [`Kriegeskorte et al., 2006`](https://doi.org/10.1073/pnas.0600244103) [`Kriegeskorte et al., 2008`](https://doi.org/10.3389/neuro.06.004.2008) |
| W 2/19 (*C*) | Reinforcement learning |                                                                                                                                                                                       | [`Montague et al., 1996`](https://doi.org/10.1523/JNEUROSCI.16-05-01936.1996) [`Botvinick et al., 2020`](https://doi.org/10.1016/j.neuron.2020.06.014) |
| Tu 2/25 (*E*) | Naturalistic neuroimaging and voxelwise encoding models<br>fMRI project experimental design |                                                                                                                                                                                       | [`Naselaris et al., 2011`](https://doi.org/10.1016/j.neuroimage.2010.07.073) [`Huth et al., 2016`](https://doi.org/10.1038/nature17637) [`Nastase et al., 2020`](https://doi.org/10.1016/j.neuroimage.2020.117254) [`Hasson et al., 2020`](https://doi.org/10.1016/j.neuron.2019.12.002) |
| W 3/4 (*C*) | Statistical learning and backpropagation |                                                                                                                                                                                       | [`Rumelhart et al., 1986`](https://doi.org/10.1038/323533a0) [`McClelland & Rogers, 2003`](https://doi.org/10.1038/nrn1076) |
| Tu 3/4 (*E*) | fMRI project data collection |                                                                                                                                                                                       | |
| W 3/5 (*E*) | fMRI project data collection |                                                                                                                                                                                       | |
| Tu 3/11 | _No class (spring recess)_ |                                                                                                                                                                                       | |
| W 3/12 | _No class (spring recess)_ |                                                                                                                                                                                       | |
| Tu 3/18 (*E*) | fMRI project data analysis |                                                                                                                                                                                       | |
| W 3/19 (*C*) | Statistical learning and language processing |                                                                                                                                                                                       | [`Manning et al., 2020`](https://doi.org/10.1073/pnas.1907367117) |
| Tu 3/25 (*E*) | EEG/MEG signal, preprocessing, and modeling |                                                                                                                                                                                       | [`Buzsáki et al., 2012`](https://doi.org/10.1038/nrn3241) [`Fries, 2015`](https://doi.org/10.1016/j.neuron.2015.09.034) |
| W 3/26 (*C*) | Selective attention, automaticity, and control |                                                                                                                                                                                       | [`Cohen et al., 1990`](https://doi.org/10.1037/0033-295X.97.3.332) |
| Tu 4/1 (*E*) | MEG project proposals and experimental design |                                                                                                                                                                                       | [`Baillet, 2017`](https://doi.org/10.1038/nn.4504) [`Brooks et al., 2022`](https://doi.org/10.1016/j.tins.2022.05.008) |
| W 4/2 (*C*) | Conflict monitoring, effort, and control |                                                                                                                                                                                       | [`Shenhav et al., 2017`](https://doi.org/10.1146/annurev-neuro-072116-031526) |
| Tu 4/8 (*E*) | MEG project data collection |                                                                                                                                                                                       | |
| W 4/9 (*E*) | MEG project data analysis |                                                                                                                                                                                       | |
| Tu 4/15 (*E*) | Deep learning models for vision |                                                                                                                                                                                       | [`Kriegeskorte et al., 2015`](https://doi.org/10.1146/annurev-vision-082114-035447) [`Yamins & DiCarlo, 2016`](https://doi.org/10.1038/nn.4244) [`Lindsay, 2021`](https://doi.org/10.1162/jocn_a_01544) |
| W 4/16 (*E*) | Progress report presentations |                                                                                                                                                                                       | |
| Tu 4/22 (*E*) | Deep learning models for language |                                                                                                                                                                                       | [`Schrimpf et al., 2021`](https://doi.org/10.1073/pnas.2105646118) [`Goldstein et al., 2022`](https://doi.org/10.1038/s41593-022-01026-4) [`Zada et al., 2024`](https://doi.org/10.1016/j.neuron.2024.06.025) |
| W 4/23 (*E*) | fMRI and MEG project presentations |                                                                                                                                                                                       | |
| M 5/6 | _No class (final written reports due)_ |                                                                                                                                                                                       | |


The content of this course is inspired by related courses designed by Jonathan Cohen, Leigh Nystrom, Jody Culham, and Jim Haxby, and built on top of lots of hard work by Younes Strittmatter, Zaid Zada, and many others.

---

### Supplementary reading

Rokem, A., & Yarkoni, T. (2024). _Data Science for Neuroimaging: An Introduction_. Princeton University Press. [`link`](https://press.princeton.edu/books/hardcover/9780691222738/data-science-for-neuroimaging)

Huettel, S. A., Song, A. W., & McCarthy, G. (2014). _Functional Magnetic Resonance Imaging_ (3rd Ed.). Sinauer Associates. [`link`](https://global.oup.com/academic/product/functional-magnetic-resonance-imaging-9780878936274)

Poldrack, R. A., Mumford, J. A., & Nichols, T. E. (2011). _Handbook of Functional MRI Data Analysis_. Cambridge University Press. [`DOI`](https://doi.org/10.1017/CBO9780511895029)

Bandettini, P. A. (2020). _fMRI_. MIT Press. [`link`](https://mitpress.mit.edu/9780262538039/fmri/)

Luck, S. J. (2014). _An Introduction to the Event-Related Potential Technique_ (2nd ed.). MIT Press. [`link`](https://mitpress.mit.edu/9780262621960/an-introduction-to-the-event-related-potential-technique/)

McClelland, J. L. (2015). _Explorations in Parallel Distributed Processing: A Handbook of Models, Programs, and Exercises_ (2nd ed.). MIT Press. [`PDF`](https://web.stanford.edu/group/pdplab/pdphandbook/handbook.pdf)

Duvernoy, H. M. (1999). _The Human Brain: Surface, Three-Dimensional Sectional Anatomy with MRI, and Blood Supply_ (2nd ed.). Springer. [`DOI`](https://doi.org/10.1007/978-3-7091-6792-2)

