# Results

- fork: brandtbucher/justin_dwarf
- version: 3.14.0a1+
- config: JIT
- commit hash: [b20a4b8](https://github.com/brandtbucher/cpython/commit/b20a4b8)
- commit date: 2024-11-14T10:55:50-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: justin_dwarf

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11843762068)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 99.99%, 1.08x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.10.4.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.068x slower (HPT: reliability of 57.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.12.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.141x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.13.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 many_optionals, subparsers
- [🧠memory plot](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-base-mem.svg)
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-base.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-b20a4b8-vs-base.svg)

