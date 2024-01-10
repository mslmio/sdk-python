# Generate requirements.txt with lowercase package names.
pipreqs . --force

# Convert contents to lowercase and overwrite requirements.txt.
awk '{print tolower($1)}' requirements.txt > temp_requirements.txt
mv temp_requirements.txt requirements.txt
