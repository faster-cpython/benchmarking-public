# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 217 ms: 1.05x slower                                        |
| chameleon      | 4.80 ms                                                         | 4.72 ms: 1.02x faster                                       |
| docutils       | 1.63 sec                                                        | 1.57 sec: 1.03x faster                                      |
| html5lib       | 35.0 ms                                                         | 38.6 ms: 1.10x slower                                       |
| tornado_http   | 81.8 ms                                                         | 92.8 ms: 1.13x slower                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 512 ms: 1.18x faster                                        |
| async_tree_io             | 588 ms                                                          | 521 ms: 1.13x faster                                        |
| async_tree_none           | 218 ms                                                          | 223 ms: 1.02x slower                                        |
| async_tree_memoization_tg | 258 ms                                                          | 288 ms: 1.12x slower                                        |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 64.5 ms: 1.05x faster                                       |
| float          | 49.7 ms                                                         | 48.1 ms: 1.03x faster                                       |
| pidigits       | 150 ms                                                          | 148 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                           | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                       |
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                        |
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                       |
| regex_compile  | 78.0 ms                                                         | 80.1 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                           | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                         | 18.0 us: 1.01x faster                                       |
| tomli_loads          | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                       |
| xml_etree_parse      | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                       |
| json_dumps           | 5.61 ms                                                         | 5.76 ms: 1.03x slower                                       |
| unpickle             | 8.40 us                                                         | 8.63 us: 1.03x slower                                       |
| pickle               | 7.11 us                                                         | 7.34 us: 1.03x slower                                       |
| unpickle_pure_python | 122 us                                                          | 127 us: 1.04x slower                                        |
| unpickle_list        | 2.62 us                                                         | 2.72 us: 1.04x slower                                       |
| pickle_pure_python   | 175 us                                                          | 183 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                |

Benchmark hidden because not significant (4): pickle_list, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                       |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 6.36 ms                                                         | 6.24 ms: 1.02x faster                                       |
| genshi_text    | 14.4 ms                                                         | 14.9 ms: 1.03x slower                                       |
| genshi_xml     | 31.6 ms                                                         | 32.8 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 512 ms: 1.18x faster                                        |
| async_tree_io             | 588 ms                                                          | 521 ms: 1.13x faster                                        |
| spectral_norm             | 63.7 ms                                                         | 59.2 ms: 1.08x faster                                       |
| regex_v8                  | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                       |
| create_gc_cycles          | 888 us                                                          | 829 us: 1.07x faster                                        |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.34 ms: 1.07x faster                                       |
| json                      | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                       |
| crypto_pyaes              | 45.5 ms                                                         | 42.8 ms: 1.06x faster                                       |
| nbody                     | 67.6 ms                                                         | 64.5 ms: 1.05x faster                                       |
| scimark_lu                | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                       |
| scimark_sor               | 75.3 ms                                                         | 72.0 ms: 1.05x faster                                       |
| regex_dna                 | 119 ms                                                          | 114 ms: 1.04x faster                                        |
| raytrace                  | 162 ms                                                          | 156 ms: 1.04x faster                                        |
| logging_silent            | 52.9 ns                                                         | 51.0 ns: 1.04x faster                                       |
| float                     | 49.7 ms                                                         | 48.1 ms: 1.03x faster                                       |
| docutils                  | 1.63 sec                                                        | 1.57 sec: 1.03x faster                                      |
| richards_super            | 30.2 ms                                                         | 29.3 ms: 1.03x faster                                       |
| richards                  | 26.7 ms                                                         | 26.0 ms: 1.03x faster                                       |
| nqueens                   | 56.7 ms                                                         | 55.5 ms: 1.02x faster                                       |
| mako                      | 6.36 ms                                                         | 6.24 ms: 1.02x faster                                       |
| chameleon                 | 4.80 ms                                                         | 4.72 ms: 1.02x faster                                       |
| coroutines                | 12.8 ms                                                         | 12.5 ms: 1.02x faster                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                       |
| chaos                     | 38.4 ms                                                         | 37.9 ms: 1.01x faster                                       |
| pyflate                   | 279 ms                                                          | 275 ms: 1.01x faster                                        |
| deepcopy_memo             | 22.1 us                                                         | 21.8 us: 1.01x faster                                       |
| logging_format            | 6.22 us                                                         | 6.15 us: 1.01x faster                                       |
| sqlglot_normalize         | 173 ms                                                          | 171 ms: 1.01x faster                                        |
| logging_simple            | 5.78 us                                                         | 5.72 us: 1.01x faster                                       |
| deltablue                 | 1.88 ms                                                         | 1.86 ms: 1.01x faster                                       |
| pidigits                  | 150 ms                                                          | 148 ms: 1.01x faster                                        |
| hexiom                    | 3.72 ms                                                         | 3.69 ms: 1.01x faster                                       |
| pickle_dict               | 18.1 us                                                         | 18.0 us: 1.01x faster                                       |
| generators                | 19.6 ms                                                         | 19.5 ms: 1.00x faster                                       |
| sympy_integrate           | 12.2 ms                                                         | 12.3 ms: 1.00x slower                                       |
| flaskblogging             | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                      |
| fannkuch                  | 243 ms                                                          | 245 ms: 1.01x slower                                        |
| tomli_loads               | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 33.1 ms: 1.01x slower                                       |
| deepcopy_reduce           | 1.99 us                                                         | 2.02 us: 1.01x slower                                       |
| deepcopy                  | 220 us                                                          | 223 us: 1.02x slower                                        |
| sqlglot_parse             | 748 us                                                          | 761 us: 1.02x slower                                        |
| scimark_fft               | 171 ms                                                          | 174 ms: 1.02x slower                                        |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                       |
| async_tree_none           | 218 ms                                                          | 223 ms: 1.02x slower                                        |
| sympy_sum                 | 84.4 ms                                                         | 86.4 ms: 1.02x slower                                       |
| xml_etree_parse           | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                       |
| json_dumps                | 5.61 ms                                                         | 5.76 ms: 1.03x slower                                       |
| pprint_pformat            | 966 ms                                                          | 991 ms: 1.03x slower                                        |
| mypy2                     | 418 ms                                                          | 429 ms: 1.03x slower                                        |
| regex_compile             | 78.0 ms                                                         | 80.1 ms: 1.03x slower                                       |
| unpickle                  | 8.40 us                                                         | 8.63 us: 1.03x slower                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 40.3 ms: 1.03x slower                                       |
| go                        | 82.1 ms                                                         | 84.6 ms: 1.03x slower                                       |
| pickle                    | 7.11 us                                                         | 7.34 us: 1.03x slower                                       |
| genshi_text               | 14.4 ms                                                         | 14.9 ms: 1.03x slower                                       |
| meteor_contest            | 69.9 ms                                                         | 72.3 ms: 1.03x slower                                       |
| genshi_xml                | 31.6 ms                                                         | 32.8 ms: 1.04x slower                                       |
| telco                     | 4.67 ms                                                         | 4.85 ms: 1.04x slower                                       |
| pprint_safe_repr          | 474 ms                                                          | 493 ms: 1.04x slower                                        |
| unpickle_pure_python      | 122 us                                                          | 127 us: 1.04x slower                                        |
| unpickle_list             | 2.62 us                                                         | 2.72 us: 1.04x slower                                       |
| sympy_str                 | 159 ms                                                          | 166 ms: 1.04x slower                                        |
| pickle_pure_python        | 175 us                                                          | 183 us: 1.04x slower                                        |
| aiohttp                   | 889 us                                                          | 932 us: 1.05x slower                                        |
| 2to3                      | 207 ms                                                          | 217 ms: 1.05x slower                                        |
| sympy_expand              | 271 ms                                                          | 285 ms: 1.05x slower                                        |
| mdp                       | 1.31 sec                                                        | 1.38 sec: 1.06x slower                                      |
| dulwich_log               | 38.0 ms                                                         | 40.4 ms: 1.06x slower                                       |
| pathlib                   | 75.9 ms                                                         | 81.2 ms: 1.07x slower                                       |
| thrift                    | 8.11 ms                                                         | 8.68 ms: 1.07x slower                                       |
| bench_mp_pool             | 64.8 ms                                                         | 69.6 ms: 1.07x slower                                       |
| bench_thread_pool         | 768 us                                                          | 828 us: 1.08x slower                                        |
| python_startup            | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                       |
| html5lib                  | 35.0 ms                                                         | 38.6 ms: 1.10x slower                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.64 sec: 1.11x slower                                      |
| coverage                  | 42.1 ms                                                         | 46.7 ms: 1.11x slower                                       |
| async_tree_memoization_tg | 258 ms                                                          | 288 ms: 1.12x slower                                        |
| tornado_http              | 81.8 ms                                                         | 92.8 ms: 1.13x slower                                       |
| asyncio_tcp               | 471 ms                                                          | 654 ms: 1.39x slower                                        |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, typing_runtime_protocols, pickle_list, sqlglot_transpile, async_generators, sqlite_synth, xml_etree_iterparse, gc_traversal, xml_etree_process, xml_etree_generate, django_template, pycparser, async_tree_none_tg, async_tree_memoization, pylint
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 98.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown