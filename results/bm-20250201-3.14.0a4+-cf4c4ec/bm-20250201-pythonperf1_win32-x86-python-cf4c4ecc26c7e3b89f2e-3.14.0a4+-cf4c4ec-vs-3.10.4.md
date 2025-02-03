# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                          |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 451 ms: 2.05x faster                                                            |
| async_tree_io           | 940 ms                                                          | 461 ms: 2.04x faster                                                            |
| async_tree_none         | 394 ms                                                          | 216 ms: 1.82x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 264 ms: 1.77x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.92x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                           |
| nbody          | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.08 ms: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 274 us: 1.02x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.01x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 49.6 ms: 1.03x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 68.0 ms: 1.10x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.0 us: 1.12x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.68 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.1 us: 1.16x slower                                                           |
| pickle               | 7.83 us                                                         | 9.30 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.88 ms: 1.16x faster                                                           |
| django_template | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 47.2 ms: 1.01x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.76x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 451 ms: 2.05x faster                                                            |
| async_tree_io            | 940 ms                                                          | 461 ms: 2.04x faster                                                            |
| async_tree_none          | 394 ms                                                          | 216 ms: 1.82x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 264 ms: 1.77x faster                                                            |
| pylint                   | 384 ms                                                          | 220 ms: 1.74x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.84 ms: 1.42x faster                                                           |
| go                       | 146 ms                                                          | 105 ms: 1.39x faster                                                            |
| chaos                    | 74.4 ms                                                         | 54.2 ms: 1.37x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 59.5 ms: 1.37x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.8 us: 1.36x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.31x faster                                                           |
| deepcopy                 | 310 us                                                          | 243 us: 1.28x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 71.2 ms: 1.26x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 78.7 ns: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                           |
| pyflate                  | 422 ms                                                          | 344 ms: 1.23x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                           |
| thrift                   | 902 us                                                          | 749 us: 1.21x faster                                                            |
| pycparser                | 1.04 sec                                                        | 871 ms: 1.20x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                           |
| generators               | 31.6 ms                                                         | 27.1 ms: 1.17x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.31 ms: 1.16x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.88 ms: 1.16x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 51.1 ms: 1.15x faster                                                           |
| raytrace                 | 303 ms                                                          | 267 ms: 1.13x faster                                                            |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.9 ms: 1.11x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.5 ms: 1.11x faster                                                           |
| scimark_sor              | 115 ms                                                          | 105 ms: 1.10x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.97 ms: 1.09x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.8 ms: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.08 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 81.3 ms: 1.07x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.55 us: 1.05x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.2 ms: 1.04x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.1 ms: 1.04x faster                                                           |
| fannkuch                 | 317 ms                                                          | 306 ms: 1.04x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 224 ms: 1.03x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 641 ms: 1.03x faster                                                            |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.02x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 274 us: 1.02x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 47.2 ms: 1.01x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 49.6 ms: 1.03x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                           |
| scimark_fft              | 216 ms                                                          | 226 ms: 1.05x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 85.1 ms: 1.05x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 42.4 ns: 1.06x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 68.0 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.0 us: 1.12x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.87 us: 1.12x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.5 ms: 1.13x slower                                                           |
| nbody                    | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.25 us: 1.13x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.68 us: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.1 us: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.30 us: 1.19x slower                                                           |
| async_generators         | 241 ms                                                          | 302 ms: 1.25x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 93.0 ms: 1.40x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.15 ms: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (5): json, richards, json_loads, meteor_contest, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown