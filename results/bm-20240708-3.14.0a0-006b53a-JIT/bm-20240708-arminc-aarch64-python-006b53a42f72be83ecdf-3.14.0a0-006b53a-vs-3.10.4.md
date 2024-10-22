# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-aarch64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| html5lib       | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.06 sec: 2.15x faster                                                  |
| async_tree_none         | 950 ms                                                                | 447 ms: 2.13x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 581 ms: 1.95x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 735 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.1 ms: 1.51x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 274 us: 1.34x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 412 us: 1.29x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 79.6 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.18x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.06 sec: 2.15x faster                                                  |
| async_tree_none          | 950 ms                                                                | 447 ms: 2.13x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 581 ms: 1.95x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.21 ms: 1.77x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 38.6 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.6 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 735 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.3 ms: 1.69x faster                                                   |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 87.5 ms: 1.53x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 624 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 89.1 ms: 1.51x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                   |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.2 ms: 1.43x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.3 us: 1.42x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 179 ms: 1.37x faster                                                    |
| deepcopy                 | 511 us                                                                | 374 us: 1.37x faster                                                    |
| chaos                    | 121 ms                                                                | 89.3 ms: 1.36x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.22 us: 1.35x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 274 us: 1.34x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.98 us: 1.33x faster                                                   |
| pyflate                  | 795 ms                                                                | 599 ms: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 958 us: 1.32x faster                                                    |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.30x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 412 us: 1.29x faster                                                    |
| tornado_http             | 178 ms                                                                | 139 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 69.6 ms: 1.24x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.01 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                   |
| pylint                   | 485 ms                                                                | 416 ms: 1.17x faster                                                    |
| dask                     | 450 ms                                                                | 388 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.08 us: 1.13x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.89 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.07x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 70.2 ms: 1.07x faster                                                   |
| scimark_fft              | 500 ms                                                                | 467 ms: 1.07x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 71.9 ms: 1.02x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.38 sec: 1.01x slower                                                  |
| nqueens                  | 117 ms                                                                | 118 ms: 1.01x slower                                                    |
| sympy_str                | 329 ms                                                                | 332 ms: 1.01x slower                                                    |
| sympy_expand             | 543 ms                                                                | 550 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.32 ms: 1.03x slower                                                   |
| sympy_sum                | 184 ms                                                                | 192 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 499 ms: 1.10x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 79.6 ms: 1.14x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.00 ms: 1.20x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.6 ms: 1.24x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (8): xml_etree_iterparse, docutils, pidigits, pprint_safe_repr, json, sympy_integrate, asyncio_websockets, regex_compile
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.23x