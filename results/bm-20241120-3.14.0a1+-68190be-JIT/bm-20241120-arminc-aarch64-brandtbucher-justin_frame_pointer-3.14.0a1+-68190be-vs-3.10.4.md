# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: 68190be
- commit date: 2024-11-20
- overall geometric mean: 1.162x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 362 ms: 1.05x faster                                                           |
| html5lib       | 86.5 ms                                                               | 80.6 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                         |
| async_tree_none         | 950 ms                                                                | 462 ms: 2.06x faster                                                           |
| async_tree_memoization  | 1.13 sec                                                              | 574 ms: 1.97x faster                                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 752 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 135 ms: 1.22x faster                                                           |
| float          | 135 ms                                                                | 111 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 172 ms: 1.03x faster                                                           |
| regex_v8       | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 412 us: 1.28x faster                                                           |
| unpickle_pure_python | 366 us                                                                | 294 us: 1.24x faster                                                           |
| tomli_loads          | 3.36 sec                                                              | 2.86 sec: 1.18x faster                                                         |
| xml_etree_process    | 99.5 ms                                                               | 86.8 ms: 1.15x faster                                                          |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                                           |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                          |
| xml_etree_iterparse  | 156 ms                                                                | 175 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                          |
| python_startup         | 11.2 ms                                                               | 15.8 ms: 1.41x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.33x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                          |
| django_template | 53.3 ms                                                               | 50.1 ms: 1.06x faster                                                          |
| genshi_xml      | 69.8 ms                                                               | 84.0 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 239 us: 2.77x faster                                                           |
| async_tree_io            | 2.28 sec                                                              | 1.01 sec: 2.26x faster                                                         |
| async_tree_none          | 950 ms                                                                | 462 ms: 2.06x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 574 ms: 1.97x faster                                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 752 ms: 1.69x faster                                                           |
| deltablue                | 8.94 ms                                                               | 5.47 ms: 1.64x faster                                                          |
| richards_super           | 107 ms                                                                | 72.1 ms: 1.49x faster                                                          |
| gc_traversal             | 4.15 ms                                                               | 2.88 ms: 1.44x faster                                                          |
| crypto_pyaes             | 134 ms                                                                | 94.4 ms: 1.42x faster                                                          |
| raytrace                 | 573 ms                                                                | 405 ms: 1.42x faster                                                           |
| richards                 | 91.7 ms                                                               | 65.6 ms: 1.40x faster                                                          |
| deepcopy_memo            | 61.7 us                                                               | 44.3 us: 1.39x faster                                                          |
| scimark_lu               | 227 ms                                                                | 166 ms: 1.37x faster                                                           |
| logging_silent           | 222 ns                                                                | 164 ns: 1.36x faster                                                           |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                          |
| scimark_sor              | 246 ms                                                                | 183 ms: 1.35x faster                                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.81 ms: 1.32x faster                                                          |
| sqlglot_transpile        | 2.84 ms                                                               | 2.17 ms: 1.31x faster                                                          |
| scimark_monte_carlo      | 128 ms                                                                | 98.2 ms: 1.30x faster                                                          |
| go                       | 264 ms                                                                | 203 ms: 1.30x faster                                                           |
| pylint                   | 485 ms                                                                | 375 ms: 1.29x faster                                                           |
| chaos                    | 121 ms                                                                | 93.9 ms: 1.29x faster                                                          |
| pickle_pure_python       | 529 us                                                                | 412 us: 1.28x faster                                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 156 ms: 1.26x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                          |
| unpickle_pure_python     | 366 us                                                                | 294 us: 1.24x faster                                                           |
| deepcopy                 | 511 us                                                                | 413 us: 1.24x faster                                                           |
| logging_simple           | 9.78 us                                                               | 7.93 us: 1.23x faster                                                          |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.23x faster                                                          |
| logging_format           | 10.6 us                                                               | 8.62 us: 1.23x faster                                                          |
| nbody                    | 166 ms                                                                | 135 ms: 1.22x faster                                                           |
| float                    | 135 ms                                                                | 111 ms: 1.22x faster                                                           |
| comprehensions           | 33.1 us                                                               | 27.8 us: 1.19x faster                                                          |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                          |
| tomli_loads              | 3.36 sec                                                              | 2.86 sec: 1.18x faster                                                         |
| generators               | 68.1 ms                                                               | 58.2 ms: 1.17x faster                                                          |
| pyflate                  | 795 ms                                                                | 689 ms: 1.15x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 86.8 ms: 1.15x faster                                                          |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.0 ms: 1.14x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                          |
| spectral_norm            | 186 ms                                                                | 166 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.42 ms: 1.12x faster                                                          |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                           |
| pycparser                | 1.69 sec                                                              | 1.55 sec: 1.09x faster                                                         |
| html5lib                 | 86.5 ms                                                               | 80.6 ms: 1.07x faster                                                          |
| scimark_fft              | 500 ms                                                                | 467 ms: 1.07x faster                                                           |
| django_template          | 53.3 ms                                                               | 50.1 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 4.60 us                                                               | 4.33 us: 1.06x faster                                                          |
| 2to3                     | 381 ms                                                                | 362 ms: 1.05x faster                                                           |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                          |
| regex_compile            | 177 ms                                                                | 172 ms: 1.03x faster                                                           |
| sympy_sum                | 184 ms                                                                | 179 ms: 1.03x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                                          |
| mdp                      | 3.70 sec                                                              | 3.75 sec: 1.01x slower                                                         |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                           |
| meteor_contest           | 126 ms                                                                | 130 ms: 1.03x slower                                                           |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                          |
| sympy_str                | 329 ms                                                                | 345 ms: 1.05x slower                                                           |
| hexiom                   | 10.9 ms                                                               | 11.6 ms: 1.06x slower                                                          |
| create_gc_cycles         | 2.26 ms                                                               | 2.40 ms: 1.06x slower                                                          |
| dulwich_log              | 73.5 ms                                                               | 78.5 ms: 1.07x slower                                                          |
| pprint_pformat           | 2.36 sec                                                              | 2.60 sec: 1.10x slower                                                         |
| sympy_expand             | 543 ms                                                                | 608 ms: 1.12x slower                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 175 ms: 1.12x slower                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 1.29 sec: 1.12x slower                                                         |
| nqueens                  | 117 ms                                                                | 137 ms: 1.17x slower                                                           |
| telco                    | 8.49 ms                                                               | 9.97 ms: 1.17x slower                                                          |
| genshi_xml               | 69.8 ms                                                               | 84.0 ms: 1.20x slower                                                          |
| async_generators         | 452 ms                                                                | 547 ms: 1.21x slower                                                           |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                          |
| python_startup           | 11.2 ms                                                               | 15.8 ms: 1.41x slower                                                          |
| bench_mp_pool            | 14.5 ms                                                               | 1.60 sec: 110.12x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.08x faster                                                                   |

Benchmark hidden because not significant (12): sympy_integrate, regex_effbot, genshi_text, xml_etree_generate, sqlglot_optimize, docutils, fannkuch, scimark_sparse_mat_mult, sqlglot_normalize, regex_dna, sqlite_synth, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241120-3.14.0a1+-68190be-JIT/bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.162x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.31x