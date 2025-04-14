# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.14 sec: 1.12x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 887 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 480 ms: 2.36x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 669 ms: 1.90x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.2 ms: 1.58x faster                                                    |
| nbody          | 166 ms                                                                | 132 ms: 1.26x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.7 ms: 1.12x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| regex_dna      | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 404 us: 1.31x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 77.9 ms: 1.28x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 292 us: 1.25x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.33 us: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.1 us: 1.10x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.77 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.3 us: 1.12x slower                                                    |
| pickle               | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 216 us: 3.05x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 887 ms: 2.58x faster                                                     |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 480 ms: 2.36x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.13 ms: 2.17x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 669 ms: 1.90x faster                                                     |
| richards_super           | 107 ms                                                                | 56.5 ms: 1.90x faster                                                    |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.83x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.8 ms: 1.80x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 545 ms: 1.73x faster                                                     |
| raytrace                 | 573 ms                                                                | 334 ms: 1.72x faster                                                     |
| chaos                    | 121 ms                                                                | 71.5 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                    |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                     |
| float                    | 135 ms                                                                | 85.2 ms: 1.58x faster                                                    |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                     |
| pylint                   | 485 ms                                                                | 322 ms: 1.51x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.18 sec: 1.51x faster                                                   |
| scimark_lu               | 227 ms                                                                | 155 ms: 1.46x faster                                                     |
| go                       | 264 ms                                                                | 181 ms: 1.46x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 88.4 ms: 1.45x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.05 us: 1.39x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| spectral_norm            | 186 ms                                                                | 135 ms: 1.38x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.73 us: 1.37x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                     |
| thrift                   | 1.26 ms                                                               | 942 us: 1.34x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.33x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 55.8 ms: 1.32x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.51 us: 1.31x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 404 us: 1.31x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.6 us: 1.30x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 154 ms: 1.28x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 77.9 ms: 1.28x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.58 ms: 1.27x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                    |
| nbody                    | 166 ms                                                                | 132 ms: 1.26x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 292 us: 1.25x faster                                                     |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.7 ms: 1.22x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.40 sec: 1.21x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| sympy_sum                | 184 ms                                                                | 154 ms: 1.19x faster                                                     |
| sympy_str                | 329 ms                                                                | 282 ms: 1.17x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.14 sec: 1.12x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 28.7 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.33 us: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| nqueens                  | 117 ms                                                                | 108 ms: 1.09x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.08 ms: 1.08x faster                                                    |
| regex_dna                | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| sympy_expand             | 543 ms                                                                | 505 ms: 1.07x faster                                                     |
| fannkuch                 | 546 ms                                                                | 529 ms: 1.03x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| async_generators         | 452 ms                                                                | 474 ms: 1.05x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.56 sec: 1.08x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.1 us: 1.10x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.77 us: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.3 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.91 ms: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.1 ms: 1.17x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.81 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.36 sec: 93.84x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (4): pidigits, meteor_contest, json, unpickle
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.33x