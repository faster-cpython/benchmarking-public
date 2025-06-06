# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.343x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 60.2 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 927 ms: 2.46x faster                                                     |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 497 ms: 2.28x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 755 ms: 1.69x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.0 ms: 1.53x faster                                                    |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| pidigits       | 235 ms                                                                | 305 ms: 1.30x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 34.6 ms: 1.08x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 75.5 ms: 1.32x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.86 us: 1.19x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| unpickle             | 17.5 us                                                               | 16.8 us: 1.04x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.65 us: 1.08x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.7 us: 1.12x slower                                                    |
| pickle               | 12.5 us                                                               | 15.4 us: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 186 us: 3.55x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 927 ms: 2.46x faster                                                     |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 497 ms: 2.28x faster                                                     |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                     |
| logging_silent           | 222 ns                                                                | 118 ns: 1.88x faster                                                     |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.5 ms: 1.81x faster                                                    |
| chaos                    | 121 ms                                                                | 67.0 ms: 1.81x faster                                                    |
| raytrace                 | 573 ms                                                                | 318 ms: 1.80x faster                                                     |
| spectral_norm            | 186 ms                                                                | 107 ms: 1.75x faster                                                     |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.74x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 36.5 us: 1.69x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 755 ms: 1.69x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.6 us: 1.69x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 567 ms: 1.66x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.77 ms: 1.60x faster                                                    |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.60x faster                                                     |
| deepcopy                 | 511 us                                                                | 320 us: 1.59x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 81.7 ms: 1.57x faster                                                    |
| float                    | 135 ms                                                                | 88.0 ms: 1.53x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                    |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 89.4 ms: 1.50x faster                                                    |
| pyflate                  | 795 ms                                                                | 541 ms: 1.47x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 60.2 ms: 1.44x faster                                                    |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.60 us: 1.40x faster                                                    |
| django_template          | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 75.5 ms: 1.32x faster                                                    |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                                     |
| scimark_fft              | 500 ms                                                                | 383 ms: 1.31x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.7 ms: 1.30x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                                    |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.09 ms: 1.25x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.25x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.23x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.9 ms: 1.22x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.95 sec: 1.21x faster                                                   |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 60.7 ms: 1.21x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.86 us: 1.19x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 966 ms: 1.19x faster                                                     |
| nqueens                  | 117 ms                                                                | 99.6 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.17x faster                                                   |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.28 sec: 1.13x faster                                                   |
| fannkuch                 | 546 ms                                                                | 497 ms: 1.10x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.08x faster                                                     |
| async_generators         | 452 ms                                                                | 425 ms: 1.07x faster                                                     |
| unpickle                 | 17.5 us                                                               | 16.8 us: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 6.04 ms: 1.03x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 34.6 ms: 1.08x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.65 us: 1.08x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.25 ms: 1.09x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.7 us: 1.12x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 94.9 ms: 1.14x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.4 us: 1.23x slower                                                    |
| pidigits                 | 235 ms                                                                | 305 ms: 1.30x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.76 ms: 1.63x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.86 ms: 1.71x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.43 sec: 304.47x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (5): sqlite_synth, xml_etree_iterparse, xml_etree_parse, regex_dna, asyncio_websockets
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.343x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.34x