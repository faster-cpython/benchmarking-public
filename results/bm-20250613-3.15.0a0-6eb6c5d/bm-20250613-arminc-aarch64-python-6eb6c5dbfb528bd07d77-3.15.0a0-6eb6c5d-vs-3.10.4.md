# Results vs. 3.10.4

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-aarch64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 898 ms: 2.54x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 467 ms: 2.43x faster                                                    |
| async_tree_none         | 950 ms                                                                | 396 ms: 2.40x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.8 ms: 1.50x faster                                                   |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                   |
| regex_dna      | 257 ms                                                                | 221 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 384 us: 1.38x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 191 us: 3.47x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 898 ms: 2.54x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 467 ms: 2.43x faster                                                    |
| async_tree_none          | 950 ms                                                                | 396 ms: 2.40x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.24x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.04 ms: 2.21x faster                                                   |
| go                       | 264 ms                                                                | 127 ms: 2.08x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                   |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                                   |
| chaos                    | 121 ms                                                                | 69.8 ms: 1.73x faster                                                   |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.69x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.2 ms: 1.59x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.0 ms: 1.58x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.95 ms: 1.57x faster                                                   |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 328 us: 1.55x faster                                                    |
| pyflate                  | 795 ms                                                                | 527 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 89.8 ms: 1.50x faster                                                   |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 128 ms: 1.46x faster                                                    |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 51.5 ms: 1.43x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 384 us: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                  |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.56 us: 1.29x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.25 us: 1.29x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                    |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.61 us: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                  |
| nqueens                  | 117 ms                                                                | 99.9 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.02 sec: 1.17x faster                                                  |
| regex_dna                | 257 ms                                                                | 221 ms: 1.16x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 989 ms: 1.16x faster                                                    |
| sympy_expand             | 543 ms                                                                | 471 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                   |
| meteor_contest           | 126 ms                                                                | 110 ms: 1.15x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.01 ms: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                   |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.48 ms: 1.12x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.84 ms: 1.65x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.88 ms: 1.72x slower                                                   |
| logging_silent           | 222 ns                                                                | 615 ns: 2.77x slower                                                    |
| coverage                 | 83.6 ms                                                               | 566 ms: 6.77x slower                                                    |
| thrift                   | 1.26 ms                                                               | 193 ms: 153.53x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.229x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x