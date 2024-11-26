# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: linux-aarch64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.294x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                 |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                               |
| html5lib       | 86.5 ms                                                               | 66.0 ms: 1.31x faster                                                |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 448 ms: 2.12x faster                                                 |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                               |
| async_tree_memoization  | 1.13 sec                                                              | 603 ms: 1.88x faster                                                 |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 760 ms: 1.67x faster                                                 |
| Geometric mean          | (ref)                                                                 | 1.90x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 135 ms                                                                | 96.8 ms: 1.39x faster                                                |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                 |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                 |
| regex_effbot   | 4.25 ms                                                               | 5.17 ms: 1.22x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                 |
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                 |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                               |
| xml_etree_process    | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                 |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                                |
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                |
| django_template | 53.3 ms                                                               | 41.2 ms: 1.29x faster                                                |
| genshi_text     | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                |
| genshi_xml      | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.24x faster                                                 |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                                |
| async_tree_none          | 950 ms                                                                | 448 ms: 2.12x faster                                                 |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                               |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                |
| async_tree_memoization   | 1.13 sec                                                              | 603 ms: 1.88x faster                                                 |
| go                       | 264 ms                                                                | 143 ms: 1.84x faster                                                 |
| raytrace                 | 573 ms                                                                | 321 ms: 1.79x faster                                                 |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                                |
| richards_super           | 107 ms                                                                | 62.7 ms: 1.71x faster                                                |
| chaos                    | 121 ms                                                                | 71.3 ms: 1.70x faster                                                |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 760 ms: 1.67x faster                                                 |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                 |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.63x faster                                                |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                 |
| crypto_pyaes             | 134 ms                                                                | 85.0 ms: 1.58x faster                                                |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                 |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.54x faster                                                |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                                |
| sqlglot_transpile        | 2.84 ms                                                               | 1.86 ms: 1.53x faster                                                |
| deepcopy_memo            | 61.7 us                                                               | 40.6 us: 1.52x faster                                                |
| hexiom                   | 10.9 ms                                                               | 7.34 ms: 1.49x faster                                                |
| deepcopy                 | 511 us                                                                | 353 us: 1.45x faster                                                 |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.44x faster                                                 |
| float                    | 135 ms                                                                | 96.8 ms: 1.39x faster                                                |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                 |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                 |
| pyflate                  | 795 ms                                                                | 582 ms: 1.37x faster                                                 |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                 |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                 |
| pylint                   | 485 ms                                                                | 365 ms: 1.33x faster                                                 |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                               |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                 |
| html5lib                 | 86.5 ms                                                               | 66.0 ms: 1.31x faster                                                |
| logging_format           | 10.6 us                                                               | 8.15 us: 1.30x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.52 us: 1.30x faster                                                |
| django_template          | 53.3 ms                                                               | 41.2 ms: 1.29x faster                                                |
| thrift                   | 1.26 ms                                                               | 980 us: 1.29x faster                                                 |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                 |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.27x faster                                                |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                                |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.26x faster                                                |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                 |
| dulwich_log              | 73.5 ms                                                               | 59.6 ms: 1.23x faster                                                |
| sympy_str                | 329 ms                                                                | 266 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.22 ms: 1.23x faster                                                |
| genshi_text              | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                                |
| xml_etree_process        | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                |
| pprint_pformat           | 2.36 sec                                                              | 1.96 sec: 1.20x faster                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 955 ms: 1.20x faster                                                 |
| sympy_integrate          | 26.5 ms                                                               | 22.1 ms: 1.20x faster                                                |
| sqlglot_optimize         | 75.4 ms                                                               | 63.1 ms: 1.20x faster                                                |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                 |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                |
| sqlglot_normalize        | 156 ms                                                                | 135 ms: 1.15x faster                                                 |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                 |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                               |
| sympy_expand             | 543 ms                                                                | 479 ms: 1.13x faster                                                 |
| genshi_xml               | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                |
| fannkuch                 | 546 ms                                                                | 491 ms: 1.11x faster                                                 |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.07x faster                                               |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                 |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                 |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                 |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                 |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                 |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                |
| async_generators         | 452 ms                                                                | 500 ms: 1.10x slower                                                 |
| telco                    | 8.49 ms                                                               | 9.91 ms: 1.17x slower                                                |
| regex_effbot             | 4.25 ms                                                               | 5.17 ms: 1.22x slower                                                |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                                |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                |
| gc_traversal             | 4.15 ms                                                               | 6.66 ms: 1.60x slower                                                |
| create_gc_cycles         | 2.26 ms                                                               | 3.93 ms: 1.74x slower                                                |
| bench_mp_pool            | 14.5 ms                                                               | 6.73 sec: 462.74x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, json, regex_v8, pidigits, sqlite_synth
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.294x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x