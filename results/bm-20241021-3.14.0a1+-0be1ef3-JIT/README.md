# Results

- fork: nick-arm
- version: 3.14.0a1+
- config: JIT
- commit hash: [0be1ef3](https://github.com/nick%2darm/cpython/commit/0be1ef3)
- commit date: 2024-10-21T10:10:27+00:00
- commit merge base: [ded105a62b9d78717f8dc64652e3903190b585dd](https://github.com/nick%2darm/cpython/commit/ded105a62b9d78717f8dc64652e3903190b585dd)
- ref: codecache

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11469935165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x slower (HPT: reliability of 55.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)
- [📈time plot](bm-20241021-linux-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11469935165)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x slower (HPT: reliability of 75.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x slower (HPT: reliability of 78.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11469935165)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 97.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 98.45%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-nick%252darm-codecache-3.14.0a1%2B-0be1ef3-vs-3.13.0.svg)

