# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.111x faster
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 413 ms: 1.09x slower                                                           |
| docutils       | 3.53 sec                                                              | 3.83 sec: 1.08x slower                                                         |
| html5lib       | 86.5 ms                                                               | 76.4 ms: 1.13x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 489 ms: 1.94x faster                                                           |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.88x faster                                                         |
| async_tree_memoization  | 1.13 sec                                                              | 635 ms: 1.78x faster                                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 809 ms: 1.57x faster                                                           |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 108 ms: 1.25x faster                                                           |
| nbody          | 166 ms                                                                | 133 ms: 1.24x faster                                                           |
| pidigits       | 235 ms                                                                | 243 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 33.4 ms: 1.04x slower                                                          |
| regex_compile  | 177 ms                                                                | 186 ms: 1.06x slower                                                           |
| regex_dna      | 257 ms                                                                | 277 ms: 1.07x slower                                                           |
| regex_effbot   | 4.25 ms                                                               | 5.38 ms: 1.27x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 292 us: 1.25x faster                                                           |
| pickle_pure_python   | 529 us                                                                | 432 us: 1.22x faster                                                           |
| tomli_loads          | 3.36 sec                                                              | 2.82 sec: 1.19x faster                                                         |
| xml_etree_process    | 99.5 ms                                                               | 86.1 ms: 1.16x faster                                                          |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                                           |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.16 ms: 1.33x slower                                                          |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                          |
| django_template | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                          |
| genshi_text     | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                                          |
| genshi_xml      | 69.8 ms                                                               | 84.5 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 233 us: 2.83x faster                                                           |
| async_tree_none          | 950 ms                                                                | 489 ms: 1.94x faster                                                           |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.88x faster                                                         |
| async_tree_memoization   | 1.13 sec                                                              | 635 ms: 1.78x faster                                                           |
| deltablue                | 8.94 ms                                                               | 5.31 ms: 1.69x faster                                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 809 ms: 1.57x faster                                                           |
| raytrace                 | 573 ms                                                                | 402 ms: 1.43x faster                                                           |
| scimark_lu               | 227 ms                                                                | 161 ms: 1.41x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 95.3 ms: 1.41x faster                                                          |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                           |
| chaos                    | 121 ms                                                                | 90.0 ms: 1.35x faster                                                          |
| go                       | 264 ms                                                                | 197 ms: 1.34x faster                                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.80 ms: 1.34x faster                                                          |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                          |
| deepcopy_memo            | 61.7 us                                                               | 46.4 us: 1.33x faster                                                          |
| logging_silent           | 222 ns                                                                | 169 ns: 1.31x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 98.2 ms: 1.30x faster                                                          |
| richards_super           | 107 ms                                                                | 83.2 ms: 1.29x faster                                                          |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                          |
| unpickle_pure_python     | 366 us                                                                | 292 us: 1.25x faster                                                           |
| float                    | 135 ms                                                                | 108 ms: 1.25x faster                                                           |
| richards                 | 91.7 ms                                                               | 73.5 ms: 1.25x faster                                                          |
| nbody                    | 166 ms                                                                | 133 ms: 1.24x faster                                                           |
| thrift                   | 1.26 ms                                                               | 1.03 ms: 1.23x faster                                                          |
| pickle_pure_python       | 529 us                                                                | 432 us: 1.22x faster                                                           |
| logging_format           | 10.6 us                                                               | 8.67 us: 1.22x faster                                                          |
| sqlglot_transpile        | 2.84 ms                                                               | 2.35 ms: 1.21x faster                                                          |
| logging_simple           | 9.78 us                                                               | 8.11 us: 1.21x faster                                                          |
| deepcopy                 | 511 us                                                                | 427 us: 1.20x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.82 sec: 1.19x faster                                                         |
| comprehensions           | 33.1 us                                                               | 28.2 us: 1.18x faster                                                          |
| pyflate                  | 795 ms                                                                | 678 ms: 1.17x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 86.1 ms: 1.16x faster                                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.15x faster                                                          |
| generators               | 68.1 ms                                                               | 59.5 ms: 1.14x faster                                                          |
| html5lib                 | 86.5 ms                                                               | 76.4 ms: 1.13x faster                                                          |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.5 ms: 1.11x faster                                                          |
| spectral_norm            | 186 ms                                                                | 169 ms: 1.10x faster                                                           |
| deepcopy_reduce          | 4.60 us                                                               | 4.21 us: 1.09x faster                                                          |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                                           |
| pylint                   | 485 ms                                                                | 451 ms: 1.08x faster                                                           |
| django_template          | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.60 sec: 1.06x faster                                                         |
| scimark_fft              | 500 ms                                                                | 483 ms: 1.04x faster                                                           |
| fannkuch                 | 546 ms                                                                | 528 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.54 ms: 1.01x faster                                                          |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                           |
| pidigits                 | 235 ms                                                                | 243 ms: 1.03x slower                                                           |
| regex_v8                 | 32.2 ms                                                               | 33.4 ms: 1.04x slower                                                          |
| genshi_text              | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                                          |
| meteor_contest           | 126 ms                                                                | 133 ms: 1.05x slower                                                           |
| regex_compile            | 177 ms                                                                | 186 ms: 1.06x slower                                                           |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                          |
| regex_dna                | 257 ms                                                                | 277 ms: 1.07x slower                                                           |
| dulwich_log              | 73.5 ms                                                               | 79.2 ms: 1.08x slower                                                          |
| docutils                 | 3.53 sec                                                              | 3.83 sec: 1.08x slower                                                         |
| 2to3                     | 381 ms                                                                | 413 ms: 1.09x slower                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                         |
| sqlglot_normalize        | 156 ms                                                                | 171 ms: 1.10x slower                                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.64 sec: 1.12x slower                                                         |
| sympy_str                | 329 ms                                                                | 370 ms: 1.13x slower                                                           |
| sympy_integrate          | 26.5 ms                                                               | 30.0 ms: 1.13x slower                                                          |
| sympy_expand             | 543 ms                                                                | 619 ms: 1.14x slower                                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 88.4 ms: 1.17x slower                                                          |
| sympy_sum                | 184 ms                                                                | 216 ms: 1.18x slower                                                           |
| nqueens                  | 117 ms                                                                | 139 ms: 1.18x slower                                                           |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                                          |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                           |
| genshi_xml               | 69.8 ms                                                               | 84.5 ms: 1.21x slower                                                          |
| async_generators         | 452 ms                                                                | 552 ms: 1.22x slower                                                           |
| regex_effbot             | 4.25 ms                                                               | 5.38 ms: 1.27x slower                                                          |
| python_startup_no_site   | 6.89 ms                                                               | 9.16 ms: 1.33x slower                                                          |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                          |
| gc_traversal             | 4.15 ms                                                               | 6.50 ms: 1.57x slower                                                          |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                          |
| bench_mp_pool            | 14.5 ms                                                               | 1.60 sec: 109.81x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.03x faster                                                                   |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_iterparse, mdp, json, sqlalchemy_declarative, hexiom, sqlite_synth
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.111x faster
# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.38x