# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.03x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 536 ms: 1.10x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 191 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 383 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 78.5 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 89.0 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.97 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.5 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.6 ms: 1.11x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 204 us: 1.16x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 23.9 ms: 1.10x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| mako            | 6.36 ms                                                         | 7.37 ms: 1.16x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.2 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 522 us: 15.54x faster                                                      |
| deepcopy                  | 220 us                                                          | 181 us: 1.21x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 536 ms: 1.10x faster                                                       |
| json                      | 3.19 ms                                                         | 2.95 ms: 1.08x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.86 us: 1.07x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.8 us: 1.06x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 191 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| pathlib                   | 75.9 ms                                                         | 74.1 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 383 ms: 1.02x faster                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 151 ms: 1.00x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 65.2 ms: 1.01x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 793 us: 1.03x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.68 sec: 1.03x slower                                                     |
| python_startup            | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.86 ms: 1.04x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.6 ms: 1.05x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 106 us: 1.05x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.60 us: 1.06x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.97 ms: 1.06x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.5 ms: 1.07x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 185 ms: 1.07x slower                                                       |
| coroutines                | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                      |
| logging_simple            | 5.78 us                                                         | 6.21 us: 1.07x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 75.7 ms: 1.08x slower                                                      |
| 2to3                      | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| async_generators          | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| sympy_str                 | 159 ms                                                          | 173 ms: 1.09x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                      |
| sympy_expand              | 271 ms                                                          | 296 ms: 1.09x slower                                                       |
| coverage                  | 42.1 ms                                                         | 46.2 ms: 1.10x slower                                                      |
| django_template           | 21.7 ms                                                         | 23.9 ms: 1.10x slower                                                      |
| pyflate                   | 279 ms                                                          | 309 ms: 1.11x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 62.9 ms: 1.11x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 40.6 ms: 1.11x slower                                                      |
| raytrace                  | 162 ms                                                          | 181 ms: 1.11x slower                                                       |
| comprehensions            | 10.4 us                                                         | 11.6 us: 1.12x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.08 ms: 1.13x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 72.4 ms: 1.14x slower                                                      |
| generators                | 19.6 ms                                                         | 22.2 ms: 1.14x slower                                                      |
| float                     | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 89.0 ms: 1.14x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 52.0 ms: 1.14x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.10 sec: 1.14x slower                                                     |
| genshi_text               | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.6 ms: 1.15x slower                                                      |
| chaos                     | 38.4 ms                                                         | 44.0 ms: 1.15x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.7 ms: 1.15x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 546 ms: 1.15x slower                                                       |
| mako                      | 6.36 ms                                                         | 7.37 ms: 1.16x slower                                                      |
| nbody                     | 67.6 ms                                                         | 78.5 ms: 1.16x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| pickle_pure_python        | 175 us                                                          | 204 us: 1.16x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.53 sec: 1.17x slower                                                     |
| scimark_lu                | 56.6 ms                                                         | 66.2 ms: 1.17x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.93 ms: 1.17x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 878 us: 1.17x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.21 ms: 1.17x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 37.2 ms: 1.18x slower                                                      |
| go                        | 82.1 ms                                                         | 97.0 ms: 1.18x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 63.5 ns: 1.20x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 90.7 ms: 1.20x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.51 ms: 1.21x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 150 us: 1.23x slower                                                       |
| fannkuch                  | 243 ms                                                          | 304 ms: 1.25x slower                                                       |
| scimark_fft               | 171 ms                                                          | 216 ms: 1.26x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 52.0 ms: 1.33x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, tornado_http, regex_effbot, regex_dna, json_loads, asyncio_tcp, create_gc_cycles, async_tree_cpu_io_mixed_tg, pylint, pycparser, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown