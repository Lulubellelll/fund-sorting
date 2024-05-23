import os 

try:
    PRIVATE_KEY_ID = os.environ["PRIVATE_KEY_ID"]
except KeyError:
    PRIVATE_KEY_ID = "Key not available!"
    logger.info("Key not available!")
    raise


credentials = {
        "type": "service_account",
        "project_id": "sheets-automation-terminal",
        "private_key_id": PRIVATE_KEY_ID,
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNZnIx9tWNZ3xK\nkJ74cce4ZqRVsiDpj2JjwCJBlGYhE2w/ppc1wyKnz5cM4eKWyJqXSf1PSeK/y/ZC\n5H3RgzuNAdiNTq5FDBqHxi+3MmzxPu6gEePtO/wBe/nVwJ5X5Uvq8NsfUHH4//2E\nwnpWT1pCWLsa2+8nVcLHpDaradYMwSNO/CWBWhMkffOI/lRMtmsEip3ltPtEh9HO\nbh1GQ+otkaBMmJiKzKBc204p+0CLD3Bu0edJoFQUB2gpN1KKMnk4KmNsiyalIOcA\nlPopBlVUyvR45QRiJLtupVDxLIN2J8uZ1Rp1LcTORHUlNRIVkVctnARio+UlC7KL\nYir1E0XDAgMBAAECggEAIELOfd2EljSiV33WkjQgx+xLNHCJbdXJANzdJIq/7cME\ntgye5GFVUKEw2uOhuMgiS8/huvHibPiGoeQMhPtFP7UCA9PPWGX5xsiQlwgTB2M4\njKiysYDB6KPFzlZ2KF0J6wlQiV8Tv6XJdnArUeIdzZztKl9P9VApizzWH188sPze\n2Zn0e9bFguCm+Y+/J1AtqdIT34HTx6m6EuLSLeKURdd6LaDzugKokBWdTkaEPUBH\nM3iOIPUpUFdsbpoKRd/uhGvffGlvZbzkqWRyIeI3TIxi6sQphCEqCpitehQ4BJYI\n/v1d+rCceCI8WAqnRwiEPvZo1IqRc2fLQSsI77xs2QKBgQDo49fpMB0Xb44Kj+dc\n8Gc5tSzHkb6Y13Gt/t6MauSPTlap51SUEfy1Sdy1gqL3HUFNUYmouvvuvWwOCdHl\nISOLnx3v5o5U9PH65F7wc3IkIjI5EzLn5wCT34wL6dGZzZ6GzK5yfg3a7SYjO32w\n/K2I9pBV4Zd9RFjMMJp0O8r2ywKBgQDhyEW4lfKmfF26PKGci8pcuILdKkZ1fUB5\nq//NhbarelOFa7D9P4Owj7N3cUTzMqBgn9GclzC0vGTkaXjtusa4d3Owb36bt0OX\ngfB8+U3Hzd5FAw8hddCGUeNWS2tsjelW+xO0tbbSOMrxkmXI/L34oaW1BXJfjAKa\nucbNrA4V6QKBgQDngt/26qJw0q+UJlur0zv6bPV36pVbIQjcG/omAnj1UL3sJo+4\npmzd1vA17AiOuSFaeEztU/vv55PMHMzwBtJsEKBVBI/HOrx2WaFbTJhR/UCJ5mD7\nkXLMjTSN/0EisPn/LOfZ3x9s28TGz3Pyhi0Ic3smNJ1ApLnVOhfAplPsowKBgA0v\nN7sOrovASWzdq4ZLt3Zwo9usY07rEH/KZnam70LWMthgsIYpVlRSH+XCrIcTFsBt\ntLzTK1nygmXALvqa5I3TE+Nir18CdaT8RoHVwRAA2pDnG9QVYCbn00Gvx8cgBlc4\n9C6iSdm+zUMMDHuPHrzNG7MVbVddAq3sWUqbWHs5AoGAduBsM6nLfEjJhjjzAf8s\nLcQ0UEfpfQtwLC9nX60CFzmhZATC1RU/MCb9ssrRa3kMrMoPm+ntXCIco2nv2qpt\nA9Q3aBEhLxpOQ34EeE2Zayqy0mB1zPMi+NV9rlbd6Ghd6qipd/y5EIUyXUsZcUCl\n5BwKRwqJpwOFzq5VT1eCrY0=\n-----END PRIVATE KEY-----\n",
        "client_email": "sat-service-account@sheets-automation-terminal.iam.gserviceaccount.com",
        "client_id": "100596045666848406610",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sat-service-account%40sheets-automation-terminal.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
}
