# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.01x slower
- HPT reliability: 95.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                      |
| chameleon      | 7.40 ms                                                          | 7.66 ms: 1.04x slower                                                     |
| html5lib       | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                     |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                            | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 365 ms                                                           | 377 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 604 ms                                                           | 627 ms: 1.04x slower                                                      |
| async_tree_io           | 873 ms                                                           | 909 ms: 1.04x slower                                                      |
| async_tree_memoization  | 460 ms                                                           | 480 ms: 1.04x slower                                                      |
| Geometric mean          | (ref)                                                            | 1.03x slower                                                              |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                     |
| float          | 80.2 ms                                                          | 77.6 ms: 1.03x faster                                                     |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                            | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                      |
| regex_dna      | 249 ms                                                           | 243 ms: 1.02x faster                                                      |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                     |
| regex_effbot   | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                            | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.08 sec: 1.16x faster                                                    |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                      |
| unpickle             | 15.7 us                                                          | 14.9 us: 1.05x faster                                                     |
| xml_etree_generate   | 85.7 ms                                                          | 82.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                      |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                     |
| pickle_dict          | 32.8 us                                                          | 32.4 us: 1.01x faster                                                     |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                     |
| pickle_list          | 4.44 us                                                          | 4.40 us: 1.01x faster                                                     |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                     |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                                      |
| xml_etree_parse      | 144 ms                                                           | 146 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                     |
| python_startup_no_site | 8.85 ms                                                          | 9.45 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                            | 1.04x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.10 ms: 1.14x faster                                                     |
| django_template | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                     |
| genshi_text     | 25.9 ms                                                          | 28.2 ms: 1.09x slower                                                     |
| genshi_xml      | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                            | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards                 | 53.4 ms                                                          | 43.8 ms: 1.22x faster                                                     |
| richards_super           | 61.2 ms                                                          | 50.9 ms: 1.20x faster                                                     |
| spectral_norm            | 97.3 ms                                                          | 82.2 ms: 1.18x faster                                                     |
| tomli_loads              | 2.40 sec                                                         | 2.08 sec: 1.16x faster                                                    |
| mako                     | 10.4 ms                                                          | 9.10 ms: 1.14x faster                                                     |
| pyflate                  | 482 ms                                                           | 447 ms: 1.08x faster                                                      |
| scimark_fft              | 312 ms                                                           | 291 ms: 1.07x faster                                                      |
| unpickle_pure_python     | 224 us                                                           | 213 us: 1.05x faster                                                      |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.07 ms: 1.05x faster                                                     |
| unpickle                 | 15.7 us                                                          | 14.9 us: 1.05x faster                                                     |
| nbody                    | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                     |
| xml_etree_generate       | 85.7 ms                                                          | 82.2 ms: 1.04x faster                                                     |
| pathlib                  | 17.1 ms                                                          | 16.4 ms: 1.04x faster                                                     |
| regex_compile            | 144 ms                                                           | 139 ms: 1.04x faster                                                      |
| crypto_pyaes             | 73.6 ms                                                          | 71.1 ms: 1.03x faster                                                     |
| coroutines               | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                     |
| float                    | 80.2 ms                                                          | 77.6 ms: 1.03x faster                                                     |
| telco                    | 8.40 ms                                                          | 8.14 ms: 1.03x faster                                                     |
| go                       | 165 ms                                                           | 160 ms: 1.03x faster                                                      |
| regex_dna                | 249 ms                                                           | 243 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 103 ms                                                           | 100 ms: 1.02x faster                                                      |
| fannkuch                 | 353 ms                                                           | 345 ms: 1.02x faster                                                      |
| pprint_safe_repr         | 818 ms                                                           | 802 ms: 1.02x faster                                                      |
| regex_v8                 | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                     |
| html5lib                 | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                     |
| pprint_pformat           | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                    |
| json_loads               | 25.0 us                                                          | 24.6 us: 1.02x faster                                                     |
| asyncio_websockets       | 395 ms                                                           | 389 ms: 1.02x faster                                                      |
| json                     | 5.35 ms                                                          | 5.28 ms: 1.01x faster                                                     |
| pickle_dict              | 32.8 us                                                          | 32.4 us: 1.01x faster                                                     |
| json_dumps               | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                     |
| sqlite_synth             | 2.80 us                                                          | 2.76 us: 1.01x faster                                                     |
| dulwich_log              | 67.3 ms                                                          | 66.5 ms: 1.01x faster                                                     |
| coverage                 | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                                     |
| pickle_list              | 4.44 us                                                          | 4.40 us: 1.01x faster                                                     |
| pidigits                 | 254 ms                                                           | 251 ms: 1.01x faster                                                      |
| xml_etree_process        | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                    |
| pickle_pure_python       | 307 us                                                           | 311 us: 1.01x slower                                                      |
| logging_format           | 7.11 us                                                          | 7.22 us: 1.02x slower                                                     |
| xml_etree_parse          | 144 ms                                                           | 146 ms: 1.02x slower                                                      |
| sqlglot_parse            | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                     |
| python_startup           | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                     |
| pycparser                | 1.22 sec                                                         | 1.25 sec: 1.03x slower                                                    |
| logging_simple           | 6.40 us                                                          | 6.58 us: 1.03x slower                                                     |
| tornado_http             | 119 ms                                                           | 123 ms: 1.03x slower                                                      |
| sqlglot_transpile        | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                     |
| async_tree_none          | 365 ms                                                           | 377 ms: 1.03x slower                                                      |
| mdp                      | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                    |
| chameleon                | 7.40 ms                                                          | 7.66 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 627 ms: 1.04x slower                                                      |
| generators               | 33.5 ms                                                          | 34.8 ms: 1.04x slower                                                     |
| dask                     | 391 ms                                                           | 406 ms: 1.04x slower                                                      |
| async_tree_io            | 873 ms                                                           | 909 ms: 1.04x slower                                                      |
| thrift                   | 880 us                                                           | 916 us: 1.04x slower                                                      |
| bench_thread_pool        | 908 us                                                           | 948 us: 1.04x slower                                                      |
| async_tree_memoization   | 460 ms                                                           | 480 ms: 1.04x slower                                                      |
| 2to3                     | 291 ms                                                           | 305 ms: 1.05x slower                                                      |
| flaskblogging            | 4.68 ms                                                          | 4.91 ms: 1.05x slower                                                     |
| async_generators         | 363 ms                                                           | 381 ms: 1.05x slower                                                      |
| gc_traversal             | 4.69 ms                                                          | 4.94 ms: 1.05x slower                                                     |
| sympy_expand             | 501 ms                                                           | 528 ms: 1.06x slower                                                      |
| django_template          | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                     |
| sympy_str                | 295 ms                                                           | 312 ms: 1.06x slower                                                      |
| comprehensions           | 17.0 us                                                          | 18.0 us: 1.06x slower                                                     |
| hexiom                   | 6.35 ms                                                          | 6.74 ms: 1.06x slower                                                     |
| sqlglot_optimize         | 59.5 ms                                                          | 63.5 ms: 1.07x slower                                                     |
| logging_silent           | 96.3 ns                                                          | 103 ns: 1.07x slower                                                      |
| python_startup_no_site   | 8.85 ms                                                          | 9.45 ms: 1.07x slower                                                     |
| sympy_sum                | 155 ms                                                           | 166 ms: 1.07x slower                                                      |
| regex_effbot             | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                                     |
| typing_runtime_protocols | 171 us                                                           | 185 us: 1.08x slower                                                      |
| sqlglot_normalize        | 120 ms                                                           | 131 ms: 1.09x slower                                                      |
| deepcopy                 | 377 us                                                           | 411 us: 1.09x slower                                                      |
| genshi_text              | 25.9 ms                                                          | 28.2 ms: 1.09x slower                                                     |
| deepcopy_reduce          | 3.39 us                                                          | 3.71 us: 1.09x slower                                                     |
| scimark_sor              | 119 ms                                                           | 130 ms: 1.10x slower                                                      |
| sympy_integrate          | 23.2 ms                                                          | 25.6 ms: 1.10x slower                                                     |
| raytrace                 | 260 ms                                                           | 288 ms: 1.10x slower                                                      |
| nqueens                  | 88.4 ms                                                          | 97.8 ms: 1.11x slower                                                     |
| chaos                    | 59.6 ms                                                          | 66.1 ms: 1.11x slower                                                     |
| deltablue                | 3.37 ms                                                          | 3.75 ms: 1.11x slower                                                     |
| genshi_xml               | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                     |
| pylint                   | 339 ms                                                           | 381 ms: 1.12x slower                                                      |
| scimark_lu               | 97.5 ms                                                          | 115 ms: 1.18x slower                                                      |
| Geometric mean           | (ref)                                                            | 1.01x slower                                                              |

Benchmark hidden because not significant (12): bench_mp_pool, unpickle_list, create_gc_cycles, pickle, asyncio_tcp, meteor_contest, deepcopy_memo, scimark_monte_carlo, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, docutils, gunicorn, mypy2

# HPT report

- Reliability score: 95.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x