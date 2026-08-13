<!-- 
Color palette: 
#fb8500 -> vibrant, fiery orange 
#219ebc -> cool, mid-tone cerulean blue 

Not much to say really. It's my first domain-specific language, hopefully 
I defined it well enough and added appropriate syntax highlighting. 
Nevertheless, I think it's a very good domain-specific language. 

Hope you think the same,
— William Bowley, 14th of August, 2026

P.S: Thanks for downloading the UnitValues repository `▽`ʃ♡
-->


<p align="center">
  <img src="https://raw.githubusercontent.com/Bowley-Systems/UnitValues/refs/heads/main/media/logo.png" alt="UnitValues" style="max-width:600px;">
</p>
<p align="center">A typed language for numerical quantities.</p>

# Overview
 
![License](https://img.shields.io/badge/License-MIT-219ebc?style=flat-square)
![DSL](https://img.shields.io/badge/Domain-DSL-fb8500?style=flat-square&labelColor)
![Status](https://img.shields.io/badge/Status-Active-219EBC?style=flat-square)

UnitValues is a set of domain-specific typed languages for numerical quantities. The set consists of two languages:
- Unit Types (`.ut`) for defining units from fundamental dimensions.
- Unit Informed Values (`.uiv`) import Unit Types and uses dimensional construction to encode numerical quantities.

> [!IMPORTANT]
> Language specification for `.ut` and `.uiv` can be found within [docs/language.pdf](./docs/language.pdf)

## Example

### .ut
```ut
# Example Units - Derived from Fundamental Dimensions (kg, m, s, A, etc.)
[version]
format: 0.1.0
 
[units]
# name: unit
ρ: kg/m^3                             # Defines the unit for pressure
V: kg*m^2*s^-3*A^-1                   # Defines the unit for voltage
```

> [!NOTE]
> The fundamental unit semantics and prefixes `(kg, m, s, A, etc.)` & `(u, m, k, M, etc.)` is defined by the runtime environment.

### .uiv

```
[version]
format: 0.1.0
unit_frame: units.ut

[model]
# name: value prefix(unit)
num_samples: 100                        # Implicitly dimensionless
sample_size: 10         (∅)             # Explicitly dimensionless
output_energy: 1.0      (kg*m^2*s^-2)   # Defines unit via construction
output_signal: 5.0      (V)             # Defined unit `V` for voltage
inlet_pressure: 101     k(ρ)            # Defined unit `ρ` for pressure with kilo prefix
```

## Implementation

UnitValues is implemented by [PicoUnits](https://github.com/Bowley-Systems/PicoUnits).  
You can try the language today by installing PicoUnits:

```bash
pip install PicoUnits
```

## Local Installation

To install the UnitValues extension locally for Visual Studio Code:

### Windows

```powershell
npx @vscode/vsce package
code --install-extension .\UnitValues-0.0.1.vsix --force
```

### MacOS/Linux

```bash
npx @vscode/vsce package
code --install-extension ./uiv-0.0.1.vsix --force
```

## Documentation

All internal documentation can be found within this repo's [issues](https://github.com/Bowley-Systems/UnitValues/issues).

