# Results

- fork: gvanrossum
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [225ea17](https://github.com/gvanrossum/cpython/commit/225ea17)
- commit date: 2024-03-27T11:16:03-07:00
- commit merge base: [48c0b05cf0dd2db275bd4653f84aa36c22bddcd2](https://github.com/gvanrossum/cpython/commit/48c0b05cf0dd2db275bd4653f84aa36c22bddcd2)
- ref: exp_backoff

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8456963569)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.10.4.md)
- [📈time plot](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 54.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.11.0.md)
- [📈time plot](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 54.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.12.0.md)
- [📈time plot](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base-mem.png)
- [📄table](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base.md)
- [📈time plot](bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-225ea17-vs-base.png)

