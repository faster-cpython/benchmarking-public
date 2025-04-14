# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.111x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.32 sec: 1.06x faster                                                   |
| html5lib       | 86.5 ms                                                               | 75.3 ms: 1.15x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 974 ms: 2.35x faster                                                     |
| async_tree_none         | 950 ms                                                                | 452 ms: 2.10x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 549 ms: 2.07x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.06x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 101 ms: 1.33x faster                                                     |
| nbody          | 166 ms                                                                | 185 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 165 ms: 1.07x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.00 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 460 us: 1.15x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 319 us: 1.15x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.23 sec: 1.04x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 7.42 us: 1.06x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 139 ms: 1.13x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 41.0 us: 1.17x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.13 us: 1.17x slower                                                    |
| unpickle             | 17.5 us                                                               | 21.0 us: 1.20x slower                                                    |
| json_loads           | 30.9 us                                                               | 38.4 us: 1.24x slower                                                    |
| pickle               | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.79x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 54.6 ms: 1.02x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 36.8 ms: 1.04x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 78.7 ms: 1.13x slower                                                    |
| mako            | 18.9 ms                                                               | 22.4 ms: 1.18x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.09x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 974 ms: 2.35x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 287 us: 2.30x faster                                                     |
| async_tree_none          | 950 ms                                                                | 452 ms: 2.10x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 549 ms: 2.07x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.76x faster                                                     |
| deltablue                | 8.94 ms                                                               | 5.29 ms: 1.69x faster                                                    |
| generators               | 68.1 ms                                                               | 43.0 ms: 1.58x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 619 ms: 1.52x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.78 ms: 1.49x faster                                                    |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                     |
| logging_silent           | 222 ns                                                                | 156 ns: 1.43x faster                                                     |
| scimark_sor              | 246 ms                                                                | 178 ms: 1.38x faster                                                     |
| raytrace                 | 573 ms                                                                | 423 ms: 1.36x faster                                                     |
| chaos                    | 121 ms                                                                | 90.0 ms: 1.34x faster                                                    |
| float                    | 135 ms                                                                | 101 ms: 1.33x faster                                                     |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                     |
| richards                 | 91.7 ms                                                               | 71.5 ms: 1.28x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.57 sec: 1.28x faster                                                   |
| pylint                   | 485 ms                                                                | 382 ms: 1.27x faster                                                     |
| richards_super           | 107 ms                                                                | 87.4 ms: 1.23x faster                                                    |
| comprehensions           | 33.1 us                                                               | 27.0 us: 1.23x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.98 ms: 1.21x faster                                                    |
| deepcopy                 | 511 us                                                                | 423 us: 1.21x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.06 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 51.6 us: 1.20x faster                                                    |
| pyflate                  | 795 ms                                                                | 671 ms: 1.18x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                     |
| scimark_lu               | 227 ms                                                                | 193 ms: 1.17x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                                   |
| coroutines               | 37.2 ms                                                               | 31.9 ms: 1.17x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.45 ms: 1.16x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 460 us: 1.15x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 75.3 ms: 1.15x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 319 us: 1.15x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 117 ms: 1.14x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.75 us: 1.12x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 116 ms: 1.10x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.9 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                    |
| regex_compile            | 177 ms                                                                | 165 ms: 1.07x faster                                                     |
| logging_format           | 10.6 us                                                               | 9.96 us: 1.07x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.00 ms: 1.06x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.32 sec: 1.06x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 70.4 ms: 1.04x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.23 sec: 1.04x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.51 us: 1.02x faster                                                    |
| django_template          | 53.3 ms                                                               | 54.6 ms: 1.02x slower                                                    |
| mdp                      | 3.70 sec                                                              | 3.86 sec: 1.04x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 36.8 ms: 1.04x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 687 ms: 1.05x slower                                                     |
| sympy_sum                | 184 ms                                                                | 194 ms: 1.05x slower                                                     |
| unpickle_list            | 6.99 us                                                               | 7.42 us: 1.06x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.22 ms: 1.08x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 22.2 ms: 1.08x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.0 ms: 1.09x slower                                                    |
| sympy_str                | 329 ms                                                                | 359 ms: 1.09x slower                                                     |
| json                     | 5.88 ms                                                               | 6.50 ms: 1.11x slower                                                    |
| nbody                    | 166 ms                                                                | 185 ms: 1.11x slower                                                     |
| sympy_expand             | 543 ms                                                                | 605 ms: 1.11x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 78.7 ms: 1.13x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 139 ms: 1.13x slower                                                     |
| nqueens                  | 117 ms                                                                | 133 ms: 1.13x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 41.0 us: 1.17x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.13 us: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 530 ms: 1.17x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.87 ms: 1.18x slower                                                    |
| mako                     | 18.9 ms                                                               | 22.4 ms: 1.18x slower                                                    |
| unpickle                 | 17.5 us                                                               | 21.0 us: 1.20x slower                                                    |
| json_loads               | 30.9 us                                                               | 38.4 us: 1.24x slower                                                    |
| meteor_contest           | 126 ms                                                                | 157 ms: 1.25x slower                                                     |
| fannkuch                 | 546 ms                                                                | 681 ms: 1.25x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.8 us: 1.27x slower                                                    |
| telco                    | 8.49 ms                                                               | 12.0 ms: 1.42x slower                                                    |
| coverage                 | 83.6 ms                                                               | 127 ms: 1.52x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 58.8 ms: 4.05x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (14): thrift, scimark_fft, regex_v8, create_gc_cycles, 2to3, sqlglot_normalize, sqlalchemy_declarative, pprint_pformat, regex_dna, pprint_safe_repr, sqlglot_optimize, xml_etree_process, pidigits, json_dumps
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.58x