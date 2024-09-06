# ML-accelerated-discovery-of-heat-resistant-polysulfates-for-electrostatic-energy-storage
Machine learning models and hypothetical polysulfates library for paper "Machine learning-accelerated discovery of heat-resistant polysulfates for electrostatic energy storage"

The pre-trained models needed for prediction can be found at: https://zenodo.org/records/13714161

To predict polymer properties using models specifically designed for polysulfates, save the dataframe containing the polymer's SMILES information into a .csv file, and then use a command like:

`python Tg_Property.py xxx.csv`

`python Eg_Property.py xxx.csv`

`python DC_Property.py xxx.csv`
