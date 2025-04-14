# Results vs. 3.10.4

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.468x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                              |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                            |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                             |
| Geometric mean | (ref)                                                  | 1.37x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                              |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.79x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 476 ms: 2.14x faster                                              |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.1 ms: 1.74x faster                                             |
| nbody          | 154 ms                                                 | 95.2 ms: 1.61x faster                                             |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.42x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                              |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                             |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.21x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                            |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                              |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 83.4 ms: 1.19x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                             |
| json_loads           | 31.2 us                                                | 29.2 us: 1.07x faster                                             |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                             |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                             |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.53x faster                                             |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                             |
| genshi_xml      | 66.0 ms                                                | 48.1 ms: 1.37x faster                                             |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                              |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                              |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.79x faster                                              |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                             |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.37x faster                                            |
| deltablue                | 7.91 ms                                                | 3.39 ms: 2.34x faster                                             |
| go                       | 240 ms                                                 | 110 ms: 2.17x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 476 ms: 2.14x faster                                              |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                             |
| logging_silent           | 190 ns                                                 | 94.8 ns: 2.00x faster                                             |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                              |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                              |
| deepcopy                 | 479 us                                                 | 249 us: 1.93x faster                                              |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.90x faster                                             |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                              |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.83x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                             |
| float                    | 117 ms                                                 | 67.1 ms: 1.74x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                             |
| spectral_norm            | 170 ms                                                 | 98.1 ms: 1.73x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                            |
| nbody                    | 154 ms                                                 | 95.2 ms: 1.61x faster                                             |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                             |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                              |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                             |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.53x faster                                             |
| logging_simple           | 8.30 us                                                | 5.44 us: 1.53x faster                                             |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                             |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                              |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                              |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                             |
| coroutines               | 35.1 ms                                                | 24.1 ms: 1.45x faster                                             |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                             |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.39x faster                                             |
| genshi_xml               | 66.0 ms                                                | 48.1 ms: 1.37x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                             |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                            |
| scimark_fft              | 466 ms                                                 | 345 ms: 1.35x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                              |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                              |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                             |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                              |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                            |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 83.4 ms: 1.19x faster                                             |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                             |
| async_generators         | 444 ms                                                 | 393 ms: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                             |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                             |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                             |
| json_loads               | 31.2 us                                                | 29.2 us: 1.07x faster                                             |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                              |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                             |
| coverage                 | 79.4 ms                                                | 87.0 ms: 1.10x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                             |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                             |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                      |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.468x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.28x