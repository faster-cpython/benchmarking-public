# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: linux-aarch64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 313 ms: 1.22x faster                                     |
| chameleon      | 10.8 ms                                                               | 9.11 ms: 1.19x faster                                    |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                   |
| html5lib       | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                    |
| tornado_http   | 178 ms                                                                | 126 ms: 1.41x faster                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                   |
| async_tree_none         | 950 ms                                                                | 507 ms: 1.87x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 674 ms: 1.68x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 784 ms: 1.62x faster                                     |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                     |
| float          | 135 ms                                                                | 97.4 ms: 1.38x faster                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 133 ms: 1.33x faster                                     |
| regex_v8       | 32.2 ms                                                               | 31.7 ms: 1.01x faster                                    |
| regex_dna      | 257 ms                                                                | 269 ms: 1.04x slower                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 373 us: 1.42x faster                                     |
| unpickle_pure_python | 366 us                                                                | 262 us: 1.39x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                    |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                    |
| xml_etree_parse      | 212 ms                                                                | 194 ms: 1.09x faster                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                     |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                    |
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.36x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                    |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                    |
| genshi_text     | 35.2 ms                                                               | 29.8 ms: 1.18x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.23x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.20x faster                                     |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                   |
| async_tree_none          | 950 ms                                                                | 507 ms: 1.87x faster                                     |
| raytrace                 | 573 ms                                                                | 308 ms: 1.86x faster                                     |
| bench_mp_pool            | 14.5 ms                                                               | 7.90 ms: 1.84x faster                                    |
| generators               | 68.1 ms                                                               | 38.0 ms: 1.79x faster                                    |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                    |
| richards_super           | 107 ms                                                                | 62.8 ms: 1.71x faster                                    |
| async_tree_memoization   | 1.13 sec                                                              | 674 ms: 1.68x faster                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                    |
| richards                 | 91.7 ms                                                               | 55.4 ms: 1.66x faster                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 784 ms: 1.62x faster                                     |
| go                       | 264 ms                                                                | 164 ms: 1.61x faster                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.79 ms: 1.59x faster                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                     |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                     |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 87.2 ms: 1.54x faster                                    |
| scimark_sor              | 246 ms                                                                | 165 ms: 1.49x faster                                     |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                     |
| hexiom                   | 10.9 ms                                                               | 7.45 ms: 1.46x faster                                    |
| pickle_pure_python       | 529 us                                                                | 373 us: 1.42x faster                                     |
| tornado_http             | 178 ms                                                                | 126 ms: 1.41x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.39x faster                                     |
| float                    | 135 ms                                                                | 97.4 ms: 1.38x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 93.6 ms: 1.36x faster                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                    |
| pylint                   | 485 ms                                                                | 361 ms: 1.35x faster                                     |
| regex_compile            | 177 ms                                                                | 133 ms: 1.33x faster                                     |
| pyflate                  | 795 ms                                                                | 604 ms: 1.32x faster                                     |
| html5lib                 | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                    |
| logging_format           | 10.6 us                                                               | 8.13 us: 1.31x faster                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                    |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.29x faster                                     |
| logging_simple           | 9.78 us                                                               | 7.60 us: 1.29x faster                                    |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                    |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.27x faster                                   |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                    |
| tomli_loads              | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                   |
| gunicorn                 | 1.45 ms                                                               | 1.15 ms: 1.25x faster                                    |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                    |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.25x faster                                     |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.23x faster                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                    |
| 2to3                     | 381 ms                                                                | 313 ms: 1.22x faster                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                    |
| chameleon                | 10.8 ms                                                               | 9.11 ms: 1.19x faster                                    |
| genshi_text              | 35.2 ms                                                               | 29.8 ms: 1.18x faster                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 977 ms: 1.17x faster                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.17x faster                                   |
| deepcopy_memo            | 61.7 us                                                               | 52.6 us: 1.17x faster                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 64.3 ms: 1.17x faster                                    |
| sqlglot_normalize        | 156 ms                                                                | 134 ms: 1.17x faster                                     |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                   |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                     |
| sympy_expand             | 543 ms                                                                | 475 ms: 1.14x faster                                     |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.72 ms: 1.13x faster                                    |
| pathlib                  | 26.3 ms                                                               | 23.6 ms: 1.11x faster                                    |
| genshi_xml               | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                    |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                     |
| scimark_fft              | 500 ms                                                                | 461 ms: 1.08x faster                                     |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                     |
| deepcopy                 | 511 us                                                                | 479 us: 1.07x faster                                     |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                   |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.38 us: 1.05x faster                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                     |
| regex_v8                 | 32.2 ms                                                               | 31.7 ms: 1.01x faster                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                     |
| async_generators         | 452 ms                                                                | 464 ms: 1.02x slower                                     |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                    |
| regex_dna                | 257 ms                                                                | 269 ms: 1.04x slower                                     |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                     |
| telco                    | 8.49 ms                                                               | 10.8 ms: 1.28x slower                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 5.92 ms: 1.43x slower                                    |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                             |

Benchmark hidden because not significant (4): json, sqlite_synth, regex_effbot, pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.27x