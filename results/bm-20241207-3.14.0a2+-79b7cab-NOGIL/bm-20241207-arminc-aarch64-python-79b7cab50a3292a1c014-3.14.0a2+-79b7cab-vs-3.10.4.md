# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.105x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 468 ms: 1.23x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.77 sec: 1.07x slower                                                   |
| html5lib       | 86.5 ms                                                               | 118 ms: 1.36x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.31 sec: 1.74x faster                                                   |
| async_tree_none         | 950 ms                                                                | 592 ms: 1.60x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 708 ms: 1.60x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 900 ms: 1.41x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.59x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 235 ms                                                                | 232 ms: 1.01x faster                                                     |
| nbody          | 166 ms                                                                | 183 ms: 1.10x slower                                                     |
| float          | 135 ms                                                                | 198 ms: 1.47x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 34.0 ms: 1.06x slower                                                    |
| regex_compile  | 177 ms                                                                | 203 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.69 sec: 1.10x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 19.3 ms: 1.15x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 116 ms: 1.17x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 144 ms: 1.17x slower                                                     |
| json_loads           | 30.9 us                                                               | 37.1 us: 1.20x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 459 us: 1.25x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 668 us: 1.26x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.8 ms: 1.85x slower                                                    |
| python_startup         | 11.2 ms                                                               | 21.6 ms: 1.93x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.89x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 84.5 ms: 1.21x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 43.3 ms: 1.23x slower                                                    |
| django_template | 53.3 ms                                                               | 68.5 ms: 1.28x slower                                                    |
| mako            | 18.9 ms                                                               | 26.3 ms: 1.39x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 284 us: 2.33x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.31 sec: 1.74x faster                                                   |
| async_tree_none          | 950 ms                                                                | 592 ms: 1.60x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 708 ms: 1.60x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 900 ms: 1.41x faster                                                     |
| generators               | 68.1 ms                                                               | 56.4 ms: 1.21x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| deepcopy                 | 511 us                                                                | 449 us: 1.14x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 118 ms: 1.13x faster                                                     |
| coroutines               | 37.2 ms                                                               | 33.4 ms: 1.11x faster                                                    |
| spectral_norm            | 186 ms                                                                | 168 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| pidigits                 | 235 ms                                                                | 232 ms: 1.01x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 687 ms: 1.05x slower                                                     |
| regex_v8                 | 32.2 ms                                                               | 34.0 ms: 1.06x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.77 sec: 1.07x slower                                                   |
| scimark_fft              | 500 ms                                                                | 536 ms: 1.07x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.94 us: 1.07x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.23 ms: 1.08x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.69 sec: 1.10x slower                                                   |
| nbody                    | 166 ms                                                                | 183 ms: 1.10x slower                                                     |
| mdp                      | 3.70 sec                                                              | 4.10 sec: 1.11x slower                                                   |
| richards_super           | 107 ms                                                                | 119 ms: 1.11x slower                                                     |
| json                     | 5.88 ms                                                               | 6.55 ms: 1.12x slower                                                    |
| chaos                    | 121 ms                                                                | 136 ms: 1.12x slower                                                     |
| pycparser                | 1.69 sec                                                              | 1.91 sec: 1.13x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 179 ms: 1.15x slower                                                     |
| regex_compile            | 177 ms                                                                | 203 ms: 1.15x slower                                                     |
| richards                 | 91.7 ms                                                               | 106 ms: 1.15x slower                                                     |
| json_dumps               | 16.7 ms                                                               | 19.3 ms: 1.15x slower                                                    |
| pyflate                  | 795 ms                                                                | 927 ms: 1.17x slower                                                     |
| xml_etree_process        | 99.5 ms                                                               | 116 ms: 1.17x slower                                                     |
| comprehensions           | 33.1 us                                                               | 38.7 us: 1.17x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 144 ms: 1.17x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 12.8 ms: 1.18x slower                                                    |
| nqueens                  | 117 ms                                                                | 138 ms: 1.18x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.36 sec: 1.19x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.80 sec: 1.19x slower                                                   |
| logging_silent           | 222 ns                                                                | 265 ns: 1.19x slower                                                     |
| scimark_lu               | 227 ms                                                                | 271 ms: 1.19x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.1 us: 1.20x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 88.9 ms: 1.21x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 84.5 ms: 1.21x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.06 ms: 1.22x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 92.2 ms: 1.22x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 32.6 ms: 1.23x slower                                                    |
| 2to3                     | 381 ms                                                                | 468 ms: 1.23x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 43.3 ms: 1.23x slower                                                    |
| meteor_contest           | 126 ms                                                                | 158 ms: 1.25x slower                                                     |
| unpickle_pure_python     | 366 us                                                                | 459 us: 1.25x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 2.00 ms: 1.26x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 668 us: 1.26x slower                                                     |
| fannkuch                 | 546 ms                                                                | 690 ms: 1.26x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.60 ms: 1.27x slower                                                    |
| scimark_sor              | 246 ms                                                                | 314 ms: 1.28x slower                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 164 ms: 1.28x slower                                                     |
| raytrace                 | 573 ms                                                                | 736 ms: 1.28x slower                                                     |
| django_template          | 53.3 ms                                                               | 68.5 ms: 1.28x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.94 ms: 1.30x slower                                                    |
| logging_format           | 10.6 us                                                               | 14.0 us: 1.32x slower                                                    |
| deltablue                | 8.94 ms                                                               | 11.8 ms: 1.32x slower                                                    |
| logging_simple           | 9.78 us                                                               | 13.1 us: 1.34x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 118 ms: 1.36x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 271 ms: 1.37x slower                                                     |
| mako                     | 18.9 ms                                                               | 26.3 ms: 1.39x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.8 ms: 1.39x slower                                                    |
| sympy_str                | 329 ms                                                                | 458 ms: 1.39x slower                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 3.96 ms: 1.39x slower                                                    |
| async_generators         | 452 ms                                                                | 637 ms: 1.41x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.38 ms: 1.41x slower                                                    |
| go                       | 264 ms                                                                | 373 ms: 1.41x slower                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 29.1 ms: 1.42x slower                                                    |
| float                    | 135 ms                                                                | 198 ms: 1.47x slower                                                     |
| sympy_sum                | 184 ms                                                                | 287 ms: 1.56x slower                                                     |
| sympy_expand             | 543 ms                                                                | 859 ms: 1.58x slower                                                     |
| coverage                 | 83.6 ms                                                               | 136 ms: 1.63x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.8 ms: 1.85x slower                                                    |
| python_startup           | 11.2 ms                                                               | 21.6 ms: 1.93x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 66.8 ms: 4.60x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.16x slower                                                             |

Benchmark hidden because not significant (5): deepcopy_memo, pylint, sqlite_synth, pathlib, regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.105x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.56x