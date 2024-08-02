# Results vs. 3.10.4

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: ecb7974
- commit date: 2024-06-07
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                      |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                       |
| tornado_http   | 136 ms                                                 | 98.0 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 377 ms: 1.93x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 949 ms: 1.86x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 483 ms: 1.80x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 634 ms: 1.60x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.1 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                       |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                       |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| unpickle_list        | 5.20 us                                                | 5.43 us: 1.04x slower                                                       |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.33 us: 1.05x slower                                                       |
| pickle               | 10.7 us                                                | 12.3 us: 1.15x slower                                                       |
| pickle_dict          | 29.6 us                                                | 36.3 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.64 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                       |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                        |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.74 ms: 2.11x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                       |
| async_tree_none          | 728 ms                                                 | 377 ms: 1.93x faster                                                        |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                       |
| nbody                    | 154 ms                                                 | 80.1 ms: 1.92x faster                                                       |
| richards                 | 79.3 ms                                                | 41.8 ms: 1.90x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 949 ms: 1.86x faster                                                        |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 483 ms: 1.80x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                                        |
| logging_silent           | 190 ns                                                 | 108 ns: 1.75x faster                                                        |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                       |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                       |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 634 ms: 1.60x faster                                                        |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                                        |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                       |
| pyflate                  | 716 ms                                                 | 463 ms: 1.55x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 38.3 us: 1.53x faster                                                       |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                        |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.43x faster                                                       |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                      |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.39x faster                                                        |
| tornado_http             | 136 ms                                                 | 98.0 ms: 1.39x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                      |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                       |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                       |
| thrift                   | 1.07 ms                                                | 811 us: 1.32x faster                                                        |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                       |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| deepcopy                 | 479 us                                                 | 369 us: 1.30x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.25x faster                                                       |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 69.2 ms: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 87.3 ms: 1.21x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.21x faster                                                       |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                       |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                        |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 514 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                        |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                       |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.79 sec: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                        |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.59 ms: 1.01x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                        |
| unpickle_list            | 5.20 us                                                | 5.43 us: 1.04x slower                                                       |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                       |
| pickle_list              | 5.08 us                                                | 5.33 us: 1.05x slower                                                       |
| async_generators         | 444 ms                                                 | 470 ms: 1.06x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                       |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                       |
| pickle                   | 10.7 us                                                | 12.3 us: 1.15x slower                                                       |
| coverage                 | 79.4 ms                                                | 94.4 ms: 1.19x slower                                                       |
| pickle_dict              | 29.6 us                                                | 36.3 us: 1.23x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.64 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240607-3.14.0a0-ecb7974-JIT/bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x