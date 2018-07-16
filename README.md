# pharmacy_count
# This repo is for insight data_engineering track question

# Every Id name medicine and cost are given in each line of the input data 
# The top cost of the medicines are sorted and given in python code 


Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.


Output : program needs to create the output file, top_cost_drug.txt, that contains comma (,) separated fields in each line.

Each line of this file should contain these fields:

    drug_name: the exact drug name as shown in the input dataset
    num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
    total_cost: total cost of the drug across all prescribers

