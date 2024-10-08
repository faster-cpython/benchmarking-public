# Results vs. 3.10.4

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.8 ms: 1.28x faster                                                   |
| tornado_http   | 178 ms                                                                | 125 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 423 ms: 2.25x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 557 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 108 ms: 1.54x faster                                                    |
| float          | 135 ms                                                                | 91.2 ms: 1.48x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 356 us: 1.49x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 78.3 ms: 1.27x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.8 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.45x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                                   |
| async_tree_none          | 950 ms                                                                | 423 ms: 2.25x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.99 ms: 2.08x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 557 ms: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| generators               | 68.1 ms                                                               | 35.0 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 303 ms: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                   |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.69x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 564 ms: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.66x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.62x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.5 ms: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.02 ms: 1.55x faster                                                   |
| nbody                    | 166 ms                                                                | 108 ms: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 336 us: 1.52x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 356 us: 1.49x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| float                    | 135 ms                                                                | 91.2 ms: 1.48x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 554 ms: 1.44x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| tornado_http             | 178 ms                                                                | 125 ms: 1.42x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.61 us: 1.39x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| thrift                   | 1.26 ms                                                               | 921 us: 1.37x faster                                                    |
| go                       | 264 ms                                                                | 193 ms: 1.37x faster                                                    |
| pylint                   | 485 ms                                                                | 358 ms: 1.36x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 67.8 ms: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.3 ms: 1.27x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.87 sec: 1.26x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 909 ms: 1.26x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.3 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 458 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.49 ms: 1.17x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 59.8 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.37 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.66 ms: 1.04x faster                                                   |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.77 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.4 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.91 ms: 1.18x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.14x