# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                |
| html5lib       | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 666 ms: 2.66x faster                                                  |
| async_tree_none         | 728 ms                                                 | 291 ms: 2.50x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 349 ms: 2.49x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 596 ms: 1.70x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.0 ms: 1.56x faster                                                 |
| nbody          | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| pidigits       | 191 ms                                                 | 207 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.01 ms: 1.21x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                |
| pickle_pure_python   | 484 us                                                 | 375 us: 1.29x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 256 us: 1.29x faster                                                  |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 75.3 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| json_loads           | 31.2 us                                                | 33.6 us: 1.08x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 110 ms: 1.11x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.96 us: 1.15x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.05 us: 1.19x slower                                                 |
| pickle_dict          | 29.6 us                                                | 37.9 us: 1.28x slower                                                 |
| unpickle             | 14.4 us                                                | 19.0 us: 1.32x slower                                                 |
| pickle               | 10.7 us                                                | 14.9 us: 1.40x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.35 ms: 1.24x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| django_template | 48.2 ms                                                | 40.2 ms: 1.20x faster                                                 |
| mako            | 16.3 ms                                                | 13.8 ms: 1.18x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 197 us: 2.76x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 666 ms: 2.66x faster                                                  |
| async_tree_none          | 728 ms                                                 | 291 ms: 2.50x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 349 ms: 2.49x faster                                                  |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.84 ms: 2.06x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.03x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.48 sec: 1.93x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                  |
| pylint                   | 551 ms                                                 | 311 ms: 1.77x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 596 ms: 1.70x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 34.3 us: 1.70x faster                                                 |
| chaos                    | 115 ms                                                 | 69.9 ms: 1.65x faster                                                 |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.61x faster                                                  |
| raytrace                 | 507 ms                                                 | 322 ms: 1.57x faster                                                  |
| float                    | 117 ms                                                 | 75.0 ms: 1.56x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                 |
| richards_super           | 94.7 ms                                                | 61.4 ms: 1.54x faster                                                 |
| deepcopy                 | 479 us                                                 | 314 us: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 78.2 ms: 1.51x faster                                                 |
| comprehensions           | 28.8 us                                                | 19.2 us: 1.50x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 86.9 ms: 1.47x faster                                                 |
| richards                 | 79.3 ms                                                | 54.0 ms: 1.47x faster                                                 |
| nbody                    | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                |
| scimark_lu               | 176 ms                                                 | 133 ms: 1.32x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                 |
| html5lib                 | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                 |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| coroutines               | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 375 us: 1.29x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 256 us: 1.29x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.34 us: 1.25x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 21.0 ms: 1.23x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.01 ms: 1.21x faster                                                 |
| django_template          | 48.2 ms                                                | 40.2 ms: 1.20x faster                                                 |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| mako                     | 16.3 ms                                                | 13.8 ms: 1.18x faster                                                 |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.18x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 52.1 ns: 1.15x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.68 ms: 1.14x faster                                                 |
| scimark_fft              | 466 ms                                                 | 412 ms: 1.13x faster                                                  |
| pathlib                  | 20.5 ms                                                | 18.2 ms: 1.12x faster                                                 |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                  |
| sympy_str                | 346 ms                                                 | 310 ms: 1.12x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| logging_simple           | 8.30 us                                                | 7.51 us: 1.11x faster                                                 |
| fannkuch                 | 532 ms                                                 | 491 ms: 1.08x faster                                                  |
| logging_format           | 9.09 us                                                | 8.46 us: 1.07x faster                                                 |
| sympy_expand             | 566 ms                                                 | 534 ms: 1.06x faster                                                  |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                  |
| nqueens                  | 106 ms                                                 | 100 ms: 1.06x faster                                                  |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 75.3 ms: 1.05x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 954 us: 1.03x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 2.05 sec: 1.03x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 1.00 sec: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| meteor_contest           | 120 ms                                                 | 119 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.21 us: 1.06x slower                                                 |
| json                     | 5.69 ms                                                | 6.11 ms: 1.07x slower                                                 |
| json_loads               | 31.2 us                                                | 33.6 us: 1.08x slower                                                 |
| pidigits                 | 191 ms                                                 | 207 ms: 1.09x slower                                                  |
| xml_etree_generate       | 99.4 ms                                                | 110 ms: 1.11x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.96 us: 1.15x slower                                                 |
| pickle_list              | 5.08 us                                                | 6.05 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.35 ms: 1.24x slower                                                 |
| pickle_dict              | 29.6 us                                                | 37.9 us: 1.28x slower                                                 |
| unpickle                 | 14.4 us                                                | 19.0 us: 1.32x slower                                                 |
| telco                    | 7.27 ms                                                | 9.64 ms: 1.33x slower                                                 |
| pickle                   | 10.7 us                                                | 14.9 us: 1.40x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.13 ms: 1.42x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                                 |
| logging_silent           | 190 ns                                                 | 625 ns: 3.30x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 104 ms: 4.34x slower                                                  |
| coverage                 | 79.4 ms                                                | 519 ms: 6.53x slower                                                  |
| thrift                   | 1.07 ms                                                | 149 ms: 139.12x slower                                                |
| Geometric mean           | (ref)                                                  | 1.11x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.31x