# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 78dbf36
- commit date: 2024-06-08
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                | 268 ms: 1.01x faster                                                    |
| tornado_http   | 94.5 ms                                                               | 93.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                               | 86.3 ms: 1.02x faster                                                   |
| pidigits       | 190 ms                                                                | 190 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 132 ms: 1.01x faster                                                    |
| regex_v8       | 25.8 ms                                                               | 26.0 ms: 1.01x slower                                                   |
| regex_dna      | 226 ms                                                                | 233 ms: 1.03x slower                                                    |
| regex_effbot   | 3.68 ms                                                               | 3.80 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 10.8 ms                                                               | 10.4 ms: 1.04x faster                                                   |
| unpickle_list        | 5.45 us                                                               | 5.31 us: 1.03x faster                                                   |
| xml_etree_generate   | 87.3 ms                                                               | 85.6 ms: 1.02x faster                                                   |
| unpickle_pure_python | 220 us                                                                | 216 us: 1.02x faster                                                    |
| json_loads           | 29.1 us                                                               | 28.6 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                                | 106 ms: 1.02x faster                                                    |
| pickle_pure_python   | 304 us                                                                | 299 us: 1.02x faster                                                    |
| xml_etree_process    | 60.5 ms                                                               | 59.6 ms: 1.02x faster                                                   |
| tomli_loads          | 2.14 sec                                                              | 2.15 sec: 1.01x slower                                                  |
| pickle_dict          | 34.4 us                                                               | 35.2 us: 1.02x slower                                                   |
| pickle_list          | 5.06 us                                                               | 5.18 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (3): pickle, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                   |
| python_startup_no_site | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                               | 23.2 ms: 1.01x faster                                                   |
| mako           | 11.2 ms                                                               | 11.2 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                      | 2.78 sec                                                              | 2.56 sec: 1.09x faster                                                  |
| scimark_sparse_mat_mult  | 5.17 ms                                                               | 4.92 ms: 1.05x faster                                                   |
| pyflate                  | 495 ms                                                                | 473 ms: 1.05x faster                                                    |
| scimark_sor              | 131 ms                                                                | 126 ms: 1.04x faster                                                    |
| json_dumps               | 10.8 ms                                                               | 10.4 ms: 1.04x faster                                                   |
| unpickle_list            | 5.45 us                                                               | 5.31 us: 1.03x faster                                                   |
| richards                 | 48.6 ms                                                               | 47.4 ms: 1.03x faster                                                   |
| spectral_norm            | 117 ms                                                                | 114 ms: 1.03x faster                                                    |
| go                       | 145 ms                                                                | 142 ms: 1.02x faster                                                    |
| logging_format           | 6.39 us                                                               | 6.24 us: 1.02x faster                                                   |
| async_generators         | 451 ms                                                                | 441 ms: 1.02x faster                                                    |
| comprehensions           | 16.9 us                                                               | 16.5 us: 1.02x faster                                                   |
| chaos                    | 60.6 ms                                                               | 59.3 ms: 1.02x faster                                                   |
| deepcopy                 | 369 us                                                                | 362 us: 1.02x faster                                                    |
| xml_etree_generate       | 87.3 ms                                                               | 85.6 ms: 1.02x faster                                                   |
| unpickle_pure_python     | 220 us                                                                | 216 us: 1.02x faster                                                    |
| richards_super           | 55.0 ms                                                               | 54.0 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 167 us                                                                | 164 us: 1.02x faster                                                    |
| nbody                    | 87.8 ms                                                               | 86.3 ms: 1.02x faster                                                   |
| json_loads               | 29.1 us                                                               | 28.6 us: 1.02x faster                                                   |
| deepcopy_reduce          | 3.30 us                                                               | 3.24 us: 1.02x faster                                                   |
| raytrace                 | 268 ms                                                                | 264 ms: 1.02x faster                                                    |
| xml_etree_iterparse      | 108 ms                                                                | 106 ms: 1.02x faster                                                    |
| pickle_pure_python       | 304 us                                                                | 299 us: 1.02x faster                                                    |
| xml_etree_process        | 60.5 ms                                                               | 59.6 ms: 1.02x faster                                                   |
| generators               | 29.5 ms                                                               | 29.0 ms: 1.02x faster                                                   |
| sqlglot_transpile        | 1.64 ms                                                               | 1.61 ms: 1.01x faster                                                   |
| hexiom                   | 6.28 ms                                                               | 6.19 ms: 1.01x faster                                                   |
| meteor_contest           | 109 ms                                                                | 108 ms: 1.01x faster                                                    |
| json                     | 5.43 ms                                                               | 5.36 ms: 1.01x faster                                                   |
| logging_simple           | 5.70 us                                                               | 5.62 us: 1.01x faster                                                   |
| sqlglot_parse            | 1.32 ms                                                               | 1.31 ms: 1.01x faster                                                   |
| genshi_text              | 23.5 ms                                                               | 23.2 ms: 1.01x faster                                                   |
| pprint_safe_repr         | 753 ms                                                                | 744 ms: 1.01x faster                                                    |
| sqlite_synth             | 2.97 us                                                               | 2.93 us: 1.01x faster                                                   |
| sympy_str                | 281 ms                                                                | 277 ms: 1.01x faster                                                    |
| sympy_integrate          | 20.5 ms                                                               | 20.3 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.83 sec: 1.01x faster                                                  |
| deepcopy_memo            | 39.6 us                                                               | 39.3 us: 1.01x faster                                                   |
| scimark_monte_carlo      | 68.3 ms                                                               | 67.7 ms: 1.01x faster                                                   |
| pathlib                  | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                   |
| tornado_http             | 94.5 ms                                                               | 93.8 ms: 1.01x faster                                                   |
| coroutines               | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                                   |
| 2to3                     | 270 ms                                                                | 268 ms: 1.01x faster                                                    |
| regex_compile            | 133 ms                                                                | 132 ms: 1.01x faster                                                    |
| dulwich_log              | 65.5 ms                                                               | 65.1 ms: 1.01x faster                                                   |
| asyncio_tcp              | 504 ms                                                                | 501 ms: 1.01x faster                                                    |
| thrift                   | 811 us                                                                | 806 us: 1.01x faster                                                    |
| mako                     | 11.2 ms                                                               | 11.2 ms: 1.00x faster                                                   |
| sqlglot_optimize         | 55.0 ms                                                               | 54.8 ms: 1.00x faster                                                   |
| nqueens                  | 79.5 ms                                                               | 79.3 ms: 1.00x faster                                                   |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                   |
| pidigits                 | 190 ms                                                                | 190 ms: 1.00x slower                                                    |
| python_startup_no_site   | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                                   |
| logging_silent           | 105 ns                                                                | 105 ns: 1.01x slower                                                    |
| regex_v8                 | 25.8 ms                                                               | 26.0 ms: 1.01x slower                                                   |
| tomli_loads              | 2.14 sec                                                              | 2.15 sec: 1.01x slower                                                  |
| create_gc_cycles         | 1.77 ms                                                               | 1.78 ms: 1.01x slower                                                   |
| fannkuch                 | 395 ms                                                                | 398 ms: 1.01x slower                                                    |
| scimark_lu               | 115 ms                                                                | 117 ms: 1.02x slower                                                    |
| pickle_dict              | 34.4 us                                                               | 35.2 us: 1.02x slower                                                   |
| pickle_list              | 5.06 us                                                               | 5.18 us: 1.03x slower                                                   |
| crypto_pyaes             | 73.3 ms                                                               | 75.2 ms: 1.03x slower                                                   |
| regex_dna                | 226 ms                                                                | 233 ms: 1.03x slower                                                    |
| regex_effbot             | 3.68 ms                                                               | 3.80 ms: 1.03x slower                                                   |
| gc_traversal             | 3.78 ms                                                               | 3.98 ms: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (30): async_tree_none_tg, pickle, async_tree_memoization_tg, xml_etree_parse, async_tree_io_tg, async_tree_memoization, pycparser, pylint, unpickle, async_tree_none, telco, async_tree_io, pprint_pformat, genshi_xml, float, deltablue, html5lib, bench_thread_pool, sympy_sum, asyncio_websockets, dask, docutils, sqlglot_normalize, bench_mp_pool, django_template, coverage, sympy_expand, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, scimark_fft

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x