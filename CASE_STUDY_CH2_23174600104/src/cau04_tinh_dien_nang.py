cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(
    type(dien_nang_kwh),
    type(chi_phi)
)
print(dien_nang_kwh,chi_phi)
so_phut1 = 60 
dien_nang_kwh1 = cong_suat_w * so_phut1 / 60 / 1000 
chi_phi1 = dien_nang_kwh * don_gia_kwh
print(dien_nang_kwh1,chi_phi)