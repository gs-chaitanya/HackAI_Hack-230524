from uagents import Agent,Context,Model

perry = Agent(name="Perry", seed="red phrase")

@perry.on_event("startup")
async def startup_func(ctx:Context):
    ctx.storage.set(f"min_range",40)
    ctx.storage.set(f"max_range",90)
    ctx.logger.info(f"min_temp: {ctx.storage.get(f'min_range')} max_temp: {ctx.storage.get(f'max_range')}")

# @perry.on_interval(period=2.0)
# async def period_func(ctx:Context):
#     ctx.logger.info(f"min_temp: {ctx.storage.get(f'{ctx.address}_min_range')} max_temp: {ctx.storage.get(f'{ctx.address}_max_range')}")

if __name__ == "__main__":
    perry.run()