# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 215 ms: 1.23x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.4 ms: 1.39x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 381 ms: 2.47x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 200 ms: 2.34x faster                                                             |
| async_tree_none         | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.48x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| float          | 69.6 ms                                                         | 42.0 ms: 1.66x faster                                                            |
| nbody          | 79.1 ms                                                         | 63.9 ms: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.91x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.0 ms: 1.49x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.9 ms: 1.13x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.31 ms: 1.85x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 132 us: 1.43x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.33 sec: 1.43x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 85.3 ms: 1.41x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 213 us: 1.32x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.3 ms: 1.26x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.31 us: 1.18x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.4 ms: 1.14x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.80 us: 1.07x faster                                                            |
| pickle               | 7.83 us                                                         | 7.93 us: 1.01x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.1 ms: 1.50x faster                                                            |
| mako            | 9.10 ms                                                         | 6.66 ms: 1.37x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.4 ms: 1.36x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.37 sec: 12.41x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.92x faster                                                             |
| pidigits                 | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.3 ms: 2.77x faster                                                            |
| async_tree_io            | 940 ms                                                          | 381 ms: 2.47x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 200 ms: 2.34x faster                                                             |
| async_tree_none          | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| mdp                      | 1.83 sec                                                        | 793 ms: 2.30x faster                                                             |
| go                       | 146 ms                                                          | 74.2 ms: 1.96x faster                                                            |
| pylint                   | 384 ms                                                          | 197 ms: 1.95x faster                                                             |
| deepcopy                 | 310 us                                                          | 164 us: 1.89x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.14 ms: 1.88x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.1 ms: 1.86x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.31 ms: 1.85x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.7 us: 1.77x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 55.4 ns: 1.77x faster                                                            |
| thrift                   | 902 us                                                          | 511 us: 1.76x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 47.0 ms: 1.73x faster                                                            |
| raytrace                 | 303 ms                                                          | 176 ms: 1.72x faster                                                             |
| richards_super           | 49.9 ms                                                         | 29.6 ms: 1.69x faster                                                            |
| float                    | 69.6 ms                                                         | 42.0 ms: 1.66x faster                                                            |
| generators               | 31.6 ms                                                         | 19.2 ms: 1.65x faster                                                            |
| json                     | 4.76 ms                                                         | 2.92 ms: 1.63x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.9 us: 1.63x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| scimark_sor              | 115 ms                                                          | 74.2 ms: 1.55x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.1 ms: 1.54x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.00 ms: 1.53x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.7 ms: 1.53x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.6 ms: 1.53x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.76 us: 1.52x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 491 ms: 1.52x faster                                                             |
| pyflate                  | 422 ms                                                          | 280 ms: 1.51x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 38.9 ms: 1.50x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.1 ms: 1.50x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.0 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 699 ms: 1.49x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.0 ms: 1.44x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 132 us: 1.43x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.33 sec: 1.43x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 61.3 ms: 1.42x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 85.3 ms: 1.41x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 37.4 ms: 1.39x faster                                                            |
| sympy_expand             | 391 ms                                                          | 283 ms: 1.38x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 995 ms: 1.38x faster                                                             |
| sympy_str                | 229 ms                                                          | 167 ms: 1.37x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.66 ms: 1.37x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.2 ms: 1.36x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.4 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 490 ms: 1.34x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 213 us: 1.32x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 61.9 ms: 1.30x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.55 ms: 1.27x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.3 ms: 1.26x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.86 us: 1.24x faster                                                            |
| nbody                    | 79.1 ms                                                         | 63.9 ms: 1.24x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.40 us: 1.24x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.5 ms: 1.23x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.4 ns: 1.23x faster                                                            |
| fannkuch                 | 317 ms                                                          | 257 ms: 1.23x faster                                                             |
| 2to3                     | 265 ms                                                          | 215 ms: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| scimark_fft              | 216 ms                                                          | 179 ms: 1.21x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.31 us: 1.18x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.4 ms: 1.14x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.9 ms: 1.13x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.29 ms: 1.13x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.5 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.80 us: 1.07x faster                                                            |
| async_generators         | 241 ms                                                          | 227 ms: 1.06x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.93 us: 1.01x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.4 ms: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 90.9 ms: 1.37x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.10 ms: 1.64x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.27 ms: 1.83x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 8.12 ms: 7.25x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.42x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.425x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown