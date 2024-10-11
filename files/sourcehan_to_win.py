import os, shutil
from pathlib import Path

from weiwin import run as convert
from otf2otc import run as otf2otc

# Initalize path variables and output folders
output_paths = {}
output_dir = 'output'

if Path(output_dir).exists():
    shutil.rmtree(output_dir)

for folder in ['sans', 'sans/hw', 'serif', 'serif/hw', 'rounded', 'rounded/hw', 'kai', 'ext']:
    output_paths[folder] = str(Path(output_dir) / folder)
    (Path(output_dir) / folder).mkdir(parents=True)

# Fonts location

SANS = {
    'regular': 'input/sans/ShangguSans-Regular.ttf',
    'bold': 'input/sans/ShangguSans-Bold.ttf',
    'medium': 'input/sans/ShangguSans-Medium.ttf',
    'light': 'input/sans/ShangguSans-Light.ttf',
    }
SANS_HW = {
    'regular': 'input/sans/ShangguSansHW-Regular.ttf',
    'bold': 'input/sans/ShangguSansHW-Bold.ttf',
    'light': 'input/sans/ShangguSansHW-Light.ttf',
    }

ROUNDED = SANS
ROUNDED_HW = SANS_HW

SERIF = {
    'regular': 'input/serif/ShangguSerif-Regular.ttf',
    'bold': 'input/serif/ShangguSerif-Bold.ttf',
    'heavy': 'input/serif/ShangguSerif-Heavy.ttf',
    'light': 'input/serif/ShangguSerif-Light.ttf',
    }
SERIF_HW = {
    'regular': 'input/serif/ShangguSerifHW-Regular.ttf',
    'bold': 'input/serif/ShangguSerifHW-Bold.ttf',
    'light': 'input/serif/ShangguSerifHW-Light.ttf',
    }
    
KAI = 'input/kai/LXGWWenKaiMonoTC-Regular.ttf'

EXT_P2 = 'input/ext/PlangothicP1-Regular.allideo.ttf'
EXT_P3 = 'input/ext/PlangothicP2-Regular.ttf'

# Sans/Rounded fonts

convert(['-i', SANS['regular'], '-tg', 'allsans', '-d', output_paths["sans"]])
convert(['-i', SANS['bold'], '-tg', 'msyh', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['bold'], '-tg', 'msjh', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['bold'], '-tg', 'meiryo', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['bold'], '-tg', 'malgun', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['bold'], '-tg', 'yugoth', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['bold'], '-tg', 'deng', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['medium'], '-tg', 'yugoth', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['light'], '-tg', 'malgun', '-wt', 'Semilight', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['light'], '-tg', 'msyh', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['light'], '-tg', 'msjh', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['light'], '-tg', 'yugoth', '-d', output_paths["sans"], '-r'])
convert(['-i', SANS['light'], '-tg', 'deng', '-d', output_paths["sans"], '-r'])

convert(['-i', SANS_HW['regular'], '-tg', 'gulim', '-d', output_paths["sans/hw"]])
convert(['-i', SANS_HW['regular'], '-tg', 'msgothic', '-d', output_paths["sans/hw"]])

convert(['-i', ROUNDED['regular'], '-tg', 'gulim', '-d', output_paths["rounded"]])
convert(['-i', ROUNDED_HW['regular'], '-tg', 'gulim', '-d', output_paths["rounded/hw"]])

## gulim -> ttc

shutil.move(f'{output_paths["rounded"]}/gulim.ttf', f'{output_paths["sans"]}/gulim.ttf')
shutil.move(f'{output_paths["rounded/hw"]}/gulimche.ttf', f'{output_paths["sans"]}/gulimche.ttf')
shutil.move(f'{output_paths["sans/hw"]}/dotumche.ttf', f'{output_paths["sans"]}/dotumche.ttf')

GULIM_PATHS = [f'{output_paths["sans"]}/gulim.ttf', f'{output_paths["sans"]}/gulimche.ttf', f'{output_paths["sans"]}/dotum.ttf', f'{output_paths["sans"]}/dotumche.ttf']

otf2otc(['-o', f'{output_paths["sans"]}/gulim.ttc', *GULIM_PATHS])
for file in GULIM_PATHS:
    os.remove(file)

## msgothic -> ttc

shutil.move(f'{output_paths["sans/hw"]}/msgothic.ttf', f'{output_paths["sans"]}/msgothic.ttf')

MSGOTHIC_PATHS = [f'{output_paths["sans"]}/msgothic.ttf', f'{output_paths["sans"]}/msuigothic.ttf', f'{output_paths["sans"]}/mspgothic.ttf']

otf2otc(['-o', f'{output_paths["sans"]}/msgothic.ttc', *MSGOTHIC_PATHS])
for file in MSGOTHIC_PATHS:
    os.remove(file)

## Remove redundant TTFs

os.remove(f'{output_paths["sans"]}/msjh.ttf')
os.remove(f'{output_paths["sans"]}/msjhui.ttf')
os.remove(f'{output_paths["sans"]}/msyh.ttf')
os.remove(f'{output_paths["sans"]}/msyhui.ttf')
os.remove(f'{output_paths["sans"]}/meiryo.ttf')
os.remove(f'{output_paths["sans"]}/meiryoui.ttf')
os.remove(f'{output_paths["sans"]}/YuGothR.ttf')
os.remove(f'{output_paths["sans"]}/YuGothuiSL.ttf')
shutil.rmtree(output_paths["sans/hw"])
shutil.rmtree(output_paths["rounded"])

# Serif fonts

convert(['-i', SERIF['regular'], '-tg', 'allserif', '-d', output_paths['serif']])
convert(['-i', SERIF['bold'], '-tg', 'yumin', '-d', output_paths['serif'], '-r'])
convert(['-i', SERIF['heavy'], '-tg', 'yumin', '-wt', 'Demibold', '-d', output_paths['serif'], '-r'])
convert(['-i', SERIF['light'], '-tg', 'yumin', '-d', output_paths['serif'], '-r'])

convert(['-i', SERIF_HW['regular'], '-tg', 'batang', '-d', output_paths['serif/hw']])
convert(['-i', SERIF_HW['regular'], '-tg', 'mingliu', '-d', output_paths['serif/hw']])
convert(['-i', SERIF_HW['regular'], '-tg', 'msmincho', '-d', output_paths['serif/hw']])
convert(['-i', SERIF_HW['regular'], '-tg', 'simsun', '-d', output_paths['serif/hw']])

## batang -> ttc

shutil.move(f'{output_paths["serif/hw"]}/batangche.ttf', f'{output_paths["serif"]}/batangche.ttf')
shutil.move(f'{output_paths["serif/hw"]}/gungsuhche.ttf', f'{output_paths["serif"]}/gungsuhche.ttf')

BATANG_PATHS = [f'{output_paths["serif"]}/batang.ttf', f'{output_paths["serif"]}/batangche.ttf', f'{output_paths["serif"]}/gungsuh.ttf', f'{output_paths["serif"]}/gungsuhche.ttf']

otf2otc(['-o', f'{output_paths["serif"]}/batang.ttc', *BATANG_PATHS])
for file in BATANG_PATHS:
    os.remove(file)

## mingliu -> ttc

shutil.move(f'{output_paths["serif/hw"]}/mingliu.ttf', f'{output_paths["serif"]}/mingliu.ttf')
shutil.move(f'{output_paths["serif/hw"]}/mingliu_hkscs.ttf', f'{output_paths["serif"]}/mingliu_hkscs.ttf')

MINGLIU_PATHS = [f'{output_paths["serif"]}/mingliu.ttf', f'{output_paths["serif"]}/pmingliu.ttf', f'{output_paths["serif"]}/mingliu_hkscs.ttf']

otf2otc(['-o', f'{output_paths["serif"]}/mingliu.ttc', *MINGLIU_PATHS])
for file in MINGLIU_PATHS:
    os.remove(file)

## msmincho -> ttc

shutil.move(f'{output_paths["serif/hw"]}/msmincho.ttf', f'{output_paths["serif"]}/msmincho.ttf')

MSMINCHO_PATHS = [f'{output_paths["serif"]}/msmincho.ttf', f'{output_paths["serif"]}/mspmincho.ttf']

otf2otc(['-o', f'{output_paths["serif"]}/msmincho.ttc', *MSMINCHO_PATHS])
for file in MSMINCHO_PATHS:
    os.remove(file)

## simsun -> ttc

shutil.move(f'{output_paths["serif/hw"]}/nsimsun.ttf', f'{output_paths["serif"]}/nsimsun.ttf')

SIMSUN_PATHS = [f'{output_paths["serif"]}/simsun.ttf', f'{output_paths["serif"]}/nsimsun.ttf']

otf2otc(['-o', f'{output_paths["serif"]}/simsun.ttc', *SIMSUN_PATHS])
for file in SIMSUN_PATHS:
    os.remove(file)

## Remove redundant TTFs

shutil.rmtree(output_paths["serif/hw"])

# Kai

convert(['-i', KAI, '-tg', 'allkai', '-d', output_paths['kai'], '-r'])

# Extension Planes

convert(['-i', EXT_P2, '-tg', 'allextb', '-d', output_paths['ext'], '-r'])
convert(['-i', EXT_P3, '-tg', 'simsunextg', '-d', output_paths['ext'], '-r'])
