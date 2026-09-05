<!-- 
Color palette:
#219EBC -> cool, mid-tone cerulean blue 
#ffb703 -> warm, golden-amber yellow 

Not much to say really. It's my first domain-specific language, hopefully 
I defined it well enough and added appropriate syntax highlighting. 
Nevertheless, I think it's a very good domain-specific language. 

Hope you think the same,
— William Bowley, 14th of August, 2026

P.S: Thanks for downloading the UnitValues repository `▽`ʃ♡
-->


<p align="center">
  <img 
    src="https://raw.githubusercontent.com/Bowley-Systems/UnitValues/refs/heads/main/media/logo.png" 
    alt="UnitValues" 
    width="100%" 
    style="max-width:100%; display:block;"
  >
</p>

<p align="center">
    <strong>Define the type. Define the quality.</strong><br>
    Make numerical meaning explicit before computation begins.
</p>

### Overview
![Version](https://img.shields.io/badge/Version-0.1.2-ffb703?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-219EBC?style=flat-square)
![DSL](https://img.shields.io/badge/Domain-DSL-ffb703?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-219ebc?style=flat-square)

UnitValues is a set of two domain-specific languages that encode dimensional quantities as types. The first language, `.ut`, defines units from fundamental dimensions. The second, `.uiv`, imports `.ut` and uses those constructs to encode numerical quantities across integers, floats, arrays, and complex numbers.

Language specification for `.ut` and `.uiv` can be found within [language.pdf](./docs/language.pdf)

#### Implementation

UnitValues is implemented by [PicoUnits](https://github.com/Bowley-Systems/PicoUnits).  
You can try the language today by installing PicoUnits:

```bash
pip install PicoUnits
```

---

### Example

Both are dimensionally aware formats: `.ut` defines custom units, while `.uiv` encodes quantities as:

```
attribute: value prefix(unit)
```

#### .ut

```ut
# Example Units - Derived from Fundamental Dimensions (kg, m, s, A, etc.)
[version]
format: 0.1.0
 
[units]
# name: unit
p: kg*m^-1*s^-2                       # Defines the unit for pressure (Pascal)
V: kg*m^2*s^-3*A^-1                   # Defines the unit for voltage
```

> The fundamental unit semantics and prefixes `(kg, m, s, A, etc.)` & `(u, m, k, M, etc.)` is defined by the runtime environment.

#### .uiv

```uiv
[version]
format: 0.1.2
unit_frame: units.ut

[model]
# name: value prefix(unit)
num_samples: 100                        # Implicitly dimensionless
sample_size: 10         (∅)             # Explicitly dimensionless
output_energy: 1.0      (kg*m^2*s^-2)   # Defines unit via construction
output_signal: 5.0      (V)             # Defined unit `V` for voltage
inlet_pressure: 101     k(p)            # Defined unit `p` for pressure with kilo prefix
```

---

### Local Installation

To install the extension locally for Visual Studio Code:

> From the Marketplace: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=wgbowley.UnitValues)

---

### Manual Installation

To install the UnitValues extension manually for Visual Studio Code:

#### Windows

```powershell
npx @vscode/vsce package
code --install-extension .\UnitValues-0.0.3.vsix --force
```

#### MacOS/Linux

```bash
npx @vscode/vsce package
code --install-extension ./uiv-0.0.3.vsix --force
```

---

### Documentation

For internal documentation, credits, and contributors, see [docs](./docs/README.md).

---
