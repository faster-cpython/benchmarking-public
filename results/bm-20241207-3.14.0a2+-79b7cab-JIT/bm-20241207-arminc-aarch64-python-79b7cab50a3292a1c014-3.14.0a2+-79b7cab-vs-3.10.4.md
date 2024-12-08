# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                   |
| html5lib       | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 946 ms: 2.41x faster                                                     |
| async_tree_none         | 950 ms                                                                | 423 ms: 2.25x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 547 ms: 2.07x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 719 ms: 1.77x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.11x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 94.4 ms: 1.43x faster                                                    |
| nbody          | 166 ms                                                                | 118 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| regex_dna      | 257 ms                                                                | 264 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.39x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 408 us: 1.30x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.18 ms: 1.33x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| django_template | 53.3 ms                                                               | 48.4 ms: 1.10x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 32.7 ms: 1.08x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 220 us: 3.01x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 946 ms: 2.41x faster                                                     |
| async_tree_none          | 950 ms                                                                | 423 ms: 2.25x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.14 ms: 2.16x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 547 ms: 2.07x faster                                                     |
| richards_super           | 107 ms                                                                | 59.8 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 719 ms: 1.77x faster                                                     |
| richards                 | 91.7 ms                                                               | 56.7 ms: 1.62x faster                                                    |
| raytrace                 | 573 ms                                                                | 361 ms: 1.59x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 40.1 us: 1.54x faster                                                    |
| logging_silent           | 222 ns                                                                | 146 ns: 1.52x faster                                                     |
| scimark_sor              | 246 ms                                                                | 164 ms: 1.50x faster                                                     |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.48x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.63 ms: 1.47x faster                                                    |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 88.5 ms: 1.44x faster                                                    |
| pylint                   | 485 ms                                                                | 336 ms: 1.44x faster                                                     |
| chaos                    | 121 ms                                                                | 84.1 ms: 1.44x faster                                                    |
| float                    | 135 ms                                                                | 94.4 ms: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 94.2 ms: 1.42x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                    |
| nbody                    | 166 ms                                                                | 118 ms: 1.40x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.39x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                    |
| generators               | 68.1 ms                                                               | 50.5 ms: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.3 us: 1.31x faster                                                    |
| pyflate                  | 795 ms                                                                | 610 ms: 1.30x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 408 us: 1.30x faster                                                     |
| deepcopy                 | 511 us                                                                | 396 us: 1.29x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.4 ms: 1.25x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| regex_compile            | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.90 us: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                                   |
| thrift                   | 1.26 ms                                                               | 1.04 ms: 1.21x faster                                                    |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                     |
| 2to3                     | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.89 us: 1.19x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.35 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.05 us: 1.13x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| sympy_sum                | 184 ms                                                                | 166 ms: 1.11x faster                                                     |
| scimark_fft              | 500 ms                                                                | 452 ms: 1.11x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                   |
| django_template          | 53.3 ms                                                               | 48.4 ms: 1.10x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 24.1 ms: 1.10x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 69.7 ms: 1.08x faster                                                    |
| sympy_str                | 329 ms                                                                | 304 ms: 1.08x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 145 ms: 1.08x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 32.7 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.13 ms: 1.07x faster                                                    |
| fannkuch                 | 546 ms                                                                | 512 ms: 1.07x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 69.6 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                    |
| sympy_expand             | 543 ms                                                                | 523 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.59 sec: 1.03x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.03 us: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                     |
| regex_dna                | 257 ms                                                                | 264 ms: 1.03x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.11x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.63 sec: 1.12x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| nqueens                  | 117 ms                                                                | 134 ms: 1.14x slower                                                     |
| async_generators         | 452 ms                                                                | 528 ms: 1.17x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.18 ms: 1.33x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.23 ms: 1.43x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.74 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.46 sec: 100.18x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (5): regex_effbot, meteor_contest, regex_v8, pidigits, json_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.32x