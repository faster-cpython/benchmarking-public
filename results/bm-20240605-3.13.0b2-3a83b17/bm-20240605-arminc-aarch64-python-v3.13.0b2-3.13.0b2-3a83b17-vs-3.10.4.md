# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.95 ms: 1.21x faster                                        |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                       |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                        |
| tornado_http   | 178 ms                                                                | 128 ms: 1.39x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 492 ms: 1.93x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 645 ms: 1.76x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 791 ms: 1.61x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.4 ms: 1.47x faster                                        |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                         |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                         |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                        |
| regex_effbot   | 4.25 ms                                                               | 4.98 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 359 us: 1.48x faster                                         |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.45x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                       |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| unpickle_list        | 6.99 us                                                               | 6.52 us: 1.07x faster                                        |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.27 us: 1.01x slower                                        |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| pickle               | 12.5 us                                                               | 13.4 us: 1.07x slower                                        |
| unpickle             | 17.5 us                                                               | 19.8 us: 1.13x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                        |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.31x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.03 ms: 2.07x faster                                        |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                         |
| async_tree_none          | 950 ms                                                                | 492 ms: 1.93x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                       |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.83x faster                                        |
| chaos                    | 121 ms                                                                | 68.3 ms: 1.77x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 645 ms: 1.76x faster                                         |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                        |
| logging_silent           | 222 ns                                                                | 133 ns: 1.66x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.66x faster                                        |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                         |
| richards                 | 91.7 ms                                                               | 55.9 ms: 1.64x faster                                        |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.64x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 584 ms: 1.62x faster                                         |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.61x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 791 ms: 1.61x faster                                         |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.60x faster                                         |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                        |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                         |
| hexiom                   | 10.9 ms                                                               | 7.08 ms: 1.54x faster                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                       |
| pickle_pure_python       | 529 us                                                                | 359 us: 1.48x faster                                         |
| float                    | 135 ms                                                                | 91.4 ms: 1.47x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.45x faster                                         |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                         |
| pylint                   | 485 ms                                                                | 337 ms: 1.44x faster                                         |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| pyflate                  | 795 ms                                                                | 557 ms: 1.43x faster                                         |
| tornado_http             | 178 ms                                                                | 128 ms: 1.39x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                       |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.21 us: 1.36x faster                                        |
| logging_format           | 10.6 us                                                               | 7.82 us: 1.36x faster                                        |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                         |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                         |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                        |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                        |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                         |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.27x faster                                        |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 58.5 ms: 1.26x faster                                        |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                         |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 933 ms: 1.23x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                       |
| gunicorn                 | 1.45 ms                                                               | 1.19 ms: 1.22x faster                                        |
| mypy2                    | 936 ms                                                                | 767 ms: 1.22x faster                                         |
| deepcopy_memo            | 61.7 us                                                               | 50.8 us: 1.22x faster                                        |
| dask                     | 450 ms                                                                | 370 ms: 1.21x faster                                         |
| chameleon                | 10.8 ms                                                               | 8.95 ms: 1.21x faster                                        |
| fannkuch                 | 546 ms                                                                | 451 ms: 1.21x faster                                         |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 62.6 ms: 1.20x faster                                        |
| nqueens                  | 117 ms                                                                | 98.9 ms: 1.19x faster                                        |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                         |
| aiohttp                  | 1.39 ms                                                               | 1.18 ms: 1.18x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.55 ms: 1.16x faster                                        |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                        |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                        |
| deepcopy                 | 511 us                                                                | 448 us: 1.14x faster                                         |
| deepcopy_reduce          | 4.60 us                                                               | 4.04 us: 1.14x faster                                        |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                       |
| scimark_fft              | 500 ms                                                                | 445 ms: 1.12x faster                                         |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                       |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| unpickle_list            | 6.99 us                                                               | 6.52 us: 1.07x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.05x faster                                        |
| json                     | 5.88 ms                                                               | 5.64 ms: 1.04x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                        |
| flaskblogging            | 4.83 ms                                                               | 4.70 ms: 1.03x faster                                        |
| pickle_list              | 5.24 us                                                               | 5.27 us: 1.01x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                        |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                        |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.07x slower                                        |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                         |
| unpickle                 | 17.5 us                                                               | 19.8 us: 1.13x slower                                        |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.98 ms: 1.17x slower                                        |
| coverage                 | 83.6 ms                                                               | 98.4 ms: 1.18x slower                                        |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 5.17 ms: 1.25x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                 |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, regex_dna
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x