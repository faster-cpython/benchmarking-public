# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.09x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 385 ms: 1.01x slower                                                      |
| docutils       | 3.53 sec                                                              | 3.62 sec: 1.02x slower                                                    |
| html5lib       | 86.5 ms                                                               | 71.1 ms: 1.22x faster                                                     |
| tornado_http   | 178 ms                                                                | 146 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 458 ms: 2.07x faster                                                      |
| async_tree_io           | 2.28 sec                                                              | 1.16 sec: 1.98x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 603 ms: 1.88x faster                                                      |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 755 ms: 1.69x faster                                                      |
| Geometric mean          | (ref)                                                                 | 1.90x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                                      |
| float          | 135 ms                                                                | 97.2 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                      |
| regex_v8       | 32.2 ms                                                               | 31.4 ms: 1.03x faster                                                     |
| regex_compile  | 177 ms                                                                | 183 ms: 1.03x slower                                                      |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                      |
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                      |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                      |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                      |
| unpickle_list        | 6.99 us                                                               | 6.50 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                      |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.03x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                     |
| unpickle             | 17.5 us                                                               | 19.0 us: 1.09x slower                                                     |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                     |
| python_startup         | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                     |
| django_template | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                     |
| genshi_text     | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                     |
| genshi_xml      | 69.8 ms                                                               | 84.6 ms: 1.21x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 218 us: 3.03x faster                                                      |
| async_tree_none          | 950 ms                                                                | 458 ms: 2.07x faster                                                      |
| async_tree_io            | 2.28 sec                                                              | 1.16 sec: 1.98x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.63 ms: 1.93x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 603 ms: 1.88x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 755 ms: 1.69x faster                                                      |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                      |
| raytrace                 | 573 ms                                                                | 352 ms: 1.63x faster                                                      |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                      |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                     |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                      |
| richards_super           | 107 ms                                                                | 71.7 ms: 1.50x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.7 ms: 1.48x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 639 ms: 1.48x faster                                                      |
| richards                 | 91.7 ms                                                               | 63.8 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.44x faster                                                    |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                      |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 90.7 ms: 1.41x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.40x faster                                                     |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                                      |
| chaos                    | 121 ms                                                                | 87.2 ms: 1.39x faster                                                     |
| float                    | 135 ms                                                                | 97.2 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                      |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                      |
| deepcopy                 | 511 us                                                                | 379 us: 1.35x faster                                                      |
| comprehensions           | 33.1 us                                                               | 24.9 us: 1.33x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.41 us: 1.32x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.06 us: 1.32x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                     |
| thrift                   | 1.26 ms                                                               | 979 us: 1.29x faster                                                      |
| sqlglot_transpile        | 2.84 ms                                                               | 2.24 ms: 1.27x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                    |
| pyflate                  | 795 ms                                                                | 643 ms: 1.24x faster                                                      |
| xml_etree_process        | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                     |
| tornado_http             | 178 ms                                                                | 146 ms: 1.22x faster                                                      |
| html5lib                 | 86.5 ms                                                               | 71.1 ms: 1.22x faster                                                     |
| spectral_norm            | 186 ms                                                                | 155 ms: 1.21x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                     |
| generators               | 68.1 ms                                                               | 58.9 ms: 1.16x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.99 us: 1.15x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                      |
| pycparser                | 1.69 sec                                                              | 1.52 sec: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                      |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                      |
| unpickle_list            | 6.99 us                                                               | 6.50 us: 1.08x faster                                                     |
| fannkuch                 | 546 ms                                                                | 508 ms: 1.08x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.16 ms: 1.06x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                     |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                      |
| django_template          | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                      |
| genshi_text              | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.4 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                     |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                      |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                      |
| 2to3                     | 381 ms                                                                | 385 ms: 1.01x slower                                                      |
| docutils                 | 3.53 sec                                                              | 3.62 sec: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.03x slower                                                     |
| regex_compile            | 177 ms                                                                | 183 ms: 1.03x slower                                                      |
| nqueens                  | 117 ms                                                                | 123 ms: 1.05x slower                                                      |
| dulwich_log              | 73.5 ms                                                               | 77.4 ms: 1.05x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.0 us: 1.09x slower                                                     |
| sympy_expand             | 543 ms                                                                | 592 ms: 1.09x slower                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 82.9 ms: 1.10x slower                                                     |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 29.3 ms: 1.10x slower                                                     |
| sympy_str                | 329 ms                                                                | 363 ms: 1.11x slower                                                      |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.11x slower                                                    |
| async_generators         | 452 ms                                                                | 513 ms: 1.13x slower                                                      |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.89 ms: 1.17x slower                                                     |
| sympy_sum                | 184 ms                                                                | 216 ms: 1.18x slower                                                      |
| coverage                 | 83.6 ms                                                               | 98.8 ms: 1.18x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 84.6 ms: 1.21x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                     |
| python_startup           | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 6.23 ms: 1.50x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                     |
| bench_mp_pool            | 14.5 ms                                                               | 1.92 sec: 132.35x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                              |

Benchmark hidden because not significant (4): pickle_list, pidigits, sqlglot_normalize, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x