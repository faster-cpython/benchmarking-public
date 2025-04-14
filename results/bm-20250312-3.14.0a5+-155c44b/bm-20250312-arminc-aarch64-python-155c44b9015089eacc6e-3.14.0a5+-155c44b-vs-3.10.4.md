# Results vs. 3.10.4

- fork: python
- ref: 155c44b9015089eacc6e
- machine: linux-aarch64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 879 ms: 2.60x faster                                                     |
| async_tree_none         | 950 ms                                                                | 379 ms: 2.51x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 467 ms: 2.43x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 653 ms: 1.95x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.1 ms: 1.55x faster                                                    |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 29.0 ms: 1.11x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.87 ms: 1.10x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 175 ms: 1.21x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.35x faster                                                    |
| django_template | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.30x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 59.9 ms: 1.17x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.43x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 879 ms: 2.60x faster                                                     |
| async_tree_none          | 950 ms                                                                | 379 ms: 2.51x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 467 ms: 2.43x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.27x faster                                                    |
| go                       | 264 ms                                                                | 135 ms: 1.96x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 653 ms: 1.95x faster                                                     |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                    |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                    |
| raytrace                 | 573 ms                                                                | 319 ms: 1.80x faster                                                     |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.65x faster                                                    |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                                     |
| richards                 | 91.7 ms                                                               | 56.7 ms: 1.62x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.9 us: 1.58x faster                                                    |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                     |
| float                    | 135 ms                                                                | 87.1 ms: 1.55x faster                                                    |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                                    |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 88.3 ms: 1.52x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.21 ms: 1.51x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                     |
| pyflate                  | 795 ms                                                                | 547 ms: 1.45x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 51.7 ms: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.97 us: 1.40x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.35x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                   |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.44 us: 1.34x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.4 ms: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 956 us: 1.32x faster                                                     |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                    |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                     |
| 2to3                     | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.30x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 938 ms: 1.22x faster                                                     |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                     |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 175 ms: 1.21x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.50 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 59.9 ms: 1.17x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 29.0 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.87 ms: 1.10x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.38 sec: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                    |
| async_generators         | 452 ms                                                                | 434 ms: 1.04x faster                                                     |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.63 ms: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.72 ms: 1.62x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.66 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.91 sec: 269.15x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                             |

Benchmark hidden because not significant (3): json, asyncio_websockets, pidigits
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x