"""
Filename: 02_introduction.py

Description:
    Introduces the program interface for
    unit types and unit informed values 
    via picounits implementation
"""

from pathlib import Path
from picounits import Parser, length

# Finds the paths with respect to this file
BASE_DIR = Path(__file__).parent

# Creates the path to the derived units and unit informed values
derived_path = BASE_DIR / "00_derived.ut"
material_path = BASE_DIR / "01_values.uiv"

# Opens the material file with derived units & prints attribute tree
material = Parser.open(material_path, derived_path)
material.info("material")

# Example usage of the attribute tree to compute mass
print("\n", "\n")
print("-" * 20, " Example Usage ", "-" * 20)

density = material.NdFeB.physical.density
print(f"NdFeB Density: {density}")

volume = 10 * length **3
print(f"Object with volume: {volume} @ density: {density} = {volume * density}")
print("-" * 57)
