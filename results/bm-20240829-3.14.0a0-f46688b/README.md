# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [f46688b](https://github.com/mdboom/cpython/commit/f46688b)
- commit date: 2024-08-29T11:54:12-04:00
- commit merge base: [58ce131037ecb34d506a613f21993cde2056f628](https://github.com/mdboom/cpython/commit/58ce131037ecb34d506a613f21993cde2056f628)
- ref: mimalloc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10618476654)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b.json)

### vs. 3.10.4

- Geometric mean: 1.459x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.10.4.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.12.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.13.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-base-mem.svg)
- [📄table](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-base.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b-vs-base.svg)

