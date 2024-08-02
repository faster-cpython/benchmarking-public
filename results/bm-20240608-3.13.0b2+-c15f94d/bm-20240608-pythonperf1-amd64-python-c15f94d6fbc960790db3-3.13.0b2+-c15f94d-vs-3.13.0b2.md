# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x slower
- HPT reliability: 95.23%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| docutils       | 1.63 sec                                                        | 1.62 sec: 1.00x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 64.9 ms: 1.04x faster                                                       |
| float          | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                        |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.00x faster                                                       |
| pickle               | 7.11 us                                                         | 7.16 us: 1.01x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.45 us: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.01x slower                                                        |
| xml_etree_process    | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.70 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| django_template | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                     | 3.19 ms                                                         | 2.94 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.40 ms: 1.04x faster                                                       |
| nbody                    | 67.6 ms                                                         | 64.9 ms: 1.04x faster                                                       |
| scimark_lu               | 56.6 ms                                                         | 54.7 ms: 1.03x faster                                                       |
| thrift                   | 8.11 ms                                                         | 7.90 ms: 1.03x faster                                                       |
| pickle_pure_python       | 175 us                                                          | 172 us: 1.02x faster                                                        |
| scimark_sor              | 75.3 ms                                                         | 73.9 ms: 1.02x faster                                                       |
| raytrace                 | 162 ms                                                          | 159 ms: 1.02x faster                                                        |
| logging_simple           | 5.78 us                                                         | 5.69 us: 1.02x faster                                                       |
| nqueens                  | 56.7 ms                                                         | 55.9 ms: 1.01x faster                                                       |
| chaos                    | 38.4 ms                                                         | 37.9 ms: 1.01x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 45.0 ms: 1.01x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.98 us: 1.01x faster                                                       |
| logging_format           | 6.22 us                                                         | 6.17 us: 1.01x faster                                                       |
| generators               | 19.6 ms                                                         | 19.4 ms: 1.01x faster                                                       |
| deepcopy                 | 220 us                                                          | 218 us: 1.01x faster                                                        |
| logging_silent           | 52.9 ns                                                         | 52.6 ns: 1.01x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| pathlib                  | 75.9 ms                                                         | 75.4 ms: 1.01x faster                                                       |
| pprint_safe_repr         | 474 ms                                                          | 471 ms: 1.01x faster                                                        |
| spectral_norm            | 63.7 ms                                                         | 63.4 ms: 1.01x faster                                                       |
| scimark_fft              | 171 ms                                                          | 170 ms: 1.01x faster                                                        |
| docutils                 | 1.63 sec                                                        | 1.62 sec: 1.00x faster                                                      |
| json_loads               | 14.2 us                                                         | 14.1 us: 1.00x faster                                                       |
| sqlglot_normalize        | 173 ms                                                          | 172 ms: 1.00x faster                                                        |
| hexiom                   | 3.72 ms                                                         | 3.71 ms: 1.00x faster                                                       |
| pyflate                  | 279 ms                                                          | 278 ms: 1.00x faster                                                        |
| fannkuch                 | 243 ms                                                          | 244 ms: 1.00x slower                                                        |
| dulwich_log              | 38.0 ms                                                         | 38.2 ms: 1.00x slower                                                       |
| sympy_expand             | 271 ms                                                          | 272 ms: 1.01x slower                                                        |
| pickle                   | 7.11 us                                                         | 7.16 us: 1.01x slower                                                       |
| unpickle                 | 8.40 us                                                         | 8.45 us: 1.01x slower                                                       |
| sympy_str                | 159 ms                                                          | 160 ms: 1.01x slower                                                        |
| pickle_dict              | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| async_generators         | 223 ms                                                          | 225 ms: 1.01x slower                                                        |
| float                    | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                                       |
| 2to3                     | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 955 us                                                          | 964 us: 1.01x slower                                                        |
| sqlglot_parse            | 748 us                                                          | 755 us: 1.01x slower                                                        |
| xml_etree_iterparse      | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 85.3 ms: 1.01x slower                                                       |
| aiohttp                  | 889 us                                                          | 898 us: 1.01x slower                                                        |
| tomli_loads              | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                       |
| xml_etree_parse          | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 35.5 ms: 1.01x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 900 us: 1.01x slower                                                        |
| unpickle_pure_python     | 122 us                                                          | 124 us: 1.01x slower                                                        |
| typing_runtime_protocols | 101 us                                                          | 102 us: 1.02x slower                                                        |
| go                       | 82.1 ms                                                         | 83.4 ms: 1.02x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                                       |
| richards_super           | 30.2 ms                                                         | 30.8 ms: 1.02x slower                                                       |
| genshi_text              | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| richards                 | 26.7 ms                                                         | 27.3 ms: 1.02x slower                                                       |
| python_startup_no_site   | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 787 us: 1.03x slower                                                        |
| scimark_monte_carlo      | 39.1 ms                                                         | 40.1 ms: 1.03x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 71.8 ms: 1.03x slower                                                       |
| coverage                 | 42.1 ms                                                         | 43.3 ms: 1.03x slower                                                       |
| coroutines               | 12.8 ms                                                         | 13.1 ms: 1.03x slower                                                       |
| unpickle_list            | 2.62 us                                                         | 2.70 us: 1.03x slower                                                       |
| django_template          | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.37 sec: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (35): asyncio_tcp_ssl, async_tree_io, async_tree_none, pickle_list, json_dumps, deepcopy_memo, python_startup, pprint_pformat, async_tree_io_tg, comprehensions, deltablue, mypy2, gc_traversal, regex_dna, async_tree_cpu_io_mixed, pylint, pidigits, async_tree_memoization_tg, flaskblogging, chameleon, telco, regex_compile, async_tree_memoization, sympy_integrate, sqlglot_optimize, sqlite_synth, tornado_http, bench_mp_pool, async_tree_cpu_io_mixed_tg, genshi_xml, mako, async_tree_none_tg, asyncio_tcp, pycparser, regex_v8

# HPT report

- Reliability score: 95.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown