import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import functools

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1UFTRhXxV0Hd0DgTNXP1yznf8v52htAPk_brnytVnxMQ'
SAMPLE_RANGE_NAME = 'Sheet1!B1:B52'

def main():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("/Users/lanza/Downloads/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    import pudb; pudb.set_trace()
    values = result.get('values', [])

    flat = [item for sublist in values for item in sublist]


    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(f"{row[0]}, {row[4]}")

if __name__ == '__main__':
    main()
