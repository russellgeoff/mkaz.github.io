---
id: 1007
title: Hands on Introduction to Dogecoin
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=1007
permalink: /2014/02/13/hands-on-introduction-to-dogecoin/
publicize_google_plus_url:
  - https://plus.google.com/115308324500133456489/posts/66dWogRorYS
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/JbCtpoYGLs
categories:
  - technology
tags:
  - bitcoin
  - cryptocurrency
  - dogecoin
---
This week's newsletter I try to figure out what is going on in the world of crypto-currency, specifically Dogecoin. I learn by doing, so here are my sad attempts at mining Dogecoin and how I spent and lost money along the way, I like to think I did it for you the reader.

I have a degree in math and stats so crypto-currencies interested me from the math and technical side; but I didn't really see much practicality in them and a little too much anarchy.

However, Dogecoin came along and dismissed the notions of being practical and trying to be a legitimate alternative-currency and was having fun with it. A lot less overthrow-the-governments and a lot more &#8220;to the moon&#8221; silliness. They made it approachable and set a fairly low bar so most people can participate.

I started to read a bit more about Dogecoin and even made a sad first attempt to use it. I downloaded the wallet, scratched my head while it took hours to sync and then it didn't really do anything. It wasn't until last week my coworkers [@TooTallNate][1] and [@rauchg][2] were playing with it that I got anywhere. Nate gave me a couple of pointers and got me started.

So let's get on with it, here are a few pointers, hopefully this article will be a good introduction to crypto-currencies and help you avoid the dumb mistakes I made and get you started in the fun world of Dogecoin.

## Background

Crypto-currencies are a currency based on solving a very complex mathematical cryptographic problem, the exact math isn't necessary to understand, but similar to how SSL and web security works; basically all around cryptographic keys and probably prime numbers.

The way coins are generated is to run a program on your computer to solve these crypto problems, this is called mining. If you are able to discover a block, you are awarded, if you're mining Bitcoin you are awarded 1 coin, if mining Dogecoin awarded between 0 and 500,000 coins.

Relatively simple in concept, but finding those blocks is quite difficult and computationally intense. The probability of finding a block is a 1 in `( d * 2^32 )` chance where `d` is an increasing difficulty level, as more blocks are found, d is increased to slow down the production of coins and attempt to maintain their value by not flooding the market.

A single individual's chance of finding a coin is pretty slim, my iMac rate for solving is around 28,000 hashes a second. This is how many crypto hashes it can check per second. This sounds like a lot, but the overall network right now is running at 234 GH/s (giga-hashes a second) or 10 million times more than my little computer.

A new block on the network is found every minute or so, I would have to get lucky or wait a million minutes, which is a long time. So people join a pool and combine their resources to mine the coins and when a block is found, it is divided up amongst those in the pool based on how much computing power you contributed.

After the coins are mined, they are delivered to your Dogecoin address, and you can then send the coins to other people in various ways. I'll explain below how to actually do all of this.

## Dogecoin Wallet

The first thing you need is to download a Dogecoin wallet, this will give you a Dogecoin address. You can download a wallet for most platforms at [Dogecoin.com][3], you can even get mobile or online wallets. Unfortunately they don't have a pre-built binary for Linux, here's [a guide on dogecoin and linux][4], the quick install

<pre class="brush: plain; title: ; notranslate" title="">sudo add-apt-repository ppa:cwayne18/doge
sudo apt-get update &amp;&amp; sudo apt-get install dogecoin-qt
</pre>

Once you have your wallet installed, run it and you were see something like this.

![Dogecoin Wallet][5]

The wallet will need to synchronize with the network, this takes a few hours. What it is doing is downloading what is called the **block chain** which is a record of every transaction, ever.

The **way you receive money** is your wallet checks your address against these transactions and if there is a match, confirms you by using your crypto private key (held in your wallet) and then the coins are deposited in your wallet.

To get your Dogecoin address, go to the **Much Receive** tab and it will list your address. You can copy it from there, for example here is my Doegcoin address:

<pre class="brush: plain; title: ; notranslate" title="">DQpwDDrW8gqJJWiW7TvXgNtbfD5Du94wy3
</pre>

You can send money using the **Pls Send** tab, where you can enter in someone else's address and how much you want to send them. Note, you'll need coins in your wallet to do so. If you have coin and want to test sending some, my address is above ;-)

**Important** Don't start two wallets and confuse the addresses, which I did. After my first successful mine, I some how used an old wallet address due to browser auto-complete and sent 600 coins to a deleted wallet, they are lost forever.

Your wallet on your computer is the only record of the coins you hold, if you lose it, they're gone. You can back it up and encrypt your wallet, which I would recommend.

## So how to mine some coin!

As mentioned in the background section above, to mine coin you will want to join a mining pool. You want a pool that has a fair amount of activity and horsepower to actually receive some coins in a reasonable time.

The [first pool I joined][6] it took 8 days and then after we finally discovered a block just last night, and I had 2,700 coins coming my way. It turned out to be an orphan block already claimed by another pool. No coins for you!

During that time, I realized that pool didn't have much fire power and joined a larger pool at [Dogechain Info][7] which has netted results, its a larger pool so I get a smaller cut, but at least its something.

You can find a [large list of pools available here][8], and to join you can simply follow the registration instructions on the pool, some require email verification.

Once you have joined a pool, you need to create some workers. Click the &#8220;My Workers&#8221; link and add a worker. Use a simple worker name and password, the worker is the info you feed the mining program to identify who should get credit for the mining being done.

The last bit of info you need is the URL for the mining, this is typically found under the &#8220;Getting Started&#8221; link on the mining pool. For my pool it looks like `stratum+tcp://stratum2.dogechain.info:3333`

## Mining Locally

Now with a worker setup and a URL, now we just need a miner to do some work. There are two main ways to mine, GPU mining using your powerful video card, this is fastest! Or CPU mining using your processors, this is a bit slower but better if you have a laptop and a weak video card. People warn about over-heating and burning both up, but my guess is that's over-clockers pushing things to the edge.

There are various mining applications, the ones I've used are [cgminer][9] for GPU mining, [minerd][10] for CPU mining. On a Mac, there is an easy front-end called [Asteroid][11] which bundles it all up making it easy just edit the config and enter your pool info.

![Asteroid Miner][12]

So download one of the miners above, and for the command-line miners you configure using your pool url and worker credentials like so

<pre class="brush: plain; title: ; notranslate" title="">./minerd -o stratum+tcp://stratum2.dogechain.info:3333 -u user.worker -p password
</pre>

**Note:** I initially confused the worker username, your user is prepended with a dot to the name you give. So if your username is &#8220;marcus&#8221; and your worker name &#8220;mac&#8221; &#8211; you would pass &#8220;marcus.mac&#8221;

Once configured or running, your miner will report how many hashes it is, you can confirm the pool is receiving it by going to the dashboard. You can see your hash rate there.

![Hashrate Graph][13]  
And then you wait&#8230; and wait&#8230; and wait&#8230; you might get refresh crazy. It takes hours sometimes days. Patience helps.

When the pool eventually finds a block, you will see it show up in the dashboard as Unconfirmed balance, and once the block is confirmed it will be deposited into your account. Woo hoo!

**Transferring coins out**: In the account settings, you can enter in your dogecoin address and transfer the coins to your wallet. You don't need your wallet running, the next time you start it up, it will sync the block chain and see your transaction and deposit the coins.

That's it to mining.

## Using EC2 to Mine Coins &#8211; no profit here

Now for those who are impatient like myself and didn't want to wait so long. You can build yourself some [crazy powerful mining rig][14] or in the age of cloud computing you can turn to Amazon and EC2 which I did.

I figured it would be cheaper to spend a little money on Amazon and learn how to mine than ordering a new computer. It was cheaper than a new computer, but by no means cost effective. I've spent around $120 on EC2 and netted about $4.00 in Dogecoin.

The mining aspect is the same for EC2 as it is locally, it really helps if you have previous EC2 experience. You basically spin up an EC2 instance and install and configure a miner. I then setup an init script to start the miner on boot and confirmed by rebooting.

I then saved this whole instance as a new AMI. So then anytime I spin up a new instance and pick this AMI, the miner would automatically start. So I don't even need to login to the boxes, just start and stop instances.

A couple of tips on EC2, I found the c1.xlarge with 8-cores is a pretty good bargain when buying on Spot Instances. I was able to get them for around 7 cents per hour. On-demand pricing, for these instances is $0.66/hr. Familiarize yourself with [EC2 pricing][15]. Also, since lazy, I would spin 10 or 20 of them up at a time instead of waiting. Much power!

EC2 also has a GPU instance which is more expensive, around 65 cents an hour. I found the 10x CPU would net me about the same hashes per second as a GPU instance, which is funny since it matches the pricing. Spot pricing on GPU instances was much harder to get a bargain.

The GPU instance is a little trickier to setup, you can search Community AMIs and find a Doge one already setup for GPU mining. [See this post for more][16] make sure you configure it for your own pool. Also, once configured save your own AMI, and you can spin up without needing to configure each time.

#### EC2 Results

If I spin up around 10x c1.xlarge instances with 8-cores each, I would get around 556 KH/s for comparison the pool combined was doing 2.6 GH/s so 4,000 times more which means I would get 1/4,000th of a block when found or around 12 coins. The current conversion is roughly 500 dogecoins is worth a $1.00 USD, so those 12 coins are worth about 2 cents.

Now, a lot of the finding is based on luck to a certain degree, the more horse power you have searching the better luck you'll have, I've seen several blocks found in an hour and I've seen no blocks found for 6 hours or more.

At peak mining, I launched 5x GPU instances and 20x CPU instances which was costing me about $5/hr and netted around 1,700 coins overnight, roughly 8-hours or so. The math, I spent around $40 on EC2 and got around $3 in Dogecoins.

No money to be made, but a great learning experience.

### Summary

I hope you found this guide useful and good intro to Dogecoin. If you are curious, I recommend trying it out, the best way to learn is by your own experience and dive in.

One of the most exciting things about Dogecoin is the community around it and the relatively low value of the coin. People are actually using and sending dogecoin to each other. In contrast, Bitcoin seems to be more greed, hording and speculation of people trying to get rich.

The Dogecoin community is having fun and using it as micro-payments and a reward system. For example, a tip bot is setup on reddit which allows you to reward a good post or comment. I read the amount of Dogecoins transacted in a week is more than the total value which is crazy active!

See further resources below to dive deeper into the world of Dogecoin and if you found this guide helpful, once you're setup you can throw me a bone to my doge address: DNYJ2ANdx1GL4sbCyikaVgYrf2GfiCtf8N

## Further Resources

  * [Dogecoin on Reddit][17] &#8211; the best community and resouces. Hunt around for links in header and sidebar, they have a [mining guide][18] and everything else you'll need.

  * [Doge Education][19] &#8211; a reddit for newcomers to the world of doge.

  * [DogePay][20] &#8211; calculate price of doge &#8211; one of many sites. The common way people calculate or convert is to convert Dogecoin to Bitcoin and then Bitcoin to dollars.

 [1]: https://twitter.com/tootallnate
 [2]: https://twitter.com/rauchg
 [3]: http://dogecoin.com/
 [4]: http://www.reddit.com/r/dogecoin/comments/1tvmnd/dogecoin_on_linux_the_complete_beginners_guide/
 [5]: http://ebeab.files.wordpress.com/2014/02/doge-wallet.png
 [6]: http://doge-pool.com/
 [7]: http://pool.dogechain.info
 [8]: http://www.doktorrf.com/dogecoin/pools.html
 [9]: https://github.com/ckolivas/cgminer
 [10]: http://sourceforge.net/projects/cpuminer/
 [11]: http://www.asteroidapp.com/
 [12]: http://ebeab.files.wordpress.com/2014/02/asteroid-miner.png
 [13]: http://ebeab.files.wordpress.com/2014/02/hashrate-graph.png
 [14]: http://bitcoinexaminer.org/20-insane-bitcoin-mining-rigs/
 [15]: http://aws.amazon.com/ec2/pricing/
 [16]: http://www.reddit.com/r/dogecoin/comments/1tvj41/free_release_cloud_computing_doges_an_open_ami/
 [17]: http://www.reddit.com/r/dogecoin
 [18]: http://www.reddit.com/r/dogecoin/wiki/index/mining
 [19]: http://www.reddit.com/r/dogeducation
 [20]: http://dogepay.com/