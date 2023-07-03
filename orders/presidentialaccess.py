import os
from dossier import *

class espionage:
    def intelclass(self):
        return 'sh'
    def intelsummary(self):
        return 'run a shell command'
    def intelreport(self):
        return 'run the contents after the command name in a shell'
    async def orderdronestrike(self,order,pipebomb,explosive,message):
        try:
            if message.author.id==president:
                await message.channel.send('```'+os.popen(explosive).read()+'```')
        except Exception as error:
            await message.channel.send('could not complete command\n'+str(error))
