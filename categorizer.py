import ollama
import os 

#Configuration
model="jerry"
input_file=".dataset/grocery_list.txt"
output_file=".dataset/aftereffectgrocery_list.txt"

#Check if it exist or not 
if not os.path.exists(input_file):
    print(f"Error:{input_file} not found")
    exit(1)

else:
    with open(input_file,"r") as f :
        items=f.read().strip()

#Prompt
prompt="""
You are ans assisant to all the moms of the country who go to the grocery store;
and your work is to categorize the grocey items in separte categories so that it would be easy for her to collect the items from a respective block 

Categorize these items into appropriate categories.
Sort the items alphabetically within each category.
Present the categorized list in a clear and organized manner, 
"""



#code remaing
try:
    resposne = ollama.generate(
        model=model,
        prompt=prompt,
    )
    txt=response.get("resposne","")
#Output file 
    with open(output_file,"w") as f:
        f.write(txt.strip())



