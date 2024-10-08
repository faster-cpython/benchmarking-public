# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x slower
- HPT reliability: 94.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 171 ms: 1.06x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.53 sec: 1.07x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 638 ms: 1.20x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 498 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 677 ms: 1.13x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 45.9 ms: 1.06x faster                                                 |
| nbody          | 59.6 ms                                                    | 63.0 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 72.8 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.19x faster                                                |
| unpickle_pure_python | 141 us                                                     | 133 us: 1.06x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 171 us: 1.04x faster                                                  |
| xml_etree_parse      | 106 ms                                                     | 104 ms: 1.02x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.9 ms: 1.01x faster                                                 |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.39 ms: 1.09x faster                                                 |
| django_template | 19.4 ms                                                    | 21.1 ms: 1.09x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.5 ms: 1.18x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.12x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.37x faster                                                 |
| deepcopy                         | 204 us                                                     | 151 us: 1.35x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 638 ms: 1.20x faster                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.19x faster                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 1.56 us: 1.17x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 498 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 677 ms: 1.13x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.39 ms: 1.09x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 182 ms: 1.09x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 195 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 241 ms: 1.07x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                |
| generators                       | 22.9 ms                                                    | 21.5 ms: 1.06x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 133 us: 1.06x faster                                                  |
| float                            | 48.6 ms                                                    | 45.9 ms: 1.06x faster                                                 |
| richards                         | 31.8 ms                                                    | 30.2 ms: 1.05x faster                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 228 ms: 1.05x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 171 us: 1.04x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 33.9 ms: 1.04x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 2.94 us: 1.04x faster                                                 |
| pyflate                          | 321 ms                                                     | 310 ms: 1.04x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 544 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                                  |
| logging_format                   | 3.31 us                                                    | 3.24 us: 1.02x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.6 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 104 ms: 1.02x faster                                                  |
| json                             | 2.93 ms                                                    | 2.89 ms: 1.01x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.02 sec: 1.01x faster                                                |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| go                               | 101 ms                                                     | 99.7 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.9 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 355 ms: 1.01x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                                 |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| fannkuch                         | 248 ms                                                     | 249 ms: 1.00x slower                                                  |
| coverage                         | 45.0 ms                                                    | 45.1 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.7 ms: 1.01x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 66.9 ms: 1.01x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.0 ms: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 907 us: 1.01x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 61.0 ns: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 28.2 ms: 1.02x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 477 ms: 1.03x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 974 ms: 1.03x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.87 ms: 1.04x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.4 ms: 1.04x slower                                                 |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 99.6 ms: 1.05x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 470 us: 1.05x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 73.1 ms: 1.06x slower                                                 |
| sympy_str                        | 131 ms                                                     | 139 ms: 1.06x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 175 ms: 1.06x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.0 ms: 1.06x slower                                                 |
| pycparser                        | 632 ms                                                     | 670 ms: 1.06x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.27 ms: 1.06x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 32.8 ms: 1.06x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 72.8 ms: 1.06x slower                                                 |
| 2to3                             | 161 ms                                                     | 171 ms: 1.06x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 240 ms: 1.06x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.53 sec: 1.07x slower                                                |
| sympy_integrate                  | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.38 ms: 1.08x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 50.9 ms: 1.08x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 56.6 ms: 1.09x slower                                                 |
| raytrace                         | 147 ms                                                     | 160 ms: 1.09x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 95.1 us: 1.09x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.1 ms: 1.09x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 444 ms: 1.10x slower                                                  |
| pylint                           | 170 ms                                                     | 189 ms: 1.11x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 996 us: 1.12x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 820 us: 1.12x slower                                                  |
| chaos                            | 34.0 ms                                                    | 38.5 ms: 1.13x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.5 ms: 1.18x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 79.6 ms: 1.19x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, pidigits, regex_v8, pathlib, dask, tornado_http
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 94.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.42x