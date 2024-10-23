# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [ded105a](https://github.com/python/cpython/commit/ded105a)
- commit date: 2024-10-21T10:44:18+02:00
- commit merge base: [c5c21fee7ae1ea689a351caa454c98e716a6e537](https://github.com/python/cpython/commit/c5c21fee7ae1ea689a351caa454c98e716a6e537)
- ref: ded105a62b9d78717f8d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x slower (HPT: reliability of 51.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x slower (HPT: reliability of 67.39%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x slower (HPT: reliability of 62.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 86.75%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 75.38%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.65%, 1.00x faster at 99th %ile)
- Memory usage: 6.69x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

