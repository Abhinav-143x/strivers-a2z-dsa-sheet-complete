"""
Fixed extraction script that handles split problem data across script chunks
"""
import re
import json

def extract_problems_from_html(html_file='playwright_page.html'):
    """Extract problem data from the HTML file, handling split data"""
    print(f"Reading {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, let's combine the split script chunks
    # Look for the pattern where data is split: [1,"..."]
    # We need to reconstruct the complete JSON

    # Find all the script content that contains problem data
    # The data is in self.__next_f.push([1,"..."]) format

    # Extract all the pushed content chunks
    chunk_pattern = r'self\.__next_f\.push\(\[1,"(.*?)"\]\)'
    chunks = []
    for match in re.finditer(chunk_pattern, content, re.DOTALL):
        chunk_content = match.group(1)
        # Unescape the content
        unescaped = chunk_content.replace('\\\"', '"').replace('\\\\', '\\')
        chunks.append(unescaped)

    print(f"Found {len(chunks)} data chunks")

    # Combine all chunks
    combined_content = ''.join(chunks)

    # Now extract problems from the combined content
    problem_pattern = r'problem_id":"(\d+)","problem_name":"([^"]+)","article":"([^"]*)","youtube":"([^"]*)","leetcode":"([^"]*)","plus":"([^"]*)","editorial":"([^"]*)","link":"([^"]*)","difficulty":"([^"]+)"'

    problems = []
    seen_ids = set()

    for match in re.finditer(problem_pattern, combined_content):
        problem_id = match.group(1)
        if problem_id not in seen_ids:
            seen_ids.add(problem_id)
            problem = {
                'problem_id': match.group(1),
                'problem_name': match.group(2),
                'article': match.group(3),
                'youtube': match.group(4),
                'leetcode': match.group(5),
                'plus': match.group(6),
                'editorial': match.group(7),
                'link': match.group(8),
                'difficulty': match.group(9)
            }
            problems.append(problem)

    print(f"Extracted {len(problems)} unique problems")

    # Extract categories
    category_pattern = r'category_id":"(\d+)","category_name":"([^"]+)"'
    categories = {}
    for match in re.finditer(category_pattern, combined_content):
        cat_id = match.group(1)
        cat_name = match.group(2)
        if cat_id not in categories:
            categories[cat_id] = cat_name

    print(f"Extracted {len(categories)} categories")

    # Extract subcategories
    subcategory_pattern = r'subcategory_id":"(\d+)","subcategory_name":"([^"]+)"'
    subcategories = {}
    for match in re.finditer(subcategory_pattern, combined_content):
        sub_id = match.group(1)
        sub_name = match.group(2)
        if sub_id not in subcategories:
            subcategories[sub_id] = sub_name

    print(f"Extracted {len(subcategories)} subcategories")

    # Save to JSON
    with open('problems_fixed.json', 'w', encoding='utf-8') as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)
    print("Saved to problems_fixed.json")

    with open('categories_fixed.json', 'w', encoding='utf-8') as f:
        json.dump(categories, f, indent=2, ensure_ascii=False)
    print("Saved to categories_fixed.json")

    with open('subcategories_fixed.json', 'w', encoding='utf-8') as f:
        json.dump(subcategories, f, indent=2, ensure_ascii=False)
    print("Saved to subcategories_fixed.json")

    # Create markdown
    create_markdown(problems, categories, subcategories)

    return problems, categories, subcategories

def create_markdown(problems, categories, subcategories):
    """Create a comprehensive markdown file"""
    with open('DSA_SHEET_FIXED.md', 'w', encoding='utf-8') as f:
        f.write("# Striver's A2Z DSA Sheet - Complete Problem List\n\n")
        f.write(f"**Total Problems**: {len(problems)}\n")
        f.write(f"**Total Categories**: {len(categories)}\n")
        f.write(f"**Total Subcategories**: {len(subcategories)}\n\n")

        # Count by difficulty
        easy = len([p for p in problems if p.get('difficulty') == 'Easy'])
        medium = len([p for p in problems if p.get('difficulty') == 'Medium'])
        hard = len([p for p in problems if p.get('difficulty') == 'Hard'])

        f.write("## Difficulty Breakdown\n\n")
        f.write(f"| Difficulty | Count |\n")
        f.write(f"|------------|-------|\n")
        f.write(f"| Easy | {easy} |\n")
        f.write(f"| Medium | {medium} |\n")
        f.write(f"| Hard | {hard} |\n\n")

        # List categories
        f.write("## Categories\n\n")
        for cat_id, cat_name in sorted(categories.items(), key=lambda x: int(x[0])):
            f.write(f"- {cat_name} (ID: {cat_id})\n")
        f.write("\n")

        # All problems
        f.write("## All Problems\n\n")

        # Sort by problem_id
        problems_sorted = sorted(problems, key=lambda x: int(x.get('problem_id', '0')))

        for i, prob in enumerate(problems_sorted, 1):
            f.write(f"### {i}. {prob['problem_name']}\n\n")
            f.write(f"- **Problem ID**: {prob['problem_id']}\n")
            f.write(f"- **Difficulty**: {prob['difficulty']}\n")

            if prob.get('article') and prob['article'] not in ['$undefined', '']:
                f.write(f"- **Article**: [{prob['article']}]({prob['article']})\n")

            if prob.get('youtube') and prob['youtube'] not in ['$undefined', '']:
                f.write(f"- **YouTube**: [{prob['youtube']}]({prob['youtube']})\n")

            if prob.get('leetcode') and prob['leetcode'] not in ['$undefined', '']:
                f.write(f"- **LeetCode**: [{prob['leetcode']}]({prob['leetcode']})\n")

            if prob.get('plus') and prob['plus'] not in ['$undefined', '']:
                f.write(f"- **Practice**: https://takeuforward.org{prob['plus']}\n")

            f.write("\n---\n\n")

    print("Created DSA_SHEET_FIXED.md")

if __name__ == "__main__":
    extract_problems_from_html()