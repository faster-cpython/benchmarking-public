# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.225x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 336 ms: 1.27x slower                                                             |
| docutils       | 1.95 sec                                                        | 4.15 sec: 2.13x slower                                                           |
| html5lib       | 52.1 ms                                                         | 63.9 ms: 1.23x slower                                                            |
| Geometric mean | (ref)                                                           | 1.49x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                             |
| async_tree_io           | 940 ms                                                          | 577 ms: 1.63x faster                                                             |
| async_tree_none         | 394 ms                                                          | 274 ms: 1.43x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 334 ms: 1.40x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.58x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 141 ms: 3.56x faster                                                             |
| float          | 69.6 ms                                                         | 97.9 ms: 1.41x slower                                                            |
| nbody          | 79.1 ms                                                         | 177 ms: 2.23x slower                                                             |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                            |
| regex_compile  | 117 ms                                                          | 160 ms: 1.37x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 9.48 ms: 1.04x faster                                                            |
| json_loads           | 22.4 us                                                         | 22.7 us: 1.01x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.44 us: 1.15x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.78 us: 1.17x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| unpickle             | 9.82 us                                                         | 12.2 us: 1.24x slower                                                            |
| pickle               | 7.83 us                                                         | 9.74 us: 1.24x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 93.0 ms: 1.31x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 448 us: 1.60x slower                                                             |
| xml_etree_process    | 48.1 ms                                                         | 79.0 ms: 1.64x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| unpickle_pure_python | 189 us                                                          | 358 us: 1.89x slower                                                             |
| tomli_loads          | 1.91 sec                                                        | 5.01 sec: 2.62x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.35x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                            |
| python_startup         | 22.9 ms                                                         | 28.0 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 45.4 ms: 1.26x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 66.0 ms: 1.42x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 33.2 ms: 1.58x slower                                                            |
| mako            | 9.10 ms                                                         | 16.5 ms: 1.81x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.50x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.65 sec: 6.41x faster                                                           |
| pidigits                 | 502 ms                                                          | 141 ms: 3.56x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 36.0 ms: 2.25x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 198 us: 2.00x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                             |
| async_tree_io            | 940 ms                                                          | 577 ms: 1.63x faster                                                             |
| async_tree_none          | 394 ms                                                          | 274 ms: 1.43x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 334 ms: 1.40x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.67 us: 1.37x faster                                                            |
| pylint                   | 384 ms                                                          | 280 ms: 1.37x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 613 ms: 1.21x faster                                                             |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| json                     | 4.76 ms                                                         | 4.20 ms: 1.13x faster                                                            |
| thrift                   | 902 us                                                          | 837 us: 1.08x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 9.48 ms: 1.04x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 56.8 ms: 1.03x faster                                                            |
| json_loads               | 22.4 us                                                         | 22.7 us: 1.01x slower                                                            |
| deepcopy                 | 310 us                                                          | 332 us: 1.07x slower                                                             |
| regex_v8                 | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.22 ms: 1.09x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.44 us: 1.15x slower                                                            |
| sympy_sum                | 122 ms                                                          | 144 ms: 1.17x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.78 us: 1.17x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| python_startup           | 22.9 ms                                                         | 28.0 ms: 1.22x slower                                                            |
| mdp                      | 1.83 sec                                                        | 2.24 sec: 1.22x slower                                                           |
| html5lib                 | 52.1 ms                                                         | 63.9 ms: 1.23x slower                                                            |
| unpickle                 | 9.82 us                                                         | 12.2 us: 1.24x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.74 us: 1.24x slower                                                            |
| sympy_expand             | 391 ms                                                          | 490 ms: 1.25x slower                                                             |
| django_template          | 36.0 ms                                                         | 45.4 ms: 1.26x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 21.0 ms: 1.26x slower                                                            |
| 2to3                     | 265 ms                                                          | 336 ms: 1.27x slower                                                             |
| sympy_str                | 229 ms                                                          | 292 ms: 1.28x slower                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 3.44 us: 1.28x slower                                                            |
| chaos                    | 74.4 ms                                                         | 95.7 ms: 1.29x slower                                                            |
| go                       | 146 ms                                                          | 190 ms: 1.31x slower                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 93.0 ms: 1.31x slower                                                            |
| generators               | 31.6 ms                                                         | 41.5 ms: 1.32x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.5 ms: 1.35x slower                                                            |
| raytrace                 | 303 ms                                                          | 408 ms: 1.35x slower                                                             |
| regex_compile            | 117 ms                                                          | 160 ms: 1.37x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.38x slower                                                            |
| float                    | 69.6 ms                                                         | 97.9 ms: 1.41x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 66.0 ms: 1.42x slower                                                            |
| comprehensions           | 17.7 us                                                         | 25.6 us: 1.44x slower                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 118 ms: 1.45x slower                                                             |
| nqueens                  | 87.1 ms                                                         | 126 ms: 1.45x slower                                                             |
| deepcopy_memo            | 29.6 us                                                         | 43.3 us: 1.46x slower                                                            |
| deltablue                | 4.04 ms                                                         | 5.92 ms: 1.47x slower                                                            |
| pyflate                  | 422 ms                                                          | 619 ms: 1.47x slower                                                             |
| logging_format           | 7.91 us                                                         | 11.7 us: 1.47x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 120 ms: 1.50x slower                                                             |
| logging_simple           | 7.29 us                                                         | 11.0 us: 1.51x slower                                                            |
| richards_super           | 49.9 ms                                                         | 78.5 ms: 1.57x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 33.2 ms: 1.58x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 448 us: 1.60x slower                                                             |
| pycparser                | 1.04 sec                                                        | 1.68 sec: 1.61x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.13 ms: 1.62x slower                                                            |
| scimark_sor              | 115 ms                                                          | 187 ms: 1.63x slower                                                             |
| telco                    | 4.83 ms                                                         | 7.92 ms: 1.64x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 79.0 ms: 1.64x slower                                                            |
| async_generators         | 241 ms                                                          | 410 ms: 1.70x slower                                                             |
| richards                 | 40.3 ms                                                         | 69.4 ms: 1.72x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 10.6 ms: 1.73x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 107 ms: 1.73x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| coverage                 | 46.6 ms                                                         | 83.7 ms: 1.80x slower                                                            |
| mako                     | 9.10 ms                                                         | 16.5 ms: 1.81x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 163 ms: 1.82x slower                                                             |
| fannkuch                 | 317 ms                                                          | 580 ms: 1.83x slower                                                             |
| coroutines               | 17.9 ms                                                         | 32.8 ms: 1.83x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 358 us: 1.89x slower                                                             |
| scimark_fft              | 216 ms                                                          | 411 ms: 1.90x slower                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 6.37 ms: 1.97x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 80.4 ns: 2.01x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 166 ms: 2.07x slower                                                             |
| docutils                 | 1.95 sec                                                        | 4.15 sec: 2.13x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 1.43 sec: 2.17x slower                                                           |
| nbody                    | 79.1 ms                                                         | 177 ms: 2.23x slower                                                             |
| tomli_loads              | 1.91 sec                                                        | 5.01 sec: 2.62x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 4.07 sec: 2.97x slower                                                           |
| logging_silent           | 97.9 ns                                                         | 589 ns: 6.02x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.28x slower                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.225x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: unknown