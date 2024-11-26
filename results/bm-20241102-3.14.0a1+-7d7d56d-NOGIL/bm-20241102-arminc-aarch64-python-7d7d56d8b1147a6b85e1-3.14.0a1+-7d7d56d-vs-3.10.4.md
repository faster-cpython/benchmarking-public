# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.203x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 532 ms: 1.40x slower                                                     |
| docutils       | 3.53 sec                                                              | 4.17 sec: 1.18x slower                                                   |
| html5lib       | 86.5 ms                                                               | 120 ms: 1.38x slower                                                     |
| tornado_http   | 178 ms                                                                | 196 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.46 sec: 1.56x faster                                                   |
| async_tree_none         | 950 ms                                                                | 636 ms: 1.49x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 780 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 950 ms: 1.34x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 213 ms: 1.58x slower                                                     |
| nbody          | 166 ms                                                                | 295 ms: 1.78x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.43x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 268 ms: 1.04x slower                                                     |
| regex_v8       | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.63 ms: 1.09x slower                                                    |
| regex_compile  | 177 ms                                                                | 260 ms: 1.47x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.10x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 20.0 ms: 1.20x slower                                                    |
| json_loads           | 30.9 us                                                               | 39.1 us: 1.26x slower                                                    |
| tomli_loads          | 3.36 sec                                                              | 4.33 sec: 1.29x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 135 ms: 1.35x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 170 ms: 1.38x slower                                                     |
| unpickle_pure_python | 366 us                                                                | 566 us: 1.55x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 828 us: 1.56x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.26x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.8 ms: 1.86x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.82x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 54.0 ms: 1.54x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 109 ms: 1.56x slower                                                     |
| mako            | 18.9 ms                                                               | 29.7 ms: 1.57x slower                                                    |
| django_template | 53.3 ms                                                               | 85.1 ms: 1.60x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.57x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 338 us: 1.95x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.46 sec: 1.56x faster                                                   |
| async_tree_none          | 950 ms                                                                | 636 ms: 1.49x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 780 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 950 ms: 1.34x faster                                                     |
| generators               | 68.1 ms                                                               | 61.5 ms: 1.11x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.10x faster                                                     |
| regex_dna                | 257 ms                                                                | 268 ms: 1.04x slower                                                     |
| sqlite_synth             | 4.12 us                                                               | 4.34 us: 1.06x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 693 ms: 1.06x slower                                                     |
| regex_v8                 | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                    |
| pylint                   | 485 ms                                                                | 522 ms: 1.07x slower                                                     |
| crypto_pyaes             | 134 ms                                                                | 145 ms: 1.08x slower                                                     |
| deepcopy                 | 511 us                                                                | 551 us: 1.08x slower                                                     |
| coroutines               | 37.2 ms                                                               | 40.3 ms: 1.08x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.63 ms: 1.09x slower                                                    |
| tornado_http             | 178 ms                                                                | 196 ms: 1.10x slower                                                     |
| pathlib                  | 26.3 ms                                                               | 29.0 ms: 1.10x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 4.59 ms: 1.11x slower                                                    |
| json                     | 5.88 ms                                                               | 6.87 ms: 1.17x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.97 ms: 1.18x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.17 sec: 1.18x slower                                                   |
| scimark_fft              | 500 ms                                                                | 593 ms: 1.18x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.71 ms: 1.20x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 20.0 ms: 1.20x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.48 sec: 1.21x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 76.2 us: 1.24x slower                                                    |
| spectral_norm            | 186 ms                                                                | 231 ms: 1.24x slower                                                     |
| json_loads               | 30.9 us                                                               | 39.1 us: 1.26x slower                                                    |
| pycparser                | 1.69 sec                                                              | 2.14 sec: 1.26x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.03 ms: 1.28x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 4.33 sec: 1.29x slower                                                   |
| comprehensions           | 33.1 us                                                               | 42.9 us: 1.30x slower                                                    |
| richards_super           | 107 ms                                                                | 139 ms: 1.30x slower                                                     |
| logging_silent           | 222 ns                                                                | 290 ns: 1.31x slower                                                     |
| pyflate                  | 795 ms                                                                | 1.04 sec: 1.31x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 6.10 us: 1.33x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 97.7 ms: 1.33x slower                                                    |
| chaos                    | 121 ms                                                                | 161 ms: 1.33x slower                                                     |
| nqueens                  | 117 ms                                                                | 157 ms: 1.33x slower                                                     |
| richards                 | 91.7 ms                                                               | 124 ms: 1.35x slower                                                     |
| xml_etree_process        | 99.5 ms                                                               | 135 ms: 1.35x slower                                                     |
| meteor_contest           | 126 ms                                                                | 172 ms: 1.36x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 36.3 ms: 1.37x slower                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 271 ms: 1.37x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 120 ms: 1.38x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 170 ms: 1.38x slower                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 177 ms: 1.39x slower                                                     |
| 2to3                     | 381 ms                                                                | 532 ms: 1.40x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.79 ms: 1.42x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.8 ms: 1.43x slower                                                    |
| scimark_sor              | 246 ms                                                                | 359 ms: 1.46x slower                                                     |
| fannkuch                 | 546 ms                                                                | 797 ms: 1.46x slower                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 30.0 ms: 1.46x slower                                                    |
| regex_compile            | 177 ms                                                                | 260 ms: 1.47x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 16.1 ms: 1.48x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.5 us: 1.48x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 234 ms: 1.50x slower                                                     |
| async_generators         | 452 ms                                                                | 684 ms: 1.51x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 3.61 sec: 1.53x slower                                                   |
| scimark_lu               | 227 ms                                                                | 347 ms: 1.53x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 54.0 ms: 1.54x slower                                                    |
| telco                    | 8.49 ms                                                               | 13.0 ms: 1.54x slower                                                    |
| logging_format           | 10.6 us                                                               | 16.3 us: 1.54x slower                                                    |
| go                       | 264 ms                                                                | 407 ms: 1.54x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.77 sec: 1.54x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 566 us: 1.55x slower                                                     |
| raytrace                 | 573 ms                                                                | 891 ms: 1.55x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 109 ms: 1.56x slower                                                     |
| pickle_pure_python       | 529 us                                                                | 828 us: 1.56x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 118 ms: 1.57x slower                                                     |
| mako                     | 18.9 ms                                                               | 29.7 ms: 1.57x slower                                                    |
| float                    | 135 ms                                                                | 213 ms: 1.58x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.80 ms: 1.58x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.51 ms: 1.59x slower                                                    |
| django_template          | 53.3 ms                                                               | 85.1 ms: 1.60x slower                                                    |
| sympy_str                | 329 ms                                                                | 530 ms: 1.61x slower                                                     |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.70x slower                                                     |
| nbody                    | 166 ms                                                                | 295 ms: 1.78x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| sympy_sum                | 184 ms                                                                | 329 ms: 1.79x slower                                                     |
| sympy_expand             | 543 ms                                                                | 980 ms: 1.81x slower                                                     |
| python_startup           | 11.2 ms                                                               | 20.8 ms: 1.86x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 63.9 ms: 4.39x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.31x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.203x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.51x