#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser, PPBuilder
import matplotlib.ticker as ticker
def calculate_phi_psi(structure):
    phi_angles = []
    psi_angles = []

    for model in structure:
        for chain in model:
            ppb = PPBuilder()
            polypeptides = ppb.build_peptides(chain)

            for poly in polypeptides:
                residues = list(poly)  # Get the residue objects
                num_residues = len(residues)

                for i in range(num_residues):
                    # Calculate phi (if there's a previous residue)
                    if i > 0 and i < num_residues - 1:
                        phi = calculate_phi(residues[i - 1], residues[i], residues[i + 1])
                        if phi is not None:
                            phi_angles.append(np.degrees(phi))
                    
                    # Calculate psi (if there's a next residue)
                    if i < num_residues - 2:
                        psi = calculate_psi(residues[i], residues[i + 1], residues[i + 2])
                        if psi is not None:
                            psi_angles.append(np.degrees(psi))

    return phi_angles, psi_angles

def calculate_phi(res1, res2, res3):
    if res1.has_id('N') and res2.has_id('CA') and res3.has_id('C'):
        N = res1['N'].get_vector()
        CA_prev = res1['CA'].get_vector()
        CA = res2['CA'].get_vector()
        C = res3['C'].get_vector()
        return np.arctan2(CA_prev[1] - N[1], CA_prev[0] - N[0])  # Simplified for illustration
    return None

def calculate_psi(res1, res2, res3):
    if res1.has_id('CA') and res2.has_id('C') and res3.has_id('N'):
        CA = res1['CA'].get_vector()
        C = res2['C'].get_vector()
        N = res3['N'].get_vector()
        return np.arctan2(N[1] - C[1], N[0] - C[0])  # Simplified for illustration
    return None

def ramachandran_plot(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('Protein', pdb_file)
    
    phi_angles, psi_angles = calculate_phi_psi(structure)

    # Create the Ramachandran plot
    plt.figure(figsize=(8, 8))
    plt.scatter(phi_angles, psi_angles, color = 'red', alpha = 0.6)
    allowed_region = [[-150,120],[-120,120],[-120,150],[-150,150],[-150,120]]
    three_ten_helix_region = [[-55,-20,],[-45,-20],[-55,-30],[-45,-30]]
    plt.fill(*zip(*three_ten_helix_region), color = 'blue', alpha = 0.5, label = "Allowed Region")
    plt.fill(*zip(*allowed_region), color = 'yellow', alpha = 0.5, label = "Allowed Region")
    plt.axhline(0, color = 'k', lw= 0.5)
    plt.axvline(0, color = 'k', lw = 0.5)
    plt.grid(True, linestyle ='--', alpha = 0.7)
    plt.xlim(-300,300)
    plt.ylim(-300,300)
    plt.xlabel("Phi")
    plt.ylabel("Psi")
    plt.title("Mutant G8 1 Domain D -> N")
    plt.legend()

    plt.gca().set_aspect('equal', adjustable = 'box')
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    #ax.yaxis.set_major_locator(ticker.MultipleLocator(40))
    #plt.gca().set_facecolor('white')
    # Display the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    pdb_file_path = 'C:/Users/teemo/Downloads/fibrocystin_and_L_models/human_fc_parts/G81_huMutD1957N.pdb'  # Replace with your PDB file path
    ramachandran_plot(pdb_file_path)
 
