# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-x86
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                                   |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                                 |
| html5lib       | 52.1 ms                                                         | 50.3 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 486 ms: 1.93x faster                                                                   |
| async_tree_cpu_io_mixed | 922 ms                                                          | 481 ms: 1.92x faster                                                                   |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.72x faster                                                                   |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                                   |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.48x faster                                                                   |
| float          | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                                  |
| nbody          | 79.1 ms                                                         | 91.0 ms: 1.15x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                                   |
| regex_compile  | 117 ms                                                          | 111 ms: 1.05x faster                                                                   |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                                  |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.32 ms: 1.18x faster                                                                  |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                                   |
| tomli_loads          | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                                  |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.03x faster                                                                  |
| unpickle_pure_python | 189 us                                                          | 186 us: 1.02x faster                                                                   |
| pickle_pure_python   | 280 us                                                          | 287 us: 1.03x slower                                                                   |
| xml_etree_process    | 48.1 ms                                                         | 51.3 ms: 1.07x slower                                                                  |
| xml_etree_generate   | 61.6 ms                                                         | 68.8 ms: 1.12x slower                                                                  |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.5 ms: 1.19x slower                                                                  |
| python_startup         | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                                  |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.97 ms: 1.14x faster                                                                  |
| django_template | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                                  |
| genshi_xml      | 46.6 ms                                                         | 50.5 ms: 1.08x slower                                                                  |
| genshi_text     | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                                  |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.61x faster                                                                   |
| pidigits                 | 502 ms                                                          | 202 ms: 2.48x faster                                                                   |
| pathlib                  | 81.2 ms                                                         | 34.1 ms: 2.38x faster                                                                  |
| async_tree_io            | 940 ms                                                          | 486 ms: 1.93x faster                                                                   |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 481 ms: 1.92x faster                                                                   |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.72x faster                                                                   |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                                   |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                                   |
| deltablue                | 4.04 ms                                                         | 2.86 ms: 1.41x faster                                                                  |
| logging_silent           | 97.9 ns                                                         | 72.8 ns: 1.34x faster                                                                  |
| go                       | 146 ms                                                          | 108 ms: 1.34x faster                                                                   |
| deepcopy_memo            | 29.6 us                                                         | 22.3 us: 1.33x faster                                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 61.7 ms: 1.32x faster                                                                  |
| scimark_lu               | 89.8 ms                                                         | 69.6 ms: 1.29x faster                                                                  |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                                   |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                                  |
| chaos                    | 74.4 ms                                                         | 59.2 ms: 1.26x faster                                                                  |
| float                    | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                                  |
| pyflate                  | 422 ms                                                          | 354 ms: 1.19x faster                                                                   |
| raytrace                 | 303 ms                                                          | 254 ms: 1.19x faster                                                                   |
| json_dumps               | 9.82 ms                                                         | 8.32 ms: 1.18x faster                                                                  |
| generators               | 31.6 ms                                                         | 26.9 ms: 1.17x faster                                                                  |
| richards_super           | 49.9 ms                                                         | 43.0 ms: 1.16x faster                                                                  |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.16x faster                                                                  |
| hexiom                   | 6.13 ms                                                         | 5.31 ms: 1.16x faster                                                                  |
| thrift                   | 902 us                                                          | 786 us: 1.15x faster                                                                   |
| mako                     | 9.10 ms                                                         | 7.97 ms: 1.14x faster                                                                  |
| sqlglot_transpile        | 1.58 ms                                                         | 1.40 ms: 1.13x faster                                                                  |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                                   |
| coroutines               | 17.9 ms                                                         | 16.0 ms: 1.12x faster                                                                  |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                                   |
| pycparser                | 1.04 sec                                                        | 930 ms: 1.12x faster                                                                   |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.12x faster                                                                   |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.12x faster                                                                  |
| tomli_loads              | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                                 |
| nqueens                  | 87.1 ms                                                         | 79.8 ms: 1.09x faster                                                                  |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.9 ms: 1.09x faster                                                                  |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                                   |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                                 |
| richards                 | 40.3 ms                                                         | 37.3 ms: 1.08x faster                                                                  |
| spectral_norm            | 80.2 ms                                                         | 75.1 ms: 1.07x faster                                                                  |
| json                     | 4.76 ms                                                         | 4.46 ms: 1.07x faster                                                                  |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.07x faster                                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                                  |
| django_template          | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 1.06 ms: 1.05x faster                                                                  |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                                 |
| regex_compile            | 117 ms                                                          | 111 ms: 1.05x faster                                                                   |
| fannkuch                 | 317 ms                                                          | 301 ms: 1.05x faster                                                                   |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                                  |
| html5lib                 | 52.1 ms                                                         | 50.3 ms: 1.04x faster                                                                  |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.03x faster                                                                  |
| sympy_integrate          | 16.6 ms                                                         | 16.1 ms: 1.03x faster                                                                  |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                                   |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                                   |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 2.63 us: 1.02x faster                                                                  |
| unpickle_pure_python     | 189 us                                                          | 186 us: 1.02x faster                                                                   |
| meteor_contest           | 80.0 ms                                                         | 80.6 ms: 1.01x slower                                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.39 sec: 1.01x slower                                                                 |
| pprint_safe_repr         | 658 ms                                                          | 669 ms: 1.02x slower                                                                   |
| sqlglot_normalize        | 230 ms                                                          | 235 ms: 1.02x slower                                                                   |
| pickle_pure_python       | 280 us                                                          | 287 us: 1.03x slower                                                                   |
| xml_etree_process        | 48.1 ms                                                         | 51.3 ms: 1.07x slower                                                                  |
| scimark_fft              | 216 ms                                                          | 231 ms: 1.07x slower                                                                   |
| genshi_xml               | 46.6 ms                                                         | 50.5 ms: 1.08x slower                                                                  |
| genshi_text              | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                                  |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                                  |
| xml_etree_generate       | 61.6 ms                                                         | 68.8 ms: 1.12x slower                                                                  |
| nbody                    | 79.1 ms                                                         | 91.0 ms: 1.15x slower                                                                  |
| python_startup_no_site   | 18.1 ms                                                         | 21.5 ms: 1.19x slower                                                                  |
| logging_format           | 7.91 us                                                         | 9.55 us: 1.21x slower                                                                  |
| logging_simple           | 7.29 us                                                         | 8.82 us: 1.21x slower                                                                  |
| python_startup           | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                                  |
| async_generators         | 241 ms                                                          | 317 ms: 1.31x slower                                                                   |
| bench_mp_pool            | 66.4 ms                                                         | 90.0 ms: 1.36x slower                                                                  |
| telco                    | 4.83 ms                                                         | 6.57 ms: 1.36x slower                                                                  |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                                  |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                                  |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                           |

Benchmark hidden because not significant (2): sqlglot_optimize, sympy_expand
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown