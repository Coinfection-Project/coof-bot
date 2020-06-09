from bot import client
import time
import discord

BLOCK_TIME = 60 # secconds

# network param vars
bCount = 0
eNum = 0
EInfectCount = 0
InfectCount = 0
InfectedTokenClumps = 0
InfectProb = "50%"
lBlockHash = "0000000000000000000000000000000000000000000000000000000000000000"
lBlockAlgo = None
LBAD = 1
AvgDiff = 1
POWreward = 50
LBTXNC = 1
MempoolTxnC = 0
NetHash = "1 H/s"
coins = 0
active_wallets = 0
NextEpochHeight = 10
TimeToEpoch = str(10 * BLOCK_TIME) + " secconds"
EBlock = 0

# bot params
update_channel = None
msg = None
update_interval = 5 # secs

# node params
node_addr = "127.0.0.1"
node_port = "1234"
node == None

def update_stats(node):
  return True # TODO
  
def connect_node():
  return None # TODO

def gen_embed():
  embed=discord.Embed(title="Coinfection Network Stats", color=0xff0000)
  embed.add_field(name="Block Count", value=bCount, inline=True)
  embed.add_field(name="Epoch number", value=eNum, inline=True)
  embed.add_field(name="Infections This Epoch", value=EInfectCount, inline=True)
  embed.add_field(name="Total Infections", value=InfectCount, inline=True)
  embed.add_field(name="Infected Token Clumps", value=InfectedTokenClumps, inline=True)
  embed.add_field(name="Infection Prob", value=InfectProb, inline=True)
  embed.add_field(name="Last Block Hash", value=lBlockHash, inline=False)
  embed.add_field(name="Last Block Mined Algo", value=lBlockAlgo, inline=True)
  embed.add_field(name="Last Mined Algo Diff", value=LBAD, inline=True)
  embed.add_field(name="Avg. diff", value=AvgDiff, inline=True)
  embed.add_field(name="Last PoW reward", value=POWreward + " COOF", inline=True)
  embed.add_field(name="Txn in last Block", value=LBTxnC, inline=True)
  embed.add_field(name="Txn in mempool", value=MempoolTxnC, inline=True)
  embed.add_field(name="Est. total hash rate", value=NetHash, inline=True)
  embed.add_field(name="Coins in circulation", value=coins + " COOF", inline=True)
  embed.add_field(name="Active Wallet Count", value=active_wallets, inline=True)
  embed.add_field(name="Next Epoch Height", value=NextEpochHeight, inline=True)
  embed.add_field(name="Est Time to Next Epoch", value=TimeToEpoch, inline=True)
  embed.add_field(name="Epoch Block", value=EBlock + "/10", inline=True)
  return embed
  
async def on_ready_stats():
    for server in client.servers:
      if server.name == "Coinfection":
        for channel in server.channels:
          if channel.name == "blockchain-status":
            update_channel = channel
    if update_channel == None:
      print("Channel not found... ")
    node = connect_node()
    else:
      while True:
        if msg == None:
          # create a new one
          update_stats(node) # update the stats vars
          message = gen_embed() # get the stuff to send
          await update_channel.send(embed=message)
        else:
          # edit the old one
          update_stats(node) # update the stats vars
          message = gen_embed() # get the stuff to send
          await msg.edit(embed=message)
        time.sleep(update_interval)
