# uiv-language
UIV is a dimensionally-aware data format for scientific programming

> [!NOTE]
> Visual studio code extension works. Format documentation is currently a WIP

Example of the .ut and .uiv formats used to define materials within a library:

<a href="example_derived.ut">Examples_derived.uiv</a><br>
<a href="example_values.uiv">Example_values.uiv</a>

Currently picounits is the only tool with an implementation of .uiv:
Jump to the **release branch** of picounits for more details: 
<a href="https://github.com/wgbowley/PicoUnits/tree/release">picounits/release</a>

## Installation

To install the Unit-Informed Values `(UIV)` language extension for Visual Studio Code:

### Windows

```powershell
Copy-Item -Recurse -Force $PWD "$HOME\.vscode\extensions\uiv-0.0.4"
```

### Linux/MacOs
```bash
cp -r . "$HOME/.vscode/extensions/uiv-0.0.4"
```