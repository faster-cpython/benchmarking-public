# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.418x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 224 ms: 1.18x faster                                                  |
| docutils       | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                |
| html5lib       | 52.1 ms                                                         | 38.4 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                           | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.79x faster                                                  |
| async_tree_io           | 940 ms                                                          | 408 ms: 2.30x faster                                                  |
| async_tree_none         | 394 ms                                                          | 175 ms: 2.25x faster                                                  |
| async_tree_memoization  | 467 ms                                                          | 212 ms: 2.20x faster                                                  |
| Geometric mean          | (ref)                                                           | 2.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 149 ms: 3.38x faster                                                  |
| float          | 69.6 ms                                                         | 44.5 ms: 1.57x faster                                                 |
| nbody          | 79.1 ms                                                         | 64.3 ms: 1.23x faster                                                 |
| Geometric mean | (ref)                                                           | 1.87x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 82.5 ms: 1.41x faster                                                 |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                           | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.27 ms: 1.57x faster                                                 |
| json_loads           | 22.4 us                                                         | 14.7 us: 1.52x faster                                                 |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.41x faster                                                  |
| xml_etree_parse      | 120 ms                                                          | 89.1 ms: 1.35x faster                                                 |
| tomli_loads          | 1.91 sec                                                        | 1.44 sec: 1.33x faster                                                |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                  |
| xml_etree_process    | 48.1 ms                                                         | 39.7 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.0 ms: 1.09x faster                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                 |
| python_startup         | 22.9 ms                                                         | 26.2 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.4 ms: 1.42x faster                                                 |
| mako            | 9.10 ms                                                         | 6.68 ms: 1.36x faster                                                 |
| genshi_xml      | 46.6 ms                                                         | 34.4 ms: 1.35x faster                                                 |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 107 us: 3.68x faster                                                  |
| pidigits                 | 502 ms                                                          | 149 ms: 3.38x faster                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.79x faster                                                  |
| pathlib                  | 81.2 ms                                                         | 32.2 ms: 2.53x faster                                                 |
| async_tree_io            | 940 ms                                                          | 408 ms: 2.30x faster                                                  |
| async_tree_none          | 394 ms                                                          | 175 ms: 2.25x faster                                                  |
| mdp                      | 1.83 sec                                                        | 818 ms: 2.23x faster                                                  |
| async_tree_memoization   | 467 ms                                                          | 212 ms: 2.20x faster                                                  |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                  |
| chaos                    | 74.4 ms                                                         | 39.5 ms: 1.88x faster                                                 |
| deltablue                | 4.04 ms                                                         | 2.18 ms: 1.85x faster                                                 |
| go                       | 146 ms                                                          | 78.6 ms: 1.85x faster                                                 |
| deepcopy                 | 310 us                                                          | 171 us: 1.81x faster                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 46.9 ms: 1.73x faster                                                 |
| raytrace                 | 303 ms                                                          | 183 ms: 1.65x faster                                                  |
| deepcopy_memo            | 29.6 us                                                         | 18.5 us: 1.60x faster                                                 |
| json                     | 4.76 ms                                                         | 2.98 ms: 1.60x faster                                                 |
| generators               | 31.6 ms                                                         | 19.8 ms: 1.59x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 6.27 ms: 1.57x faster                                                 |
| float                    | 69.6 ms                                                         | 44.5 ms: 1.57x faster                                                 |
| richards_super           | 49.9 ms                                                         | 32.0 ms: 1.56x faster                                                 |
| scimark_lu               | 89.8 ms                                                         | 58.5 ms: 1.53x faster                                                 |
| json_loads               | 22.4 us                                                         | 14.7 us: 1.52x faster                                                 |
| comprehensions           | 17.7 us                                                         | 11.7 us: 1.52x faster                                                 |
| scimark_sor              | 115 ms                                                          | 76.7 ms: 1.50x faster                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.4 ms: 1.50x faster                                                 |
| pyflate                  | 422 ms                                                          | 284 ms: 1.49x faster                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.46x faster                                                 |
| hexiom                   | 6.13 ms                                                         | 4.24 ms: 1.45x faster                                                 |
| richards                 | 40.3 ms                                                         | 28.0 ms: 1.44x faster                                                 |
| pycparser                | 1.04 sec                                                        | 727 ms: 1.43x faster                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.61 us: 1.43x faster                                                 |
| django_template          | 36.0 ms                                                         | 25.4 ms: 1.42x faster                                                 |
| regex_compile            | 117 ms                                                          | 82.5 ms: 1.41x faster                                                 |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.41x faster                                                  |
| dulwich_log              | 58.5 ms                                                         | 41.9 ms: 1.40x faster                                                 |
| sympy_sum                | 122 ms                                                          | 89.1 ms: 1.37x faster                                                 |
| nqueens                  | 87.1 ms                                                         | 63.8 ms: 1.36x faster                                                 |
| mako                     | 9.10 ms                                                         | 6.68 ms: 1.36x faster                                                 |
| html5lib                 | 52.1 ms                                                         | 38.4 ms: 1.36x faster                                                 |
| genshi_xml               | 46.6 ms                                                         | 34.4 ms: 1.35x faster                                                 |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                 |
| xml_etree_parse          | 120 ms                                                          | 89.1 ms: 1.35x faster                                                 |
| sympy_str                | 229 ms                                                          | 171 ms: 1.34x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 60.1 ms: 1.34x faster                                                 |
| sympy_integrate          | 16.6 ms                                                         | 12.5 ms: 1.33x faster                                                 |
| sympy_expand             | 391 ms                                                          | 293 ms: 1.33x faster                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.03 sec: 1.33x faster                                                |
| tomli_loads              | 1.91 sec                                                        | 1.44 sec: 1.33x faster                                                |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                  |
| pprint_safe_repr         | 658 ms                                                          | 508 ms: 1.30x faster                                                  |
| coroutines               | 17.9 ms                                                         | 13.9 ms: 1.29x faster                                                 |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.62 ms: 1.24x faster                                                 |
| fannkuch                 | 317 ms                                                          | 258 ms: 1.23x faster                                                  |
| nbody                    | 79.1 ms                                                         | 64.3 ms: 1.23x faster                                                 |
| scimark_fft              | 216 ms                                                          | 177 ms: 1.22x faster                                                  |
| xml_etree_process        | 48.1 ms                                                         | 39.7 ms: 1.21x faster                                                 |
| docutils                 | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                |
| 2to3                     | 265 ms                                                          | 224 ms: 1.18x faster                                                  |
| logging_format           | 7.91 us                                                         | 6.81 us: 1.16x faster                                                 |
| logging_simple           | 7.29 us                                                         | 6.38 us: 1.14x faster                                                 |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.0 ms: 1.09x faster                                                 |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                 |
| meteor_contest           | 80.0 ms                                                         | 73.7 ms: 1.09x faster                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                 |
| async_generators         | 241 ms                                                          | 230 ms: 1.05x faster                                                  |
| telco                    | 4.83 ms                                                         | 4.66 ms: 1.04x faster                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                 |
| coverage                 | 46.6 ms                                                         | 51.2 ms: 1.10x slower                                                 |
| python_startup           | 22.9 ms                                                         | 26.2 ms: 1.14x slower                                                 |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                 |
| create_gc_cycles         | 694 us                                                          | 1.31 ms: 1.89x slower                                                 |
| logging_silent           | 97.9 ns                                                         | 328 ns: 3.35x slower                                                  |
| Geometric mean           | (ref)                                                           | 1.39x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.418x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown