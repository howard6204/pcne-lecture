"""Convert Marp .md to Reveal.js markdown format."""
import re
import sys

def convert(src: str) -> str:
    # Remove YAML frontmatter block (--- ... ---)
    src = re.sub(r'^---\n.*?^---\n', '', src, count=1, flags=re.DOTALL | re.MULTILINE)

    lines = src.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Convert _class directives
        m = re.match(r'^<!-- _class: (.+?) -->', line)
        if m:
            out.append(f'<!-- .slide: class="{m.group(1)}" -->')
            i += 1
            continue

        # Remove _footer and _paginate directives
        if re.match(r'^<!-- _footer:.*?-->', line) or re.match(r'^<!-- _paginate:.*?-->', line):
            i += 1
            continue

        # Convert multiline HTML comment speaker notes
        if line.strip().startswith('<!--') and '-->' not in line:
            note_lines = []
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                note_lines.append(lines[i])
                i += 1
            i += 1  # skip closing -->
            # strip trailing empty lines from note
            while note_lines and not note_lines[-1].strip():
                note_lines.pop()
            if note_lines:
                out.append('Note:')
                out.extend(note_lines)
            continue

        # Convert inline HTML comment speaker notes (single line)
        m = re.match(r'^<!--\n?(.*?)\n?-->$', line, re.DOTALL)
        if m:
            content = m.group(1).strip()
            if content:
                out.append('Note:')
                out.append(content)
            i += 1
            continue

        out.append(line)
        i += 1

    return '\n'.join(out)


if __name__ == '__main__':
    src_path = sys.argv[1] if len(sys.argv) > 1 else \
        r'C:\Users\USER\OneDrive\Claude_Workspace\06_行政與出差\簡報\PCNE簡介\PCNE-DRP概論簡報.md'
    dst_path = sys.argv[2] if len(sys.argv) > 2 else \
        r'C:\Users\USER\OneDrive\Claude_Workspace\06_行政與出差\簡報\PCNE簡介\pcne-web\pcne-slides.md'

    with open(src_path, encoding='utf-8') as f:
        src = f.read()

    result = convert(src)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f'Done → {dst_path}')
