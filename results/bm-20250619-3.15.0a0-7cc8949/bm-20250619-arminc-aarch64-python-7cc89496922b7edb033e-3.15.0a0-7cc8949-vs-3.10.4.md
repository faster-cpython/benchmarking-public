# Results vs. 3.10.4

- fork: python
- ref: 7cc89496922b7edb033e
- machine: linux-aarch64
- commit hash: 7cc8949
- commit date: 2025-06-19
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 62.8 ms: 1.38x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 894 ms: 2.56x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 463 ms: 2.45x faster                                                    |
| async_tree_none         | 950 ms                                                                | 389 ms: 2.44x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 654 ms: 1.95x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.1 ms: 1.56x faster                                                   |
| nbody          | 166 ms                                                                | 120 ms: 1.39x faster                                                    |
| pidigits       | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.9 ms: 1.20x faster                                                   |
| regex_dna      | 257 ms                                                                | 219 ms: 1.18x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                   |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.31x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 894 ms: 2.56x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 463 ms: 2.45x faster                                                    |
| async_tree_none          | 950 ms                                                                | 389 ms: 2.44x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                                  |
| go                       | 264 ms                                                                | 129 ms: 2.04x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 654 ms: 1.95x faster                                                    |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.83x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                                   |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                   |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.6 ms: 1.65x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 83.5 ms: 1.60x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.9 ms: 1.58x faster                                                   |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                    |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                    |
| float                    | 135 ms                                                                | 86.1 ms: 1.56x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.07 ms: 1.54x faster                                                   |
| pylint                   | 485 ms                                                                | 317 ms: 1.53x faster                                                    |
| pyflate                  | 795 ms                                                                | 522 ms: 1.52x faster                                                    |
| scimark_lu               | 227 ms                                                                | 155 ms: 1.46x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                    |
| nbody                    | 166 ms                                                                | 120 ms: 1.39x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 62.8 ms: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 54.2 ms: 1.36x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 943 us: 1.34x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.56 us: 1.29x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.28x faster                                                   |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.30 us: 1.28x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                    |
| sympy_sum                | 184 ms                                                                | 153 ms: 1.21x faster                                                    |
| nqueens                  | 117 ms                                                                | 97.6 ms: 1.20x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 26.9 ms: 1.20x faster                                                   |
| scimark_fft              | 500 ms                                                                | 421 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                   |
| regex_dna                | 257 ms                                                                | 219 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                                    |
| meteor_contest           | 126 ms                                                                | 109 ms: 1.16x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.01 sec: 1.14x faster                                                  |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.08 sec: 1.13x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.85 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                   |
| pidigits                 | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.44 ms: 1.11x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.97 ms: 1.68x slower                                                   |
| logging_silent           | 222 ns                                                                | 627 ns: 2.82x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (2): json, async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-7cc8949/bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.36x