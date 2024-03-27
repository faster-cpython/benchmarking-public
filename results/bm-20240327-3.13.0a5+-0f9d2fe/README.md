# Results

- fork: brandtbucher
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [0f9d2fe](https://github.com/brandtbucher/cpython/commit/0f9d2fe)
- commit date: 2024-03-27T10:50:23-07:00
- commit merge base: [74c8568d07719529b874897598d8b3bc25ff0434](https://github.com/brandtbucher/cpython/commit/74c8568d07719529b874897598d8b3bc25ff0434)
- ref: revert_90a1b28

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8456363740)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.10.4.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.11.0.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.12.0.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base-mem.png)
- [📄table](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base.md)
- [📈time plot](bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5%2B-0f9d2fe-vs-base.png)

