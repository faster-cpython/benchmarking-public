# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 370 ms: 1.03x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.2 ms: 1.21x faster                                                   |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 500 ms: 1.90x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.24 sec: 1.84x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 664 ms: 1.71x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 799 ms: 1.59x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.76x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.2 ms: 1.53x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 279 us: 1.31x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.65 us: 1.05x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.8 ms: 1.41x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.2 ms: 1.63x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.51x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 49.0 ms: 1.09x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 79.0 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.10x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.21x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.41 ms: 2.03x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.50 ms: 1.94x faster                                                   |
| async_tree_none          | 950 ms                                                                | 500 ms: 1.90x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.24 sec: 1.84x faster                                                  |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 38.8 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.5 ms: 1.74x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 664 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.8 ms: 1.67x faster                                                   |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.5 us: 1.60x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 799 ms: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.5 ms: 1.57x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 611 ms: 1.55x faster                                                    |
| float                    | 135 ms                                                                | 88.2 ms: 1.53x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 85.1 ms: 1.50x faster                                                   |
| go                       | 264 ms                                                                | 176 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| comprehensions           | 33.1 us                                                               | 23.0 us: 1.44x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 174 ms: 1.41x faster                                                    |
| chaos                    | 121 ms                                                                | 86.7 ms: 1.40x faster                                                   |
| deepcopy                 | 511 us                                                                | 378 us: 1.35x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.25 us: 1.35x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.88 us: 1.35x faster                                                   |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 958 us: 1.32x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 279 us: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| scimark_lu               | 227 ms                                                                | 181 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 71.2 ms: 1.21x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.00 ms: 1.21x faster                                                   |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                    |
| pylint                   | 485 ms                                                                | 418 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.03 us: 1.14x faster                                                   |
| dask                     | 450 ms                                                                | 396 ms: 1.14x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.89 ms: 1.11x faster                                                   |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| django_template          | 53.3 ms                                                               | 49.0 ms: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 70.0 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                                  |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.65 us: 1.05x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.5 ms: 1.05x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                  |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                    |
| 2to3                     | 381 ms                                                                | 370 ms: 1.03x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.03x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 26.2 ms: 1.01x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| sympy_str                | 329 ms                                                                | 332 ms: 1.01x slower                                                    |
| sympy_expand             | 543 ms                                                                | 550 ms: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.58 sec: 1.02x slower                                                  |
| sympy_sum                | 184 ms                                                                | 188 ms: 1.02x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 76.2 ms: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 122 ms: 1.04x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 79.0 ms: 1.13x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.85 ms: 1.14x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.97 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.01 ms: 1.21x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.21x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.8 ms: 1.41x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 11.2 ms: 1.63x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (4): regex_compile, pidigits, asyncio_websockets, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.25x