# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.03x faster                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 117 ms                                                 | 65.9 ms: 1.78x faster                                 |
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.43x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                  |
| regex_v8       | 27.8 ms                                                | 22.6 ms: 1.23x faster                                 |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                  |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.64x faster                                  |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                  |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.40x faster                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                 |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                 |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.53x faster                                 |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                 |
| django_template | 48.2 ms                                                | 33.1 ms: 1.45x faster                                 |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.30x faster                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                  |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                  |
| generators               | 80.1 ms                                                | 30.6 ms: 2.62x faster                                 |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.53x faster                                 |
| richards_super           | 94.7 ms                                                | 39.6 ms: 2.39x faster                                 |
| richards                 | 79.3 ms                                                | 34.3 ms: 2.31x faster                                 |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.03x faster                                  |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                 |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                  |
| go                       | 240 ms                                                 | 124 ms: 1.93x faster                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.85x faster                                  |
| chaos                    | 115 ms                                                 | 63.7 ms: 1.81x faster                                 |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                  |
| float                    | 117 ms                                                 | 65.9 ms: 1.78x faster                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                 |
| pyflate                  | 716 ms                                                 | 424 ms: 1.69x faster                                  |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 76.8 ms: 1.66x faster                                 |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.64x faster                                  |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                 |
| hexiom                   | 10.4 ms                                                | 6.41 ms: 1.62x faster                                 |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.53x faster                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                 |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                  |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                  |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.45x faster                                 |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                 |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.40x faster                                 |
| scimark_fft              | 466 ms                                                 | 332 ms: 1.40x faster                                  |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                |
| coroutines               | 35.1 ms                                                | 25.3 ms: 1.39x faster                                 |
| dulwich_log              | 84.3 ms                                                | 62.1 ms: 1.36x faster                                 |
| logging_simple           | 8.30 us                                                | 6.16 us: 1.35x faster                                 |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| logging_format           | 9.09 us                                                | 6.84 us: 1.33x faster                                 |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                 |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.30x faster                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                 |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                  |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                  |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                  |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 815 ms: 1.25x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.69 sec: 1.24x faster                                |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                 |
| regex_v8                 | 27.8 ms                                                | 22.6 ms: 1.23x faster                                 |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                 |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                 |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                  |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                  |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                 |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                 |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                 |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                  |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                 |
| gc_traversal             | 3.62 ms                                                | 5.01 ms: 1.38x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                 |
| logging_silent           | 190 ns                                                 | 475 ns: 2.51x slower                                  |
| coverage                 | 79.4 ms                                                | 424 ms: 5.34x slower                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 138.07x slower                                |
| Geometric mean           | (ref)                                                  | 1.31x faster                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.33x