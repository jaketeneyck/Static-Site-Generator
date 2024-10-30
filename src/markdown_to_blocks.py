

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