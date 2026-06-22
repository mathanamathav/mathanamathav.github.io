---
title: "Finally built a PC, for myself in 2026 🫪"
date: 2026-06-21
tags: ["PC Build", "Gaming"]
---

## Intro

Building my own PC has been a quiet dream for years. I first seriously wanted to do it and then didn't. I didn't really have the headspace, and honestly I didn't know what I was building *for*. "A good PC" isn't a spec. So I sat on it.

Fast-forward to 2026, and the timing looks almost comedic: this is one of the more expensive years in recent memory to buy PC parts. RAM , GPU  and SSD  pricing are all over the place most of it downstream of the enormous demand for AI. So naturally, *this* is the year I decided to finally do it.

This post is the story of how I built a PC given current market situation with the mental model I used to make decisions, the trade-offs I made, and what I learned along the way. If you're staring down your own first build and feeling overwhelmed by the sheer number of choices, hopefully my reasoning helps. If you just want the parts list, [skip to it](#the-parts).

## The spark

The honest origin story: I was lying in bed one night, scrolling YouTube, when Christian Selig's [*"I made the PC I couldn't buy"*](https://www.youtube.com/watch?v=7HgAN5cEmkk) dropped into my feed.

What grabbed me wasn't the build itself — it was the *way* he thought about it. A longtime Mac user building his first gaming PC since 2008, he set hard constraints up front (a strict $700 budget; compact, modern, upgradeable; tuned for 4K *fidelity* over raw frame rates) and then worked backwards to parts, buying used off Facebook Marketplace where it made sense. He even 3D-printed a Mac-Pro "cheese grater" front panel for airflow and added walnut feet. He landed the whole thing at $596. Something about that mindset flipped a switch: *why not me, with the same framework?*

So this build is, more than anything, a derivative of that video — a big shoutout to Christian. And yes, I ended up buying some of the parts from his build all without planning to. Good frameworks converge.

## Set the expectations before the parts

Before pricing a single component, I wrote down what I actually wanted out of this machine. This is the part most first-timers (including past me) skip, and it's the part that makes every later decision easy. Here was my mental model:

![My mental model — five constraints set before buying any parts: budget, purpose, modern, upgradable, compact](expectations-bento.png)

A bit of detail on each:

- **Budget** — ₹70k–90k at the absolute max, and as low as I could push it.
- **Purpose** — gaming. Specifically demanding, story-driven AAA games (*The Last of Us*, *RDR2*), at 1080p now and ideally 2K (and maybe 4K someday) with a decent, steady FPS.
- **Modern** — I like a clean, wireless desk, so Wi-Fi, Bluetooth, and USB-C support were non-negotiable.
- **Upgradable** — on a budget build, you cut corners on purpose. I wanted a clear upgrade path so I could improve parts later instead of rebuilding.
- **Compact** — a small, console-like machine I could tuck onto a desk or even sit in the living room.

Five constraints. Everything below is just me trying to satisfy them for the least money.

## Choosing the components

Here's the thing nobody warns you about: PC building is *deeply* personal and there are a dozen valid answers for every slot. The trick is to let your constraints — not your FOMO — narrow the field.

### The pricing reality shaped everything

With RAM, SSD, and GPU prices all inflated, the single most important decision was made for me: **DDR5 was out**. The DDR5 premium just wasn't worth it for budget gaming, so I committed to a **DDR4** platform from the start. That one choice cascaded into the CPU and motherboard picks.

### CPU + motherboard

For budget gaming, **AMD** was the obvious value pick. I went with the **Ryzen 5 5600** on the **AM4** socket — mature platform, cheap, and still very capable for 1080p/1440p gaming.

For the board, my "compact" constraint pointed me at **micro-ATX** — the sensible middle ground between a full ATX board (too big) and mini-ITX (small, but pricier and fiddlier). I picked the **Gigabyte B550M Gaming X** with Wi-Fi 6. It checked every box: AM4 socket, four RAM slots, M.2 support, and modern Wi-Fi + Bluetooth built in, all at a reasonable price.

### GPU — the one that matters most

This is where most of the budget and most of the agonizing went.

My target was 1080p today (that's the monitor I have) with headroom for 2K later. So I wasn't chasing the top of the stack — I wanted pure **value for money**. New cards were brutal: the latest 50-series pricing was bloated well past my budget, and the older 30/40-series new stock wasn't much friendlier.

So I made peace with the **second-hand market**. After a lot of searching across Amazon, OLX, and other listings, I got lucky and found a **Zotac RTX 3060 Twin Edge 12GB** for **₹19,500** — with 6–8 months of remaining warranty as a safety net. The 12GB of VRAM is genuinely useful for modern titles, and at that price it was the single best value decision in the whole build.

### Storage, RAM, PSU

- **Storage** — a **WD Blue SN5100 500GB** Gen4 NVMe M.2. Fast, and easy to add a second drive later.
- **RAM** — **16GB DDR4 3200** (2×8GB Corsair Vengeance LPX), running in dual channel.
- **PSU** — an **850W** MSI MAG A850GL (Gold, fully modular). Yes, this is *wildly* overkill for the current draw — the system happily sips 300–400W under load. But it's a deliberate future-proofing call: when I upgrade the GPU, the power headroom is already there, and a good Gold unit runs efficiently even when lightly loaded.

### The case (and the console-like dream)

The **Asus Prime AP201** mini tower locked in the compact, "could live in the living room" feel I was after — while still fitting a micro-ATX board and a full-size GPU. I added **5× Arctic P12 Slim** fans to keep airflow honest in a small box.

## Jugaad

If I had to compress the whole decision-making process into a single idea, it's this: almost every PC part has the same performance-vs-price curve, and it splits into three zones.

![Performance vs price, split into three zones — E-Waste, Best Value, and Gamer Tax — with the RTX 3060 marked in the best-value sweet spot](framework-zones.png)

My entire strategy was to camp in that best-value zone for every component: spend where it mattered the most.

## The parts

![Where the ₹80,813 went — PC parts price breakdown by part](parts-breakdown.png)

The full list, if you want the exact models: a **Ryzen 5 5600** CPU (₹11,999, new), the **Zotac RTX 3060 12GB** GPU (₹19,500, used), a **Gigabyte B550M Gaming X Wi-Fi 6** board (₹10,349), **16GB Corsair Vengeance LPX DDR4-3200** (₹11,344), a **WD Blue SN5100 500GB** NVMe (₹8,515), the **MSI MAG A850GL** 850W Gold PSU (₹8,694), an **Asus Prime AP201** case (₹5,799), and **5× Arctic P12 Slim** fans (₹4,613) — **₹80,813** all in.

Plus a couple of tools that earned their keep: a Bosch ratchet screwdriver (₹848) and a Stanley PH2 screwdriver (₹178).

<!-- TODO: add full build links - pcpartpicker.com/list/RTBYNp and pickpcparts.in build -->

## Build day

<!-- TODO: this section is the "in the process" learnings. Expand with real build-day specifics + photos. -->

<!-- TODO: photos - parts laid out, mid-build, finished build, BIOS first boot -->


## Benchmarks

<!-- TODO: benchmarks - Cinebench, 3DMark, Cyberpunk, etc. -->


## Future plans

<!-- TODO: upgrade path - CPU, RAM, Storage, GPU, etc. -->

## Wrapping up

<!-- TODO: my final thoughts and closure note. -->