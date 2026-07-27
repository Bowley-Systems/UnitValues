<!-- 
Color palette: 
#006d77ff, 
#d92c2aff 
-->

# Overview
 
![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![DSL](https://img.shields.io/badge/Domain-DSL-006d77?style=flat-square&labelColor)

Unit-Informed Values (`.uiv`) and Unit Types (`.ut`) are domain-specific languages for computational engineering. Unlike general-purpose formats, 
`.uiv` and `.ut` allow users to encode values with dimensional constraints.

### Features

> [!important]
> - Dimensionally aware formats with derived units via the `.ut` format.
> - Value:unit pairs within the `.uiv` format.
> - Support for complex numbers, strings, integers, floats, arrays, and column-wise arrays.

## How do `.uiv` and `.ut` work?
 
`.ut` (Unit Types) encodes custom base units for your system, and `.uiv` (Unit-Informed Values) encodes value:unit pairs.

### `.ut`
 
 
```
# Coilgun Units - Derived from Base Dimensions (kg, m, s, A, etc.)
[version]
format: 0.1.0
 
[units]
ρ: kg/m^3
V: kg*m^2*s^-3*A^-1
```
 
### `.uiv`
 
All `value:prefix(unit)` pairs exist in the form value `prefix(unit)`, for example:
 
```
[version]
format: 0.1.0
unit_frame: units.ut
 
[notes]
# Analytical model for a multi-stage coil-gun
# Models electrical, magnetic and motional dynamics
 
[model]
number_stages: 10 (∅)    # Explicitly dimensionless
 
# Millimeter -> prefix `m` and unit `m` hence prefix(unit), m(m)
stage_gap: 10 m(m)
 
# Value without prefix (volts - empty prefix)
voltage: 18 (V)         # Equivalent to ""(V)
current_limit: 40 (A) 
time_steps: 50 u(s)
atmospheric_density: 1.225 (ρ)
```


## Quick Start

Currently, PicoUnits is the only tool with an implementation of UIV: [`picounits`](https://github.com/wgbowley/PicoUnits).
A standard introduction example is available in [`example/`](https://github.com/wgbowley/UIV/tree/main/02_example).

## Local Installation

To install the Unit-Informed Values (`UIV`) language extension locally for Visual Studio Code:

### Windows

```powershell
Copy-Item -Recurse -Force $PWD "$HOME\.vscode\extensions\uiv-0.0.4"
```

### Linux/MacOs
```bash
cp -r . "$HOME/.vscode/extensions/uiv-0.0.4"
```