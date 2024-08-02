# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_pragma_313
- machine: windows-amd64
- commit hash: 3fbe4c2
- commit date: 2024-07-02
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 213 ms: 1.03x slower                                                     |
| chameleon      | 4.80 ms                                                         | 4.68 ms: 1.03x faster                                                    |
| docutils       | 1.63 sec                                                        | 1.64 sec: 1.01x slower                                                   |
| html5lib       | 35.0 ms                                                         | 38.2 ms: 1.09x slower                                                    |
| tornado_http   | 81.8 ms                                                         | 82.4 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                           | 1.02x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                     |
| float          | 49.7 ms                                                         | 50.0 ms: 1.01x slower                                                    |
| nbody          | 67.6 ms                                                         | 69.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                           | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                     |
| regex_compile  | 78.0 ms                                                         | 81.4 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                           | 1.02x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                    |
| json_dumps           | 5.61 ms                                                         | 5.67 ms: 1.01x slower                                                    |
| tomli_loads          | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                   |
| xml_etree_generate   | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                    |
| xml_etree_parse      | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                    |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                    |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.02x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 181 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                    |
| python_startup_no_site | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                    |
| genshi_xml      | 31.6 ms                                                         | 32.3 ms: 1.02x slower                                                    |
| genshi_text     | 14.4 ms                                                         | 14.9 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pycparser                | 754 ms                                                          | 665 ms: 1.13x faster                                                     |
| json                     | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                                    |
| comprehensions           | 10.4 us                                                         | 9.95 us: 1.04x faster                                                    |
| raytrace                 | 162 ms                                                          | 158 ms: 1.03x faster                                                     |
| scimark_lu               | 56.6 ms                                                         | 55.1 ms: 1.03x faster                                                    |
| chameleon                | 4.80 ms                                                         | 4.68 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.45 ms: 1.02x faster                                                    |
| logging_simple           | 5.78 us                                                         | 5.68 us: 1.02x faster                                                    |
| logging_format           | 6.22 us                                                         | 6.12 us: 1.02x faster                                                    |
| logging_silent           | 52.9 ns                                                         | 52.2 ns: 1.01x faster                                                    |
| spectral_norm            | 63.7 ms                                                         | 63.0 ms: 1.01x faster                                                    |
| chaos                    | 38.4 ms                                                         | 37.9 ms: 1.01x faster                                                    |
| hexiom                   | 3.72 ms                                                         | 3.68 ms: 1.01x faster                                                    |
| crypto_pyaes             | 45.5 ms                                                         | 45.1 ms: 1.01x faster                                                    |
| deepcopy_reduce          | 1.99 us                                                         | 1.98 us: 1.01x faster                                                    |
| nqueens                  | 56.7 ms                                                         | 56.5 ms: 1.00x faster                                                    |
| sqlglot_normalize        | 173 ms                                                          | 172 ms: 1.00x faster                                                     |
| pyflate                  | 279 ms                                                          | 280 ms: 1.00x slower                                                     |
| pidigits                 | 150 ms                                                          | 151 ms: 1.00x slower                                                     |
| richards                 | 26.7 ms                                                         | 26.8 ms: 1.00x slower                                                    |
| float                    | 49.7 ms                                                         | 50.0 ms: 1.01x slower                                                    |
| regex_dna                | 119 ms                                                          | 120 ms: 1.01x slower                                                     |
| xml_etree_process        | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                                    |
| tornado_http             | 81.8 ms                                                         | 82.4 ms: 1.01x slower                                                    |
| xml_etree_iterparse      | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                    |
| sympy_integrate          | 12.2 ms                                                         | 12.4 ms: 1.01x slower                                                    |
| json_dumps               | 5.61 ms                                                         | 5.67 ms: 1.01x slower                                                    |
| pathlib                  | 75.9 ms                                                         | 76.7 ms: 1.01x slower                                                    |
| tomli_loads              | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                   |
| docutils                 | 1.63 sec                                                        | 1.64 sec: 1.01x slower                                                   |
| django_template          | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                    |
| xml_etree_generate       | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                    |
| create_gc_cycles         | 888 us                                                          | 901 us: 1.02x slower                                                     |
| xml_etree_parse          | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                    |
| bench_mp_pool            | 64.8 ms                                                         | 65.7 ms: 1.02x slower                                                    |
| scimark_fft              | 171 ms                                                          | 174 ms: 1.02x slower                                                     |
| typing_runtime_protocols | 101 us                                                          | 103 us: 1.02x slower                                                     |
| json_loads               | 14.2 us                                                         | 14.4 us: 1.02x slower                                                    |
| generators               | 19.6 ms                                                         | 19.9 ms: 1.02x slower                                                    |
| unpickle_pure_python     | 122 us                                                          | 124 us: 1.02x slower                                                     |
| sympy_sum                | 84.4 ms                                                         | 86.0 ms: 1.02x slower                                                    |
| pprint_safe_repr         | 474 ms                                                          | 483 ms: 1.02x slower                                                     |
| fannkuch                 | 243 ms                                                          | 248 ms: 1.02x slower                                                     |
| nbody                    | 67.6 ms                                                         | 69.0 ms: 1.02x slower                                                    |
| coroutines               | 12.8 ms                                                         | 13.0 ms: 1.02x slower                                                    |
| pprint_pformat           | 966 ms                                                          | 987 ms: 1.02x slower                                                     |
| python_startup           | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                    |
| genshi_xml               | 31.6 ms                                                         | 32.3 ms: 1.02x slower                                                    |
| deltablue                | 1.88 ms                                                         | 1.93 ms: 1.03x slower                                                    |
| mypy2                    | 418 ms                                                          | 429 ms: 1.03x slower                                                     |
| async_generators         | 223 ms                                                          | 229 ms: 1.03x slower                                                     |
| sqlglot_transpile        | 955 us                                                          | 982 us: 1.03x slower                                                     |
| 2to3                     | 207 ms                                                          | 213 ms: 1.03x slower                                                     |
| scimark_monte_carlo      | 39.1 ms                                                         | 40.3 ms: 1.03x slower                                                    |
| pickle_pure_python       | 175 us                                                          | 181 us: 1.03x slower                                                     |
| meteor_contest           | 69.9 ms                                                         | 72.0 ms: 1.03x slower                                                    |
| go                       | 82.1 ms                                                         | 84.8 ms: 1.03x slower                                                    |
| genshi_text              | 14.4 ms                                                         | 14.9 ms: 1.03x slower                                                    |
| thrift                   | 8.11 ms                                                         | 8.44 ms: 1.04x slower                                                    |
| sqlglot_parse            | 748 us                                                          | 780 us: 1.04x slower                                                     |
| regex_compile            | 78.0 ms                                                         | 81.4 ms: 1.04x slower                                                    |
| mdp                      | 1.31 sec                                                        | 1.37 sec: 1.04x slower                                                   |
| sqlglot_optimize         | 32.7 ms                                                         | 34.2 ms: 1.05x slower                                                    |
| sympy_str                | 159 ms                                                          | 167 ms: 1.05x slower                                                     |
| python_startup_no_site   | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                    |
| sympy_expand             | 271 ms                                                          | 286 ms: 1.06x slower                                                     |
| dulwich_log              | 38.0 ms                                                         | 40.5 ms: 1.07x slower                                                    |
| coverage                 | 42.1 ms                                                         | 45.7 ms: 1.09x slower                                                    |
| html5lib                 | 35.0 ms                                                         | 38.2 ms: 1.09x slower                                                    |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                             |

Benchmark hidden because not significant (21): async_tree_cpu_io_mixed, bench_thread_pool, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, deepcopy, gc_traversal, scimark_sor, deepcopy_memo, richards_super, pylint, async_tree_io_tg, mako, telco, regex_effbot, asyncio_tcp, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, regex_v8, asyncio_tcp_ssl
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown