# Exam Questions

## 2022/23

**Helmig, Koch, Schneider**

*Master A: Ich habe die Prüfung allein gemacht, üblich ist eine Tandem-Prüfung. Prüfer waren Timo und Martin. Fragen hat nur Timo gestellt. Formeln und Skizzen sollten auf ein bereitgestelltes Blatt geschrieben werden. Atmosphäre war entspannt. Es gab Schokolade aus Norwegen und Wasser.*

#### A Physiologie:

* Welche Arten den Blutfluss zu betrachen, haben wir angeschaut?
  * Einphasenmodell / Zweiphasenmodell
* Was ändert sich, wenn wir das Einphasenmodell betrachten und welche effektive Variable beschreibt das?
  * Viskosität und Reynoldszahl
* Wie ändert sich der Durchmesser über die verschiedenen Vessel?
  * - da meine Zeichnung nicht schön war sollte ich noch Zahlen hinschreiben.
* Welchen Einfluss hat der Durchmesser in den Kapillaren auf die Reynoldszahl?
  * keiner Durchmesser verringert die Re

#### B Navier-Stokes:

* welche Annahmen haben wir getroffen?
  * Runde Geometrien und zentriert auf z-Achse, inkompressibel, alles abhängig von theta und abgeleitet nach theta ist null
* Hinschreiben der Massengleichung nach Integration und bennenen der Variablen
  * - A Fläche, Q Fluss
* Welches Problem haben wir nach der Herleitung der Gleichungen?
  * mit p, Q, A drei Unbekannte, aber nur zwei Gleichungen -> Beziehung zwischen A und p
* skalare Transportgleichung aufschreiben
* FVM: Wie bestimmen wir den Fluss und warum betrachten wir den Fluss an den Kontrollvolumengrenzen?
  * Central, Lax-Friedrich und Upwind erklären und dazu erählen, dass es ausreicht, den Fluss über die Kontrollvolumengrenzen zu betrachten, da sich damit die Änderung beschreiben lässt.

## 2018/19

**Herkert/Selmi bei Helmig**

* Windkesseleffekt erklären
  * Windkessel malen und dann auf Herzkreislaufsystem übertragen
  * Druckverlaufen malen über Entfernung zum Herzen
* NS-Gleichung aufschreiben und
  Transportgleichung
* Annahmen aufschreiben
  * inkompressibles Fluid, wie würde kompressible
    Transportgleichung aussehen?
* NS vereinfachen unter Annahme konstanter Viskosität
  * Wo ist Viskosität konstant? => Fahreus-
    Linquist-Effekt aufmalen.
* Zur **Transportgleichung**:
  * Welchen Term kann man bei schneller Strömung weglassen?
    * (Diffusionsterm)
  * Welche Zahl gibt darüber Auskunft?
    * (Peclet-Zahl)
* **Charakteristiken**
  * Was sind Charakteristiken
  * Wie bestimmt man mithilfe der Charakteristiken und den Anfangsdaten die Lösung zum Zeitpunkt $t$ an der Stelle $x$?
  * Was passiert, wenn sich Charakteristiken schneiden?
    * Lösung uneindeutig, Schockwelle
  * Warum sind Charakteristiken hier linear? (da Gleichung linear)
* Transportgleichung mit FD diskretisieren bei vorgegebener Strömungsrichtung.
  * Welche Ordnung hat das Verfahren bei den einzelnen Termen?
    * (einseitige FD für Transport ist von Ordnung 1, zweiseitige
      FD für Diffusion ist zweite Ordnung)
  * 1D Gleichung aufschreiben (mit Q und A).
    * Wo steckt der Verlusttermin drin? (Kr)
    * Welche Ordnung hat der Verlustterm? (=>2)

## 2018

**Köppl**

Pro Prüfung 25 min mit je 2 Personen. Die Leute werden nacheinander geprüft, daher keine
Zwischenfragen an den anderen.

1. Prüfung
   1. Prüfling
      • Herz inklusive Klappen beschriften
      • 0D-Modell wie modelliert
      o Wie aufgebaut
      o 3 Gleichungen: dQ/dt, dp/dt, dV/dt
      o Wie wird die Diode modelliert
      o Wie sind die Formeln für die Flüsse e(t)=...
   2. Prüfling
      • 3D-Navier Stokes hinschreiben und erklären
      • 1D Mittelung vornehmen
      • Fahreaus-Linquist Effekt beschreiben, auf welche Blutkörperchen
      wirkt er sich aus
2. Prüfung
   1. Prüfling
      • p-t-Diagramm in der Aorta und im Herz (Systole, Diastole
      einzeichnen) zeichnen und erklären
      • RCR (Windkesselmodell) beschriften und erklären
   2. Prüfling
      • Geschwindigkeit in verschiedenen Gefäßen
      • FD-Verfahren Ordnungen, Vor-/Nachteile
3. Prüfung
   1. Prüfling
      • Fahraeus-Linquist Diagramm
      • Reynolds und Womersley Zahl
      • Gebietszerlegung
      • Geschwindigkeitsmodellierung in den Gefäßen (Diagramm mit der
      Abhängigkeit von Gamma)
   2. Prüfling
      • RCR erklären
      • Carreau-Modell Formel
      • Eigenschaften Blut -> newtonsch/nicht-newtonsch
4. Prüfung
   1. Prüfling
      • Circle of Willis + Krankheiten + Ausgleichsmaßnahmen -> warum
      Simulation
      • 1D-Navier Stokes auf Transportgleichungen
      • Lineare Transportgleichung wie lösen? Welche Charakteristik? Was
      ist eine Charakteristik? Warum ist z=z0+at eine Lösung?
   2. Prüfling
      • Druckverteilung Gefäßstruktur. Warum nimmt Geschwindigkeit und
      Druck in den Kapillaren ab? Metabolische Autoregulierung der
      Muskeln
      • FD numerische Verfahren. Wann gibt es Probleme bei
      Transportgleichungen (Sprung). Was passiert bei verschiedenen
      Verfahren (LF, LW)
      • Stabilität (hinschreiben), Konsistenz (hinschreiben)
      • TVD, lokale Massenbilanz, Monotonie hinschreiben
5. Prüfung
   1. Prüfling
      • p-t-Diagramm Aorta und Herzkammer
      • Herzkammer modell hinzeichnen und erklären
      • Massenerhaltung, P_i(t), LQ=...
      • Dioden -> ideal, nicht ideal,...
   2. Prüfling
      • Alles zu DG
      • Slope Limiter
      • Wie könnte man Slope Limiter am Rand umsetzen? -> Konstante
      Fortsetzung des Dirichlet Randwerts
6. Prüfung
   1. Prüfling
      • Von Neumann-Analyse (nicht in den Folien)
      • Abhängigkeitsbaum zur Erklärung von CFL
      • Herleitung Charakteristiken z(t) = z0+at für lineare
      Transportgleichung
   2. Prüfling
      • Herzkammermodell
      • Konsistenz, Konvergenz, Stabilität
7. Prüfung
   1. Prüfling
      • p-t-Diagramm
      • RCR
      • Numerische Verfahren: Merkmale -> Stabilität, Konsistenz,
      Konvergenz
   2. Prüfling
      • Warum wird Blut in den Venen und nicht in den Arterien
      abgenommen?
      • 1D Navier-Stokes
      • DG: Vorteile, Warum, Wie? Slope Limiting -> Basis?
      • 1D-0D Übergang

## 2015/16

**Helmig**

- Wie kann man Blut modellieren?
  - -> welche Bestandteile sind im Blut
    - (rote Blutkörperchen, weiße, Blutplättchen,…);
    - Blut ist eigentlich nicht-newtonsch kann aber teilweise newtonsch
      modelliert werden
- Formel für Viskosität aufschreiben und motivieren
  - -> Element welches verzerrt wird aufmalen
- Formel für **Reynoldszahl** und **Peclet-Zahl** aufschreiben
  - erklären, wofür sie stehen
- Wie modellieren wir?
  - -> Gebietszerlegungsansatz,
  - 3D -> 1D/0D,
  - sinnvolle RB finden durch
    Charakteristikenverfahren
- RB am Auströmrand -> ausströmende Charakteristik mit Upwinding, andere über freies
  Ausströmen (konstanter Wert) oder Einfluß kleiner Gefäße (0D, Vergleich E-Lehre, Schaltkreis
  aufmalen)
- Wie geht man bei Charakteristikenverfahren vor
  - -> Jakobi-Matrix, Eigenwerte und Eigenvektoren finden
  - in charakteristische Variablen transformieren
  - $\pm \lambda_{1,2} \to$  unterschiedliche Fließrichtungen
- RB am Einströmrand -> ausströmende Charakteristik mit Upwinding, andere mit physiologischem
  Modell (Sinus; 5.7 Liter modelliert Q_in)
- Numerisches Modellproblem aufschreiben
  - Qualitätskriterien nennen
    - Konsistenz
    - Stabilität
    - Konvergenz
    - Dissipation
    - Dispersion
    - Monotonie
    - TVD
    - Massenerhaltung – auch erklären können)
- Wann ist Konsistenzordnung gleich Konvergenzordnung
  - Stabilität + hinreichend glatte Funktion
- Wie haben wir Konsistenzordnung für Lax-Wendroff hergeleitet
  - Taylorapproximation, würde deshalb für nicht glatte Lösungen nicht funktionieren
- Aufzeichnen, wie sich Lax-Wendroff an Sprungstelle verhält
  - Oszillationen

## 2014/15

**Tobi & Niko bei Helmig**

Helmig/Köppl (Köppl stellt die Fragen)

> #### A Physiologie
>
> * Probleme beim Modellieren von Gefäsystemen
>
>   * (groß/kleine Gefäße, Konvektions/Diffusionsgetrieben) Fließeschwindigkeit in großen Arterien (20cm/s)
> * Einfache Transportgleichung aufstellen und ~~schwache Formulierung~~ motivieren und erklären
>
>   * DG Verfahre motivieren und erklären
> * schiebt uns ein Blatt zu auf dem man ein **Konzentrationspeak** zu einer gegebenen einfachen Advektionsgleichung ver鋘dern soll.. einfach nach rechts verschieben (a war positiv)
> * zeichne Ansatzfunktionen vom Grad 0 in Graph ein (stückweise konstant)
>
>   * -> welche Probleme treten auf (Diffusion)
>
> ##### Gewebe
>
> * Wie modelliert man das -> por鰏es Medium
> * Welche Gleichungen treten auf (Perfusion, Transport)
> * Zur Transportgleichung: wie ist die aufgebaut/einzelne Terme
> * Warum benutzen wir finite Volumen bzw. DG -> lokal massenkonservativ sonst gro遝 Probleme, Massenverlust

## Ungeordnet aus *Helmig gesamt*

Köpl:

- Herzschlag aufmahlen in großer Aterie (t-P Digramm)
- wie moddeliert man den Abfall des Drucks
  - 0D System mit Wiederstand und Kapazität
- Wie moddeliert man Adernsystem
  - Navier-Stokes die dann 1-D gamcht werden über Integration
- Welche Größen kommen in 1D Gleichung vor
- Numerisches lösen dieser Gleichung
  - Diskretisierung, Zeitschrittverfahren
- Wann ist ein Verfahren Konvergent
  - Konsistent + Stabil
- Stabilitäts bedingung (CFL) motiviert durch geo. Anschauung mit Abhängigkeitskegel und Charakteristik

Helmig/Köppl:

- Wofür Simulationen von Gefäßssysstemen? (im Vgl. zu realen Messungen usw.)
- Welche Modelle gab's
  - 3D Navier-Stokes...-1D-1D linear-0D
- Motivation: Stenosis, Malformation (bei den Kapillaren), Aneurysmen
- Geschwindigkeitsplot über Größenskalen (Arterien, Arteriolen, Kapillaren, Venen), Koordinatensystem schon von Köppl ausgedruckt vorbereitet - was ist daran das Problem?
- Druck über einen Herzschlag (1s), auch hier Koordinatensystem schon vorbereitet
- Diskretisierungen/Numerik: Probleme (Dissipation usw.) -> 3 zusätzliche Qualitätskriterien
- Idee schwache Lösungen (Integral, Testfunktionen)
- Kopplung gegenüber weggelassenen Gefäßen (Compliance, Resistance)
- Geschwindigkeitsprofil in Arterie - wieso sieht das so aus, wie in Modellierung/Gleichungen berücksichtigt?

Helmig:

> Gibt Impulsgleichung, Massenerhaltung und Transportgleichung vor, zeichnet Netzwerk mit Verzweigung an
>
> * welche Probleme treten an Bifurkationen auf
>   * evtl. Schockwellen
> * welcher Term macht Probleme
>   * konvektiver
> * Wie kann man dies umgehen?
>   * Wann Stokesgleichung?
>   * Unter welchen Annahmen ($Re \ll 1$)?
>   * Wann gut?
>     ... (mind. zwei weitere Fragen)
> * Welche Drücke gibt es?
>   * Hydrostatischer Druck und osmotischer Druck,
>   * Beispiele nennen.
>     * Bspw. **Kirsche platzt im Sommer nach Regen.**
>     * Nochmal allgemeiner mit Membran und Konzentrationsunterschieden. Wieso funktioniert das? Woher wissen die Wassermoleküle, dass innen weniger Zucker vorhanden ist?

* Brownsche Molekularbewegung etc.
  * Modellierung des kapillaren Betts/Interstitiums.
  * Ansätze?
    * Einkontinuums-/Doppelkontinuumsansatz.
    * Erklärung und Auswahl treffen?

> * Wie wird gemittelt, Porositäten etc.
>   * Welche Annahmen
>   * warum sind diese gut?
>   * Wo liegen Nachteile?
>   * Wie kann man das Doppelkontinuumsmodell weiter verbessern?

 Helmig:

- Er hat die **Blianzgleichungen** aufgeschrieben: Wenn man eine **Bifurkation** modelliert, welche RB hat man am Bifurkation-Punkt?
- Welcher Term der Bilanzgleichung macht mir Probleme bei der Bifurkation?
  - hab ich nicht gewusst, daher hat er erst nach den Termen einzeln gefragt: Was bedeutet der advektive Anteil? Charakteristiken? Upscaling? etc.)
- Angenommen wir betrachten einen Teil des Vaskularensystems, der so klein ist, dass Bifurkationen keine Rolle spielen, welche Terme kann man am ehesten weglassen (ungefähr welche Größenordnung im Menschen?) welche Kennzahl gibt mir darüber aufschluss?
- Wie modelliert man das Kapillare Bett?
  - Welche Kräfte sind für den Austausch wichtig?
  - Osmothischer Druck
    - was ist osmotischer Druck?
  - hydrostatischer Druckgradient
    - wie sieht es beim hydrostatischen Druck aus?
- Wurden Deformationen des Gewebes bei der Modellierung im DCM berücksichtigt?
  - Nachdem ich dies verneint hatte, hakte Helmig nochmal nach warum man diese vernachlässigen kann.
  - (An dieser Stelle wollte er hören, dass das aufgrund der großen Reibung im System vernachlässigt werden kann.)

"Helmig" (Fragen stellt Köppl)

* Was modeliliert? (Arterien, Venen, Herz/Lungenkreislauf)
* Geschwindigkeiten in Venen und Arterien ?(Diagramm zeichnen)
* iwas zu gemittelte Navier Stokes
* Probleme bei FD Verfahren? (Diffusiv, Osizillation skizzieren)
* bei Bifurkationen was gemacht? Char.Variablen upwinden, #Unbekannte, Welche Gleichungen
* Modell in Kapillaren? (Re<<1 => Darcy hinschreiben + nicht Newtonität vernachlässigbar)
* (Idee von)Herleitung von Diff/Adv Gleichungen? (Kontrollvolumen, Verlustterme, Darcy einsetzen)

(Dopplung)
