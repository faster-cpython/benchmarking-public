# Results vs. 3.10.4

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-x86_64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                        |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                          |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.77x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                         |
| nbody          | 154 ms                                                 | 97.1 ms: 1.58x faster                                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                         |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                                         |
| json_loads           | 31.2 us                                                | 30.5 us: 1.02x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                         |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                         |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                          |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.77x faster                                                          |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                        |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.03x faster                                                         |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                         |
| logging_silent           | 190 ns                                                 | 95.5 ns: 1.99x faster                                                         |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                          |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.95x faster                                                         |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                          |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                          |
| richards                 | 79.3 ms                                                | 42.4 ms: 1.87x faster                                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.05 ms: 1.72x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.70x faster                                                         |
| pyflate                  | 716 ms                                                 | 425 ms: 1.69x faster                                                          |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                         |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.58x faster                                                          |
| nbody                    | 154 ms                                                 | 97.1 ms: 1.58x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                          |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                          |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                         |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                         |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                         |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                         |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                          |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                          |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                         |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                          |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.10 ms: 1.27x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                        |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                         |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                          |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                         |
| json                     | 5.69 ms                                                | 5.54 ms: 1.03x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| json_loads               | 31.2 us                                                | 30.5 us: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                         |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x