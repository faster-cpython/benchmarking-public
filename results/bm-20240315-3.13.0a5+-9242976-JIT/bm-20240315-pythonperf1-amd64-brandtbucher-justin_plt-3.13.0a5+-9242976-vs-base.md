# Results vs. base

- fork: brandtbucher
- ref: justin_plt
- machine: windows-amd64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.01x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                      | 220 ms: 1.01x faster                                                    |
| chameleon      | 4.76 ms                                                                     | 4.71 ms: 1.01x faster                                                   |
| docutils       | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                  |
| html5lib       | 37.0 ms                                                                     | 36.0 ms: 1.03x faster                                                   |
| tornado_http   | 85.0 ms                                                                     | 83.9 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 446 ms                                                                      | 451 ms: 1.01x slower                                                    |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 58.7 ms                                                                     | 57.3 ms: 1.02x faster                                                   |
| pidigits       | 150 ms                                                                      | 149 ms: 1.00x faster                                                    |
| float          | 47.8 ms                                                                     | 48.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                                      | 125 ms: 1.01x faster                                                    |
| regex_compile  | 83.1 ms                                                                     | 82.3 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle               | 7.55 us                                                                     | 7.25 us: 1.04x faster                                                   |
| pickle_pure_python   | 178 us                                                                      | 174 us: 1.03x faster                                                    |
| pickle_dict          | 17.9 us                                                                     | 17.5 us: 1.02x faster                                                   |
| unpickle_pure_python | 127 us                                                                      | 125 us: 1.02x faster                                                    |
| json_loads           | 13.8 us                                                                     | 13.6 us: 1.01x faster                                                   |
| unpickle             | 8.64 us                                                                     | 8.57 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 62.3 ms                                                                     | 63.1 ms: 1.01x slower                                                   |
| xml_etree_parse      | 92.2 ms                                                                     | 93.7 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                            |

Benchmark hidden because not significant (6): unpickle_list, pickle_list, json_dumps, xml_etree_process, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.7 ms                                                                     | 23.1 ms: 1.07x faster                                                   |
| python_startup_no_site | 22.5 ms                                                                     | 21.0 ms: 1.07x faster                                                   |
| Geometric mean         | (ref)                                                                       | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 21.5 ms                                                                     | 21.8 ms: 1.01x slower                                                   |
| genshi_text     | 15.3 ms                                                                     | 15.6 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json                     | 3.36 ms                                                                     | 3.07 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 2.39 ms                                                                     | 2.24 ms: 1.07x faster                                                   |
| pycparser                | 716 ms                                                                      | 669 ms: 1.07x faster                                                    |
| python_startup           | 24.7 ms                                                                     | 23.1 ms: 1.07x faster                                                   |
| python_startup_no_site   | 22.5 ms                                                                     | 21.0 ms: 1.07x faster                                                   |
| deepcopy_memo            | 22.8 us                                                                     | 21.6 us: 1.05x faster                                                   |
| logging_silent           | 55.5 ns                                                                     | 53.2 ns: 1.04x faster                                                   |
| scimark_monte_carlo      | 41.9 ms                                                                     | 40.1 ms: 1.04x faster                                                   |
| typing_runtime_protocols | 71.1 us                                                                     | 68.2 us: 1.04x faster                                                   |
| scimark_sor              | 84.4 ms                                                                     | 81.0 ms: 1.04x faster                                                   |
| pickle                   | 7.55 us                                                                     | 7.25 us: 1.04x faster                                                   |
| sympy_sum                | 88.5 ms                                                                     | 85.7 ms: 1.03x faster                                                   |
| richards_super           | 31.6 ms                                                                     | 30.6 ms: 1.03x faster                                                   |
| meteor_contest           | 75.0 ms                                                                     | 72.7 ms: 1.03x faster                                                   |
| comprehensions           | 10.7 us                                                                     | 10.4 us: 1.03x faster                                                   |
| richards                 | 28.2 ms                                                                     | 27.4 ms: 1.03x faster                                                   |
| coroutines               | 13.3 ms                                                                     | 12.9 ms: 1.03x faster                                                   |
| html5lib                 | 37.0 ms                                                                     | 36.0 ms: 1.03x faster                                                   |
| pickle_pure_python       | 178 us                                                                      | 174 us: 1.03x faster                                                    |
| pickle_dict              | 17.9 us                                                                     | 17.5 us: 1.02x faster                                                   |
| fannkuch                 | 217 ms                                                                      | 212 ms: 1.02x faster                                                    |
| nbody                    | 58.7 ms                                                                     | 57.3 ms: 1.02x faster                                                   |
| go                       | 96.1 ms                                                                     | 94.1 ms: 1.02x faster                                                   |
| raytrace                 | 182 ms                                                                      | 178 ms: 1.02x faster                                                    |
| scimark_fft              | 172 ms                                                                      | 169 ms: 1.02x faster                                                    |
| pyflate                  | 282 ms                                                                      | 277 ms: 1.02x faster                                                    |
| bench_mp_pool            | 70.3 ms                                                                     | 69.0 ms: 1.02x faster                                                   |
| unpickle_pure_python     | 127 us                                                                      | 125 us: 1.02x faster                                                    |
| deltablue                | 2.03 ms                                                                     | 2.00 ms: 1.02x faster                                                   |
| sqlglot_normalize        | 175 ms                                                                      | 172 ms: 1.02x faster                                                    |
| sympy_integrate          | 13.1 ms                                                                     | 12.9 ms: 1.02x faster                                                   |
| docutils                 | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                  |
| sqlglot_parse            | 772 us                                                                      | 761 us: 1.01x faster                                                    |
| json_loads               | 13.8 us                                                                     | 13.6 us: 1.01x faster                                                   |
| tornado_http             | 85.0 ms                                                                     | 83.9 ms: 1.01x faster                                                   |
| sympy_str                | 164 ms                                                                      | 162 ms: 1.01x faster                                                    |
| regex_dna                | 126 ms                                                                      | 125 ms: 1.01x faster                                                    |
| 2to3                     | 222 ms                                                                      | 220 ms: 1.01x faster                                                    |
| sqlglot_transpile        | 991 us                                                                      | 981 us: 1.01x faster                                                    |
| sympy_expand             | 281 ms                                                                      | 278 ms: 1.01x faster                                                    |
| sqlglot_optimize         | 34.3 ms                                                                     | 33.9 ms: 1.01x faster                                                   |
| chameleon                | 4.76 ms                                                                     | 4.71 ms: 1.01x faster                                                   |
| generators               | 19.9 ms                                                                     | 19.7 ms: 1.01x faster                                                   |
| regex_compile            | 83.1 ms                                                                     | 82.3 ms: 1.01x faster                                                   |
| unpickle                 | 8.64 us                                                                     | 8.57 us: 1.01x faster                                                   |
| pprint_pformat           | 954 ms                                                                      | 948 ms: 1.01x faster                                                    |
| hexiom                   | 4.32 ms                                                                     | 4.29 ms: 1.01x faster                                                   |
| sqlite_synth             | 1.58 us                                                                     | 1.57 us: 1.00x faster                                                   |
| async_generators         | 238 ms                                                                      | 236 ms: 1.00x faster                                                    |
| mypy2                    | 436 ms                                                                      | 435 ms: 1.00x faster                                                    |
| pidigits                 | 150 ms                                                                      | 149 ms: 1.00x faster                                                    |
| crypto_pyaes             | 43.3 ms                                                                     | 43.5 ms: 1.00x slower                                                   |
| deepcopy_reduce          | 1.93 us                                                                     | 1.94 us: 1.01x slower                                                   |
| aiohttp                  | 889 us                                                                      | 897 us: 1.01x slower                                                    |
| spectral_norm            | 51.0 ms                                                                     | 51.5 ms: 1.01x slower                                                   |
| unpack_sequence          | 48.6 ns                                                                     | 49.1 ns: 1.01x slower                                                   |
| float                    | 47.8 ms                                                                     | 48.3 ms: 1.01x slower                                                   |
| chaos                    | 39.4 ms                                                                     | 39.8 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed  | 446 ms                                                                      | 451 ms: 1.01x slower                                                    |
| xml_etree_iterparse      | 62.3 ms                                                                     | 63.1 ms: 1.01x slower                                                   |
| django_template          | 21.5 ms                                                                     | 21.8 ms: 1.01x slower                                                   |
| logging_format           | 6.24 us                                                                     | 6.33 us: 1.02x slower                                                   |
| xml_etree_parse          | 92.2 ms                                                                     | 93.7 ms: 1.02x slower                                                   |
| gc_traversal             | 1.50 ms                                                                     | 1.53 ms: 1.02x slower                                                   |
| genshi_text              | 15.3 ms                                                                     | 15.6 ms: 1.02x slower                                                   |
| scimark_lu               | 70.7 ms                                                                     | 72.2 ms: 1.02x slower                                                   |
| telco                    | 4.57 ms                                                                     | 4.70 ms: 1.03x slower                                                   |
| mdp                      | 1.44 sec                                                                    | 1.49 sec: 1.04x slower                                                  |
| dulwich_log              | 39.7 ms                                                                     | 41.6 ms: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                            |

Benchmark hidden because not significant (29): bench_thread_pool, pylint, genshi_xml, async_tree_memoization_tg, regex_v8, async_tree_io_tg, mako, async_tree_io, async_tree_memoization, unpickle_list, nqueens, pickle_list, json_dumps, deepcopy, pathlib, xml_etree_process, pprint_safe_repr, regex_effbot, xml_etree_generate, logging_simple, coverage, tomli_loads, create_gc_cycles, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_tcp, async_tree_none_tg, thrift, asyncio_tcp_ssl


# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown