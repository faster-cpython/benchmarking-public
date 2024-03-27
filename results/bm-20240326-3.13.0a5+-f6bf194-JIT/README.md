# Results

- fork: gvanrossum
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [f6bf194](https://github.com/gvanrossum/cpython/commit/f6bf194)
- commit date: 2024-03-26T22:01:20-07:00
- commit merge base: [48c0b05cf0dd2db275bd4653f84aa36c22bddcd2](https://github.com/gvanrossum/cpython/commit/48c0b05cf0dd2db275bd4653f84aa36c22bddcd2)
- ref: exp_backoff

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8447334369)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.10.4.md)
- [📈time plot](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 87.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.11.0.md)
- [📈time plot](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 85.87%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.12.0.md)
- [📈time plot](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 69.70%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base-mem.png)
- [📄table](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base.md)
- [📈time plot](bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-f6bf194-vs-base.png)

