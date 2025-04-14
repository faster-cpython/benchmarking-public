# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.399x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                         |
| chameleon      | 9.68 ms                                                | 6.88 ms: 1.41x faster                                        |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                       |
| html5lib       | 88.9 ms                                                | 66.6 ms: 1.33x faster                                        |
| tornado_http   | 136 ms                                                 | 91.0 ms: 1.50x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 367 ms: 1.99x faster                                         |
| async_tree_io           | 1.77 sec                                               | 893 ms: 1.98x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 451 ms: 1.93x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 594 ms: 1.71x faster                                         |
| Geometric mean          | (ref)                                                  | 1.90x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.6 ms: 1.79x faster                                        |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.41x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                         |
| regex_v8       | 27.8 ms                                                | 26.3 ms: 1.06x faster                                        |
| regex_dna      | 227 ms                                                 | 237 ms: 1.05x slower                                         |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                         |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                        |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 88.0 ms: 1.13x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                         |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                        |
| django_template | 48.2 ms                                                | 33.6 ms: 1.44x faster                                        |
| genshi_text     | 31.8 ms                                                | 22.9 ms: 1.39x faster                                        |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                         |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                        |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                        |
| async_tree_none          | 728 ms                                                 | 367 ms: 1.99x faster                                         |
| async_tree_io            | 1.77 sec                                               | 893 ms: 1.98x faster                                         |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                        |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 451 ms: 1.93x faster                                         |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                         |
| nbody                    | 154 ms                                                 | 85.6 ms: 1.79x faster                                        |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                        |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.75x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.02 ms: 1.73x faster                                        |
| pylint                   | 551 ms                                                 | 322 ms: 1.71x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 594 ms: 1.71x faster                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                        |
| go                       | 240 ms                                                 | 142 ms: 1.70x faster                                         |
| richards                 | 79.3 ms                                                | 47.5 ms: 1.67x faster                                        |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.63x faster                                        |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                         |
| coroutines               | 35.1 ms                                                | 22.0 ms: 1.59x faster                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                         |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                        |
| pyflate                  | 716 ms                                                 | 477 ms: 1.50x faster                                         |
| tornado_http             | 136 ms                                                 | 91.0 ms: 1.50x faster                                        |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                       |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                         |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                        |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                        |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                        |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.44x faster                                        |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                       |
| chameleon                | 9.68 ms                                                | 6.88 ms: 1.41x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                       |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                        |
| genshi_text              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                        |
| deepcopy                 | 479 us                                                 | 354 us: 1.35x faster                                         |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                         |
| html5lib                 | 88.9 ms                                                | 66.6 ms: 1.33x faster                                        |
| dulwich_log              | 84.3 ms                                                | 63.2 ms: 1.33x faster                                        |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.16 us: 1.32x faster                                        |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                        |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                         |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                        |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 54.0 ms: 1.28x faster                                        |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                         |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                         |
| mypy2                    | 894 ms                                                 | 714 ms: 1.25x faster                                         |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                         |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                         |
| bench_thread_pool        | 986 us                                                 | 812 us: 1.21x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                        |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                       |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 88.0 ms: 1.13x faster                                        |
| json                     | 5.69 ms                                                | 5.04 ms: 1.13x faster                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                         |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                       |
| regex_v8                 | 27.8 ms                                                | 26.3 ms: 1.06x faster                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                         |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                         |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                        |
| regex_dna                | 227 ms                                                 | 237 ms: 1.05x slower                                         |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                        |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                        |
| telco                    | 7.27 ms                                                | 8.23 ms: 1.13x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.399x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x