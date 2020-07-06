import os, sys, string
import pandas as pd

GE_path = "/Users/ram5ge/Desktop/Gtex_v7_GE/samples_groups/"
SRA_table_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/SRA_to_GTEX_sample_table.csv"
output_path = "/Users/ram5ge/Desktop/GTEX_breast_v8/"
groups_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/groups.Gtex_Breast1.txt"
expression_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/exp.GTEX-steady-state.txt"
def create_sample_and_donor_ordering():
    #output1 = open(output_path+"CYCLOPS_donor_order_summary.txt", 'w')
    #output2 = open(output_path+"CYCLOPS_order_phase_diff_btw_samples_plot.txt", 'w')
    #output2.write("Donor"+'\t'+"# tissue"+'\t'+"Min"+'\t'+"Max"+'\t'+"Phase_diff"+'\t'+"Phase"+'\t'+"Tissues"+'\n')
    #output3 =open (output_path+"SRR_mapping.txt", 'w')
    SRA_dict= {}
    SRA_dict1 = {}
    SRA_dict2 = {}
    groups_list = []
    cyclops_ordering_dict1 = {}
    cyclops_ordering_dict2 = {}
    cyclops_ordering_dict3 = {}
    for lines2 in open(groups_file, 'rU').xreadlines():
        data2 = lines2.rstrip()
        groups_data = string.split(data2, '\t')
        #print groups_data;sys.exit()
        SRR_id = groups_data[0]
        groups_list.append(SRR_id)
    for lines1 in open(SRA_table_file, 'rU').xreadlines():
        data1 = lines1.rstrip()
        SRA_data = string.split(data1, ',')
        SRR = SRA_data[1]
        Gtex = SRA_data[2]
        tis = SRA_data[3]
        #print SRR, Gtex, tis;sys.exit()
        if tis =="Breast - Mammary Tissue":
            #print Gtex;sys.exit()
            Gtex_donor = string.split(Gtex, '-')
            Gtex_donor = Gtex_donor[0]+"-"+Gtex_donor[1]
            try:SRA_dict[Gtex_donor].append(SRR,)
            except Exception: SRA_dict[Gtex_donor] = [SRR]
            SRA_dict1 [SRR] = (Gtex)
    #print len(SRA_dict2);sys.exit()
    newgroups = []
    for don in SRA_dict:
        #print don
        for SRRs in SRA_dict[don]:
            #print SRRs
            if SRRs in groups_list:
                G_sample = SRA_dict1[SRRs]
                SRA_dict2[SRRs] = (G_sample)
                #print don, SRRs;sys,exit()
                #newgroups.append(SRRs+'\t'+don+'\t'+G_sample+'\n')
    #print SRA_dict2;sys.exit()
    #print newgroups
    #print len(newgroups);sys.exit()
    exp_data = pd.read_csv(expression_file,sep="\t")
    exp_data = exp_data.rename(columns = SRA_dict2)
    exp_data.to_csv("/Users/ram5ge/Desktop/GTEX_breast_v8/exp.GTEX-Breast_w_sample_numbers.csv", index=False )
    
    #sys.exit()
    #print exp_data.columns;sys.exit()
    exp_data = exp_data.set_index('Gene_ID')
    GE_dict = exp_data.T.to_dict(orient='list')
    #print GE_dict;sys.exit()
    #headers = pd.read_csv(expression_file,index_col=0, nrows=0).columns.tolist()
    #print headers
                
    #print len(SRA_dict);sys.exit()
    # for don in SRA_dict:
    #     output3.write(don+'\t'+str(SRA_dict[don])[1:-1]+'\n')
    # output3.close()
    
    Donor_phase_list = []
    directory1 = os.listdir(GE_path)
    for files in directory1:
        x = 0
        if '_sample_phase_ordered' in files:
            tissue = string.split(files, '_')
            tissue = tissue[0]
            fname = GE_path+files
            for lines in open(fname).xreadlines():
                if x >=1:
                    data = lines.rstrip()
                    cylops_data = string.split(data, ',')
                    #print cylops_data;sys.exit()
                    sample_ID = cylops_data[0]
                    donor = string.split(sample_ID, ".")
                    donor_ID = donor[0]+"-"+donor[1]
                    Ephase = float(cylops_data[1])*3.8216
                    #print sample_ID, donor_ID, Ephase;sys.exit()
                    try: cyclops_ordering_dict1 [donor_ID].append(Ephase,)
                    except Exception: cyclops_ordering_dict1 [donor_ID]= [Ephase]
                    #Donor_phase_list.append(donor_ID, Ephase)
                    try: cyclops_ordering_dict2 [donor_ID].append(sample_ID,)
                    except Exception: cyclops_ordering_dict2 [donor_ID]= [sample_ID]
                    try: cyclops_ordering_dict3 [donor_ID].append(tissue,)
                    except Exception: cyclops_ordering_dict3 [donor_ID]= [tissue]
                x+=1           
    #print len(cyclops_ordering_dict1), len(cyclops_ordering_dict2)
    #print cyclops_ordering_dict1
    #print cyclops_ordering_dict2 
    for D in cyclops_ordering_dict1:
        phase_list = str(cyclops_ordering_dict1[D])[1:-1]
        sample_list = '\t'.join(cyclops_ordering_dict2[D])
        Min = min(cyclops_ordering_dict1[D])
        Max = max(cyclops_ordering_dict1[D])
        n = len(cyclops_ordering_dict2[D])
        Tissues = '|'.join(cyclops_ordering_dict3[D])
        if Max >= 21 and Min <=1 or Max >= 22 and Min <=2 or Max >= 23 and Min <=3 or Max >= 24 and Min <=4:
            Min1 = Min+24
            phase_diff = Min1-Max
            if phase_diff<4:
               print phase_list;sys.exit()
            #in_phase_list.append()
            #print D, Min,Max, phase_diff#;sys.exit()
            #print phase_list;sys.exit()
            #output2.write(D+'\t'+str(n)+'\t'+str(Min)+'\t'+str(Max)+'\t'+str(phase_diff)+'\t'+phase_list+'\t'+Tissues+'\n')
        else:
            phase_diff = Max-Min
            #output2.write(D+'\t'+str(n)+'\t'+str(Min)+'\t'+str(Max)+'\t'+str(phase_diff)+'\t'+phase_list+'\t'+Tissues+'\n')
        #print Min, Max, phase_diff;sys.exit()
        #output1.write(D+'\t'+str(cyclops_ordering_dict1[D])[1:-1]+'\t'+str(cyclops_ordering_dict2[D])[1:-1]+'\n')
        #output2.write(D+'\t'+str(n)+'\t'+str(Min)+'\t'+str(Max)+'\t'+str(phase_diff)+'\n')
    #output1.close()
    #output2.close()
    
if __name__ == '__main__':
   create_sample_and_donor_ordering() 
            