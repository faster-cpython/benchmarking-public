# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.013x faster
- HPT reliability: 58.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 276 ms: 1.04x slower                                                           |
| docutils       | 1.95 sec                                                        | 3.19 sec: 1.64x slower                                                         |
| html5lib       | 52.1 ms                                                         | 52.8 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.20x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 428 ms: 2.20x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| async_tree_none         | 394 ms                                                          | 207 ms: 1.90x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 254 ms: 1.84x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.96x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 190 ms: 2.64x faster                                                           |
| float          | 69.6 ms                                                         | 59.3 ms: 1.17x faster                                                          |
| nbody          | 79.1 ms                                                         | 114 ms: 1.44x slower                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                          |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                          |
| regex_compile  | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.42 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 206 us: 1.09x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 318 us: 1.13x slower                                                           |
| json_loads           | 22.4 us                                                         | 25.7 us: 1.15x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.50 us: 1.17x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 56.5 ms: 1.17x slower                                                          |
| pickle_list          | 3.22 us                                                         | 4.00 us: 1.24x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 77.9 ms: 1.26x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 24.4 us: 1.34x slower                                                          |
| unpickle             | 9.82 us                                                         | 13.2 us: 1.34x slower                                                          |
| pickle               | 7.83 us                                                         | 10.5 us: 1.35x slower                                                          |
| tomli_loads          | 1.91 sec                                                        | 3.32 sec: 1.74x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.9 ms: 1.22x slower                                                          |
| python_startup         | 22.9 ms                                                         | 29.4 ms: 1.28x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 38.2 ms: 1.06x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 59.9 ms: 1.29x slower                                                          |
| mako            | 9.10 ms                                                         | 12.0 ms: 1.32x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 28.7 ms: 1.37x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.25x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 190 ms: 2.64x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 177 us: 2.23x faster                                                           |
| async_tree_io            | 940 ms                                                          | 428 ms: 2.20x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 37.4 ms: 2.17x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| async_tree_none          | 394 ms                                                          | 207 ms: 1.90x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 254 ms: 1.84x faster                                                           |
| pylint                   | 384 ms                                                          | 254 ms: 1.51x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.68 us: 1.36x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.98 ms: 1.36x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 604 ms: 1.23x faster                                                           |
| chaos                    | 74.4 ms                                                         | 60.6 ms: 1.23x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.51 sec: 1.21x faster                                                         |
| go                       | 146 ms                                                          | 122 ms: 1.20x faster                                                           |
| float                    | 69.6 ms                                                         | 59.3 ms: 1.17x faster                                                          |
| regex_v8                 | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 25.7 us: 1.15x faster                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.12 ms: 1.14x faster                                                          |
| deepcopy                 | 310 us                                                          | 273 us: 1.14x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.1 ms: 1.11x faster                                                          |
| generators               | 31.6 ms                                                         | 28.5 ms: 1.11x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 74.1 ms: 1.10x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 53.5 ms: 1.09x faster                                                          |
| thrift                   | 902 us                                                          | 827 us: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                           |
| raytrace                 | 303 ms                                                          | 281 ms: 1.08x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 83.5 ms: 1.08x faster                                                          |
| comprehensions           | 17.7 us                                                         | 17.0 us: 1.04x faster                                                          |
| scimark_sor              | 115 ms                                                          | 110 ms: 1.04x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.42 ms: 1.04x faster                                                          |
| pyflate                  | 422 ms                                                          | 407 ms: 1.04x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 6.01 ms: 1.02x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 60.8 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 52.8 ms: 1.01x slower                                                          |
| richards_super           | 49.9 ms                                                         | 50.9 ms: 1.02x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                          |
| 2to3                     | 265 ms                                                          | 276 ms: 1.04x slower                                                           |
| spectral_norm            | 80.2 ms                                                         | 83.8 ms: 1.04x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                          |
| regex_compile            | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| django_template          | 36.0 ms                                                         | 38.2 ms: 1.06x slower                                                          |
| sympy_str                | 229 ms                                                          | 244 ms: 1.07x slower                                                           |
| sympy_expand             | 391 ms                                                          | 423 ms: 1.08x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 206 us: 1.09x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 95.4 ms: 1.10x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.95 us: 1.10x slower                                                          |
| richards                 | 40.3 ms                                                         | 44.7 ms: 1.11x slower                                                          |
| pycparser                | 1.04 sec                                                        | 1.16 sec: 1.11x slower                                                         |
| pickle_pure_python       | 280 us                                                          | 318 us: 1.13x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.28 ms: 1.15x slower                                                          |
| json_loads               | 22.4 us                                                         | 25.7 us: 1.15x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.79 ms: 1.17x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.50 us: 1.17x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 56.5 ms: 1.17x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 96.4 ms: 1.20x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 794 ms: 1.21x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 21.9 ms: 1.22x slower                                                          |
| fannkuch                 | 317 ms                                                          | 387 ms: 1.22x slower                                                           |
| scimark_fft              | 216 ms                                                          | 269 ms: 1.24x slower                                                           |
| pickle_list              | 3.22 us                                                         | 4.00 us: 1.24x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 77.9 ms: 1.26x slower                                                          |
| python_startup           | 22.9 ms                                                         | 29.4 ms: 1.28x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 59.9 ms: 1.29x slower                                                          |
| logging_format           | 7.91 us                                                         | 10.2 us: 1.29x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 86.6 ms: 1.30x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 52.4 ns: 1.31x slower                                                          |
| logging_simple           | 7.29 us                                                         | 9.58 us: 1.31x slower                                                          |
| mako                     | 9.10 ms                                                         | 12.0 ms: 1.32x slower                                                          |
| async_generators         | 241 ms                                                          | 321 ms: 1.33x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 24.4 us: 1.34x slower                                                          |
| unpickle                 | 9.82 us                                                         | 13.2 us: 1.34x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 22.9 sec: 1.35x slower                                                         |
| pickle                   | 7.83 us                                                         | 10.5 us: 1.35x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 28.7 ms: 1.37x slower                                                          |
| nbody                    | 79.1 ms                                                         | 114 ms: 1.44x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.13 ms: 1.48x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.09 ms: 1.57x slower                                                          |
| docutils                 | 1.95 sec                                                        | 3.19 sec: 1.64x slower                                                         |
| coverage                 | 46.6 ms                                                         | 76.7 ms: 1.65x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 2.30 sec: 1.68x slower                                                         |
| tomli_loads              | 1.91 sec                                                        | 3.32 sec: 1.74x slower                                                         |
| logging_silent           | 97.9 ns                                                         | 425 ns: 4.34x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): sympy_sum, json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 58.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown