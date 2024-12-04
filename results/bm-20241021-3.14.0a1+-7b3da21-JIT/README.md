# Results

- fork: nick-arm
- version: 3.14.0a1+
- config: JIT
- commit hash: [7b3da21](https://github.com/nick%2darm/cpython/commit/7b3da21)
- commit date: 2024-10-21T10:11:34+00:00
- commit merge base: [ded105a62b9d78717f8dc64652e3903190b585dd](https://github.com/nick%2darm/cpython/commit/ded105a62b9d78717f8dc64652e3903190b585dd)
- ref: codecache_rwx

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg)
- [📄table](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-arminc-aarch64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.410x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 62.46%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg)
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.280x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 74.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 62.63%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 98.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg)
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.235x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 97.07%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 95.08%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x faster (HPT: reliability of 89.24%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21.json)

### vs. 3.10.4

- Geometric mean: 1.279x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.md)
- [📈time plot](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.md)
- [📈time plot](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.md)
- [📈time plot](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base-mem.svg)
- [📄table](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.md)
- [📈time plot](bm-20241021-darwin-arm64-nick%252darm-codecache_rwx-3.14.0a1%2B-7b3da21-vs-base.svg)

