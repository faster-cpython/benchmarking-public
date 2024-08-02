# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.62 ms: 1.03x slower                                                          |
| docutils       | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                         |
| html5lib       | 52.1 ms                                                         | 50.5 ms: 1.03x faster                                                          |
| tornado_http   | 118 ms                                                          | 99.4 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 498 ms: 1.85x faster                                                           |
| async_tree_io           | 940 ms                                                          | 545 ms: 1.73x faster                                                           |
| async_tree_none         | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 284 ms: 1.64x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.72x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 56.6 ms: 1.23x faster                                                          |
| nbody          | 79.1 ms                                                         | 80.5 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.45x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 125 ms: 1.04x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 117 ms                                                          | 127 ms: 1.09x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.00 ms: 1.40x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 254 us: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 181 us: 1.05x faster                                                           |
| pickle               | 7.83 us                                                         | 8.10 us: 1.03x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.11 us: 1.04x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.59 us: 1.11x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.2 ms: 1.04x faster                                                          |
| python_startup_no_site | 18.1 ms                                                         | 18.7 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.84 ms: 1.16x faster                                                          |
| django_template | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.0 ms: 1.03x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.1 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 149 us: 2.66x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 498 ms: 1.85x faster                                                           |
| async_tree_io            | 940 ms                                                          | 545 ms: 1.73x faster                                                           |
| async_tree_none          | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 284 ms: 1.64x faster                                                           |
| pylint                   | 384 ms                                                          | 245 ms: 1.57x faster                                                           |
| raytrace                 | 303 ms                                                          | 214 ms: 1.42x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.00 ms: 1.40x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.3 ms: 1.37x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.3 ms: 1.37x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.96 ms: 1.36x faster                                                          |
| richards_super           | 49.9 ms                                                         | 37.3 ms: 1.34x faster                                                          |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                          |
| thrift                   | 902 us                                                          | 727 us: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 56.6 ms: 1.23x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.5 us: 1.23x faster                                                          |
| go                       | 146 ms                                                          | 119 ms: 1.22x faster                                                           |
| richards                 | 40.3 ms                                                         | 32.9 ms: 1.22x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 80.1 ns: 1.22x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                          |
| pycparser                | 1.04 sec                                                        | 878 ms: 1.19x faster                                                           |
| tornado_http             | 118 ms                                                          | 99.4 ms: 1.18x faster                                                          |
| scimark_sor              | 115 ms                                                          | 97.7 ms: 1.18x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 634 ms: 1.17x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.84 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                         |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.3 ms: 1.12x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 254 us: 1.10x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.1 ms: 1.10x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                          |
| pyflate                  | 422 ms                                                          | 385 ms: 1.10x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 83.0 ms: 1.08x faster                                                          |
| fannkuch                 | 317 ms                                                          | 294 ms: 1.08x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 181 us: 1.05x faster                                                           |
| regex_dna                | 131 ms                                                          | 125 ms: 1.04x faster                                                           |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.2 ms: 1.04x faster                                                          |
| 2to3                     | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 50.5 ms: 1.03x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 78.4 ms: 1.02x faster                                                          |
| scimark_fft              | 216 ms                                                          | 212 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 651 ms: 1.01x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 80.2 ms: 1.00x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.7 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.26 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                           |
| deepcopy                 | 310 us                                                          | 314 us: 1.01x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 6.23 ms: 1.01x slower                                                          |
| nbody                    | 79.1 ms                                                         | 80.5 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| chameleon                | 6.42 ms                                                         | 6.62 ms: 1.03x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.0 ms: 1.03x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.7 ms: 1.03x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.10 us: 1.03x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                         |
| deepcopy_memo            | 29.6 us                                                         | 30.7 us: 1.04x slower                                                          |
| sympy_str                | 229 ms                                                          | 239 ms: 1.04x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.11 us: 1.04x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.81 us: 1.05x slower                                                          |
| coverage                 | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.1 ms: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.34 us: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.71 us: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.0 ms: 1.06x slower                                                          |
| sympy_expand             | 391 ms                                                          | 421 ms: 1.08x slower                                                           |
| regex_compile            | 117 ms                                                          | 127 ms: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 72.1 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 757 us: 1.09x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.59 us: 1.11x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| async_generators         | 241 ms                                                          | 306 ms: 1.27x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.46 ms: 1.34x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (4): json, xml_etree_generate, asyncio_tcp_ssl, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown