# Results vs. 3.13.0b2

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: darwin-arm64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.03x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 177 ms: 1.10x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.7 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 508 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (6): async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.2 ms: 1.03x faster                                                 |
| nbody          | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.00x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                     | 150 ms: 1.01x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 73.6 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 174 us: 1.02x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 36.2 ms: 1.02x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.0 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.1 ms: 1.14x slower                                                 |
| python_startup         | 15.2 ms                                                    | 20.7 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.25x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.54 ms: 1.07x faster                                                 |
| django_template | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 40.7 ms: 1.36x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 152 us: 1.34x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 17.1 us: 1.32x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 1.57 us: 1.16x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 175 ms: 1.13x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 233 ms: 1.11x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 508 ms: 1.11x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 698 ms: 1.10x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 515 ms: 1.10x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.54 ms: 1.07x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.06x faster                                                |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                  |
| richards                         | 31.8 ms                                                    | 30.6 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 34.1 ms: 1.03x faster                                                 |
| float                            | 48.6 ms                                                    | 47.2 ms: 1.03x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 174 us: 1.02x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 36.2 ms: 1.02x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.7 ms: 1.02x faster                                                 |
| fannkuch                         | 248 ms                                                     | 245 ms: 1.02x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.57 ms: 1.00x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 410 ms: 1.00x slower                                                  |
| go                               | 101 ms                                                     | 101 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| thrift                           | 435 us                                                     | 437 us: 1.00x slower                                                  |
| pyflate                          | 321 ms                                                     | 322 ms: 1.01x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| regex_dna                        | 149 ms                                                     | 150 ms: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 903 us: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.0 ms: 1.01x slower                                                 |
| generators                       | 22.9 ms                                                    | 23.1 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.36 us: 1.02x slower                                                 |
| dask                             | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.3 ms: 1.03x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.14 sec: 1.03x slower                                                |
| logging_silent                   | 60.1 ns                                                    | 62.0 ns: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 68.9 ms: 1.04x slower                                                 |
| coverage                         | 45.0 ms                                                    | 46.7 ms: 1.04x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 485 ms: 1.04x slower                                                  |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.6 ms: 1.05x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 996 ms: 1.05x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.1 ms: 1.05x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 191 ms: 1.06x slower                                                  |
| sympy_str                        | 131 ms                                                     | 140 ms: 1.06x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 73.6 ms: 1.06x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 240 ms: 1.06x slower                                                  |
| pycparser                        | 632 ms                                                     | 674 ms: 1.07x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 478 us: 1.07x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 430 ms: 1.07x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 73.6 ms: 1.07x slower                                                 |
| nbody                            | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 178 ms: 1.08x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.3 ms: 1.08x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 102 ms: 1.08x slower                                                  |
| pylint                           | 170 ms                                                     | 184 ms: 1.08x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.32 ms: 1.08x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.43 ms: 1.09x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.3 ms: 1.10x slower                                                 |
| 2to3                             | 161 ms                                                     | 177 ms: 1.10x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.05 ms: 1.10x slower                                                 |
| raytrace                         | 147 ms                                                     | 163 ms: 1.11x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 58.1 ms: 1.11x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 994 us: 1.12x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 98.4 us: 1.12x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 828 us: 1.13x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 14.1 ms: 1.14x slower                                                 |
| chaos                            | 34.0 ms                                                    | 39.6 ms: 1.16x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.22x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 57.8 ms: 1.23x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 83.0 ms: 1.24x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 40.7 ms: 1.36x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 20.7 ms: 1.36x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (11): async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, pidigits, logging_simple, asyncio_tcp_ssl, json, async_tree_memoization_tg, tornado_http
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x