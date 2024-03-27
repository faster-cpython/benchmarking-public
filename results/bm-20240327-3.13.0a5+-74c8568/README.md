# Results

- fork: brandtbucher
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [74c8568](https://github.com/brandtbucher/cpython/commit/74c8568)
- commit date: 2024-03-27T17:53:27+01:00
- commit merge base: [ce00de4c8cd39816f992e749c1074487d93abe9d](https://github.com/brandtbucher/cpython/commit/ce00de4c8cd39816f992e749c1074487d93abe9d)
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8456354958)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.10.4.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.11.0.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.12.0.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 54.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base-mem.png)
- [📄table](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5%2B-74c8568-vs-base.png)

