# Results vs. 3.10.4

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-aarch64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.2 ms: 1.31x faster                                                   |
| tornado_http   | 178 ms                                                                | 128 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 420 ms: 2.26x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 551 ms: 2.06x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.04x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                   |
| django_template | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| async_tree_none          | 950 ms                                                                | 420 ms: 2.26x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 551 ms: 2.06x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.08 ms: 2.05x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| generators               | 68.1 ms                                                               | 35.0 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.4 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 132 ns: 1.69x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 560 ms: 1.68x faster                                                    |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.9 ms: 1.62x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.8 ms: 1.54x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.16 ms: 1.52x faster                                                   |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                                    |
| float                    | 135 ms                                                                | 91.6 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| pyflate                  | 795 ms                                                                | 563 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.95 us: 1.41x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| tornado_http             | 178 ms                                                                | 128 ms: 1.39x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                                   |
| go                       | 264 ms                                                                | 193 ms: 1.37x faster                                                    |
| thrift                   | 1.26 ms                                                               | 927 us: 1.36x faster                                                    |
| pylint                   | 485 ms                                                                | 358 ms: 1.36x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.31x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 66.2 ms: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 20.8 ms: 1.26x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 918 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.43 ms: 1.19x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.28 ms: 1.01x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.68 ms: 1.14x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.83 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-fe85a82/bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x