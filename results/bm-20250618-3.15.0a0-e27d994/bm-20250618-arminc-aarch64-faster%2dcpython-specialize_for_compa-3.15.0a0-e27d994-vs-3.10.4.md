# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-aarch64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 893 ms: 2.56x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 468 ms: 2.42x faster                                                              |
| async_tree_none         | 950 ms                                                                | 393 ms: 2.42x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 666 ms: 1.91x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.5 ms: 1.58x faster                                                             |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                                             |
| regex_dna      | 257 ms                                                                | 219 ms: 1.18x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                            |
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                             |
| django_template | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 893 ms: 2.56x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 468 ms: 2.42x faster                                                              |
| async_tree_none          | 950 ms                                                                | 393 ms: 2.42x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                            |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                              |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 666 ms: 1.91x faster                                                              |
| richards_super           | 107 ms                                                                | 59.3 ms: 1.81x faster                                                             |
| chaos                    | 121 ms                                                                | 69.0 ms: 1.75x faster                                                             |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                              |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                              |
| richards                 | 91.7 ms                                                               | 54.3 ms: 1.69x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.1 us: 1.65x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 82.7 ms: 1.62x faster                                                             |
| float                    | 135 ms                                                                | 85.5 ms: 1.58x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.94 ms: 1.57x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 82.4 ms: 1.55x faster                                                             |
| spectral_norm            | 186 ms                                                                | 120 ms: 1.55x faster                                                              |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.54x faster                                                              |
| pylint                   | 485 ms                                                                | 316 ms: 1.54x faster                                                              |
| pyflate                  | 795 ms                                                                | 518 ms: 1.53x faster                                                              |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 52.3 ms: 1.40x faster                                                             |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                                            |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                            |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                                              |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                             |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                              |
| thrift                   | 1.26 ms                                                               | 940 us: 1.34x faster                                                              |
| django_template          | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.55 us: 1.30x faster                                                             |
| sympy_integrate          | 26.5 ms                                                               | 20.5 ms: 1.29x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.22 us: 1.29x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                             |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                              |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.25x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                             |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| sympy_str                | 329 ms                                                                | 266 ms: 1.24x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.74 us: 1.23x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| nqueens                  | 117 ms                                                                | 97.7 ms: 1.20x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                                             |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                              |
| regex_dna                | 257 ms                                                                | 219 ms: 1.18x faster                                                              |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                              |
| meteor_contest           | 126 ms                                                                | 108 ms: 1.17x faster                                                              |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                             |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.08 sec: 1.13x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.01 sec: 1.13x faster                                                            |
| regex_effbot             | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                             |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.70 ms: 1.14x slower                                                             |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.65x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.97 ms: 1.68x slower                                                             |
| logging_silent           | 222 ns                                                                | 646 ns: 2.91x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x