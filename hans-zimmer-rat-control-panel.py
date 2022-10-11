#!/usr/bin/env python3
import discord as obama
rat=obama.Client()
from dossier import *

from orders.russiansurveillance import *
from orders.propagandacampaign import *
from orders.presidentialaccess import *
orders=[pingsatellites(),
        updateintelligence(),
        intelligencereport(),
        spreadpropaganda(),
        espionage()]

@rat.event
async def on_ready():
    print('Authorized as double agent {0.user}'.format(rat))
    await rat.change_presence(activity=obama.Activity(type=obama.ActivityType.watching, name="war crimes"))

@rat.event
async def on_message(message):
    print('{0.author} in {0.guild} nation {0.channel}: {0.content}'.format(message))
    if message.author.id==rat.user.id:
        return

    # require raccoon to begin orders
    if message.content.startswith(raccoon):
        order=message.content.split(' ',1)[0][1:]
        pipebomb=message.content.split(' ')[1:]
        explosive=' '.join(pipebomb)

        # intel briefing for specific intel
        if order=='help':
            if len(pipebomb)>0:
                briefing=pipebomb[0]
                intelbriefing=None
                for intel in orders:
                    if intel.intelclass()==briefing:
                        intelbriefing=intel
                        break
                if intelbriefing==None:
                    await message.channel.send('command not found: '+briefing)
                else:
                    await message.channel.send('help for '+briefing+':\n'+intelbriefing.intelreport())

            # intel briefing for a summary of all intel
            else:
                briefingtemplate='available commands (do '+raccoon+'help <command name> for more detailed help):'
                for intel in orders:
                    briefingtemplate=briefingtemplate+'\n'+raccoon+intel.intelclass()+': '+intel.intelsummary()
                await message.channel.send(briefingtemplate)

        # execute orders
        else:
            for intel in orders:
                if intel.intelclass()==order:
                    await intel.orderdronestrike(order,pipebomb,explosive,message)

rat.run(launchcodes)
