# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-aarch64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| html5lib       | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none         | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 584 ms: 1.94x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 734 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.9 ms: 1.50x faster                                                   |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| regex_compile  | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 411 us: 1.29x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.78 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| django_template | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.5 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 80.2 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.18x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 584 ms: 1.94x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.18 ms: 1.78x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| richards_super           | 107 ms                                                                | 61.3 ms: 1.75x faster                                                   |
| generators               | 68.1 ms                                                               | 39.2 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 734 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.2 ms: 1.69x faster                                                   |
| logging_silent           | 222 ns                                                                | 137 ns: 1.63x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.4 us: 1.61x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 619 ms: 1.53x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 88.5 ms: 1.51x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                   |
| float                    | 135 ms                                                                | 89.9 ms: 1.50x faster                                                   |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 88.7 ms: 1.44x faster                                                   |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.02 ms: 1.41x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.6 us: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| deepcopy                 | 511 us                                                                | 372 us: 1.37x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.14 us: 1.37x faster                                                   |
| chaos                    | 121 ms                                                                | 89.6 ms: 1.35x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.96 us: 1.33x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                    |
| pyflate                  | 795 ms                                                                | 608 ms: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 965 us: 1.31x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 411 us: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| tornado_http             | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.23x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.04 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.20x faster                                                   |
| pylint                   | 485 ms                                                                | 405 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| dask                     | 450 ms                                                                | 387 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 68.6 ms: 1.10x faster                                                   |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.19 us: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.99 ms: 1.09x faster                                                   |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 69.4 ms: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.5 ms: 1.02x faster                                                   |
| nqueens                  | 117 ms                                                                | 116 ms: 1.01x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 26.4 ms: 1.01x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.39 sec: 1.01x slower                                                  |
| sympy_sum                | 184 ms                                                                | 187 ms: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| regex_compile            | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 512 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 80.2 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.90 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.78 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (6): json, pprint_safe_repr, pidigits, sympy_str, sympy_expand, asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.22x