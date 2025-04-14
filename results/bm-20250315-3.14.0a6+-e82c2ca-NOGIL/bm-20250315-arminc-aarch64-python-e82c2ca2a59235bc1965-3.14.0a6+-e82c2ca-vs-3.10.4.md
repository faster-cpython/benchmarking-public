# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.142x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 357 ms: 1.07x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.18 sec: 1.11x faster                                                   |
| html5lib       | 86.5 ms                                                               | 73.5 ms: 1.18x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 902 ms: 2.53x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 511 ms: 2.22x faster                                                     |
| async_tree_none         | 950 ms                                                                | 428 ms: 2.22x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 689 ms: 1.85x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| pidigits       | 235 ms                                                                | 231 ms: 1.02x faster                                                     |
| nbody          | 166 ms                                                                | 181 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                    |
| regex_compile  | 177 ms                                                                | 159 ms: 1.11x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 127 ms: 1.23x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 440 us: 1.20x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 310 us: 1.18x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.06 sec: 1.10x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 16.4 ms: 1.02x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 7.27 us: 1.04x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 134 ms: 1.09x slower                                                     |
| pickle_list          | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.2 us: 1.12x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.3 us: 1.16x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| json_loads           | 30.9 us                                                               | 38.2 us: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 19.6 ms: 1.75x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 14.0 ms: 2.03x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.89x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 69.8 ms                                                               | 74.0 ms: 1.06x slower                                                    |
| genshi_text    | 35.2 ms                                                               | 37.4 ms: 1.06x slower                                                    |
| mako           | 18.9 ms                                                               | 21.9 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 902 ms: 2.53x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 263 us: 2.51x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 511 ms: 2.22x faster                                                     |
| async_tree_none          | 950 ms                                                                | 428 ms: 2.22x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 689 ms: 1.85x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.97 ms: 1.80x faster                                                    |
| generators               | 68.1 ms                                                               | 40.0 ms: 1.70x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 589 ms: 1.60x faster                                                     |
| go                       | 264 ms                                                                | 169 ms: 1.56x faster                                                     |
| logging_silent           | 222 ns                                                                | 143 ns: 1.55x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.71 ms: 1.53x faster                                                    |
| scimark_sor              | 246 ms                                                                | 169 ms: 1.46x faster                                                     |
| raytrace                 | 573 ms                                                                | 407 ms: 1.41x faster                                                     |
| chaos                    | 121 ms                                                                | 87.2 ms: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.43 sec: 1.35x faster                                                   |
| float                    | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| richards                 | 91.7 ms                                                               | 69.8 ms: 1.31x faster                                                    |
| richards_super           | 107 ms                                                                | 81.7 ms: 1.31x faster                                                    |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.31x faster                                                     |
| pylint                   | 485 ms                                                                | 373 ms: 1.30x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| deepcopy                 | 511 us                                                                | 399 us: 1.28x faster                                                     |
| pyflate                  | 795 ms                                                                | 625 ms: 1.27x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 59.2 ms: 1.24x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 49.7 us: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.37 sec: 1.24x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 108 ms: 1.24x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 127 ms: 1.23x faster                                                     |
| comprehensions           | 33.1 us                                                               | 26.9 us: 1.23x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 440 us: 1.20x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.08 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| scimark_lu               | 227 ms                                                                | 189 ms: 1.20x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.44 us: 1.20x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 310 us: 1.18x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 73.5 ms: 1.18x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 110 ms: 1.16x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.53 us: 1.15x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.42 us: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.18 sec: 1.11x faster                                                   |
| regex_compile            | 177 ms                                                                | 159 ms: 1.11x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.8 ms: 1.11x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.14 ms: 1.10x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.06 sec: 1.10x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.08 ms: 1.09x faster                                                    |
| 2to3                     | 381 ms                                                                | 357 ms: 1.07x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 187 ms: 1.05x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                    |
| scimark_fft              | 500 ms                                                                | 481 ms: 1.04x faster                                                     |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.04x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.28 sec: 1.03x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 16.4 ms: 1.02x faster                                                    |
| pidigits                 | 235 ms                                                                | 231 ms: 1.02x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 27.1 ms: 1.02x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 21.1 ms: 1.03x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.27 us: 1.04x slower                                                    |
| sympy_sum                | 184 ms                                                                | 192 ms: 1.04x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 74.0 ms: 1.06x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 37.4 ms: 1.06x slower                                                    |
| sympy_str                | 329 ms                                                                | 352 ms: 1.07x slower                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.24 ms: 1.08x slower                                                    |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 134 ms: 1.09x slower                                                     |
| nbody                    | 166 ms                                                                | 181 ms: 1.09x slower                                                     |
| sympy_expand             | 543 ms                                                                | 595 ms: 1.10x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.74 us: 1.10x slower                                                    |
| json                     | 5.88 ms                                                               | 6.47 ms: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.2 us: 1.12x slower                                                    |
| async_generators         | 452 ms                                                                | 514 ms: 1.14x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.82 ms: 1.14x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.9 ms: 1.16x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.3 us: 1.16x slower                                                    |
| fannkuch                 | 546 ms                                                                | 652 ms: 1.19x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| meteor_contest           | 126 ms                                                                | 155 ms: 1.23x slower                                                     |
| json_loads               | 30.9 us                                                               | 38.2 us: 1.24x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.5 ms: 1.35x slower                                                    |
| coverage                 | 83.6 ms                                                               | 128 ms: 1.53x slower                                                     |
| python_startup           | 11.2 ms                                                               | 19.6 ms: 1.75x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 14.0 ms: 2.03x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 57.7 ms: 3.97x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (4): deepcopy_reduce, xml_etree_process, django_template, mdp
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.142x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.59x