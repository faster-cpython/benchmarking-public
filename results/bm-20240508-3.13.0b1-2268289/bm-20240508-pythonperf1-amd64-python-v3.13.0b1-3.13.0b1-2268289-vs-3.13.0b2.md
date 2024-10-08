# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b1
- machine: windows-amd64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.00x slower
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 212 ms: 1.03x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.75 ms: 1.01x faster                                           |
| docutils       | 1.63 sec                                                        | 1.64 sec: 1.01x slower                                          |
| tornado_http   | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none_tg | 202 ms                                                          | 213 ms: 1.05x slower                                            |
| Geometric mean     | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 48.5 ms: 1.03x faster                                           |
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| nbody          | 67.6 ms                                                         | 67.1 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                           |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| regex_effbot   | 1.58 ms                                                         | 1.58 ms: 1.01x faster                                           |
| regex_compile  | 78.0 ms                                                         | 78.5 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.7 us: 1.03x faster                                           |
| xml_etree_parse      | 90.9 ms                                                         | 90.0 ms: 1.01x faster                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.9 ms: 1.01x faster                                           |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                           |
| pickle_pure_python   | 175 us                                                          | 177 us: 1.01x slower                                            |
| xml_etree_generate   | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                           |
| xml_etree_process    | 36.4 ms                                                         | 36.8 ms: 1.01x slower                                           |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.02x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.02x slower                                          |
| unpickle_pure_python | 122 us                                                          | 127 us: 1.04x slower                                            |
| pickle_list          | 2.90 us                                                         | 3.02 us: 1.04x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.28 ms: 1.01x faster                                           |
| django_template | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                           |
| genshi_xml      | 31.6 ms                                                         | 32.2 ms: 1.02x slower                                           |
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pycparser                | 754 ms                                                          | 669 ms: 1.13x faster                                            |
| regex_v8                 | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                           |
| json                     | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                           |
| raytrace                 | 162 ms                                                          | 154 ms: 1.06x faster                                            |
| generators               | 19.6 ms                                                         | 18.6 ms: 1.05x faster                                           |
| json_loads               | 14.2 us                                                         | 13.7 us: 1.03x faster                                           |
| spectral_norm            | 63.7 ms                                                         | 61.9 ms: 1.03x faster                                           |
| float                    | 49.7 ms                                                         | 48.5 ms: 1.03x faster                                           |
| logging_silent           | 52.9 ns                                                         | 51.7 ns: 1.02x faster                                           |
| pidigits                 | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| comprehensions           | 10.4 us                                                         | 10.2 us: 1.01x faster                                           |
| mako                     | 6.36 ms                                                         | 6.28 ms: 1.01x faster                                           |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| chameleon                | 4.80 ms                                                         | 4.75 ms: 1.01x faster                                           |
| xml_etree_parse          | 90.9 ms                                                         | 90.0 ms: 1.01x faster                                           |
| django_template          | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                           |
| coroutines               | 12.8 ms                                                         | 12.6 ms: 1.01x faster                                           |
| nqueens                  | 56.7 ms                                                         | 56.2 ms: 1.01x faster                                           |
| nbody                    | 67.6 ms                                                         | 67.1 ms: 1.01x faster                                           |
| richards_super           | 30.2 ms                                                         | 29.9 ms: 1.01x faster                                           |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.9 ms: 1.01x faster                                           |
| deepcopy_reduce          | 1.99 us                                                         | 1.98 us: 1.01x faster                                           |
| richards                 | 26.7 ms                                                         | 26.6 ms: 1.01x faster                                           |
| sqlglot_normalize        | 173 ms                                                          | 172 ms: 1.01x faster                                            |
| regex_effbot             | 1.58 ms                                                         | 1.58 ms: 1.01x faster                                           |
| sqlglot_optimize         | 32.7 ms                                                         | 32.9 ms: 1.01x slower                                           |
| async_generators         | 223 ms                                                          | 225 ms: 1.01x slower                                            |
| pyflate                  | 279 ms                                                          | 280 ms: 1.01x slower                                            |
| regex_compile            | 78.0 ms                                                         | 78.5 ms: 1.01x slower                                           |
| docutils                 | 1.63 sec                                                        | 1.64 sec: 1.01x slower                                          |
| scimark_sor              | 75.3 ms                                                         | 75.9 ms: 1.01x slower                                           |
| sqlglot_transpile        | 955 us                                                          | 962 us: 1.01x slower                                            |
| sqlglot_parse            | 748 us                                                          | 754 us: 1.01x slower                                            |
| tornado_http             | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                           |
| bench_mp_pool            | 64.8 ms                                                         | 65.3 ms: 1.01x slower                                           |
| pickle                   | 7.11 us                                                         | 7.17 us: 1.01x slower                                           |
| pickle_pure_python       | 175 us                                                          | 177 us: 1.01x slower                                            |
| hexiom                   | 3.72 ms                                                         | 3.76 ms: 1.01x slower                                           |
| xml_etree_generate       | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                           |
| deltablue                | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.53 ms: 1.01x slower                                           |
| xml_etree_process        | 36.4 ms                                                         | 36.8 ms: 1.01x slower                                           |
| sympy_sum                | 84.4 ms                                                         | 85.2 ms: 1.01x slower                                           |
| telco                    | 4.67 ms                                                         | 4.72 ms: 1.01x slower                                           |
| pprint_safe_repr         | 474 ms                                                          | 481 ms: 1.01x slower                                            |
| thrift                   | 8.11 ms                                                         | 8.23 ms: 1.01x slower                                           |
| pickle_dict              | 18.1 us                                                         | 18.4 us: 1.02x slower                                           |
| deepcopy                 | 220 us                                                          | 223 us: 1.02x slower                                            |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.02x slower                                           |
| sympy_expand             | 271 ms                                                          | 275 ms: 1.02x slower                                            |
| pprint_pformat           | 966 ms                                                          | 982 ms: 1.02x slower                                            |
| python_startup_no_site   | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                           |
| tomli_loads              | 1.35 sec                                                        | 1.37 sec: 1.02x slower                                          |
| sympy_integrate          | 12.2 ms                                                         | 12.5 ms: 1.02x slower                                           |
| sympy_str                | 159 ms                                                          | 162 ms: 1.02x slower                                            |
| meteor_contest           | 69.9 ms                                                         | 71.3 ms: 1.02x slower                                           |
| genshi_xml               | 31.6 ms                                                         | 32.2 ms: 1.02x slower                                           |
| mypy2                    | 418 ms                                                          | 427 ms: 1.02x slower                                            |
| scimark_fft              | 171 ms                                                          | 175 ms: 1.02x slower                                            |
| typing_runtime_protocols | 101 us                                                          | 103 us: 1.02x slower                                            |
| aiohttp                  | 889 us                                                          | 908 us: 1.02x slower                                            |
| asyncio_tcp              | 471 ms                                                          | 482 ms: 1.02x slower                                            |
| genshi_text              | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                           |
| 2to3                     | 207 ms                                                          | 212 ms: 1.03x slower                                            |
| go                       | 82.1 ms                                                         | 84.3 ms: 1.03x slower                                           |
| crypto_pyaes             | 45.5 ms                                                         | 46.9 ms: 1.03x slower                                           |
| bench_thread_pool        | 768 us                                                          | 793 us: 1.03x slower                                            |
| scimark_monte_carlo      | 39.1 ms                                                         | 40.5 ms: 1.04x slower                                           |
| unpickle_pure_python     | 122 us                                                          | 127 us: 1.04x slower                                            |
| pickle_list              | 2.90 us                                                         | 3.02 us: 1.04x slower                                           |
| dulwich_log              | 38.0 ms                                                         | 39.6 ms: 1.04x slower                                           |
| deepcopy_memo            | 22.1 us                                                         | 23.1 us: 1.05x slower                                           |
| async_tree_none_tg       | 202 ms                                                          | 213 ms: 1.05x slower                                            |
| pathlib                  | 75.9 ms                                                         | 80.1 ms: 1.06x slower                                           |
| unpickle_list            | 2.62 us                                                         | 2.77 us: 1.06x slower                                           |
| coverage                 | 42.1 ms                                                         | 45.3 ms: 1.08x slower                                           |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                    |

Benchmark hidden because not significant (22): async_tree_cpu_io_mixed, async_tree_io, json_dumps, async_tree_io_tg, chaos, gc_traversal, flaskblogging, html5lib, logging_format, mdp, fannkuch, logging_simple, async_tree_cpu_io_mixed_tg, scimark_lu, python_startup, unpickle, create_gc_cycles, async_tree_none, async_tree_memoization, asyncio_tcp_ssl, pylint, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: dask

# HPT report

- Reliability score: 99.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown