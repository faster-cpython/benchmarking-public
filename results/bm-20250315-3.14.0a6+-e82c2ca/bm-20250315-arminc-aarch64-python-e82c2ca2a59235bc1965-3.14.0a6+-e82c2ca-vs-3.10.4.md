# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.99 sec: 1.18x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.3 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 885 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 388 ms: 2.45x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 477 ms: 2.38x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.7 ms: 1.54x faster                                                    |
| nbody          | 166 ms                                                                | 128 ms: 1.30x faster                                                     |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 29.4 ms: 1.09x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                    |
| regex_dna      | 257 ms                                                                | 243 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 388 us: 1.37x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.50 sec: 1.35x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.39 us: 1.09x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| unpickle             | 17.5 us                                                               | 17.6 us: 1.01x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.55 us: 1.06x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| pickle               | 12.5 us                                                               | 15.7 us: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                    |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 199 us: 3.32x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 885 ms: 2.58x faster                                                     |
| async_tree_none          | 950 ms                                                                | 388 ms: 2.45x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 477 ms: 2.38x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.95 ms: 2.26x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.86x faster                                                    |
| go                       | 264 ms                                                                | 144 ms: 1.84x faster                                                     |
| richards_super           | 107 ms                                                                | 58.9 ms: 1.82x faster                                                    |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 543 ms: 1.74x faster                                                     |
| richards                 | 91.7 ms                                                               | 53.2 ms: 1.72x faster                                                    |
| chaos                    | 121 ms                                                                | 71.3 ms: 1.70x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                    |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 87.0 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 87.7 ms: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                     |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.52x faster                                                     |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.52x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 84.5 ms: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.18 sec: 1.51x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.52 ms: 1.45x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 51.4 ms: 1.43x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.95 us: 1.41x faster                                                    |
| pyflate                  | 795 ms                                                                | 569 ms: 1.40x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.60 us: 1.39x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 388 us: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.50 sec: 1.35x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 64.3 ms: 1.34x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.32x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| nbody                    | 166 ms                                                                | 128 ms: 1.30x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                    |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                                     |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 948 ms: 1.21x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                     |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                                     |
| docutils                 | 3.53 sec                                                              | 2.99 sec: 1.18x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.54 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 430 ms: 1.16x faster                                                     |
| sympy_expand             | 543 ms                                                                | 472 ms: 1.15x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                    |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.39 us: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 29.4 ms: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.07x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| regex_dna                | 257 ms                                                                | 243 ms: 1.06x faster                                                     |
| json                     | 5.88 ms                                                               | 5.85 ms: 1.00x faster                                                    |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                                     |
| unpickle                 | 17.5 us                                                               | 17.6 us: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.55 us: 1.06x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.49 ms: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.26x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.54 ms: 1.57x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.64 ms: 1.60x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.92 sec: 200.79x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                             |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x