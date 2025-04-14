# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                             |
| html5lib       | 88.9 ms                                                | 60.7 ms: 1.46x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.9 ms: 1.73x faster                                                            |
| float          | 117 ms                                                 | 69.5 ms: 1.69x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.44x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                            |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.60x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                            |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                            |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                            |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.35x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                             |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                             |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                             |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.90x faster                                                            |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                             |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                             |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                            |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                             |
| spectral_norm            | 170 ms                                                 | 97.8 ms: 1.74x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 73.7 ms: 1.73x faster                                                            |
| nbody                    | 154 ms                                                 | 88.9 ms: 1.73x faster                                                            |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                            |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                           |
| float                    | 117 ms                                                 | 69.5 ms: 1.69x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.63x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.60x faster                                                             |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                            |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.56x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                                            |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                            |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                            |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                             |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                             |
| html5lib                 | 88.9 ms                                                | 60.7 ms: 1.46x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                            |
| thrift                   | 1.07 ms                                                | 747 us: 1.43x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                           |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                            |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                             |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.30x faster                                                            |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                            |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                            |
| sympy_expand             | 566 ms                                                 | 464 ms: 1.22x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                           |
| async_generators         | 444 ms                                                 | 391 ms: 1.14x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                                            |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                            |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                            |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                             |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                            |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.38x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 82.4 ms: 3.43x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                     |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x