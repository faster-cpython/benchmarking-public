# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 876 ms: 2.61x faster                                                     |
| async_tree_none         | 950 ms                                                                | 392 ms: 2.42x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 660 ms: 1.93x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.6 ms: 1.57x faster                                                    |
| nbody          | 166 ms                                                                | 128 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.4 ms: 1.13x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 246 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 78.4 ms: 1.27x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.35 us: 1.10x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.63 us: 1.07x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.10x slower                                                    |
| json_loads           | 30.9 us                                                               | 35.0 us: 1.13x slower                                                    |
| pickle               | 12.5 us                                                               | 15.5 us: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                    |
| mako            | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 59.0 ms: 1.18x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 876 ms: 2.61x faster                                                     |
| async_tree_none          | 950 ms                                                                | 392 ms: 2.42x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.79 ms: 2.36x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.25x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 660 ms: 1.93x faster                                                     |
| go                       | 264 ms                                                                | 137 ms: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                                    |
| richards_super           | 107 ms                                                                | 57.3 ms: 1.87x faster                                                    |
| raytrace                 | 573 ms                                                                | 313 ms: 1.83x faster                                                     |
| richards                 | 91.7 ms                                                               | 50.7 ms: 1.81x faster                                                    |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                                    |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 550 ms: 1.72x faster                                                     |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                     |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                     |
| float                    | 135 ms                                                                | 85.6 ms: 1.57x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.3 ms: 1.57x faster                                                    |
| pylint                   | 485 ms                                                                | 310 ms: 1.56x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.5 us: 1.56x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.0 ms: 1.54x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.51x faster                                                   |
| deepcopy                 | 511 us                                                                | 340 us: 1.50x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.30 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                                     |
| pyflate                  | 795 ms                                                                | 554 ms: 1.43x faster                                                     |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 53.7 ms: 1.37x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 63.3 ms: 1.37x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                    |
| nbody                    | 166 ms                                                                | 128 ms: 1.30x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                    |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                     |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 78.4 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.68 us: 1.25x faster                                                    |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 938 ms: 1.22x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.94 sec: 1.22x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.35 ms: 1.20x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                    |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 59.0 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                                     |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 28.4 ms: 1.13x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.35 us: 1.10x faster                                                    |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                    |
| regex_dna                | 257 ms                                                                | 246 ms: 1.05x faster                                                     |
| async_generators         | 452 ms                                                                | 441 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.63 us: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.10x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.58 ms: 1.13x slower                                                    |
| json_loads               | 30.9 us                                                               | 35.0 us: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.0 ms: 1.18x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.5 us: 1.24x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.65 ms: 1.60x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.63 ms: 1.61x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.93 sec: 132.84x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                             |

Benchmark hidden because not significant (2): pidigits, unpickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.345x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.31x