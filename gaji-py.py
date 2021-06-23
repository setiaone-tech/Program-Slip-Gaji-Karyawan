import os
prd = []
nm_kryn = []
jbtn = []
stts = []
jm_tg = []
n = int(input('masukkan jumlah data : '))
print()
for x in range(n):
    periode = input('Periode \t\t= ')
    prd.append(periode)
    nama_karyawan = str(input('Nama Karyawan \t\t= '))
    nm_kryn.append(nama_karyawan)
    print("")
    print("1. Manager \n2. Kabag \n3. Kasie \n4. Staff \n5. Karyawann \n6. Admin")
    jabatan = int(input('Jabatan \t\t= '))
    jbtn.append(jabatan)
    print("pilih angka ")
    print("")
    print("1. Sudah Menikah \n2. Belum Menikah")
    status = int(input('Status \t\t\t= '))
    stts.append(status)
    print("")
    jum_tang = int(input('Jumlah Tanggungan \t= '))
    jm_tg.append(jum_tang)
    os.system('cls')

for i in range(n):
    if (jbtn[i]==1 ):
        gaji_pokok=10000000
        tun_jab=5000000
        tu_trans=5000000
        tu_bpjs=2000000
        bonus=5000000
        jab="Manager"
        iy_bpjs_kes=500000
        iy_bpjs_ket=450000
    elif(jbtn[i]==2):
        gaji_pokok=8500000
        tun_jab=4500000
        tu_trans=4500000
        tu_bpjs=1500000
        bonus=4500000
        jab="Kabag"
        iy_bpjs_kes=450000
        iy_bpjs_ket=400000
    elif(jbtn[i]==3):
        gaji_pokok=6000000
        tun_jab=4000000
        tu_trans=4000000
        tu_bpjs=1000000
        bonus=4000000
        jab="Kasie"  
        iy_bpjs_kes=400000
        iy_bpjs_ket=350000
    elif(jbtn[i]==4):
        gaji_pokok=5000000
        tun_jab=3500000
        tu_trans=3500000
        tu_bpjs=900000
        bonus=3500000
        jab="Staff"
        iy_bpjs_kes=350000
        iy_bpjs_ket=300000
    elif(jbtn[i]==5):
        gaji_pokok=4000000
        tun_jab=3000000
        tu_trans=3000000
        tu_bpjs=800000
        bonus=3000000
        jab="Karyawan"
        iy_bpjs_kes=300000
        iy_bpjs_ket=250000
    elif(jbtn[i]==6):
        gaji_pokok=3000000
        tun_jab=2500000
        tu_trans=2500000
        tu_bpjs=700000
        bonus=2500000
        jab="Admin"
        iy_bpjs_kes=250000
        iy_bpjs_ket=200000

    if (stts[i] ==1):
        tunjangan=1000000
        stat="Sudah Menikah"
    else:
        tunjangan=500000
        stat="Belum Menikah"

    if (jm_tg[i] ==0):
        tun_tang=0
    elif(int(jm_tg[i]) >=1 and int(jm_tg[i])<3):
        tun_tang=1000000
    elif(int(jm_tg[i]) >=3 and int(jm_tg[i])<6):
        tun_tang=2000000
    else:
        tun_tang=4000000

    lembur=0
    pen_lain= tunjangan + tun_tang
    pinalty=0
    asuransi=0
    da_pen=0
    pot_lain=0
    pajak= int(gaji_pokok *0.15)
    total_penerimaan= gaji_pokok + tun_jab + tu_trans + tu_bpjs + lembur + bonus + pen_lain
    total_pengurangan= iy_bpjs_kes + iy_bpjs_ket + pajak + pinalty + asuransi + da_pen + pot_lain
    total_diterima_karyawan= total_penerimaan - total_pengurangan

    print("_"*121)
    print('')
    print(" "*55,"\033[1mSLIP GAJI\033[0m")
    print("_"*121)
    print("")
    print(" \033[1mPT JAVA ANIMA DARMAJA\033[0m                                                   Periode       :",prd[i])
    print(" One Stop Business and IT Solution                                       Nama Karyawan :",nm_kryn[i])
    print(" Jl.Cempaka Blok C3 No.24 Perum Beringin Raya,Kemiling                   Jabatan       :",jbtn[i])
    print(" Bandar Lampung                                                          Status        :",stts[i])
        
    print("_"*121)
    print("")
    print(" \033[1mPENERIMAAN\033[0m")
    print("  - Gaji Pokok \t\t\t\t\t",' '*63,gaji_pokok)
    print("  - Tunjangan Jabatan \t\t\t",' '*71,tun_jab)
    print("  - Tunjangan Transportasi \t\t",' '*71,tu_trans)
    print("  - Tunjangan BPJS \t\t\t\t",' '*63,tu_bpjs)
    print("  - Lembur \t\t\t\t",' '*77,lembur)
    print("  - Bonus / THR \t\t",' '*79,bonus)
    print("  - Penerimaan Lainnya \t\t",' '*79,pen_lain)
    print(" "*107,"\033[4m            \033[0m")
    print("  \033[1mTotal Penerimaan\033[0m \t\t",' '*74,"\033[1mRp\033[0m ",total_penerimaan)
    print("")
        
    print(" \033[1mPENGURANGAN\033[0m")
    print("  - Iuran BPJS Kesehatan                                                                                         ",iy_bpjs_kes)
    print("  - Iuran BPJS Ketenagakerjaan                                                                                   ",iy_bpjs_ket)
    print("  - Pajak                                                                                                       ",pajak)
    print("  - Pinalty                                                                                                           ",pinalty)
    print("  - Asuransi                                                                                                          ",asuransi)
    print("  - Dana Pensiun                                                                                                      ",da_pen)
    print("  - Potongan Lainnya                                                                                                  ",pot_lain)
    print("                                                                                                            \033[4m            \033[0m")
    print("  \033[1mTotal Pengurangan                                                                                         Rp  \033[0m" ,total_pengurangan)
    print("")
        
    print("                                                                                                            \033[4m            \033[0m")
    print(" \033[1mTOTAL DITERIMA KARYAWAN                                                                                    Rp\033[0m ",total_diterima_karyawan)
    print("")
    print("")
    print("")
        
    print("_"*121)
        
    print("")
    print("")
    print(" "*33," Jakarta, ",prd[i])
    print("")
    print("")
    print("        \tPenerima                                                              \tPT JAVA ANIMA DARMAJA")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("    \t",nm_kryn[i],"                         \t\t\tAdministrasi PT JAVA ANIMA DARMAJA") 
    print('')
    print('')
    print("_"*121)
    print('')
    print('')