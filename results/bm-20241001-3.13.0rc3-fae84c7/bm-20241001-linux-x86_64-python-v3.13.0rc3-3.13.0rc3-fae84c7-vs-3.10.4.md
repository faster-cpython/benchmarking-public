# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.394x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                         |
| chameleon      | 9.68 ms                                                | 6.85 ms: 1.41x faster                                        |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                       |
| html5lib       | 88.9 ms                                                | 63.1 ms: 1.41x faster                                        |
| tornado_http   | 136 ms                                                 | 91.2 ms: 1.50x faster                                        |
| Geometric mean | (ref)                                                  | 1.38x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 832 ms: 2.12x faster                                         |
| async_tree_none         | 728 ms                                                 | 349 ms: 2.08x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 437 ms: 1.99x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                         |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.4 ms: 1.74x faster                                        |
| float          | 117 ms                                                 | 79.0 ms: 1.48x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.38x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.43x faster                                         |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                        |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.51 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.17x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                         |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.16x faster                                        |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.09x faster                                         |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                        |
| unpickle_list        | 5.20 us                                                | 5.36 us: 1.03x slower                                        |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                        |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                        |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                        |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                        |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.39x faster                                        |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                         |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                        |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                        |
| async_tree_io            | 1.77 sec                                               | 832 ms: 2.12x faster                                         |
| async_tree_none          | 728 ms                                                 | 349 ms: 2.08x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 437 ms: 1.99x faster                                         |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                        |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                         |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                         |
| pylint                   | 551 ms                                                 | 311 ms: 1.78x faster                                         |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                        |
| richards_super           | 94.7 ms                                                | 53.8 ms: 1.76x faster                                        |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                        |
| nbody                    | 154 ms                                                 | 88.4 ms: 1.74x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.71x faster                                        |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                         |
| richards                 | 79.3 ms                                                | 47.8 ms: 1.66x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                        |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                         |
| coroutines               | 35.1 ms                                                | 22.1 ms: 1.59x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                         |
| pyflate                  | 716 ms                                                 | 468 ms: 1.53x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.52x faster                                        |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                         |
| tornado_http             | 136 ms                                                 | 91.2 ms: 1.50x faster                                        |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                       |
| float                    | 117 ms                                                 | 79.0 ms: 1.48x faster                                        |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                        |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.46x faster                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.77 sec: 1.45x faster                                       |
| logging_format           | 9.09 us                                                | 6.29 us: 1.44x faster                                        |
| regex_compile            | 188 ms                                                 | 131 ms: 1.43x faster                                         |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                        |
| chameleon                | 9.68 ms                                                | 6.85 ms: 1.41x faster                                        |
| html5lib                 | 88.9 ms                                                | 63.1 ms: 1.41x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                        |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.39x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                       |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                         |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                         |
| dulwich_log              | 84.3 ms                                                | 63.2 ms: 1.33x faster                                        |
| deepcopy                 | 479 us                                                 | 360 us: 1.33x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                        |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                        |
| dask                     | 441 ms                                                 | 336 ms: 1.31x faster                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                        |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                        |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                        |
| aiohttp                  | 1.44 ms                                                | 1.13 ms: 1.28x faster                                        |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                         |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.26x faster                                         |
| gunicorn                 | 1.53 ms                                                | 1.22 ms: 1.25x faster                                        |
| unpack_sequence          | 60.0 ns                                                | 48.1 ns: 1.25x faster                                        |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                         |
| djangocms                | 38.4 us                                                | 31.3 us: 1.23x faster                                        |
| bench_thread_pool        | 986 us                                                 | 813 us: 1.21x faster                                         |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                        |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.16x faster                                        |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                         |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                        |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.09x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                        |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                       |
| regex_effbot             | 3.63 ms                                                | 3.51 ms: 1.03x faster                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| pickle_list              | 5.08 us                                                | 4.98 us: 1.02x faster                                        |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.63 ms: 1.01x slower                                        |
| unpickle_list            | 5.20 us                                                | 5.36 us: 1.03x slower                                        |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                        |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                        |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                        |
| flaskblogging            | 8.58 ms                                                | 9.13 ms: 1.06x slower                                        |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                        |
| telco                    | 7.27 ms                                                | 8.52 ms: 1.17x slower                                        |
| mypy2                    | 894 ms                                                 | 1.06 sec: 1.19x slower                                       |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                        |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-linux-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.394x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x