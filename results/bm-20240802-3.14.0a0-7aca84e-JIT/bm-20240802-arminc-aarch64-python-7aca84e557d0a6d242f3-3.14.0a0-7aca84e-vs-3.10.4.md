# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 367 ms: 1.04x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.6 ms: 1.23x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 435 ms: 2.18x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 574 ms: 1.97x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 744 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.94x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.3 ms: 1.48x faster                                                   |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| regex_compile  | 177 ms                                                                | 174 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 32.9 ms: 1.07x faster                                                   |
| django_template | 53.3 ms                                                               | 52.1 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 72.7 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.11x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 213 us: 3.10x faster                                                    |
| async_tree_none          | 950 ms                                                                | 435 ms: 2.18x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.44 ms: 2.01x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 574 ms: 1.97x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 8.23 ms: 1.77x faster                                                   |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                   |
| raytrace                 | 573 ms                                                                | 332 ms: 1.73x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 744 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.9 ms: 1.67x faster                                                   |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                    |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.4 us: 1.61x faster                                                   |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 90.2 ms: 1.49x faster                                                   |
| float                    | 135 ms                                                                | 91.3 ms: 1.48x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 641 ms: 1.47x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.65 ms: 1.46x faster                                                   |
| go                       | 264 ms                                                                | 182 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.44x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 89.1 ms: 1.44x faster                                                   |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| chaos                    | 121 ms                                                                | 87.7 ms: 1.38x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.1 us: 1.37x faster                                                   |
| deepcopy                 | 511 us                                                                | 376 us: 1.36x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.11 ms: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.35 us: 1.33x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.00 us: 1.33x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| pyflate                  | 795 ms                                                                | 612 ms: 1.30x faster                                                    |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 979 us: 1.29x faster                                                    |
| tornado_http             | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.6 ms: 1.23x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                                   |
| generators               | 68.1 ms                                                               | 57.3 ms: 1.19x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.24 ms: 1.18x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                                  |
| dask                     | 450 ms                                                                | 391 ms: 1.15x faster                                                    |
| fannkuch                 | 546 ms                                                                | 481 ms: 1.14x faster                                                    |
| pylint                   | 485 ms                                                                | 429 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.90 ms: 1.10x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.22 us: 1.09x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 32.9 ms: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.06x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| scimark_fft              | 500 ms                                                                | 476 ms: 1.05x faster                                                    |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 72.5 ms: 1.04x faster                                                   |
| 2to3                     | 381 ms                                                                | 367 ms: 1.04x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| django_template          | 53.3 ms                                                               | 52.1 ms: 1.02x faster                                                   |
| regex_compile            | 177 ms                                                                | 174 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.39 sec: 1.02x slower                                                  |
| sympy_integrate          | 26.5 ms                                                               | 27.5 ms: 1.04x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 72.7 ms: 1.04x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 123 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| sympy_str                | 329 ms                                                                | 350 ms: 1.06x slower                                                    |
| sympy_expand             | 543 ms                                                                | 589 ms: 1.09x slower                                                    |
| sympy_sum                | 184 ms                                                                | 201 ms: 1.09x slower                                                    |
| async_generators         | 452 ms                                                                | 506 ms: 1.12x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.3 ms: 1.18x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.91 ms: 1.18x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.25x