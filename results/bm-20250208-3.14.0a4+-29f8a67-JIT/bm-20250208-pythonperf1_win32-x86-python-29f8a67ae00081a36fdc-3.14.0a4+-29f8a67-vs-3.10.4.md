# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.079x faster
- HPT reliability: 97.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 272 ms: 1.02x slower                                                            |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                          |
| html5lib       | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 481 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_none         | 394 ms                                                          | 231 ms: 1.70x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| float          | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                           |
| nbody          | 79.1 ms                                                         | 114 ms: 1.44x slower                                                            |
| Geometric mean | (ref)                                                           | 1.31x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_dna      | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.10x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.26 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.95 us: 1.01x faster                                                           |
| pickle_list          | 3.22 us                                                         | 3.28 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 18.7 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 326 us: 1.16x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 226 us: 1.19x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 73.7 ms: 1.20x slower                                                           |
| pickle               | 7.83 us                                                         | 9.54 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.9 ms: 1.21x slower                                                           |
| python_startup         | 22.9 ms                                                         | 29.0 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.63 ms: 1.19x faster                                                           |
| django_template | 36.0 ms                                                         | 35.8 ms: 1.01x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 173 us: 2.29x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.25x faster                                                            |
| async_tree_io            | 940 ms                                                          | 481 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_none          | 394 ms                                                          | 231 ms: 1.70x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                            |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 69.9 ns: 1.40x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.4 us: 1.38x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.97 ms: 1.36x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 66.2 ms: 1.36x faster                                                           |
| generators               | 31.6 ms                                                         | 23.4 ms: 1.35x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                            |
| chaos                    | 74.4 ms                                                         | 56.7 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                           |
| pyflate                  | 422 ms                                                          | 340 ms: 1.24x faster                                                            |
| deepcopy                 | 310 us                                                          | 252 us: 1.23x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.22x faster                                                           |
| thrift                   | 902 us                                                          | 741 us: 1.22x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 65.9 ms: 1.22x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.0 ms: 1.21x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 67.7 ms: 1.20x faster                                                           |
| raytrace                 | 303 ms                                                          | 253 ms: 1.20x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.63 ms: 1.19x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.7 ms: 1.17x faster                                                           |
| richards_super           | 49.9 ms                                                         | 43.8 ms: 1.14x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.8 ms: 1.13x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.19 ms: 1.12x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.4 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.10x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 74.6 ms: 1.09x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.46 ms: 1.08x faster                                                           |
| comprehensions           | 17.7 us                                                         | 16.4 us: 1.08x faster                                                           |
| pycparser                | 1.04 sec                                                        | 968 ms: 1.08x faster                                                            |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.26 ms: 1.06x faster                                                           |
| richards                 | 40.3 ms                                                         | 38.1 ms: 1.06x faster                                                           |
| json                     | 4.76 ms                                                         | 4.52 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.07 ms: 1.04x faster                                                           |
| regex_dna                | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.93 ms: 1.03x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.63 us: 1.02x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.81 sec: 1.01x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.95 us: 1.01x faster                                                           |
| django_template          | 36.0 ms                                                         | 35.8 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.28 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.3 sec: 1.02x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.28 us: 1.02x slower                                                           |
| sympy_str                | 229 ms                                                          | 234 ms: 1.02x slower                                                            |
| 2to3                     | 265 ms                                                          | 272 ms: 1.02x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.1 ms: 1.02x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 18.7 us: 1.02x slower                                                           |
| sympy_expand             | 391 ms                                                          | 409 ms: 1.05x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 50.2 ms: 1.12x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.90 us: 1.12x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.21 us: 1.13x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 92.3 ms: 1.15x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.59 sec: 1.16x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 326 us: 1.16x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 773 ms: 1.17x slower                                                            |
| coverage                 | 46.6 ms                                                         | 55.1 ms: 1.18x slower                                                           |
| scimark_fft              | 216 ms                                                          | 258 ms: 1.19x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 226 us: 1.19x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 73.7 ms: 1.20x slower                                                           |
| fannkuch                 | 317 ms                                                          | 380 ms: 1.20x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 21.9 ms: 1.21x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.54 us: 1.22x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 106 ms: 1.22x slower                                                            |
| python_startup           | 22.9 ms                                                         | 29.0 ms: 1.27x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 54.3 ns: 1.36x slower                                                           |
| async_generators         | 241 ms                                                          | 335 ms: 1.39x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.4 ms: 1.44x slower                                                           |
| nbody                    | 79.1 ms                                                         | 114 ms: 1.44x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.85 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.89 ms: 1.63x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (3): json_loads, regex_compile, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 97.38% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown