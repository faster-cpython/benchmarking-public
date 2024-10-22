# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.01x faster
- HPT reliability: 62.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                         |
| docutils       | 2.58 sec                                               | 2.95 sec: 1.14x slower                                                       |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                        |
| tornado_http   | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 410 ms: 1.13x faster                                                         |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                                         |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                                         |
| async_tree_none_tg        | 320 ms                                                 | 316 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 568 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 494 ms: 1.01x slower                                                         |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                        |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                         |
| async_tree_io_tg          | 825 ms                                                 | 910 ms: 1.10x slower                                                         |
| async_tree_io             | 843 ms                                                 | 946 ms: 1.12x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                        |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                        |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.58 ms: 1.09x faster                                                        |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                        |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                        |
| xml_etree_process   | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                        |
| tomli_loads         | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                       |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.06x faster                                                         |
| xml_etree_iterparse | 102 ms                                                 | 98.8 ms: 1.03x faster                                                        |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                        |
| json_loads          | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.21 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                        |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                        |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.0 us: 1.41x faster                                                        |
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                         |
| richards                  | 48.1 ms                                                | 39.2 ms: 1.23x faster                                                        |
| richards_super            | 54.4 ms                                                | 44.8 ms: 1.22x faster                                                        |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                         |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.19x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.37 ms: 1.15x faster                                                        |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 410 ms: 1.13x faster                                                         |
| xml_etree_generate        | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                        |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| crypto_pyaes              | 73.0 ms                                                | 65.7 ms: 1.11x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                        |
| float                     | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                       |
| go                        | 142 ms                                                 | 130 ms: 1.09x faster                                                         |
| pathlib                   | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.58 ms: 1.09x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                       |
| nbody                     | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                        |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                                         |
| telco                     | 8.45 ms                                                | 7.91 ms: 1.07x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                                         |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.06x faster                                                         |
| bpe_tokeniser             | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 63.2 ms: 1.05x faster                                                        |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| scimark_sor               | 122 ms                                                 | 118 ms: 1.04x faster                                                         |
| regex_dna                 | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| html5lib                  | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 102 ms                                                 | 98.8 ms: 1.03x faster                                                        |
| fannkuch                  | 381 ms                                                 | 371 ms: 1.03x faster                                                         |
| regex_v8                  | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                        |
| pprint_safe_repr          | 744 ms                                                 | 729 ms: 1.02x faster                                                         |
| thrift                    | 796 us                                                 | 782 us: 1.02x faster                                                         |
| logging_format            | 6.25 us                                                | 6.14 us: 1.02x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 316 ms: 1.01x faster                                                         |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 568 ms: 1.01x faster                                                         |
| logging_simple            | 5.66 us                                                | 5.61 us: 1.01x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                        |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                        |
| pyflate                   | 460 ms                                                 | 456 ms: 1.01x faster                                                         |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.00x slower                                                        |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.18 ms: 1.01x slower                                                        |
| chaos                     | 58.4 ms                                                | 59.1 ms: 1.01x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 494 ms: 1.01x slower                                                         |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 831 us: 1.02x slower                                                         |
| pycparser                 | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                       |
| json                      | 5.20 ms                                                | 5.33 ms: 1.03x slower                                                        |
| coverage                  | 83.7 ms                                                | 86.4 ms: 1.03x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.21 ms: 1.03x slower                                                        |
| tornado_http              | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                        |
| raytrace                  | 262 ms                                                 | 272 ms: 1.04x slower                                                         |
| typing_runtime_protocols  | 159 us                                                 | 166 us: 1.04x slower                                                         |
| 2to3                      | 265 ms                                                 | 276 ms: 1.04x slower                                                         |
| django_template           | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                                         |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                        |
| nqueens                   | 80.6 ms                                                | 85.3 ms: 1.06x slower                                                        |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                         |
| sqlglot_transpile         | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                        |
| genshi_text               | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                        |
| regex_compile             | 131 ms                                                 | 141 ms: 1.08x slower                                                         |
| dulwich_log               | 63.0 ms                                                | 68.4 ms: 1.09x slower                                                        |
| sympy_str                 | 274 ms                                                 | 299 ms: 1.09x slower                                                         |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                         |
| async_tree_io_tg          | 825 ms                                                 | 910 ms: 1.10x slower                                                         |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                        |
| async_tree_io             | 843 ms                                                 | 946 ms: 1.12x slower                                                         |
| genshi_xml                | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                        |
| hexiom                    | 6.13 ms                                                | 6.92 ms: 1.13x slower                                                        |
| docutils                  | 2.58 sec                                               | 2.95 sec: 1.14x slower                                                       |
| generators                | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                        |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.15x slower                                                         |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): logging_silent, bench_mp_pool, asyncio_websockets, pickle_pure_python, pprint_pformat, unpickle_pure_python, async_tree_cpu_io_mixed_tg
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 62.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x