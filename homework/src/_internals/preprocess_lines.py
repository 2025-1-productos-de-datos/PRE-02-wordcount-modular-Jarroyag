def preprocess_lines(all_lines):
    all_lines = (line.lower().srip() for line in all_lines)
    return all_lines