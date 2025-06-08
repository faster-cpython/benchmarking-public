# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.074x faster
- HPT reliability: 98.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 339 ms: 1.03x faster                                                  |
| docutils       | 3.30 sec                                               | 3.14 sec: 1.05x faster                                                |
| html5lib       | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 642 ms: 2.75x faster                                                  |
| async_tree_none         | 728 ms                                                 | 301 ms: 2.42x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 381 ms: 2.28x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 626 ms: 1.62x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 82.0 ms: 1.43x faster                                                 |
| nbody          | 154 ms                                                 | 154 ms: 1.01x slower                                                  |
| pidigits       | 191 ms                                                 | 201 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                | 2.97 ms: 1.22x faster                                                 |
| regex_dna      | 227 ms                                                 | 192 ms: 1.18x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| regex_compile  | 188 ms                                                 | 172 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.63 sec: 1.19x faster                                                |
| pickle_pure_python   | 484 us                                                 | 423 us: 1.15x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 301 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 164 ms: 1.02x faster                                                  |
| json_dumps           | 14.2 ms                                                | 14.9 ms: 1.05x slower                                                 |
| xml_etree_process    | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.95 us: 1.17x slower                                                 |
| unpickle_list        | 5.20 us                                                | 6.28 us: 1.21x slower                                                 |
| json_loads           | 31.2 us                                                | 37.7 us: 1.21x slower                                                 |
| pickle_dict          | 29.6 us                                                | 36.9 us: 1.25x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 125 ms: 1.26x slower                                                  |
| pickle               | 10.7 us                                                | 15.2 us: 1.43x slower                                                 |
| unpickle             | 14.4 us                                                | 22.0 us: 1.53x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 17.1 ms: 1.17x slower                                                 |
| python_startup_no_site | 5.93 ms                                                | 9.97 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 53.2 ms: 1.11x slower                                                 |
| genshi_text     | 31.8 ms                                                | 35.2 ms: 1.11x slower                                                 |
| mako            | 16.3 ms                                                | 18.6 ms: 1.14x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 76.2 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 642 ms: 2.75x faster                                                  |
| async_tree_none          | 728 ms                                                 | 301 ms: 2.42x faster                                                  |
| generators               | 80.1 ms                                                | 34.8 ms: 2.30x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 381 ms: 2.28x faster                                                  |
| typing_runtime_protocols | 544 us                                                 | 244 us: 2.23x faster                                                  |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                                  |
| deltablue                | 7.91 ms                                                | 4.63 ms: 1.71x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 544 ms: 1.70x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.74 sec: 1.63x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 626 ms: 1.62x faster                                                  |
| pylint                   | 551 ms                                                 | 357 ms: 1.55x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 2.48 ms: 1.46x faster                                                 |
| float                    | 117 ms                                                 | 82.0 ms: 1.43x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 41.2 us: 1.42x faster                                                 |
| chaos                    | 115 ms                                                 | 82.7 ms: 1.40x faster                                                 |
| scimark_sor              | 220 ms                                                 | 158 ms: 1.39x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.87 ms: 1.32x faster                                                 |
| pyflate                  | 716 ms                                                 | 549 ms: 1.31x faster                                                  |
| raytrace                 | 507 ms                                                 | 388 ms: 1.31x faster                                                  |
| comprehensions           | 28.8 us                                                | 22.6 us: 1.27x faster                                                 |
| deepcopy                 | 479 us                                                 | 383 us: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.07 sec: 1.24x faster                                                |
| regex_effbot             | 3.63 ms                                                | 2.97 ms: 1.22x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.30 sec: 1.22x faster                                                |
| coroutines               | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                 |
| richards_super           | 94.7 ms                                                | 78.9 ms: 1.20x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.63 sec: 1.19x faster                                                |
| regex_dna                | 227 ms                                                 | 192 ms: 1.18x faster                                                  |
| spectral_norm            | 170 ms                                                 | 144 ms: 1.18x faster                                                  |
| html5lib                 | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 101 ms: 1.17x faster                                                  |
| richards                 | 79.3 ms                                                | 68.0 ms: 1.17x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 72.4 ms: 1.17x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 423 us: 1.15x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 112 ms: 1.14x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 301 us: 1.10x faster                                                  |
| regex_compile            | 188 ms                                                 | 172 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| scimark_lu               | 176 ms                                                 | 165 ms: 1.07x faster                                                  |
| unpack_sequence          | 60.0 ns                                                | 56.9 ns: 1.06x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.14 sec: 1.05x faster                                                |
| pathlib                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| 2to3                     | 348 ms                                                 | 339 ms: 1.03x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 25.2 ms: 1.03x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 164 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 4.13 us: 1.01x faster                                                 |
| nbody                    | 154 ms                                                 | 154 ms: 1.01x slower                                                  |
| sympy_sum                | 196 ms                                                 | 198 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                  |
| scimark_fft              | 466 ms                                                 | 485 ms: 1.04x slower                                                  |
| json_dumps               | 14.2 ms                                                | 14.9 ms: 1.05x slower                                                 |
| pidigits                 | 191 ms                                                 | 201 ms: 1.05x slower                                                  |
| sympy_str                | 346 ms                                                 | 369 ms: 1.07x slower                                                  |
| sqlite_synth             | 3.02 us                                                | 3.24 us: 1.07x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                 |
| logging_simple           | 8.30 us                                                | 9.10 us: 1.10x slower                                                 |
| xml_etree_process        | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                 |
| django_template          | 48.2 ms                                                | 53.2 ms: 1.11x slower                                                 |
| fannkuch                 | 532 ms                                                 | 588 ms: 1.11x slower                                                  |
| genshi_text              | 31.8 ms                                                | 35.2 ms: 1.11x slower                                                 |
| sympy_expand             | 566 ms                                                 | 627 ms: 1.11x slower                                                  |
| nqueens                  | 106 ms                                                 | 118 ms: 1.11x slower                                                  |
| thrift                   | 1.07 ms                                                | 1.21 ms: 1.13x slower                                                 |
| logging_format           | 9.09 us                                                | 10.2 us: 1.13x slower                                                 |
| meteor_contest           | 120 ms                                                 | 135 ms: 1.13x slower                                                  |
| mako                     | 16.3 ms                                                | 18.6 ms: 1.14x slower                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.40 sec: 1.14x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.86 ms: 1.15x slower                                                 |
| json                     | 5.69 ms                                                | 6.54 ms: 1.15x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.17 sec: 1.15x slower                                                |
| genshi_xml               | 66.0 ms                                                | 76.2 ms: 1.15x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.95 us: 1.17x slower                                                 |
| python_startup           | 14.6 ms                                                | 17.1 ms: 1.17x slower                                                 |
| unpickle_list            | 5.20 us                                                | 6.28 us: 1.21x slower                                                 |
| json_loads               | 31.2 us                                                | 37.7 us: 1.21x slower                                                 |
| pickle_dict              | 29.6 us                                                | 36.9 us: 1.25x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 125 ms: 1.26x slower                                                  |
| pickle                   | 10.7 us                                                | 15.2 us: 1.43x slower                                                 |
| unpickle                 | 14.4 us                                                | 22.0 us: 1.53x slower                                                 |
| telco                    | 7.27 ms                                                | 11.9 ms: 1.63x slower                                                 |
| coverage                 | 79.4 ms                                                | 132 ms: 1.66x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.97 ms: 1.68x slower                                                 |
| bench_thread_pool        | 986 us                                                 | 3.51 ms: 3.56x slower                                                 |
| logging_silent           | 190 ns                                                 | 705 ns: 3.71x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 111 ms: 4.62x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 98.17% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.59x