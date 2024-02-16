# VS-PrepFinalList
This tool assists in selecting compounds from an SD file to generate a final hit list of 3D poses.

## Execution
```
python VS-PrepFinalList.py test.csv glidedock.sdf selected_compounds.sdf
```

The inputfiles for this process are `test.csv` and `glidedock.sdf`. The resulting output file is named `selected_compounds.sdf`. This command utilizes the information from a CSV file to extract 3D structures from `glidedock.sdf`, resulting in the generation of selected compounds saved in an SD file format.
