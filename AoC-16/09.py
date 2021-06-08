import re

def uncompressed_length(compressed, recursive):
    current_length = 0

    while len(compressed) > 0:
        match = re.search("\((\d+)x(\d+)\)", compressed)
        if not match:
            return len(compressed)
        
        match_len = len(match.group(0))
        segment_len = int(match.group(1))
        repeat_len = segment_len
        repeat_reps = int(match.group(2))

        if recursive:
            repeated = compressed[match_len:match_len + repeat_len]
            repeat_len = uncompressed_length(repeated, recursive)

        current_length += match.start() + repeat_len * repeat_reps
        compressed = compressed[match.start() + match_len + segment_len:]

    return current_length

with open("input/09.txt") as f:
    data = f.read()

print(f"Uncompressed Length: {uncompressed_length(data, False)}")
print(f"Uncompressed Length Recursive: {uncompressed_length(data, True)}")