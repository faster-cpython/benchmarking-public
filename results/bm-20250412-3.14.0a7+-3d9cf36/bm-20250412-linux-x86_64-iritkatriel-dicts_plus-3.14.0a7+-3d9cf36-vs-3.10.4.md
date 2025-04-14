# Results vs. 3.10.4

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.474x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.40x faster                                              |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                            |
| html5lib       | 88.9 ms                                                | 60.4 ms: 1.47x faster                                             |
| Geometric mean | (ref)                                                  | 1.38x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.90x faster                                              |
| async_tree_none         | 728 ms                                                 | 254 ms: 2.86x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.81x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 476 ms: 2.13x faster                                              |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.1 ms: 1.72x faster                                             |
| nbody          | 154 ms                                                 | 90.0 ms: 1.71x faster                                             |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.44x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                              |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.16 ms: 1.15x faster                                             |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.55x faster                                              |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.20x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                             |
| json_loads           | 31.2 us                                                | 29.3 us: 1.07x faster                                             |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                             |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.1 ms: 1.55x faster                                             |
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                             |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                             |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.35x faster                                             |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                              |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.90x faster                                              |
| async_tree_none          | 728 ms                                                 | 254 ms: 2.86x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.81x faster                                              |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                             |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.38x faster                                            |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                             |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 476 ms: 2.13x faster                                              |
| chaos                    | 115 ms                                                 | 55.9 ms: 2.07x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                             |
| logging_silent           | 190 ns                                                 | 95.0 ns: 2.00x faster                                             |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                              |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                              |
| deepcopy                 | 479 us                                                 | 248 us: 1.94x faster                                              |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.93x faster                                             |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                              |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                             |
| float                    | 117 ms                                                 | 68.1 ms: 1.72x faster                                             |
| nbody                    | 154 ms                                                 | 90.0 ms: 1.71x faster                                             |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.58 us: 1.62x faster                                             |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                              |
| django_template          | 48.2 ms                                                | 31.1 ms: 1.55x faster                                             |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.55x faster                                              |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                              |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                              |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                              |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                             |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                             |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                             |
| html5lib                 | 88.9 ms                                                | 60.4 ms: 1.47x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                            |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.42x faster                                             |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                            |
| 2to3                     | 348 ms                                                 | 250 ms: 1.40x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.73 ms: 1.37x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                             |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.35x faster                                             |
| scimark_fft              | 466 ms                                                 | 345 ms: 1.35x faster                                              |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                              |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                             |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                              |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                              |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                            |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.20x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.16 ms: 1.15x faster                                             |
| async_generators         | 444 ms                                                 | 390 ms: 1.14x faster                                              |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                              |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                             |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                              |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                             |
| json_loads               | 31.2 us                                                | 29.3 us: 1.07x faster                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                             |
| coverage                 | 79.4 ms                                                | 87.6 ms: 1.10x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.72 ms: 1.30x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                             |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                             |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                      |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.474x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.28x