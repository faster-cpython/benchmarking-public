# Results vs. 3.10.4

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-x86
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.157x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 243 ms: 1.09x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 43.5 ms: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 426 ms: 2.21x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 434 ms: 2.13x faster                                                            |
| async_tree_none         | 394 ms                                                          | 194 ms: 2.03x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 240 ms: 1.94x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.07x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 55.8 ms: 1.25x faster                                                           |
| nbody          | 79.1 ms                                                         | 85.8 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.43x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.16x faster                                                            |
| regex_dna      | 131 ms                                                          | 126 ms: 1.03x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.81 ms: 1.12x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 171 us: 1.11x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 259 us: 1.08x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.79 ms: 1.17x faster                                                           |
| django_template | 36.0 ms                                                         | 31.8 ms: 1.13x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 45.0 ms: 1.04x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.5 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                                            |
| pidigits                 | 502 ms                                                          | 197 ms: 2.56x faster                                                            |
| async_tree_io            | 940 ms                                                          | 426 ms: 2.21x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 434 ms: 2.13x faster                                                            |
| async_tree_none          | 394 ms                                                          | 194 ms: 2.03x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 240 ms: 1.94x faster                                                            |
| pylint                   | 384 ms                                                          | 216 ms: 1.77x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.59 ms: 1.56x faster                                                           |
| go                       | 146 ms                                                          | 96.4 ms: 1.51x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 70.7 ns: 1.38x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.0 ms: 1.38x faster                                                           |
| deepcopy                 | 310 us                                                          | 227 us: 1.37x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 60.9 ms: 1.34x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.2 us: 1.33x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.6 ms: 1.31x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.8 us: 1.29x faster                                                           |
| generators               | 31.6 ms                                                         | 24.6 ms: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 812 ms: 1.28x faster                                                            |
| pyflate                  | 422 ms                                                          | 336 ms: 1.25x faster                                                            |
| raytrace                 | 303 ms                                                          | 242 ms: 1.25x faster                                                            |
| thrift                   | 902 us                                                          | 721 us: 1.25x faster                                                            |
| float                    | 69.6 ms                                                         | 55.8 ms: 1.25x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.00 ms: 1.23x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 43.5 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.3 ms: 1.18x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.79 ms: 1.17x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                            |
| regex_compile            | 117 ms                                                          | 101 ms: 1.16x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 75.6 ms: 1.15x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.8 ms: 1.15x faster                                                           |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                            |
| json                     | 4.76 ms                                                         | 4.17 ms: 1.14x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.8 ms: 1.13x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 71.3 ms: 1.12x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.81 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.11x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.42 us: 1.11x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 171 us: 1.11x faster                                                            |
| 2to3                     | 265 ms                                                          | 243 ms: 1.09x faster                                                            |
| richards                 | 40.3 ms                                                         | 36.8 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.97 ms: 1.09x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| coroutines               | 17.9 ms                                                         | 16.6 ms: 1.08x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 259 us: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| sympy_str                | 229 ms                                                          | 213 ms: 1.07x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.7 ms: 1.07x faster                                                           |
| fannkuch                 | 317 ms                                                          | 298 ms: 1.06x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 217 ms: 1.06x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.05x faster                                                          |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 45.0 ms: 1.04x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                                          |
| regex_dna                | 131 ms                                                          | 126 ms: 1.03x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.5 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 647 ms: 1.02x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 82.2 ms: 1.03x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.80 us: 1.07x slower                                                           |
| nbody                    | 79.1 ms                                                         | 85.8 ms: 1.08x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                                           |
| mypy2                    | 590 ms                                                          | 680 ms: 1.15x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 302 ms: 1.25x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.2 ms: 1.31x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.73 ms: 1.39x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): scimark_fft
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.157x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown