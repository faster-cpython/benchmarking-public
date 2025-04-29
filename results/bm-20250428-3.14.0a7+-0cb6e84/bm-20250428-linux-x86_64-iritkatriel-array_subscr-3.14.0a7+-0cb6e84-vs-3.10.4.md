# Results vs. 3.10.4

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 0cb6e84
- commit date: 2025-04-28
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                              |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 590 ms: 3.00x faster                                                |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                                |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                               |
| nbody          | 154 ms                                                 | 97.8 ms: 1.57x faster                                               |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.2 ms: 1.25x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.15x faster                                               |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                |
| Geometric mean | (ref)                                                  | 1.24x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 30.4 us: 1.03x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                |
| async_tree_io            | 1.77 sec                                               | 590 ms: 3.00x faster                                                |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                               |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                               |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                              |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                                |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                               |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                                |
| logging_silent           | 190 ns                                                 | 96.3 ns: 1.97x faster                                               |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                               |
| deepcopy                 | 479 us                                                 | 252 us: 1.90x faster                                                |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                               |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                               |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                               |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                               |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                               |
| nbody                    | 154 ms                                                 | 97.8 ms: 1.57x faster                                               |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                               |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                               |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                               |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                               |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                              |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                |
| regex_v8                 | 27.8 ms                                                | 22.2 ms: 1.25x faster                                               |
| scimark_fft              | 466 ms                                                 | 382 ms: 1.22x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.50 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.15x faster                                               |
| async_generators         | 444 ms                                                 | 396 ms: 1.12x faster                                                |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                               |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                               |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                               |
| json_loads               | 31.2 us                                                | 30.4 us: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                               |
| coverage                 | 79.4 ms                                                | 92.3 ms: 1.16x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.37x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250428-3.14.0a7+-0cb6e84/bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x