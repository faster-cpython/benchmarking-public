# Results vs. 3.10.4

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.199x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 373 ms: 1.02x faster                                                        |
| docutils       | 3.53 sec                                                              | 3.66 sec: 1.04x slower                                                      |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                       |
| tornado_http   | 178 ms                                                                | 150 ms: 1.19x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 458 ms: 2.07x faster                                                        |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                      |
| async_tree_memoization  | 1.13 sec                                                              | 605 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 760 ms: 1.68x faster                                                        |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 108 ms: 1.54x faster                                                        |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 165 ms: 1.07x faster                                                        |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 377 us: 1.40x faster                                                        |
| unpickle_pure_python | 366 us                                                                | 264 us: 1.38x faster                                                        |
| tomli_loads          | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                      |
| xml_etree_process    | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                       |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                        |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                        |
| unpickle_list        | 6.99 us                                                               | 6.66 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                        |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                                       |
| json_loads           | 30.9 us                                                               | 31.5 us: 1.02x slower                                                       |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.08x slower                                                       |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                                       |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                       |
| python_startup         | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                       |
| genshi_text     | 35.2 ms                                                               | 32.2 ms: 1.09x faster                                                       |
| django_template | 53.3 ms                                                               | 49.0 ms: 1.09x faster                                                       |
| genshi_xml      | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                        |
| deltablue                | 8.94 ms                                                               | 4.15 ms: 2.16x faster                                                       |
| async_tree_none          | 950 ms                                                                | 458 ms: 2.07x faster                                                        |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                      |
| async_tree_memoization   | 1.13 sec                                                              | 605 ms: 1.87x faster                                                        |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 760 ms: 1.68x faster                                                        |
| raytrace                 | 573 ms                                                                | 350 ms: 1.64x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 83.0 ms: 1.61x faster                                                       |
| richards_super           | 107 ms                                                                | 67.9 ms: 1.58x faster                                                       |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                                        |
| chaos                    | 121 ms                                                                | 78.8 ms: 1.54x faster                                                       |
| nbody                    | 166 ms                                                                | 108 ms: 1.54x faster                                                        |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                        |
| asyncio_tcp              | 944 ms                                                                | 618 ms: 1.53x faster                                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                       |
| richards                 | 91.7 ms                                                               | 60.9 ms: 1.51x faster                                                       |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 86.4 ms: 1.48x faster                                                       |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                        |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                      |
| comprehensions           | 33.1 us                                                               | 23.3 us: 1.42x faster                                                       |
| generators               | 68.1 ms                                                               | 48.3 ms: 1.41x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 377 us: 1.40x faster                                                        |
| deepcopy                 | 511 us                                                                | 366 us: 1.40x faster                                                        |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.38x faster                                                        |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 2.10 ms: 1.35x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.49 sec: 1.35x faster                                                      |
| logging_simple           | 9.78 us                                                               | 7.35 us: 1.33x faster                                                       |
| logging_format           | 10.6 us                                                               | 8.04 us: 1.32x faster                                                       |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                       |
| thrift                   | 1.26 ms                                                               | 977 us: 1.29x faster                                                        |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                        |
| xml_etree_process        | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 3.78 us: 1.22x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                       |
| tornado_http             | 178 ms                                                                | 150 ms: 1.19x faster                                                        |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                                        |
| fannkuch                 | 546 ms                                                                | 463 ms: 1.18x faster                                                        |
| pycparser                | 1.69 sec                                                              | 1.45 sec: 1.17x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                       |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                       |
| hexiom                   | 10.9 ms                                                               | 9.54 ms: 1.14x faster                                                       |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                        |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.94 ms: 1.10x faster                                                       |
| genshi_text              | 35.2 ms                                                               | 32.2 ms: 1.09x faster                                                       |
| django_template          | 53.3 ms                                                               | 49.0 ms: 1.09x faster                                                       |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                       |
| json                     | 5.88 ms                                                               | 5.48 ms: 1.07x faster                                                       |
| regex_compile            | 177 ms                                                                | 165 ms: 1.07x faster                                                        |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                      |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                                        |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                        |
| unpickle_list            | 6.99 us                                                               | 6.66 us: 1.05x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                        |
| sqlglot_normalize        | 156 ms                                                                | 151 ms: 1.03x faster                                                        |
| 2to3                     | 381 ms                                                                | 373 ms: 1.02x faster                                                        |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                                       |
| asyncio_websockets       | 657 ms                                                                | 660 ms: 1.00x slower                                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                                      |
| json_loads               | 30.9 us                                                               | 31.5 us: 1.02x slower                                                       |
| pprint_pformat           | 2.36 sec                                                              | 2.42 sec: 1.03x slower                                                      |
| docutils                 | 3.53 sec                                                              | 3.66 sec: 1.04x slower                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 79.3 ms: 1.05x slower                                                       |
| sympy_str                | 329 ms                                                                | 347 ms: 1.05x slower                                                        |
| sympy_expand             | 543 ms                                                                | 580 ms: 1.07x slower                                                        |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.08x slower                                                       |
| sympy_integrate          | 26.5 ms                                                               | 29.1 ms: 1.10x slower                                                       |
| dulwich_log              | 73.5 ms                                                               | 80.8 ms: 1.10x slower                                                       |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                                       |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                       |
| async_generators         | 452 ms                                                                | 508 ms: 1.12x slower                                                        |
| genshi_xml               | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                       |
| telco                    | 8.49 ms                                                               | 9.57 ms: 1.13x slower                                                       |
| sympy_sum                | 184 ms                                                                | 211 ms: 1.15x slower                                                        |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                       |
| coverage                 | 83.6 ms                                                               | 98.5 ms: 1.18x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                       |
| python_startup           | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 6.34 ms: 1.53x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.73 ms: 1.65x slower                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 2.16 sec: 148.72x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                                |

Benchmark hidden because not significant (4): regex_v8, nqueens, pidigits, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.199x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.37x