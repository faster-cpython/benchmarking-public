# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 354 ms: 1.08x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| html5lib       | 86.5 ms                                                               | 70.4 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 863 ms: 2.65x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none         | 950 ms                                                                | 397 ms: 2.39x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 674 ms: 1.89x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 93.8 ms: 1.44x faster                                                   |
| nbody          | 166 ms                                                                | 182 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 26.2 ms: 1.23x faster                                                   |
| regex_compile  | 177 ms                                                                | 149 ms: 1.19x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.76 ms: 1.13x faster                                                   |
| regex_dna      | 257 ms                                                                | 240 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 301 us: 1.22x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 133 ms: 1.17x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 452 us: 1.17x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.89 sec: 1.16x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 100 ms: 1.01x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.60 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.9 us: 1.11x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 139 ms: 1.13x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.2 us: 1.16x slower                                                   |
| pickle               | 12.5 us                                                               | 15.0 us: 1.21x slower                                                   |
| json_loads           | 30.9 us                                                               | 37.6 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.76x slower                                                   |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 51.3 ms: 1.04x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                   |
| mako            | 18.9 ms                                                               | 21.3 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 244 us: 2.71x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 863 ms: 2.65x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none          | 950 ms                                                                | 397 ms: 2.39x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.93 sec: 1.91x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.74 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 674 ms: 1.89x faster                                                    |
| go                       | 264 ms                                                                | 154 ms: 1.71x faster                                                    |
| generators               | 68.1 ms                                                               | 40.3 ms: 1.69x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 573 ms: 1.65x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.58x faster                                                    |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                                    |
| chaos                    | 121 ms                                                                | 81.9 ms: 1.48x faster                                                   |
| raytrace                 | 573 ms                                                                | 394 ms: 1.45x faster                                                    |
| float                    | 135 ms                                                                | 93.8 ms: 1.44x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 2.92 ms: 1.42x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.81 ms: 1.40x faster                                                   |
| pyflate                  | 795 ms                                                                | 588 ms: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.34x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.45 sec: 1.34x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 46.1 us: 1.34x faster                                                   |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                    |
| richards_super           | 107 ms                                                                | 82.2 ms: 1.31x faster                                                   |
| richards                 | 91.7 ms                                                               | 70.8 ms: 1.29x faster                                                   |
| deepcopy                 | 511 us                                                                | 395 us: 1.29x faster                                                    |
| pylint                   | 485 ms                                                                | 385 ms: 1.26x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.26x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 107 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.3 ms: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.24x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 103 ms: 1.24x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.4 ms: 1.23x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.2 ms: 1.23x faster                                                   |
| logging_simple           | 9.78 us                                                               | 8.03 us: 1.22x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 301 us: 1.22x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.44 us: 1.20x faster                                                   |
| regex_compile            | 177 ms                                                                | 149 ms: 1.19x faster                                                    |
| coroutines               | 37.2 ms                                                               | 31.4 ms: 1.18x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 133 ms: 1.17x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 452 us: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.09 us: 1.17x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.89 sec: 1.16x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.76 ms: 1.13x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.5 ms: 1.12x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.04 sec: 1.10x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.14 sec: 1.10x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.27 us: 1.08x faster                                                   |
| 2to3                     | 381 ms                                                                | 354 ms: 1.08x faster                                                    |
| regex_dna                | 257 ms                                                                | 240 ms: 1.07x faster                                                    |
| scimark_fft              | 500 ms                                                                | 467 ms: 1.07x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.20 ms: 1.05x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.3 ms: 1.04x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 100 ms: 1.01x slower                                                    |
| sympy_sum                | 184 ms                                                                | 186 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| sympy_str                | 329 ms                                                                | 345 ms: 1.05x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.60 us: 1.07x slower                                                   |
| meteor_contest           | 126 ms                                                                | 136 ms: 1.08x slower                                                    |
| json                     | 5.88 ms                                                               | 6.36 ms: 1.08x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                   |
| sympy_expand             | 543 ms                                                                | 589 ms: 1.09x slower                                                    |
| fannkuch                 | 546 ms                                                                | 596 ms: 1.09x slower                                                    |
| nbody                    | 166 ms                                                                | 182 ms: 1.10x slower                                                    |
| async_generators         | 452 ms                                                                | 500 ms: 1.11x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.9 us: 1.11x slower                                                   |
| mako                     | 18.9 ms                                                               | 21.3 ms: 1.12x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 139 ms: 1.13x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.83 ms: 1.15x slower                                                   |
| unpickle                 | 17.5 us                                                               | 20.2 us: 1.16x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.21x slower                                                   |
| json_loads               | 30.9 us                                                               | 37.6 us: 1.22x slower                                                   |
| coverage                 | 83.6 ms                                                               | 143 ms: 1.71x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.76x slower                                                   |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 64.7 ms: 4.45x slower                                                   |
| telco                    | 8.49 ms                                                               | 189 ms: 22.21x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (7): sympy_integrate, pidigits, unpickle_list, create_gc_cycles, scimark_sparse_mat_mult, genshi_text, nqueens
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.141x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.67x