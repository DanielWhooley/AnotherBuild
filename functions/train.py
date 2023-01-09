import os

import pefile


def train(root):
    data = []
    # Recursively traverse the directory tree and process each PE file
    for path, dirs, files in os.walk(root):
        for file in files:
            # Check if file is a PE file
            if file.endswith(".exe"):
                pe = pefile.PE(os.path.join(path, file))
                # Extract imphash and rich PE hash
                imphash = pe.get_imphash()
                rich_hash = pe.get_rich_header_hash()
                # Append data to the list in the format: (family, imphash, rich_hash)
                data.append(("family_label", imphash, rich_hash))
    return data
