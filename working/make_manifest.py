"""
Util script for MTGA localization.
Author: B.F.M.

"data_loc_*.mtga" 파일을 통해 downloads.manifest 파일을 수정해준다.
"""
import hashlib
import os

def get_md5(full_path):
    return hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()

def file_as_bytes(file):
    with file:
        return file.read()

def get_size(full_path):
    statinfo = os.stat(full_path)
    return statinfo.st_size

if __name__ == "__main__":
    full_path = "./data_loc_333ad7faf94b7025fc22655c7299e770.mtga"
    manifest_template_name = "./template_downloads.manifest"

    file_hash = get_md5(full_path)
    file_size = get_size(full_path)

    print("MD5: ", file_hash)
    print("Size: ", file_size)

    print("Make downloads.manifest")
    manifest_template = file_as_bytes(open(manifest_template_name, 'rb'))

    content_new = manifest_template.decode() \
                .replace('file_length_here', str(file_size)) \
                .replace('file_hash_here', file_hash) \
                .replace('\r\n', '\n')

    new_manifest = open("./downloads.manifest", 'w')
    new_manifest.write(content_new)

    new_manifest.close()
    print("End")