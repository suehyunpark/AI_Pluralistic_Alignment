# This file contains a dictionary of tokens to extract of the answer choices in the GlobalQA and MPI dataset
# A single answer has multiple tokens which could produce it
# Used in "create_model_response_globalqa.py" and "create_model_response_mpi.py"

def token_to_extract_globalqa_fn(model):
    if "Llama-2" in model or 'llama' in model or 'alpaca' or 'tulu' in model:
        return {"A": [68, 319, 29909], 
                "B":[69, 350, 29933],
                "C":[70, 315, 29907],
                "D":[71, 360, 29928],
                "E":[72, 382, 29923],
                "F":[73, 383, 29943],
                "G":[74, 402, 29954],
                "H":[75, 379, 29950],
                "I":[76, 306, 29902],
                "J":[77, 435, 29967],
                "K":[78, 476, 29968],
                "L":[79, 365, 29931],
                "M":[80, 341, 29924],
                "N":[81, 405, 29940],
                "O":[82, 438, 29949],
                "P":[83, 349, 29925],
                "Q":[84, 660, 29984],
                "R":[85, 390, 29934]}
    elif "mistral" in model or "Mistral" in model or "janus" in model:
        return {'A': [68, 330, 28741],
                'B': [69, 365, 28760],
                'C': [70, 334, 28743],
                'D': [71, 384, 28757],
                'E': [72, 413, 28749],
                'F': [73, 401, 28765],
                'G': [74, 420, 28777],
                'H': [75, 382, 28769],
                'I': [76, 315, 28737],
                'J': [77, 475, 28798],
                'K': [78, 524, 28796],
                'L': [79, 393, 28758],
                'M': [80, 351, 28755],
                'N': [81, 418, 28759],
                'O': [82, 451, 28762],
                'P': [83, 367, 28753],
                'Q': [84, 1186, 28824],
                'R': [85, 399, 28754]}
    
def token_to_extract_mpi_fn(model):
    if "Llama-2" in model or 'llama' in model or 'alpaca' or 'tulu' in model:
        return {"A": [68, 319, 29909], 
                "B":[69, 350, 29933],
                "C":[70, 315, 29907],
                "D":[71, 360, 29928],
                "E":[72, 382, 29923]}
    elif "mistral" in model or "Mistral" in model or "janus" in model:
        return {'A': [68, 330, 28741],
                'B': [69, 365, 28760],
                'C': [70, 334, 28743],
                'D': [71, 384, 28757],
                'E': [72, 413, 28749]}