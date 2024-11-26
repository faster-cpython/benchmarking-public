# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [87cbfd7](https://github.com/brandtbucher/cpython/commit/87cbfd7)
- commit date: 2024-09-23T16:31:47-07:00
- commit merge base: [6e06e01881dcffbeef5baac0c112ffb14cfa0b27](https://github.com/brandtbucher/cpython/commit/6e06e01881dcffbeef5baac0c112ffb14cfa0b27)
- ref: decref_escapes

## linux x86_64 (azure)

- [pystats raw](bm-20240923-azure-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-pystats.json)
- [pystats table](bm-20240923-azure-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-pystats.md)

### vs. base

- [pystats diff](bm-20240923-azure-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004104890)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7.json)

### vs. 3.10.4

- Geometric mean: 1.420x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.10.4.md)
- [📈time plot](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.12.0.md)
- [📈time plot](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 94.82%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.13.0.md)
- [📈time plot](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 90.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-base-mem.svg)
- [📄table](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-base.md)
- [📈time plot](bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7-vs-base.svg)

