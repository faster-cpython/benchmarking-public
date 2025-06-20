# Results vs. 3.10.4

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.465x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                                 |
| nbody          | 154 ms                                                 | 90.9 ms: 1.69x faster                                                 |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.45x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 21.5 ms: 1.29x faster                                                 |
| regex_dna      | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| generators               | 80.1 ms                                                | 31.1 ms: 2.58x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.9 ms: 2.37x faster                                                 |
| richards                 | 79.3 ms                                                | 34.3 ms: 2.31x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                  |
| go                       | 240 ms                                                 | 124 ms: 1.94x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| chaos                    | 115 ms                                                 | 62.5 ms: 1.85x faster                                                 |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                  |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                                 |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                                 |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                 |
| pyflate                  | 716 ms                                                 | 414 ms: 1.73x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                                 |
| nbody                    | 154 ms                                                 | 90.9 ms: 1.69x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.67x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.47 ms: 1.61x faster                                                 |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.45x faster                                                 |
| scimark_fft              | 466 ms                                                 | 330 ms: 1.41x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.41x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.09 us: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                  |
| logging_format           | 9.09 us                                                | 6.72 us: 1.35x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 21.5 ms: 1.29x faster                                                 |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                 |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.70 sec: 1.23x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 840 ms: 1.21x faster                                                  |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| regex_dna                | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.73 ms: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.2 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.465x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x