"""
Caveman Mode: Clean and structure the extracted data - FINAL VERSION
"""
import json
import re

def extract_category_mapping():
    """Extract category to subcategory to problem mappings from HTML"""

    with open('playwright_page.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Combine chunks
    chunk_pattern = r'self\.__next_f\.push\(\[1,\"(.*?)\"\]\)'
    chunks = []
    for match in re.finditer(chunk_pattern, html_content, re.DOTALL):
        chunk_content = match.group(1)
        unescaped = chunk_content.replace('\\\"', '"').replace('\\\\', '\\')
        chunks.append(unescaped)

    combined_content = ''.join(chunks)

    # Create mapping: problem_id -> (category_name, subcategory_name)
    problem_mapping = {}

    # Find all category blocks
    category_pattern = r'\{"category_id":"(\d+)","category_name":"([^"]+)","subcategories":\[(.*?)\]\}'

    for match in re.finditer(category_pattern, combined_content, re.DOTALL):
        cat_id = match.group(1)
        cat_name = match.group(2)
        subcategories_str = match.group(3)

        # Parse using improved regex approach
        parse_problems_improved_regex(problem_mapping, cat_name, subcategories_str)

    return problem_mapping

def parse_problems_improved_regex(mapping, category_name, subcategories_str):
    """Parse problems using improved regex that captures subcategory names"""

    # Find subcategory boundaries by looking for subcategory_id
    # Then capture everything until the next subcategory_id or end
    current_subcategory = "General"
    pos = 0

    while pos < len(subcategories_str):
        # Look for subcategory_id
        subcat_match = re.search(r'"subcategory_id":"(\d+)","subcategory_name":"([^"]+)"', subcategories_str[pos:])
        if subcat_match:
            # Update current subcategory
            current_subcategory = subcat_match.group(2)
            # Move position past this match
            pos += subcat_match.end()
        else:
            # No more subcategories, process remaining problems
            break

        # Find all problem IDs until next subcategory
        remaining_text = subcategories_str[pos:]
        next_subcat_pos = remaining_text.find('"subcategory_id"')

        if next_subcat_pos == -1:
            # No more subcategories, process all remaining problems
            problem_section = remaining_text
        else:
            # Process only until next subcategory
            problem_section = remaining_text[:next_subcat_pos]

        # Extract problem IDs from this section
        problem_ids = re.findall(r'"problem_id":"(\d+)"', problem_section)

        # Map each problem ID to current category and subcategory
        for problem_id in problem_ids:
            mapping[problem_id] = {
                'category': category_name,
                'subcategory': current_subcategory
            }

        # Move position for next iteration
        if next_subcat_pos == -1:
            break
        pos += next_subcat_pos

def clean_and_structure_data():
    """Convert raw data to clean, usable format"""

    # Load existing data
    with open('problems_fixed.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)

    # Extract category mapping
    print("Extracting category structure...")
    problem_mapping = extract_category_mapping()
    print(f"Mapped {len(problem_mapping)} problems to categories")

    # Clean and structure each problem
    clean_problems = []

    for i, problem in enumerate(problems, start=1):
        problem_id = problem.get('problem_id', '')

        # Get category info from mapping
        category_info = problem_mapping.get(problem_id, {})
        topic = category_info.get('category', 'General')
        subtopic = category_info.get('subcategory', problem.get('difficulty', 'Medium'))

        # Extract LeetCode link if available
        leetcode_link = problem.get('leetcode', '')
        if leetcode_link == '$undefined' or not leetcode_link:
            # Fallback to plus link if no LeetCode link
            plus_link = problem.get('plus', '')
            if plus_link and plus_link != '$undefined':
                leetcode_link = f"https://takeuforward.org{plus_link}"
            else:
                leetcode_link = ''

        clean_problem = {
            "id": i,
            "topic": topic,
            "subtopic": subtopic,
            "name": problem.get('problem_name', '').strip(),
            "link": leetcode_link,
            "status": "not_started"
        }

        clean_problems.append(clean_problem)

    # Save clean data
    with open('problems.json', 'w', encoding='utf-8') as f:
        json.dump(clean_problems, f, indent=2, ensure_ascii=False)

    print(f"Cleaned and structured {len(clean_problems)} problems")
    print(f"Saved to problems.json")

    # Show sample
    print(f"\nSample problem:")
    print(json.dumps(clean_problems[0], indent=2))

    # Show statistics
    topics = {}
    for p in clean_problems:
        topic = p['topic']
        topics[topic] = topics.get(topic, 0) + 1

    print(f"\nTopics distribution:")
    for topic, count in sorted(topics.items(), key=lambda x: x[1], reverse=True):
        print(f"  {topic}: {count}")

    return clean_problems

if __name__ == "__main__":
    clean_and_structure_data()