# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.02x faster
- HPT reliability: 94.24%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 235 ms: 1.14x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 521 ms: 1.13x faster                                                       |
| async_tree_none           | 218 ms                                                          | 199 ms: 1.10x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 251 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.1 ms: 1.35x faster                                                      |
| float          | 49.7 ms                                                         | 44.2 ms: 1.12x faster                                                      |
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 87.6 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.09x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.73 ms: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 128 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 25.3 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 505 us: 16.06x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.6 us: 1.42x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 46.1 ms: 1.38x faster                                                      |
| nbody                     | 67.6 ms                                                         | 50.1 ms: 1.35x faster                                                      |
| deepcopy                  | 220 us                                                          | 179 us: 1.22x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.08 ms: 1.20x faster                                                      |
| scimark_fft               | 171 ms                                                          | 147 ms: 1.16x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 39.8 ms: 1.14x faster                                                      |
| pyflate                   | 279 ms                                                          | 245 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 521 ms: 1.13x faster                                                       |
| float                     | 49.7 ms                                                         | 44.2 ms: 1.12x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.78 us: 1.12x faster                                                      |
| fannkuch                  | 243 ms                                                          | 220 ms: 1.11x faster                                                       |
| async_tree_none           | 218 ms                                                          | 199 ms: 1.10x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.09x faster                                                     |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 251 ms: 1.05x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.45 ms: 1.05x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.9 ms: 1.03x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 461 ms: 1.03x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.1 us: 1.02x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 944 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| logging_simple            | 5.78 us                                                         | 5.69 us: 1.02x faster                                                      |
| logging_format            | 6.22 us                                                         | 6.17 us: 1.01x faster                                                      |
| xml_etree_process         | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                      |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 70.2 ms: 1.01x slower                                                      |
| gc_traversal              | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 906 us: 1.02x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.73 ms: 1.02x slower                                                      |
| chaos                     | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                                      |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 55.0 ns: 1.04x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 128 us: 1.05x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 807 us: 1.05x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 59.7 ms: 1.05x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.5 ms: 1.06x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.6 ms: 1.06x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| richards_super            | 30.2 ms                                                         | 32.4 ms: 1.07x slower                                                      |
| raytrace                  | 162 ms                                                          | 174 ms: 1.08x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.8 ms: 1.08x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 808 us: 1.08x slower                                                       |
| generators                | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 35.5 ms: 1.09x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 189 ms: 1.09x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 71.1 ms: 1.10x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| asyncio_tcp               | 471 ms                                                          | 518 ms: 1.10x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                     |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 94.4 ms: 1.12x slower                                                      |
| coverage                  | 42.1 ms                                                         | 47.2 ms: 1.12x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 87.6 ms: 1.12x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| async_generators          | 223 ms                                                          | 253 ms: 1.13x slower                                                       |
| pylint                    | 205 ms                                                          | 232 ms: 1.14x slower                                                       |
| sympy_str                 | 159 ms                                                          | 181 ms: 1.14x slower                                                       |
| go                        | 82.1 ms                                                         | 93.3 ms: 1.14x slower                                                      |
| 2to3                      | 207 ms                                                          | 235 ms: 1.14x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 86.1 ms: 1.14x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                                      |
| django_template           | 21.7 ms                                                         | 25.3 ms: 1.17x slower                                                      |
| sympy_expand              | 271 ms                                                          | 316 ms: 1.17x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.22 ms: 1.18x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 67.7 ms: 1.20x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.60 ms: 1.24x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (7): regex_v8, json, asyncio_tcp_ssl, pycparser, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, pickle_pure_python
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 94.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown