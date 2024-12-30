# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.168x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 245 ms: 1.08x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.78 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.0 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 442 ms: 2.13x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 442 ms: 2.08x faster                                                            |
| async_tree_none         | 394 ms                                                          | 202 ms: 1.95x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 250 ms: 1.87x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| float          | 69.6 ms                                                         | 59.1 ms: 1.18x faster                                                           |
| nbody          | 79.1 ms                                                         | 86.5 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.64 ms: 1.14x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 169 us: 1.12x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.3 ms: 1.09x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 262 us: 1.07x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 66.5 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.53 ms: 1.21x faster                                                           |
| django_template | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                            |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| async_tree_io            | 940 ms                                                          | 442 ms: 2.13x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 442 ms: 2.08x faster                                                            |
| async_tree_none          | 394 ms                                                          | 202 ms: 1.95x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 250 ms: 1.87x faster                                                            |
| pylint                   | 384 ms                                                          | 216 ms: 1.77x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.56 ms: 1.58x faster                                                           |
| go                       | 146 ms                                                          | 95.8 ms: 1.52x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 70.2 ns: 1.39x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.2 ms: 1.37x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 59.9 ms: 1.36x faster                                                           |
| deepcopy                 | 310 us                                                          | 231 us: 1.34x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 22.1 us: 1.34x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.4 ms: 1.31x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.31x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.30x faster                                                           |
| pyflate                  | 422 ms                                                          | 334 ms: 1.26x faster                                                            |
| generators               | 31.6 ms                                                         | 25.0 ms: 1.26x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.87 ms: 1.26x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 828 ms: 1.26x faster                                                            |
| thrift                   | 902 us                                                          | 722 us: 1.25x faster                                                            |
| richards_super           | 49.9 ms                                                         | 40.4 ms: 1.23x faster                                                           |
| raytrace                 | 303 ms                                                          | 247 ms: 1.22x faster                                                            |
| scimark_sor              | 115 ms                                                          | 94.6 ms: 1.22x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.53 ms: 1.21x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.5 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.0 ms: 1.18x faster                                                           |
| float                    | 69.6 ms                                                         | 59.1 ms: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 69.9 ms: 1.15x faster                                                           |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| richards                 | 40.3 ms                                                         | 35.2 ms: 1.14x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.64 ms: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 169 us: 1.12x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.39 us: 1.12x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.92 ms: 1.11x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.2 ms: 1.11x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.10x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.78 sec: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.3 ms: 1.09x faster                                                           |
| 2to3                     | 265 ms                                                          | 245 ms: 1.08x faster                                                            |
| fannkuch                 | 317 ms                                                          | 293 ms: 1.08x faster                                                            |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.8 ms: 1.07x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 262 us: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.29 sec: 1.06x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 624 ms: 1.06x faster                                                            |
| sympy_expand             | 391 ms                                                          | 372 ms: 1.05x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.1 ms: 1.02x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.69 us: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 66.5 ms: 1.08x slower                                                           |
| nbody                    | 79.1 ms                                                         | 86.5 ms: 1.09x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.2 ms: 1.10x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| mypy2                    | 590 ms                                                          | 686 ms: 1.16x slower                                                            |
| async_generators         | 241 ms                                                          | 298 ms: 1.24x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.3 ms: 1.32x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.47 ms: 1.34x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.79 ms: 1.40x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (3): genshi_xml, meteor_contest, scimark_fft
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.168x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown