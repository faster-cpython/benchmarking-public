# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.055x faster
- HPT reliability: 74.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 1.96 sec: 1.00x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 495 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_none         | 394 ms                                                          | 237 ms: 1.66x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 289 ms: 1.62x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 55.5 ms: 1.25x faster                                                           |
| nbody          | 79.1 ms                                                         | 98.7 ms: 1.25x slower                                                           |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.2 us: 1.11x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.07 ms: 1.08x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 204 us: 1.08x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 54.3 ms: 1.13x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.9 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.40 ms: 1.23x faster                                                           |
| django_template | 36.0 ms                                                         | 38.2 ms: 1.06x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.5 ms: 1.26x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 166 us: 2.38x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 107 ms: 2.14x faster                                                            |
| async_tree_io            | 940 ms                                                          | 495 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_none          | 394 ms                                                          | 237 ms: 1.66x faster                                                            |
| pylint                   | 384 ms                                                          | 237 ms: 1.62x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 289 ms: 1.62x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.19 ms: 1.26x faster                                                           |
| float                    | 69.6 ms                                                         | 55.5 ms: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.40 ms: 1.23x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.2 us: 1.22x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 73.7 ms: 1.22x faster                                                           |
| go                       | 146 ms                                                          | 122 ms: 1.20x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 70.5 ms: 1.15x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.15x faster                                                           |
| chaos                    | 74.4 ms                                                         | 65.0 ms: 1.14x faster                                                           |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                           |
| thrift                   | 902 us                                                          | 792 us: 1.14x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 86.3 ns: 1.13x faster                                                           |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                            |
| deepcopy                 | 310 us                                                          | 275 us: 1.13x faster                                                            |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.43 ms: 1.11x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.2 us: 1.11x faster                                                           |
| pycparser                | 1.04 sec                                                        | 945 ms: 1.10x faster                                                            |
| coroutines               | 17.9 ms                                                         | 16.4 ms: 1.10x faster                                                           |
| pyflate                  | 422 ms                                                          | 385 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.99 ms: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.07 ms: 1.08x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.06 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 76.4 ms: 1.05x faster                                                           |
| regex_compile            | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| richards_super           | 49.9 ms                                                         | 49.5 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.96 sec: 1.00x slower                                                          |
| sympy_str                | 229 ms                                                          | 236 ms: 1.03x slower                                                            |
| mdp                      | 1.83 sec                                                        | 1.88 sec: 1.03x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.7 ms: 1.03x slower                                                           |
| raytrace                 | 303 ms                                                          | 313 ms: 1.04x slower                                                            |
| sympy_expand             | 391 ms                                                          | 406 ms: 1.04x slower                                                            |
| fannkuch                 | 317 ms                                                          | 331 ms: 1.04x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.5 ms: 1.05x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.7 us: 1.05x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.84 us: 1.06x slower                                                           |
| django_template          | 36.0 ms                                                         | 38.2 ms: 1.06x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 204 us: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                            |
| richards                 | 40.3 ms                                                         | 44.5 ms: 1.11x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.2 ms: 1.12x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 54.3 ms: 1.13x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 744 ms: 1.13x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 90.5 ms: 1.13x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 98.9 ms: 1.14x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 51.1 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.11 us: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.43 us: 1.16x slower                                                           |
| generators               | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.9 ms: 1.18x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.34 ms: 1.20x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                           |
| mypy2                    | 590 ms                                                          | 725 ms: 1.23x slower                                                            |
| nbody                    | 79.1 ms                                                         | 98.7 ms: 1.25x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 26.5 ms: 1.26x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 87.3 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 336 ms: 1.39x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.44 ms: 1.54x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, scimark_monte_carlo
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 74.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown