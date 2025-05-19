# Results vs. 3.10.4

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: linux-aarch64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.221x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                  |
| html5lib       | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 888 ms: 2.57x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none         | 950 ms                                                                | 395 ms: 2.40x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.9 ms: 1.55x faster                                                   |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.9 ms: 1.15x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.81 ms: 1.12x faster                                                   |
| regex_dna      | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 35.2 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                   |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 202 us: 3.27x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 888 ms: 2.57x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_none          | 950 ms                                                                | 395 ms: 2.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.79 ms: 2.36x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.24x faster                                                  |
| go                       | 264 ms                                                                | 132 ms: 2.00x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                    |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.88x faster                                                   |
| richards_super           | 107 ms                                                                | 58.4 ms: 1.84x faster                                                   |
| richards                 | 91.7 ms                                                               | 51.9 ms: 1.77x faster                                                   |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                    |
| chaos                    | 121 ms                                                                | 69.9 ms: 1.73x faster                                                   |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.64x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.2 ms: 1.59x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.7 ms: 1.58x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.98 ms: 1.56x faster                                                   |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                   |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.56x faster                                                    |
| float                    | 135 ms                                                                | 86.9 ms: 1.55x faster                                                   |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                    |
| deepcopy                 | 511 us                                                                | 336 us: 1.52x faster                                                    |
| pyflate                  | 795 ms                                                                | 532 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 128 ms: 1.46x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 53.2 ms: 1.38x faster                                                   |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                  |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.27x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.68 us: 1.27x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.37 us: 1.27x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 915 ms: 1.25x faster                                                    |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 274 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 467 ms: 1.17x faster                                                    |
| sympy_expand             | 543 ms                                                                | 468 ms: 1.16x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.9 ms: 1.15x faster                                                   |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.81 ms: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| regex_dna                | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.00 ms: 1.09x faster                                                   |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.97 us: 1.04x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| json                     | 5.88 ms                                                               | 6.07 ms: 1.03x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.39 ms: 1.11x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.2 us: 1.14x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.17 ms: 1.73x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.95 ms: 1.75x slower                                                   |
| logging_silent           | 222 ns                                                                | 612 ns: 2.75x slower                                                    |
| coverage                 | 83.6 ms                                                               | 559 ms: 6.68x slower                                                    |
| thrift                   | 1.26 ms                                                               | 194 ms: 154.02x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 2.60 sec: 178.93x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.221x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.34x