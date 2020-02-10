import sys
import argparse
import json
sys.path.append("../") # Go to parent folder
from src.data.make_dataset import DataImportTransform

def main():
    # Parsing input argument
    parser = argparse.ArgumentParser(description='Analyses of models for inpatient admission flow prediction')
    parser.add_argument('json_experiment_file', type=str, help='the JSON file containing experiments specifications')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    # Read from the JSON to extract features into a dictionnary
    with open(args.json_experiment_file) as file:
        exp_dict = json.load(file)

    if args.verbose:
        print('Parsing arguments from :', args.json_experiment_file)
        print(json.dumps(exp_dict, indent = 2, sort_keys=True))
        
    path_raw_visits = exp_dict["visits"]
    bloc = exp_dict["bloc"]
    holidays = exp_dict["include_holidays"] == "True"
    weather = exp_dict["weather"]
    events = exp_dict["events"]
    flu = exp_dict["flu"]
    models = exp_dict["models"]
    output_visual = exp_dict["output_visual"]
        
    # Import and transform data
    data = DataImportTransform(bloc)
    data.import_data(visits=path_raw_visits, holiday=holidays)

    
if __name__ == "__main__":
    main()