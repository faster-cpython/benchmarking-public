# Results vs. 3.10.4

- fork: python
- ref: 4f18916c5c28321f363e
- machine: linux-aarch64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.374x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 288 ms: 1.32x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                   |
| html5lib       | 86.5 ms                                                               | 58.2 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.34x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 865 ms: 2.64x faster                                                     |
| async_tree_none         | 950 ms                                                                | 365 ms: 2.60x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 441 ms: 2.57x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 713 ms: 1.78x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.8 ms: 1.61x faster                                                    |
| nbody          | 166 ms                                                                | 126 ms: 1.32x faster                                                     |
| pidigits       | 235 ms                                                                | 290 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 118 ms: 1.50x faster                                                     |
| regex_dna      | 257 ms                                                                | 234 ms: 1.10x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 29.4 ms: 1.09x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 246 us: 1.49x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.36 sec: 1.43x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 372 us: 1.42x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 75.1 ms: 1.33x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.57 us: 1.25x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| unpickle             | 17.5 us                                                               | 16.5 us: 1.06x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 203 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.40 us: 1.03x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 36.4 us: 1.04x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.4 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.49x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.1 ms: 1.40x faster                                                    |
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 25.8 ms: 1.37x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.0 ms: 1.21x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.33x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 187 us: 3.54x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 865 ms: 2.64x faster                                                     |
| async_tree_none          | 950 ms                                                                | 365 ms: 2.60x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 441 ms: 2.57x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.72 ms: 2.40x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.59 sec: 2.33x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.04x faster                                                     |
| logging_silent           | 222 ns                                                                | 116 ns: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 35.8 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 57.1 ms: 1.88x faster                                                    |
| richards                 | 91.7 ms                                                               | 49.3 ms: 1.86x faster                                                    |
| chaos                    | 121 ms                                                                | 65.9 ms: 1.84x faster                                                    |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 713 ms: 1.78x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 34.8 us: 1.77x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 546 ms: 1.73x faster                                                     |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                     |
| deepcopy                 | 511 us                                                                | 306 us: 1.67x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.9 us: 1.67x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 78.1 ms: 1.64x faster                                                    |
| float                    | 135 ms                                                                | 83.8 ms: 1.61x faster                                                    |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.60x faster                                                     |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 84.7 ms: 1.58x faster                                                    |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.00 ms: 1.56x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.51x faster                                                   |
| pyflate                  | 795 ms                                                                | 528 ms: 1.51x faster                                                     |
| regex_compile            | 177 ms                                                                | 118 ms: 1.50x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 246 us: 1.49x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 58.2 ms: 1.48x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.9 ms: 1.44x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.85 us: 1.43x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.36 sec: 1.43x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 372 us: 1.42x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.47 us: 1.42x faster                                                    |
| django_template          | 53.3 ms                                                               | 38.1 ms: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.32 us: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 25.8 ms: 1.37x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 19.4 ms: 1.37x faster                                                    |
| sympy_sum                | 184 ms                                                                | 137 ms: 1.34x faster                                                     |
| coroutines               | 37.2 ms                                                               | 27.8 ms: 1.34x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 149 ms: 1.33x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 75.1 ms: 1.33x faster                                                    |
| 2to3                     | 381 ms                                                                | 288 ms: 1.32x faster                                                     |
| nbody                    | 166 ms                                                                | 126 ms: 1.32x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 890 ms: 1.29x faster                                                     |
| sympy_str                | 329 ms                                                                | 256 ms: 1.28x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.28x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 5.57 us: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.1 ms: 1.25x faster                                                    |
| scimark_fft              | 500 ms                                                                | 401 ms: 1.25x faster                                                     |
| docutils                 | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                   |
| sympy_expand             | 543 ms                                                                | 450 ms: 1.21x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 58.0 ms: 1.21x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 104 ms: 1.18x faster                                                     |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.55 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 493 ms: 1.11x faster                                                     |
| regex_dna                | 257 ms                                                                | 234 ms: 1.10x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 29.4 ms: 1.09x faster                                                    |
| async_generators         | 452 ms                                                                | 416 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                                    |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                     |
| unpickle                 | 17.5 us                                                               | 16.5 us: 1.06x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 203 ms: 1.04x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.92 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.40 us: 1.03x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.4 us: 1.04x slower                                                    |
| telco                    | 8.49 ms                                                               | 8.83 ms: 1.04x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.4 us: 1.08x slower                                                    |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| pidigits                 | 235 ms                                                                | 290 ms: 1.24x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.49x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.67 ms: 1.61x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.84 ms: 1.70x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.29 sec: 226.57x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                             |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.36x