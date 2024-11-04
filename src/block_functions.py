import re

def markdown_to_blocks(markdown):
    blocks = []
    strings = markdown.split("\n\n")

    for s in strings:
        if s != None and s != "" and s != "\n":
            lines = s.splitlines()
            clean = []
            for l in lines:
                clean.append(l.strip())

            blocks.append("\n".join(clean))

    return blocks


def block_to_block_type(block):
    if re.search(r"\A\#{1,6}\ ", block) != None: # headings
        return "HEADING"
    elif re.search(r"\A```.*```", block, re.DOTALL) != None: # code
        return "CODE"
    elif re.search(r"\A\>.*", block, re.MULTILINE) != None: # quotes
        return "QUOTE"
    elif is_unordered_list(block): # unordered list
        return "UNORDERED_LIST"
    elif is_ordered_list(block):
        return "ORDERED_LIST"
    else:
        return "PARAGRAPH"
    
def is_unordered_list(block):
    lines = block.splitlines()
    for line in lines:
        line = line.lstrip()  # Remove leading whitespace
        if not re.match(r"^(\*|-)\s", line):
            return False
    return True

def is_ordered_list(block):
    lines = block.splitlines()
    expected_number = 1
    for line in lines:
        line = line.lstrip()
        match = re.match(r"^(\d+)\. ", line)
        if match:
            number = int(match.group(1))
            if number != expected_number:
                return False
            expected_number += 1
        else:
            return False
    return True