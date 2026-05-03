![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk Maya](https://img.shields.io/badge/Autodesk%20Maya-37A5CC?style=for-the-badge)

# MaterialCheck Tool for Autodesk Maya

---

## Overview

**MaterialCheck** is a lightweight utility tool for Autodesk Maya designed to help production teams validate and manage material naming between a source file and the latest working file.

This tool is especially useful for maintaining consistency during asset development, lookdev checks, and scene assembly workflows where material naming accuracy is important for downstream tasks.

It provides a simple workflow to:

- compare material naming between files
- verify naming consistency
- import and export material lists for checking and review

This tool may be especially helpful for:

- **Modelers**
- **Riggers**
- **Assembly / Scene Build teams**

---

## Features

- Check material names from a source file against the latest file
- Validate material naming consistency in Maya scenes
- Import material lists into Maya for comparison or review
- Export material lists from Maya for external checking
- Simple drag-and-drop installation workflow
- Lightweight utility for pipeline support and scene validation

---

## Workflow Concept

### Material Name Validation

The main purpose of this tool is to help users compare material naming between files and ensure that naming remains clean and consistent throughout production.

This is useful when:

- transferring assets between departments
- checking final scene readiness
- validating lookdev or assembly files
- catching naming mismatches before publish or handoff

---

### Import / Export Material List Support

The tool also supports importing and exporting material lists.

This allows users to:

- store material name data externally
- review naming outside the scene
- compare previous and current material states
- streamline material tracking between source and latest versions

---

## Installation

1. Open **Autodesk Maya**
2. Drag and drop `MaterialCheck_Install.mel` into the Maya viewport
3. A shelf icon will be created automatically
4. Click the icon to launch the tool

---

## Usage

1. Launch the tool from the Maya shelf
2. Load or define the source file / source material reference
3. Compare the material names against the current or latest file
4. Review mismatched or missing material naming
5. Import or export the material list when needed

---

## Use Cases

This tool can be used in several production scenarios, such as:

- checking whether material naming matches a source asset
- validating material setup before publish
- reviewing naming consistency after scene updates
- exporting material lists for documentation or handoff
- importing approved material lists back into Maya for verification

---

## Notes

- This tool is intended as a utility support tool for Maya workflows
- It is designed to assist naming validation rather than replace lookdev or shader management processes
- Final validation should still follow your studio or project pipeline requirements

---

## Feedback & Contributions

This is an evolving workflow utility.

Any further feedback, suggestions, or enhancement ideas are welcome.

If you find issues or would like to improve the workflow, feel free to update the tool or extend the README based on your production needs.

---

## License

Provided **as-is** for personal, educational, or internal production workflow use.
