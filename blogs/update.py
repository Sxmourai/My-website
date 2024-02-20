import glob
LOOK_KEYWORD = "look:"
LAYOUTS = {
    "default": "../../layouts/DefaultBlog.astro",
}



for file in glob.glob("./*.md"):
    with open(file, "r") as f:
        lines = f.readlines()
    for i,line in enumerate(lines):
        if line.startswith(LOOK_KEYWORD):
            raw_look = line[len(LOOK_KEYWORD):].strip()
            look = raw_look.lstrip() # Removes spaces if: look: default
                                                        #      | this one
            if layout := LAYOUTS.get(look):
                lines[i] = f"layout: {layout}\n"
                content = "".join(lines)
                with open(f"../src/pages/blogs/{file}", "w") as f:
                    f.write(content)
                    print(f"Wrote {file} with layout {layout}")
                    break # Done with file
            else:
                raise ValueError(f"{file} has an unknown layout !")
print("Done !")