# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.01x faster
- HPT reliability: 94.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 207 ms: 1.05x faster                                            |
| chameleon      | 4.72 ms                                                     | 4.80 ms: 1.02x slower                                           |
| docutils       | 1.57 sec                                                    | 1.63 sec: 1.03x slower                                          |
| html5lib       | 38.6 ms                                                     | 35.0 ms: 1.10x faster                                           |
| tornado_http   | 92.8 ms                                                     | 81.8 ms: 1.13x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 471 ms: 1.39x faster                                            |
| async_tree_memoization_tg | 288 ms                                                      | 258 ms: 1.12x faster                                            |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.48 sec: 1.11x faster                                          |
| async_tree_none           | 223 ms                                                      | 218 ms: 1.02x faster                                            |
| coroutines                | 12.5 ms                                                     | 12.8 ms: 1.02x slower                                           |
| async_tree_io             | 521 ms                                                      | 588 ms: 1.13x slower                                            |
| async_tree_io_tg          | 512 ms                                                      | 605 ms: 1.18x slower                                            |
| Geometric mean            | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_none_tg, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| float          | 48.1 ms                                                     | 49.7 ms: 1.03x slower                                           |
| nbody          | 64.5 ms                                                     | 67.6 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 78.0 ms: 1.03x faster                                           |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                            |
| regex_v8       | 14.7 ms                                                     | 15.8 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 183 us                                                      | 175 us: 1.04x faster                                            |
| unpickle_list        | 2.72 us                                                     | 2.62 us: 1.04x faster                                           |
| unpickle_pure_python | 127 us                                                      | 122 us: 1.04x faster                                            |
| pickle               | 7.34 us                                                     | 7.11 us: 1.03x faster                                           |
| unpickle             | 8.63 us                                                     | 8.40 us: 1.03x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.61 ms: 1.03x faster                                           |
| xml_etree_parse      | 93.2 ms                                                     | 90.9 ms: 1.03x faster                                           |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                           |
| tomli_loads          | 1.36 sec                                                    | 1.35 sec: 1.01x faster                                          |
| pickle_dict          | 18.0 us                                                     | 18.1 us: 1.01x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 16.2 ms: 1.10x faster                                           |
| python_startup         | 22.2 ms                                                     | 20.3 ms: 1.09x faster                                           |
| Geometric mean         | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml     | 32.8 ms                                                     | 31.6 ms: 1.04x faster                                           |
| genshi_text    | 14.9 ms                                                     | 14.4 ms: 1.03x faster                                           |
| mako           | 6.24 ms                                                     | 6.36 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 471 ms: 1.39x faster                                            |
| tornado_http              | 92.8 ms                                                     | 81.8 ms: 1.13x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 258 ms: 1.12x faster                                            |
| coverage                  | 46.7 ms                                                     | 42.1 ms: 1.11x faster                                           |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.48 sec: 1.11x faster                                          |
| html5lib                  | 38.6 ms                                                     | 35.0 ms: 1.10x faster                                           |
| python_startup_no_site    | 17.8 ms                                                     | 16.2 ms: 1.10x faster                                           |
| python_startup            | 22.2 ms                                                     | 20.3 ms: 1.09x faster                                           |
| bench_thread_pool         | 828 us                                                      | 768 us: 1.08x faster                                            |
| bench_mp_pool             | 69.6 ms                                                     | 64.8 ms: 1.07x faster                                           |
| thrift                    | 8.68 ms                                                     | 8.11 ms: 1.07x faster                                           |
| pathlib                   | 81.2 ms                                                     | 75.9 ms: 1.07x faster                                           |
| dulwich_log               | 40.4 ms                                                     | 38.0 ms: 1.06x faster                                           |
| mdp                       | 1.38 sec                                                    | 1.31 sec: 1.06x faster                                          |
| sympy_expand              | 285 ms                                                      | 271 ms: 1.05x faster                                            |
| 2to3                      | 217 ms                                                      | 207 ms: 1.05x faster                                            |
| aiohttp                   | 932 us                                                      | 889 us: 1.05x faster                                            |
| pickle_pure_python        | 183 us                                                      | 175 us: 1.04x faster                                            |
| sympy_str                 | 166 ms                                                      | 159 ms: 1.04x faster                                            |
| unpickle_list             | 2.72 us                                                     | 2.62 us: 1.04x faster                                           |
| unpickle_pure_python      | 127 us                                                      | 122 us: 1.04x faster                                            |
| pprint_safe_repr          | 493 ms                                                      | 474 ms: 1.04x faster                                            |
| telco                     | 4.85 ms                                                     | 4.67 ms: 1.04x faster                                           |
| genshi_xml                | 32.8 ms                                                     | 31.6 ms: 1.04x faster                                           |
| meteor_contest            | 72.3 ms                                                     | 69.9 ms: 1.03x faster                                           |
| genshi_text               | 14.9 ms                                                     | 14.4 ms: 1.03x faster                                           |
| pickle                    | 7.34 us                                                     | 7.11 us: 1.03x faster                                           |
| go                        | 84.6 ms                                                     | 82.1 ms: 1.03x faster                                           |
| scimark_monte_carlo       | 40.3 ms                                                     | 39.1 ms: 1.03x faster                                           |
| unpickle                  | 8.63 us                                                     | 8.40 us: 1.03x faster                                           |
| regex_compile             | 80.1 ms                                                     | 78.0 ms: 1.03x faster                                           |
| mypy2                     | 429 ms                                                      | 418 ms: 1.03x faster                                            |
| pprint_pformat            | 991 ms                                                      | 966 ms: 1.03x faster                                            |
| json_dumps                | 5.76 ms                                                     | 5.61 ms: 1.03x faster                                           |
| xml_etree_parse           | 93.2 ms                                                     | 90.9 ms: 1.03x faster                                           |
| sympy_sum                 | 86.4 ms                                                     | 84.4 ms: 1.02x faster                                           |
| async_tree_none           | 223 ms                                                      | 218 ms: 1.02x faster                                            |
| regex_effbot              | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| scimark_fft               | 174 ms                                                      | 171 ms: 1.02x faster                                            |
| sqlglot_parse             | 761 us                                                      | 748 us: 1.02x faster                                            |
| deepcopy                  | 223 us                                                      | 220 us: 1.02x faster                                            |
| deepcopy_reduce           | 2.02 us                                                     | 1.99 us: 1.01x faster                                           |
| sqlglot_optimize          | 33.1 ms                                                     | 32.7 ms: 1.01x faster                                           |
| json_loads                | 14.3 us                                                     | 14.2 us: 1.01x faster                                           |
| tomli_loads               | 1.36 sec                                                    | 1.35 sec: 1.01x faster                                          |
| fannkuch                  | 245 ms                                                      | 243 ms: 1.01x faster                                            |
| flaskblogging             | 2.04 sec                                                    | 2.03 sec: 1.00x faster                                          |
| sympy_integrate           | 12.3 ms                                                     | 12.2 ms: 1.00x faster                                           |
| generators                | 19.5 ms                                                     | 19.6 ms: 1.00x slower                                           |
| pickle_dict               | 18.0 us                                                     | 18.1 us: 1.01x slower                                           |
| hexiom                    | 3.69 ms                                                     | 3.72 ms: 1.01x slower                                           |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| deltablue                 | 1.86 ms                                                     | 1.88 ms: 1.01x slower                                           |
| logging_simple            | 5.72 us                                                     | 5.78 us: 1.01x slower                                           |
| sqlglot_normalize         | 171 ms                                                      | 173 ms: 1.01x slower                                            |
| logging_format            | 6.15 us                                                     | 6.22 us: 1.01x slower                                           |
| deepcopy_memo             | 21.8 us                                                     | 22.1 us: 1.01x slower                                           |
| pyflate                   | 275 ms                                                      | 279 ms: 1.01x slower                                            |
| chaos                     | 37.9 ms                                                     | 38.4 ms: 1.01x slower                                           |
| comprehensions            | 10.2 us                                                     | 10.4 us: 1.01x slower                                           |
| coroutines                | 12.5 ms                                                     | 12.8 ms: 1.02x slower                                           |
| chameleon                 | 4.72 ms                                                     | 4.80 ms: 1.02x slower                                           |
| mako                      | 6.24 ms                                                     | 6.36 ms: 1.02x slower                                           |
| nqueens                   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                           |
| richards                  | 26.0 ms                                                     | 26.7 ms: 1.03x slower                                           |
| richards_super            | 29.3 ms                                                     | 30.2 ms: 1.03x slower                                           |
| docutils                  | 1.57 sec                                                    | 1.63 sec: 1.03x slower                                          |
| float                     | 48.1 ms                                                     | 49.7 ms: 1.03x slower                                           |
| logging_silent            | 51.0 ns                                                     | 52.9 ns: 1.04x slower                                           |
| raytrace                  | 156 ms                                                      | 162 ms: 1.04x slower                                            |
| regex_dna                 | 114 ms                                                      | 119 ms: 1.04x slower                                            |
| scimark_sor               | 72.0 ms                                                     | 75.3 ms: 1.05x slower                                           |
| scimark_lu                | 54.0 ms                                                     | 56.6 ms: 1.05x slower                                           |
| nbody                     | 64.5 ms                                                     | 67.6 ms: 1.05x slower                                           |
| crypto_pyaes              | 42.8 ms                                                     | 45.5 ms: 1.06x slower                                           |
| json                      | 2.98 ms                                                     | 3.19 ms: 1.07x slower                                           |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.50 ms: 1.07x slower                                           |
| create_gc_cycles          | 829 us                                                      | 888 us: 1.07x slower                                            |
| regex_v8                  | 14.7 ms                                                     | 15.8 ms: 1.08x slower                                           |
| spectral_norm             | 59.2 ms                                                     | 63.7 ms: 1.08x slower                                           |
| async_tree_io             | 521 ms                                                      | 588 ms: 1.13x slower                                            |
| async_tree_io_tg          | 512 ms                                                      | 605 ms: 1.18x slower                                            |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (16): pylint, async_tree_memoization, async_tree_none_tg, pycparser, django_template, xml_etree_generate, xml_etree_process, gc_traversal, xml_etree_iterparse, sqlite_synth, async_generators, sqlglot_transpile, pickle_list, typing_runtime_protocols, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 94.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown