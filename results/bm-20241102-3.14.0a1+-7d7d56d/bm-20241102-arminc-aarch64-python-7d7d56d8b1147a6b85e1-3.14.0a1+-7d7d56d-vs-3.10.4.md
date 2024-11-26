# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                    |
| tornado_http   | 178 ms                                                                | 128 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 457 ms: 2.08x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 611 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 763 ms: 1.67x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| float          | 135 ms                                                                | 99.9 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 132 ms: 1.34x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.11 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 381 us: 1.39x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.74 sec: 1.23x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 84.7 ms: 1.18x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.12x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 195 ms: 1.09x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.95 ms: 1.30x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| django_template | 53.3 ms                                                               | 43.6 ms: 1.22x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 63.9 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.21x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.18x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.11 ms: 2.17x faster                                                    |
| async_tree_none          | 950 ms                                                                | 457 ms: 2.08x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                                   |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 611 ms: 1.86x faster                                                     |
| go                       | 264 ms                                                                | 143 ms: 1.85x faster                                                     |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                     |
| chaos                    | 121 ms                                                                | 71.9 ms: 1.68x faster                                                    |
| richards_super           | 107 ms                                                                | 63.8 ms: 1.68x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 763 ms: 1.67x faster                                                     |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                     |
| richards                 | 91.7 ms                                                               | 56.1 ms: 1.63x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.48 ms: 1.63x faster                                                    |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 85.8 ms: 1.56x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 39.6 us: 1.56x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.55x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.85 ms: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.35 ms: 1.48x faster                                                    |
| scimark_sor              | 246 ms                                                                | 166 ms: 1.48x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 88.8 ms: 1.44x faster                                                    |
| deepcopy                 | 511 us                                                                | 355 us: 1.44x faster                                                     |
| tornado_http             | 178 ms                                                                | 128 ms: 1.39x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 381 us: 1.39x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 143 ms: 1.38x faster                                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.20 us: 1.36x faster                                                    |
| float                    | 135 ms                                                                | 99.9 ms: 1.35x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 362 ms: 1.34x faster                                                     |
| regex_compile            | 177 ms                                                                | 132 ms: 1.34x faster                                                     |
| pyflate                  | 795 ms                                                                | 605 ms: 1.31x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.13 us: 1.30x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 985 us: 1.28x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                                    |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.73 us: 1.23x faster                                                    |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.23x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.74 sec: 1.23x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.7 ms: 1.23x faster                                                    |
| django_template          | 53.3 ms                                                               | 43.6 ms: 1.22x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 963 ms: 1.19x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 61.9 ms: 1.19x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.18x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 84.7 ms: 1.18x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 134 ms: 1.17x faster                                                     |
| sympy_str                | 329 ms                                                                | 283 ms: 1.16x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 65.8 ms: 1.15x faster                                                    |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                     |
| fannkuch                 | 546 ms                                                                | 478 ms: 1.14x faster                                                     |
| sympy_expand             | 543 ms                                                                | 476 ms: 1.14x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.77 ms: 1.13x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                     |
| scimark_fft              | 500 ms                                                                | 457 ms: 1.09x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 63.9 ms: 1.09x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 195 ms: 1.09x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| async_generators         | 452 ms                                                                | 498 ms: 1.10x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.87 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.11 ms: 1.20x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.95 ms: 1.30x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.88 ms: 1.66x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.89 ms: 1.72x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.50 sec: 378.23x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                             |

Benchmark hidden because not significant (7): json, sqlite_synth, regex_dna, xml_etree_iterparse, asyncio_websockets, pidigits, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.283x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x