---
id: 1082
title: The ★ Bash Prompt
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=1082
permalink: /2014/04/17/the-bash-prompt/
geo_latitude:
  - 0.000000
geo_longitude:
  - 0.000000
geo_accuracy:
  - 0
geo_address:
  - '           '
geo_public:
  - 0
publicize_google_plus_url:
  - https://plus.google.com/115308324500133456489/posts/jnec68wDAeM
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/7lZBOF5CMB
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
categories:
  - technology
tags:
  - bash
  - command-line
  - linux
  - prompt
  - unicode
---
I know you already love the command-line, the power of the whole world at your finger tips brings a smile to your face. Now make your time on the command-line extra special using a **unicode bash prompt**

Most modern terminal clients support UTF-8 characters, which means they can display the wide range of unicode characters, depending on fonts installed on your system. I do see quite a bit of difference in design and availability of characters between Linux and Mac clients.

Here's what my current bash prompt looks like, relatively simple but still a touch of fancy:

<pre style="background:#002B36;"><code>
&lt;span style="color:#2AA198;">limbo:&lt;/span> &lt;span style="color:#859900;">~&lt;/span> &lt;span style="color:#CB4B16;">&#x25ba;&lt;/span>
</code></pre>

Here's how I set my bash prompt, I source this [colors file ][1] and set using color names:

    
    source ~/dotfiles/extras/colors
    FANCY="342226270"   # my fancy unicode prompt
    export PS1="[$Cyan]h: [$Red]W [$Yellow]$FANCY [$Color_Off] "
    

Where the FANCY variable is the **unicode character** that I want. I've seen various different ways to get unicode to show in the terminal, including the simpliest copy-and-paste. I've found converting the character to octal to be the most portable especially for use within a prompt.

To get the octal number, copy and paste the character you want and echo into hexdump like so:

    
    echo &#x25b8; | hexdump -b
    

Which outputs the following, use the three bold parts:

    
    0000000 <b>342 226 270</b> 012                                                
    0000004
    

So in simpliest form it can be used, like so:

    
    export PS1="\342\226\270"
    

#### Other Parameters within Prompt 

You can put just about anything within the prompt, I used to include the time and more but found simple works well for me. Here are a few common ones you can include:

    
    D{format} : date formatted using strftime
    h         : short hostname 
    H         : full hostname
    t         : current time in 24-hour HH:MM:SS format
    T         : current time in 12-hour HH:MM:SS format
    u         : username of the current user
    w         : current working directory (long)
    W         : basename of current working directory (short)
    

Additionally, you can include the output of any command within your prompt, be selective because this will run everytime the prompt shows. See [Bash Prompt HOWTO][2] for more info.

#### Unicode Character Table 

Here is a table of unicode characters I think would work well in a command-line prompt, there are 10,000 or so unicode characters. You can [browse them all][3] if you didn't find something you like below.

<div class="unicode">
  <dl>
    <dt>
      &#x2010;
    </dt>
    
    <dd>
      2010
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2011;
    </dt>
    
    <dd>
      2011
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2022;
    </dt>
    
    <dd>
      2022
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2023;
    </dt>
    
    <dd>
      2023
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2039;
    </dt>
    
    <dd>
      2039
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2039;
    </dt>
    
    <dd>
      2039
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x203b;
    </dt>
    
    <dd>
      203b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x203b;
    </dt>
    
    <dd>
      203b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2043;
    </dt>
    
    <dd>
      2043
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x204e;
    </dt>
    
    <dd>
      204e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2051;
    </dt>
    
    <dd>
      2051
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2052;
    </dt>
    
    <dd>
      2052
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2053;
    </dt>
    
    <dd>
      2053
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2055;
    </dt>
    
    <dd>
      2055
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2056;
    </dt>
    
    <dd>
      2056
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2058;
    </dt>
    
    <dd>
      2058
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2059;
    </dt>
    
    <dd>
      2059
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x205a;
    </dt>
    
    <dd>
      205a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x205c;
    </dt>
    
    <dd>
      205c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x205d;
    </dt>
    
    <dd>
      205d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x205e;
    </dt>
    
    <dd>
      205e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2192;
    </dt>
    
    <dd>
      2192
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21a3;
    </dt>
    
    <dd>
      21a3
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21a6;
    </dt>
    
    <dd>
      21a6
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21aa;
    </dt>
    
    <dd>
      21aa
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21b1;
    </dt>
    
    <dd>
      21b1
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21b3;
    </dt>
    
    <dd>
      21b3
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21c9;
    </dt>
    
    <dd>
      21c9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21d2;
    </dt>
    
    <dd>
      21d2
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21db;
    </dt>
    
    <dd>
      21db
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21dd;
    </dt>
    
    <dd>
      21dd
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21e2;
    </dt>
    
    <dd>
      21e2
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21e8;
    </dt>
    
    <dd>
      21e8
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x21fe;
    </dt>
    
    <dd>
      21fe
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2217;
    </dt>
    
    <dd>
      2217
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x221e;
    </dt>
    
    <dd>
      221e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2234;
    </dt>
    
    <dd>
      2234
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2235;
    </dt>
    
    <dd>
      2235
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x226b;
    </dt>
    
    <dd>
      226b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x227b;
    </dt>
    
    <dd>
      227b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2299;
    </dt>
    
    <dd>
      2299
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229a;
    </dt>
    
    <dd>
      229a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229b;
    </dt>
    
    <dd>
      229b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229c;
    </dt>
    
    <dd>
      229c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229d;
    </dt>
    
    <dd>
      229d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229e;
    </dt>
    
    <dd>
      229e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x229f;
    </dt>
    
    <dd>
      229f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22a0;
    </dt>
    
    <dd>
      22a0
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22a1;
    </dt>
    
    <dd>
      22a1
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22a2;
    </dt>
    
    <dd>
      22a2
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22a6;
    </dt>
    
    <dd>
      22a6
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22b3;
    </dt>
    
    <dd>
      22b3
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22b9;
    </dt>
    
    <dd>
      22b9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x22d9;
    </dt>
    
    <dd>
      22d9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2316;
    </dt>
    
    <dd>
      2316
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x233e;
    </dt>
    
    <dd>
      233e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x235f;
    </dt>
    
    <dd>
      235f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x23e9;
    </dt>
    
    <dd>
      23e9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x254c;
    </dt>
    
    <dd>
      254c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x254d;
    </dt>
    
    <dd>
      254d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25b6;
    </dt>
    
    <dd>
      25b6
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25b7;
    </dt>
    
    <dd>
      25b7
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25b8;
    </dt>
    
    <dd>
      25b8
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25b9;
    </dt>
    
    <dd>
      25b9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ba;
    </dt>
    
    <dd>
      25ba
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25bb;
    </dt>
    
    <dd>
      25bb
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25c6;
    </dt>
    
    <dd>
      25c6
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25c7;
    </dt>
    
    <dd>
      25c7
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25c8;
    </dt>
    
    <dd>
      25c8
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25c9;
    </dt>
    
    <dd>
      25c9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ca;
    </dt>
    
    <dd>
      25ca
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25cb;
    </dt>
    
    <dd>
      25cb
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25cc;
    </dt>
    
    <dd>
      25cc
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25cd;
    </dt>
    
    <dd>
      25cd
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ce;
    </dt>
    
    <dd>
      25ce
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25cf;
    </dt>
    
    <dd>
      25cf
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ec;
    </dt>
    
    <dd>
      25ec
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ed;
    </dt>
    
    <dd>
      25ed
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ee;
    </dt>
    
    <dd>
      25ee
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x25ef;
    </dt>
    
    <dd>
      25ef
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2600;
    </dt>
    
    <dd>
      2600
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2601;
    </dt>
    
    <dd>
      2601
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2602;
    </dt>
    
    <dd>
      2602
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2603;
    </dt>
    
    <dd>
      2603
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2604;
    </dt>
    
    <dd>
      2604
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2605;
    </dt>
    
    <dd>
      2605
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2606;
    </dt>
    
    <dd>
      2606
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2609;
    </dt>
    
    <dd>
      2609
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x260a;
    </dt>
    
    <dd>
      260a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x260b;
    </dt>
    
    <dd>
      260b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2614;
    </dt>
    
    <dd>
      2614
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2615;
    </dt>
    
    <dd>
      2615
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2618;
    </dt>
    
    <dd>
      2618
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x261e;
    </dt>
    
    <dd>
      261e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2620;
    </dt>
    
    <dd>
      2620
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2622;
    </dt>
    
    <dd>
      2622
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2623;
    </dt>
    
    <dd>
      2623
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2624;
    </dt>
    
    <dd>
      2624
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2625;
    </dt>
    
    <dd>
      2625
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2626;
    </dt>
    
    <dd>
      2626
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2629;
    </dt>
    
    <dd>
      2629
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262a;
    </dt>
    
    <dd>
      262a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262b;
    </dt>
    
    <dd>
      262b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262c;
    </dt>
    
    <dd>
      262c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262d;
    </dt>
    
    <dd>
      262d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262e;
    </dt>
    
    <dd>
      262e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x262f;
    </dt>
    
    <dd>
      262f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2638;
    </dt>
    
    <dd>
      2638
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2639;
    </dt>
    
    <dd>
      2639
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263a;
    </dt>
    
    <dd>
      263a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263b;
    </dt>
    
    <dd>
      263b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263c;
    </dt>
    
    <dd>
      263c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263d;
    </dt>
    
    <dd>
      263d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263e;
    </dt>
    
    <dd>
      263e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x263f;
    </dt>
    
    <dd>
      263f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2640;
    </dt>
    
    <dd>
      2640
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2641;
    </dt>
    
    <dd>
      2641
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2642;
    </dt>
    
    <dd>
      2642
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2654;
    </dt>
    
    <dd>
      2654
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2655;
    </dt>
    
    <dd>
      2655
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2656;
    </dt>
    
    <dd>
      2656
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2657;
    </dt>
    
    <dd>
      2657
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2658;
    </dt>
    
    <dd>
      2658
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2659;
    </dt>
    
    <dd>
      2659
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265a;
    </dt>
    
    <dd>
      265a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265b;
    </dt>
    
    <dd>
      265b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265c;
    </dt>
    
    <dd>
      265c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265d;
    </dt>
    
    <dd>
      265d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265e;
    </dt>
    
    <dd>
      265e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x265f;
    </dt>
    
    <dd>
      265f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2660;
    </dt>
    
    <dd>
      2660
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2661;
    </dt>
    
    <dd>
      2661
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2662;
    </dt>
    
    <dd>
      2662
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2663;
    </dt>
    
    <dd>
      2663
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2664;
    </dt>
    
    <dd>
      2664
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2665;
    </dt>
    
    <dd>
      2665
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2666;
    </dt>
    
    <dd>
      2666
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2667;
    </dt>
    
    <dd>
      2667
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2668;
    </dt>
    
    <dd>
      2668
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2669;
    </dt>
    
    <dd>
      2669
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266a;
    </dt>
    
    <dd>
      266a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266b;
    </dt>
    
    <dd>
      266b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266c;
    </dt>
    
    <dd>
      266c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266d;
    </dt>
    
    <dd>
      266d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266e;
    </dt>
    
    <dd>
      266e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x266f;
    </dt>
    
    <dd>
      266f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2670;
    </dt>
    
    <dd>
      2670
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2671;
    </dt>
    
    <dd>
      2671
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2690;
    </dt>
    
    <dd>
      2690
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2691;
    </dt>
    
    <dd>
      2691
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2692;
    </dt>
    
    <dd>
      2692
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2693;
    </dt>
    
    <dd>
      2693
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2694;
    </dt>
    
    <dd>
      2694
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2695;
    </dt>
    
    <dd>
      2695
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2696;
    </dt>
    
    <dd>
      2696
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2698;
    </dt>
    
    <dd>
      2698
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2699;
    </dt>
    
    <dd>
      2699
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x269a;
    </dt>
    
    <dd>
      269a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x269b;
    </dt>
    
    <dd>
      269b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x269c;
    </dt>
    
    <dd>
      269c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x26bd;
    </dt>
    
    <dd>
      26bd
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x26be;
    </dt>
    
    <dd>
      26be
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x26c4;
    </dt>
    
    <dd>
      26c4
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x26c5;
    </dt>
    
    <dd>
      26c5
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x270b;
    </dt>
    
    <dd>
      270b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x270c;
    </dt>
    
    <dd>
      270c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x270d;
    </dt>
    
    <dd>
      270d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x270e;
    </dt>
    
    <dd>
      270e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x270f;
    </dt>
    
    <dd>
      270f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2710;
    </dt>
    
    <dd>
      2710
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2711;
    </dt>
    
    <dd>
      2711
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2712;
    </dt>
    
    <dd>
      2712
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2713;
    </dt>
    
    <dd>
      2713
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2714;
    </dt>
    
    <dd>
      2714
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2715;
    </dt>
    
    <dd>
      2715
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2716;
    </dt>
    
    <dd>
      2716
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2717;
    </dt>
    
    <dd>
      2717
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2718;
    </dt>
    
    <dd>
      2718
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2719;
    </dt>
    
    <dd>
      2719
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271a;
    </dt>
    
    <dd>
      271a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271b;
    </dt>
    
    <dd>
      271b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271c;
    </dt>
    
    <dd>
      271c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271d;
    </dt>
    
    <dd>
      271d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271e;
    </dt>
    
    <dd>
      271e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x271f;
    </dt>
    
    <dd>
      271f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2720;
    </dt>
    
    <dd>
      2720
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2721;
    </dt>
    
    <dd>
      2721
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2722;
    </dt>
    
    <dd>
      2722
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2723;
    </dt>
    
    <dd>
      2723
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2724;
    </dt>
    
    <dd>
      2724
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2725;
    </dt>
    
    <dd>
      2725
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2726;
    </dt>
    
    <dd>
      2726
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2727;
    </dt>
    
    <dd>
      2727
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2728;
    </dt>
    
    <dd>
      2728
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2729;
    </dt>
    
    <dd>
      2729
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272a;
    </dt>
    
    <dd>
      272a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272b;
    </dt>
    
    <dd>
      272b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272c;
    </dt>
    
    <dd>
      272c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272d;
    </dt>
    
    <dd>
      272d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272e;
    </dt>
    
    <dd>
      272e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x272f;
    </dt>
    
    <dd>
      272f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2730;
    </dt>
    
    <dd>
      2730
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2731;
    </dt>
    
    <dd>
      2731
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2732;
    </dt>
    
    <dd>
      2732
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2733;
    </dt>
    
    <dd>
      2733
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2734;
    </dt>
    
    <dd>
      2734
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2735;
    </dt>
    
    <dd>
      2735
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2736;
    </dt>
    
    <dd>
      2736
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2737;
    </dt>
    
    <dd>
      2737
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2738;
    </dt>
    
    <dd>
      2738
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2739;
    </dt>
    
    <dd>
      2739
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273a;
    </dt>
    
    <dd>
      273a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273b;
    </dt>
    
    <dd>
      273b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273c;
    </dt>
    
    <dd>
      273c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273d;
    </dt>
    
    <dd>
      273d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273e;
    </dt>
    
    <dd>
      273e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x273f;
    </dt>
    
    <dd>
      273f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2740;
    </dt>
    
    <dd>
      2740
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2741;
    </dt>
    
    <dd>
      2741
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2742;
    </dt>
    
    <dd>
      2742
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2743;
    </dt>
    
    <dd>
      2743
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2744;
    </dt>
    
    <dd>
      2744
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2745;
    </dt>
    
    <dd>
      2745
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2746;
    </dt>
    
    <dd>
      2746
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2747;
    </dt>
    
    <dd>
      2747
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2748;
    </dt>
    
    <dd>
      2748
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2749;
    </dt>
    
    <dd>
      2749
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x274a;
    </dt>
    
    <dd>
      274a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x274b;
    </dt>
    
    <dd>
      274b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2763;
    </dt>
    
    <dd>
      2763
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2764;
    </dt>
    
    <dd>
      2764
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2799;
    </dt>
    
    <dd>
      2799
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279a;
    </dt>
    
    <dd>
      279a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279b;
    </dt>
    
    <dd>
      279b
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279c;
    </dt>
    
    <dd>
      279c
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279d;
    </dt>
    
    <dd>
      279d
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279e;
    </dt>
    
    <dd>
      279e
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x279f;
    </dt>
    
    <dd>
      279f
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a0;
    </dt>
    
    <dd>
      27a0
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a1;
    </dt>
    
    <dd>
      27a1
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a2;
    </dt>
    
    <dd>
      27a2
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a3;
    </dt>
    
    <dd>
      27a3
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a4;
    </dt>
    
    <dd>
      27a4
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a5;
    </dt>
    
    <dd>
      27a5
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a6;
    </dt>
    
    <dd>
      27a6
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a7;
    </dt>
    
    <dd>
      27a7
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a8;
    </dt>
    
    <dd>
      27a8
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27a9;
    </dt>
    
    <dd>
      27a9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27aa;
    </dt>
    
    <dd>
      27aa
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27ab;
    </dt>
    
    <dd>
      27ab
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27ac;
    </dt>
    
    <dd>
      27ac
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27ad;
    </dt>
    
    <dd>
      27ad
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27ae;
    </dt>
    
    <dd>
      27ae
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27af;
    </dt>
    
    <dd>
      27af
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27b8;
    </dt>
    
    <dd>
      27b8
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27b9;
    </dt>
    
    <dd>
      27b9
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27ba;
    </dt>
    
    <dd>
      27ba
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27bb;
    </dt>
    
    <dd>
      27bb
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27bc;
    </dt>
    
    <dd>
      27bc
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27bd;
    </dt>
    
    <dd>
      27bd
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x27be;
    </dt>
    
    <dd>
      27be
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2b50;
    </dt>
    
    <dd>
      2b50
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2e2a;
    </dt>
    
    <dd>
      2e2a
    </dd>
  </dl>
  
  <dl>
    <dt>
      &#x2e2b;
    </dt>
    
    <dd>
      2e2b
    </dd>
  </dl>
</div>

 [1]: https://github.com/mkaz/dotfiles/blob/master/extras/colors
 [2]: http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x279.html
 [3]: http://unicode-table.com/en/