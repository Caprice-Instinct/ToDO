import zipfile


def extract_archive(archivepath, destfolder):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destfolder)


if __name__ == '__main__':
    extract_archive(r"C:\Users\linet\PycharmProjects\ToDo\bonus_examples\dest\compressed.zip",
                    r"C:\Users\linet\PycharmProjects\ToDo\bonus_examples\dest")
