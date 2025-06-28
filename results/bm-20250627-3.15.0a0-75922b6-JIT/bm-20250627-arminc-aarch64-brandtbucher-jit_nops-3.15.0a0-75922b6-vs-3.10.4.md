# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_nops
- machine: linux-aarch64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                              |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                            |
| html5lib       | 86.5 ms                                                               | 62.6 ms: 1.38x faster                                             |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 905 ms: 2.53x faster                                              |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                              |
| async_tree_none         | 950 ms                                                                | 404 ms: 2.35x faster                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 671 ms: 1.90x faster                                              |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.1 ms: 1.62x faster                                             |
| nbody          | 166 ms                                                                | 126 ms: 1.31x faster                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                              |
| regex_v8       | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                             |
| regex_dna      | 257 ms                                                                | 218 ms: 1.18x faster                                              |
| regex_effbot   | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                             |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 248 us: 1.48x faster                                              |
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                            |
| pickle_pure_python   | 529 us                                                                | 401 us: 1.32x faster                                              |
| xml_etree_process    | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                             |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                             |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                              |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                              |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                              |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.23x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                             |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                             |
| django_template | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                             |
| genshi_text     | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                             |
| genshi_xml      | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                             |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 213 us: 3.11x faster                                              |
| async_tree_io            | 2.28 sec                                                              | 905 ms: 2.53x faster                                              |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                              |
| async_tree_none          | 950 ms                                                                | 404 ms: 2.35x faster                                              |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                             |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                            |
| richards_super           | 107 ms                                                                | 51.1 ms: 2.10x faster                                             |
| richards                 | 91.7 ms                                                               | 44.1 ms: 2.08x faster                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 671 ms: 1.90x faster                                              |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.87x faster                                             |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                             |
| scimark_sor              | 246 ms                                                                | 139 ms: 1.77x faster                                              |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                              |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                              |
| go                       | 264 ms                                                                | 156 ms: 1.70x faster                                              |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.64x faster                                             |
| float                    | 135 ms                                                                | 83.1 ms: 1.62x faster                                             |
| scimark_monte_carlo      | 128 ms                                                                | 79.7 ms: 1.60x faster                                             |
| spectral_norm            | 186 ms                                                                | 120 ms: 1.56x faster                                              |
| comprehensions           | 33.1 us                                                               | 21.7 us: 1.53x faster                                             |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                              |
| deepcopy                 | 511 us                                                                | 337 us: 1.51x faster                                              |
| unpickle_pure_python     | 366 us                                                                | 248 us: 1.48x faster                                              |
| pyflate                  | 795 ms                                                                | 539 ms: 1.48x faster                                              |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.47x faster                                              |
| hexiom                   | 10.9 ms                                                               | 7.47 ms: 1.46x faster                                             |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                            |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                             |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                              |
| crypto_pyaes             | 134 ms                                                                | 94.6 ms: 1.42x faster                                             |
| logging_simple           | 9.78 us                                                               | 6.99 us: 1.40x faster                                             |
| html5lib                 | 86.5 ms                                                               | 62.6 ms: 1.38x faster                                             |
| dulwich_log              | 73.5 ms                                                               | 53.5 ms: 1.37x faster                                             |
| logging_format           | 10.6 us                                                               | 7.82 us: 1.36x faster                                             |
| django_template          | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                             |
| thrift                   | 1.26 ms                                                               | 944 us: 1.33x faster                                              |
| genshi_text              | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                             |
| pickle_pure_python       | 529 us                                                                | 401 us: 1.32x faster                                              |
| nbody                    | 166 ms                                                                | 126 ms: 1.31x faster                                              |
| xml_etree_process        | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                             |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                             |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.27x faster                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                             |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                             |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                              |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                              |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                            |
| scimark_fft              | 500 ms                                                                | 409 ms: 1.22x faster                                              |
| regex_v8                 | 32.2 ms                                                               | 26.6 ms: 1.21x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                              |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                              |
| regex_dna                | 257 ms                                                                | 218 ms: 1.18x faster                                              |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                              |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                              |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                            |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                              |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                             |
| genshi_xml               | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                             |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                              |
| sqlite_synth             | 4.12 us                                                               | 3.72 us: 1.11x faster                                             |
| sympy_expand             | 543 ms                                                                | 493 ms: 1.10x faster                                              |
| regex_effbot             | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.06 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                              |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.39 sec: 1.01x slower                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                            |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                              |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                             |
| async_generators         | 452 ms                                                                | 484 ms: 1.07x slower                                              |
| telco                    | 8.49 ms                                                               | 9.08 ms: 1.07x slower                                             |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                             |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                             |
| gc_traversal             | 4.15 ms                                                               | 6.86 ms: 1.65x slower                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.84 ms: 1.70x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                      |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.336x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.39x