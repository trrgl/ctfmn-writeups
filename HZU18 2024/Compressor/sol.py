def reverse_process_file(input_path, output_path="recovered", chunk_size=2):
    with open(input_path, "rb") as f:
        data = f.read()

    recovered = bytearray()
    i = 0
    while i < len(data):
        chunk = data[i:i+chunk_size]
        chunk = chunk[::-1]
        chunk = bytearray((b + 17) % 256 for b in chunk)
        recovered.extend(chunk)
        i += chunk_size

    with open(output_path, "wb") as f:
        f.write(recovered)

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    reverse_process_file(input_file)