# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.268x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 323 ms: 1.18x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.19 sec: 1.10x faster                                                   |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 936 ms: 2.44x faster                                                     |
| async_tree_none         | 950 ms                                                                | 400 ms: 2.38x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 689 ms: 1.85x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.3 ms: 1.53x faster                                                    |
| nbody          | 166 ms                                                                | 130 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 135 ms: 1.31x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.97 ms: 1.07x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 404 us: 1.31x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 291 us: 1.26x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| unpickle             | 17.5 us                                                               | 18.5 us: 1.06x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.5 us: 1.13x slower                                                    |
| json_loads           | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| pickle               | 12.5 us                                                               | 15.7 us: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 64.5 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.25x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 219 us: 3.02x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 936 ms: 2.44x faster                                                     |
| async_tree_none          | 950 ms                                                                | 400 ms: 2.38x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.27 ms: 2.09x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 689 ms: 1.85x faster                                                     |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.82x faster                                                    |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                    |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 71.5 ms: 1.69x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 567 ms: 1.67x faster                                                     |
| scimark_sor              | 246 ms                                                                | 153 ms: 1.61x faster                                                     |
| go                       | 264 ms                                                                | 165 ms: 1.61x faster                                                     |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                     |
| logging_silent           | 222 ns                                                                | 142 ns: 1.57x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.7 us: 1.55x faster                                                    |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.55x faster                                                     |
| float                    | 135 ms                                                                | 88.3 ms: 1.53x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.61 ms: 1.50x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.93 ms: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.9 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                   |
| pylint                   | 485 ms                                                                | 338 ms: 1.43x faster                                                     |
| deepcopy                 | 511 us                                                                | 359 us: 1.42x faster                                                     |
| pyflate                  | 795 ms                                                                | 584 ms: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.8 us: 1.34x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.32x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.45 us: 1.31x faster                                                    |
| regex_compile            | 177 ms                                                                | 135 ms: 1.31x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 404 us: 1.31x faster                                                     |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.12 us: 1.31x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.41 ms: 1.30x faster                                                    |
| nbody                    | 166 ms                                                                | 130 ms: 1.28x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.26x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 291 us: 1.26x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.23x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                    |
| sympy_sum                | 184 ms                                                                | 155 ms: 1.19x faster                                                     |
| 2to3                     | 381 ms                                                                | 323 ms: 1.18x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.6 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                                   |
| sympy_str                | 329 ms                                                                | 287 ms: 1.14x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 64.7 ms: 1.14x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.13x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 67.8 ms: 1.11x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.19 sec: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.00 ms: 1.09x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 64.5 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.97 ms: 1.07x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.06x faster                                                     |
| sympy_expand             | 543 ms                                                                | 511 ms: 1.06x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.95 us: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                                     |
| unpickle                 | 17.5 us                                                               | 18.5 us: 1.06x slower                                                    |
| async_generators         | 452 ms                                                                | 491 ms: 1.09x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.11x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 39.5 us: 1.13x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.66 sec: 1.13x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.89 ms: 1.16x slower                                                    |
| json_loads               | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.26x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.58 ms: 1.58x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.96 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.23 sec: 153.16x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.16x faster                                                             |

Benchmark hidden because not significant (7): nqueens, unpickle_list, fannkuch, meteor_contest, json, pidigits, regex_dna
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.268x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.32x