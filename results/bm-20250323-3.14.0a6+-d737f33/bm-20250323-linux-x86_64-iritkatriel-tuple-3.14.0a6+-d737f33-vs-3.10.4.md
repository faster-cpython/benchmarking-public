# Results vs. 3.10.4

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: d737f33
- commit date: 2025-03-23
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                         |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                       |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.89x faster                                         |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                        |
| nbody          | 154 ms                                                 | 97.4 ms: 1.58x faster                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                         |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                        |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                       |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                         |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                        |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                         |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.89x faster                                         |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                         |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                        |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                        |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                         |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                        |
| logging_silent           | 190 ns                                                 | 98.9 ns: 1.92x faster                                        |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                        |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                         |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                         |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                        |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 76.1 ms: 1.68x faster                                        |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                        |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                       |
| nbody                    | 154 ms                                                 | 97.4 ms: 1.58x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                        |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                        |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                         |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                         |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                         |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                         |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                        |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                        |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                        |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                        |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.43x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                       |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                        |
| sympy_sum                | 196 ms                                                 | 145 ms: 1.36x faster                                         |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                        |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                       |
| sympy_str                | 346 ms                                                 | 260 ms: 1.33x faster                                         |
| scimark_fft              | 466 ms                                                 | 351 ms: 1.33x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.89 ms: 1.32x faster                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                        |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                       |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                        |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.24x faster                                        |
| fannkuch                 | 532 ms                                                 | 436 ms: 1.22x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                        |
| mdp                      | 2.85 sec                                               | 2.47 sec: 1.15x faster                                       |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                         |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                         |
| async_generators         | 444 ms                                                 | 399 ms: 1.11x faster                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                        |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                        |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                         |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                         |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                        |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.6 ms: 3.48x slower                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250323-3.14.0a6+-d737f33/bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x