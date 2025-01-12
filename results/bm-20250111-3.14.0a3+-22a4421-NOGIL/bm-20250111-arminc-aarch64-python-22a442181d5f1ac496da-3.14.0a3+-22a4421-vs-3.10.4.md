# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.043x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 458 ms: 1.20x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.68 sec: 1.04x slower                                                   |
| html5lib       | 86.5 ms                                                               | 110 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                   |
| async_tree_none         | 950 ms                                                                | 543 ms: 1.75x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 666 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 840 ms: 1.51x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.71x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 150 ms: 1.11x slower                                                     |
| nbody          | 166 ms                                                                | 185 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| regex_compile  | 177 ms                                                                | 186 ms: 1.06x slower                                                     |
| regex_v8       | 32.2 ms                                                               | 34.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 136 ms: 1.15x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 7.52 us: 1.08x slower                                                    |
| json_dumps           | 16.7 ms                                                               | 18.4 ms: 1.10x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 111 ms: 1.11x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 40.2 us: 1.15x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.02 us: 1.15x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 143 ms: 1.16x slower                                                     |
| json_loads           | 30.9 us                                                               | 36.4 us: 1.18x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.9 us: 1.20x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 440 us: 1.20x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 661 us: 1.25x slower                                                     |
| pickle               | 12.5 us                                                               | 16.0 us: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.80x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 39.7 ms: 1.13x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                    |
| django_template | 53.3 ms                                                               | 64.2 ms: 1.20x slower                                                    |
| mako            | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 276 us: 2.40x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                   |
| async_tree_none          | 950 ms                                                                | 543 ms: 1.75x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 666 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 840 ms: 1.51x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 647 ms: 1.46x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.61 sec: 1.26x faster                                                   |
| spectral_norm            | 186 ms                                                                | 150 ms: 1.24x faster                                                     |
| generators               | 68.1 ms                                                               | 55.4 ms: 1.23x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 136 ms: 1.15x faster                                                     |
| deepcopy                 | 511 us                                                                | 446 us: 1.15x faster                                                     |
| coroutines               | 37.2 ms                                                               | 32.6 ms: 1.14x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 119 ms: 1.12x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.8 ms: 1.11x faster                                                    |
| pylint                   | 485 ms                                                                | 443 ms: 1.10x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.08x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 683 ms: 1.04x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.68 sec: 1.04x slower                                                   |
| chaos                    | 121 ms                                                                | 126 ms: 1.04x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.81 us: 1.05x slower                                                    |
| scimark_sor              | 246 ms                                                                | 258 ms: 1.05x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.33 ms: 1.05x slower                                                    |
| regex_compile            | 177 ms                                                                | 186 ms: 1.06x slower                                                     |
| unpickle_list            | 6.99 us                                                               | 7.52 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.22 ms: 1.08x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.00 sec: 1.08x slower                                                   |
| regex_v8                 | 32.2 ms                                                               | 34.9 ms: 1.08x slower                                                    |
| json                     | 5.88 ms                                                               | 6.38 ms: 1.09x slower                                                    |
| pyflate                  | 795 ms                                                                | 866 ms: 1.09x slower                                                     |
| json_dumps               | 16.7 ms                                                               | 18.4 ms: 1.10x slower                                                    |
| logging_simple           | 9.78 us                                                               | 10.8 us: 1.11x slower                                                    |
| float                    | 135 ms                                                                | 150 ms: 1.11x slower                                                     |
| nbody                    | 166 ms                                                                | 185 ms: 1.11x slower                                                     |
| xml_etree_process        | 99.5 ms                                                               | 111 ms: 1.11x slower                                                     |
| logging_format           | 10.6 us                                                               | 11.8 us: 1.11x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 143 ms: 1.12x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 12.2 ms: 1.12x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 83.0 ms: 1.13x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 39.7 ms: 1.13x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 30.1 ms: 1.13x slower                                                    |
| raytrace                 | 573 ms                                                                | 655 ms: 1.14x slower                                                     |
| sympy_sum                | 184 ms                                                                | 210 ms: 1.14x slower                                                     |
| nqueens                  | 117 ms                                                                | 134 ms: 1.15x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 40.2 us: 1.15x slower                                                    |
| comprehensions           | 33.1 us                                                               | 38.0 us: 1.15x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.32 sec: 1.15x slower                                                   |
| pickle_list              | 5.24 us                                                               | 6.02 us: 1.15x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 87.1 ms: 1.16x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.73 sec: 1.16x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 143 ms: 1.16x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 181 ms: 1.16x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 231 ms: 1.17x slower                                                     |
| json_loads               | 30.9 us                                                               | 36.4 us: 1.18x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.9 us: 1.20x slower                                                    |
| 2to3                     | 381 ms                                                                | 458 ms: 1.20x slower                                                     |
| deltablue                | 8.94 ms                                                               | 10.8 ms: 1.20x slower                                                    |
| django_template          | 53.3 ms                                                               | 64.2 ms: 1.20x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 440 us: 1.20x slower                                                     |
| logging_silent           | 222 ns                                                                | 269 ns: 1.21x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 5.03 ms: 1.21x slower                                                    |
| sympy_str                | 329 ms                                                                | 401 ms: 1.22x slower                                                     |
| sympy_expand             | 543 ms                                                                | 665 ms: 1.23x slower                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 3.49 ms: 1.23x slower                                                    |
| fannkuch                 | 546 ms                                                                | 674 ms: 1.23x slower                                                     |
| pickle_pure_python       | 529 us                                                                | 661 us: 1.25x slower                                                     |
| meteor_contest           | 126 ms                                                                | 158 ms: 1.25x slower                                                     |
| go                       | 264 ms                                                                | 332 ms: 1.25x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 2.00 ms: 1.26x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 110 ms: 1.27x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.89 ms: 1.28x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.0 us: 1.28x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 26.7 ms: 1.30x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.16 ms: 1.32x slower                                                    |
| mako                     | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                    |
| async_generators         | 452 ms                                                                | 606 ms: 1.34x slower                                                     |
| telco                    | 8.49 ms                                                               | 13.3 ms: 1.56x slower                                                    |
| coverage                 | 83.6 ms                                                               | 139 ms: 1.66x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 61.3 ms: 4.22x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.08x slower                                                             |

Benchmark hidden because not significant (9): deepcopy_memo, scimark_lu, scimark_fft, richards_super, tomli_loads, pycparser, pidigits, richards, regex_dna
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.56x