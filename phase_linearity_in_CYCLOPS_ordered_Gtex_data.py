import os, sys, string

all_groups_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/GTExv7CircAtlas_SmplPhases.csv"
output_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/Gtex_comp_orders_for_breast_donors_more_than_2_tissues.csv"
phase_diff_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/CYCLOPS_order_phase_diff_btw_samples.txt"
breast_groups_file = "/Users/ram5ge/Desktop/GTEX_breast_v8/groups.Gtex_Breast.txt"
def phase_linearity():
    output = open(output_file, 'w')
    #output.write("Donor"+','+"Aorta_sample"+','+"Aorta_Phase"+','+"Liver_sample"+','+"Liver_Phase"+'\n')
    sample_dict = {}
    donor_dict= {}
    phase_diff_dict = {}
    for dlines in open(phase_diff_file, 'rU').readlines()[1:]:
        ddata = dlines.rstrip()
        pre_orer_data = string.split(ddata, '\t')
        Donor = pre_orer_data[0]
        phase_diff = float(pre_orer_data[4])
        Tissues = pre_orer_data[6]
        Tissues1 = string.split(Tissues, "|")
        #print len(Tissues1)
        #print Tissues#, Donor, phase_diff;sys.exit()
        if phase_diff <4 and len(Tissues1)>=2:
            phase_diff_dict[Donor] = (Tissues)
    #print phase_diff_dict;sys.exit()
    b_dict = {}
    for blines in open(breast_groups_file, 'rU').readlines()[1:]:
        bdata = blines.rstrip()
        #print bdata;sys.exit()
        b_samples =bdata
        b_donor = string.split(bdata, '-')
        b_donor = b_donor[0]+'-'+b_donor[1]
        b_dict[b_donor] = (b_samples)
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
        try:donor_dict[donor].append (Sample,)
        except Exception:donor_dict[donor] = [Sample]
    comp_list=[]    
    for p in phase_diff_dict:
        if p in b_dict:
            #print p
            b = b_dict[p]
            sam_id = donor_dict[p]
            #print sam_id#;sys.exit()
            for x in sam_id:
                T = sample_dict[x]
                #print T;sys.exit()
                comp_list.append([p,b,x,T])
    #print comp_list;sys.exit()
    for m in comp_list:#(m, n, o) in comp_list:
        output.write(str(m)[1:-1])
        output.write('\n')
    output.close()
        
        #print tissue, Sample#, Ephase, #;sys.exit()
        # if tissue == "Aorta" or tissue == "Liver":
        #     #print Sample, tissue
        #     donor = string.split(Sample, '-')
        #     donor = donor[0]+'-'+donor[1]
        #     try:donor_dict[donor].append (Sample,)
        #     except Exception:donor_dict[donor] = [Sample]
        #     sample_dict [Sample] = (Ephase)
    # print len(sample_dict)
    # print len(donor_dict);sys.exit()
    
    # x =0
    # for D in donor_dict:
    #     if len(donor_dict[D]) ==2:
    #         x+=1
    #         #print x
    #         #print D
    #         S_Heart = donor_dict[D][0]
    #         S_Liver = donor_dict[D][1]
    #         Liver_Phase =sample_dict[S_Liver]
    #         Heart_Phase = sample_dict[S_Heart]
    #         output.write(D+','+S_Heart+','+Heart_Phase+','+S_Liver+','+Liver_Phase+'\n')
    #         #print D, S_Heart, S_Liver;sys.exit()
    # output.close()
            
            
if __name__ == '__main__':
    phase_linearity()
        
            