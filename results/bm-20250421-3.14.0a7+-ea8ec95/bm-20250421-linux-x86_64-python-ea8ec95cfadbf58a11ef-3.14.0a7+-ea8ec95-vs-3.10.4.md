# Results vs. 3.10.4

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-x86_64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                   |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 614 ms: 2.88x faster                                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 483 ms: 2.11x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                  |
| nbody          | 154 ms                                                 | 96.1 ms: 1.60x faster                                                  |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.24x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                  |
| regex_dna      | 227 ms                                                 | 205 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                  |
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                  |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 614 ms: 2.88x faster                                                   |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| generators               | 80.1 ms                                                | 29.1 ms: 2.76x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.41 ms: 2.32x faster                                                  |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 483 ms: 2.11x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                  |
| chaos                    | 115 ms                                                 | 56.7 ms: 2.03x faster                                                  |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                   |
| logging_silent           | 190 ns                                                 | 97.2 ns: 1.95x faster                                                  |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                   |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.89x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| richards                 | 79.3 ms                                                | 43.7 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.79x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.5 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                                  |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                  |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                   |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| nbody                    | 154 ms                                                 | 96.1 ms: 1.60x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                   |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                  |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                                   |
| html5lib                 | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                                  |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                  |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                   |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                                  |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.27x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| async_generators         | 444 ms                                                 | 401 ms: 1.11x faster                                                   |
| regex_dna                | 227 ms                                                 | 205 ms: 1.11x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.07x faster                                                  |
| json                     | 5.69 ms                                                | 5.49 ms: 1.04x faster                                                  |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x