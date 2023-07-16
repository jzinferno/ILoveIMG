from ..iloveimg import ILoveIMG

class ConvertIMG(ILoveIMG):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str, to: str):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'to': to}
        self.tool = 'convertimage'

        await self.execute()
