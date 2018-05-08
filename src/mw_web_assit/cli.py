import click
from click import command
from mw_web_assit import __version__,ApiMethods,SwaggerHelper
import sys


def get_version(ctx, param, value):
    # print([ctx,param,value])
    if value:
        click.echo('mw-web-assit {ver}'.format(ver=__version__))
        sys.exit(0)



CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# @click.option('--aa' ,callback=get_bb, help="bb",expose_value=False,is_eager =False )
@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-v','--version',is_flag =True,callback=get_version,help="show version",expose_value=False,is_eager =True,required=False )
def cli():
    pass


@cli.command()
@click.argument('infile','swagger yml/json file')
@click.argument('outpath','产生的js api 及 assit 文件的目录')
@click.argument('name','文件名')
def gen(infile,outpath,name):
    '''
     web代码助手，根据设计文档产生web代码，eg.根据swagger产生api.js
    '''

    helper =SwaggerHelper(infile)
    helper.gen(outpath,name)


if __name__ =='__main__':
    cli()
    # command()