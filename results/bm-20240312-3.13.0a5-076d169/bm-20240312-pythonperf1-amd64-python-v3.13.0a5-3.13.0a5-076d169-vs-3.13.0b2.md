# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: windows-amd64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.05x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.84 ms: 1.01x slower                                           |
| docutils       | 1.63 sec                                                        | 1.54 sec: 1.06x faster                                          |
| html5lib       | 35.0 ms                                                         | 36.5 ms: 1.04x slower                                           |
| tornado_http   | 81.8 ms                                                         | 84.8 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 454 ms: 1.17x slower                                            |
| async_tree_none            | 218 ms                                                          | 270 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 474 ms: 1.24x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 758 ms: 1.25x slower                                            |
| async_tree_io              | 588 ms                                                          | 738 ms: 1.26x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 274 ms: 1.36x slower                                            |
| Geometric mean             | (ref)                                                           | 1.27x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| float          | 49.7 ms                                                         | 50.8 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                           |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                           |
| unpickle             | 8.40 us                                                         | 8.29 us: 1.01x faster                                           |
| xml_etree_process    | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                           |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                           |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.68 us: 1.02x slower                                           |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.02x slower                                            |
| pickle_pure_python   | 175 us                                                          | 180 us: 1.03x slower                                            |
| xml_etree_parse      | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (2): pickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.21 ms: 1.02x faster                                           |
| django_template | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                           |
| genshi_xml      | 31.6 ms                                                         | 34.6 ms: 1.10x slower                                           |
| genshi_text     | 14.4 ms                                                         | 15.8 ms: 1.10x slower                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 75.1 us: 1.34x faster                                           |
| create_gc_cycles           | 888 us                                                          | 745 us: 1.19x faster                                            |
| pycparser                  | 754 ms                                                          | 693 ms: 1.09x faster                                            |
| spectral_norm              | 63.7 ms                                                         | 59.7 ms: 1.07x faster                                           |
| crypto_pyaes               | 45.5 ms                                                         | 42.6 ms: 1.07x faster                                           |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.35 ms: 1.06x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.54 sec: 1.06x faster                                          |
| gc_traversal               | 1.55 ms                                                         | 1.50 ms: 1.04x faster                                           |
| mako                       | 6.36 ms                                                         | 6.21 ms: 1.02x faster                                           |
| deepcopy_reduce            | 1.99 us                                                         | 1.95 us: 1.02x faster                                           |
| json_loads                 | 14.2 us                                                         | 13.9 us: 1.02x faster                                           |
| scimark_lu                 | 56.6 ms                                                         | 55.5 ms: 1.02x faster                                           |
| sympy_sum                  | 84.4 ms                                                         | 82.9 ms: 1.02x faster                                           |
| pidigits                   | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| unpickle                   | 8.40 us                                                         | 8.29 us: 1.01x faster                                           |
| raytrace                   | 162 ms                                                          | 160 ms: 1.01x faster                                            |
| mypy2                      | 418 ms                                                          | 413 ms: 1.01x faster                                            |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                           |
| sympy_str                  | 159 ms                                                          | 158 ms: 1.01x faster                                            |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| sqlite_synth               | 1.60 us                                                         | 1.59 us: 1.00x faster                                           |
| sympy_expand               | 271 ms                                                          | 270 ms: 1.00x faster                                            |
| sqlglot_normalize          | 173 ms                                                          | 172 ms: 1.00x faster                                            |
| flaskblogging              | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                          |
| async_generators           | 223 ms                                                          | 224 ms: 1.00x slower                                            |
| chameleon                  | 4.80 ms                                                         | 4.84 ms: 1.01x slower                                           |
| xml_etree_process          | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                           |
| pickle                     | 7.11 us                                                         | 7.17 us: 1.01x slower                                           |
| aiohttp                    | 889 us                                                          | 896 us: 1.01x slower                                            |
| sympy_integrate            | 12.2 ms                                                         | 12.3 ms: 1.01x slower                                           |
| pyflate                    | 279 ms                                                          | 281 ms: 1.01x slower                                            |
| xml_etree_iterparse        | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                           |
| thrift                     | 8.11 ms                                                         | 8.19 ms: 1.01x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                           |
| logging_silent             | 52.9 ns                                                         | 53.5 ns: 1.01x slower                                           |
| richards_super             | 30.2 ms                                                         | 30.6 ms: 1.02x slower                                           |
| telco                      | 4.67 ms                                                         | 4.75 ms: 1.02x slower                                           |
| sqlglot_parse              | 748 us                                                          | 762 us: 1.02x slower                                            |
| django_template            | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                           |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                           |
| float                      | 49.7 ms                                                         | 50.8 ms: 1.02x slower                                           |
| unpickle_list              | 2.62 us                                                         | 2.68 us: 1.02x slower                                           |
| unpickle_pure_python       | 122 us                                                          | 125 us: 1.02x slower                                            |
| pickle_pure_python         | 175 us                                                          | 180 us: 1.03x slower                                            |
| sqlglot_transpile          | 955 us                                                          | 980 us: 1.03x slower                                            |
| pprint_pformat             | 966 ms                                                          | 992 ms: 1.03x slower                                            |
| richards                   | 26.7 ms                                                         | 27.5 ms: 1.03x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 487 ms: 1.03x slower                                            |
| bench_mp_pool              | 64.8 ms                                                         | 66.6 ms: 1.03x slower                                           |
| xml_etree_parse            | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                           |
| logging_format             | 6.22 us                                                         | 6.41 us: 1.03x slower                                           |
| coroutines                 | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                           |
| logging_simple             | 5.78 us                                                         | 5.97 us: 1.03x slower                                           |
| tornado_http               | 81.8 ms                                                         | 84.8 ms: 1.04x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 72.8 ms: 1.04x slower                                           |
| html5lib                   | 35.0 ms                                                         | 36.5 ms: 1.04x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.37 sec: 1.04x slower                                          |
| 2to3                       | 207 ms                                                          | 216 ms: 1.05x slower                                            |
| go                         | 82.1 ms                                                         | 86.1 ms: 1.05x slower                                           |
| deltablue                  | 1.88 ms                                                         | 1.98 ms: 1.05x slower                                           |
| hexiom                     | 3.72 ms                                                         | 3.91 ms: 1.05x slower                                           |
| generators                 | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                           |
| nqueens                    | 56.7 ms                                                         | 59.9 ms: 1.06x slower                                           |
| pathlib                    | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| dulwich_log                | 38.0 ms                                                         | 40.4 ms: 1.06x slower                                           |
| comprehensions             | 10.4 us                                                         | 11.0 us: 1.06x slower                                           |
| bench_thread_pool          | 768 us                                                          | 831 us: 1.08x slower                                            |
| genshi_xml                 | 31.6 ms                                                         | 34.6 ms: 1.10x slower                                           |
| genshi_text                | 14.4 ms                                                         | 15.8 ms: 1.10x slower                                           |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                           |
| coverage                   | 42.1 ms                                                         | 47.1 ms: 1.12x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 454 ms: 1.17x slower                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.80 sec: 1.22x slower                                          |
| async_tree_none            | 218 ms                                                          | 270 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 474 ms: 1.24x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 758 ms: 1.25x slower                                            |
| async_tree_io              | 588 ms                                                          | 738 ms: 1.26x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 274 ms: 1.36x slower                                            |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (17): regex_v8, pickle_list, sqlglot_optimize, fannkuch, python_startup, scimark_monte_carlo, scimark_sor, deepcopy, chaos, regex_compile, json_dumps, pylint, scimark_fft, nbody, deepcopy_memo, asyncio_tcp, json

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown