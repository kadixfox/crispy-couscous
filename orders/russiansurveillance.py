import os, random, string

class pingsatellites:
    def intelclass(self):
        return 'quote'
    def intelsummary(self):
        return 'get a random quote'
    def intelreport(self):
        return 'send a randomly selected quote from the quotes database'
    async def orderdronestrike(self,order,pipebomb,explosive,message):
        try:
            intel=random.choice([secret for secret in os.listdir('russianintelligence') if os.path.isfile(os.path.join('russianintelligence',secret))])
            russianintelligence=open('russianintelligence/'+intel)
            russianintelligence.close
            await message.channel.send(russianintelligence.read())
        except Exception as error:
            await message.channel.send('could not get quote. maybe there are no quotes in the database?\n'+str(error))

class updateintelligence:
    def intelclass(self):
        return 'addquote'
    def intelsummary(self):
        return 'add a quote'
    def intelreport(self):
        return 'add a quote following the command to the quotes database. up to one attachment is accepted and will be converted to a url at the end of the quote message'
    async def orderdronestrike(self,order,pipebomb,explosive,message):
        try:
            if message.attachments:
                explosive=explosive+'\n'+message.attachments[0].url
            if len(explosive)>1900:
                await message.channel.send('your quote is too long')
                return
            if len(explosive)<1:
                await message.channel.send('you need to provide text or an attached file/image to add as a quote')
                return
            russianintelligence=random.choices(string.ascii_uppercase+string.digits, k=9)
            intel=open('russianintelligence/'+''.join(russianintelligence),'w')
            intel.write(explosive+'\nproblem? ||dm the following code to ka10#0787 for quote removal `'+''.join(russianintelligence)+'`||')
            intel.close()
            await message.channel.send('quote added')
        except Exception as error:
            await message.channel.send('could not add quote\n'+str(error))

class intelligencereport:
    def intelclass(self):
        return 'quotes'
    def intelsummary(self):
        return 'get number of quotes and total size'
    def intelreport(self):
        return 'get the number of quotes in the quotes database and the total size of all combined quotes'
    async def orderdronestrike(self,order,pipebomb,explosive,message):
        try:
            await message.channel.send(os.popen('find russianintelligence/ -type f | wc -l | tr -d \'\\n\'').read()+' quotes with a total size of '+os.popen('du -h -d0 russianintelligence/ | cut -f1 -d"	"').read())
        except Exception as error:
            await message.channel.send('could not get quote report\n'+str(error))
