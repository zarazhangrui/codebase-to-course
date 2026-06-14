#!/usr/bin/env python3
"""Verify built codebase-to-course course(s).

HTML-parses each index.html and checks structure + interactive-element wiring,
so the common authoring bugs (truncated quiz tags, apostrophe-broken flow JSON,
missing mandatory animations, leftover placeholders) can't ship silently.

Usage:
    python scripts/verify_courses.py <path>

<path> may be either a single course directory (one that contains index.html)
or a parent directory containing several course subdirectories. Exit code is
0 if everything passes, 1 otherwise.
"""
import sys, os, glob, json
from html.parser import HTMLParser


class CourseParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.modules = self.navdots = self.chat = self.flow = 0
        self.translations = self.quiz_blocks = 0
        self.quiz_bad = []      # quiz blocks missing a required data-* attribute
        self.flow_bad = []      # data-steps that fail JSON.parse
        self.module_ids = []
        self.navdot_targets = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = (d.get("class") or "").split()
        if tag == "section" and "module" in cls:
            self.modules += 1
            if d.get("id"):
                self.module_ids.append(d["id"])
        if tag == "button" and "nav-dot" in cls:
            self.navdots += 1
            if d.get("data-target"):
                self.navdot_targets.append(d["data-target"])
        if "chat-window" in cls:
            self.chat += 1
        if "flow-animation" in cls:
            self.flow += 1
            steps = d.get("data-steps")
            if steps is None:
                self.flow_bad.append("missing data-steps")
            else:
                try:
                    json.loads(steps)
                except Exception as e:
                    self.flow_bad.append(str(e)[:60])
        if "translation-block" in cls:
            self.translations += 1
        if "quiz-question-block" in cls:
            self.quiz_blocks += 1
            for a in ("data-correct", "data-explanation-right", "data-explanation-wrong"):
                if not d.get(a):
                    self.quiz_bad.append(a)


def find_indexes(path):
    if os.path.isfile(os.path.join(path, "index.html")):
        return [os.path.join(path, "index.html")]
    return sorted(glob.glob(os.path.join(path, "*", "index.html")))


def check(idx):
    raw = open(idx, encoding="utf-8").read()
    p = CourseParser()
    p.feed(raw)
    issues = []
    if raw.count("<!DOCTYPE html>") != 1:
        issues.append(f"DOCTYPE={raw.count('<!DOCTYPE html>')}")
    if raw.count("</html>") != 1:
        issues.append(f"</html>={raw.count('</html>')}")
    if p.modules != p.navdots:
        issues.append(f"modules({p.modules})!=navdots({p.navdots})")
    if p.chat < 1:
        issues.append("no group-chat")
    if p.flow < 1:
        issues.append("no flow-animation")
    if p.quiz_blocks < p.modules:
        issues.append(f"quizzes({p.quiz_blocks})<modules({p.modules})")
    if p.quiz_bad:
        issues.append(f"quiz-attr-missing:{len(p.quiz_bad)}")
    if p.flow_bad:
        issues.append(f"flow-json-bad:{p.flow_bad}")
    for ph in ("COURSE_TITLE", "ACCENT_COLOR", "ACCENT_HOVER", "NAV_DOTS", "MODULE_N_NAME"):
        if ph in raw:
            issues.append(f"placeholder:{ph}")
    if set(p.navdot_targets) - set(p.module_ids):
        issues.append("nav-target-unmatched")
    return p, issues


def main():
    if len(sys.argv) < 2:
        print("usage: python scripts/verify_courses.py <course-dir-or-parent>")
        return 2
    path = sys.argv[1]
    indexes = find_indexes(path)
    if not indexes:
        print(f"No index.html found under: {path}")
        return 2

    print(f"{'COURSE':<44}{'mod':>4}{'dot':>4}{'cht':>4}{'flw':>4}{'trn':>4}{'quiz':>5}  status")
    print("-" * 100)
    all_ok = True
    for idx in indexes:
        name = os.path.basename(os.path.dirname(idx))
        p, issues = check(idx)
        status = "OK" if not issues else "FAIL -> " + "; ".join(issues)
        if issues:
            all_ok = False
        print(f"{name[:44]:<44}{p.modules:>4}{p.navdots:>4}{p.chat:>4}{p.flow:>4}{p.translations:>4}{p.quiz_blocks:>5}  {status}")
    print("-" * 100)
    print("ALL COURSES PASS" if all_ok else "SOME COURSES HAVE ISSUES (see above)")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
