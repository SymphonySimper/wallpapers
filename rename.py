import os

not_file_exts: list[str] = [".py", ".txt", ".git"]
files_to_rename: list[str] = []
for file in os.listdir("."):
    if any([True if file.endswith(nfe) else False for nfe in not_file_exts]):
        continue

    files_to_rename.append(file)

for index, file in enumerate(files_to_rename):
    new_name = f"{index}.{file.split('.')[-1]}"
    os.rename(file, new_name)
