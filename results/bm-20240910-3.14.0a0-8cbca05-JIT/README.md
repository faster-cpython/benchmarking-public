# Results

- fork: diegorusso/gh_119726_generate_a
- version: 3.14.0a0
- config: JIT
- commit hash: [8cbca05](https://github.com/diegorusso/cpython/commit/8cbca05)
- commit date: 2024-09-10T16:37:32+01:00
- commit merge base: [3597642ed57d184511ca2dbd1a382ffe8e280ac4](https://github.com/python/cpython/commit/3597642ed57d184511ca2dbd1a382ffe8e280ac4)
- ref: gh_119726_generate_a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10890711250)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json)

### vs. 3.10.4

- Geometric mean: 1.184x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.10.4.md)
- [📈time plot](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.12.0.md)
- [📈time plot](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.13.0.md)
- [📈time plot](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base-mem.svg)
- [📄table](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base.md)
- [📈time plot](bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240910-azure-x86_64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-pystats.json)
- [pystats table](bm-20240910-azure-x86_64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-pystats.md)

### vs. base

- [pystats diff](bm-20240910-azure-x86_64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-pystats-vs-base.md)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10890714433)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json)

### vs. 3.10.4

- Geometric mean: 1.232x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.10.4.md)
- [📈time plot](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 96.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.12.0.md)
- [📈time plot](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.13.0.md)
- [📈time plot](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base-mem.svg)
- [📄table](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base.md)
- [📈time plot](bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05-vs-base.svg)

