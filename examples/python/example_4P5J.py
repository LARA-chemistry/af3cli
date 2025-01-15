"""
Example:
tRNA-mimicking RNA from TYM Virus
    - Protein Data Bank (PDB) Entry: 4P5J
    - Reference: https://www.rcsb.org/structure/4P5J

This script provides a Python implementation as an alternative to the af3cli input bash script.
"""

import pprint
from pathlib import Path
from af3cli import InputBuilder, Sequence, SequenceType
from af3cli.sequence import read_fasta

# Define constants
FILENAME = "example_4P5J_python.py"
JOB_NAME = "example_4P5J_py_job"
INPUT_SEQUENCE_TYPE = SequenceType.RNA
INPUT_FASTA_FILEPATH = str(Path(__file__).resolve().parent.parent / "example_files/rcsb_pdb_4P5J.fasta")

# Create RNA sequence object
for _, fasta_sequence_string in read_fasta(INPUT_FASTA_FILEPATH):
    sequence = Sequence(seq_type=INPUT_SEQUENCE_TYPE, seq_str=fasta_sequence_string)

# Build input configuration for the job
input_builder = InputBuilder()
input_builder.set_name(JOB_NAME)
input_builder.add_sequence(sequence)
internal_input = input_builder.build()

# Uncomment following line to generate output as JSON file
#internal_input.write(FILENAME)

print_json_via_debug = pprint.PrettyPrinter(indent=4)
print_json_via_debug.pprint(internal_input.to_dict())
