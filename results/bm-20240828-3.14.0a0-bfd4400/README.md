# Results

- fork: Fidget-Spinner/deferred_globals_fin
- version: 3.14.0a0
- config: 
- commit hash: [bfd4400](https://github.com/Fidget%2dSpinner/cpython/commit/bfd4400)
- commit date: 2024-08-28T20:30:12+08:00
- commit merge base: [e913d2c87f1ae4e7a4aef5ba78368ef31d060767](https://github.com/python/cpython/commit/e913d2c87f1ae4e7a4aef5ba78368ef31d060767)
- ref: deferred_globals_fin

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.11%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 99.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base-mem.svg)
- [📄table](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-arminc-aarch64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base-mem.svg)
- [📄table](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-linux-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 86.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 54.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base-mem.svg)
- [📄table](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-pythonperf2-x86_64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.178x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.39%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-pythonperf1-amd64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.111x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x slower (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-pythonperf1_win32-x86-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json)

### vs. 3.10.4

- Geometric mean: 1.293x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.md)
- [📈time plot](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.md)
- [📈time plot](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.md)
- [📈time plot](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base-mem.svg)
- [📄table](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.md)
- [📈time plot](bm-20240828-darwin-arm64-Fidget%252dSpinner-deferred_globals_fin-3.14.0a0-bfd4400-vs-base.svg)

