# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.122x slower
- HPT reliability: 99.26%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 297 ms: 1.12x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.10 sec: 1.08x slower                                                           |
| html5lib       | 52.1 ms                                                         | 51.4 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 440 ms: 2.10x faster                                                             |
| async_tree_io           | 940 ms                                                          | 548 ms: 1.71x faster                                                             |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 297 ms: 1.57x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| float          | 69.6 ms                                                         | 76.7 ms: 1.10x slower                                                            |
| nbody          | 79.1 ms                                                         | 107 ms: 1.35x slower                                                             |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.73 ms: 1.04x slower                                                            |
| regex_compile  | 117 ms                                                          | 124 ms: 1.06x slower                                                             |
| regex_v8       | 15.8 ms                                                         | 17.0 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.41 ms: 1.17x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                             |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.08 sec: 1.09x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.4 us: 1.16x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.87 us: 1.20x slower                                                            |
| pickle               | 7.83 us                                                         | 9.61 us: 1.23x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.7 us: 1.25x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 90.6 ms: 1.28x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 364 us: 1.30x slower                                                             |
| xml_etree_process    | 48.1 ms                                                         | 65.7 ms: 1.37x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 278 us: 1.47x slower                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 90.9 ms: 1.48x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.5 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 24.3 ms: 1.16x slower                                                            |
| mako            | 9.10 ms                                                         | 13.0 ms: 1.43x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.40 sec: 12.13x faster                                                          |
| pidigits                 | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 155 us: 2.56x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 34.6 ms: 2.35x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 440 ms: 2.10x faster                                                             |
| async_tree_io            | 940 ms                                                          | 548 ms: 1.71x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 457 ms: 1.63x faster                                                             |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 297 ms: 1.57x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.17 sec: 1.56x faster                                                           |
| pylint                   | 384 ms                                                          | 248 ms: 1.55x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.86 us: 1.23x faster                                                            |
| json                     | 4.76 ms                                                         | 4.02 ms: 1.19x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.41 ms: 1.17x faster                                                            |
| deepcopy                 | 310 us                                                          | 267 us: 1.16x faster                                                             |
| chaos                    | 74.4 ms                                                         | 66.1 ms: 1.13x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 999 us: 1.12x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                            |
| go                       | 146 ms                                                          | 134 ms: 1.09x faster                                                             |
| pycparser                | 1.04 sec                                                        | 992 ms: 1.05x faster                                                             |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 79.8 ms: 1.02x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 51.4 ms: 1.01x faster                                                            |
| raytrace                 | 303 ms                                                          | 304 ms: 1.00x slower                                                             |
| sympy_str                | 229 ms                                                          | 234 ms: 1.02x slower                                                             |
| sympy_expand             | 391 ms                                                          | 403 ms: 1.03x slower                                                             |
| django_template          | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.78 us: 1.04x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.73 ms: 1.04x slower                                                            |
| regex_compile            | 117 ms                                                          | 124 ms: 1.06x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 17.0 ms: 1.08x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.10 sec: 1.08x slower                                                           |
| deltablue                | 4.04 ms                                                         | 4.37 ms: 1.08x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.08 sec: 1.09x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 94.9 ms: 1.09x slower                                                            |
| pyflate                  | 422 ms                                                          | 460 ms: 1.09x slower                                                             |
| float                    | 69.6 ms                                                         | 76.7 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| 2to3                     | 265 ms                                                          | 297 ms: 1.12x slower                                                             |
| comprehensions           | 17.7 us                                                         | 19.9 us: 1.12x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 33.6 us: 1.14x slower                                                            |
| generators               | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                            |
| scimark_sor              | 115 ms                                                          | 133 ms: 1.16x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 24.3 ms: 1.16x slower                                                            |
| unpickle                 | 9.82 us                                                         | 11.4 us: 1.16x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 92.9 ms: 1.16x slower                                                            |
| richards_super           | 49.9 ms                                                         | 58.5 ms: 1.17x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 73.8 ms: 1.19x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.5 ms: 1.20x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.87 us: 1.20x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.46 ms: 1.22x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.61 us: 1.23x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.7 us: 1.25x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.97 us: 1.26x slower                                                            |
| scimark_fft              | 216 ms                                                          | 276 ms: 1.28x slower                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 90.6 ms: 1.28x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.75 sec: 1.28x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.41 us: 1.29x slower                                                            |
| richards                 | 40.3 ms                                                         | 52.2 ms: 1.30x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.26 ms: 1.30x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 855 ms: 1.30x slower                                                             |
| pickle_pure_python       | 280 us                                                          | 364 us: 1.30x slower                                                             |
| fannkuch                 | 317 ms                                                          | 413 ms: 1.30x slower                                                             |
| scimark_lu               | 89.8 ms                                                         | 120 ms: 1.34x slower                                                             |
| nbody                    | 79.1 ms                                                         | 107 ms: 1.35x slower                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 4.39 ms: 1.36x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 65.7 ms: 1.37x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 111 ms: 1.38x slower                                                             |
| async_generators         | 241 ms                                                          | 341 ms: 1.42x slower                                                             |
| mako                     | 9.10 ms                                                         | 13.0 ms: 1.43x slower                                                            |
| coroutines               | 17.9 ms                                                         | 26.0 ms: 1.45x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 278 us: 1.47x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 90.9 ms: 1.48x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 104 ms: 1.57x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 83.8 ns: 2.09x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.47 ms: 2.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.95 ms: 2.30x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 502 ns: 5.13x slower                                                             |
| coverage                 | 46.6 ms                                                         | 471 ms: 10.12x slower                                                            |
| thrift                   | 902 us                                                          | 103 ms: 114.29x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.13x slower                                                                     |

Benchmark hidden because not significant (1): sympy_integrate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.122x slower

# HPT report

- Reliability score: 99.26% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown