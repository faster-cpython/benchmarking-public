# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                        |
| chameleon      | 4.80 ms                                                         | 5.07 ms: 1.06x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                      |
| html5lib       | 35.0 ms                                                         | 37.0 ms: 1.06x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 85.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 399 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 623 ms: 1.03x slower                                                        |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                       |
| float          | 49.7 ms                                                         | 43.4 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 88.6 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.0 ms: 1.04x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 51.6 ms: 1.03x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| pickle_pure_python   | 175 us                                                          | 174 us: 1.01x faster                                                        |
| xml_etree_parse      | 90.9 ms                                                         | 90.3 ms: 1.01x faster                                                       |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.70 ms: 1.02x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.60 us: 1.02x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.03x slower                                                        |
| pickle_list          | 2.90 us                                                         | 3.05 us: 1.05x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.82 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.93 ms: 1.29x faster                                                       |
| django_template | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm             | 63.7 ms                                                         | 44.1 ms: 1.44x faster                                                       |
| nbody                     | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                       |
| mako                      | 6.36 ms                                                         | 4.93 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.10 ms: 1.19x faster                                                       |
| float                     | 49.7 ms                                                         | 43.4 ms: 1.15x faster                                                       |
| scimark_fft               | 171 ms                                                          | 150 ms: 1.14x faster                                                        |
| fannkuch                  | 243 ms                                                          | 216 ms: 1.13x faster                                                        |
| crypto_pyaes              | 45.5 ms                                                         | 41.0 ms: 1.11x faster                                                       |
| pyflate                   | 279 ms                                                          | 257 ms: 1.09x faster                                                        |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.6 us: 1.07x faster                                                       |
| pprint_safe_repr          | 474 ms                                                          | 446 ms: 1.06x faster                                                        |
| pprint_pformat            | 966 ms                                                          | 924 ms: 1.05x faster                                                        |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.0 ms: 1.04x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 51.6 ms: 1.03x faster                                                       |
| pickle_dict               | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.55 ms: 1.03x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.2 ms: 1.02x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                                       |
| pickle_pure_python        | 175 us                                                          | 174 us: 1.01x faster                                                        |
| xml_etree_parse           | 90.9 ms                                                         | 90.3 ms: 1.01x faster                                                       |
| sqlite_synth              | 1.60 us                                                         | 1.59 us: 1.01x faster                                                       |
| pickle                    | 7.11 us                                                         | 7.17 us: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.29 us: 1.01x slower                                                       |
| logging_simple            | 5.78 us                                                         | 5.87 us: 1.01x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.70 ms: 1.02x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.60 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 399 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 623 ms: 1.03x slower                                                        |
| unpickle_pure_python      | 122 us                                                          | 126 us: 1.03x slower                                                        |
| create_gc_cycles          | 888 us                                                          | 920 us: 1.04x slower                                                        |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.04x slower                                                       |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                        |
| meteor_contest            | 69.9 ms                                                         | 72.8 ms: 1.04x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 85.9 ms: 1.05x slower                                                       |
| pickle_list               | 2.90 us                                                         | 3.05 us: 1.05x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                        |
| chameleon                 | 4.80 ms                                                         | 5.07 ms: 1.06x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                        |
| pathlib                   | 75.9 ms                                                         | 80.2 ms: 1.06x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 37.0 ms: 1.06x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 55.9 ns: 1.06x slower                                                       |
| coverage                  | 42.1 ms                                                         | 44.5 ms: 1.06x slower                                                       |
| aiohttp                   | 889 us                                                          | 940 us: 1.06x slower                                                        |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.58 sec: 1.06x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 800 us: 1.07x slower                                                        |
| deepcopy_reduce           | 1.99 us                                                         | 2.14 us: 1.07x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.82 us: 1.08x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                       |
| raytrace                  | 162 ms                                                          | 175 ms: 1.08x slower                                                        |
| deepcopy                  | 220 us                                                          | 238 us: 1.08x slower                                                        |
| nqueens                   | 56.7 ms                                                         | 61.4 ms: 1.08x slower                                                       |
| python_startup            | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                       |
| richards                  | 26.7 ms                                                         | 29.1 ms: 1.09x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 82.2 ms: 1.09x slower                                                       |
| richards_super            | 30.2 ms                                                         | 33.0 ms: 1.09x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 93.1 ms: 1.10x slower                                                       |
| generators                | 19.6 ms                                                         | 21.6 ms: 1.10x slower                                                       |
| dulwich_log               | 38.0 ms                                                         | 42.1 ms: 1.11x slower                                                       |
| async_generators          | 223 ms                                                          | 248 ms: 1.11x slower                                                        |
| mdp                       | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                        |
| sqlglot_optimize          | 32.7 ms                                                         | 36.7 ms: 1.12x slower                                                       |
| sympy_str                 | 159 ms                                                          | 179 ms: 1.12x slower                                                        |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.13x slower                                                       |
| 2to3                      | 207 ms                                                          | 234 ms: 1.13x slower                                                        |
| regex_compile             | 78.0 ms                                                         | 88.6 ms: 1.14x slower                                                       |
| go                        | 82.1 ms                                                         | 93.6 ms: 1.14x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 73.9 ms: 1.14x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.28 ms: 1.14x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.15x slower                                                       |
| sympy_expand              | 271 ms                                                          | 311 ms: 1.15x slower                                                        |
| pylint                    | 205 ms                                                          | 238 ms: 1.16x slower                                                        |
| mypy2                     | 418 ms                                                          | 488 ms: 1.17x slower                                                        |
| django_template           | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 572 ms: 1.21x slower                                                        |
| bench_thread_pool         | 768 us                                                          | 944 us: 1.23x slower                                                        |
| hexiom                    | 3.72 ms                                                         | 4.67 ms: 1.25x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 72.2 ms: 1.28x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (11): json, regex_effbot, json_loads, flaskblogging, xml_etree_process, regex_dna, pidigits, pycparser, async_tree_cpu_io_mixed_tg, regex_v8, async_tree_io
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown