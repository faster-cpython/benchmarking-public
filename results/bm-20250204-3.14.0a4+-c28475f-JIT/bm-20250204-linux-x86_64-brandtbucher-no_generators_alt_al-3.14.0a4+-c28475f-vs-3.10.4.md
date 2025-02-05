# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: c28475f
- commit date: 2025-02-04
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                         |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.70x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.2 ms: 1.74x faster                                                        |
| nbody          | 154 ms                                                 | 90.6 ms: 1.70x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.64x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 78.6 ms: 1.26x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 94.6 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| django_template | 48.2 ms                                                | 33.2 ms: 1.45x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                         |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                        |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.70x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                         |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                        |
| scimark_sor              | 220 ms                                                 | 113 ms: 1.94x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                        |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.90x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 70.0 ms: 1.83x faster                                                        |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                        |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                         |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                         |
| spectral_norm            | 170 ms                                                 | 96.5 ms: 1.76x faster                                                        |
| float                    | 117 ms                                                 | 67.2 ms: 1.74x faster                                                        |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                       |
| nbody                    | 154 ms                                                 | 90.6 ms: 1.70x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.69x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.64x faster                                                         |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                        |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                         |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| django_template          | 48.2 ms                                                | 33.2 ms: 1.45x faster                                                        |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.59 ms: 1.41x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.39 ms: 1.41x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                        |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                       |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.28x faster                                                        |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 78.6 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                        |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 94.6 ms: 1.22x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                         |
| nqueens                  | 106 ms                                                 | 89.6 ms: 1.18x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                        |
| async_generators         | 444 ms                                                 | 405 ms: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                        |
| coverage                 | 79.4 ms                                                | 90.6 ms: 1.14x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250204-3.14.0a4+-c28475f-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x