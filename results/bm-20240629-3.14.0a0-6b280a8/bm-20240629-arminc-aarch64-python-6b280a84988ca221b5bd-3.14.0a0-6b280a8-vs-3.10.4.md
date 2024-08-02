# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                   |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 441 ms: 2.16x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 359 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.82 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| django_template | 53.3 ms                                                               | 42.9 ms: 1.24x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                                   |
| async_tree_none          | 950 ms                                                                | 441 ms: 2.16x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 6.97 ms: 2.09x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                                    |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                   |
| generators               | 68.1 ms                                                               | 38.1 ms: 1.79x faster                                                   |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                                   |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.7 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 581 ms: 1.62x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.61x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                   |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                    |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.14 ms: 1.53x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 359 us: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.46x faster                                                  |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                   |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.69 us: 1.38x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| pyflate                  | 795 ms                                                                | 583 ms: 1.36x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.47 us: 1.32x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                  |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.25 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.25x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.9 ms: 1.24x faster                                                   |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| dask                     | 450 ms                                                                | 364 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 946 ms: 1.21x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.8 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| fannkuch                 | 546 ms                                                                | 456 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.9 ms: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.57 ms: 1.16x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.36 ms: 1.05x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.86 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.82 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x