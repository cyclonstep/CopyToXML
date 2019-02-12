import sys
import xml.etree.ElementTree as ET
import shutil
from pathlib import Path
from pprint import pprint

def argev():
    print("This is the name of the script: ", sys.argv[0])
    print("Number of arguments: ", len(sys.argv))
    # print("The arguments are: ", str(sys.argv))
    print("XML files is: ", sys.argv[1])
    print("XML search node is: ", sys.argv[2])
    print("Directory src is: ", sys.argv[3])
    # print("Directory backup is: ", sys.argv[3])
    # print("Target directory for backup is: ", sys.argv[4])

def search_all_files(directory):
    dirpath = Path(directory)
    assert(dirpath.is_dir())
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x)
        else:
            file_list.extend(search_all_files(directory/x))
    # pprint(file_list)
    return file_list

def xmlParser(xml, node):
    tree = ET.parse(xml)
    root = tree.getroot()
    id_list = []
    for utterance in root.findall('utterance'):
        id = utterance.find('id').text
        id_list.append(id)
        print(id)
    return id_list

def copyFiles(file_name, dir_from, dir_to):
    in_file = Path(dir_from / file_name)
    to_file = Path(dir_to / file_name / "audio")
    shutil.copy(str(in_file), str(to_file))


def run():
    argev()
    search_all_files(sys.argv[3])
    xmlParser(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    run()