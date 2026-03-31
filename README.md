
# Roman Numeral Converter with Automated Testing

## Overview
This project is a Python-based implementation of a **Roman numeral to integer converter**, developed alongside a comprehensive **automated testing suite** using PyUnit (`unittest`).  

It demonstrates core software engineering principles including **algorithm design**, **input validation**, and **test-driven development practices**.



##  Objectives
- Implement a reliable algorithm to convert Roman numerals into integers.
- Apply **automated testing** to verify correctness and handle edge cases.
- Ensure robustness through **input validation and error handling**.



## Features
- Converts standard Roman numerals (I, V, X, L, C, D, M) to integers  
- Supports subtractive notation (e.g., `IV`, `IX`, `MCMXCIV`)  
- Detects invalid inputs:
  - Non-Roman characters (`ABC`)
  - Invalid numeral ordering (`VX`, `IC`)
  - Excessive repetition (`IIII`, `XXXX`)
  - Empty input  
- Includes automated unit tests for validation  



## Technologies Used
- **Python 3**
- **PyUnit (`unittest`)** for automated testing
- **Git & GitHub** for version control



## Testing Approach
The project follows a structured testing strategy inspired by software testing principles:

- **Unit Testing:** Each function is tested independently  
- **Test Case Design Includes:**
  - Single numerals (`I`, `V`, `X`)
  - Composite numerals (`LVIII`, `MCMXCIV`)
  - Subtractive notation (`IV`, `IX`)
  - Invalid inputs and edge cases  

Example:
```python
with self.assertRaises(ValueError):
    RomanConverter.roman_to_int("VX")
````

All tests are automated and can be executed using:

```bash
python -m unittest test_roman_to_int.py
```

---

## How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd roman-numeral-converter
```

### 2. Run the converter

```bash
python roman_to_int.py
```

### 3. Run tests

```bash
python -m unittest test_roman_to_int.py
```

---

## 📂 Project Structure

```
roman-numeral-converter/
│
├── roman_to_int.py        # Core conversion logic
├── test_roman_to_int.py   # Unit tests using PyUnit
├── README.md              # Project documentation
└── .gitignore             # Ignored files
```

---

## Key Learnings

* Applied **automated testing frameworks** to validate functionality
* Strengthened understanding of **edge case handling and input validation**
* Practiced **clean, maintainable code design**
* Gained experience using **Git for version control and collaboration**


---

## 👤 Author

**Lisa Adisa Magada**

