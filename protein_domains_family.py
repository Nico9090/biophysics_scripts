import requests
from Bio import Entrez
import pandas as pd
class ProteinFunc():
        def __init__(self, family_name):
                self.family_name=family_name
                self.protein_data_frame=pd.DataFrame(columns=["Protein Id","Protein Name"])
        def entrez_protein_names(self,protein_ids):
            handle = Entrez.esummary(db="protein", id=protein_ids)
            names_record = Entrez.read(handle)
            return names_record
        def access_Entrez(self):
            query = Entrez.esearch(db="protein", term=self.family_name, retmax=100)
            record = Entrez.read(query)
            names=self.entrez_protein_names(record["IdList"])
            return names
        def extract_families(self): #must include self to become an instance
            entrez_result=self.access_Entrez() #need self. to access instances
            self.protein_data_frame["Protein Id"] = entrez_result["IdList"]
            self.protein_data_frame["Protein Name"]=self.protein_data_frame["Protein Id"].apply()
              # Replace with your ID
            return None

ipt=ProteinFunc("IPT")
proteins_with_ipt=ipt.extract_families()
print(proteins_with_ipt)
