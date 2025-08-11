# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.28x faster                                                             |
| async_tree_none         | 394 ms                                                          | 177 ms: 2.23x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.43x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 44.0 ms: 1.58x faster                                                            |
| nbody          | 79.1 ms                                                         | 65.8 ms: 1.20x faster                                                            |
| Geometric mean | (ref)                                                           | 1.88x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.3 ms: 1.43x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.48 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.1 us: 1.59x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 88.9 ms: 1.35x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.44 sec: 1.33x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 214 us: 1.31x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.52 us: 1.15x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.4 ms: 1.10x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 57.9 ms: 1.06x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 8.05 us: 1.03x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.46 us: 1.08x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.3 ms: 1.48x faster                                                            |
| mako            | 9.10 ms                                                         | 6.66 ms: 1.37x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.40 sec: 12.12x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.81x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 31.9 ms: 2.55x faster                                                            |
| async_tree_io            | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| mdp                      | 1.83 sec                                                        | 794 ms: 2.30x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.28x faster                                                             |
| async_tree_none          | 394 ms                                                          | 177 ms: 2.23x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.94x faster                                                             |
| go                       | 146 ms                                                          | 76.7 ms: 1.90x faster                                                            |
| deepcopy                 | 310 us                                                          | 168 us: 1.85x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.6 ms: 1.83x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.82x faster                                                            |
| thrift                   | 902 us                                                          | 502 us: 1.80x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 46.9 ms: 1.73x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.0 ns: 1.69x faster                                                            |
| generators               | 31.6 ms                                                         | 19.1 ms: 1.65x faster                                                            |
| raytrace                 | 303 ms                                                          | 184 ms: 1.64x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.2 us: 1.63x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.62x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.1 ms: 1.60x faster                                                            |
| json                     | 4.76 ms                                                         | 2.97 ms: 1.60x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.1 us: 1.59x faster                                                            |
| float                    | 69.6 ms                                                         | 44.0 ms: 1.58x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.3 ms: 1.51x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.11 ms: 1.49x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.80 us: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 702 ms: 1.48x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 39.4 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.3 ms: 1.48x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.2 ms: 1.48x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 506 ms: 1.47x faster                                                             |
| scimark_sor              | 115 ms                                                          | 78.9 ms: 1.46x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.4 ms: 1.46x faster                                                            |
| pyflate                  | 422 ms                                                          | 293 ms: 1.44x faster                                                             |
| regex_compile            | 117 ms                                                          | 81.3 ms: 1.43x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.61 us: 1.42x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.3 ms: 1.40x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 63.1 ms: 1.38x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.66 ms: 1.37x faster                                                            |
| sympy_expand             | 391 ms                                                          | 287 ms: 1.36x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 88.9 ms: 1.35x faster                                                            |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.02 sec: 1.34x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.44 sec: 1.33x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 497 ms: 1.32x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 848 us: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 214 us: 1.31x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 63.9 ms: 1.26x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.52 us: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| logging_simple           | 7.29 us                                                         | 6.03 us: 1.21x faster                                                            |
| fannkuch                 | 317 ms                                                          | 262 ms: 1.21x faster                                                             |
| nbody                    | 79.1 ms                                                         | 65.8 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.69 ms: 1.20x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| scimark_fft              | 216 ms                                                          | 187 ms: 1.16x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.52 us: 1.15x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.48 ms: 1.12x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 35.8 ns: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.6 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.4 ms: 1.10x faster                                                            |
| async_generators         | 241 ms                                                          | 224 ms: 1.08x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 57.9 ms: 1.06x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.72 ms: 1.02x faster                                                            |
| pickle                   | 7.83 us                                                         | 8.05 us: 1.03x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.6 ms: 1.06x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.46 us: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.5 ms: 1.42x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.15 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.31 ms: 1.88x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown