# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: darwin-arm64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.00x faster
- HPT reliability: 88.28%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 170 ms: 1.06x slower                                                            |
| docutils       | 1.44 sec                                                   | 1.53 sec: 1.06x slower                                                          |
| html5lib       | 31.2 ms                                                    | 29.4 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|---------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io             | 766 ms                                                     | 616 ms: 1.24x faster                                                            |
| async_tree_eager_io_tg          | 768 ms                                                     | 652 ms: 1.18x faster                                                            |
| async_tree_io_tg                | 565 ms                                                     | 498 ms: 1.13x faster                                                            |
| async_tree_none_tg              | 198 ms                                                     | 178 ms: 1.11x faster                                                            |
| async_tree_none                 | 209 ms                                                     | 189 ms: 1.11x faster                                                            |
| async_tree_memoization          | 260 ms                                                     | 236 ms: 1.10x faster                                                            |
| async_tree_memoization_tg       | 240 ms                                                     | 224 ms: 1.07x faster                                                            |
| async_tree_io                   | 563 ms                                                     | 538 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 448 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg      | 451 ms                                                     | 436 ms: 1.03x faster                                                            |
| async_tree_eager_memoization_tg | 126 ms                                                     | 121 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                     | 354 ms: 1.01x faster                                                            |
| async_tree_eager                | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                                           |
| Geometric mean                  | (ref)                                                      | 1.07x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                           |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| nbody          | 59.6 ms                                                    | 62.9 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                           |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                            |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                           |
| regex_compile  | 68.5 ms                                                    | 72.1 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.21 sec: 1.22x faster                                                          |
| unpickle_pure_python | 141 us                                                     | 128 us: 1.10x faster                                                            |
| xml_etree_process    | 37.1 ms                                                    | 34.8 ms: 1.06x faster                                                           |
| pickle_pure_python   | 179 us                                                     | 170 us: 1.05x faster                                                            |
| xml_etree_generate   | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                           |
| json_dumps           | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 71.5 ms                                                    | 71.2 ms: 1.00x faster                                                           |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                                           |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                           |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                           |
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                           |
| django_template | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                           |
| genshi_xml      | 29.9 ms                                                    | 33.3 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|---------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo                   | 22.6 us                                                    | 16.8 us: 1.34x faster                                                           |
| deepcopy                        | 204 us                                                     | 154 us: 1.33x faster                                                            |
| async_tree_eager_io             | 766 ms                                                     | 616 ms: 1.24x faster                                                            |
| tomli_loads                     | 1.47 sec                                                   | 1.21 sec: 1.22x faster                                                          |
| deepcopy_reduce                 | 1.82 us                                                    | 1.52 us: 1.20x faster                                                           |
| scimark_sor                     | 94.9 ms                                                    | 79.6 ms: 1.19x faster                                                           |
| async_tree_eager_io_tg          | 768 ms                                                     | 652 ms: 1.18x faster                                                            |
| async_tree_io_tg                | 565 ms                                                     | 498 ms: 1.13x faster                                                            |
| async_tree_none_tg              | 198 ms                                                     | 178 ms: 1.11x faster                                                            |
| async_tree_none                 | 209 ms                                                     | 189 ms: 1.11x faster                                                            |
| async_tree_memoization          | 260 ms                                                     | 236 ms: 1.10x faster                                                            |
| unpickle_pure_python            | 141 us                                                     | 128 us: 1.10x faster                                                            |
| coroutines                      | 15.8 ms                                                    | 14.4 ms: 1.10x faster                                                           |
| mako                            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                           |
| go                              | 101 ms                                                     | 94.0 ms: 1.07x faster                                                           |
| async_tree_memoization_tg       | 240 ms                                                     | 224 ms: 1.07x faster                                                            |
| xml_etree_process               | 37.1 ms                                                    | 34.8 ms: 1.06x faster                                                           |
| html5lib                        | 31.2 ms                                                    | 29.4 ms: 1.06x faster                                                           |
| richards                        | 31.8 ms                                                    | 30.0 ms: 1.06x faster                                                           |
| mdp                             | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                                          |
| pickle_pure_python              | 179 us                                                     | 170 us: 1.05x faster                                                            |
| async_tree_io                   | 563 ms                                                     | 538 ms: 1.05x faster                                                            |
| float                           | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 448 ms: 1.04x faster                                                            |
| logging_simple                  | 3.04 us                                                    | 2.93 us: 1.04x faster                                                           |
| pyflate                         | 321 ms                                                     | 309 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg      | 451 ms                                                     | 436 ms: 1.03x faster                                                            |
| async_tree_eager_memoization_tg | 126 ms                                                     | 121 ms: 1.03x faster                                                            |
| xml_etree_generate              | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                           |
| richards_super                  | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                                           |
| logging_format                  | 3.31 us                                                    | 3.24 us: 1.02x faster                                                           |
| genshi_text                     | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl                 | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                     | 354 ms: 1.01x faster                                                            |
| regex_effbot                    | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                           |
| json_dumps                      | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                           |
| bpe_tokeniser                   | 3.05 sec                                                   | 3.04 sec: 1.00x faster                                                          |
| xml_etree_iterparse             | 71.5 ms                                                    | 71.2 ms: 1.00x faster                                                           |
| asyncio_websockets              | 409 ms                                                     | 408 ms: 1.00x faster                                                            |
| regex_dna                       | 149 ms                                                     | 149 ms: 1.00x faster                                                            |
| regex_v8                        | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                           |
| pidigits                        | 282 ms                                                     | 282 ms: 1.00x faster                                                            |
| thrift                          | 435 us                                                     | 438 us: 1.01x slower                                                            |
| create_gc_cycles                | 897 us                                                     | 902 us: 1.01x slower                                                            |
| gc_traversal                    | 2.45 ms                                                    | 2.48 ms: 1.01x slower                                                           |
| deltablue                       | 2.14 ms                                                    | 2.17 ms: 1.01x slower                                                           |
| logging_silent                  | 60.1 ns                                                    | 61.0 ns: 1.01x slower                                                           |
| python_startup                  | 15.2 ms                                                    | 15.4 ms: 1.02x slower                                                           |
| dulwich_log                     | 27.6 ms                                                    | 28.0 ms: 1.02x slower                                                           |
| json_loads                      | 16.8 us                                                    | 17.1 us: 1.02x slower                                                           |
| xml_etree_parse                 | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| meteor_contest                  | 70.3 ms                                                    | 71.7 ms: 1.02x slower                                                           |
| fannkuch                        | 248 ms                                                     | 254 ms: 1.02x slower                                                            |
| scimark_monte_carlo             | 42.5 ms                                                    | 43.5 ms: 1.03x slower                                                           |
| async_tree_eager                | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                                           |
| spectral_norm                   | 66.4 ms                                                    | 68.6 ms: 1.03x slower                                                           |
| async_generators                | 281 ms                                                     | 292 ms: 1.04x slower                                                            |
| python_startup_no_site          | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                           |
| crypto_pyaes                    | 49.5 ms                                                    | 51.7 ms: 1.05x slower                                                           |
| pycparser                       | 632 ms                                                     | 662 ms: 1.05x slower                                                            |
| scimark_fft                     | 181 ms                                                     | 189 ms: 1.05x slower                                                            |
| bench_thread_pool               | 447 us                                                     | 469 us: 1.05x slower                                                            |
| typing_runtime_protocols        | 87.6 us                                                    | 92.1 us: 1.05x slower                                                           |
| regex_compile                   | 68.5 ms                                                    | 72.1 ms: 1.05x slower                                                           |
| nbody                           | 59.6 ms                                                    | 62.9 ms: 1.06x slower                                                           |
| 2to3                            | 161 ms                                                     | 170 ms: 1.06x slower                                                            |
| pprint_safe_repr                | 465 ms                                                     | 491 ms: 1.06x slower                                                            |
| sympy_sum                       | 69.2 ms                                                    | 73.4 ms: 1.06x slower                                                           |
| pprint_pformat                  | 947 ms                                                     | 1.01 sec: 1.06x slower                                                          |
| sympy_str                       | 131 ms                                                     | 140 ms: 1.06x slower                                                            |
| sqlglot_normalize               | 166 ms                                                     | 176 ms: 1.06x slower                                                            |
| docutils                        | 1.44 sec                                                   | 1.53 sec: 1.06x slower                                                          |
| sqlglot_optimize                | 30.9 ms                                                    | 32.9 ms: 1.07x slower                                                           |
| generators                      | 22.9 ms                                                    | 24.5 ms: 1.07x slower                                                           |
| sympy_expand                    | 226 ms                                                     | 242 ms: 1.07x slower                                                            |
| asyncio_tcp                     | 402 ms                                                     | 432 ms: 1.07x slower                                                            |
| bench_mp_pool                   | 47.2 ms                                                    | 50.9 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult         | 2.77 ms                                                    | 3.00 ms: 1.08x slower                                                           |
| raytrace                        | 147 ms                                                     | 161 ms: 1.09x slower                                                            |
| sympy_integrate                 | 10.3 ms                                                    | 11.3 ms: 1.09x slower                                                           |
| hexiom                          | 4.06 ms                                                    | 4.46 ms: 1.10x slower                                                           |
| django_template                 | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                           |
| nqueens                         | 52.2 ms                                                    | 57.7 ms: 1.11x slower                                                           |
| genshi_xml                      | 29.9 ms                                                    | 33.3 ms: 1.11x slower                                                           |
| pylint                          | 170 ms                                                     | 191 ms: 1.12x slower                                                            |
| chaos                           | 34.0 ms                                                    | 38.5 ms: 1.13x slower                                                           |
| sqlglot_transpile               | 891 us                                                     | 1.01 ms: 1.13x slower                                                           |
| sqlglot_parse                   | 732 us                                                     | 836 us: 1.14x slower                                                            |
| scimark_lu                      | 66.9 ms                                                    | 79.9 ms: 1.19x slower                                                           |
| comprehensions                  | 10.2 us                                                    | 12.2 us: 1.21x slower                                                           |
| Geometric mean                  | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (9): async_tree_eager_memoization, telco, json, dask, async_tree_eager_cpu_io_mixed_tg, tornado_http, coverage, async_tree_eager_tg, pathlib
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.63x