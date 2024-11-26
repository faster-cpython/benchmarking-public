# Results vs. 3.10.4

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-x86
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.036x faster
- HPT reliability: 67.03%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 294 ms: 1.11x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| async_tree_io           | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.64x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                           |
| nbody          | 79.1 ms                                                         | 97.0 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| regex_compile  | 117 ms                                                          | 122 ms: 1.05x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.05x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 70.2 ms: 1.01x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 188 us: 1.01x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 302 us: 1.08x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 55.3 ms: 1.15x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.32 ms: 1.24x faster                                                           |
| django_template | 36.0 ms                                                         | 36.5 ms: 1.01x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 58.0 ms: 1.24x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 27.1 ms: 1.29x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 164 us: 2.41x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 116 ms: 1.99x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| async_tree_io            | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.64x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| pylint                   | 384 ms                                                          | 293 ms: 1.31x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.4 us: 1.26x faster                                                           |
| float                    | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.22 ms: 1.26x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 78.1 ns: 1.25x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 71.9 ms: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.32 ms: 1.24x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 67.5 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.18x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.9 ms: 1.16x faster                                                           |
| go                       | 146 ms                                                          | 127 ms: 1.15x faster                                                            |
| thrift                   | 902 us                                                          | 784 us: 1.15x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.1 ms: 1.14x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.17 ms: 1.13x faster                                                           |
| deepcopy                 | 310 us                                                          | 275 us: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                           |
| pycparser                | 1.04 sec                                                        | 933 ms: 1.12x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.08x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 49.4 ms: 1.05x faster                                                           |
| pyflate                  | 422 ms                                                          | 402 ms: 1.05x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.05x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.05x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.52 ms: 1.04x faster                                                           |
| richards_super           | 49.9 ms                                                         | 49.0 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 70.2 ms: 1.01x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 188 us: 1.01x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 62.5 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.27 ms: 1.01x slower                                                           |
| django_template          | 36.0 ms                                                         | 36.5 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.5 ms: 1.02x slower                                                           |
| sympy_sum                | 122 ms                                                          | 125 ms: 1.02x slower                                                            |
| mdp                      | 1.83 sec                                                        | 1.87 sec: 1.03x slower                                                          |
| spectral_norm            | 80.2 ms                                                         | 82.5 ms: 1.03x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.77 us: 1.03x slower                                                           |
| raytrace                 | 303 ms                                                          | 314 ms: 1.04x slower                                                            |
| regex_compile            | 117 ms                                                          | 122 ms: 1.05x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.8 us: 1.06x slower                                                           |
| fannkuch                 | 317 ms                                                          | 336 ms: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 302 us: 1.08x slower                                                            |
| richards                 | 40.3 ms                                                         | 43.6 ms: 1.08x slower                                                           |
| sympy_expand             | 391 ms                                                          | 425 ms: 1.09x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.49 sec: 1.09x slower                                                          |
| sympy_str                | 229 ms                                                          | 250 ms: 1.09x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| 2to3                     | 265 ms                                                          | 294 ms: 1.11x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 89.0 ms: 1.11x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 97.1 ms: 1.11x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 735 ms: 1.12x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.92 us: 1.13x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.26 us: 1.13x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 55.3 ms: 1.15x slower                                                           |
| generators               | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 19.6 ms: 1.18x slower                                                           |
| scimark_fft              | 216 ms                                                          | 255 ms: 1.18x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.28 ms: 1.19x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| nbody                    | 79.1 ms                                                         | 97.0 ms: 1.23x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 58.0 ms: 1.24x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 57.2 ms: 1.28x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 27.1 ms: 1.29x slower                                                           |
| async_generators         | 241 ms                                                          | 322 ms: 1.34x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.8 ms: 1.40x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.01 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.68x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 67.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown