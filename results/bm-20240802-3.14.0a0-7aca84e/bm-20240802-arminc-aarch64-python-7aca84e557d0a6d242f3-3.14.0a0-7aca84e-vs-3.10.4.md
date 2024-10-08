# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 434 ms: 2.19x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.10 sec: 2.09x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 552 ms: 2.05x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 728 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.4 ms: 1.19x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| django_template | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.81 ms: 2.35x faster                                                   |
| async_tree_none          | 950 ms                                                                | 434 ms: 2.19x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.10 sec: 2.09x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 552 ms: 2.05x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.11 ms: 2.05x faster                                                   |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| raytrace                 | 573 ms                                                                | 294 ms: 1.95x faster                                                    |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                   |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                   |
| richards                 | 91.7 ms                                                               | 51.9 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 728 ms: 1.75x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 576 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.60x faster                                                   |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.5 ms: 1.57x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                                   |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                    |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.97 us: 1.40x faster                                                   |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| tornado_http             | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.73 us: 1.37x faster                                                   |
| pyflate                  | 795 ms                                                                | 582 ms: 1.37x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.38 us: 1.36x faster                                                   |
| pylint                   | 485 ms                                                                | 357 ms: 1.36x faster                                                    |
| spectral_norm            | 186 ms                                                                | 139 ms: 1.34x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| thrift                   | 1.26 ms                                                               | 979 us: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| dask                     | 450 ms                                                                | 362 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.23x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 61.5 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 941 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.33 ms: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.8 ms: 1.20x faster                                                   |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 467 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                   |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.86 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.0 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.4 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.98 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x