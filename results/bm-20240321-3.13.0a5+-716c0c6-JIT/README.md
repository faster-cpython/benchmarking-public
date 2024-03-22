# Results

- fork: gvanrossum
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [716c0c6](https://github.com/gvanrossum/cpython/commit/716c0c6)
- commit date: 2024-03-21T18:22:12-07:00
- commit merge base: [50f9b0b1e0fb181875751cef951351ed007b6397](https://github.com/gvanrossum/cpython/commit/50f9b0b1e0fb181875751cef951351ed007b6397)
- ref: exp_backoff

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8384069642)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.10.4.md)
- [📈time plot](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.21x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.11.0.md)
- [📈time plot](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.24x slower (HPT: reliability of 99.93%, 1.01x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.12.0.md)
- [📈time plot](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-base-mem.png)
- [📄table](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-base.md)
- [📈time plot](bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5%2B-716c0c6-vs-base.png)

