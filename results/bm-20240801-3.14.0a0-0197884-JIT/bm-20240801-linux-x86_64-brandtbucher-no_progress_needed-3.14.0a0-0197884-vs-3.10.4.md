# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 0197884
- commit date: 2024-08-01
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 284 ms: 1.23x faster                                                      |
| docutils       | 3.30 sec                                               | 2.99 sec: 1.10x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.3 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 908 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 145 ms: 1.30x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                     |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.41x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| json_loads           | 31.2 us                                                | 28.2 us: 1.10x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                     |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                     |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 53.3 ms: 1.24x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                     |
| generators               | 80.1 ms                                                | 32.9 ms: 2.43x faster                                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                                      |
| chaos                    | 115 ms                                                 | 57.9 ms: 2.00x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 908 ms: 1.95x faster                                                      |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.93x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                      |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                      |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                      |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                     |
| mako                     | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                     |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                     |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                      |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                                      |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| go                       | 240 ms                                                 | 150 ms: 1.60x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                     |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                     |
| pylint                   | 551 ms                                                 | 370 ms: 1.49x faster                                                      |
| tornado_http             | 136 ms                                                 | 94.3 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.41x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.64 ms: 1.36x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                    |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                     |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                                     |
| regex_compile            | 188 ms                                                 | 145 ms: 1.30x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 53.3 ms: 1.24x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                     |
| 2to3                     | 348 ms                                                 | 284 ms: 1.23x faster                                                      |
| dask                     | 441 ms                                                 | 364 ms: 1.21x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 820 us: 1.20x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.6 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                                     |
| sympy_str                | 346 ms                                                 | 310 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                     |
| json_loads               | 31.2 us                                                | 28.2 us: 1.10x faster                                                     |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.99 sec: 1.10x faster                                                    |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.05x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                     |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                     |
| coverage                 | 79.4 ms                                                | 90.4 ms: 1.14x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-0197884-JIT/bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x