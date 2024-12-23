# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.076x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 477 ms: 1.25x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.78 sec: 1.07x slower                                                   |
| html5lib       | 86.5 ms                                                               | 109 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_none         | 950 ms                                                                | 542 ms: 1.75x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 678 ms: 1.67x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 852 ms: 1.49x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.70x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 188 ms: 1.13x slower                                                     |
| float          | 135 ms                                                                | 159 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 191 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 135 ms: 1.15x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.57 sec: 1.06x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 111 ms: 1.12x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 143 ms: 1.17x slower                                                     |
| json_loads           | 30.9 us                                                               | 37.4 us: 1.21x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 472 us: 1.29x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 692 us: 1.31x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.5 ms: 1.82x slower                                                    |
| python_startup         | 11.2 ms                                                               | 21.4 ms: 1.91x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.86x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 42.2 ms: 1.20x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 83.9 ms: 1.20x slower                                                    |
| django_template | 53.3 ms                                                               | 67.4 ms: 1.26x slower                                                    |
| mako            | 18.9 ms                                                               | 25.6 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.25x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 284 us: 2.33x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_none          | 950 ms                                                                | 542 ms: 1.75x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 678 ms: 1.67x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 852 ms: 1.49x faster                                                     |
| spectral_norm            | 186 ms                                                                | 157 ms: 1.19x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| deepcopy                 | 511 us                                                                | 435 us: 1.17x faster                                                     |
| generators               | 68.1 ms                                                               | 58.1 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 135 ms: 1.15x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 122 ms: 1.10x faster                                                     |
| pylint                   | 485 ms                                                                | 446 ms: 1.09x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 24.2 ms: 1.09x faster                                                    |
| coroutines               | 37.2 ms                                                               | 34.6 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 57.8 us: 1.07x faster                                                    |
| scimark_lu               | 227 ms                                                                | 218 ms: 1.04x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.74 sec: 1.03x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 687 ms: 1.05x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.81 us: 1.05x slower                                                    |
| richards                 | 91.7 ms                                                               | 96.0 ms: 1.05x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.57 sec: 1.06x slower                                                   |
| chaos                    | 121 ms                                                                | 129 ms: 1.07x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.78 sec: 1.07x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.35 ms: 1.07x slower                                                    |
| regex_compile            | 177 ms                                                                | 191 ms: 1.08x slower                                                     |
| json_dumps               | 16.7 ms                                                               | 18.2 ms: 1.09x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.05 sec: 1.10x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.38 ms: 1.10x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 111 ms: 1.12x slower                                                     |
| pyflate                  | 795 ms                                                                | 894 ms: 1.12x slower                                                     |
| nbody                    | 166 ms                                                                | 188 ms: 1.13x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 179 ms: 1.14x slower                                                     |
| scimark_sor              | 246 ms                                                                | 283 ms: 1.15x slower                                                     |
| nqueens                  | 117 ms                                                                | 135 ms: 1.15x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 84.9 ms: 1.15x slower                                                    |
| raytrace                 | 573 ms                                                                | 663 ms: 1.16x slower                                                     |
| logging_silent           | 222 ns                                                                | 258 ns: 1.16x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 87.9 ms: 1.17x slower                                                    |
| json                     | 5.88 ms                                                               | 6.85 ms: 1.17x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 143 ms: 1.17x slower                                                     |
| comprehensions           | 33.1 us                                                               | 38.8 us: 1.17x slower                                                    |
| logging_simple           | 9.78 us                                                               | 11.5 us: 1.17x slower                                                    |
| logging_format           | 10.6 us                                                               | 12.5 us: 1.18x slower                                                    |
| float                    | 135 ms                                                                | 159 ms: 1.18x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 13.0 ms: 1.19x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 42.2 ms: 1.20x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 83.9 ms: 1.20x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 154 ms: 1.20x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.4 us: 1.21x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.39 sec: 1.21x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.03 ms: 1.21x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.87 sec: 1.22x slower                                                   |
| deltablue                | 8.94 ms                                                               | 11.0 ms: 1.23x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 32.7 ms: 1.23x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 3.52 ms: 1.24x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.97 ms: 1.24x slower                                                    |
| 2to3                     | 381 ms                                                                | 477 ms: 1.25x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 248 ms: 1.26x slower                                                     |
| meteor_contest           | 126 ms                                                                | 159 ms: 1.26x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 109 ms: 1.26x slower                                                     |
| django_template          | 53.3 ms                                                               | 67.4 ms: 1.26x slower                                                    |
| go                       | 264 ms                                                                | 336 ms: 1.27x slower                                                     |
| fannkuch                 | 546 ms                                                                | 698 ms: 1.28x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.90 ms: 1.28x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 472 us: 1.29x slower                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 26.5 ms: 1.29x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.12 ms: 1.30x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 692 us: 1.31x slower                                                     |
| async_generators         | 452 ms                                                                | 606 ms: 1.34x slower                                                     |
| mako                     | 18.9 ms                                                               | 25.6 ms: 1.35x slower                                                    |
| sympy_str                | 329 ms                                                                | 468 ms: 1.42x slower                                                     |
| telco                    | 8.49 ms                                                               | 12.1 ms: 1.43x slower                                                    |
| sympy_sum                | 184 ms                                                                | 290 ms: 1.58x slower                                                     |
| sympy_expand             | 543 ms                                                                | 870 ms: 1.60x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.53 sec: 1.63x slower                                                   |
| coverage                 | 83.6 ms                                                               | 144 ms: 1.72x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.5 ms: 1.82x slower                                                    |
| python_startup           | 11.2 ms                                                               | 21.4 ms: 1.91x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 64.1 ms: 4.41x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (6): regex_effbot, richards_super, scimark_fft, regex_dna, pidigits, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.076x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.54x