import os

class spreadpropaganda:
    def intelclass(self):
        return 'fortune'
    def intelsummary(self):
        return 'get a fortune'
    def intelreport(self):
        return 'send a fortune from the UNIX fortune-mod'
    async def orderdronestrike(self,order,pipebomb,explosive,message):
        try:
            await message.channel.send(os.popen('fortune').read())
        except Exception as error:
            await message.channel.send('could not get fortune\n'+str(error))
