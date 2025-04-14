# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.355x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.9 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 475 ms: 2.39x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 745 ms: 1.71x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.25x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.3 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| pidigits       | 235 ms                                                                | 306 ms: 1.30x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 255 us: 1.44x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 385 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 74.8 ms: 1.33x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.83 us: 1.20x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| unpickle             | 17.5 us                                                               | 16.6 us: 1.05x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.52 us: 1.05x slower                                                    |
| json_loads           | 30.9 us                                                               | 35.4 us: 1.14x slower                                                    |
| pickle               | 12.5 us                                                               | 15.8 us: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.09 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 186 us: 3.56x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 475 ms: 2.39x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                    |
| logging_silent           | 222 ns                                                                | 112 ns: 1.97x faster                                                     |
| richards_super           | 107 ms                                                                | 55.0 ms: 1.95x faster                                                    |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                     |
| richards                 | 91.7 ms                                                               | 48.5 ms: 1.89x faster                                                    |
| raytrace                 | 573 ms                                                                | 308 ms: 1.86x faster                                                     |
| generators               | 68.1 ms                                                               | 37.5 ms: 1.82x faster                                                    |
| chaos                    | 121 ms                                                                | 66.8 ms: 1.81x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.38 ms: 1.74x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.6 us: 1.73x faster                                                    |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 745 ms: 1.71x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.5 us: 1.69x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.69 ms: 1.68x faster                                                    |
| spectral_norm            | 186 ms                                                                | 111 ms: 1.68x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 76.8 ms: 1.66x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 573 ms: 1.65x faster                                                     |
| deepcopy                 | 511 us                                                                | 318 us: 1.61x faster                                                     |
| pylint                   | 485 ms                                                                | 311 ms: 1.56x faster                                                     |
| float                    | 135 ms                                                                | 86.3 ms: 1.56x faster                                                    |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.56x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 87.1 ms: 1.54x faster                                                    |
| pyflate                  | 795 ms                                                                | 527 ms: 1.51x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 59.9 ms: 1.44x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.44x faster                                                     |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.49 us: 1.42x faster                                                    |
| nbody                    | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.94 us: 1.41x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.28 us: 1.40x faster                                                    |
| django_template          | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 385 us: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.37x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                   |
| thrift                   | 1.26 ms                                                               | 937 us: 1.34x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 74.8 ms: 1.33x faster                                                    |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.33x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                    |
| scimark_fft              | 500 ms                                                                | 386 ms: 1.30x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.28x faster                                                    |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.7 ms: 1.25x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.12 ms: 1.25x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 934 ms: 1.23x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 61.6 ms: 1.22x faster                                                    |
| sympy_str                | 329 ms                                                                | 272 ms: 1.21x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 5.83 us: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.6 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.27 sec: 1.13x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                     |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                                     |
| async_generators         | 452 ms                                                                | 415 ms: 1.09x faster                                                     |
| unpickle                 | 17.5 us                                                               | 16.6 us: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| json                     | 5.88 ms                                                               | 6.11 ms: 1.04x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.52 us: 1.05x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.22 ms: 1.09x slower                                                    |
| coverage                 | 83.6 ms                                                               | 94.0 ms: 1.12x slower                                                    |
| json_loads               | 30.9 us                                                               | 35.4 us: 1.14x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.8 us: 1.26x slower                                                    |
| pidigits                 | 235 ms                                                                | 306 ms: 1.30x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.09 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.87 ms: 1.65x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.88 ms: 1.72x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.84 sec: 470.96x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (5): meteor_contest, xml_etree_iterparse, xml_etree_parse, sqlite_synth, regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.355x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.35x