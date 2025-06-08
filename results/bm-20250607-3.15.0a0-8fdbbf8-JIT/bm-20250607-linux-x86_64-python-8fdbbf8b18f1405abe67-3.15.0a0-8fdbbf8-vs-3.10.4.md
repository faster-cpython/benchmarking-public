# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.155x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 297 ms: 1.17x faster                                                  |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 655 ms: 2.70x faster                                                  |
| async_tree_none         | 728 ms                                                 | 285 ms: 2.55x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 343 ms: 2.53x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 600 ms: 1.69x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.33x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.9 ms: 1.73x faster                                                 |
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                                 |
| pidigits       | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                |
| unpickle_pure_python | 331 us                                                 | 240 us: 1.38x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 377 us: 1.29x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 68.8 ms: 1.15x faster                                                 |
| json_dumps           | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 102 ms: 1.02x slower                                                  |
| json_loads           | 31.2 us                                                | 33.5 us: 1.07x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.86 us: 1.13x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.04 us: 1.19x slower                                                 |
| pickle_dict          | 29.6 us                                                | 37.7 us: 1.27x slower                                                 |
| unpickle             | 14.4 us                                                | 19.0 us: 1.32x slower                                                 |
| pickle               | 10.7 us                                                | 15.0 us: 1.41x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| mako            | 16.3 ms                                                | 13.2 ms: 1.23x faster                                                 |
| django_template | 48.2 ms                                                | 40.6 ms: 1.19x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 200 us: 2.73x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 655 ms: 2.70x faster                                                  |
| async_tree_none          | 728 ms                                                 | 285 ms: 2.55x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 343 ms: 2.53x faster                                                  |
| generators               | 80.1 ms                                                | 33.5 ms: 2.39x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.45 ms: 2.30x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.3 ms: 2.04x faster                                                 |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.48 sec: 1.92x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                  |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                  |
| pylint                   | 551 ms                                                 | 315 ms: 1.75x faster                                                  |
| float                    | 117 ms                                                 | 67.9 ms: 1.73x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 34.4 us: 1.70x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 600 ms: 1.69x faster                                                  |
| chaos                    | 115 ms                                                 | 70.2 ms: 1.65x faster                                                 |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 72.7 ms: 1.63x faster                                                 |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                                 |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                  |
| raytrace                 | 507 ms                                                 | 323 ms: 1.57x faster                                                  |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                  |
| deepcopy                 | 479 us                                                 | 312 us: 1.54x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.94 ms: 1.50x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 86.3 ms: 1.48x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| comprehensions           | 28.8 us                                                | 20.4 us: 1.41x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 240 us: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                 |
| scimark_fft              | 466 ms                                                 | 351 ms: 1.33x faster                                                  |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.31x faster                                                  |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| coroutines               | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 377 us: 1.29x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.24x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.38 us: 1.23x faster                                                 |
| mako                     | 16.3 ms                                                | 13.2 ms: 1.23x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 21.5 ms: 1.20x faster                                                 |
| django_template          | 48.2 ms                                                | 40.6 ms: 1.19x faster                                                 |
| 2to3                     | 348 ms                                                 | 297 ms: 1.17x faster                                                  |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 68.8 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.64 ms: 1.15x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                                  |
| pathlib                  | 20.5 ms                                                | 18.1 ms: 1.13x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| logging_simple           | 8.30 us                                                | 7.45 us: 1.11x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| fannkuch                 | 532 ms                                                 | 482 ms: 1.10x faster                                                  |
| sympy_str                | 346 ms                                                 | 314 ms: 1.10x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                 |
| logging_format           | 9.09 us                                                | 8.38 us: 1.08x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                 |
| nqueens                  | 106 ms                                                 | 100 ms: 1.06x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| sympy_expand             | 566 ms                                                 | 548 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 965 us: 1.02x faster                                                  |
| meteor_contest           | 120 ms                                                 | 117 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 102 ms: 1.02x slower                                                  |
| pprint_pformat           | 2.10 sec                                               | 2.15 sec: 1.02x slower                                                |
| sqlite_synth             | 3.02 us                                                | 3.14 us: 1.04x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.06 sec: 1.04x slower                                                |
| json                     | 5.69 ms                                                | 6.02 ms: 1.06x slower                                                 |
| pidigits                 | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| json_loads               | 31.2 us                                                | 33.5 us: 1.07x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.86 us: 1.13x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 70.2 ns: 1.17x slower                                                 |
| pickle_list              | 5.08 us                                                | 6.04 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                 |
| telco                    | 7.27 ms                                                | 9.07 ms: 1.25x slower                                                 |
| pickle_dict              | 29.6 us                                                | 37.7 us: 1.27x slower                                                 |
| unpickle                 | 14.4 us                                                | 19.0 us: 1.32x slower                                                 |
| pickle                   | 10.7 us                                                | 15.0 us: 1.41x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.11 ms: 1.41x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.62 ms: 1.62x slower                                                 |
| logging_silent           | 190 ns                                                 | 633 ns: 3.34x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 104 ms: 4.33x slower                                                  |
| coverage                 | 79.4 ms                                                | 518 ms: 6.52x slower                                                  |
| thrift                   | 1.07 ms                                                | 149 ms: 138.63x slower                                                |
| Geometric mean           | (ref)                                                  | 1.12x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.155x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.33x