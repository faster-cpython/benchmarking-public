# Results vs. 3.10.4

- fork: iritkatriel
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 6cacd2b
- commit date: 2024-12-04
- overall geometric mean: 1.418x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                             |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                           |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                            |
| tornado_http   | 136 ms                                                 | 90.7 ms: 1.50x faster                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 425 ms: 2.05x faster                                             |
| async_tree_io           | 1.77 sec                                               | 891 ms: 1.99x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 554 ms: 1.83x faster                                             |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.4 ms: 1.72x faster                                            |
| float          | 117 ms                                                 | 75.3 ms: 1.56x faster                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.40x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                            |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                             |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                           |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                            |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                             |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.15x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 6.97 ms: 1.17x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                            |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                            |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                            |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                            |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                             |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                            |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                            |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                             |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 425 ms: 2.05x faster                                             |
| chaos                    | 115 ms                                                 | 57.0 ms: 2.02x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                            |
| async_tree_io            | 1.77 sec                                               | 891 ms: 1.99x faster                                             |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                             |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 554 ms: 1.83x faster                                             |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                            |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                            |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                            |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                             |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                            |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                            |
| nbody                    | 154 ms                                                 | 89.4 ms: 1.72x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                            |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                             |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                             |
| float                    | 117 ms                                                 | 75.3 ms: 1.56x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                            |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                            |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                             |
| tornado_http             | 136 ms                                                 | 90.7 ms: 1.50x faster                                            |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                            |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                            |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                            |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                           |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                             |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                             |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                            |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                             |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                            |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                            |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                            |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                            |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                             |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                             |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                            |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                            |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                             |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                            |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.15x faster                                            |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                            |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                             |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                            |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                             |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                           |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                             |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                             |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                            |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 6.97 ms: 1.17x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.45 ms: 1.23x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 77.9 ms: 3.24x slower                                            |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                     |

Benchmark hidden because not significant (2): regex_effbot, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, raytrace, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241204-3.14.0a0-6cacd2b/bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.418x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.25x