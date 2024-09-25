# This file contains a dictionary of tokens to extract of the answer choices in the GlobalQA and MPI dataset
# A single answer has multiple tokens which could produce it
# Used in "create_model_response_globalqa.py" and "create_model_response_mpi.py"

def token_to_extract_globalqa_fn(tokenizer):
    tokens_to_extract = {}
    for i in range(0x41, 0x53):  # A to R
        hex_value = hex(i).upper().replace('X', 'x')
        tokens = [f"<{hex_value}>", f"▁{chr(i)}", chr(i)]
        tokens_to_extract[chr(i)] = tokenizer.convert_tokens_to_ids(tokens)
    return tokens_to_extract
    
def token_to_extract_mpi_fn(tokenizer):
    tokens_to_extract = {}
    for i in range(0x41, 0x46):  # A to E
        hex_value = hex(i).upper().replace('X', 'x')
        tokens = [f"<{hex_value}>", f"▁{chr(i)}", chr(i)]
        tokens_to_extract[chr(i)] = tokenizer.convert_tokens_to_ids(tokens)
    return tokens_to_extract