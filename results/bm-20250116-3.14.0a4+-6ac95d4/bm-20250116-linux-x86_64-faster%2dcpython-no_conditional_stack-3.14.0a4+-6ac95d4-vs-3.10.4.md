# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: 6ac95d4
- commit date: 2025-01-16
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.93x faster                                                             |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.67x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                                            |
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.17 ms: 1.15x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                            |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 228 us: 1.45x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                             |
| xml_etree_generate   | 99.4 ms                                                | 84.0 ms: 1.18x faster                                                            |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                            |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                            |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                            |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.93x faster                                                             |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                            |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.67x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                             |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                             |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                                             |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                                            |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                             |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                             |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                             |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                             |
| richards                 | 79.3 ms                                                | 44.5 ms: 1.78x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                            |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.35 ms: 1.64x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                            |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                            |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                            |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                             |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                            |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                             |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 228 us: 1.45x faster                                                             |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                            |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                            |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                            |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                             |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                           |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                             |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                                            |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                            |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                            |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 84.0 ms: 1.18x faster                                                            |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                            |
| async_generators         | 444 ms                                                 | 380 ms: 1.17x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.17 ms: 1.15x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 861 us: 1.15x faster                                                             |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                            |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                            |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                            |
| coverage                 | 79.4 ms                                                | 91.3 ms: 1.15x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.86 ms: 1.34x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-6ac95d4/bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.440x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x