'''
获得知乎网页源码 request.urlopen()
'''
from urllib import  request
#构建请求对象
url="https://www.zhihu.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Cookie":"_zap=86bdce66-8e31-4a86-8b2d-10dfb9ec74e2; d_c0=ADAarl5vdBiPTr8lvaIlpsiVAcfgGUfW5AY=|1712910683; __snaker__id=MZKrpgwmbwsqrQT5; gdxidpyhxdE=hI7%2FybkrdH80frqgJP2K9Q%5C%2FuUPLVT2PlpM%5C4NuHJJWcw%2B9dyIhjbJYOI%2BOrlk%5CUMT%2BIEyurfD%2Bg%2FKL4sJgLS5jHbR2WNiyrNnWBa7liSpzSpyEq6TqTRtiP8a6MMi%5CB9B1Psf04WUq%2BbplQ2yo23Wpmud0Yat2XXZ%5CUe%2BaSjq4ijvH2%3A1712911583341; captcha_session_v2=2|1:0|10:1712910695|18:captcha_session_v2|88:b2M4ZFlYV3NySFhuWjhFa3I3M1lsMVFZdEZ5YUplNC94ckdIcVZ4c0tDV2NFenJvbmpUR0lqYVhlS2xEWWJ4ag==|ebc97599b3cb188877b6f6e152e607446c73443c3269e9dae7765709d2178188; q_c1=a4c3330c8a894e89b7f9c412fa2991e3|1712911155000|1712911155000; z_c0=2|1:0|10:1712911158|4:z_c0|92:Mi4xalJLR01BQUFBQUFBTUJxdVhtOTBHQmNBQUFCZ0FsVk5NMEVHWndCRFNDNnR5Nmx0M3FtSDhMaVJ3UmllNDBfeE9n|912fdb26543ebebc5d97759dc54f34700f65cebe24159e82a4db90cf382921eb; _xsrf=dad50b0b-9ca6-4b11-9792-30e46f5e8e32; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1712980688,1712987663,1712989869,1712991324; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1713000794; SESSIONID=52fGIRkunfklAEoC0aextchCUGKryaUZ1mWm571bk14; JOID=U1sUBU8ZJ3VC5o-6bh4Q5mKpcDZ7LhcUB6rf0xxyQxwppc_XL0RzaiPhj79r3tuqN8zcFtwft0dHiP7595WqpYg=; osd=Wl8VAE8QI3RH5oa-bxsQ72aodTZyKhYRB6Pb0hlyShgooM_eK0V2airljrpr19-rMszVEt0at05Difv5_pGroIg=; tst=r; KLBRSID=d017ffedd50a8c265f0e648afe355952|1713000826|1712991325"
    ,
}
req=request.Request(url,headers=headers)
#发送请求
resp=request.urlopen(req)
#获得HTML并解码
html=resp.read().decode()
with open("demo01.html", "w", encoding="utf-8") as f:
    f.write(html)
