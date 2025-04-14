# Results vs. 3.10.4

- fork: python
- ref: 98fa4a49fecbac3c990a
- machine: linux-aarch64
- commit hash: 98fa4a4
- commit date: 2025-03-09
- overall geometric mean: 1.309x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                   |
| html5lib       | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 886 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 382 ms: 2.48x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 468 ms: 2.42x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 660 ms: 1.93x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.7 ms: 1.63x faster                                                    |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.43x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                    |
| regex_dna      | 257 ms                                                                | 237 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.39 sec: 1.40x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 76.4 ms: 1.30x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.8 ms: 1.42x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.44x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.24x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 886 ms: 2.58x faster                                                     |
| async_tree_none          | 950 ms                                                                | 382 ms: 2.48x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 468 ms: 2.42x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                                    |
| richards_super           | 107 ms                                                                | 53.9 ms: 1.99x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 660 ms: 1.93x faster                                                     |
| richards                 | 91.7 ms                                                               | 48.1 ms: 1.90x faster                                                    |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                                    |
| chaos                    | 121 ms                                                                | 66.4 ms: 1.82x faster                                                    |
| raytrace                 | 573 ms                                                                | 317 ms: 1.81x faster                                                     |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                     |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.65x faster                                                     |
| float                    | 135 ms                                                                | 82.7 ms: 1.63x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                    |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                                     |
| deepcopy                 | 511 us                                                                | 324 us: 1.58x faster                                                     |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                     |
| go                       | 264 ms                                                                | 172 ms: 1.53x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 84.3 ms: 1.52x faster                                                    |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.84 us: 1.43x faster                                                    |
| regex_compile            | 177 ms                                                                | 124 ms: 1.43x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.39 sec: 1.40x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.57 us: 1.40x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                    |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.2 us: 1.37x faster                                                    |
| thrift                   | 1.26 ms                                                               | 923 us: 1.37x faster                                                     |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 98.3 ms: 1.36x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.40 us: 1.35x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 8.12 ms: 1.34x faster                                                    |
| coroutines               | 37.2 ms                                                               | 27.7 ms: 1.34x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 55.8 ms: 1.32x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 76.4 ms: 1.30x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.8 ms: 1.30x faster                                                    |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                    |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.3 ms: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 417 ms: 1.20x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                     |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                                    |
| sympy_expand             | 543 ms                                                                | 475 ms: 1.14x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.28 sec: 1.13x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.73 us: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| regex_dna                | 257 ms                                                                | 237 ms: 1.08x faster                                                     |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                     |
| fannkuch                 | 546 ms                                                                | 515 ms: 1.06x faster                                                     |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.52 sec: 1.07x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.1 ms: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.8 ms: 1.42x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.58 ms: 1.58x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.67 sec: 183.59x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (3): pidigits, async_generators, asyncio_websockets
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250309-3.14.0a5+-98fa4a4-JIT/bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.309x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.32x