# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 886 ms: 2.58x faster                                                     |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.39x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 479 ms: 2.37x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 81.4 ms: 1.65x faster                                                    |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.40 sec: 1.40x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 77.6 ms: 1.28x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.36 us: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.10x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.85 us: 1.12x slower                                                    |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| pickle               | 12.5 us                                                               | 15.4 us: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| django_template | 53.3 ms                                                               | 40.3 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.13x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 886 ms: 2.58x faster                                                     |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.39x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 479 ms: 2.37x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.81 ms: 2.35x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.63 sec: 2.26x faster                                                   |
| richards_super           | 107 ms                                                                | 53.5 ms: 2.00x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 35.5 ms: 1.92x faster                                                    |
| richards                 | 91.7 ms                                                               | 48.1 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 545 ms: 1.73x faster                                                     |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 36.3 us: 1.70x faster                                                    |
| chaos                    | 121 ms                                                                | 72.0 ms: 1.68x faster                                                    |
| float                    | 135 ms                                                                | 81.4 ms: 1.65x faster                                                    |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                                     |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                                     |
| go                       | 264 ms                                                                | 171 ms: 1.55x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 83.8 ms: 1.53x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| pylint                   | 485 ms                                                                | 320 ms: 1.51x faster                                                     |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                     |
| spectral_norm            | 186 ms                                                                | 126 ms: 1.48x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 94.9 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.40x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.40 sec: 1.40x faster                                                   |
| pyflate                  | 795 ms                                                                | 567 ms: 1.40x faster                                                     |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.91 ms: 1.38x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.70 us: 1.38x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.3 us: 1.36x faster                                                    |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 54.9 ms: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                     |
| django_template          | 53.3 ms                                                               | 40.3 ms: 1.32x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 77.6 ms: 1.28x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.69 us: 1.24x faster                                                    |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.22x faster                                                   |
| scimark_fft              | 500 ms                                                                | 414 ms: 1.21x faster                                                     |
| sympy_str                | 329 ms                                                                | 272 ms: 1.21x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.49 ms: 1.17x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.68 us: 1.12x faster                                                    |
| sympy_expand             | 543 ms                                                                | 486 ms: 1.12x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.36 us: 1.10x faster                                                    |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                     |
| fannkuch                 | 546 ms                                                                | 498 ms: 1.10x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                    |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.40 sec: 1.02x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| async_generators         | 452 ms                                                                | 471 ms: 1.04x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.10x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.85 us: 1.12x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.79 ms: 1.15x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.18x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.4 us: 1.24x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.62 ms: 1.59x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.09 sec: 75.07x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (4): meteor_contest, json, unpickle, pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.33x