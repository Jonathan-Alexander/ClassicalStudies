# you'll need:
# - bionode-ncbi (https://github.com/bionode/bionode-ncbi)
# - jq (https://github.com/stedolan/jq)

# count the number of retracted papers
# bionode-ncbi search pubmed "\"Retracted Publication\"" \
# | jq -c 'select(.pubtype[] | inside("Retracted Publication"))'
#  | wc -l

# get PMCIDs for all the retracted papers
# note that not all retracted papers have PMCIDs - those without PMCIDs will be left out of this list
bionode-ncbi search pubmed "\"Retracted Publication\"" \
  | jq -c 'select(.pubtype[] | inside("Retracted Publication")) | .articleids | .[] | select(.idtype == "pmcid")| .value' \
  > pubmed_retracted_pmcids.txt
  
# get all notifications of retraction
# bionode-ncbi search pubmed "\"Retraction of Publication\"" \
# | jq -c 'select(.pubtype[] | inside("Retraction of Publication"))' > pubmed_notifications.json
