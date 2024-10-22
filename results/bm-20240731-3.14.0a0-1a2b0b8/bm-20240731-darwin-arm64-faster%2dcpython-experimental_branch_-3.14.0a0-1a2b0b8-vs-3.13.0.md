# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 163 ms: 1.09x faster                                                            |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                          |
| html5lib       | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                            |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.14x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 61.7 ms: 1.14x faster                                                           |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                            |
| asyncio_tcp                      | 457 ms                                                 | 423 ms: 1.08x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                            |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 452 ms: 1.02x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 511 ms: 1.02x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 677 ms: 1.42x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.1 ms: 1.25x faster                                                           |
| float          | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                           |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 69.1 ms: 1.14x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.64 ms: 1.00x slower                                                           |
| regex_dna      | 148 ms                                                 | 150 ms: 1.01x slower                                                            |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 185 us: 1.15x faster                                                            |
| unpickle_pure_python | 163 us                                                 | 145 us: 1.13x faster                                                            |
| xml_etree_process    | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                           |
| xml_etree_generate   | 56.6 ms                                                | 53.7 ms: 1.05x faster                                                           |
| tomli_loads          | 1.56 sec                                               | 1.50 sec: 1.04x faster                                                          |
| json_dumps           | 6.56 ms                                                | 6.45 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                           |
| json_loads           | 16.9 us                                                | 17.4 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.06x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.19x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 30.5 ms: 1.13x faster                                                           |
| django_template | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                           |
| mako            | 7.68 ms                                                | 6.98 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 17.1 us: 1.59x faster                                                           |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                            |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                            |
| deltablue                        | 2.68 ms                                                | 2.13 ms: 1.26x faster                                                           |
| nbody                            | 73.9 ms                                                | 59.1 ms: 1.25x faster                                                           |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                            |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.19x faster                                                           |
| hexiom                           | 4.85 ms                                                | 4.12 ms: 1.18x faster                                                           |
| logging_silent                   | 69.9 ns                                                | 59.5 ns: 1.18x faster                                                           |
| logging_simple                   | 3.57 us                                                | 3.05 us: 1.17x faster                                                           |
| nqueens                          | 62.9 ms                                                | 53.8 ms: 1.17x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                           |
| comprehensions                   | 12.2 us                                                | 10.4 us: 1.17x faster                                                           |
| go                               | 115 ms                                                 | 98.8 ms: 1.16x faster                                                           |
| html5lib                         | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                           |
| float                            | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                           |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.15x faster                                                           |
| dask                             | 255 ms                                                 | 222 ms: 1.15x faster                                                            |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                                           |
| pickle_pure_python               | 213 us                                                 | 185 us: 1.15x faster                                                            |
| sqlglot_parse                    | 856 us                                                 | 748 us: 1.14x faster                                                            |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.14x faster                                                           |
| spectral_norm                    | 77.3 ms                                                | 67.6 ms: 1.14x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 61.7 ms: 1.14x faster                                                           |
| regex_compile                    | 78.5 ms                                                | 69.1 ms: 1.14x faster                                                           |
| unpickle_pure_python             | 163 us                                                 | 145 us: 1.13x faster                                                            |
| genshi_xml                       | 34.4 ms                                                | 30.5 ms: 1.13x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                | 908 us: 1.13x faster                                                            |
| richards                         | 35.4 ms                                                | 31.5 ms: 1.13x faster                                                           |
| richards_super                   | 39.1 ms                                                | 34.8 ms: 1.12x faster                                                           |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                            |
| django_template                  | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                           |
| bench_thread_pool                | 506 us                                                 | 453 us: 1.12x faster                                                            |
| pprint_safe_repr                 | 531 ms                                                 | 475 ms: 1.12x faster                                                            |
| pprint_pformat                   | 1.08 sec                                               | 967 ms: 1.12x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                            |
| sqlglot_optimize                 | 34.9 ms                                                | 31.6 ms: 1.10x faster                                                           |
| sqlglot_normalize                | 189 ms                                                 | 171 ms: 1.10x faster                                                            |
| pycparser                        | 706 ms                                                 | 641 ms: 1.10x faster                                                            |
| mako                             | 7.68 ms                                                | 6.98 ms: 1.10x faster                                                           |
| python_startup                   | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 92.2 us: 1.10x faster                                                           |
| 2to3                             | 178 ms                                                 | 163 ms: 1.09x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                            |
| scimark_lu                       | 76.5 ms                                                | 70.5 ms: 1.09x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 97.4 ms: 1.08x faster                                                           |
| pyflate                          | 351 ms                                                 | 324 ms: 1.08x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                            |
| asyncio_tcp                      | 457 ms                                                 | 423 ms: 1.08x faster                                                            |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.08x faster                                                            |
| xml_etree_process                | 40.9 ms                                                | 37.9 ms: 1.08x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                                           |
| scimark_fft                      | 201 ms                                                 | 187 ms: 1.08x faster                                                            |
| sympy_expand                     | 246 ms                                                 | 230 ms: 1.07x faster                                                            |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.06x faster                                                           |
| crypto_pyaes                     | 54.0 ms                                                | 51.1 ms: 1.06x faster                                                           |
| sympy_sum                        | 75.6 ms                                                | 71.6 ms: 1.06x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 27.2 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.84 ms: 1.06x faster                                                           |
| xml_etree_generate               | 56.6 ms                                                | 53.7 ms: 1.05x faster                                                           |
| fannkuch                         | 282 ms                                                 | 267 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                            |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                          |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                            |
| bench_mp_pool                    | 50.9 ms                                                | 49.0 ms: 1.04x faster                                                           |
| tomli_loads                      | 1.56 sec                                               | 1.50 sec: 1.04x faster                                                          |
| bpe_tokeniser                    | 3.24 sec                                               | 3.13 sec: 1.04x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                            |
| json_dumps                       | 6.56 ms                                                | 6.45 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 452 ms: 1.02x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 73.1 ms: 1.01x faster                                                           |
| meteor_contest                   | 73.8 ms                                                | 72.8 ms: 1.01x faster                                                           |
| coverage                         | 46.1 ms                                                | 45.6 ms: 1.01x faster                                                           |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                           |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.64 ms: 1.00x slower                                                           |
| regex_dna                        | 148 ms                                                 | 150 ms: 1.01x slower                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 511 ms: 1.02x slower                                                            |
| json                             | 2.94 ms                                                | 3.01 ms: 1.02x slower                                                           |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                           |
| json_loads                       | 16.9 us                                                | 17.4 us: 1.03x slower                                                           |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                          |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                            |
| create_gc_cycles                 | 803 us                                                 | 906 us: 1.13x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 677 ms: 1.42x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (6): tornado_http, async_tree_cpu_io_mixed_tg, telco, xml_etree_parse, pylint, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x