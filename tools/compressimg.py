from ..iloveimg import ILoveIMG

class CompressIMG(ILoveIMG):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str, compression_level: str='recommended'):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'compression_level': compression_level}
        self.tool = 'compressimage'

        await self.execute()
