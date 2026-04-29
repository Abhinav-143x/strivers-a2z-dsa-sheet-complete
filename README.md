# Striver's A2Z DSA Sheet - Complete Extraction

A complete extraction and organization of Striver's A2Z DSA Sheet from takeuforward.org, featuring all 474 problems with official website formatting.

## 📊 Overview

This project contains a complete extraction of the DSA (Data Structures and Algorithms) problems from Striver's A2Z DSA Sheet, organized in the official website format with progress tracking capabilities.

### 📈 Statistics

- **Total Problems**: 474
- **Categories**: 18
- **Subcategories**: 62
- **Difficulty Breakdown**:
  - Easy: 152 problems
  - Medium: 185 problems
  - Hard: 135 problems

## 🚀 Features

- ✅ **Complete Problem Extraction**: All 474 problems extracted (previously missing 46 problems due to script chunk splitting)
- ✅ **Official Format**: Matches the official website structure with progress tracking
- ✅ **Comprehensive Data**: Includes problem names, difficulty, article links, YouTube tutorials, LeetCode links, and practice resources
- ✅ **Progress Tracking**: Built-in progress tracking with 0 / X format for categories and subcategories
- ✅ **Interactive Tables**: Markdown tables with status checkboxes, resource links, and action buttons
- ✅ **Organized Structure**: Problems organized by category and difficulty-based subcategories

## 📁 Project Structure

```
.
├── DSA_SHEET_OFFICIAL_FORMAT.md    # Main DSA sheet in official format
├── DSA_SHEET_COMPLETE.md           # Complete problem list with all details
├── problems_fixed.json             # All 474 problems with full metadata
├── categories_fixed.json           # 18 main categories
├── subcategories_fixed.json        # 62 subcategories
├── playwright_page.html           # Original scraped HTML content
├── extract_problems_fixed.py      # Fixed extraction script (handles split data)
├── create_official_format_simple.py # Script to generate official format
└── README.md                      # This file
```

## 🛠️ Technical Details

### Extraction Process

The project uses a sophisticated extraction approach to handle the complex Next.js rendering:

1. **Script Chunk Combination**: The website splits problem data across multiple Next.js script chunks using `self.__next_f.push([1,"..."])` format
2. **Data Reconstruction**: Combines 57+ script chunks to reconstruct complete problem objects
3. **Split Problem Handling**: Captures problems that were cut mid-stream and continued in subsequent chunks
4. **Structure Parsing**: Extracts hierarchical category → subcategory → problem relationships

### Key Challenges Solved

- **Split Problem Data**: Problems like "Maximum Xor with an element from an array" (ID: 1025) were being cut across script boundaries
- **JSON Parsing**: Handles escaped JSON strings within Next.js chunks
- **Category Structure**: Reconstructs the complete hierarchical organization

## 📝 Usage

### View the DSA Sheet

Simply open `DSA_SHEET_OFFICIAL_FORMAT.md` in any Markdown viewer or GitHub to see the complete DSA sheet with progress tracking.

### Extract Data Yourself

```bash
# Install dependencies
pip install beautifulsoup4 requests

# Run the extraction script
python extract_problems_fixed.py

# Generate official format
python create_official_format_simple.py
```

### Data Files

- **problems_fixed.json**: Complete problem data with all metadata
- **categories_fixed.json**: Category information and IDs
- **subcategories_fixed.json**: Subcategory structure

## 🎯 Categories Included

1. Binary Search [1D, 2D Arrays, Search Space]
2. Binary Search Trees [Concept and Problems]
3. Binary Trees [Traversals, Medium and Hard Problems]
4. Bit Manipulation [Concepts & Problems]
5. Dynamic Programming [Patterns and Problems]
6. Graphs [Concepts & Problems]
7. Greedy Algorithms [Easy, Medium/Hard]
8. Heaps [Learning, Medium, Hard Problems]
9. Learn Important Sorting Techniques
10. Learn LinkedList [Single LL, Double LL, Medium, Hard Problems]
11. Learn the basics
12. Recursion [PatternWise]
13. Sliding Window & Two Pointer Combined Problems
14. Solve Problems on Arrays [Easy -> Medium -> Hard]
15. Stack and Queues [Learning, Pre-In-Post-fix, Monotonic Stack, Implementation]
16. Strings
17. Strings [Basic and Medium]
18. Tries

## 📊 Sample Format

```markdown
## Binary Search [1D, 2D Arrays, Search Space]
0 / 27

### Easy Problems
0 / 5

| Status | Problem | Plus Resource | Practice | Note | Revision | Difficulty |
|--------|---------|---------------|----------|------|----------|------------|
| ⬜ | **Two Sum** | Solve | Editorial | Add Note | --- | Easy |
| ⬜ | **Find out how many times the array is rotated** | Solve | Editorial | Add Note | --- | Easy |
```

## 🤝 Contributing

This is a static extraction project. If you find issues with the data or want to improve the extraction scripts, feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project contains extracted data from takeuforward.org. The original content belongs to their respective owners. This extraction is for educational purposes.

## 🙏 Acknowledgments

- **Striver (Raj Vikramaditya)** - For creating the comprehensive A2Z DSA Sheet
- **takeuforward.org** - For providing excellent DSA learning resources
- **Next.js** - The framework that powers the original website

## 📞 Contact

For issues or questions about this extraction project, please open an issue on GitHub.

---

**Note**: This project is for educational purposes. For the most up-to-date version of the DSA sheet, please visit [takeuforward.org](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z).