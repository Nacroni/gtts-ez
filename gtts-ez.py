#!/usr/bin/env python3
import os, argparse, logging, gtts
from pydub import AudioSegment
from pydub.playback import play

# argparse
parser = argparse.ArgumentParser('gtts-ez', description='Easy to use Google TTS audio player.', epilog='by Nacroni')
parser.add_argument('INPUT', help='Input for gtts')
parser.add_argument('-l', '--lang', help='Language for TTS', default='en')
parser.add_argument('-s', '--slow', help='Speak slowly', action='store_true', default=False)
parser.add_argument('-f', '--save_file', help='Save the MP3 file.', action='store_true')
parser.add_argument('--tld', help='TLD for Google Translate URL', default='com')
parser.add_argument('--lang_chk', help='Check language', action='store_true', default=True)
parser.add_argument('--debug', '-d', help='show debug-level messages', action='store_true')
args = parser.parse_args()

if args.debug: 
  logging_level = logging.DEBUG  
else: 
  logging_level = logging.INFO

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging_level)

# Arguments and stuff
tts_input = args.INPUT
tts_tld = args.tld
tts_lang = args.lang
tts_slow = args.slow
tts_lc = args.lang_chk

# Garbage code because of course it is
tts_out = gtts.gTTS(f'{tts_input}', tts_tld, tts_lang, tts_slow, tts_lc)
if args.save_file:
  logging.info('Not adding hidden prefix')
  tts_out_filename = 'gtts_output.mp3'
else:
  tts_out_filename = '.gtts_output.mp3'
tts_out.save(tts_out_filename)

tts_out_as = AudioSegment.from_mp3(tts_out_filename)
play(tts_out_as)

if args.save_file:
  logging.info('Not removing temp audio file')
else:
  os.remove(tts_out_filename)
  logging.debug(f'Removed {tts_out_filename}')

exit()