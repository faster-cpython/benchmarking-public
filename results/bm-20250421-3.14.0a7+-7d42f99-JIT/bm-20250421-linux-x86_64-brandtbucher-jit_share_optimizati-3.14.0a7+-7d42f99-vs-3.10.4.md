# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_share_optimizati
- machine: linux-x86_64
- commit hash: 7d42f99
- commit date: 2025-04-21
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.88x faster                                                         |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 207 us: 1.60x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                                        |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.25 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.88x faster                                                         |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                         |
| generators               | 80.1 ms                                                | 29.8 ms: 2.68x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                                        |
| richards_super           | 94.7 ms                                                | 38.2 ms: 2.48x faster                                                        |
| richards                 | 79.3 ms                                                | 33.0 ms: 2.40x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                         |
| logging_silent           | 190 ns                                                 | 94.5 ns: 2.01x faster                                                        |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                        |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                         |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                         |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                         |
| deepcopy                 | 479 us                                                 | 254 us: 1.88x faster                                                         |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.5 ms: 1.78x faster                                                        |
| nbody                    | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                        |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                        |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.60x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                         |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                         |
| comprehensions           | 28.8 us                                                | 19.2 us: 1.50x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                        |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                        |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.43x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.38x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                        |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                        |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                         |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                         |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                        |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                        |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                        |
| async_generators         | 444 ms                                                 | 420 ms: 1.06x faster                                                         |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 93.0 ms: 1.17x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.25 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250421-3.14.0a7+-7d42f99-JIT/bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.30x