# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.8 ms: 1.47x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.5 ms: 1.88x faster                                                 |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                |
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.75 ms: 1.67x faster                                                 |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                  |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.46 ms: 2.29x faster                                                 |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| richards_super           | 94.7 ms                                                | 46.3 ms: 2.05x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                 |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.0 ms: 1.97x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                  |
| richards                 | 79.3 ms                                                | 40.6 ms: 1.95x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.93x faster                                                 |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                  |
| nbody                    | 154 ms                                                 | 81.5 ms: 1.88x faster                                                 |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                  |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                 |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                  |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                  |
| mako                     | 16.3 ms                                                | 9.75 ms: 1.67x faster                                                 |
| pyflate                  | 716 ms                                                 | 430 ms: 1.67x faster                                                  |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.54 ms: 1.59x faster                                                 |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.8 ms: 1.47x faster                                                 |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                  |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                                  |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                                 |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                                  |
| sympy_str                | 346 ms                                                 | 297 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                 |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                 |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 90.5 ms: 1.14x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x