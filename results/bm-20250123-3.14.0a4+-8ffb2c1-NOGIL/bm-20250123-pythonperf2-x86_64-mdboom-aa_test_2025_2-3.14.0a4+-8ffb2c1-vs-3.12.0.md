# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.073x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 337 ms: 1.18x slower                                                   |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                        | 1.10x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 568 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 431 ms                                                       | 247 ms: 1.75x faster                                                   |
| async_tree_io              | 1.04 sec                                                     | 608 ms: 1.72x faster                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 319 ms: 1.69x faster                                                   |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                   |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 485 ms: 1.44x faster                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 525 ms: 1.33x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.60x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                   |
| float          | 76.6 ms                                                      | 76.0 ms: 1.01x faster                                                  |
| nbody          | 88.0 ms                                                      | 134 ms: 1.52x slower                                                   |
| Geometric mean | (ref)                                                        | 1.12x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.27 ms: 1.09x faster                                                  |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                   |
| regex_compile  | 144 ms                                                       | 155 ms: 1.08x slower                                                   |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                        | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 91.2 ms: 1.13x faster                                                  |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 98.4 ms: 1.14x slower                                                  |
| json_loads           | 24.4 us                                                      | 28.4 us: 1.17x slower                                                  |
| unpickle_pure_python | 210 us                                                       | 254 us: 1.21x slower                                                   |
| pickle_pure_python   | 318 us                                                       | 392 us: 1.23x slower                                                   |
| xml_etree_process    | 58.4 ms                                                      | 74.4 ms: 1.27x slower                                                  |
| json_dumps           | 10.2 ms                                                      | 13.4 ms: 1.31x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                  |
| python_startup         | 11.6 ms                                                      | 18.7 ms: 1.60x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 46.3 ms: 1.21x slower                                                  |
| mako            | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.47x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 568 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 431 ms                                                       | 247 ms: 1.75x faster                                                   |
| async_tree_io              | 1.04 sec                                                     | 608 ms: 1.72x faster                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 319 ms: 1.69x faster                                                   |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                   |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 485 ms: 1.44x faster                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 525 ms: 1.33x faster                                                   |
| generators                 | 37.4 ms                                                      | 31.4 ms: 1.19x faster                                                  |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 91.2 ms: 1.13x faster                                                  |
| deepcopy                   | 368 us                                                       | 335 us: 1.10x faster                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.27 ms: 1.09x faster                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.58 us: 1.07x faster                                                  |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                   |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                   |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                                  |
| comprehensions             | 21.9 us                                                      | 21.5 us: 1.02x faster                                                  |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                   |
| float                      | 76.6 ms                                                      | 76.0 ms: 1.01x faster                                                  |
| go                         | 150 ms                                                       | 149 ms: 1.00x faster                                                   |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                   |
| deepcopy_memo              | 36.8 us                                                      | 37.9 us: 1.03x slower                                                  |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                 |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                 |
| dulwich_log                | 65.4 ms                                                      | 70.0 ms: 1.07x slower                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 3.62 us: 1.07x slower                                                  |
| mdp                        | 2.57 sec                                                     | 2.76 sec: 1.07x slower                                                 |
| regex_compile              | 144 ms                                                       | 155 ms: 1.08x slower                                                   |
| sympy_sum                  | 162 ms                                                       | 177 ms: 1.09x slower                                                   |
| logging_format             | 7.48 us                                                      | 8.15 us: 1.09x slower                                                  |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                   |
| json                       | 5.12 ms                                                      | 5.58 ms: 1.09x slower                                                  |
| chaos                      | 64.0 ms                                                      | 69.8 ms: 1.09x slower                                                  |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                   |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                  |
| logging_simple             | 6.71 us                                                      | 7.43 us: 1.11x slower                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 177 ms: 1.11x slower                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.9 ms: 1.12x slower                                                  |
| scimark_fft                | 301 ms                                                       | 336 ms: 1.12x slower                                                   |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.12x slower                                                   |
| sympy_str                  | 302 ms                                                       | 339 ms: 1.12x slower                                                   |
| pyflate                    | 439 ms                                                       | 494 ms: 1.13x slower                                                   |
| sympy_integrate            | 23.9 ms                                                      | 27.1 ms: 1.13x slower                                                  |
| pprint_safe_repr           | 807 ms                                                       | 915 ms: 1.13x slower                                                   |
| sqlglot_optimize           | 57.5 ms                                                      | 65.3 ms: 1.14x slower                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 98.4 ms: 1.14x slower                                                  |
| raytrace                   | 298 ms                                                       | 341 ms: 1.14x slower                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.89 sec: 1.14x slower                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 92.6 ms: 1.15x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.60 ms: 1.16x slower                                                  |
| json_loads                 | 24.4 us                                                      | 28.4 us: 1.17x slower                                                  |
| sympy_expand               | 484 ms                                                       | 565 ms: 1.17x slower                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 2.08 ms: 1.17x slower                                                  |
| logging_silent             | 94.4 ns                                                      | 110 ns: 1.17x slower                                                   |
| 2to3                       | 285 ms                                                       | 337 ms: 1.18x slower                                                   |
| async_generators           | 390 ms                                                       | 466 ms: 1.19x slower                                                   |
| meteor_contest             | 128 ms                                                       | 153 ms: 1.20x slower                                                   |
| unpickle_pure_python       | 210 us                                                       | 254 us: 1.21x slower                                                   |
| django_template            | 38.2 ms                                                      | 46.3 ms: 1.21x slower                                                  |
| scimark_lu                 | 98.8 ms                                                      | 120 ms: 1.21x slower                                                   |
| hexiom                     | 5.96 ms                                                      | 7.25 ms: 1.22x slower                                                  |
| pickle_pure_python         | 318 us                                                       | 392 us: 1.23x slower                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 85.8 ms: 1.24x slower                                                  |
| nqueens                    | 89.9 ms                                                      | 112 ms: 1.25x slower                                                   |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                  |
| richards                   | 45.7 ms                                                      | 57.5 ms: 1.26x slower                                                  |
| xml_etree_process          | 58.4 ms                                                      | 74.4 ms: 1.27x slower                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.43 ms: 1.29x slower                                                  |
| json_dumps                 | 10.2 ms                                                      | 13.4 ms: 1.31x slower                                                  |
| richards_super             | 51.3 ms                                                      | 67.0 ms: 1.31x slower                                                  |
| telco                      | 6.96 ms                                                      | 9.13 ms: 1.31x slower                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                  |
| deltablue                  | 3.24 ms                                                      | 4.47 ms: 1.38x slower                                                  |
| fannkuch                   | 350 ms                                                       | 489 ms: 1.40x slower                                                   |
| gc_traversal               | 3.48 ms                                                      | 4.95 ms: 1.42x slower                                                  |
| typing_runtime_protocols   | 152 us                                                       | 226 us: 1.49x slower                                                   |
| nbody                      | 88.0 ms                                                      | 134 ms: 1.52x slower                                                   |
| bench_thread_pool          | 950 us                                                       | 1.46 ms: 1.54x slower                                                  |
| coverage                   | 66.7 ms                                                      | 103 ms: 1.55x slower                                                   |
| python_startup             | 11.6 ms                                                      | 18.7 ms: 1.60x slower                                                  |
| mako                       | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 48.9 ms: 10.27x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                           |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.26x