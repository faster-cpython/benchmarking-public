# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 928 ms: 2.46x faster                                                     |
| async_tree_none         | 950 ms                                                                | 403 ms: 2.35x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 520 ms: 2.18x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 686 ms: 1.86x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.20x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 96.1 ms: 1.40x faster                                                    |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 385 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 83.2 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.97 ms: 1.30x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                    |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.21x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 928 ms: 2.46x faster                                                     |
| async_tree_none          | 950 ms                                                                | 403 ms: 2.35x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.02 ms: 2.22x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 520 ms: 2.18x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 686 ms: 1.86x faster                                                     |
| go                       | 264 ms                                                                | 144 ms: 1.83x faster                                                     |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.83x faster                                                    |
| richards_super           | 107 ms                                                                | 60.3 ms: 1.78x faster                                                    |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                     |
| chaos                    | 121 ms                                                                | 72.7 ms: 1.67x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.63x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.7 ms: 1.62x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 83.6 ms: 1.60x faster                                                    |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                                     |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| logging_silent           | 222 ns                                                                | 142 ns: 1.56x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.87 ms: 1.52x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.3 us: 1.49x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.7 ms: 1.49x faster                                                    |
| pylint                   | 485 ms                                                                | 326 ms: 1.49x faster                                                     |
| deepcopy                 | 511 us                                                                | 346 us: 1.48x faster                                                     |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.51 ms: 1.45x faster                                                    |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.41x faster                                                     |
| float                    | 135 ms                                                                | 96.1 ms: 1.40x faster                                                    |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 385 us: 1.37x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.17 us: 1.36x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                    |
| pyflate                  | 795 ms                                                                | 596 ms: 1.33x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.97 us: 1.33x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 149 ms: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                                     |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.61 us: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                     |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.20 ms: 1.23x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 83.2 ms: 1.20x faster                                                    |
| sympy_str                | 329 ms                                                                | 275 ms: 1.19x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.4 ms: 1.19x faster                                                    |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 62.3 ms: 1.18x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 974 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.02 sec: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 66.4 ms: 1.14x faster                                                    |
| sympy_expand             | 543 ms                                                                | 481 ms: 1.13x faster                                                     |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                     |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| async_generators         | 452 ms                                                                | 496 ms: 1.10x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.04 sec: 1.11x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.52 ms: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.97 ms: 1.30x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.56 ms: 1.58x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.92 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.45 sec: 375.29x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (8): genshi_xml, regex_effbot, sqlite_synth, json, regex_v8, xml_etree_generate, pidigits, regex_dna
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.299x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.30x