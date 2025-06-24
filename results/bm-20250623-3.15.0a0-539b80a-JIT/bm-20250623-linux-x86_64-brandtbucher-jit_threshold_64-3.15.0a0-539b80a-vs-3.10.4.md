# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_threshold_64
- machine: linux-x86_64
- commit hash: 539b80a
- commit date: 2025-06-23
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                    |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.6 ms: 1.79x faster                                                   |
| nbody          | 154 ms                                                 | 90.9 ms: 1.69x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.46x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                    |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                   |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                   |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                    |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                    |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                  |
| richards_super           | 94.7 ms                                                | 42.0 ms: 2.26x faster                                                   |
| richards                 | 79.3 ms                                                | 36.9 ms: 2.15x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                   |
| go                       | 240 ms                                                 | 122 ms: 1.96x faster                                                    |
| pylint                   | 551 ms                                                 | 289 ms: 1.91x faster                                                    |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                    |
| chaos                    | 115 ms                                                 | 62.2 ms: 1.86x faster                                                   |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                    |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.79x faster                                                    |
| float                    | 117 ms                                                 | 65.6 ms: 1.79x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.77x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 74.8 ms: 1.71x faster                                                   |
| pyflate                  | 716 ms                                                 | 421 ms: 1.70x faster                                                    |
| nbody                    | 154 ms                                                 | 90.9 ms: 1.69x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                  |
| djangocms                | 38.4 us                                                | 23.1 us: 1.67x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                    |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.53 ms: 1.59x faster                                                   |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                    |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                   |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                    |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.42x faster                                                   |
| scimark_fft              | 466 ms                                                 | 328 ms: 1.42x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                   |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                    |
| coroutines               | 35.1 ms                                                | 25.6 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.18 us: 1.34x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.60 sec: 1.32x faster                                                  |
| logging_format           | 9.09 us                                                | 6.94 us: 1.31x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                   |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                   |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                   |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                    |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 816 ms: 1.25x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                    |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                   |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                    |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                   |
| coverage                 | 79.4 ms                                                | 88.4 ms: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                                   |
| logging_silent           | 190 ns                                                 | 477 ns: 2.51x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                            |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250623-3.15.0a0-539b80a-JIT/bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.38x