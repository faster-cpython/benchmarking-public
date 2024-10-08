
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.34x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.30x faster                                       |
| chameleon      | 9.68 ms                                                | 7.07 ms: 1.37x faster                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| tornado_http   | 136 ms                                                 | 96.0 ms: 1.42x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 437 ms: 1.67x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 564 ms: 1.54x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.19 sec: 1.49x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 712 ms: 1.43x faster                                       |
| Geometric mean          | (ref)                                                  | 1.53x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.6 ms: 1.73x faster                                      |
| float          | 117 ms                                                 | 81.6 ms: 1.43x faster                                      |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                       |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                      |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                       |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 86.9 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.05 us: 1.03x faster                                      |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                      |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                      |
| Geometric mean       | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.1 ms: 1.45x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 6.87 ms: 1.16x slower                                      |
| Geometric mean         | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 156 us: 3.50x faster                                       |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                      |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                       |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                      |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                       |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 71.8 ms: 1.78x faster                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                       |
| nbody                    | 154 ms                                                 | 88.6 ms: 1.73x faster                                      |
| richards_super           | 94.7 ms                                                | 55.0 ms: 1.72x faster                                      |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 69.5 ms: 1.70x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                      |
| async_tree_none          | 728 ms                                                 | 437 ms: 1.67x faster                                       |
| richards                 | 79.3 ms                                                | 48.6 ms: 1.63x faster                                      |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                      |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 564 ms: 1.54x faster                                       |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                       |
| pyflate                  | 716 ms                                                 | 473 ms: 1.51x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 38.7 us: 1.51x faster                                      |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                     |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                     |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |
| python_startup           | 14.6 ms                                                | 10.1 ms: 1.45x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                     |
| float                    | 117 ms                                                 | 81.6 ms: 1.43x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 712 ms: 1.43x faster                                       |
| tornado_http             | 136 ms                                                 | 96.0 ms: 1.42x faster                                      |
| logging_simple           | 8.30 us                                                | 5.90 us: 1.41x faster                                      |
| logging_format           | 9.09 us                                                | 6.47 us: 1.41x faster                                      |
| comprehensions           | 28.8 us                                                | 20.8 us: 1.38x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                     |
| chameleon                | 9.68 ms                                                | 7.07 ms: 1.37x faster                                      |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                       |
| deepcopy                 | 479 us                                                 | 353 us: 1.36x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.14 us: 1.33x faster                                      |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                      |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                     |
| 2to3                     | 348 ms                                                 | 269 ms: 1.30x faster                                       |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                      |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                       |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                       |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                      |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                       |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                       |
| bench_thread_pool        | 986 us                                                 | 815 us: 1.21x faster                                       |
| unpack_sequence          | 60.0 ns                                                | 51.0 ns: 1.18x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 86.9 ms: 1.14x faster                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                      |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                      |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.48 ms: 1.10x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                      |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| pathlib                  | 20.5 ms                                                | 19.4 ms: 1.06x faster                                      |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                     |
| unpickle_list            | 5.20 us                                                | 5.05 us: 1.03x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                       |
| pickle_list              | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                       |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                       |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                      |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                      |
| telco                    | 7.27 ms                                                | 8.17 ms: 1.12x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 6.87 ms: 1.16x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                      |
| coverage                 | 79.4 ms                                                | 94.4 ms: 1.19x slower                                      |
| Geometric mean           | (ref)                                                  | 1.34x faster                                               |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x


# Memory

- memory change: 1.05x