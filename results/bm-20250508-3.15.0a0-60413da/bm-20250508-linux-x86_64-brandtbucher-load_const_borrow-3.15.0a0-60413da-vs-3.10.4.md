# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.301x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                     |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                     |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.6 ms: 1.61x faster                                                    |
| nbody          | 154 ms                                                 | 96.0 ms: 1.60x faster                                                    |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                     |
| regex_v8       | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                    |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.22x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 97.6 ms: 1.18x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                    |
| json_loads           | 31.2 us                                                | 30.3 us: 1.03x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                    |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                    |
| mako            | 16.3 ms                                                | 11.9 ms: 1.38x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                     |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                     |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.32x faster                                                    |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                   |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                    |
| pylint                   | 551 ms                                                 | 281 ms: 1.97x faster                                                     |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                    |
| richards_super           | 94.7 ms                                                | 49.6 ms: 1.91x faster                                                    |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                     |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                     |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.82x faster                                                    |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                    |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                     |
| float                    | 117 ms                                                 | 72.6 ms: 1.61x faster                                                    |
| nbody                    | 154 ms                                                 | 96.0 ms: 1.60x faster                                                    |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                    |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                     |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                    |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                    |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                     |
| mako                     | 16.3 ms                                                | 11.9 ms: 1.38x faster                                                    |
| logging_simple           | 8.30 us                                                | 6.10 us: 1.36x faster                                                    |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                    |
| logging_format           | 9.09 us                                                | 6.85 us: 1.33x faster                                                    |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                    |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                     |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                    |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                   |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.25x faster                                                     |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                    |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 97.6 ms: 1.18x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                     |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                     |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                    |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                    |
| json_loads               | 31.2 us                                                | 30.3 us: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.11x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.35x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.56 ms: 1.58x slower                                                    |
| dask                     | 441 ms                                                 | 915 ms: 2.08x slower                                                     |
| logging_silent           | 190 ns                                                 | 481 ns: 2.53x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 93.3 ms: 3.89x slower                                                    |
| coverage                 | 79.4 ms                                                | 419 ms: 5.28x slower                                                     |
| thrift                   | 1.07 ms                                                | 148 ms: 138.48x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250508-3.15.0a0-60413da/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.301x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x