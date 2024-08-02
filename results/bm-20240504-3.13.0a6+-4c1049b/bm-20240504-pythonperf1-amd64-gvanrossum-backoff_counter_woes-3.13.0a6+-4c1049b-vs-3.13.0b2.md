# Results vs. 3.13.0b2

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: windows-amd64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 98.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chameleon      | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                           |
| docutils       | 1.63 sec                                                        | 1.63 sec: 1.01x slower                                                          |
| html5lib       | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                           |
| tornado_http   | 81.8 ms                                                         | 79.8 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg | 202 ms                                                          | 211 ms: 1.05x slower                                                            |
| Geometric mean     | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 48.7 ms: 1.02x faster                                                           |
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                                            |
| nbody          | 67.6 ms                                                         | 67.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 88.2 ms: 1.03x faster                                                           |
| unpickle             | 8.40 us                                                         | 8.17 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.8 ms: 1.03x faster                                                           |
| pickle_pure_python   | 175 us                                                          | 174 us: 1.01x faster                                                            |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                           |
| json_dumps           | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                           |
| xml_etree_process    | 36.4 ms                                                         | 36.2 ms: 1.01x faster                                                           |
| xml_etree_generate   | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                           |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                          |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.02x slower                                                            |
| pickle_dict          | 18.1 us                                                         | 18.9 us: 1.04x slower                                                           |
| unpickle_list        | 2.62 us                                                         | 2.74 us: 1.05x slower                                                           |
| pickle               | 7.11 us                                                         | 7.47 us: 1.05x slower                                                           |
| pickle_list          | 2.90 us                                                         | 3.28 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 20.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 6.36 ms                                                         | 6.48 ms: 1.02x slower                                                           |
| genshi_text    | 14.4 ms                                                         | 15.0 ms: 1.05x slower                                                           |
| genshi_xml     | 31.6 ms                                                         | 34.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm            | 63.7 ms                                                         | 59.3 ms: 1.07x faster                                                           |
| logging_silent           | 52.9 ns                                                         | 50.7 ns: 1.04x faster                                                           |
| raytrace                 | 162 ms                                                          | 156 ms: 1.04x faster                                                            |
| scimark_lu               | 56.6 ms                                                         | 54.4 ms: 1.04x faster                                                           |
| generators               | 19.6 ms                                                         | 19.0 ms: 1.03x faster                                                           |
| xml_etree_parse          | 90.9 ms                                                         | 88.2 ms: 1.03x faster                                                           |
| unpickle                 | 8.40 us                                                         | 8.17 us: 1.03x faster                                                           |
| xml_etree_iterparse      | 62.3 ms                                                         | 60.8 ms: 1.03x faster                                                           |
| tornado_http             | 81.8 ms                                                         | 79.8 ms: 1.03x faster                                                           |
| float                    | 49.7 ms                                                         | 48.7 ms: 1.02x faster                                                           |
| comprehensions           | 10.4 us                                                         | 10.2 us: 1.02x faster                                                           |
| pidigits                 | 150 ms                                                          | 147 ms: 1.02x faster                                                            |
| richards_super           | 30.2 ms                                                         | 29.7 ms: 1.01x faster                                                           |
| deepcopy                 | 220 us                                                          | 217 us: 1.01x faster                                                            |
| typing_runtime_protocols | 101 us                                                          | 99.5 us: 1.01x faster                                                           |
| python_startup           | 20.3 ms                                                         | 20.0 ms: 1.01x faster                                                           |
| chameleon                | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                           |
| richards                 | 26.7 ms                                                         | 26.4 ms: 1.01x faster                                                           |
| coroutines               | 12.8 ms                                                         | 12.6 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 1.99 us                                                         | 1.97 us: 1.01x faster                                                           |
| chaos                    | 38.4 ms                                                         | 37.9 ms: 1.01x faster                                                           |
| pickle_pure_python       | 175 us                                                          | 174 us: 1.01x faster                                                            |
| json_loads               | 14.2 us                                                         | 14.0 us: 1.01x faster                                                           |
| logging_format           | 6.22 us                                                         | 6.17 us: 1.01x faster                                                           |
| nbody                    | 67.6 ms                                                         | 67.0 ms: 1.01x faster                                                           |
| json_dumps               | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                           |
| deepcopy_memo            | 22.1 us                                                         | 21.9 us: 1.01x faster                                                           |
| sqlglot_normalize        | 173 ms                                                          | 172 ms: 1.01x faster                                                            |
| xml_etree_process        | 36.4 ms                                                         | 36.2 ms: 1.01x faster                                                           |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                            |
| xml_etree_generate       | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                           |
| logging_simple           | 5.78 us                                                         | 5.76 us: 1.00x faster                                                           |
| sqlglot_optimize         | 32.7 ms                                                         | 32.6 ms: 1.00x faster                                                           |
| deltablue                | 1.88 ms                                                         | 1.89 ms: 1.00x slower                                                           |
| mypy2                    | 418 ms                                                          | 420 ms: 1.01x slower                                                            |
| docutils                 | 1.63 sec                                                        | 1.63 sec: 1.01x slower                                                          |
| sympy_sum                | 84.4 ms                                                         | 84.9 ms: 1.01x slower                                                           |
| fannkuch                 | 243 ms                                                          | 245 ms: 1.01x slower                                                            |
| sympy_integrate          | 12.2 ms                                                         | 12.3 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 955 us                                                          | 963 us: 1.01x slower                                                            |
| sympy_expand             | 271 ms                                                          | 273 ms: 1.01x slower                                                            |
| aiohttp                  | 889 us                                                          | 896 us: 1.01x slower                                                            |
| pprint_safe_repr         | 474 ms                                                          | 478 ms: 1.01x slower                                                            |
| scimark_sor              | 75.3 ms                                                         | 76.0 ms: 1.01x slower                                                           |
| sympy_str                | 159 ms                                                          | 161 ms: 1.01x slower                                                            |
| pprint_pformat           | 966 ms                                                          | 975 ms: 1.01x slower                                                            |
| pyflate                  | 279 ms                                                          | 281 ms: 1.01x slower                                                            |
| create_gc_cycles         | 888 us                                                          | 898 us: 1.01x slower                                                            |
| sqlglot_parse            | 748 us                                                          | 757 us: 1.01x slower                                                            |
| tomli_loads              | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                          |
| scimark_monte_carlo      | 39.1 ms                                                         | 39.7 ms: 1.01x slower                                                           |
| meteor_contest           | 69.9 ms                                                         | 70.9 ms: 1.01x slower                                                           |
| sqlite_synth             | 1.60 us                                                         | 1.63 us: 1.02x slower                                                           |
| mako                     | 6.36 ms                                                         | 6.48 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 122 us                                                          | 124 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.55 ms: 1.02x slower                                                           |
| async_generators         | 223 ms                                                          | 228 ms: 1.02x slower                                                            |
| hexiom                   | 3.72 ms                                                         | 3.81 ms: 1.02x slower                                                           |
| scimark_fft              | 171 ms                                                          | 175 ms: 1.02x slower                                                            |
| go                       | 82.1 ms                                                         | 84.5 ms: 1.03x slower                                                           |
| crypto_pyaes             | 45.5 ms                                                         | 46.9 ms: 1.03x slower                                                           |
| telco                    | 4.67 ms                                                         | 4.82 ms: 1.03x slower                                                           |
| pathlib                  | 75.9 ms                                                         | 78.7 ms: 1.04x slower                                                           |
| html5lib                 | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                           |
| pickle_dict              | 18.1 us                                                         | 18.9 us: 1.04x slower                                                           |
| bench_thread_pool        | 768 us                                                          | 801 us: 1.04x slower                                                            |
| unpickle_list            | 2.62 us                                                         | 2.74 us: 1.05x slower                                                           |
| genshi_text              | 14.4 ms                                                         | 15.0 ms: 1.05x slower                                                           |
| async_tree_none_tg       | 202 ms                                                          | 211 ms: 1.05x slower                                                            |
| pickle                   | 7.11 us                                                         | 7.47 us: 1.05x slower                                                           |
| dulwich_log              | 38.0 ms                                                         | 40.2 ms: 1.06x slower                                                           |
| coverage                 | 42.1 ms                                                         | 44.6 ms: 1.06x slower                                                           |
| genshi_xml               | 31.6 ms                                                         | 34.0 ms: 1.08x slower                                                           |
| pickle_list              | 2.90 us                                                         | 3.28 us: 1.13x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (24): regex_v8, json, async_tree_cpu_io_mixed, pycparser, bench_mp_pool, gc_traversal, flaskblogging, mdp, asyncio_tcp, thrift, async_tree_none, django_template, async_tree_io, async_tree_cpu_io_mixed_tg, regex_compile, regex_effbot, 2to3, nqueens, async_tree_memoization_tg, pylint, async_tree_io_tg, python_startup_no_site, async_tree_memoization, asyncio_tcp_ssl
Ignored benchmarks (1) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: dask

# HPT report

- Reliability score: 98.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown