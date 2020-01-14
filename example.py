import reaction_pypaths

energy_diagram = reaction_pypaths.Diagram()

# add the levels to the diagram
formula1 = energy_diagram.add_level(1.1, "crazy formula $[ZX_2]_5^{+}$\n$AB_3$")
PMM14 = energy_diagram.add_level(-0.1, "$(PMM14)_3$", True)
PZX14_mix = energy_diagram.add_level(-0.5, "$(PZX14)_3 + P4$")
transition_state = energy_diagram.add_level(0, "TS")
p1 = energy_diagram.add_level(-1.1, "product 1")
p2 = energy_diagram.add_level(-0.4, "product 2")

# add links between the levels
energy_diagram.add_link(formula1, PZX14_mix)
energy_diagram.add_link(PMM14, PZX14_mix)
energy_diagram.add_link(PZX14_mix, transition_state)
energy_diagram.add_link(transition_state, p1)
energy_diagram.add_link(transition_state, p2)

# plot the diagram and save the final result to the file
energy_diagram.plot("output.png")
