import csv

if __name__ == '__main__':
    kecil = []
    besar = []
    hasilakhir = []
    #Pembuatan variabel pemampung untuk menghitung banyak label di data >50K
    jmlyoungb = 0
    jmladultb = 0
    jmloldb = 0
    jmlprivateb = 0
    jmllocalb = 0
    jmlselfb = 0
    jmlhsb = 0
    jmlbachelorsb = 0
    jmlsomeb = 0
    jmldivorceb = 0
    jmlneverb = 0
    jmlmarriedb = 0
    jmlprofb = 0
    jmlcraftb = 0
    jmlexecb = 0
    jmlhusb = 0
    jmlnotb = 0
    jmlownb = 0
    jmlnorb = 0
    jmllowb = 0
    jmlmanb = 0
    #=========================================================================
    #Pembuatan variabel penampung untuk menghitung banyak label di data <=50K 
    jmlyoungk = 0
    jmladultk = 0
    jmloldk = 0
    jmlprivatek = 0
    jmllocalk = 0
    jmlselfk = 0
    jmlhsk = 0
    jmlbachelorsk = 0
    jmlsomek = 0
    jmldivorcek = 0
    jmlneverk = 0
    jmlmarriedk = 0
    jmlprofk = 0
    jmlcraftk = 0
    jmlexeck = 0
    jmlhusk = 0
    jmlnotk = 0
    jmlownk = 0
    jmlnork = 0
    jmllowk = 0
    jmlmank = 0
    #========================================================================
    #load file csv untuk digunakan sebagai data train
    with open('TrainsetTugas1ML.csv', newline='') as datatrain:
        next(datatrain)
        spamreader = csv.reader(datatrain, delimiter=',')
        #membagi datatrain menjadi 2, ada data >50K dan <=50K
        for a in spamreader:
            if a[8] == '>50K':
                besar.append(a)
            else:
                kecil.append(a)
        #====================================
        #menghitung banyak label di data >50k
        for b in besar:
            if b[1] == 'young':
                jmlyoungb += 1
            elif b[1] == 'adult':
                jmladultb += 1
            else:
                jmloldb += 1
        for b in besar:
            if b[2] == 'Private':
                jmlprivateb += 1
            elif b[2] == 'Local-gov':
                jmllocalb += 1
            else:
                jmlselfb += 1
        for b in besar:
            if b[3] == 'HS-grad':
                jmlhsb += 1
            elif b[3] == 'Bachelors':
                jmlbachelorsb += 1
            else:
                jmlsomeb += 1
        for b in besar:
            if b[4] == 'Divorced':
                jmldivorceb += 1
            elif b[4] == 'Never-married':
                jmlneverb += 1
            else:
                jmlmarriedb += 1
        for b in besar:
            if b[5] == 'Craft-repair':
                jmlcraftb += 1
            elif b[5] == 'Exec-managerial':
                jmlexecb += 1
            else:
                jmlprofb += 1
        for b in besar:
            if b[6] == 'Husband':
                jmlhusb += 1
            elif b[6] == 'Own-child':
                jmlownb += 1
            else:
                jmlnotb += 1
        for b in besar:
            if b[7] == 'many':
                jmlmanb += 1
            elif b[7] == 'low':
                jmllowb += 1
            else:
                jmlnorb += 1
        #=====================================
        #menghitung banyak label di data <=50k
        for c in kecil:
            if c[1] == 'young':
                jmlyoungk += 1
            elif c[1] == 'adult':
                jmladultk += 1
            else:
                jmloldk += 1
        for c in kecil:
            if c[2] == 'Private':
                jmlprivatek += 1
            elif c[2] == 'Local-gov':
                jmllocalk += 1
            else:
                jmlselfk += 1
        for c in kecil:
            if c[3] == 'HS-grad':
                jmlhsk += 1
            elif c[3] == 'Bachelors':
                jmlbachelorsk += 1
            else:
                jmlsomek += 1
        for c in kecil:
            if c[4] == 'Divorced':
                jmldivorcek += 1
            elif c[4] == 'Never-married':
                jmlneverk += 1
            else:
                jmlmarriedk += 1
        for c in kecil:
            if c[5] == 'Craft-repair':
                jmlcraftk += 1
            elif c[5] == 'Exec-managerial':
                jmlexeck += 1
            else:
                jmlprofk += 1
        for c in kecil:
            if c[6] == 'Husband':
                jmlhusk += 1
            elif c[6] == 'Own-child':
                jmlownk += 1
            else:
                jmlnotk += 1
        for c in kecil:
            if c[7] == 'many':
                jmlmank += 1
            elif c[7] == 'low':
                jmllowk += 1
            else:
                jmlnork += 1
    #======================================
    #menghitung prior
    priorb = (jmlyoungb+jmladultb+jmloldb)/(jmlyoungb+jmladultb+jmloldb+jmlyoungk+jmladultk+jmloldk)
    priork = (jmlyoungk+jmladultk+jmloldk)/(jmlyoungb+jmladultb+jmloldb+jmlyoungk+jmladultk+jmloldk)
    #menghitung probabilitas dari tiap label
    probb = {
        "young": jmlyoungb / (jmlyoungb+jmladultb+jmloldb),
        "adult": jmladultb / (jmladultb+jmlyoungb+jmloldb),
        "old": jmloldb / (jmloldb+jmlyoungb+jmladultb),
        "Private": jmlprivateb / (jmlprivateb+jmllocalb+jmlselfb),
        "Local-gov": jmllocalb / (jmlprivateb+jmllocalb+jmlselfb),
        "Self-emp-not-inc": jmlselfb / (jmlprivateb+jmllocalb+jmlselfb),
        "Some-college": jmlsomeb / (jmlhsb+jmlbachelorsb+jmlsomeb),
        "Bachelors": jmlbachelorsb / (jmlhsb+jmlbachelorsb+jmlsomeb),
        "HS-grad": jmlhsb / (jmlhsb+jmlbachelorsb+jmlsomeb),
        "Married-civ-spouse": jmlmarriedb / (jmldivorceb+jmlneverb+jmlmarriedb),
        "Never-married": jmlneverb / (jmldivorceb+jmlneverb+jmlmarriedb),
        "Divorced": jmldivorceb / (jmldivorceb+jmlneverb+jmlmarriedb),
        "Prof-special": jmlprofb / (jmlcraftb+jmlexecb+jmlprofb),
        "Exec-managerial": jmlexecb / (jmlcraftb+jmlexecb+jmlprofb),
        "Craft-repair": jmlcraftb / (jmlcraftb+jmlexecb+jmlprofb),
        "Husband": jmlhusb / (jmlhusb+jmlownb+jmlnotb),
        "Not-in-family": jmlnotb / (jmlhusb+jmlownb+jmlnotb),
        "Own-child": jmlownb / (jmlhusb+jmlownb+jmlnotb),
        "normal": jmlnorb / (jmlmanb+jmllowb+jmlnorb),
        "low": jmllowb / (jmlmanb+jmllowb+jmlnorb),
        "many": jmlmanb / (jmlmanb+jmllowb+jmlnorb)
    }
    probk = {
        "young": jmlyoungk / (jmlyoungk+jmladultk+jmloldk),
        "adult": jmladultk / (jmlyoungk+jmladultk+jmloldk),
        "old": jmloldk / (jmlyoungk+jmladultk+jmloldk),
        "Private": jmlprivatek / (jmlprivatek+jmllocalk+jmlselfk),
        "Local-gov": jmllocalk / (jmlprivatek+jmllocalk+jmlselfk),
        "Self-emp-not-inc": jmlselfk / (jmlprivatek+jmllocalk+jmlselfk),
        "Some-college": jmlsomek / (jmlhsk+jmlbachelorsk+jmlsomek),
        "Bachelors": jmlbachelorsk / (jmlhsk+jmlbachelorsk+jmlsomek),
        "HS-grad": jmlhsk / (jmlhsk+jmlbachelorsk+jmlsomek),
        "Married-civ-spouse": jmlmarriedk / (jmldivorcek+jmlneverk+jmlmarriedk),
        "Never-married": jmlneverk / (jmldivorcek+jmlneverk+jmlmarriedk),
        "Divorced": jmldivorcek / (jmldivorcek+jmlneverk+jmlmarriedk),
        "Prof-special": jmlprofk / (jmlcraftk+jmlexeck+jmlprofk),
        "Exec-managerial": jmlexeck / (jmlcraftk+jmlexeck+jmlprofk),
        "Craft-repair": jmlcraftk / (jmlcraftk+jmlexeck+jmlprofk),
        "Husband": jmlhusk / (jmlhusk+jmlownk+jmlnotk),
        "Not-in-family": jmlnotk / (jmlhusk+jmlownk+jmlnotk),
        "Own-child": jmlownk / (jmlhusk+jmlownk+jmlnotk),
        "normal": jmlnork / (jmlmank+jmllowk+jmlnork),
        "low": jmllowk / (jmlmank+jmllowk+jmlnork),
        "many": jmlmank / (jmlmank+jmllowk+jmlnork)
    }
    #=======================================================
    #load file csv yg akan dipakai untuk data test
    with open('TestsetTugas1ML.csv',newline='') as datatest:
        next(datatest)
        spamreader2 = csv.reader(datatest,delimiter=',',quotechar='|')
        for d in spamreader2:
            datat = list(d)
            hbesar = 1
            hkecil = 1
            #menghitung hasil probabilitas di data >50K
            for key,value in probb.items():
                for i in range(len(datat)):
                    if key == datat[i]:		
                        hbesar *= value
            hbesar *= priorb
            #menghitung hasil probilitas di data <=50K
            for key,value in probk.items():
                for i in range(len(datat)):
                    if key == datat[i]:
                        hkecil *= value
            hkecil *= priork
            #melakukan pembandingan probabilitas sehingga didapatkan hasil akhir
            if hbesar > hkecil :
                hasilakhir.append(">50K")
            else:
                hasilakhir.append("<=50K")
                
    #membuat file csv yg berisikan hasil akhir
    with open('TebakanTugas1ML.csv','w',newline='') as final:
        spamwriter = csv.writer(final)
        for e in hasilakhir:
            spamwriter.writerow([e])




