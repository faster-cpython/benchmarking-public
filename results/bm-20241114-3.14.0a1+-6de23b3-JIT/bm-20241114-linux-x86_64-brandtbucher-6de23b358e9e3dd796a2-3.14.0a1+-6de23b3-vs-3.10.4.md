# Results vs. 3.10.4

- fork: brandtbucher
- ref: 6de23b358e9e3dd796a2
- machine: linux-x86_64
- commit hash: 6de23b3
- commit date: 2024-11-14
- overall geometric mean: 1.222x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 1.29 sec: 3.69x slower                                                       |
| docutils       | 3.30 sec                                               | 6.92 sec: 2.10x slower                                                       |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                  | 1.80x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 335 ms: 2.17x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 865 ms: 2.04x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 586 ms: 1.73x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.1 ms: 1.87x faster                                                        |
| float          | 117 ms                                                 | 77.0 ms: 1.52x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                        |
| regex_compile  | 188 ms                                                 | 226 ms: 1.20x slower                                                         |
| regex_v8       | 27.8 ms                                                | 48.9 ms: 1.76x slower                                                        |
| Geometric mean | (ref)                                                  | 1.20x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| json_loads           | 31.2 us                                                | 34.0 us: 1.09x slower                                                        |
| pickle_pure_python   | 484 us                                                 | 623 us: 1.29x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                        |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                        |
| genshi_text     | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 61.8 ms: 1.07x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                        |
| generators               | 80.1 ms                                                | 36.1 ms: 2.22x faster                                                        |
| async_tree_none          | 728 ms                                                 | 335 ms: 2.17x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                                         |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 865 ms: 2.04x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                        |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.94x faster                                                        |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                        |
| logging_silent           | 190 ns                                                 | 99.1 ns: 1.91x faster                                                        |
| nbody                    | 154 ms                                                 | 82.1 ms: 1.87x faster                                                        |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 69.4 ms: 1.84x faster                                                        |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 64.3 ms: 1.84x faster                                                        |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                         |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 586 ms: 1.73x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                                        |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                       |
| djangocms                | 38.4 us                                                | 24.5 us: 1.57x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                        |
| float                    | 117 ms                                                 | 77.0 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.51x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                         |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                        |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.46x faster                                                        |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                         |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                       |
| pyflate                  | 716 ms                                                 | 509 ms: 1.41x faster                                                         |
| fannkuch                 | 532 ms                                                 | 382 ms: 1.39x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                        |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                        |
| genshi_text              | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                        |
| nqueens                  | 106 ms                                                 | 89.2 ms: 1.19x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 61.8 ms: 1.07x faster                                                        |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 26.3 ms: 1.02x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                        |
| async_generators         | 444 ms                                                 | 459 ms: 1.04x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                        |
| sympy_expand             | 566 ms                                                 | 599 ms: 1.06x slower                                                         |
| json                     | 5.69 ms                                                | 6.16 ms: 1.08x slower                                                        |
| json_loads               | 31.2 us                                                | 34.0 us: 1.09x slower                                                        |
| sqlite_synth             | 3.02 us                                                | 3.37 us: 1.11x slower                                                        |
| dulwich_log              | 84.3 ms                                                | 96.5 ms: 1.14x slower                                                        |
| regex_compile            | 188 ms                                                 | 226 ms: 1.20x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                        |
| pickle_pure_python       | 484 us                                                 | 623 us: 1.29x slower                                                         |
| sympy_str                | 346 ms                                                 | 457 ms: 1.32x slower                                                         |
| sqlglot_normalize        | 143 ms                                                 | 194 ms: 1.35x slower                                                         |
| telco                    | 7.27 ms                                                | 10.4 ms: 1.43x slower                                                        |
| sympy_sum                | 196 ms                                                 | 317 ms: 1.62x slower                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 284 ms: 1.65x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                        |
| regex_v8                 | 27.8 ms                                                | 48.9 ms: 1.76x slower                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 140 ms: 2.03x slower                                                         |
| docutils                 | 3.30 sec                                               | 6.92 sec: 2.10x slower                                                       |
| pylint                   | 551 ms                                                 | 2.03 sec: 3.68x slower                                                       |
| 2to3                     | 348 ms                                                 | 1.29 sec: 3.69x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                | 108 ms: 4.48x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (2): json_dumps, thrift
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241114-3.14.0a1+-6de23b3-JIT/bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.222x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.39x