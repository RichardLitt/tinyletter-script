#!/usr/bin/python

import tinyapi
import argparse
import sys
import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument('--body', help='Which file to read', type=str)
parser.add_argument('--title', help='A title for the newsletter', type=str)
parser.add_argument('--id', help='The id of a newsletter', type=int)
group = parser.add_mutually_exclusive_group()
group.add_argument('-preview', help='preview a newsletter', action='store_true')
group.add_argument('-send', help='Send a newsletter', action='store_true')
args = parser.parse_args()

session = tinyapi.Session(os.environ.get("TINYLETTER_USERNAME"), os.environ.get("TINYLETTER_PASSWORD")) #getpass())

if args.preview or args.send:
    if args.id:
        draft = session.edit_draft(message_id=args.id)

        if args.preview:
            draft.send_preview()

        if args.send:
            draft.send()
    else:
        drafts = session.get_drafts()
        for x in drafts:
            print("{0} - {1}. {2}".format(x['id'], x['subject'], datetime.datetime.fromtimestamp(x['updated_at']).strftime('%Y-%m-%d %H:%M:%S')))

else:
    draft = session.create_draft()

    if args.title and args.body:
        draft.subject = args.title
        draft.body = open(args.body, 'r+').read()
        draft.save()
        print(draft.message_id)

        draft.send_preview()
    elif (args.title and not args.body) or (args.body and not args.title):
        print('A title and a body are needed!')

if not len(sys.argv) > 1:
    print('You must pass arguments.')
    parser.print_help()




# TODO Add an option to send
