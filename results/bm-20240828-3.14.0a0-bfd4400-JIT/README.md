# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: JIT
- commit hash: [bfd4400](https://github.com/Fidget%2dSpinner/cpython/commit/bfd4400)
- commit date: 2024-08-28T20:30:12+08:00
- commit merge base: [e913d2c87f1ae4e7a4aef5ba78368ef31d060767](https://github.com/Fidget%2dSpinner/cpython/commit/e913d2c87f1ae4e7a4aef5ba78368ef31d060767)
- ref: deferred_globals_fin

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600702890)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.427x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 93.12%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base-mem.svg)
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

