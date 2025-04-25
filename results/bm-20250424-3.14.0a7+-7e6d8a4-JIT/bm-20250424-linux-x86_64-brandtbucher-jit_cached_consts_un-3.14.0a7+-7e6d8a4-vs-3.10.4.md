# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts_un
- machine: linux-x86_64
- commit hash: 7e6d8a4
- commit date: 2025-04-24
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                         |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.76x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.08x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                        |
| float          | 117 ms                                                 | 69.5 ms: 1.68x faster                                                        |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                        |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                        |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.27 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                        |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                         |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.76x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.00 ms: 2.64x faster                                                        |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.36x faster                                                       |
| richards_super           | 94.7 ms                                                | 41.1 ms: 2.31x faster                                                        |
| richards                 | 79.3 ms                                                | 36.2 ms: 2.19x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.08x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                        |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                        |
| pylint                   | 551 ms                                                 | 285 ms: 1.93x faster                                                         |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                         |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                                         |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                         |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                         |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                        |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                       |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                         |
| float                    | 117 ms                                                 | 69.5 ms: 1.68x faster                                                        |
| pyflate                  | 716 ms                                                 | 433 ms: 1.66x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.56x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| comprehensions           | 28.8 us                                                | 18.6 us: 1.55x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                        |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.47x faster                                                         |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                       |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                        |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 61.2 ms: 1.38x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                        |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                        |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                         |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                         |
| nqueens                  | 106 ms                                                 | 82.3 ms: 1.29x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 134 ms: 1.28x faster                                                         |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                        |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                        |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                        |
| async_generators         | 444 ms                                                 | 422 ms: 1.05x faster                                                         |
| json                     | 5.69 ms                                                | 5.49 ms: 1.04x faster                                                        |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 93.7 ms: 1.18x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.27 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250424-3.14.0a7+-7e6d8a4-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.30x