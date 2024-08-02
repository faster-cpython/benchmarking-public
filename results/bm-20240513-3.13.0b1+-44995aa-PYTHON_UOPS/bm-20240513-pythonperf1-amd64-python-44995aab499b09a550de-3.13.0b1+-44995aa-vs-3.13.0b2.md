# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                        |
| chameleon      | 4.80 ms                                                         | 5.12 ms: 1.07x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                      |
| html5lib       | 35.0 ms                                                         | 41.3 ms: 1.18x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 87.9 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 401 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 628 ms: 1.04x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 280 ms: 1.06x slower                                                        |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.06x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 216 ms: 1.07x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 51.7 ms: 1.04x slower                                                       |
| nbody          | 67.6 ms                                                         | 72.7 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                                        |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 107 ms: 1.38x slower                                                        |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 88.5 ms: 1.03x faster                                                       |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| pickle               | 7.11 us                                                         | 7.16 us: 1.01x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.71 ms: 1.02x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.73 us: 1.04x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.42 sec: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 56.1 ms: 1.06x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 38.9 ms: 1.07x slower                                                       |
| pickle_list          | 2.90 us                                                         | 3.11 us: 1.07x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                        |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.27x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.6 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                       |
| mako            | 6.36 ms                                                         | 7.20 ms: 1.13x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 36.5 ms: 1.15x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 16.7 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                      | 3.19 ms                                                         | 2.88 ms: 1.11x faster                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 88.5 ms: 1.03x faster                                                       |
| regex_dna                 | 119 ms                                                          | 116 ms: 1.02x faster                                                        |
| regex_effbot              | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                       |
| coroutines                | 12.8 ms                                                         | 12.6 ms: 1.01x faster                                                       |
| generators                | 19.6 ms                                                         | 19.4 ms: 1.01x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| pickle                    | 7.11 us                                                         | 7.16 us: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                       |
| sqlite_synth              | 1.60 us                                                         | 1.62 us: 1.01x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.71 ms: 1.02x slower                                                       |
| pickle_dict               | 18.1 us                                                         | 18.5 us: 1.02x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 16.6 ms: 1.03x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 914 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 401 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 628 ms: 1.04x slower                                                        |
| float                     | 49.7 ms                                                         | 51.7 ms: 1.04x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.73 us: 1.04x slower                                                       |
| telco                     | 4.67 ms                                                         | 4.88 ms: 1.05x slower                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.55 sec: 1.05x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.42 sec: 1.05x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 79.9 ms: 1.05x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 68.3 ms: 1.05x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 56.1 ms: 1.06x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 280 ms: 1.06x slower                                                        |
| coverage                  | 42.1 ms                                                         | 44.6 ms: 1.06x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.60 us: 1.06x slower                                                       |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.06x slower                                                        |
| chameleon                 | 4.80 ms                                                         | 5.12 ms: 1.07x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 38.9 ms: 1.07x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.17 us: 1.07x slower                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 2.13 us: 1.07x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.5 ms: 1.07x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 216 ms: 1.07x slower                                                        |
| pickle_list               | 2.90 us                                                         | 3.11 us: 1.07x slower                                                       |
| aiohttp                   | 889 us                                                          | 953 us: 1.07x slower                                                        |
| fannkuch                  | 243 ms                                                          | 261 ms: 1.07x slower                                                        |
| tornado_http              | 81.8 ms                                                         | 87.9 ms: 1.07x slower                                                       |
| nbody                     | 67.6 ms                                                         | 72.7 ms: 1.07x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 75.3 ms: 1.08x slower                                                       |
| async_generators          | 223 ms                                                          | 241 ms: 1.08x slower                                                        |
| richards_super            | 30.2 ms                                                         | 32.6 ms: 1.08x slower                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 49.3 ms: 1.08x slower                                                       |
| scimark_fft               | 171 ms                                                          | 190 ms: 1.11x slower                                                        |
| pprint_safe_repr          | 474 ms                                                          | 532 ms: 1.12x slower                                                        |
| raytrace                  | 162 ms                                                          | 182 ms: 1.12x slower                                                        |
| docutils                  | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.09 sec: 1.13x slower                                                      |
| django_template           | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                       |
| deepcopy                  | 220 us                                                          | 248 us: 1.13x slower                                                        |
| chaos                     | 38.4 ms                                                         | 43.3 ms: 1.13x slower                                                       |
| 2to3                      | 207 ms                                                          | 234 ms: 1.13x slower                                                        |
| bench_thread_pool         | 768 us                                                          | 868 us: 1.13x slower                                                        |
| mako                      | 6.36 ms                                                         | 7.20 ms: 1.13x slower                                                       |
| pylint                    | 205 ms                                                          | 232 ms: 1.13x slower                                                        |
| typing_runtime_protocols  | 101 us                                                          | 115 us: 1.14x slower                                                        |
| pyflate                   | 279 ms                                                          | 321 ms: 1.15x slower                                                        |
| scimark_sor               | 75.3 ms                                                         | 86.8 ms: 1.15x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.88 ms: 1.15x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 65.3 ms: 1.15x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 36.5 ms: 1.15x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 16.7 ms: 1.16x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.52 sec: 1.16x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.11 ms: 1.16x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 869 us: 1.16x slower                                                        |
| sympy_sum                 | 84.4 ms                                                         | 98.4 ms: 1.17x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 38.2 ms: 1.17x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 41.3 ms: 1.18x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.6 ms: 1.19x slower                                                       |
| spectral_norm             | 63.7 ms                                                         | 76.0 ms: 1.19x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.71 ms: 1.20x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 212 us: 1.21x slower                                                        |
| dulwich_log               | 38.0 ms                                                         | 46.0 ms: 1.21x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 47.4 ms: 1.21x slower                                                       |
| go                        | 82.1 ms                                                         | 99.6 ms: 1.21x slower                                                       |
| sympy_str                 | 159 ms                                                          | 194 ms: 1.22x slower                                                        |
| asyncio_tcp               | 471 ms                                                          | 578 ms: 1.23x slower                                                        |
| sympy_expand              | 271 ms                                                          | 332 ms: 1.23x slower                                                        |
| deepcopy_memo             | 22.1 us                                                         | 27.8 us: 1.26x slower                                                       |
| comprehensions            | 10.4 us                                                         | 13.1 us: 1.26x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 155 us: 1.27x slower                                                        |
| logging_silent            | 52.9 ns                                                         | 69.1 ns: 1.30x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 74.9 ms: 1.32x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.54 ms: 1.35x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 107 ms: 1.38x slower                                                        |
| hexiom                    | 3.72 ms                                                         | 5.23 ms: 1.40x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.10x slower                                                                |

Benchmark hidden because not significant (8): regex_v8, unpickle, python_startup, flaskblogging, pidigits, async_tree_cpu_io_mixed_tg, pycparser, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown