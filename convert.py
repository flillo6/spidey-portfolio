import sys
import re

with open(r"C:\Users\franc\.gemini\antigravity\brain\ec2c640e-08ae-49f1-a39b-899c6a4e3407\.system_generated\steps\209\output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract the JSX part inside the return ( ... );
match = re.search(r"return \(\s*(.*?)\s*\);\s*}", text, re.DOTALL)
if not match:
    match = re.search(r"(<div.*</div>)", text, re.DOTALL)

if not match:
    print("Could not find JSX")
    sys.exit(1)

jsx = match.group(1)

# Basic JSX to HTML replacements
jsx = jsx.replace("className=", "class=")

# Replace `{...}` strings. e.g. {`/// text`} -> /// text
jsx = re.sub(r"\{`([^`]+)`\}", r"\1", jsx)

# Self closing div tags.
jsx = re.sub(r"(<div[^>]*?)\s*/>", r"\1></div>", jsx)

# Image src from variables
jsx = jsx.replace('{imgTechnicalHardwareInterface}', '"http://localhost:3845/assets/4710289e0517478032616c1e2592ed05581e37ac.png"')
jsx = jsx.replace('{imgGlobalDigitalDataNetwork}', '"http://localhost:3845/assets/a0e4a4830ceb36d176a60aa6d02274769d92749c.png"')
jsx = jsx.replace('{imgContainer}', '"http://localhost:3845/assets/4181ac2fba2404fb1f4469628988b9f8ee34ba4e.svg"')

# Make sure img tags end properly if they are <img ... /> -> <img ...>
jsx = re.sub(r"(<img[^>]*?)\s*/>", r"\1>", jsx)

# Handle styles
def style_repl(m):
    inner = m.group(1).strip()
    # Replace key names (e.g., backgroundImage -> background-image)
    # Naive parse just for backgroundImage: "..."
    if "backgroundImage" in inner:
        # e.g. backgroundImage: "linear-gradient(...)"
        val = inner.split(":", 1)[1].strip()
        if val.startswith('"') and val.endswith('"'): val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"): val = val[1:-1]
        return f'style="background-image: {val};"'
    return f'style="{inner}"'

jsx = re.sub(r"style={{(.*?)}}", style_repl, jsx)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE NEIGHBORHOOD ENGINEER</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Liberation+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
    <style>
      body {{ font-family: 'Space Grotesk', sans-serif; background: #000; overflow-x: hidden; }}
      .font-\\[\\'Space_Grotesk\\:Bold\\'\\,sans-serif\\] {{
          font-family: 'Space Grotesk', sans-serif !important;
          font-weight: 700 !important;
      }}
      .font-\\[\\'Space_Grotesk\\:Regular\\'\\,sans-serif\\] {{
          font-family: 'Space Grotesk', sans-serif !important;
          font-weight: 400 !important;
      }}
      .font-\\[\\'Space_Grotesk\\:Light\\'\\,sans-serif\\] {{
          font-family: 'Space Grotesk', sans-serif !important;
          font-weight: 300 !important;
      }}
      .font-\\[\\'Liberation_Mono\\:Regular\\'\\,sans-serif\\] {{
          font-family: 'Liberation Mono', monospace !important;
          font-weight: 400 !important;
      }}
      .font-\\[\\'Liberation_Mono\\:Bold\\'\\,sans-serif\\] {{
          font-family: 'Liberation Mono', monospace !important;
          font-weight: 700 !important;
      }}
    </style>
</head>
<body class="bg-black text-white m-0 p-0">
{jsx}
</body>
</html>"""

with open(r"c:\Users\franc\Desktop\portfolio-spidey-figma\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("index.html successfully updated!")
