# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 231 ms: 1.12x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                               |
| html5lib       | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 546 ms: 1.11x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                         |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 152 ms: 1.01x slower                                                                 |
| float          | 49.7 ms                                                         | 56.8 ms: 1.14x slower                                                                |
| nbody          | 67.6 ms                                                         | 83.5 ms: 1.24x slower                                                                |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                                |
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                                 |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                                |
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                                |
| xml_etree_parse      | 90.9 ms                                                         | 95.9 ms: 1.05x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.8 ms: 1.06x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                                |
| json_dumps           | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 40.7 ms: 1.12x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                               |
| unpickle_pure_python | 122 us                                                          | 146 us: 1.20x slower                                                                 |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.97 ms: 1.10x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 35.8 ms: 1.13x slower                                                                |
| django_template | 21.7 ms                                                         | 24.6 ms: 1.14x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 526 us: 15.42x faster                                                                |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                                 |
| async_tree_io_tg           | 605 ms                                                          | 546 ms: 1.11x faster                                                                 |
| deepcopy_memo              | 22.1 us                                                         | 20.0 us: 1.10x faster                                                                |
| regex_v8                   | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                                |
| deepcopy_reduce            | 1.99 us                                                         | 1.90 us: 1.05x faster                                                                |
| regex_dna                  | 119 ms                                                          | 114 ms: 1.04x faster                                                                 |
| regex_effbot               | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                                |
| json_loads                 | 14.2 us                                                         | 14.0 us: 1.01x faster                                                                |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                                |
| pidigits                   | 150 ms                                                          | 152 ms: 1.01x slower                                                                 |
| create_gc_cycles           | 888 us                                                          | 910 us: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                                 |
| pathlib                    | 75.9 ms                                                         | 78.9 ms: 1.04x slower                                                                |
| crypto_pyaes               | 45.5 ms                                                         | 47.9 ms: 1.05x slower                                                                |
| bench_mp_pool              | 64.8 ms                                                         | 68.2 ms: 1.05x slower                                                                |
| xml_etree_parse            | 90.9 ms                                                         | 95.9 ms: 1.05x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.8 ms: 1.06x slower                                                                |
| generators                 | 19.6 ms                                                         | 20.8 ms: 1.06x slower                                                                |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.66 ms: 1.06x slower                                                                |
| docutils                   | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                               |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.59 sec: 1.07x slower                                                               |
| spectral_norm              | 63.7 ms                                                         | 68.3 ms: 1.07x slower                                                                |
| bench_thread_pool          | 768 us                                                          | 824 us: 1.07x slower                                                                 |
| telco                      | 4.67 ms                                                         | 5.02 ms: 1.07x slower                                                                |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                                |
| python_startup             | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                                |
| sympy_sum                  | 84.4 ms                                                         | 91.2 ms: 1.08x slower                                                                |
| logging_format             | 6.22 us                                                         | 6.77 us: 1.09x slower                                                                |
| scimark_lu                 | 56.6 ms                                                         | 61.6 ms: 1.09x slower                                                                |
| xml_etree_generate         | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                                |
| mako                       | 6.36 ms                                                         | 6.97 ms: 1.10x slower                                                                |
| logging_simple             | 5.78 us                                                         | 6.34 us: 1.10x slower                                                                |
| json_dumps                 | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                                |
| pylint                     | 205 ms                                                          | 226 ms: 1.10x slower                                                                 |
| sqlglot_normalize          | 173 ms                                                          | 192 ms: 1.11x slower                                                                 |
| sqlglot_optimize           | 32.7 ms                                                         | 36.4 ms: 1.11x slower                                                                |
| nqueens                    | 56.7 ms                                                         | 63.1 ms: 1.11x slower                                                                |
| coroutines                 | 12.8 ms                                                         | 14.2 ms: 1.11x slower                                                                |
| 2to3                       | 207 ms                                                          | 231 ms: 1.12x slower                                                                 |
| xml_etree_process          | 36.4 ms                                                         | 40.7 ms: 1.12x slower                                                                |
| async_generators           | 223 ms                                                          | 250 ms: 1.12x slower                                                                 |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                                                 |
| meteor_contest             | 69.9 ms                                                         | 78.5 ms: 1.12x slower                                                                |
| coverage                   | 42.1 ms                                                         | 47.4 ms: 1.13x slower                                                                |
| chaos                      | 38.4 ms                                                         | 43.3 ms: 1.13x slower                                                                |
| tornado_http               | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                                                |
| pyflate                    | 279 ms                                                          | 316 ms: 1.13x slower                                                                 |
| genshi_xml                 | 31.6 ms                                                         | 35.8 ms: 1.13x slower                                                                |
| dulwich_log                | 38.0 ms                                                         | 43.2 ms: 1.13x slower                                                                |
| django_template            | 21.7 ms                                                         | 24.6 ms: 1.14x slower                                                                |
| typing_runtime_protocols   | 101 us                                                          | 115 us: 1.14x slower                                                                 |
| sympy_expand               | 271 ms                                                          | 308 ms: 1.14x slower                                                                 |
| float                      | 49.7 ms                                                         | 56.8 ms: 1.14x slower                                                                |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                               |
| asyncio_tcp                | 471 ms                                                          | 540 ms: 1.15x slower                                                                 |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.15x slower                                                                |
| sqlglot_transpile          | 955 us                                                          | 1.10 ms: 1.15x slower                                                                |
| regex_compile              | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                                |
| pprint_safe_repr           | 474 ms                                                          | 551 ms: 1.16x slower                                                                 |
| tomli_loads                | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                               |
| hexiom                     | 3.72 ms                                                         | 4.33 ms: 1.16x slower                                                                |
| pprint_pformat             | 966 ms                                                          | 1.13 sec: 1.16x slower                                                               |
| pycparser                  | 754 ms                                                          | 883 ms: 1.17x slower                                                                 |
| genshi_text                | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                                |
| html5lib                   | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                                |
| logging_silent             | 52.9 ns                                                         | 62.7 ns: 1.18x slower                                                                |
| sqlglot_parse              | 748 us                                                          | 890 us: 1.19x slower                                                                 |
| scimark_fft                | 171 ms                                                          | 203 ms: 1.19x slower                                                                 |
| fannkuch                   | 243 ms                                                          | 290 ms: 1.19x slower                                                                 |
| scimark_sor                | 75.3 ms                                                         | 90.2 ms: 1.20x slower                                                                |
| raytrace                   | 162 ms                                                          | 194 ms: 1.20x slower                                                                 |
| unpickle_pure_python       | 122 us                                                          | 146 us: 1.20x slower                                                                 |
| deltablue                  | 1.88 ms                                                         | 2.27 ms: 1.21x slower                                                                |
| pickle_pure_python         | 175 us                                                          | 212 us: 1.21x slower                                                                 |
| go                         | 82.1 ms                                                         | 99.2 ms: 1.21x slower                                                                |
| richards_super             | 30.2 ms                                                         | 36.5 ms: 1.21x slower                                                                |
| richards                   | 26.7 ms                                                         | 32.5 ms: 1.22x slower                                                                |
| nbody                      | 67.6 ms                                                         | 83.5 ms: 1.24x slower                                                                |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.0 ms: 1.25x slower                                                                |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                                         |

Benchmark hidden because not significant (7): async_tree_memoization_tg, json, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown