# Deep Research Report: openai/o4-mini-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 02bee7af | **Time:** 102.05s | **Cost:** $0.55451
--------------------------------------------------------------------------------

In practice, designers meet this trade‐off by choosing the right equalizer architecture for the link span.  For moderate spans (tens to a couple of hundred km), a time-domain FIR equalizer of modest length can remove most dispersion with acceptable complexity.  Beyond a few hundred km (high dispersion), however, it becomes far cheaper to use an FFT-based (frequency-domain) equalizer.  In other words,  systems typically use a moderate-tap time-domain equalizer for short links and switch to an overlap-save FFT equalizer for long links.  This approach delivers nearly full dispersion compensation with far fewer multiplications per symbol.  (In fact, it has been shown that above ~200–300 km the FFT-based equalizer “has a complexity advantage over a time-domain compensator,” while for shorter links a moderate TDE suffices ([patents.google.com](https://patents.google.com/patent/EP2399354B1/en#:~:text=,order%20to%20keep%20complexity%20low)) ([patents.google.com](https://patents.google.com/patent/US8725007B2/en#:~:text=,a%20time%20domain%20dispersion%20compensator)).) 

**Answer:**  Use moderate-length time-domain equalization on short spans and an FFT/overlap-save frequency-domain equalizer on long spans – essentially “time-domain for small dispersion, FFT for large dispersion” – which balances complexity and integrity ([patents.google.com](https://patents.google.com/patent/EP2399354B1/en#:~:text=,order%20to%20keep%20complexity%20low)) ([patents.google.com](https://patents.google.com/patent/US8725007B2/en#:~:text=,a%20time%20domain%20dispersion%20compensator)).



## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 946, 'start_index': 828, 'title': 'EP2399354B1 - Method and arrangement for adaptive dispersion compensation. - Google Patents', 'url': 'https://patents.google.com/patent/EP2399354B1/en#:~:text=,order%20to%20keep%20complexity%20low'}}
{'type': 'url_citation', 'url_citation': {'end_index': 1073, 'start_index': 947, 'title': 'US8725007B2 - Method and arrangement for adaptive dispersion compensation - Google Patents', 'url': 'https://patents.google.com/patent/US8725007B2/en#:~:text=,a%20time%20domain%20dispersion%20compensator'}}
{'type': 'url_citation', 'url_citation': {'end_index': 1451, 'start_index': 1333, 'title': 'EP2399354B1 - Method and arrangement for adaptive dispersion compensation. - Google Patents', 'url': 'https://patents.google.com/patent/EP2399354B1/en#:~:text=,order%20to%20keep%20complexity%20low'}}
{'type': 'url_citation', 'url_citation': {'end_index': 1578, 'start_index': 1452, 'title': 'US8725007B2 - Method and arrangement for adaptive dispersion compensation - Google Patents', 'url': 'https://patents.google.com/patent/US8725007B2/en#:~:text=,a%20time%20domain%20dispersion%20compensator'}}

## Sources
