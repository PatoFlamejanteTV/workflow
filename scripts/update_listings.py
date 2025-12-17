import os

def update_readme_index(root_dir="."):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .git directory
        if ".git" in dirpath:
            continue

        readme_path = os.path.join(dirpath, "README.md")

        # Only update if README.md exists? Or create it?
        # The prompt says "Update all folders readme", which implies they might exist or we should ensure they have the listing.
        # But for now, let's only update existing ones, or create if it's the root (which exists).

        if not os.path.exists(readme_path):
             # Skipping folders without README for now to avoid cluttering unless instructed.
             # But wait, if there are NO other folders, this loop only runs for root.
             continue

        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Determine the content to add
        # We want to list files and subdirectories

        listing = []

        # List directories
        for d in sorted(dirnames):
            if d.startswith("."): continue
            listing.append(f"- [{d}/]({d}/)")

        # List files
        for f in sorted(filenames):
            if f.startswith("."): continue
            if f == "README.md": continue # Don't list self? Or maybe yes?
            listing.append(f"- [{f}]({f})")

        if not listing:
            continue

        listing_md = "\n".join(listing)
        header = "## Index\n\n"

        new_section = f"{header}{listing_md}\n"

        # Check if Index section exists
        if "## Index" in content:
            # Replace existing Index section
            # This is tricky without a proper parser, but let's assume it's at the end or marked?
            # Or we can just append it if not present, and update if present.

            # Simple approach: If "## Index" is present, we try to find where it starts and ends.
            # Assuming it ends at the next "## " or end of file.

            parts = content.split("## Index")
            pre_index = parts[0]
            post_index = parts[1]

            # Find end of index section in post_index
            # It ends at the next "## " or "# " or end of string
            import re
            match = re.search(r"(\n#+\s)", post_index)
            if match:
                end_pos = match.start()
                rest_of_file = post_index[end_pos:]
                new_content = pre_index + new_section + rest_of_file
            else:
                # End of file
                new_content = pre_index + new_section
        else:
            # Append to end
            new_content = content + "\n\n" + new_section

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Updated {readme_path}")

if __name__ == "__main__":
    update_readme_index()
