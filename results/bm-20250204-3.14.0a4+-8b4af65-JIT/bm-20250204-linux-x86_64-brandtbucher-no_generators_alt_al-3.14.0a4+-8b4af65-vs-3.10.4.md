# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: 8b4af65
- commit date: 2025-02-04
- overall geometric mean: 1.451x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                         |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 330 ms: 2.63x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                                        |
| nbody          | 154 ms                                                 | 90.8 ms: 1.69x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.44x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                        |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                        |
| regex_dna      | 227 ms                                                 | 195 ms: 1.16x faster                                                         |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 95.6 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                        |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                        |
| django_template | 48.2 ms                                                | 33.1 ms: 1.46x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                         |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                         |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 330 ms: 2.63x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.50 ms: 2.26x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                         |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                        |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.92x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.91x faster                                                        |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                        |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.81x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 71.0 ms: 1.80x faster                                                        |
| spectral_norm            | 170 ms                                                 | 95.2 ms: 1.78x faster                                                        |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                         |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                         |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                       |
| logging_silent           | 190 ns                                                 | 110 ns: 1.72x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                        |
| nbody                    | 154 ms                                                 | 90.8 ms: 1.69x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                         |
| mako                     | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                        |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                         |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                        |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                         |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.46x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.26 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                        |
| logging_format           | 9.09 us                                                | 6.46 us: 1.41x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                         |
| thrift                   | 1.07 ms                                                | 785 us: 1.37x faster                                                         |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.34x faster                                                        |
| nqueens                  | 106 ms                                                 | 79.6 ms: 1.33x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.29x faster                                                        |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.3 ms: 1.27x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 95.6 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                        |
| regex_dna                | 227 ms                                                 | 195 ms: 1.16x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                                        |
| async_generators         | 444 ms                                                 | 405 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                                        |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.3 ms: 3.34x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250204-3.14.0a4+-8b4af65-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.451x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x