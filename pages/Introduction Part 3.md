- ![Slides](C:\Users\jonat\OneDrive - bwedu\stud\master\2\A\Slides\00_Introduction\Part3-CRNs.pdf)
- ![Highham](C:\Users\jonat\OneDrive - bwedu\stud\master\2\A\Slides\03_Chemical_Reactions\Higham2008.pdf)
- We will discuss different stochastic modeling approaches to describe the dynamics of small chemical reaction networks
- Übungen in python
- ### Stochastische Prozesse
	- Dichtefunktion und Zufallsvariablen
- ## Chemical Reaction Networks (CRNs)
- $N$ molecule types
- $M$ reactions
- rate constants $c_j$
- state change vectors $\nu_j$
-
- Master Gleichung der Chemie (Chemical Master Equation CME)
- $$ \frac{dP(x,t)}{dt} = \sum_{j=1}^m a_j(x - \nu_j) P(x - \nu_j, t) - a_j(x) P(x,t) = MP(x,t)$$
- Vereinfachung und andere Modellklassen
- ### Problem CRNs
	- Sehr große Anzahl an Microstates
- ### Stochastische Simulationsalgorithmus (SSA)
	- Waiting time T
		- for microstate $x^k$
	- Reaktions Index $J$
- ### $\tau$-leaping
- ### Chemische Langevin Gleichung (CLE)
- ### RRE
-
- # Prüfung
-
- ## Leitfragen
- Which **modeling approaches** do exist to describe CRNs?
- On which **assumptions** are these based?
- How are these approaches **related**?
- For a given reaction system, describe approach XY.
	- How do the equations look like?
	- How does the simulation look like?
	- How to implement the model?
	- (choose 2 of the four approaches in advance that you should be able to explain in detail)