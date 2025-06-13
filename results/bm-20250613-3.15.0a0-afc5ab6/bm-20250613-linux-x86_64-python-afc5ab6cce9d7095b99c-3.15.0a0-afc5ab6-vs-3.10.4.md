# Results vs. 3.10.4

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-x86_64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.03x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.6 ms: 1.59x faster                                                 |
| nbody          | 154 ms                                                 | 102 ms: 1.51x faster                                                  |
| pidigits       | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.24x faster                                                 |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.03x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                 |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                 |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                 |
| deepcopy                 | 479 us                                                 | 256 us: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                  |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                 |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.79x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 69.6 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 76.3 ms: 1.67x faster                                                 |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 73.6 ms: 1.59x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                 |
| nbody                    | 154 ms                                                 | 102 ms: 1.51x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                  |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.48x faster                                                 |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.07 us: 1.37x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                 |
| logging_format           | 9.09 us                                                | 6.72 us: 1.35x faster                                                 |
| coroutines               | 35.1 ms                                                | 26.1 ms: 1.34x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                 |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.65 sec: 1.28x faster                                                |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 805 ms: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.18 ms: 1.25x faster                                                 |
| scimark_fft              | 466 ms                                                 | 386 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                  |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                 |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                 |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| telco                    | 7.27 ms                                                | 8.08 ms: 1.11x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 476 ns: 2.51x slower                                                  |
| coverage                 | 79.4 ms                                                | 423 ms: 5.32x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 137.65x slower                                                |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x