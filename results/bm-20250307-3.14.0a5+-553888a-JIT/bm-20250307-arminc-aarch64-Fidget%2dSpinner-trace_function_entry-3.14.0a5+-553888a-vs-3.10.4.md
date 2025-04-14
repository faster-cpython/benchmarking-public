# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                                               |
| html5lib       | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 887 ms: 2.58x faster                                                               |
| async_tree_none         | 950 ms                                                                | 379 ms: 2.51x faster                                                               |
| async_tree_memoization  | 1.13 sec                                                              | 478 ms: 2.37x faster                                                               |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 662 ms: 1.92x faster                                                               |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.8 ms: 1.63x faster                                                              |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                               |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                               |
| regex_effbot   | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 29.8 ms: 1.08x faster                                                              |
| regex_dna      | 257 ms                                                                | 242 ms: 1.06x faster                                                               |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                             |
| unpickle_pure_python | 366 us                                                                | 276 us: 1.33x faster                                                               |
| xml_etree_process    | 99.5 ms                                                               | 75.7 ms: 1.31x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 407 us: 1.30x faster                                                               |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                              |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                               |
| xml_etree_generate   | 123 ms                                                                | 106 ms: 1.16x faster                                                               |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                               |
| json_loads           | 30.9 us                                                               | 34.3 us: 1.11x slower                                                              |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                              |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                              |
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                              |
| genshi_text     | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                              |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                              |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.13x faster                                                               |
| async_tree_io            | 2.28 sec                                                              | 887 ms: 2.58x faster                                                               |
| async_tree_none          | 950 ms                                                                | 379 ms: 2.51x faster                                                               |
| async_tree_memoization   | 1.13 sec                                                              | 478 ms: 2.37x faster                                                               |
| deltablue                | 8.94 ms                                                               | 4.03 ms: 2.22x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 662 ms: 1.92x faster                                                               |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                               |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                              |
| raytrace                 | 573 ms                                                                | 310 ms: 1.85x faster                                                               |
| richards_super           | 107 ms                                                                | 58.4 ms: 1.84x faster                                                              |
| chaos                    | 121 ms                                                                | 67.0 ms: 1.81x faster                                                              |
| richards                 | 91.7 ms                                                               | 52.0 ms: 1.76x faster                                                              |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                               |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                              |
| spectral_norm            | 186 ms                                                                | 113 ms: 1.65x faster                                                               |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                               |
| float                    | 135 ms                                                                | 82.8 ms: 1.63x faster                                                              |
| deepcopy                 | 511 us                                                                | 320 us: 1.60x faster                                                               |
| scimark_lu               | 227 ms                                                                | 144 ms: 1.58x faster                                                               |
| sqlglot_parse            | 2.40 ms                                                               | 1.54 ms: 1.56x faster                                                              |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                               |
| scimark_monte_carlo      | 128 ms                                                                | 84.2 ms: 1.52x faster                                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 1.88 ms: 1.52x faster                                                              |
| hexiom                   | 10.9 ms                                                               | 7.24 ms: 1.51x faster                                                              |
| pyflate                  | 795 ms                                                                | 553 ms: 1.44x faster                                                               |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                              |
| logging_simple           | 9.78 us                                                               | 6.88 us: 1.42x faster                                                              |
| logging_format           | 10.6 us                                                               | 7.53 us: 1.41x faster                                                              |
| comprehensions           | 33.1 us                                                               | 23.6 us: 1.40x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                              |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                               |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                              |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.38 us: 1.36x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                               |
| thrift                   | 1.26 ms                                                               | 940 us: 1.34x faster                                                               |
| unpickle_pure_python     | 366 us                                                                | 276 us: 1.33x faster                                                               |
| genshi_text              | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.32x faster                                                               |
| xml_etree_process        | 99.5 ms                                                               | 75.7 ms: 1.31x faster                                                              |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 407 us: 1.30x faster                                                               |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                              |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                                               |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                               |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.24x faster                                                             |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                              |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                               |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.9 ms: 1.22x faster                                                              |
| scimark_fft              | 500 ms                                                                | 415 ms: 1.21x faster                                                               |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                               |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 106 ms: 1.16x faster                                                               |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                              |
| sympy_expand             | 543 ms                                                                | 470 ms: 1.15x faster                                                               |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.69 ms: 1.14x faster                                                              |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                             |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                                               |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 67.6 ms: 1.09x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                               |
| regex_effbot             | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 29.8 ms: 1.08x faster                                                              |
| regex_dna                | 257 ms                                                                | 242 ms: 1.06x faster                                                               |
| async_generators         | 452 ms                                                                | 427 ms: 1.06x faster                                                               |
| meteor_contest           | 126 ms                                                                | 121 ms: 1.05x faster                                                               |
| fannkuch                 | 546 ms                                                                | 529 ms: 1.03x faster                                                               |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                                              |
| json_loads               | 30.9 us                                                               | 34.3 us: 1.11x slower                                                              |
| telco                    | 8.49 ms                                                               | 9.52 ms: 1.12x slower                                                              |
| coverage                 | 83.6 ms                                                               | 99.6 ms: 1.19x slower                                                              |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                              |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                              |
| create_gc_cycles         | 2.26 ms                                                               | 3.51 ms: 1.55x slower                                                              |
| gc_traversal             | 4.15 ms                                                               | 6.67 ms: 1.60x slower                                                              |
| bench_mp_pool            | 14.5 ms                                                               | 548 ms: 37.73x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.325x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.33x