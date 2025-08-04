# Load the molecule
set mol [mol new "C:/Users/teemo/Downloads/fibrocystin_and_L_models/human_fc_parts/hfbr_1_to_500.pdb"]
set backbone [atomselect $mol "backbone" ]

# Get the number of residues
set num_residues [measure numresidues $backbone ]

# Initialize lists to hold phi and psi angles
set phi_angles {}
set psi_angles {}

# Loop over residues to calculate phi and psi
for {set i 1} {$i <= $num_residues} {incr i} {
    # Calculate phi angle
    if {$i > 1} {
        set atom1 [atomselect $backbone "resid [expr {$i-1}] and name N"]
        set atom2 [atomselect $backbone "resid $i and name CA"]
        set atom3 [atomselect $backbone "resid $i and name C"]
        set atom4 [atomselect $backbone "resid [expr {$i+1}] and name N"]
        
        if {[$atom1 num] == 1 && [$atom2 num] == 1 && [$atom3 num] == 1 && [$atom4 num] == 1} {
            set phi [measure dihedrals [$atom1 get {x y z}] [$atom2 get {x y z}] [$atom3 get {x y z}] [$atom4 get {x y z}]]
            lappend phi_angles $phi
        } else {
            puts "Skipping phi calculation for residue $i due to missing atoms."
        }

        # Clean up selections
        $atom1 delete
        $atom2 delete
        $atom3 delete
        $atom4 delete
    }

    # Calculate psi angle
    if {$i < $num_residues} {
        set atom1 [atomselect $backbone "resid $i and name N"]
        set atom2 [atomselect $backbone "resid $i and name CA"]
        set atom3 [atomselect $backbone "resid $i and name C"]
        set atom4 [atomselect $backbone "resid [expr {$i+1}] and name N"]
        
        if {[$atom1 num] == 1 && [$atom2 num] == 1 && [$atom3 num] == 1 && [$atom4 num] == 1} {
            set psi [measure dihedrals [$atom1 get {x y z}] [$atom2 get {x y z}] [$atom3 get {x y z}] [$atom4 get {x y z}]]
            lappend psi_angles $psi
        } else {
            puts "Skipping psi calculation for residue $i due to missing atoms."
        }

        # Clean up selections
        $atom1 delete
        $atom2 delete
        $atom3 delete
        $atom4 delete
    }
}

# Output phi and psi angles
puts "Phi angles: $phi_angles"
puts "Psi angles: $psi_angles"
