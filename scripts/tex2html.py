#!/usr/bin/env python3
"""Convert the LaTeX resume into an HTML fragment for the /cv/ page.

Handles the small command set resume.tex uses: \\section*, itemize, \\item,
\\resumeItem{label}{text}, \\resumeSubheading{org}{place}{role}{dates},
\\href, \\textbf and \\textit. The centered contact block is skipped.

Usage: tex2html.py path/to/resume.tex path/to/output.html
"""
import html
import re
import sys

ARGC = {"href": 2, "textbf": 1, "textit": 1, "emph": 1}
DROP = {"LARGE", "Large", "large", "small", "centering", "par", "noindent", "hfill"}
SPACE = {"enspace", "quad", "qquad", " "}
ESCAPED = {"&": "&amp;", "%": "%", "_": "_", "#": "#", "$": "$", "{": "{", "}": "}"}
SYMBOLS = {"textasciitilde": "~", "textbar": "|", "ldots": "…"}


def read_group(s, i):
    """s[i] == '{'. Return (inner text, index after the closing brace)."""
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1 : j], j + 1
        j += 1
    raise ValueError("unbalanced braces near: " + s[i : i + 60])


def skip_ws(s, i):
    while i < len(s) and s[i] in " \t\n":
        i += 1
    return i


def read_args(s, i, n):
    args = []
    for _ in range(n):
        i = skip_ws(s, i)
        arg, i = read_group(s, i)
        args.append(arg)
    return args, i


def read_command(s, i):
    """s[i] == '\\'. Return (name, index after the name)."""
    m = re.match(r"\\([A-Za-z]+\*?|.)", s[i:])
    return m.group(1), i + m.end()


def inline(s):
    """Convert inline LaTeX to HTML."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            name, i = read_command(s, i)
            if name in ESCAPED:
                out.append(ESCAPED[name])
            elif name == "\\":  # line break, with optional [2pt]
                if i < len(s) and s[i] == "[":
                    i = s.index("]", i) + 1
                out.append("<br>")
            elif name in SYMBOLS:
                if i < len(s) and s[i : i + 2] == "{}":
                    i += 2
                out.append(SYMBOLS[name])
            elif name in SPACE:
                out.append(" ")
            elif name in DROP:
                pass
            elif name in ARGC:
                args, i = read_args(s, i, ARGC[name])
                if name == "href":
                    out.append(f'<a href="{html.escape(args[0])}">{inline(args[1])}</a>')
                elif name == "textbf":
                    out.append(f"<strong>{inline(args[0])}</strong>")
                else:
                    out.append(f"<em>{inline(args[0])}</em>")
            else:
                raise ValueError(f"unsupported command \\{name}")
        elif c == "{":
            inner, i = read_group(s, i)
            out.append(inline(inner))
        elif c == "~":
            out.append("&nbsp;")
            i += 1
        elif s.startswith("--", i):
            out.append("–")
            i += 2
        else:
            out.append(html.escape(c, quote=False))
            i += 1
    return re.sub(r"\s+", " ", "".join(out)).strip()


def strip_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in s.split("\n"))


def convert(tex):
    body = tex.split("\\begin{document}", 1)[1].split("\\end{document}", 1)[0]
    body = strip_comments(body)

    out = ['<div class="cv">']
    lists = []      # stack of open <ul> levels; each holds whether an <li> is open
    section_open = False
    text = []       # pending raw text for the current item

    def flush():
        raw = "".join(text).strip()
        text.clear()
        if raw:
            out.append(inline(raw))

    def close_li():
        flush()
        if lists and lists[-1]:
            out.append("</li>")
            lists[-1] = False

    def open_li(cls=""):
        close_li()
        out.append(f'<li{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>')
        lists[-1] = True

    i = 0
    while i < len(body):
        c = body[i]
        if c == "{" and not lists and body[skip_ws(body, i + 1):].startswith("\\centering"):
            # Contact block (name + links): skipped, the site masthead and nav cover it.
            _, i = read_group(body, i)
            continue
        if c != "\\":
            text.append(c)
            i += 1
            continue
        name, j = read_command(body, i)
        if name == "section*":
            close_li()
            (title,), i = read_args(body, j, 1)
            if section_open:
                out.append("</section>")
            out.append(f"<section><h2>{inline(title)}</h2>")
            section_open = True
        elif name == "begin":
            (env,), i = read_args(body, j, 1)
            if env != "itemize":
                raise ValueError(f"unsupported environment {env}")
            if i < len(body) and body[i] == "[":
                i = body.index("]", i) + 1
            flush()
            out.append(f'<ul class="cv-list cv-level-{len(lists) + 1}">')
            lists.append(False)
        elif name == "end":
            (env,), i = read_args(body, j, 1)
            close_li()
            out.append("</ul>")
            lists.pop()
        elif name == "item":
            open_li()
            i = j
        elif name == "resumeItem":
            (label, desc), i = read_args(body, j, 2)
            open_li()
            out.append(f"<strong>{inline(label)}</strong>: {inline(desc)}")
        elif name == "resumeSubheading":
            (org, place, role, dates), i = read_args(body, j, 4)
            flush()
            if out[-1] == "<li>":
                out[-1] = '<li class="cv-entry">'
            out.append(
                f'<div class="cv-row"><strong>{inline(org)}</strong><span>{inline(place)}</span></div>'
                f'<div class="cv-row cv-sub"><em>{inline(role)}</em><span>{inline(dates)}</span></div>'
            )
        else:
            text.append(body[i:j])
            i = j
    close_li()
    if section_open:
        out.append("</section>")
    out.append("</div>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f:
        result = convert(f.read())
    with open(dst, "w") as f:
        f.write(result)
