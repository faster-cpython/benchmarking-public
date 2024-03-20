# Results

- fork: gvanrossum
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [0fd96be](https://github.com/gvanrossum/cpython/commit/0fd96be)
- commit date: 2024-03-19T17:33:41-07:00
- commit merge base: [025ef7a5f7b424fba8713e448244b952bf897df3](https://github.com/gvanrossum/cpython/commit/025ef7a5f7b424fba8713e448244b952bf897df3)
- ref: func_version_cache

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8351032410)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 54.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 73.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 80.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-base-mem.png)
- [📄table](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-base.md)
- [📈time plot](bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5%2B-0fd96be-vs-base.png)

