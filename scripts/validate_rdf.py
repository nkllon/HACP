#!/usr/bin/env python3
import sys
import argparse
from pyshacl import validate
from rdflib import Graph

def validate_file(data_file, shape_file):
    print(f"Validating {data_file} against {shape_file}...")
    
    data_graph = Graph()
    try:
        data_graph.parse(data_file, format="turtle")
    except Exception as e:
        print(f"Error parsing data file {data_file}: {e}")
        return None

    shacl_graph = Graph()
    try:
        shacl_graph.parse(shape_file, format="turtle")
    except Exception as e:
        print(f"Error parsing shape file {shape_file}: {e}")
        return None

    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        inference='rdfs',
        abort_on_first=False,
        meta_shacl=False,
        debug=False
    )

    if conforms:
        print(f"PASS: {data_file} conforms to shapes.")
        return True
    else:
        print(f"FAIL: {data_file} does not conform.")
        print(results_text)
        return False

def main():
    parser = argparse.ArgumentParser(description="Validate RDF files against SHACL shapes.")
    parser.add_argument("data_files", nargs='+', help="List of RDF data files (Turtle format)")
    parser.add_argument("--shapes", "-s", required=True, help="SHACL shape file (Turtle format)")
    
    args = parser.parse_args()
    
    failures = 0
    errors = 0
    for data_file in args.data_files:
        result = validate_file(data_file, args.shapes)
        if result is None:
            errors += 1
        elif result is False:
            failures += 1
    
    if errors > 0:
        sys.exit(2)
    if failures > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
