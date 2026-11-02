#!/usr/bin/env python3
"""Fill in your real details, then deploy. Usage:
python3 configure.py --site https://yourdomain.com --app https://app.yourdomain.com \
  --owner "Your Name"
"""
import argparse, pathlib, sys
p=argparse.ArgumentParser()
for k in ["site","app","owner"]: p.add_argument("--"+k,required=True)
a=p.parse_args()
m={"{{SITE_URL}}":a.site.rstrip("/"),"{{APP_URL}}":a.app.rstrip("/"),"{{OWNER_NAME}}":a.owner}
root=pathlib.Path(__file__).parent
for f in root.iterdir():
    if f.suffix in {".html",".txt",".xml"}:
        t=f.read_text(encoding="utf-8")
        for k,v in m.items(): t=t.replace(k,v)
        f.write_text(t,encoding="utf-8")
left=[f.name for f in root.iterdir() if f.suffix in {".html",".txt",".xml"} and "{{" in f.read_text(encoding="utf-8")]
print("Done." if not left else "Tokens still present in: "+", ".join(left))
