from ..iloveimg import ILoveIMG

class ResizeIMG(ILoveIMG):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str, width: int, height: int):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'resize_mode': 'pixels',  'pixels_width': width, 'pixels_height': height}
        self.tool = 'resizeimage'

        await self.execute()
