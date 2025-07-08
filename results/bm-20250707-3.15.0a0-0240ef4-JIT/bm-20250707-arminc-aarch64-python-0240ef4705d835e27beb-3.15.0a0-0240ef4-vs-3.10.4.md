# Results vs. 3.10.4

- fork: python
- ref: 0240ef4705d835e27beb
- machine: linux-aarch64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.287x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 905 ms: 2.52x faster                                                    |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 476 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 667 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.4 ms: 1.64x faster                                                   |
| nbody          | 166 ms                                                                | 127 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                                   |
| regex_dna      | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.75 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 250 us: 1.46x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.45x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.9 ms: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.07x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 63.2 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.24x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 905 ms: 2.52x faster                                                    |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 476 ms: 2.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                                  |
| richards_super           | 107 ms                                                                | 50.4 ms: 2.13x faster                                                   |
| richards                 | 91.7 ms                                                               | 45.6 ms: 2.01x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 667 ms: 1.91x faster                                                    |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                                   |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                                   |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                                    |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.73x faster                                                    |
| raytrace                 | 573 ms                                                                | 331 ms: 1.73x faster                                                    |
| go                       | 264 ms                                                                | 156 ms: 1.69x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 36.7 us: 1.68x faster                                                   |
| float                    | 135 ms                                                                | 82.4 ms: 1.64x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.7 ms: 1.58x faster                                                   |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                    |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.55x faster                                                    |
| spectral_norm            | 186 ms                                                                | 120 ms: 1.55x faster                                                    |
| pyflate                  | 795 ms                                                                | 525 ms: 1.51x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.0 us: 1.51x faster                                                   |
| pylint                   | 485 ms                                                                | 329 ms: 1.48x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 250 us: 1.46x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.45x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 93.3 ms: 1.44x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.70 ms: 1.42x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.91 us: 1.42x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.79 us: 1.36x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 54.5 ms: 1.35x faster                                                   |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                    |
| nbody                    | 166 ms                                                                | 127 ms: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.9 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                                  |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                                    |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                   |
| scimark_fft              | 500 ms                                                                | 409 ms: 1.22x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                                   |
| sympy_str                | 329 ms                                                                | 275 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| regex_dna                | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 473 ms: 1.15x faster                                                    |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.14x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.75 ms: 1.13x faster                                                   |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 63.2 ms: 1.11x faster                                                   |
| sympy_expand             | 543 ms                                                                | 492 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.74 us: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.15 ms: 1.07x faster                                                   |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.34 sec: 1.01x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 481 ms: 1.06x slower                                                    |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.86 ms: 1.65x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.80 ms: 1.68x slower                                                   |
| telco                    | 8.49 ms                                                               | 168 ms: 19.77x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (2): pprint_safe_repr, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.287x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x