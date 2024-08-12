from uuid import uuid4


def to_file(content: str, filename: str = "file", extension: str = "txt", save_path: str = "./") -> None:
    filename = f"{filename}-{str(uuid4()).split('-')[0]}" + "." + extension
    with open(save_path + filename, 'w') as file:
        file.write(content)
