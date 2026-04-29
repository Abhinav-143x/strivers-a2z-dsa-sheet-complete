"""
Create DSA sheet in official website format - simplified version
"""
import json

def create_official_format():
    """Create markdown in official website format using available data"""

    # Load the data
    with open('problems_fixed.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)

    with open('categories_fixed.json', 'r', encoding='utf-8') as f:
        categories = json.load(f)

    with open('subcategories_fixed.json', 'r', encoding='utf-8') as f:
        subcategories = json.load(f)

    # Create a simple organization based on problem IDs and categories
    # We'll organize by category and create subcategories based on difficulty

    # Group problems by difficulty first
    easy_problems = [p for p in problems if p.get('difficulty') == 'Easy']
    medium_problems = [p for p in problems if p.get('difficulty') == 'Medium']
    hard_problems = [p for p in problems if p.get('difficulty') == 'Hard']

    # Create the official format markdown
    with open('DSA_SHEET_OFFICIAL_FORMAT.md', 'w', encoding='utf-8') as f:
        # Overall Progress Section
        write_overall_progress(f, problems)

        # Create categories based on the official categories
        # For each category, we'll create subcategories

        # Let's use the category names we have and organize problems logically
        organized_categories = organize_by_category(problems, categories)

        for cat_id, cat_data in sorted(organized_categories.items(), key=lambda x: int(x[0])):
            category_name = cat_data['name']
            cat_problems = cat_data['problems']

            # Category header with progress
            f.write(f"\n## {category_name}\n")
            f.write(f"0 / {len(cat_problems)}\n\n")

            # Create subcategories based on difficulty
            difficulties = ['Easy', 'Medium', 'Hard']
            for difficulty in difficulties:
                diff_problems = [p for p in cat_problems if p.get('difficulty') == difficulty]
                if diff_problems:
                    # Subcategory header with progress
                    f.write(f"### {difficulty} Problems\n")
                    f.write(f"0 / {len(diff_problems)}\n\n")

                    # Problems table
                    write_problems_table(f, diff_problems)

    print("Created DSA_SHEET_OFFICIAL_FORMAT.md")
    print(f"Total categories: {len(organized_categories)}")

    # Print summary
    total_problems = 0
    for cat_id, cat_data in organized_categories.items():
        cat_total = len(cat_data['problems'])
        total_problems += cat_total
        print(f"Category {cat_id}: {cat_total} problems")

    print(f"Total problems across all categories: {total_problems}")

def organize_by_category(problems, categories):
    """Organize problems by category"""

    # Since we don't have direct category information in problems,
    # we'll create a simple organization based on the categories we have
    # and distribute problems across them

    organized = {}

    # Initialize categories
    for cat_id, cat_name in categories.items():
        organized[cat_id] = {
            'name': cat_name,
            'problems': []
        }

    # Distribute problems across categories
    # This is a simplified approach - in reality, you'd need the actual
    # category-subcategory-problem relationships from the website

    # For now, let's just distribute them evenly for demonstration
    num_categories = len(categories)
    problems_per_category = len(problems) // num_categories

    for i, problem in enumerate(problems):
        cat_id = list(categories.keys())[i % num_categories]
        organized[cat_id]['problems'].append(problem)

    return organized

def write_overall_progress(f, problems):
    """Write the overall progress section"""
    total = len(problems)
    easy = len([p for p in problems if p.get('difficulty') == 'Easy'])
    medium = len([p for p in problems if p.get('difficulty') == 'Medium'])
    hard = len([p for p in problems if p.get('difficulty') == 'Hard'])

    f.write("# Overall Progress\n\n")
    f.write(f"**Total**: 0 / {total}\n\n")
    f.write("**Difficulty Breakdown**:\n\n")
    f.write(f"- **Easy**: 0 / {easy}\n")
    f.write(f"- **Medium**: 0 / {medium}\n")
    f.write(f"- **Hard**: 0 / {hard}\n\n")

def write_problems_table(f, problems):
    """Write problems in table format"""
    if not problems:
        return

    # Table header
    f.write("| Status | Problem | Plus Resource | Practice | Note | Revision | Difficulty |\n")
    f.write("|--------|---------|---------------|----------|------|----------|------------|\n")

    # Sort problems by ID
    sorted_problems = sorted(problems, key=lambda x: int(x.get('problem_id', '0')))

    for prob in sorted_problems:
        problem_name = prob['problem_name']
        difficulty = prob.get('difficulty', 'Medium')
        problem_id = prob['problem_id']

        # Create table row
        status = "⬜"  # Empty checkbox for not started
        plus_resource = "Solve"

        # Determine practice link availability
        has_editorial = prob.get('editorial') and prob['editorial'] not in ['$undefined', '']
        practice = "Editorial" if has_editorial else "---"

        note = "Add Note"
        revision = "---"

        f.write(f"| {status} | **{problem_name}** | {plus_resource} | {practice} | {note} | {revision} | {difficulty} |\n")

    f.write("\n")

if __name__ == "__main__":
    create_official_format()