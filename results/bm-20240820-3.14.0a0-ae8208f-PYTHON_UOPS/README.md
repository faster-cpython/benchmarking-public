# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: T2
- commit hash: [ae8208f](https://github.com/faster%2dcpython/cpython/commit/ae8208f)
- commit date: 2024-08-20T09:55:31+01:00
- commit merge base: [e077b201f49a6007ddad7c1b6e3069a037b6d952](https://github.com/faster%2dcpython/cpython/commit/e077b201f49a6007ddad7c1b6e3069a037b6d952)
- ref: call_class_tier_2

## linux x86_64 (azure)

- [pystats raw](bm-20240820-azure-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-pystats.json)
- [pystats table](bm-20240820-azure-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-pystats.md)

### vs. base

- [pystats diff](bm-20240820-azure-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10469703940)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.10.4.md)
- [📈time plot](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.12.0.md)
- [📈time plot](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.13.0b2.md)
- [📈time plot](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-base-mem.svg)
- [📄table](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-base.md)
- [📈time plot](bm-20240820-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-ae8208f-vs-base.svg)

