# Results vs. 3.10.4

- fork: python
- ref: 7363e8d24d14abf65163
- machine: linux-aarch64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 58.3 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 865 ms: 2.64x faster                                                     |
| async_tree_none         | 950 ms                                                                | 372 ms: 2.56x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 452 ms: 2.51x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 723 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.4 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 128 ms: 1.29x faster                                                     |
| pidigits       | 235 ms                                                                | 292 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.59 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 371 us: 1.43x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 76.5 ms: 1.30x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.71 us: 1.23x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.14x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 203 ms: 1.04x faster                                                     |
| unpickle             | 17.5 us                                                               | 17.1 us: 1.02x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.43 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 36.8 us: 1.05x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.9 us: 1.13x slower                                                    |
| pickle               | 12.5 us                                                               | 15.7 us: 1.25x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.71 ms: 1.27x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 25.8 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.3 ms: 1.20x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.32x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 198 us: 3.34x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 865 ms: 2.64x faster                                                     |
| async_tree_none          | 950 ms                                                                | 372 ms: 2.56x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 452 ms: 2.51x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.77 ms: 2.37x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.62 sec: 2.28x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.04x faster                                                     |
| richards_super           | 107 ms                                                                | 54.9 ms: 1.95x faster                                                    |
| logging_silent           | 222 ns                                                                | 116 ns: 1.91x faster                                                     |
| chaos                    | 121 ms                                                                | 65.5 ms: 1.85x faster                                                    |
| generators               | 68.1 ms                                                               | 37.2 ms: 1.83x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.2 ms: 1.83x faster                                                    |
| raytrace                 | 573 ms                                                                | 323 ms: 1.78x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 723 ms: 1.76x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 35.2 us: 1.75x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 552 ms: 1.71x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.6 us: 1.69x faster                                                    |
| deepcopy                 | 511 us                                                                | 312 us: 1.64x faster                                                     |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.63x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.96 ms: 1.57x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.6 ms: 1.57x faster                                                    |
| pylint                   | 485 ms                                                                | 311 ms: 1.56x faster                                                     |
| float                    | 135 ms                                                                | 86.4 ms: 1.56x faster                                                    |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.52x faster                                                     |
| pyflate                  | 795 ms                                                                | 524 ms: 1.52x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.18 sec: 1.51x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 58.3 ms: 1.48x faster                                                    |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 371 us: 1.43x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.25 us: 1.42x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.61 us: 1.39x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 53.0 ms: 1.39x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 25.8 ms: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 19.7 ms: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.34x faster                                                     |
| sympy_sum                | 184 ms                                                                | 138 ms: 1.33x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 76.5 ms: 1.30x faster                                                    |
| 2to3                     | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| nbody                    | 166 ms                                                                | 128 ms: 1.29x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sympy_str                | 329 ms                                                                | 260 ms: 1.27x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.26x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 923 ms: 1.24x faster                                                     |
| scimark_fft              | 500 ms                                                                | 406 ms: 1.23x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.71 us: 1.23x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 58.3 ms: 1.20x faster                                                    |
| sympy_expand             | 543 ms                                                                | 453 ms: 1.20x faster                                                     |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.16x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.75 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 496 ms: 1.10x faster                                                     |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.94 us: 1.05x faster                                                    |
| async_generators         | 452 ms                                                                | 434 ms: 1.04x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 203 ms: 1.04x faster                                                     |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| unpickle                 | 17.5 us                                                               | 17.1 us: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.43 us: 1.04x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.8 us: 1.05x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.59 ms: 1.08x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.24 ms: 1.09x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.9 us: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.5 ms: 1.18x slower                                                    |
| pidigits                 | 235 ms                                                                | 292 ms: 1.24x slower                                                     |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.25x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.71 ms: 1.27x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.76 ms: 1.63x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.64 sec: 181.43x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.37x