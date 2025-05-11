# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.069x faster
- HPT reliability: 96.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 285 ms: 1.07x slower                                                           |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 469 ms: 2.01x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 258 ms: 1.81x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.90x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.47x faster                                                           |
| float          | 69.6 ms                                                         | 56.9 ms: 1.22x faster                                                          |
| nbody          | 79.1 ms                                                         | 119 ms: 1.51x slower                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 14.9 ms: 1.05x faster                                                          |
| regex_compile  | 117 ms                                                          | 111 ms: 1.05x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.73 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.36 ms: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.6 ms: 1.02x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.10 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_pure_python   | 280 us                                                          | 321 us: 1.14x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.4 us: 1.17x slower                                                          |
| pickle               | 7.83 us                                                         | 9.34 us: 1.19x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.85 us: 1.20x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 74.3 ms: 1.20x slower                                                          |
| unpickle_pure_python | 189 us                                                          | 241 us: 1.27x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.2 ms: 1.23x slower                                                          |
| python_startup         | 22.9 ms                                                         | 28.9 ms: 1.26x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.30 ms: 1.10x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 204 ms: 2.47x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 177 us: 2.23x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 37.2 ms: 2.19x faster                                                          |
| async_tree_io            | 940 ms                                                          | 469 ms: 2.01x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 258 ms: 1.81x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.07 sec: 1.71x faster                                                         |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.90 ms: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 56.2 ms: 1.32x faster                                                          |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.6 us: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 246 ms: 1.23x faster                                                           |
| float                    | 69.6 ms                                                         | 56.9 ms: 1.22x faster                                                          |
| deepcopy                 | 310 us                                                          | 254 us: 1.22x faster                                                           |
| thrift                   | 902 us                                                          | 741 us: 1.22x faster                                                           |
| pyflate                  | 422 ms                                                          | 353 ms: 1.20x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.36 ms: 1.18x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 78.7 ms: 1.14x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 51.7 ms: 1.13x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.0 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.11x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 677 ms: 1.10x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.30 ms: 1.10x faster                                                          |
| scimark_sor              | 115 ms                                                          | 105 ms: 1.10x faster                                                           |
| generators               | 31.6 ms                                                         | 28.8 ms: 1.09x faster                                                          |
| richards_super           | 49.9 ms                                                         | 46.0 ms: 1.08x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| pycparser                | 1.04 sec                                                        | 971 ms: 1.07x faster                                                           |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                           |
| json                     | 4.76 ms                                                         | 4.50 ms: 1.06x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 14.9 ms: 1.05x faster                                                          |
| regex_compile            | 117 ms                                                          | 111 ms: 1.05x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.86 ms: 1.05x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.03x faster                                                          |
| sympy_str                | 229 ms                                                          | 224 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.6 ms: 1.02x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 80.9 ms: 1.01x slower                                                          |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                         |
| coroutines               | 17.9 ms                                                         | 18.2 ms: 1.01x slower                                                          |
| sympy_expand             | 391 ms                                                          | 396 ms: 1.01x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.1 us: 1.02x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.03x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.73 ms: 1.04x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.10 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| nqueens                  | 87.1 ms                                                         | 91.7 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.44 ms: 1.06x slower                                                          |
| 2to3                     | 265 ms                                                          | 285 ms: 1.07x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                          |
| pickle_pure_python       | 280 us                                                          | 321 us: 1.14x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.4 us: 1.17x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 94.5 ms: 1.18x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.63 sec: 1.19x slower                                                         |
| pickle                   | 7.83 us                                                         | 9.34 us: 1.19x slower                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.34 ms: 1.20x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.85 us: 1.20x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 74.3 ms: 1.20x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 799 ms: 1.21x slower                                                           |
| coverage                 | 46.6 ms                                                         | 56.7 ms: 1.22x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.67 us: 1.22x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 22.2 ms: 1.23x slower                                                          |
| logging_simple           | 7.29 us                                                         | 9.00 us: 1.24x slower                                                          |
| scimark_fft              | 216 ms                                                          | 268 ms: 1.24x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.9 ms: 1.26x slower                                                          |
| fannkuch                 | 317 ms                                                          | 400 ms: 1.26x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 241 us: 1.27x slower                                                           |
| async_generators         | 241 ms                                                          | 324 ms: 1.34x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 57.0 ns: 1.42x slower                                                          |
| telco                    | 4.83 ms                                                         | 7.28 ms: 1.51x slower                                                          |
| nbody                    | 79.1 ms                                                         | 119 ms: 1.51x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.94 ms: 1.51x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 104 ms: 1.57x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.13 ms: 1.63x slower                                                          |
| logging_silent           | 97.9 ns                                                         | 375 ns: 3.83x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): richards, crypto_pyaes, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 96.63% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown