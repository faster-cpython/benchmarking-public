# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.086x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 270 ms: 1.02x slower                                                            |
| docutils       | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                          |
| html5lib       | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 491 ms: 1.92x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 494 ms: 1.86x faster                                                            |
| async_tree_none         | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 283 ms: 1.65x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| float          | 69.6 ms                                                         | 59.8 ms: 1.16x faster                                                           |
| nbody          | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| regex_dna      | 131 ms                                                          | 125 ms: 1.04x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 9.21 ms: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 184 us: 1.03x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 50.8 ms: 1.06x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 297 us: 1.06x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.3 us: 1.15x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.76 us: 1.17x slower                                                           |
| pickle               | 7.83 us                                                         | 9.66 us: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.9 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.13 ms: 1.12x faster                                                           |
| django_template | 36.0 ms                                                         | 37.9 ms: 1.05x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 49.5 ms: 1.06x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 154 us: 2.56x faster                                                            |
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| async_tree_io            | 940 ms                                                          | 491 ms: 1.92x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 494 ms: 1.86x faster                                                            |
| async_tree_none          | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| pylint                   | 384 ms                                                          | 230 ms: 1.67x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 283 ms: 1.65x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.05 ms: 1.32x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 61.4 ms: 1.32x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.4 us: 1.32x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 69.8 ms: 1.29x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                           |
| chaos                    | 74.4 ms                                                         | 59.3 ms: 1.26x faster                                                           |
| go                       | 146 ms                                                          | 116 ms: 1.25x faster                                                            |
| deepcopy                 | 310 us                                                          | 258 us: 1.20x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 67.5 ms: 1.20x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 81.6 ns: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| pyflate                  | 422 ms                                                          | 361 ms: 1.17x faster                                                            |
| float                    | 69.6 ms                                                         | 59.8 ms: 1.16x faster                                                           |
| pycparser                | 1.04 sec                                                        | 901 ms: 1.16x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.88 ms: 1.13x faster                                                           |
| generators               | 31.6 ms                                                         | 28.1 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.13 ms: 1.12x faster                                                           |
| thrift                   | 902 us                                                          | 807 us: 1.12x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.19 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.55 ms: 1.11x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.1 ms: 1.10x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.44 ms: 1.10x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.2 ms: 1.10x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                           |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 79.7 ms: 1.09x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                          |
| scimark_sor              | 115 ms                                                          | 107 ms: 1.07x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.21 ms: 1.07x faster                                                           |
| fannkuch                 | 317 ms                                                          | 297 ms: 1.07x faster                                                            |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.06 ms: 1.06x faster                                                           |
| richards_super           | 49.9 ms                                                         | 47.5 ms: 1.05x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 711 ms: 1.05x faster                                                            |
| raytrace                 | 303 ms                                                          | 290 ms: 1.04x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 76.9 ms: 1.04x faster                                                           |
| regex_dna                | 131 ms                                                          | 125 ms: 1.04x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 184 us: 1.03x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 78.3 ms: 1.02x faster                                                           |
| sympy_str                | 229 ms                                                          | 226 ms: 1.02x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 16.5 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.71 us: 1.01x slower                                                           |
| scimark_fft              | 216 ms                                                          | 219 ms: 1.01x slower                                                            |
| sympy_expand             | 391 ms                                                          | 395 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                          |
| 2to3                     | 265 ms                                                          | 270 ms: 1.02x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                           |
| django_template          | 36.0 ms                                                         | 37.9 ms: 1.05x slower                                                           |
| richards                 | 40.3 ms                                                         | 42.4 ms: 1.05x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.8 ms: 1.06x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 47.3 ms: 1.06x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 297 us: 1.06x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 49.5 ms: 1.06x slower                                                           |
| sqlglot_normalize        | 230 ms                                                          | 246 ms: 1.07x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 709 ms: 1.08x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.48 sec: 1.08x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 44.7 ns: 1.12x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.9 ms: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.3 us: 1.15x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.76 us: 1.17x slower                                                           |
| nbody                    | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.40 us: 1.19x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.80 us: 1.21x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.66 us: 1.23x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.9 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 307 ms: 1.28x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.79 ms: 1.40x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 95.5 ms: 1.44x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.24 ms: 1.50x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): json, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown