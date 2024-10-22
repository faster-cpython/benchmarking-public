# Results vs. 3.10.4

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-aarch64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.8 ms: 1.29x faster                                                   |
| tornado_http   | 178 ms                                                                | 125 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 443 ms: 2.14x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.12 sec: 2.05x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 734 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.49x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 198 us: 3.34x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.80 ms: 2.35x faster                                                   |
| async_tree_none          | 950 ms                                                                | 443 ms: 2.14x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.07 ms: 2.05x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.12 sec: 2.05x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.96x faster                                                   |
| raytrace                 | 573 ms                                                                | 295 ms: 1.94x faster                                                    |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                   |
| chaos                    | 121 ms                                                                | 67.7 ms: 1.79x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 734 ms: 1.73x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                    |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.67x faster                                                   |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.8 ms: 1.64x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 587 ms: 1.61x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.8 us: 1.59x faster                                                   |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                   |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.09 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.49x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                  |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.45x faster                                                    |
| tornado_http             | 178 ms                                                                | 125 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| pyflate                  | 795 ms                                                                | 562 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.05 us: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.68 us: 1.38x faster                                                   |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                                  |
| pylint                   | 485 ms                                                                | 354 ms: 1.37x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.37 us: 1.36x faster                                                   |
| thrift                   | 1.26 ms                                                               | 939 us: 1.34x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                  |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 66.8 ms: 1.29x faster                                                   |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.25 ms: 1.28x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 57.9 ms: 1.27x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| dask                     | 450 ms                                                                | 360 ms: 1.25x faster                                                    |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.23x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 936 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.9 ms: 1.22x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.1 ms: 1.21x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                   |
| fannkuch                 | 546 ms                                                                | 478 ms: 1.14x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 486 ms: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.54 ms: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.2 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.08 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (3): pidigits, regex_dna, asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x