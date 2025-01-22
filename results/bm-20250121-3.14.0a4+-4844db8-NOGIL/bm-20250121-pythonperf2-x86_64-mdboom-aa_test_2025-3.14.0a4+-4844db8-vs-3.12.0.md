# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.069x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 336 ms: 1.18x slower                                                 |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                               |
| Geometric mean | (ref)                                                        | 1.10x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 573 ms: 1.84x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 248 ms: 1.74x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 609 ms: 1.71x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 320 ms: 1.69x faster                                                 |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 487 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.07x faster                                                 |
| float          | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                |
| nbody          | 88.0 ms                                                      | 134 ms: 1.52x slower                                                 |
| Geometric mean | (ref)                                                        | 1.12x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                 |
| regex_compile  | 144 ms                                                       | 156 ms: 1.08x slower                                                 |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 87.8 ms: 1.17x faster                                                |
| xml_etree_parse      | 144 ms                                                       | 132 ms: 1.09x faster                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                               |
| xml_etree_generate   | 86.1 ms                                                      | 97.4 ms: 1.13x slower                                                |
| json_loads           | 24.4 us                                                      | 27.7 us: 1.14x slower                                                |
| unpickle_pure_python | 210 us                                                       | 250 us: 1.19x slower                                                 |
| pickle_pure_python   | 318 us                                                       | 392 us: 1.23x slower                                                 |
| xml_etree_process    | 58.4 ms                                                      | 74.2 ms: 1.27x slower                                                |
| json_dumps           | 10.2 ms                                                      | 13.4 ms: 1.31x slower                                                |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                |
| python_startup         | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 46.2 ms: 1.21x slower                                                |
| mako            | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                |
| Geometric mean  | (ref)                                                        | 1.47x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 573 ms: 1.84x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 248 ms: 1.74x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 609 ms: 1.71x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 320 ms: 1.69x faster                                                 |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 359 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 487 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                 |
| generators                 | 37.4 ms                                                      | 31.7 ms: 1.18x faster                                                |
| xml_etree_iterparse        | 103 ms                                                       | 87.8 ms: 1.17x faster                                                |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.16x faster                                                |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                |
| deepcopy                   | 368 us                                                       | 332 us: 1.11x faster                                                 |
| xml_etree_parse            | 144 ms                                                       | 132 ms: 1.09x faster                                                 |
| sqlite_synth               | 2.77 us                                                      | 2.60 us: 1.07x faster                                                |
| pidigits                   | 265 ms                                                       | 249 ms: 1.07x faster                                                 |
| comprehensions             | 21.9 us                                                      | 21.3 us: 1.03x faster                                                |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                |
| float                      | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                |
| go                         | 150 ms                                                       | 147 ms: 1.02x faster                                                 |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                 |
| deepcopy_memo              | 36.8 us                                                      | 37.4 us: 1.02x slower                                                |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                               |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                 |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                               |
| dulwich_log                | 65.4 ms                                                      | 69.7 ms: 1.07x slower                                                |
| deepcopy_reduce            | 3.37 us                                                      | 3.61 us: 1.07x slower                                                |
| mdp                        | 2.57 sec                                                     | 2.77 sec: 1.08x slower                                               |
| regex_compile              | 144 ms                                                       | 156 ms: 1.08x slower                                                 |
| json                       | 5.12 ms                                                      | 5.54 ms: 1.08x slower                                                |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                 |
| spectral_norm              | 91.6 ms                                                      | 99.4 ms: 1.09x slower                                                |
| logging_format             | 7.48 us                                                      | 8.18 us: 1.09x slower                                                |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                |
| sympy_sum                  | 162 ms                                                       | 177 ms: 1.09x slower                                                 |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.10x slower                                                 |
| logging_simple             | 6.71 us                                                      | 7.39 us: 1.10x slower                                                |
| chaos                      | 64.0 ms                                                      | 71.1 ms: 1.11x slower                                                |
| sqlalchemy_declarative     | 159 ms                                                       | 177 ms: 1.11x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.9 ms: 1.11x slower                                                |
| tomli_loads                | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                               |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                 |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.12x slower                                                 |
| sympy_str                  | 302 ms                                                       | 341 ms: 1.13x slower                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 97.4 ms: 1.13x slower                                                |
| raytrace                   | 298 ms                                                       | 338 ms: 1.13x slower                                                 |
| json_loads                 | 24.4 us                                                      | 27.7 us: 1.14x slower                                                |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                |
| pprint_safe_repr           | 807 ms                                                       | 920 ms: 1.14x slower                                                 |
| scimark_fft                | 301 ms                                                       | 343 ms: 1.14x slower                                                 |
| sqlglot_optimize           | 57.5 ms                                                      | 65.5 ms: 1.14x slower                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.90 sec: 1.15x slower                                               |
| crypto_pyaes               | 80.3 ms                                                      | 93.0 ms: 1.16x slower                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 2.08 ms: 1.17x slower                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.61 ms: 1.17x slower                                                |
| gc_traversal               | 3.48 ms                                                      | 4.09 ms: 1.18x slower                                                |
| sympy_expand               | 484 ms                                                       | 570 ms: 1.18x slower                                                 |
| 2to3                       | 285 ms                                                       | 336 ms: 1.18x slower                                                 |
| unpickle_pure_python       | 210 us                                                       | 250 us: 1.19x slower                                                 |
| scimark_lu                 | 98.8 ms                                                      | 119 ms: 1.20x slower                                                 |
| async_generators           | 390 ms                                                       | 470 ms: 1.20x slower                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 83.3 ms: 1.21x slower                                                |
| django_template            | 38.2 ms                                                      | 46.2 ms: 1.21x slower                                                |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                 |
| hexiom                     | 5.96 ms                                                      | 7.24 ms: 1.21x slower                                                |
| pickle_pure_python         | 318 us                                                       | 392 us: 1.23x slower                                                 |
| richards                   | 45.7 ms                                                      | 57.1 ms: 1.25x slower                                                |
| nqueens                    | 89.9 ms                                                      | 114 ms: 1.26x slower                                                 |
| xml_etree_process          | 58.4 ms                                                      | 74.2 ms: 1.27x slower                                                |
| richards_super             | 51.3 ms                                                      | 66.1 ms: 1.29x slower                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.05 ms: 1.29x slower                                                |
| telco                      | 6.96 ms                                                      | 9.03 ms: 1.30x slower                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.49 ms: 1.30x slower                                                |
| json_dumps                 | 10.2 ms                                                      | 13.4 ms: 1.31x slower                                                |
| fannkuch                   | 350 ms                                                       | 473 ms: 1.35x slower                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                |
| deltablue                  | 3.24 ms                                                      | 4.47 ms: 1.38x slower                                                |
| typing_runtime_protocols   | 152 us                                                       | 225 us: 1.48x slower                                                 |
| bench_thread_pool          | 950 us                                                       | 1.44 ms: 1.52x slower                                                |
| nbody                      | 88.0 ms                                                      | 134 ms: 1.52x slower                                                 |
| coverage                   | 66.7 ms                                                      | 102 ms: 1.53x slower                                                 |
| python_startup             | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                |
| mako                       | 10.0 ms                                                      | 18.0 ms: 1.80x slower                                                |
| bench_mp_pool              | 4.76 ms                                                      | 49.0 ms: 10.30x slower                                               |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                         |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.069x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.26x