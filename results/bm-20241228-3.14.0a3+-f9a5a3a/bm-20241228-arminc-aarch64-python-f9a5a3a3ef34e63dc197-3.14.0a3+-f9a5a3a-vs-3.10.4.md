# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.4 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 929 ms: 2.46x faster                                                     |
| async_tree_none         | 950 ms                                                                | 407 ms: 2.34x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 519 ms: 2.19x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 694 ms: 1.83x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.0 ms: 1.42x faster                                                    |
| nbody          | 166 ms                                                                | 126 ms: 1.31x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 131 ms: 1.35x faster                                                     |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 274 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 83.5 ms: 1.19x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.4 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                    |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 64.5 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 202 us: 3.28x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 929 ms: 2.46x faster                                                     |
| async_tree_none          | 950 ms                                                                | 407 ms: 2.34x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.98 ms: 2.25x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 519 ms: 2.19x faster                                                     |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 694 ms: 1.83x faster                                                     |
| go                       | 264 ms                                                                | 145 ms: 1.83x faster                                                     |
| raytrace                 | 573 ms                                                                | 321 ms: 1.78x faster                                                     |
| richards_super           | 107 ms                                                                | 60.6 ms: 1.77x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.6 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 72.8 ms: 1.66x faster                                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.64x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.48 ms: 1.63x faster                                                    |
| logging_silent           | 222 ns                                                                | 141 ns: 1.58x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 85.2 ms: 1.57x faster                                                    |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.86 ms: 1.53x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.1 ms: 1.50x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.1 us: 1.50x faster                                                    |
| pylint                   | 485 ms                                                                | 325 ms: 1.49x faster                                                     |
| deepcopy                 | 511 us                                                                | 344 us: 1.48x faster                                                     |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.57 ms: 1.44x faster                                                    |
| float                    | 135 ms                                                                | 95.0 ms: 1.42x faster                                                    |
| spectral_norm            | 186 ms                                                                | 133 ms: 1.40x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.22 us: 1.35x faster                                                    |
| regex_compile            | 177 ms                                                                | 131 ms: 1.35x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.89 us: 1.34x faster                                                    |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 274 us: 1.33x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.4 ms: 1.32x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| nbody                    | 166 ms                                                                | 126 ms: 1.31x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                   |
| thrift                   | 1.26 ms                                                               | 983 us: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.67 us: 1.25x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.16 ms: 1.24x faster                                                    |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.2 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.5 ms: 1.19x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 64.4 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 429 ms: 1.17x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.03 sec: 1.16x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 996 ms: 1.15x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 63.9 ms: 1.15x faster                                                    |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                     |
| sympy_expand             | 543 ms                                                                | 482 ms: 1.12x faster                                                     |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.41 sec: 1.09x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 64.5 ms: 1.08x faster                                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.66 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                     |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.4 us: 1.08x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.06 sec: 1.13x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.65 ms: 1.14x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.90 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.30 sec: 433.78x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (4): regex_effbot, sqlite_synth, pidigits, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x