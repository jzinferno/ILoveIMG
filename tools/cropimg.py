from ..iloveimg import ILoveIMG

class CropIMG(ILoveIMG):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str, width: int, height: int):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'x': 0, 'y': 0,  'width': width, 'height': height}
        self.tool = 'cropimage'

        await self.execute()
