# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: JIT
- commit hash: [3d98d27](https://github.com/Fidget%2dSpinner/cpython/commit/3d98d27)
- commit date: 2024-09-17T01:36:16+08:00
- commit merge base: [401fff7423ca3c8bf1d02e594edfd1412616a559](https://github.com/Fidget%2dSpinner/cpython/commit/401fff7423ca3c8bf1d02e594edfd1412616a559)
- ref: fewer_set_ip

## linux x86_64 (azure)

- [pystats raw](bm-20240917-azure-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-pystats.json)
- [pystats table](bm-20240917-azure-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-pystats.md)

### vs. base

- [pystats diff](bm-20240917-azure-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10890651254)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.10.4.md)
- [📈time plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.12.0.md)
- [📈time plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 68.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.13.0.md)
- [📈time plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 63.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-base-mem.svg)
- [📄table](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-base.md)
- [📈time plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.13.0b2.md)
- [📈time plot](bm-20240917-linux-x86_64-Fidget%252dSpinner-fewer_set_ip-3.14.0a0-3d98d27-vs-3.13.0b2.svg)

