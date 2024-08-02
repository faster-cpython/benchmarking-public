# Results vs. 3.13.0b2

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-amd64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.00x slower
- HPT reliability: 98.40%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 37.3 ms: 1.07x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 83.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 540 ms: 1.09x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 190 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.2 ms: 1.35x faster                                                      |
| float          | 49.7 ms                                                         | 45.7 ms: 1.09x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 88.5 ms: 1.13x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 22.3 ms: 1.41x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.07x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.0 ms: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.00x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 53.4 ms: 1.00x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 178 us: 1.02x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.85 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 38.1 ms: 1.05x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 135 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.8 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.21 ms: 1.22x faster                                                      |
| django_template | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.2 ms: 1.27x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 46.2 ms: 1.46x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 533 us: 15.21x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.9 us: 1.39x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 46.9 ms: 1.36x faster                                                      |
| nbody                     | 67.6 ms                                                         | 50.2 ms: 1.35x faster                                                      |
| deepcopy                  | 220 us                                                          | 179 us: 1.23x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.21 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 528 ms: 1.15x faster                                                       |
| scimark_fft               | 171 ms                                                          | 152 ms: 1.12x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| fannkuch                  | 243 ms                                                          | 223 ms: 1.09x faster                                                       |
| float                     | 49.7 ms                                                         | 45.7 ms: 1.09x faster                                                      |
| async_tree_io             | 588 ms                                                          | 540 ms: 1.09x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.85 us: 1.08x faster                                                      |
| json                      | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.27 sec: 1.07x faster                                                     |
| async_tree_none_tg        | 202 ms                                                          | 190 ms: 1.06x faster                                                       |
| pyflate                   | 279 ms                                                          | 263 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.54 ms: 1.03x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 61.0 ms: 1.02x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.5 ms: 1.02x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.00x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 53.4 ms: 1.00x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.83 us: 1.01x slower                                                      |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 178 us: 1.02x slower                                                       |
| comprehensions            | 10.4 us                                                         | 10.6 us: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 985 ms: 1.02x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 906 us: 1.02x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 83.7 ms: 1.02x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 486 ms: 1.03x slower                                                       |
| python_startup            | 20.3 ms                                                         | 20.8 ms: 1.03x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.85 ms: 1.04x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.1 ms: 1.05x slower                                                      |
| chaos                     | 38.4 ms                                                         | 40.6 ms: 1.06x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 37.3 ms: 1.07x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 69.1 ms: 1.07x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 75.0 ms: 1.07x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.41 sec: 1.07x slower                                                     |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| nqueens                   | 56.7 ms                                                         | 61.9 ms: 1.09x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.05 ms: 1.10x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 823 us: 1.10x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 92.9 ms: 1.10x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 36.2 ms: 1.11x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 135 us: 1.11x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 59.2 ns: 1.12x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 194 ms: 1.12x slower                                                       |
| sympy_str                 | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| richards_super            | 30.2 ms                                                         | 33.9 ms: 1.13x slower                                                      |
| 2to3                      | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 88.5 ms: 1.13x slower                                                      |
| sympy_expand              | 271 ms                                                          | 307 ms: 1.13x slower                                                       |
| richards                  | 26.7 ms                                                         | 30.3 ms: 1.14x slower                                                      |
| raytrace                  | 162 ms                                                          | 185 ms: 1.14x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.14x slower                                                      |
| coverage                  | 42.1 ms                                                         | 48.2 ms: 1.15x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 116 us: 1.15x slower                                                       |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                       |
| go                        | 82.1 ms                                                         | 94.7 ms: 1.15x slower                                                      |
| coroutines                | 12.8 ms                                                         | 14.8 ms: 1.16x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 88.6 ms: 1.18x slower                                                      |
| django_template           | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| async_generators          | 223 ms                                                          | 272 ms: 1.22x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.31 ms: 1.23x slower                                                      |
| generators                | 19.6 ms                                                         | 24.5 ms: 1.25x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.69 ms: 1.26x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.2 ms: 1.27x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 73.4 ms: 1.30x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 22.3 ms: 1.41x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 46.2 ms: 1.46x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (10): async_tree_memoization, asyncio_tcp_ssl, async_tree_cpu_io_mixed, pathlib, gc_traversal, logging_format, asyncio_tcp, async_tree_cpu_io_mixed_tg, bench_thread_pool, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.40% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown