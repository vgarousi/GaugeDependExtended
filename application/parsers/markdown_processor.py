import markdown
import re


# Helper method that takes in raw markdown string, sanitises it and returns HTML string
def process_markdown(markdown_string):
    # Remove tags
    markdown_string = re.sub(r'\n.*Tags:.*\n', '\n', markdown_string)

    # Remove lines that are just dots, used in some sample files
    markdown_string = re.sub(r"\.\.\.\.[^*]+\.\.\.\.", '', markdown_string)

    # Replace variables in steps with $Variable$
    markdown_string = re.sub(r"\"[\S\s]*?\"", "$Variable$", markdown_string)
    markdown_string = re.sub(r"<[\S\s]*?>", "$Variable$", markdown_string)

    # Properly format dividers, used for markdown headings, some files have spaces in these lines
    # which causes problems with converting to html
    markdown_string = re.sub(r"=====.*", "=====", markdown_string)
    markdown_string = re.sub(r"-----.*", "-----", markdown_string)

    # Remove comments
    markdown_string = re.sub(r'\n.*//.*\n', '\n', markdown_string)
    markdown_string = re.sub(r'// .*', '', markdown_string)
    markdown_string = re.sub(r'\n.*\\\*.*\n', '', markdown_string)

    # ?
    markdown_string = re.sub(r':', ' ', markdown_string)

    # Remove markdown tables.
    markdown_string = re.sub(r"\|.*\|", "", markdown_string);

    # Remove any lines that are contain just text and are not headers
    replace_count = -1
    while replace_count != 0:
        markdown_string, replace_count = re.subn(r"^[A-Za-z ]+\n[^=]", replace, markdown_string, flags=re.MULTILINE)

    # Convert processed markdown to HTML string.
    html = markdown.markdown(markdown_string)
    return html

# Helper function to replace lines with just text, regex will match that line and the next line, should not be removed
# if the next line starts with * i.e. the next line is a step.
def replace(match_obj):
    if match_obj.group(0).endswith("*"):
        return "*"
    else:
        return ""
