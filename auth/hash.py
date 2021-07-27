from hashlib import sha256

def hash_text(text):
    return sha256(text.encode()).hexdigest()

if __name__ == '__main__':
    ingest = str(input('Text to hash: '))
    print(hash_text(ingest))
