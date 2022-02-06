#certain properties arent accounted for in the carrot database
#things like "groups" or "inchikeys" or "whether a bin "is a real compound""
#this script adds those properties to make them congruent with the input to the pipeline

#the strategy is to read through every line in the additional property panda and add group/inchikey info as available
#to the input panda
#later down the pipeline, if there is no inchikey, then the compound will be connected to root in the networkx?
import pandas as pd

def input_addtional_properties(pipeline_input_panda, additional_property_panda):

    #set the index of each to be the bin id momentarily
    #iterate through the additional property panda, putting values into the pipeline input panda
    #reset the index
    #dont need to do this for one actually, but in a rush so leave for now

    pipeline_input_panda.set_index(keys='id',drop=False,inplace=True)
    additional_property_panda.set_index(keys='id',drop=False,inplace=True)

    pipeline_input_panda['group']=pipeline_input_panda['group'].astype(str)
    pipeline_input_panda['inchikey']=pipeline_input_panda['inchikey'].astype(str)

    for index, series in additional_property_panda.iterrows():
        #in case our input file has extra bins that our carrot data does not
        if index in pipeline_input_panda.index:
            pipeline_input_panda.at[index,'group']=series['group']
            pipeline_input_panda.at[index,'inchikey']=series['inchikey']

    pipeline_input_panda.reset_index(inplace=True,drop=True)
    additional_property_panda.reset_index(inplace=True,drop=True)
    return

if __name__ == "__main__":


    addtional_property_csv_address='./input_resources/carrot_input_prep_example.csv'
    pipeline_input_panda_address='./pipeline_input/pipeline_input.bin'
    pipeline_input_panda_output_address='./pipeline_input/pipeline_input_2.bin'

    additional_property_panda=pd.read_csv(addtional_property_csv_address,sep='¬',index_col=0)
    pipeline_input_panda=pd.read_pickle(pipeline_input_panda_address)
    #print(additional_property_panda)



    input_addtional_properties(pipeline_input_panda,additional_property_panda)

    print(pipeline_input_panda)

    pipeline_input_panda.to_pickle(pipeline_input_panda_output_address,protocol=0)
