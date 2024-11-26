# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [f03f745](https://github.com/faster%2dcpython/cpython/commit/f03f745)
- commit date: 2024-10-29T18:28:26+00:00
- commit merge base: [faa3272fb8d63d481a136cc0467a0cba6ed7b264](https://github.com/faster%2dcpython/cpython/commit/faa3272fb8d63d481a136cc0467a0cba6ed7b264)
- ref: use_stackrefs

## linux x86_64 (azure)

- [pystats raw](bm-20241029-azure-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-pystats.json)
- [pystats table](bm-20241029-azure-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-pystats.md)

### vs. base

- [pystats diff](bm-20241029-azure-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11655632292)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745.json)

### vs. 3.10.4

- Geometric mean: 1.385x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 99.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base-mem.svg)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11655636132)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745.json)

### vs. 3.10.4

- Geometric mean: 1.065x faster (HPT: reliability of 95.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.114x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: sqlite_synth
- [📄table](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.091x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base.md)
- [📈time plot](bm-20241029-pythonperf1-amd64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11655639777)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745.json)

### vs. 3.10.4

- Geometric mean: 1.218x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.md)
- [📈time plot](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 98.20%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.md)
- [📈time plot](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 98.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, dask, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.md)
- [📈time plot](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base-mem.svg)
- [📄table](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base.md)
- [📈time plot](bm-20241029-darwin-arm64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-f03f745-vs-base.svg)

