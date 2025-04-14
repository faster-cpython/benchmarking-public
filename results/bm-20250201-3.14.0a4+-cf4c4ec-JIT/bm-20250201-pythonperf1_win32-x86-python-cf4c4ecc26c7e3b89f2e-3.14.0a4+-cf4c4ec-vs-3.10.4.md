# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.039x faster
- HPT reliability: 59.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 272 ms: 1.03x slower                                                            |
| docutils       | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                          |
| html5lib       | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 477 ms: 1.97x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 493 ms: 1.87x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| async_tree_none         | 394 ms                                                          | 235 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 53.2 ms: 1.31x faster                                                           |
| nbody          | 79.1 ms                                                         | 110 ms: 1.39x slower                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_dna      | 131 ms                                                          | 125 ms: 1.05x faster                                                            |
| regex_compile  | 117 ms                                                          | 119 ms: 1.02x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.86 sec: 1.02x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 9.76 ms: 1.01x faster                                                           |
| json_loads           | 22.4 us                                                         | 22.7 us: 1.01x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.27 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 18.6 us: 1.02x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.13 us: 1.05x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 301 us: 1.07x slower                                                            |
| unpickle             | 9.82 us                                                         | 11.0 us: 1.12x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 54.6 ms: 1.13x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 216 us: 1.14x slower                                                            |
| pickle               | 7.83 us                                                         | 9.22 us: 1.18x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.1 ms: 1.23x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.8 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.64 ms: 1.19x faster                                                           |
| django_template | 36.0 ms                                                         | 38.1 ms: 1.06x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 56.8 ms: 1.22x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.3 ms: 1.25x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 166 us: 2.38x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 110 ms: 2.09x faster                                                            |
| async_tree_io            | 940 ms                                                          | 477 ms: 1.97x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 493 ms: 1.87x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| async_tree_none          | 394 ms                                                          | 235 ms: 1.68x faster                                                            |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                            |
| float                    | 69.6 ms                                                         | 53.2 ms: 1.31x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.11 ms: 1.30x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 73.3 ms: 1.22x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 66.8 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.20x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 81.6 ns: 1.20x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.64 ms: 1.19x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 25.4 us: 1.17x faster                                                           |
| go                       | 146 ms                                                          | 127 ms: 1.15x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 71.7 ms: 1.13x faster                                                           |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                            |
| thrift                   | 902 us                                                          | 806 us: 1.12x faster                                                            |
| chaos                    | 74.4 ms                                                         | 66.7 ms: 1.12x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 72.0 ms: 1.11x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.20 ms: 1.11x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.1 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| pyflate                  | 422 ms                                                          | 383 ms: 1.10x faster                                                            |
| pycparser                | 1.04 sec                                                        | 962 ms: 1.08x faster                                                            |
| deepcopy                 | 310 us                                                          | 287 us: 1.08x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.47 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                           |
| richards_super           | 49.9 ms                                                         | 47.2 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                            |
| regex_dna                | 131 ms                                                          | 125 ms: 1.05x faster                                                            |
| coroutines               | 17.9 ms                                                         | 17.2 ms: 1.04x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.08 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.16 ms: 1.03x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.86 sec: 1.02x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 9.76 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                          |
| json_loads               | 22.4 us                                                         | 22.7 us: 1.01x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.27 us: 1.02x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 18.6 us: 1.02x slower                                                           |
| regex_compile            | 117 ms                                                          | 119 ms: 1.02x slower                                                            |
| 2to3                     | 265 ms                                                          | 272 ms: 1.03x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 64.3 ms: 1.04x slower                                                           |
| sympy_str                | 229 ms                                                          | 238 ms: 1.04x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.6 us: 1.05x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.13 us: 1.05x slower                                                           |
| richards                 | 40.3 ms                                                         | 42.3 ms: 1.05x slower                                                           |
| sympy_expand             | 391 ms                                                          | 411 ms: 1.05x slower                                                            |
| raytrace                 | 303 ms                                                          | 318 ms: 1.05x slower                                                            |
| django_template          | 36.0 ms                                                         | 38.1 ms: 1.06x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.93 sec: 1.06x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.8 ms: 1.07x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 301 us: 1.07x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 44.6 ns: 1.11x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.0 us: 1.12x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 3.00 us: 1.12x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.54 sec: 1.13x slower                                                          |
| scimark_fft              | 216 ms                                                          | 244 ms: 1.13x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 54.6 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.8 ms: 1.13x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 216 us: 1.14x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 752 ms: 1.14x slower                                                            |
| fannkuch                 | 317 ms                                                          | 364 ms: 1.15x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 92.6 ms: 1.16x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 51.9 ms: 1.16x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 102 ms: 1.18x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.22 us: 1.18x slower                                                           |
| generators               | 31.6 ms                                                         | 37.5 ms: 1.19x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.73 us: 1.20x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.37 ms: 1.20x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.51 us: 1.20x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 56.8 ms: 1.22x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.1 ms: 1.23x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 26.3 ms: 1.25x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.8 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                            |
| nbody                    | 79.1 ms                                                         | 110 ms: 1.39x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.9 ms: 1.43x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.85 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.91 ms: 1.64x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): json, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 59.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown