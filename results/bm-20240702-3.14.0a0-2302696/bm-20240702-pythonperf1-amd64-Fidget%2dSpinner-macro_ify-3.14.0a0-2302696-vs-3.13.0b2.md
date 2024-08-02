# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-amd64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.04x slower                                                      |
| html5lib       | 35.0 ms                                                         | 36.1 ms: 1.03x slower                                                     |
| tornado_http   | 81.8 ms                                                         | 80.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                           | 1.01x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 514 ms: 1.18x faster                                                      |
| async_tree_io             | 588 ms                                                          | 517 ms: 1.14x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 183 ms: 1.11x faster                                                      |
| async_tree_none           | 218 ms                                                          | 201 ms: 1.08x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 238 ms: 1.08x faster                                                      |
| async_tree_memoization    | 264 ms                                                          | 245 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 376 ms: 1.04x faster                                                      |
| Geometric mean            | (ref)                                                           | 1.09x faster                                                              |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                      |
| float          | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                                     |
| nbody          | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                           | 1.04x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                     |
| regex_dna      | 119 ms                                                          | 118 ms: 1.00x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 79.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                           | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                     |
| json_dumps           | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                     |
| xml_etree_parse      | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                                     |
| xml_etree_process    | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 185 us: 1.05x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 131 us: 1.08x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                                     |
| python_startup_no_site | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 32.7 ms: 1.04x slower                                                     |
| django_template | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                     |
| genshi_text     | 14.4 ms                                                         | 15.3 ms: 1.06x slower                                                     |
| mako            | 6.36 ms                                                         | 6.78 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 510 us: 15.89x faster                                                     |
| deepcopy                  | 220 us                                                          | 173 us: 1.27x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 18.4 us: 1.20x faster                                                     |
| async_tree_io_tg          | 605 ms                                                          | 514 ms: 1.18x faster                                                      |
| async_tree_io             | 588 ms                                                          | 517 ms: 1.14x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.76 us: 1.14x faster                                                     |
| async_tree_none_tg        | 202 ms                                                          | 183 ms: 1.11x faster                                                      |
| async_tree_none           | 218 ms                                                          | 201 ms: 1.08x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 238 ms: 1.08x faster                                                      |
| async_tree_memoization    | 264 ms                                                          | 245 ms: 1.08x faster                                                      |
| regex_v8                  | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 376 ms: 1.04x faster                                                      |
| bench_thread_pool         | 768 us                                                          | 748 us: 1.03x faster                                                      |
| tornado_http              | 81.8 ms                                                         | 80.2 ms: 1.02x faster                                                     |
| spectral_norm             | 63.7 ms                                                         | 63.2 ms: 1.01x faster                                                     |
| telco                     | 4.67 ms                                                         | 4.64 ms: 1.01x faster                                                     |
| pathlib                   | 75.9 ms                                                         | 75.4 ms: 1.01x faster                                                     |
| gc_traversal              | 1.55 ms                                                         | 1.55 ms: 1.01x faster                                                     |
| regex_dna                 | 119 ms                                                          | 118 ms: 1.00x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                      |
| scimark_lu                | 56.6 ms                                                         | 57.0 ms: 1.01x slower                                                     |
| bench_mp_pool             | 64.8 ms                                                         | 65.4 ms: 1.01x slower                                                     |
| richards_super            | 30.2 ms                                                         | 30.5 ms: 1.01x slower                                                     |
| json_loads                | 14.2 us                                                         | 14.4 us: 1.01x slower                                                     |
| sympy_sum                 | 84.4 ms                                                         | 85.6 ms: 1.01x slower                                                     |
| comprehensions            | 10.4 us                                                         | 10.5 us: 1.02x slower                                                     |
| richards                  | 26.7 ms                                                         | 27.2 ms: 1.02x slower                                                     |
| python_startup            | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                                     |
| regex_compile             | 78.0 ms                                                         | 79.4 ms: 1.02x slower                                                     |
| sqlglot_optimize          | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                                     |
| asyncio_tcp               | 471 ms                                                          | 482 ms: 1.02x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.5 ms: 1.02x slower                                                     |
| json_dumps                | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                     |
| xml_etree_parse           | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                     |
| sympy_str                 | 159 ms                                                          | 163 ms: 1.03x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 178 ms: 1.03x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 36.1 ms: 1.03x slower                                                     |
| crypto_pyaes              | 45.5 ms                                                         | 46.9 ms: 1.03x slower                                                     |
| logging_simple            | 5.78 us                                                         | 5.96 us: 1.03x slower                                                     |
| sympy_expand              | 271 ms                                                          | 279 ms: 1.03x slower                                                      |
| chaos                     | 38.4 ms                                                         | 39.6 ms: 1.03x slower                                                     |
| logging_format            | 6.22 us                                                         | 6.43 us: 1.03x slower                                                     |
| nqueens                   | 56.7 ms                                                         | 58.7 ms: 1.04x slower                                                     |
| genshi_xml                | 31.6 ms                                                         | 32.7 ms: 1.04x slower                                                     |
| async_generators          | 223 ms                                                          | 231 ms: 1.04x slower                                                      |
| django_template           | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                     |
| raytrace                  | 162 ms                                                          | 168 ms: 1.04x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                                     |
| 2to3                      | 207 ms                                                          | 216 ms: 1.04x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                     |
| coroutines                | 12.8 ms                                                         | 13.4 ms: 1.05x slower                                                     |
| go                        | 82.1 ms                                                         | 86.0 ms: 1.05x slower                                                     |
| pprint_pformat            | 966 ms                                                          | 1.02 sec: 1.05x slower                                                    |
| pprint_safe_repr          | 474 ms                                                          | 499 ms: 1.05x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 185 us: 1.05x slower                                                      |
| float                     | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                                     |
| python_startup_no_site    | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                     |
| meteor_contest            | 69.9 ms                                                         | 74.0 ms: 1.06x slower                                                     |
| pyflate                   | 279 ms                                                          | 295 ms: 1.06x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.57 sec: 1.06x slower                                                    |
| genshi_text               | 14.4 ms                                                         | 15.3 ms: 1.06x slower                                                     |
| mako                      | 6.36 ms                                                         | 6.78 ms: 1.07x slower                                                     |
| scimark_sor               | 75.3 ms                                                         | 80.4 ms: 1.07x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 3.97 ms: 1.07x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.02 ms: 1.07x slower                                                     |
| deltablue                 | 1.88 ms                                                         | 2.02 ms: 1.07x slower                                                     |
| coverage                  | 42.1 ms                                                         | 45.2 ms: 1.07x slower                                                     |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.69 ms: 1.08x slower                                                     |
| generators                | 19.6 ms                                                         | 21.0 ms: 1.08x slower                                                     |
| unpickle_pure_python      | 122 us                                                          | 131 us: 1.08x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 808 us: 1.08x slower                                                      |
| nbody                     | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                                     |
| tomli_loads               | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                    |
| pycparser                 | 754 ms                                                          | 819 ms: 1.09x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                    |
| logging_silent            | 52.9 ns                                                         | 57.9 ns: 1.09x slower                                                     |
| scimark_monte_carlo       | 39.1 ms                                                         | 43.3 ms: 1.11x slower                                                     |
| scimark_fft               | 171 ms                                                          | 194 ms: 1.14x slower                                                      |
| fannkuch                  | 243 ms                                                          | 277 ms: 1.14x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, create_gc_cycles, json, docutils, pylint, regex_effbot, typing_runtime_protocols, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown