# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.160x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 405 ms: 1.06x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                   |
| html5lib       | 86.5 ms                                                               | 76.8 ms: 1.13x faster                                                    |
| tornado_http   | 178 ms                                                                | 150 ms: 1.19x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 630 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 777 ms: 1.64x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.83x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| float          | 135 ms                                                                | 95.8 ms: 1.41x faster                                                    |
| pidigits       | 235 ms                                                                | 249 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.09 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 403 us: 1.31x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 279 us: 1.31x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.9 ms: 1.22x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.16x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| genshi_text    | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                    |
| genshi_xml     | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 228 us: 2.90x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.28 ms: 2.09x faster                                                    |
| async_tree_none          | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 630 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 777 ms: 1.64x faster                                                     |
| logging_silent           | 222 ns                                                                | 138 ns: 1.60x faster                                                     |
| raytrace                 | 573 ms                                                                | 362 ms: 1.58x faster                                                     |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                                     |
| richards_super           | 107 ms                                                                | 71.2 ms: 1.51x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 42.1 us: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.2 ms: 1.47x faster                                                    |
| richards                 | 91.7 ms                                                               | 63.6 ms: 1.44x faster                                                    |
| chaos                    | 121 ms                                                                | 84.3 ms: 1.44x faster                                                    |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 93.6 ms: 1.43x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.70 ms: 1.41x faster                                                    |
| go                       | 264 ms                                                                | 187 ms: 1.41x faster                                                     |
| float                    | 135 ms                                                                | 95.8 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| generators               | 68.1 ms                                                               | 49.2 ms: 1.38x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 403 us: 1.31x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 279 us: 1.31x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.6 us: 1.30x faster                                                    |
| deepcopy                 | 511 us                                                                | 395 us: 1.29x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.22 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| pyflate                  | 795 ms                                                                | 627 ms: 1.27x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.45 us: 1.25x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.24x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.95 us: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.9 ms: 1.22x faster                                                    |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                     |
| tornado_http             | 178 ms                                                                | 150 ms: 1.19x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.15x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 76.8 ms: 1.13x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.4 ms: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.11 us: 1.12x faster                                                    |
| scimark_fft              | 500 ms                                                                | 450 ms: 1.11x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.97 ms: 1.09x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| fannkuch                 | 546 ms                                                                | 505 ms: 1.08x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 19.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.59 sec: 1.03x faster                                                   |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 677 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| pidigits                 | 235 ms                                                                | 249 ms: 1.06x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                   |
| 2to3                     | 381 ms                                                                | 405 ms: 1.06x slower                                                     |
| nqueens                  | 117 ms                                                                | 126 ms: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 80.4 ms: 1.09x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                   |
| sympy_str                | 329 ms                                                                | 368 ms: 1.12x slower                                                     |
| sympy_expand             | 543 ms                                                                | 613 ms: 1.13x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 85.3 ms: 1.13x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 537 ms: 1.19x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 31.6 ms: 1.19x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 5.09 ms: 1.20x slower                                                    |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                     |
| sympy_sum                | 184 ms                                                                | 225 ms: 1.22x slower                                                     |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.72 ms: 1.62x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.85 ms: 1.70x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.63 sec: 112.27x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (9): scimark_sparse_mat_mult, django_template, sqlite_synth, regex_compile, regex_v8, sqlglot_normalize, meteor_contest, sqlalchemy_declarative, pylint
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.160x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x