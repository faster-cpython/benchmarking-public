# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.159x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 398 ms: 1.04x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.76 sec: 1.07x slower                                                   |
| html5lib       | 86.5 ms                                                               | 74.6 ms: 1.16x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 471 ms: 2.02x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 618 ms: 1.83x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 773 ms: 1.65x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.85x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| float          | 135 ms                                                                | 96.2 ms: 1.40x faster                                                    |
| pidigits       | 235 ms                                                                | 249 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 183 ms: 1.04x slower                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.08 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 273 us: 1.34x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 422 us: 1.25x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 82.3 ms: 1.21x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.07x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.14 ms: 1.33x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| django_template | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 81.4 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 224 us: 2.95x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.38 ms: 2.04x faster                                                    |
| async_tree_none          | 950 ms                                                                | 471 ms: 2.02x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 618 ms: 1.83x faster                                                     |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 773 ms: 1.65x faster                                                     |
| raytrace                 | 573 ms                                                                | 362 ms: 1.58x faster                                                     |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| richards_super           | 107 ms                                                                | 69.9 ms: 1.54x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 87.8 ms: 1.53x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 40.7 us: 1.52x faster                                                    |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.66 ms: 1.45x faster                                                    |
| richards                 | 91.7 ms                                                               | 63.3 ms: 1.45x faster                                                    |
| chaos                    | 121 ms                                                                | 83.8 ms: 1.44x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 89.4 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| go                       | 264 ms                                                                | 187 ms: 1.41x faster                                                     |
| nbody                    | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| float                    | 135 ms                                                                | 96.2 ms: 1.40x faster                                                    |
| generators               | 68.1 ms                                                               | 49.3 ms: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 273 us: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.8 us: 1.34x faster                                                    |
| pyflate                  | 795 ms                                                                | 609 ms: 1.31x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.18 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 984 us: 1.28x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.44 us: 1.26x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.79 us: 1.26x faster                                                    |
| spectral_norm            | 186 ms                                                                | 149 ms: 1.25x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 422 us: 1.25x faster                                                     |
| deepcopy                 | 511 us                                                                | 412 us: 1.24x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.3 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 74.6 ms: 1.16x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.14x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.50 sec: 1.13x faster                                                   |
| scimark_fft              | 500 ms                                                                | 449 ms: 1.11x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.16 us: 1.11x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.08x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.07x faster                                                     |
| fannkuch                 | 546 ms                                                                | 513 ms: 1.06x faster                                                     |
| django_template          | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.58 sec: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 677 ms: 1.03x slower                                                     |
| regex_compile            | 177 ms                                                                | 183 ms: 1.04x slower                                                     |
| 2to3                     | 381 ms                                                                | 398 ms: 1.04x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| pidigits                 | 235 ms                                                                | 249 ms: 1.06x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.76 sec: 1.07x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 167 ms: 1.07x slower                                                     |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 29.3 ms: 1.10x slower                                                    |
| sympy_str                | 329 ms                                                                | 363 ms: 1.10x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 83.6 ms: 1.11x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.63 sec: 1.11x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 82.2 ms: 1.12x slower                                                    |
| sympy_expand             | 543 ms                                                                | 616 ms: 1.13x slower                                                     |
| sympy_sum                | 184 ms                                                                | 212 ms: 1.16x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.88 ms: 1.16x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 81.4 ms: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 532 ms: 1.18x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.08 ms: 1.20x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.21x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.14 ms: 1.33x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.42 ms: 1.55x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.91 sec: 131.33x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (11): genshi_text, scimark_sparse_mat_mult, json, xml_etree_iterparse, sqlite_synth, regex_dna, sqlalchemy_declarative, sqlalchemy_imperative, meteor_contest, regex_v8, pylint
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.159x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.38x