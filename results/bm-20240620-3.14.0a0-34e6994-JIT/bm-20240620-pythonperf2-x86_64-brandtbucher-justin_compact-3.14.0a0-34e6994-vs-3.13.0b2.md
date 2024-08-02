# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.01x slower
- HPT reliability: 94.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 73.2 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg        | 900 ms                                                           | 877 ms: 1.03x faster                                                        |
| async_tree_memoization  | 460 ms                                                           | 476 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                           | 629 ms: 1.04x slower                                                        |
| async_tree_none         | 365 ms                                                           | 383 ms: 1.05x slower                                                        |
| async_tree_io           | 873 ms                                                           | 915 ms: 1.05x slower                                                        |
| Geometric mean          | (ref)                                                            | 1.03x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.4 ms: 1.08x faster                                                       |
| nbody          | 87.8 ms                                                          | 82.4 ms: 1.07x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.4 ms: 1.03x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 81.0 ms: 1.06x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 31.3 us: 1.05x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 57.9 ms: 1.03x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 218 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.36 us: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.6 us: 1.02x slower                                                       |
| pickle               | 10.6 us                                                          | 10.9 us: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.9 ms: 1.05x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.50 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| django_template | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 63.5 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo            | 37.3 us                                                          | 29.0 us: 1.29x faster                                                       |
| deepcopy                 | 377 us                                                           | 307 us: 1.23x faster                                                        |
| spectral_norm            | 97.3 ms                                                          | 82.9 ms: 1.17x faster                                                       |
| richards                 | 53.4 ms                                                          | 46.9 ms: 1.14x faster                                                       |
| tomli_loads              | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                      |
| mako                     | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| richards_super           | 61.2 ms                                                          | 54.5 ms: 1.12x faster                                                       |
| deepcopy_reduce          | 3.39 us                                                          | 3.03 us: 1.12x faster                                                       |
| float                    | 80.2 ms                                                          | 74.4 ms: 1.08x faster                                                       |
| pyflate                  | 482 ms                                                           | 449 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.02 ms: 1.07x faster                                                       |
| nbody                    | 87.8 ms                                                          | 82.4 ms: 1.07x faster                                                       |
| gc_traversal             | 4.69 ms                                                          | 4.42 ms: 1.06x faster                                                       |
| pathlib                  | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| xml_etree_generate       | 85.7 ms                                                          | 81.0 ms: 1.06x faster                                                       |
| coverage                 | 83.5 ms                                                          | 79.1 ms: 1.05x faster                                                       |
| scimark_fft              | 312 ms                                                           | 296 ms: 1.05x faster                                                        |
| create_gc_cycles         | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| pickle_dict              | 32.8 us                                                          | 31.3 us: 1.05x faster                                                       |
| regex_dna                | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_compile            | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| fannkuch                 | 353 ms                                                           | 341 ms: 1.03x faster                                                        |
| xml_etree_process        | 59.7 ms                                                          | 57.9 ms: 1.03x faster                                                       |
| pprint_safe_repr         | 818 ms                                                           | 793 ms: 1.03x faster                                                        |
| unpickle_pure_python     | 224 us                                                           | 218 us: 1.03x faster                                                        |
| xml_etree_iterparse      | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| async_tree_io_tg         | 900 ms                                                           | 877 ms: 1.03x faster                                                        |
| regex_v8                 | 26.0 ms                                                          | 25.4 ms: 1.03x faster                                                       |
| crypto_pyaes             | 73.6 ms                                                          | 72.0 ms: 1.02x faster                                                       |
| telco                    | 8.40 ms                                                          | 8.22 ms: 1.02x faster                                                       |
| pprint_pformat           | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                      |
| html5lib                 | 74.7 ms                                                          | 73.2 ms: 1.02x faster                                                       |
| unpickle                 | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pickle_list              | 4.44 us                                                          | 4.36 us: 1.02x faster                                                       |
| xml_etree_parse          | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_dumps               | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| asyncio_websockets       | 395 ms                                                           | 389 ms: 1.01x faster                                                        |
| pidigits                 | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| logging_format           | 7.11 us                                                          | 7.06 us: 1.01x faster                                                       |
| asyncio_tcp              | 378 ms                                                           | 376 ms: 1.01x faster                                                        |
| sqlite_synth             | 2.80 us                                                          | 2.78 us: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| coroutines               | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                                       |
| bpe_tokeniser            | 5.14 sec                                                         | 5.21 sec: 1.01x slower                                                      |
| meteor_contest           | 128 ms                                                           | 130 ms: 1.02x slower                                                        |
| generators               | 33.5 ms                                                          | 34.1 ms: 1.02x slower                                                       |
| json_loads               | 25.0 us                                                          | 25.6 us: 1.02x slower                                                       |
| pickle                   | 10.6 us                                                          | 10.9 us: 1.02x slower                                                       |
| tornado_http             | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| pickle_pure_python       | 307 us                                                           | 316 us: 1.03x slower                                                        |
| scimark_monte_carlo      | 65.5 ms                                                          | 67.4 ms: 1.03x slower                                                       |
| json                     | 5.35 ms                                                          | 5.52 ms: 1.03x slower                                                       |
| async_tree_memoization   | 460 ms                                                           | 476 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 629 ms: 1.04x slower                                                        |
| dask                     | 391 ms                                                           | 407 ms: 1.04x slower                                                        |
| sqlglot_parse            | 1.39 ms                                                          | 1.45 ms: 1.04x slower                                                       |
| docutils                 | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                      |
| async_tree_none          | 365 ms                                                           | 383 ms: 1.05x slower                                                        |
| async_tree_io            | 873 ms                                                           | 915 ms: 1.05x slower                                                        |
| sqlglot_transpile        | 1.76 ms                                                          | 1.85 ms: 1.05x slower                                                       |
| python_startup           | 13.2 ms                                                          | 13.9 ms: 1.05x slower                                                       |
| thrift                   | 880 us                                                           | 924 us: 1.05x slower                                                        |
| pycparser                | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                      |
| mdp                      | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                      |
| genshi_text              | 25.9 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| regex_effbot             | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| django_template          | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                       |
| 2to3                     | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| sympy_sum                | 155 ms                                                           | 164 ms: 1.06x slower                                                        |
| hexiom                   | 6.35 ms                                                          | 6.75 ms: 1.06x slower                                                       |
| sympy_expand             | 501 ms                                                           | 533 ms: 1.06x slower                                                        |
| sympy_str                | 295 ms                                                           | 314 ms: 1.06x slower                                                        |
| async_generators         | 363 ms                                                           | 389 ms: 1.07x slower                                                        |
| python_startup_no_site   | 8.85 ms                                                          | 9.50 ms: 1.07x slower                                                       |
| bench_thread_pool        | 908 us                                                           | 975 us: 1.07x slower                                                        |
| comprehensions           | 17.0 us                                                          | 18.3 us: 1.08x slower                                                       |
| sqlglot_optimize         | 59.5 ms                                                          | 64.4 ms: 1.08x slower                                                       |
| logging_silent           | 96.3 ns                                                          | 104 ns: 1.08x slower                                                        |
| typing_runtime_protocols | 171 us                                                           | 185 us: 1.08x slower                                                        |
| deltablue                | 3.37 ms                                                          | 3.66 ms: 1.09x slower                                                       |
| nqueens                  | 88.4 ms                                                          | 96.2 ms: 1.09x slower                                                       |
| sqlglot_normalize        | 120 ms                                                           | 131 ms: 1.09x slower                                                        |
| genshi_xml               | 58.1 ms                                                          | 63.5 ms: 1.09x slower                                                       |
| sympy_integrate          | 23.2 ms                                                          | 25.5 ms: 1.10x slower                                                       |
| raytrace                 | 260 ms                                                           | 287 ms: 1.10x slower                                                        |
| chaos                    | 59.6 ms                                                          | 66.1 ms: 1.11x slower                                                       |
| pylint                   | 339 ms                                                           | 379 ms: 1.12x slower                                                        |
| scimark_sor              | 119 ms                                                           | 137 ms: 1.15x slower                                                        |
| scimark_lu               | 97.5 ms                                                          | 115 ms: 1.18x slower                                                        |
| Geometric mean           | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (8): bench_mp_pool, dulwich_log, go, logging_simple, unpickle_list, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 94.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x