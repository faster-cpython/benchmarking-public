# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.092x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.41 sec: 1.03x faster                                                   |
| html5lib       | 86.5 ms                                                               | 76.2 ms: 1.13x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 966 ms: 2.37x faster                                                     |
| async_tree_none         | 950 ms                                                                | 442 ms: 2.15x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 538 ms: 2.11x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 733 ms: 1.74x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.08x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 103 ms: 1.30x faster                                                     |
| nbody          | 166 ms                                                                | 182 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 159 ms: 1.11x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.20x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 133 ms: 1.18x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 331 us: 1.10x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 483 us: 1.10x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 7.27 us: 1.04x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 104 ms: 1.05x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 140 ms: 1.14x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 40.6 us: 1.16x slower                                                    |
| json_loads           | 30.9 us                                                               | 37.2 us: 1.20x slower                                                    |
| unpickle             | 17.5 us                                                               | 21.1 us: 1.20x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.32 us: 1.21x slower                                                    |
| pickle               | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.78x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 37.2 ms: 1.06x slower                                                    |
| django_template | 53.3 ms                                                               | 56.5 ms: 1.06x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 80.2 ms: 1.15x slower                                                    |
| mako            | 18.9 ms                                                               | 23.6 ms: 1.25x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.13x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 966 ms: 2.37x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 288 us: 2.30x faster                                                     |
| async_tree_none          | 950 ms                                                                | 442 ms: 2.15x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 538 ms: 2.11x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 733 ms: 1.74x faster                                                     |
| generators               | 68.1 ms                                                               | 43.9 ms: 1.55x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 618 ms: 1.53x faster                                                     |
| go                       | 264 ms                                                                | 181 ms: 1.46x faster                                                     |
| deltablue                | 8.94 ms                                                               | 6.30 ms: 1.42x faster                                                    |
| logging_silent           | 222 ns                                                                | 159 ns: 1.40x faster                                                     |
| chaos                    | 121 ms                                                                | 88.7 ms: 1.37x faster                                                    |
| scimark_sor              | 246 ms                                                                | 183 ms: 1.35x faster                                                     |
| raytrace                 | 573 ms                                                                | 426 ms: 1.35x faster                                                     |
| float                    | 135 ms                                                                | 103 ms: 1.30x faster                                                     |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.28x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.57 sec: 1.28x faster                                                   |
| richards                 | 91.7 ms                                                               | 73.8 ms: 1.24x faster                                                    |
| pylint                   | 485 ms                                                                | 392 ms: 1.24x faster                                                     |
| richards_super           | 107 ms                                                                | 88.6 ms: 1.21x faster                                                    |
| pyflate                  | 795 ms                                                                | 661 ms: 1.20x faster                                                     |
| scimark_lu               | 227 ms                                                                | 189 ms: 1.20x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.20x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 112 ms: 1.19x faster                                                     |
| deepcopy                 | 511 us                                                                | 429 us: 1.19x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 133 ms: 1.18x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 52.9 us: 1.17x faster                                                    |
| coroutines               | 37.2 ms                                                               | 31.8 ms: 1.17x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.49 ms: 1.14x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 2.12 ms: 1.13x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 76.2 ms: 1.13x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.63 ms: 1.13x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 113 ms: 1.13x faster                                                     |
| comprehensions           | 33.1 us                                                               | 29.6 us: 1.12x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.5 ms: 1.12x faster                                                    |
| regex_compile            | 177 ms                                                                | 159 ms: 1.11x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 331 us: 1.10x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 483 us: 1.10x faster                                                     |
| logging_simple           | 9.78 us                                                               | 9.16 us: 1.07x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 69.0 ms: 1.07x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| logging_format           | 10.6 us                                                               | 10.1 us: 1.05x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.17 ms: 1.04x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.41 sec: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 680 ms: 1.04x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 205 ms: 1.04x slower                                                     |
| mdp                      | 3.70 sec                                                              | 3.84 sec: 1.04x slower                                                   |
| unpickle_list            | 6.99 us                                                               | 7.27 us: 1.04x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 104 ms: 1.05x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 79.4 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.06 ms: 1.06x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 37.2 ms: 1.06x slower                                                    |
| django_template          | 53.3 ms                                                               | 56.5 ms: 1.06x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 21.8 ms: 1.06x slower                                                    |
| json                     | 5.88 ms                                                               | 6.34 ms: 1.08x slower                                                    |
| sympy_sum                | 184 ms                                                                | 199 ms: 1.08x slower                                                     |
| nbody                    | 166 ms                                                                | 182 ms: 1.10x slower                                                     |
| sympy_str                | 329 ms                                                                | 364 ms: 1.11x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 140 ms: 1.14x slower                                                     |
| sympy_expand             | 543 ms                                                                | 621 ms: 1.14x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 80.2 ms: 1.15x slower                                                    |
| nqueens                  | 117 ms                                                                | 135 ms: 1.15x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.83 ms: 1.15x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 40.6 us: 1.16x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 31.0 ms: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 542 ms: 1.20x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.2 us: 1.20x slower                                                    |
| unpickle                 | 17.5 us                                                               | 21.1 us: 1.20x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.32 us: 1.21x slower                                                    |
| fannkuch                 | 546 ms                                                                | 678 ms: 1.24x slower                                                     |
| mako                     | 18.9 ms                                                               | 23.6 ms: 1.25x slower                                                    |
| meteor_contest           | 126 ms                                                                | 158 ms: 1.25x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.42 ms: 1.30x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.8 ms: 1.39x slower                                                    |
| coverage                 | 83.6 ms                                                               | 132 ms: 1.58x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.78x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 56.3 ms: 3.88x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (11): scimark_fft, regex_v8, pidigits, json_dumps, regex_dna, pprint_safe_repr, pprint_pformat, 2to3, sqlglot_normalize, thrift, deepcopy_reduce
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.57x