# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                 |
| nbody          | 154 ms                                                 | 98.2 ms: 1.56x faster                                                 |
| pidigits       | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| regex_dna      | 227 ms                                                 | 188 ms: 1.21x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                 |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| generators               | 80.1 ms                                                | 31.0 ms: 2.59x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                |
| deltablue                | 7.91 ms                                                | 3.48 ms: 2.27x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.0 ms: 1.93x faster                                                 |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.90x faster                                                 |
| raytrace                 | 507 ms                                                 | 269 ms: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                  |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                 |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                  |
| comprehensions           | 28.8 us                                                | 15.9 us: 1.81x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                 |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                                 |
| pyflate                  | 716 ms                                                 | 430 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                 |
| nbody                    | 154 ms                                                 | 98.2 ms: 1.56x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                 |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                 |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.42x faster                                                 |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                 |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.08 us: 1.37x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.36x faster                                                |
| logging_format           | 9.09 us                                                | 6.72 us: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.91 ms: 1.32x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.61 sec: 1.30x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 794 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                  |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| scimark_fft              | 466 ms                                                 | 380 ms: 1.23x faster                                                  |
| regex_dna                | 227 ms                                                 | 188 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                 |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.84 ms: 1.34x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.58x slower                                                 |
| logging_silent           | 190 ns                                                 | 473 ns: 2.49x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.31x