### ILoveIMG python/httpx

https://developer.iloveimg.com/docs/api-reference

### Installation

```bash
git clone --depth=1 https://github.com/jzinferno/ILoveIMG.git
pip install --upgrade httpx
```

### Usage

```python
from ILoveIMG import CompressIMG
import asyncio

project_public = 'project_public_...'

async def main():
    await CompressIMG(project_public).run('input.png', 'output.png')

asyncio.run(main())
```