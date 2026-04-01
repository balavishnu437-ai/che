# ================================
# DRUG CHIRALITY ANALYZER
# ================================

from rdkit import Chem

# 🔹 Drug Information
drug_name = "Ivabradine"
print(f"\n💊 Drug Name: {drug_name}")

# 🔹 SMILES (with stereochemistry)
smiles = "COc1ccc2c(c1)CCN(C[C@H]3CCc4cc(OC)c(OC)cc4C3)C2"

# -------------------------------
# Function: Check true chirality
# -------------------------------
def is_true_chiral(mol, atom):
    neighbors = atom.GetNeighbors()
    
    envs = []
    for nbr in neighbors:
        # Capture local environment (radius = 2)
        env = Chem.FindAtomEnvironmentOfRadiusN(mol, 2, nbr.GetIdx())
        envs.append(tuple(env))
    
    return len(set(envs)) == 4


# -------------------------------
# Main Analysis Function
# -------------------------------
def analyze_chirality(smiles):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        print("❌ Invalid SMILES")
        return

    # Add hydrogens (important)
    mol = Chem.AddHs(mol)

    # Assign stereochemistry
    Chem.AssignAtomChiralTagsFromStructure(mol)
    Chem.AssignStereochemistry(mol, force=True, cleanIt=True)

    # Find chiral centers
    chiral_centers = Chem.FindMolChiralCenters(
        mol,
        includeUnassigned=True,
        useLegacyImplementation=False
    )

    print("\n🔬 ADVANCED CHIRALITY ANALYSIS")
    print("=" * 50)

    if not chiral_centers:
        print("❌ No chiral centers found.")
        return

    # Loop through chiral centers
    for idx, config in chiral_centers:
        atom = mol.GetAtomWithIdx(idx)

        print(f"\n🧪 Chiral Atom Index: {idx}")
        print(f"Element: {atom.GetSymbol()}")
        print(f"Hybridization: {atom.GetHybridization()}")
        print(f"Configuration: {config}")

        # Neighbor details
        print("🔗 Neighbor Atoms:")
        for nbr in atom.GetNeighbors():
            print(f"  - {nbr.GetSymbol()} (Index {nbr.GetIdx()})")

        # Improved chirality validation
        if is_true_chiral(mol, atom):
            print("✔ True stereogenic center (4 unique substituents)")
        else:
            print("⚠ Symmetry detected (check structure)")

        print("-" * 50)


# -------------------------------
# Run Analysis
# -------------------------------
analyze_chirality(smiles)