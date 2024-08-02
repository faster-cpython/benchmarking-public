# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.00x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 163 ms: 1.01x slower                                                            |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                                          |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 677 ms: 1.13x faster                                                            |
| async_tree_io_tg                 | 565 ms                                                     | 511 ms: 1.11x faster                                                            |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                            |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                            |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                            |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                            |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 452 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                           |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.1 ms: 1.01x faster                                                           |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 150 ms: 1.00x slower                                                            |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                           |
| regex_compile  | 68.5 ms                                                    | 69.1 ms: 1.01x slower                                                           |
| regex_effbot   | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.7 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                           |
| xml_etree_process    | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                           |
| tomli_loads          | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                                          |
| unpickle_pure_python | 141 us                                                     | 145 us: 1.03x slower                                                            |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                            |
| json_loads           | 16.8 us                                                    | 17.4 us: 1.03x slower                                                           |
| json_dumps           | 6.23 ms                                                    | 6.45 ms: 1.04x slower                                                           |
| pickle_pure_python   | 179 us                                                     | 185 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.5 ms: 1.02x slower                                                           |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.1 ms: 1.02x slower                                                           |
| genshi_xml      | 29.9 ms                                                    | 30.5 ms: 1.02x slower                                                           |
| django_template | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                            |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                           |
| async_tree_eager_io              | 766 ms                                                     | 640 ms: 1.20x faster                                                            |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                           |
| async_tree_eager_io_tg           | 768 ms                                                     | 677 ms: 1.13x faster                                                            |
| generators                       | 22.9 ms                                                    | 20.6 ms: 1.11x faster                                                           |
| async_tree_io_tg                 | 565 ms                                                     | 511 ms: 1.11x faster                                                            |
| async_tree_none_tg               | 198 ms                                                     | 183 ms: 1.08x faster                                                            |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.08x faster                                                            |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                            |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.06x faster                                                          |
| async_tree_memoization_tg        | 240 ms                                                     | 226 ms: 1.06x faster                                                            |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 452 ms: 1.03x faster                                                            |
| go                               | 101 ms                                                     | 98.8 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                          |
| dulwich_log                      | 27.6 ms                                                    | 27.2 ms: 1.01x faster                                                           |
| richards                         | 31.8 ms                                                    | 31.5 ms: 1.01x faster                                                           |
| logging_silent                   | 60.1 ns                                                    | 59.5 ns: 1.01x faster                                                           |
| richards_super                   | 35.2 ms                                                    | 34.8 ms: 1.01x faster                                                           |
| nbody                            | 59.6 ms                                                    | 59.1 ms: 1.01x faster                                                           |
| deltablue                        | 2.14 ms                                                    | 2.13 ms: 1.00x faster                                                           |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                            |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| thrift                           | 435 us                                                     | 436 us: 1.00x slower                                                            |
| regex_dna                        | 149 ms                                                     | 150 ms: 1.00x slower                                                            |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                           |
| logging_simple                   | 3.04 us                                                    | 3.05 us: 1.00x slower                                                           |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                           |
| async_generators                 | 281 ms                                                     | 283 ms: 1.01x slower                                                            |
| regex_compile                    | 68.5 ms                                                    | 69.1 ms: 1.01x slower                                                           |
| create_gc_cycles                 | 897 us                                                     | 906 us: 1.01x slower                                                            |
| pyflate                          | 321 ms                                                     | 324 ms: 1.01x slower                                                            |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                           |
| 2to3                             | 161 ms                                                     | 163 ms: 1.01x slower                                                            |
| coverage                         | 45.0 ms                                                    | 45.6 ms: 1.01x slower                                                           |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                            |
| pycparser                        | 632 ms                                                     | 641 ms: 1.01x slower                                                            |
| bench_thread_pool                | 447 us                                                     | 453 us: 1.01x slower                                                            |
| html5lib                         | 31.2 ms                                                    | 31.6 ms: 1.02x slower                                                           |
| genshi_text                      | 13.9 ms                                                    | 14.1 ms: 1.02x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                            |
| hexiom                           | 4.06 ms                                                    | 4.12 ms: 1.02x slower                                                           |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                           |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                           |
| genshi_xml                       | 29.9 ms                                                    | 30.5 ms: 1.02x slower                                                           |
| spectral_norm                    | 66.4 ms                                                    | 67.6 ms: 1.02x slower                                                           |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.02x slower                                                           |
| xml_etree_generate               | 52.7 ms                                                    | 53.7 ms: 1.02x slower                                                           |
| sqlglot_transpile                | 891 us                                                     | 908 us: 1.02x slower                                                            |
| sympy_expand                     | 226 ms                                                     | 230 ms: 1.02x slower                                                            |
| regex_effbot                     | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                                           |
| python_startup                   | 15.2 ms                                                    | 15.5 ms: 1.02x slower                                                           |
| pprint_pformat                   | 947 ms                                                     | 967 ms: 1.02x slower                                                            |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                           |
| sqlglot_parse                    | 732 us                                                     | 748 us: 1.02x slower                                                            |
| django_template                  | 19.4 ms                                                    | 19.9 ms: 1.02x slower                                                           |
| xml_etree_process                | 37.1 ms                                                    | 37.9 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.84 ms: 1.02x slower                                                           |
| pprint_safe_repr                 | 465 ms                                                     | 475 ms: 1.02x slower                                                            |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.6 ms: 1.02x slower                                                           |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                           |
| tomli_loads                      | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                                          |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.02x slower                                                          |
| sympy_str                        | 131 ms                                                     | 135 ms: 1.03x slower                                                            |
| scimark_sor                      | 94.9 ms                                                    | 97.4 ms: 1.03x slower                                                           |
| unpickle_pure_python             | 141 us                                                     | 145 us: 1.03x slower                                                            |
| json                             | 2.93 ms                                                    | 3.01 ms: 1.03x slower                                                           |
| comprehensions                   | 10.2 us                                                    | 10.4 us: 1.03x slower                                                           |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                            |
| nqueens                          | 52.2 ms                                                    | 53.8 ms: 1.03x slower                                                           |
| json_loads                       | 16.8 us                                                    | 17.4 us: 1.03x slower                                                           |
| crypto_pyaes                     | 49.5 ms                                                    | 51.1 ms: 1.03x slower                                                           |
| sqlglot_normalize                | 166 ms                                                     | 171 ms: 1.03x slower                                                            |
| sympy_sum                        | 69.2 ms                                                    | 71.6 ms: 1.03x slower                                                           |
| scimark_fft                      | 181 ms                                                     | 187 ms: 1.03x slower                                                            |
| meteor_contest                   | 70.3 ms                                                    | 72.8 ms: 1.04x slower                                                           |
| json_dumps                       | 6.23 ms                                                    | 6.45 ms: 1.04x slower                                                           |
| pickle_pure_python               | 179 us                                                     | 185 us: 1.04x slower                                                            |
| bench_mp_pool                    | 47.2 ms                                                    | 49.0 ms: 1.04x slower                                                           |
| telco                            | 4.60 ms                                                    | 4.79 ms: 1.04x slower                                                           |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                           |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                                          |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                           |
| typing_runtime_protocols         | 87.6 us                                                    | 92.2 us: 1.05x slower                                                           |
| scimark_lu                       | 66.9 ms                                                    | 70.5 ms: 1.05x slower                                                           |
| fannkuch                         | 248 ms                                                     | 267 ms: 1.08x slower                                                            |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, tornado_http, async_tree_eager_memoization_tg, mako, float, dask, async_tree_eager_cpu_io_mixed, pathlib, asyncio_tcp, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.69x