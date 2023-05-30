def pad(pad, str, padLeft):
    if str is None:
        return pad
    if padLeft:
        return (pad + str)[-len(pad):]
    else:
        return (str + pad)[:len(pad)]

def son_iki_hane(tc):
    tc_rakam = [0] * 11
    for i in range(10, -1, -1):
        tc_rakam[i] = tc % 10
        tc = tc - tc_rakam[i]
        tc = tc // 10

    cift = tc_rakam[0] + tc_rakam[2] + tc_rakam[4] + tc_rakam[6] + tc_rakam[8]
    tek = tc_rakam[1] + tc_rakam[3] + tc_rakam[5] + tc_rakam[7]
    tc_rakam[9] = (7 * cift - tek) % 10
    tc_rakam[10] = (tc_rakam[9] + tc_rakam[8] + tc_rakam[7] + tc_rakam[6] + tc_rakam[5] +
                    tc_rakam[4] + tc_rakam[3] + tc_rakam[2] + tc_rakam[1] + tc_rakam[0]) % 10
    return tc_rakam[9] * 10 + tc_rakam[10]

def tc_new(tc, tc_sayisi, yasli):
    print_output = ""
    tc5digit = int(tc[:5])
    tc4digit = int(tc[5:9])

    while tc_sayisi:
        if yasli > 0:
            # İleri iterasyon, yaşı büyükler için
            tc5digit += 3
            tc4digit -= 1
            # 6. basamağa geçerse 00000'dan devam
            if tc5digit > 99999:
                tc5digit = tc5digit - 100000
            # Eksiye düşerse 9999'dan devam
            if tc4digit < 0:
                tc4digit = tc4digit + 10000
        else:
            # Geri iterasyon, yaşı küçükler için
            tc5digit -= 3
            tc4digit += 1
            if tc4digit > 9999:
                tc4digit = tc4digit - 10000
            if tc5digit < 0:
                tc5digit = tc5digit + 100000
        
        raw_tc = pad('00000', str(tc5digit), True) + pad('0000', str(tc4digit), True) + "00"
        print_output = print_output + pad('00000', str(tc5digit), True) + pad('0000', str(tc4digit), True) + pad('00', str(son_iki_hane(int(raw_tc))), True) + " "
        tc_sayisi -= 1

    return print_output

tc = "12345678912"  # İlk TC kimlik numarası
tc_sayisi = 10000  # Oluşturulacak TC kimlik numarası sayısı
yasli = 1  # Yaşlılara ait TC kimlik numaraları mı? (1: Evet, 0: Hayır)

print(tc_new(tc, tc_sayisi, yasli))