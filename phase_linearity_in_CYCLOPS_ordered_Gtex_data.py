import os, sys, string

all_groups_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/GTExv7CircAtlas_SmplPhases_w_breast.csv"
output_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/Gtex_breast_ordering_from_adipose_donors2.csv"
phase_diff_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/CYCLOPS_order_phase_diff_btw_samples.txt"
breast_groups_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/groups.Gtex_Breast.txt"
def phase_linearity():
    output = open(output_file, 'w')
    output.write("Donor"+','+"Breast_sample"+','+"Breast_Phase"+','+"Fat_sample"+','+"Fat_Phase"+'\n')
    sample_dict = {}
    donor_dict= {}
    tissue_dict= {}
    phase_diff_dict = {}
    #print b_dict;sys.exit()
    for lines in open(all_groups_file, 'rU').readlines()[1:]:
        data = lines.rstrip()
        Gtex_data = string.split(data, ',')
        Sample = Gtex_data[0]#[1:-1]
        Sample = string.replace(Sample,'.','-' )
        Ephase = Gtex_data[1]
        tissue = Gtex_data[2]#[1:-1]
        sample_dict[Sample] = (tissue+','+Ephase)
        #print Sample;sys.exit()
        donor = string.split(Sample, '-')
        donor = donor[0]+'-'+donor[1]
        #print tissue, Sample#, Ephase, #;sys.exit()
        if tissue == "Breast" or tissue == "Fat SQ" or tissue == "Fat Visceral":
            #print Sample, tissue
            donor = string.split(Sample, '-')
            donor = donor[0]+'-'+donor[1]
            try:donor_dict[donor].append (Sample,)
            except Exception:donor_dict[donor] = [Sample]
            sample_dict [Sample] = (Ephase)
            try:tissue_dict[donor].append (tissue,)
            except Exception:tissue_dict[donor] = [tissue]
    # print len(sample_dict)
    # print len(tissue_dict)
    #print tissue_dict;sys.exit()
    x =0
    y = 0
    for D in donor_dict:
        print D, str(tissue_dict[D])#[1:-1]#;sys.exit()
        if len(donor_dict[D]) ==2:
            if "Breast" and "Fat SQ" in tissue_dict[D] or "Breast" and "Fat Visceral"in tissue_dict[D]:
                x+=1
                tis = str(tissue_dict[D])[1:-1]
                tis = string.replace(tis,',', '|')
                print tis
                S_Breast = donor_dict[D][0]
                S_Fat = donor_dict[D][1]
                Breast_Phase =sample_dict[S_Breast]
                Fat_Phase = sample_dict[S_Fat]
                #print D, S_Breast, Breast_Phase, S_Fat,Fat_Phase ;sys.exit()
                output.write(D+','+S_Breast+','+Breast_Phase+','+S_Fat+','+tis+','+Fat_Phase+'\n')
                
                
        elif len(donor_dict[D]) >2:
            if "Breast" and "Fat SQ" in tissue_dict[D] or "Breast" and "Fat Visceral"in tissue_dict[D]:
                y+=1
                tis = str(tissue_dict[D])[1:-1]
                tis = string.replace(tis,',', '|')
                S_Breast = donor_dict[D][0]
                S_Fat1 = donor_dict[D][1]
                S_Fat2 = donor_dict[D][2]
                S_Fat = S_Fat1+ "|"+S_Fat2
                Breast_Phase =sample_dict[S_Breast]
                Fat_Phase1 = float(sample_dict[S_Fat1])*3.8216
                Fat_Phase2 = float(sample_dict[S_Fat2])*3.8216
                Fat_phase = [Fat_Phase1,Fat_Phase2 ]
                Max = max(Fat_phase)
                Min = min(Fat_phase)
                if Max >= 21 and Min <=1 or Max >= 22 and Min <=2 or Max >= 23 and Min <=3 or Max >= 24 and Min <=4:
                    Min1 = Min+24
                    phase_diff = Max-Min1
                    if phase_diff <4:
                        FatPhase =str( Min1/3.8216)
                        output.write(D+','+S_Breast+','+Breast_Phase+','+S_Fat+','+tis+','+Fat_Phase+'\n')
                    else:
                        Fat_Phase = str(((Min1+Max)/2)/3.8216)
                        output.write(D+','+S_Breast+','+Breast_Phase+','+S_Fat+','+tis+','+Fat_Phase+'\n')
                else:
                    phase_diff = Max-Min
                    if phase_diff <4:
                        FatPhase = str(Min/3.8216)
                        output.write(D+','+S_Breast+','+Breast_Phase+','+S_Fat+','+tis+','+Fat_Phase+'\n')
                    else:
                        Fat_Phase = str(((Min+Max)/2)/3.8216)    
                        output.write(D+','+S_Breast+','+Breast_Phase+','+S_Fat+','+tis+','+Fat_Phase+'\n')
    #output.close()
            
            
if __name__ == '__main__':
    phase_linearity()
  
        
            
