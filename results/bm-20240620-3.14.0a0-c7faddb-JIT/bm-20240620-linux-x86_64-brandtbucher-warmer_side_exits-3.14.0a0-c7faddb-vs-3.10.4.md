# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: c7faddb
- commit date: 2024-06-20
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                     |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                   |
| html5lib       | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                    |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 368 ms: 1.98x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 452 ms: 1.93x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 594 ms: 1.71x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.89x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                                    |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                    |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.48x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                    |
| regex_dna      | 227 ms                                                 | 233 ms: 1.03x slower                                                     |
| regex_effbot   | 3.63 ms                                                | 3.95 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.63x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                                    |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                    |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                                    |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.41 ms: 1.25x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                    |
| django_template | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                     |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.85 ms: 2.05x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                    |
| async_tree_none          | 728 ms                                                 | 368 ms: 1.98x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                     |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 452 ms: 1.93x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 61.4 ms: 1.92x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                    |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 489 ms: 1.89x faster                                                     |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.88x faster                                                    |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                     |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                     |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                    |
| deepcopy                 | 479 us                                                 | 278 us: 1.72x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 594 ms: 1.71x faster                                                     |
| pyflate                  | 716 ms                                                 | 425 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                    |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                    |
| mako                     | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                                     |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.63x faster                                                     |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.57 ms: 1.58x faster                                                    |
| pylint                   | 551 ms                                                 | 349 ms: 1.58x faster                                                     |
| fannkuch                 | 532 ms                                                 | 345 ms: 1.54x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                    |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                                    |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                     |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                     |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 812 us: 1.32x faster                                                     |
| django_template          | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                    |
| html5lib                 | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                    |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.2 ms: 1.26x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.9 ms: 1.24x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                    |
| dask                     | 441 ms                                                 | 366 ms: 1.21x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.7 ms: 1.20x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 830 us: 1.19x faster                                                     |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                     |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.11x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                    |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                    |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                     |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                    |
| regex_dna                | 227 ms                                                 | 233 ms: 1.03x slower                                                     |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                    |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.95 ms: 1.09x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.01 ms: 1.11x slower                                                    |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                                    |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                                    |
| coverage                 | 79.4 ms                                                | 94.2 ms: 1.19x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.41 ms: 1.25x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-c7faddb-JIT/bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.23x