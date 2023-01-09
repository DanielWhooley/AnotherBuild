import pefile


def get_imphash(filepath):
    pe = pefile.PE(filepath)

    # Extract imphash
    return pe.get_imphash()


def get_richHash(filepath):
    pe = pefile.PE(filepath)
    rich_hash = pe.get_rich_header_hash()
    return rich_hash
