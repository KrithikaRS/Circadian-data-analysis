## This program quantifies the number of times each significant probeset is represented in all tissue
## and combine them into a seperate list to write into a file.
## This is useful in identifying the core clock related elements occuring in more number of tissues. 

import os, sys
import string

output_dir = "/Users/ram5ge/Desktop/Mouse_CR_data_literature/Baboon-GE/RAIN/Multi_tissue/"
#path = "/Users/ram5ge/Desktop/Mouse_CR_data_literature/Hogenesch_all_tissues_RNA_seq/ARS_JTK_24h_splicing/significant_files/"
path = "/Users/ram5ge/Desktop/Mouse_CR_data_literature/Baboon-GE/RAIN/significant_files/"
#tissues= ['Adrenal', 'Aorta', 'BFAT', 'BS', 'Cere', 'Heart', 'Hypo', 'Kidney','Liver','Lung',
           #'SM','WFAT']
def core_clock_probeset ():
    directory = os.listdir(path)
    #print directory
    Probeset_in_tissues_P = {}
    Probeset_in_tissues = {}

    Probeset_in_tissues2_P = {}
    Probeset_in_tissues3_P = {}
    Probeset_in_tissues_Q = {}
    significant_P_probeset_file = open(output_dir+'Multi_tissue_GE_RAIN_24h_p.txt', "w")
    #significant_P_probeset_file = open(output_dir+'SE_pathway_analysis_summary1.txt', "w")

    #significant_P_probeset_file = open(output_dir+'Multi_tissue_and_tissue_specific_circadian_splicing_events.txt', "w")
    i=0
    
    for files in directory:
        firstLine = True
        #if 'meta_' in files and i <=11:
        if '_significant_p.txt' in files:# and i <=14:
            #print files
            tissue = string.split(files, '_')
            tissue = tissue [0]
            print tissue
            #fnames = path+'/'+"meta_"+tissue+"_100_percent.txt"
            fnames = path+files
            print fnames
            #print tissue
            significant_by_P = []
            m = 0
            for lines in open(fnames,'rU').xreadlines():
                #print lines#;sys.exit()
                if firstLine:
                    firstLine = False
                else:
                    m+=1
                    #print m, tissue
                    data= lines.strip()
                    JTK_values = string.split(data,'\t')
                    #print JTK_values
                    ID = JTK_values[1]
                    #ID = string.split(ID, '|')
                    #ID = ID [0]
                    #clust_ID = JTK_values[0]
                    #print clust_ID#;sys.exit()
                    #symbol = JTK_values[2]
                    #Probeset_ID =K JTK_values[0]
                    #symbol = string.split(ID, ':')
                    #print symbol;sys.exit()
                    #Ens = Probeset_ID[0]
                    p_value = float(JTK_values[2])
                    Significant_Probes=[]        
                    if p_value <0.05:
                        try:Probeset_in_tissues_P[ID].append(tissue,)
                        except Exception:  Probeset_in_tissues_P[ID]=[tissue]
                
            i+=1
            print i
            print m
    #print len (Probeset_in_tissues_P)
        
    sorted_P_list=[]
    for Probeset_ID in Probeset_in_tissues_P:
       #x = len(Probeset_in_tissues_P[Probeset_ID])
       tissue = Probeset_in_tissues_P[Probeset_ID]
       #clust_n = Probeset_in_tissues2_P[Probeset_ID]
       #n_changed = Probeset_in_tissues3_P[Probeset_ID]
       #print type(tissue);sys.exit()
       tissue = list(set(tissue))
       #tissue = list(tissue)
       #print Probeset_ID, tissue, n_changed
       
            
       tissue.sort()
       x = len(tissue)
       tissue = string.join(tissue,'|')
       #sorted_P_list.append([x,Probeset_ID,tissue, Probeset_in_tissues2_P[Probeset_ID], Probeset_in_tissues3_P[Probeset_ID]])
       sorted_P_list.append([x,Probeset_ID,tissue])#,clust_n,n_changed])

       #print sorted_P_list
    sorted_P_list.sort()
    sorted_P_list.reverse()
    #print sorted_list
    for (x,Probeset_ID,tissue) in sorted_P_list:
        #print type(c), type(Probeset_ID), type(tissue)
        #significant_P_probeset_file.write(Probeset_ID+'\t'+str(x)+'\t'+tissue+'\t'+str(c)+'\t'+str(n)+'\n')
        significant_P_probeset_file.write(Probeset_ID+'\t'+str(x)+'\t'+tissue+'\n')
    
    significant_P_probeset_file.close()
    
    # sorted_Q_list=[]
    # for Probeset_ID in Probeset_in_tissues_Q:
    #     y = len(Probeset_in_tissues_Q[Probeset_ID])
    #     tissue = Probeset_in_tissues_Q[Probeset_ID]
    #     tissue.sort()
    #     tissue = string.join(tissue,'|')
    #     sorted_Q_list.append([y,Probeset_ID,tissue])
    #     #print sorted_Q_list
    # sorted_Q_list.sort()
    # sorted_Q_list.reverse()
    # #print sorted_Q_list
    # for (y,Probeset_ID,tissue) in sorted_Q_list:
    #     significant_Q_probeset_file.write(Probeset_ID+'\t'+str(y)+'\t'+tissue+'\n')
    # significant_Q_probeset_file.close()
    #
if __name__ == '__main__':
   core_clock_probeset()
                
    
