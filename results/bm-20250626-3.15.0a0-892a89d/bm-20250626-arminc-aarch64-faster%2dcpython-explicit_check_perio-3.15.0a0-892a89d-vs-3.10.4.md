# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.339x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                            |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 901 ms: 2.54x faster                                                              |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.41x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 664 ms: 1.92x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.3 ms: 1.54x faster                                                             |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.1 ms: 1.19x faster                                                             |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.39x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                             |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.36x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 901 ms: 2.54x faster                                                              |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.41x faster                                                              |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.21x faster                                                            |
| deltablue                | 8.94 ms                                                               | 4.06 ms: 2.21x faster                                                             |
| go                       | 264 ms                                                                | 127 ms: 2.08x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 664 ms: 1.92x faster                                                              |
| generators               | 68.1 ms                                                               | 37.2 ms: 1.83x faster                                                             |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                                             |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                             |
| raytrace                 | 573 ms                                                                | 332 ms: 1.72x faster                                                              |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                              |
| comprehensions           | 33.1 us                                                               | 20.1 us: 1.65x faster                                                             |
| richards                 | 91.7 ms                                                               | 56.3 ms: 1.63x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 38.3 us: 1.61x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 84.9 ms: 1.58x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 82.2 ms: 1.55x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                                             |
| float                    | 135 ms                                                                | 87.3 ms: 1.54x faster                                                             |
| pylint                   | 485 ms                                                                | 316 ms: 1.53x faster                                                              |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.53x faster                                                              |
| deepcopy                 | 511 us                                                                | 341 us: 1.50x faster                                                              |
| pyflate                  | 795 ms                                                                | 537 ms: 1.48x faster                                                              |
| scimark_lu               | 227 ms                                                                | 155 ms: 1.46x faster                                                              |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 52.4 ms: 1.40x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.39x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.38x faster                                                             |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                            |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| django_template          | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.29x faster                                                             |
| thrift                   | 1.26 ms                                                               | 983 us: 1.28x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.38 us: 1.27x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.79 us: 1.26x faster                                                             |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                             |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.25x faster                                                              |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                             |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                             |
| nqueens                  | 117 ms                                                                | 98.2 ms: 1.20x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 27.1 ms: 1.19x faster                                                             |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                                              |
| docutils                 | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                            |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                              |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.16x faster                                                              |
| sympy_expand             | 543 ms                                                                | 471 ms: 1.15x faster                                                              |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                             |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.08 sec: 1.13x faster                                                            |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                              |
| pprint_safe_repr         | 1.15 sec                                                              | 1.03 sec: 1.12x faster                                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.87 ms: 1.11x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.79 us: 1.09x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                             |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.61 ms: 1.13x slower                                                             |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.83 ms: 1.64x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.77 ms: 1.67x slower                                                             |
| logging_silent           | 222 ns                                                                | 650 ns: 2.93x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.30x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.339x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x