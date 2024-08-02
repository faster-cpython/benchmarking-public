# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.3 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 195 ms: 1.04x faster                                                       |
| async_tree_io             | 588 ms                                                          | 569 ms: 1.03x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 57.4 ms: 1.16x slower                                                      |
| nbody          | 67.6 ms                                                         | 82.2 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 118 ms: 1.00x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.8 us: 1.03x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.7 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.0 ms: 1.15x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 211 us: 1.20x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 156 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                      |
| mako            | 6.36 ms                                                         | 7.85 ms: 1.23x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 536 us: 15.12x faster                                                      |
| deepcopy                  | 220 us                                                          | 185 us: 1.19x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.89 us: 1.05x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 195 ms: 1.04x faster                                                       |
| async_tree_io             | 588 ms                                                          | 569 ms: 1.03x faster                                                       |
| json_loads                | 14.2 us                                                         | 13.8 us: 1.03x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 21.6 us: 1.02x faster                                                      |
| regex_dna                 | 119 ms                                                          | 118 ms: 1.00x faster                                                       |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 65.8 ms: 1.02x slower                                                      |
| python_startup            | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| telco                     | 4.67 ms                                                         | 4.86 ms: 1.04x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 491 ms: 1.04x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.9 ms: 1.05x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 13.2 ms: 1.07x slower                                                      |
| coverage                  | 42.1 ms                                                         | 45.4 ms: 1.08x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.72 us: 1.08x slower                                                      |
| sympy_expand              | 271 ms                                                          | 292 ms: 1.08x slower                                                       |
| sympy_str                 | 159 ms                                                          | 172 ms: 1.08x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.28 us: 1.09x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 35.6 ms: 1.09x slower                                                      |
| 2to3                      | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 38.3 ms: 1.09x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| sqlglot_normalize         | 173 ms                                                          | 191 ms: 1.10x slower                                                       |
| raytrace                  | 162 ms                                                          | 180 ms: 1.11x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 62.7 ms: 1.11x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 77.4 ms: 1.11x slower                                                      |
| async_generators          | 223 ms                                                          | 248 ms: 1.11x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 59.7 ms: 1.12x slower                                                      |
| django_template           | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 73.2 ms: 1.15x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.7 ms: 1.15x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 42.0 ms: 1.15x slower                                                      |
| float                     | 49.7 ms                                                         | 57.4 ms: 1.16x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 52.6 ms: 1.16x slower                                                      |
| coroutines                | 12.8 ms                                                         | 14.8 ms: 1.16x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.9 ms: 1.16x slower                                                      |
| go                        | 82.1 ms                                                         | 95.1 ms: 1.16x slower                                                      |
| comprehensions            | 10.4 us                                                         | 12.0 us: 1.16x slower                                                      |
| chaos                     | 38.4 ms                                                         | 44.6 ms: 1.16x slower                                                      |
| pyflate                   | 279 ms                                                          | 324 ms: 1.16x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.13 sec: 1.17x slower                                                     |
| pprint_safe_repr          | 474 ms                                                          | 556 ms: 1.17x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.12 ms: 1.18x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 67.0 ms: 1.18x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 89.4 ms: 1.19x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.24 ms: 1.19x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 211 us: 1.20x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 902 us: 1.21x slower                                                       |
| generators                | 19.6 ms                                                         | 23.6 ms: 1.21x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 4.50 ms: 1.21x slower                                                      |
| nbody                     | 67.6 ms                                                         | 82.2 ms: 1.22x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 64.6 ns: 1.22x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 3.07 ms: 1.23x slower                                                      |
| mako                      | 6.36 ms                                                         | 7.85 ms: 1.23x slower                                                      |
| fannkuch                  | 243 ms                                                          | 303 ms: 1.25x slower                                                       |
| scimark_fft               | 171 ms                                                          | 215 ms: 1.26x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 50.0 ms: 1.28x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 156 us: 1.28x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (15): json, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, gc_traversal, regex_effbot, pathlib, bench_thread_pool, tornado_http, create_gc_cycles, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, pycparser, pylint, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown