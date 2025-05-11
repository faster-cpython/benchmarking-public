# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 268 ms: 1.01x slower                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 447 ms: 2.11x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 450 ms: 2.05x faster                                                           |
| async_tree_none         | 394 ms                                                          | 202 ms: 1.94x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 247 ms: 1.89x faster                                                           |
| Geometric mean          | (ref)                                                           | 2.00x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 205 ms: 2.45x faster                                                           |
| float          | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                          |
| nbody          | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.43 ms: 1.16x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 176 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.06x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 272 us: 1.03x faster                                                           |
| json_loads           | 22.4 us                                                         | 22.0 us: 1.02x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| unpickle             | 9.82 us                                                         | 11.0 us: 1.12x slower                                                          |
| pickle               | 7.83 us                                                         | 9.13 us: 1.17x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.80 us: 1.18x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.6 us: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.2 ms: 1.23x slower                                                          |
| python_startup         | 22.9 ms                                                         | 29.3 ms: 1.28x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.14 ms: 1.12x faster                                                          |
| django_template | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.7 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 154 us: 2.58x faster                                                           |
| pidigits                 | 502 ms                                                          | 205 ms: 2.45x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 37.6 ms: 2.16x faster                                                          |
| async_tree_io            | 940 ms                                                          | 447 ms: 2.11x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 450 ms: 2.05x faster                                                           |
| async_tree_none          | 394 ms                                                          | 202 ms: 1.94x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 247 ms: 1.89x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.02 sec: 1.79x faster                                                         |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.6 us: 1.44x faster                                                          |
| go                       | 146 ms                                                          | 103 ms: 1.41x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.6 ms: 1.36x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 62.7 ms: 1.30x faster                                                          |
| float                    | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                          |
| deepcopy                 | 310 us                                                          | 243 us: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.1 ms: 1.24x faster                                                          |
| raytrace                 | 303 ms                                                          | 246 ms: 1.23x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.04 ms: 1.22x faster                                                          |
| pyflate                  | 422 ms                                                          | 347 ms: 1.22x faster                                                           |
| scimark_sor              | 115 ms                                                          | 94.7 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 750 us: 1.20x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.8 us: 1.20x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.6 ms: 1.20x faster                                                          |
| richards_super           | 49.9 ms                                                         | 41.7 ms: 1.20x faster                                                          |
| generators               | 31.6 ms                                                         | 26.5 ms: 1.19x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 8.43 ms: 1.16x faster                                                          |
| pycparser                | 1.04 sec                                                        | 906 ms: 1.15x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 2.00 us: 1.15x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 51.4 ms: 1.14x faster                                                          |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.14 ms: 1.12x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.0 ms: 1.11x faster                                                          |
| richards                 | 40.3 ms                                                         | 36.4 ms: 1.11x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 676 ms: 1.10x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                         |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.09x faster                                                          |
| regex_v8                 | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 176 us: 1.08x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                          |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                          |
| json                     | 4.76 ms                                                         | 4.51 ms: 1.06x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 83.8 ms: 1.04x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 77.4 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 272 us: 1.03x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| json_loads               | 22.4 us                                                         | 22.0 us: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 384 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 650 ms: 1.01x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                          |
| 2to3                     | 265 ms                                                          | 268 ms: 1.01x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.31 ms: 1.02x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                                         |
| fannkuch                 | 317 ms                                                          | 327 ms: 1.03x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 41.7 ns: 1.04x slower                                                          |
| scimark_fft              | 216 ms                                                          | 234 ms: 1.08x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| unpickle                 | 9.82 us                                                         | 11.0 us: 1.12x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.7 ms: 1.15x slower                                                          |
| pickle                   | 7.83 us                                                         | 9.13 us: 1.17x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.80 us: 1.18x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.6 us: 1.18x slower                                                          |
| nbody                    | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.33 ms: 1.18x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 22.2 ms: 1.23x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.76 us: 1.23x slower                                                          |
| async_generators         | 241 ms                                                          | 299 ms: 1.24x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.03 us: 1.24x slower                                                          |
| coverage                 | 46.6 ms                                                         | 58.8 ms: 1.26x slower                                                          |
| python_startup           | 22.9 ms                                                         | 29.3 ms: 1.28x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.70 ms: 1.39x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.91 ms: 1.49x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 104 ms: 1.57x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.14 ms: 1.64x slower                                                          |
| logging_silent           | 97.9 ns                                                         | 345 ns: 3.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown