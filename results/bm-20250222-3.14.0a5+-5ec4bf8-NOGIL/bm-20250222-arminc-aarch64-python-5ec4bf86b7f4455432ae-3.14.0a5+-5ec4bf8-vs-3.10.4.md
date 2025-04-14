# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.108x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.33 sec: 1.06x faster                                                   |
| html5lib       | 86.5 ms                                                               | 77.0 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 968 ms: 2.36x faster                                                     |
| async_tree_none         | 950 ms                                                                | 434 ms: 2.19x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 532 ms: 2.13x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 709 ms: 1.80x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.11x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 103 ms: 1.31x faster                                                     |
| nbody          | 166 ms                                                                | 185 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 163 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 462 us: 1.14x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 323 us: 1.13x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.15 sec: 1.07x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 104 ms: 1.04x slower                                                     |
| unpickle_list        | 6.99 us                                                               | 7.60 us: 1.09x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.08 us: 1.16x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.7 us: 1.18x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 146 ms: 1.19x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 43.0 us: 1.22x slower                                                    |
| pickle               | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| json_loads           | 30.9 us                                                               | 40.5 us: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.79x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 54.3 ms: 1.02x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 38.0 ms: 1.08x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                                    |
| mako            | 18.9 ms                                                               | 22.6 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.11x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 968 ms: 2.36x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 281 us: 2.35x faster                                                     |
| async_tree_none          | 950 ms                                                                | 434 ms: 2.19x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 532 ms: 2.13x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 709 ms: 1.80x faster                                                     |
| deltablue                | 8.94 ms                                                               | 5.24 ms: 1.71x faster                                                    |
| generators               | 68.1 ms                                                               | 43.2 ms: 1.57x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 2.67 ms: 1.56x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 608 ms: 1.55x faster                                                     |
| go                       | 264 ms                                                                | 177 ms: 1.50x faster                                                     |
| logging_silent           | 222 ns                                                                | 149 ns: 1.49x faster                                                     |
| scimark_sor              | 246 ms                                                                | 178 ms: 1.38x faster                                                     |
| raytrace                 | 573 ms                                                                | 416 ms: 1.38x faster                                                     |
| chaos                    | 121 ms                                                                | 89.0 ms: 1.36x faster                                                    |
| float                    | 135 ms                                                                | 103 ms: 1.31x faster                                                     |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                     |
| richards_super           | 107 ms                                                                | 83.7 ms: 1.28x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.56 sec: 1.28x faster                                                   |
| comprehensions           | 33.1 us                                                               | 26.4 us: 1.25x faster                                                    |
| pylint                   | 485 ms                                                                | 389 ms: 1.25x faster                                                     |
| richards                 | 91.7 ms                                                               | 73.9 ms: 1.24x faster                                                    |
| pyflate                  | 795 ms                                                                | 651 ms: 1.22x faster                                                     |
| coroutines               | 37.2 ms                                                               | 31.0 ms: 1.20x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 112 ms: 1.20x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 2.02 ms: 1.19x faster                                                    |
| deepcopy                 | 511 us                                                                | 430 us: 1.19x faster                                                     |
| scimark_lu               | 227 ms                                                                | 192 ms: 1.18x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.43 ms: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.37 ms: 1.16x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 53.0 us: 1.16x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 462 us: 1.14x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.62 us: 1.14x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 323 us: 1.13x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 113 ms: 1.13x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 77.0 ms: 1.12x faster                                                    |
| logging_simple           | 9.78 us                                                               | 9.01 us: 1.09x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.79 us: 1.08x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.09 ms: 1.08x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 24.3 ms: 1.08x faster                                                    |
| regex_compile            | 177 ms                                                                | 163 ms: 1.08x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 3.15 sec: 1.07x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.33 sec: 1.06x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 70.9 ms: 1.04x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.40 sec: 1.02x slower                                                   |
| django_template          | 53.3 ms                                                               | 54.3 ms: 1.02x slower                                                    |
| sympy_sum                | 184 ms                                                                | 190 ms: 1.03x slower                                                     |
| xml_etree_process        | 99.5 ms                                                               | 104 ms: 1.04x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 686 ms: 1.04x slower                                                     |
| mdp                      | 3.70 sec                                                              | 3.92 sec: 1.06x slower                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 21.8 ms: 1.06x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 38.0 ms: 1.08x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 28.8 ms: 1.09x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.60 us: 1.09x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.30 ms: 1.09x slower                                                    |
| sympy_str                | 329 ms                                                                | 367 ms: 1.12x slower                                                     |
| nbody                    | 166 ms                                                                | 185 ms: 1.12x slower                                                     |
| json                     | 5.88 ms                                                               | 6.63 ms: 1.13x slower                                                    |
| sympy_expand             | 543 ms                                                                | 613 ms: 1.13x slower                                                     |
| nqueens                  | 117 ms                                                                | 133 ms: 1.13x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.08 us: 1.16x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.88 ms: 1.18x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.7 us: 1.18x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 146 ms: 1.19x slower                                                     |
| mako                     | 18.9 ms                                                               | 22.6 ms: 1.19x slower                                                    |
| async_generators         | 452 ms                                                                | 540 ms: 1.19x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 43.0 us: 1.22x slower                                                    |
| meteor_contest           | 126 ms                                                                | 157 ms: 1.24x slower                                                     |
| fannkuch                 | 546 ms                                                                | 681 ms: 1.25x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| json_loads               | 30.9 us                                                               | 40.5 us: 1.31x slower                                                    |
| telco                    | 8.49 ms                                                               | 12.1 ms: 1.42x slower                                                    |
| coverage                 | 83.6 ms                                                               | 135 ms: 1.62x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 56.7 ms: 3.90x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (13): regex_effbot, regex_dna, sqlalchemy_declarative, regex_v8, 2to3, sqlglot_normalize, thrift, scimark_fft, pprint_safe_repr, json_dumps, pidigits, deepcopy_reduce, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.57x