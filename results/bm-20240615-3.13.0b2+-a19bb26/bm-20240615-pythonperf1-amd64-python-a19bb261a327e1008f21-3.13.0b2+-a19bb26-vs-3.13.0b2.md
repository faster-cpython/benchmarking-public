# Results vs. 3.13.0b2

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 4.80 ms                                                         | 4.71 ms: 1.02x faster                                                       |
| html5lib       | 35.0 ms                                                         | 35.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 615 ms: 1.02x slower                                                        |
| Geometric mean   | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| float          | 49.7 ms                                                         | 50.9 ms: 1.02x slower                                                       |
| nbody          | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 77.0 ms: 1.01x faster                                                       |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 5.61 ms                                                         | 5.51 ms: 1.02x faster                                                       |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.02x faster                                                       |
| pickle_pure_python   | 175 us                                                          | 176 us: 1.00x slower                                                        |
| xml_etree_generate   | 53.2 ms                                                         | 53.5 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 36.8 ms: 1.01x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.66 us: 1.02x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.02x slower                                                        |
| tomli_loads          | 1.35 sec                                                        | 1.38 sec: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.27 us: 1.02x slower                                                       |
| pickle_list          | 2.90 us                                                         | 3.02 us: 1.04x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.79 us: 1.05x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 19.2 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 31.1 ms: 1.01x faster                                                       |
| django_template | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 14.8 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_lu               | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                       |
| spectral_norm            | 63.7 ms                                                         | 62.0 ms: 1.03x faster                                                       |
| chameleon                | 4.80 ms                                                         | 4.71 ms: 1.02x faster                                                       |
| json_dumps               | 5.61 ms                                                         | 5.51 ms: 1.02x faster                                                       |
| thrift                   | 8.11 ms                                                         | 7.96 ms: 1.02x faster                                                       |
| raytrace                 | 162 ms                                                          | 159 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.46 ms: 1.02x faster                                                       |
| comprehensions           | 10.4 us                                                         | 10.2 us: 1.02x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 44.8 ms: 1.02x faster                                                       |
| json_loads               | 14.2 us                                                         | 14.0 us: 1.02x faster                                                       |
| genshi_xml               | 31.6 ms                                                         | 31.1 ms: 1.01x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                       |
| regex_compile            | 78.0 ms                                                         | 77.0 ms: 1.01x faster                                                       |
| pathlib                  | 75.9 ms                                                         | 75.1 ms: 1.01x faster                                                       |
| fannkuch                 | 243 ms                                                          | 241 ms: 1.01x faster                                                        |
| hexiom                   | 3.72 ms                                                         | 3.70 ms: 1.01x faster                                                       |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| chaos                    | 38.4 ms                                                         | 38.2 ms: 1.00x faster                                                       |
| pprint_safe_repr         | 474 ms                                                          | 476 ms: 1.00x slower                                                        |
| deltablue                | 1.88 ms                                                         | 1.89 ms: 1.00x slower                                                       |
| pickle_pure_python       | 175 us                                                          | 176 us: 1.00x slower                                                        |
| go                       | 82.1 ms                                                         | 82.5 ms: 1.00x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 84.9 ms: 1.01x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.0 ms: 1.01x slower                                                       |
| xml_etree_generate       | 53.2 ms                                                         | 53.5 ms: 1.01x slower                                                       |
| pyflate                  | 279 ms                                                          | 281 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| django_template          | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 36.8 ms: 1.01x slower                                                       |
| aiohttp                  | 889 us                                                          | 899 us: 1.01x slower                                                        |
| html5lib                 | 35.0 ms                                                         | 35.5 ms: 1.01x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 12.4 ms: 1.01x slower                                                       |
| mypy2                    | 418 ms                                                          | 423 ms: 1.01x slower                                                        |
| pprint_pformat           | 966 ms                                                          | 980 ms: 1.01x slower                                                        |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.01x slower                                                       |
| unpickle_list            | 2.62 us                                                         | 2.66 us: 1.02x slower                                                       |
| sqlglot_normalize        | 173 ms                                                          | 176 ms: 1.02x slower                                                        |
| async_tree_io_tg         | 605 ms                                                          | 615 ms: 1.02x slower                                                        |
| deepcopy                 | 220 us                                                          | 223 us: 1.02x slower                                                        |
| sympy_str                | 159 ms                                                          | 162 ms: 1.02x slower                                                        |
| sqlglot_optimize         | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                       |
| sympy_expand             | 271 ms                                                          | 275 ms: 1.02x slower                                                        |
| unpickle_pure_python     | 122 us                                                          | 124 us: 1.02x slower                                                        |
| telco                    | 4.67 ms                                                         | 4.76 ms: 1.02x slower                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.38 sec: 1.02x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 975 us: 1.02x slower                                                        |
| dulwich_log              | 38.0 ms                                                         | 38.9 ms: 1.02x slower                                                       |
| deepcopy_memo            | 22.1 us                                                         | 22.6 us: 1.02x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 765 us: 1.02x slower                                                        |
| pickle                   | 7.11 us                                                         | 7.27 us: 1.02x slower                                                       |
| float                    | 49.7 ms                                                         | 50.9 ms: 1.02x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 71.6 ms: 1.02x slower                                                       |
| scimark_fft              | 171 ms                                                          | 175 ms: 1.03x slower                                                        |
| nbody                    | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 2.05 us: 1.03x slower                                                       |
| generators               | 19.6 ms                                                         | 20.1 ms: 1.03x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 913 us: 1.03x slower                                                        |
| genshi_text              | 14.4 ms                                                         | 14.8 ms: 1.03x slower                                                       |
| typing_runtime_protocols | 101 us                                                          | 104 us: 1.03x slower                                                        |
| pickle_list              | 2.90 us                                                         | 3.02 us: 1.04x slower                                                       |
| coroutines               | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                                       |
| unpickle                 | 8.40 us                                                         | 8.79 us: 1.05x slower                                                       |
| pickle_dict              | 18.1 us                                                         | 19.2 us: 1.06x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.39 sec: 1.06x slower                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.6 ms: 1.06x slower                                                       |
| coverage                 | 42.1 ms                                                         | 45.4 ms: 1.08x slower                                                       |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (31): pycparser, json, async_tree_cpu_io_mixed, async_tree_io, bench_thread_pool, python_startup, python_startup_no_site, bench_mp_pool, async_tree_none, logging_format, async_tree_memoization, richards, async_tree_cpu_io_mixed_tg, richards_super, async_generators, pylint, gc_traversal, flaskblogging, logging_simple, logging_silent, docutils, 2to3, scimark_sor, tornado_http, xml_etree_parse, mako, asyncio_tcp, async_tree_memoization_tg, async_tree_none_tg, regex_v8, asyncio_tcp_ssl

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown