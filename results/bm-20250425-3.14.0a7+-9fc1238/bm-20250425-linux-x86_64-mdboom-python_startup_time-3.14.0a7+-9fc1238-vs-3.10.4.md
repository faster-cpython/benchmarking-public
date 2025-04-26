# Results vs. 3.10.4

- fork: mdboom
- ref: python_startup_time
- machine: linux-x86_64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                  |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                                 |
| nbody          | 154 ms                                                 | 98.7 ms: 1.56x faster                                                 |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.24x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.31 ms: 1.23x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                 |
| django_template | 48.2 ms                                                | 31.4 ms: 1.54x faster                                                 |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| generators               | 80.1 ms                                                | 29.4 ms: 2.73x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                                 |
| chaos                    | 115 ms                                                 | 57.1 ms: 2.02x faster                                                 |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                  |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                                 |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                                 |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                                  |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                                  |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.34 ms: 1.64x faster                                                 |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                  |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                |
| nbody                    | 154 ms                                                 | 98.7 ms: 1.56x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                 |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.0 ms: 1.43x faster                                                 |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.9 ms: 1.31x faster                                                 |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                  |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.30x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                  |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.24x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| async_generators         | 444 ms                                                 | 398 ms: 1.12x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                 |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                 |
| json                     | 5.69 ms                                                | 5.53 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                  |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.31 ms: 1.23x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.00 ms: 1.38x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x