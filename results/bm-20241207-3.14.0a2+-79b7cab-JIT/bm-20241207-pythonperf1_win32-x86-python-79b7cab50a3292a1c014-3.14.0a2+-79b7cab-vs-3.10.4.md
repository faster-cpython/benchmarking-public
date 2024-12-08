# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.060x faster
- HPT reliability: 89.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 259 ms: 1.02x faster                                                            |
| html5lib       | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 480 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 480 ms: 1.92x faster                                                            |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 282 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 57.5 ms: 1.21x faster                                                           |
| nbody          | 79.1 ms                                                         | 99.4 ms: 1.26x slower                                                           |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.04x faster                                                           |
| regex_compile  | 117 ms                                                          | 115 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 203 us: 1.07x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 304 us: 1.08x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 71.5 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.31 ms: 1.25x faster                                                           |
| django_template | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 57.1 ms: 1.22x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.0 ms: 1.24x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 166 us: 2.38x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 110 ms: 2.10x faster                                                            |
| async_tree_io            | 940 ms                                                          | 480 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 480 ms: 1.92x faster                                                            |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                            |
| pylint                   | 384 ms                                                          | 230 ms: 1.67x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 282 ms: 1.66x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.19 ms: 1.26x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.31 ms: 1.25x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.2 ms: 1.24x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 66.6 ms: 1.22x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.3 us: 1.22x faster                                                           |
| float                    | 69.6 ms                                                         | 57.5 ms: 1.21x faster                                                           |
| go                       | 146 ms                                                          | 121 ms: 1.20x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 83.1 ns: 1.18x faster                                                           |
| thrift                   | 902 us                                                          | 776 us: 1.16x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.99 us: 1.15x faster                                                           |
| chaos                    | 74.4 ms                                                         | 65.1 ms: 1.14x faster                                                           |
| pycparser                | 1.04 sec                                                        | 913 ms: 1.14x faster                                                            |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 52.0 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.19 ms: 1.11x faster                                                           |
| deepcopy                 | 310 us                                                          | 281 us: 1.10x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.6 ms: 1.08x faster                                                           |
| pyflate                  | 422 ms                                                          | 391 ms: 1.08x faster                                                            |
| json                     | 4.76 ms                                                         | 4.43 ms: 1.08x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.47 ms: 1.08x faster                                                           |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.06x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.04x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| 2to3                     | 265 ms                                                          | 259 ms: 1.02x faster                                                            |
| regex_compile            | 117 ms                                                          | 115 ms: 1.02x faster                                                            |
| richards_super           | 49.9 ms                                                         | 49.3 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.21 ms: 1.01x faster                                                           |
| raytrace                 | 303 ms                                                          | 301 ms: 1.00x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 79.9 ms: 1.00x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.02x slower                                                          |
| django_template          | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                           |
| sympy_str                | 229 ms                                                          | 235 ms: 1.03x slower                                                            |
| sympy_expand             | 391 ms                                                          | 408 ms: 1.05x slower                                                            |
| comprehensions           | 17.7 us                                                         | 18.7 us: 1.05x slower                                                           |
| fannkuch                 | 317 ms                                                          | 335 ms: 1.06x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.85 us: 1.06x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 203 us: 1.07x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 304 us: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 18.1 ms: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.51 sec: 1.10x slower                                                          |
| richards                 | 40.3 ms                                                         | 44.4 ms: 1.10x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 732 ms: 1.11x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 89.8 ms: 1.12x slower                                                           |
| scimark_fft              | 216 ms                                                          | 246 ms: 1.14x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 99.5 ms: 1.14x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.02 ms: 1.14x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.07 us: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.42 us: 1.15x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 51.7 ms: 1.16x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 71.5 ms: 1.16x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.7 ms: 1.18x slower                                                           |
| generators               | 31.6 ms                                                         | 37.8 ms: 1.20x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 57.1 ms: 1.22x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 26.0 ms: 1.24x slower                                                           |
| nbody                    | 79.1 ms                                                         | 99.4 ms: 1.26x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 87.0 ms: 1.31x slower                                                           |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.76 ms: 1.37x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 981 us: 1.41x slower                                                            |
| telco                    | 4.83 ms                                                         | 7.19 ms: 1.49x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (4): regex_v8, scimark_monte_carlo, docutils, pathlib
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 89.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown