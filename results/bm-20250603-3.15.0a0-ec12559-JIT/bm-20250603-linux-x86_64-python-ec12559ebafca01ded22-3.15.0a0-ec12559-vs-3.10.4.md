# Results vs. 3.10.4

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.949x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                  |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 506 ms: 2.01x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.5 ms: 1.81x faster                                                 |
| nbody          | 154 ms                                                 | 91.8 ms: 1.67x faster                                                 |
| Geometric mean | (ref)                                                  | 1.45x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.1 ms: 1.24x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                 |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat           | 2.10 sec                                               | 1.45 us: 1447997.12x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 829 ns: 1228117.49x faster                                            |
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                  |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.59x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.4 ms: 2.40x faster                                                 |
| richards                 | 79.3 ms                                                | 33.4 ms: 2.37x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 506 ms: 2.01x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                 |
| go                       | 240 ms                                                 | 123 ms: 1.96x faster                                                  |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                  |
| deepcopy                 | 479 us                                                 | 253 us: 1.90x faster                                                  |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                  |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                  |
| float                    | 117 ms                                                 | 64.5 ms: 1.81x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.9 ms: 1.77x faster                                                 |
| pyflate                  | 716 ms                                                 | 413 ms: 1.73x faster                                                  |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 76.3 ms: 1.68x faster                                                 |
| nbody                    | 154 ms                                                 | 91.8 ms: 1.67x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.48 ms: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                  |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                                |
| scimark_fft              | 466 ms                                                 | 332 ms: 1.40x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.9 ms: 1.38x faster                                                 |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.37x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.09 us: 1.36x faster                                                 |
| logging_format           | 9.09 us                                                | 6.74 us: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.31x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                                 |
| fannkuch                 | 532 ms                                                 | 421 ms: 1.26x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.1 ms: 1.24x faster                                                 |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                 |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                                 |
| logging_silent           | 190 ns                                                 | 471 ns: 2.48x slower                                                  |
| coverage                 | 79.4 ms                                                | 422 ms: 5.31x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 137.92x slower                                                |
| Geometric mean           | (ref)                                                  | 1.90x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (25) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.949x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.32x