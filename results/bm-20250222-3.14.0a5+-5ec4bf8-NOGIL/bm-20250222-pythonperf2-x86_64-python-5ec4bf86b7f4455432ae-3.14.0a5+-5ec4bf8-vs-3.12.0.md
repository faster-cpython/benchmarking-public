# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.052x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 329 ms: 1.15x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 553 ms: 1.91x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 589 ms: 1.77x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 247 ms: 1.75x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 317 ms: 1.71x faster                                                         |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 479 ms: 1.46x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 517 ms: 1.35x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 248 ms: 1.07x faster                                                         |
| float          | 76.6 ms                                                      | 74.7 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| regex_compile  | 144 ms                                                       | 160 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 90.9 ms: 1.13x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pickle_dict          | 32.5 us                                                      | 33.4 us: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.9 us: 1.07x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.77 us: 1.08x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                                       |
| pickle               | 10.5 us                                                      | 11.9 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 98.0 ms: 1.14x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 239 us: 1.14x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 365 us: 1.15x slower                                                         |
| json_loads           | 24.4 us                                                      | 28.7 us: 1.18x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.63 us: 1.21x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 71.2 ms: 1.22x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.2 ms: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.6 ms: 1.19x slower                                                        |
| mako            | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 553 ms: 1.91x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 589 ms: 1.77x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 247 ms: 1.75x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 317 ms: 1.71x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.05 ms: 1.70x faster                                                        |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 479 ms: 1.46x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 517 ms: 1.35x faster                                                         |
| generators                 | 37.4 ms                                                      | 32.1 ms: 1.17x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 90.9 ms: 1.13x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| deepcopy                   | 368 us                                                       | 329 us: 1.12x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 20.6 ms: 1.11x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.7 us: 1.11x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.58 us: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 248 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 35.2 us: 1.05x faster                                                        |
| float                      | 76.6 ms                                                      | 74.7 ms: 1.03x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 379 ms: 1.02x faster                                                         |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                       |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 33.4 us: 1.03x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.85 us: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.3 ms: 1.05x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.54 us: 1.05x slower                                                        |
| logging_simple             | 6.71 us                                                      | 7.07 us: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 69.8 ms: 1.07x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.9 us: 1.07x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.07x slower                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 171 ms: 1.08x slower                                                         |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.77 us: 1.08x slower                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.3 ms: 1.08x slower                                                        |
| chaos                      | 64.0 ms                                                      | 69.5 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.81 sec: 1.09x slower                                                       |
| json                       | 5.12 ms                                                      | 5.66 ms: 1.11x slower                                                        |
| sympy_str                  | 302 ms                                                       | 335 ms: 1.11x slower                                                         |
| pyflate                    | 439 ms                                                       | 487 ms: 1.11x slower                                                         |
| regex_compile              | 144 ms                                                       | 160 ms: 1.11x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.12x slower                                                         |
| asyncio_tcp                | 378 ms                                                       | 422 ms: 1.12x slower                                                         |
| raytrace                   | 298 ms                                                       | 334 ms: 1.12x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 26.9 ms: 1.13x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 911 ms: 1.13x slower                                                         |
| pickle                     | 10.5 us                                                      | 11.9 us: 1.13x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 98.0 ms: 1.14x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.89 sec: 1.14x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 239 us: 1.14x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 91.8 ms: 1.14x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 65.8 ms: 1.15x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 365 us: 1.15x slower                                                         |
| 2to3                       | 285 ms                                                       | 329 ms: 1.15x slower                                                         |
| scimark_fft                | 301 ms                                                       | 347 ms: 1.15x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 61.4 ns: 1.16x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 2.06 ms: 1.16x slower                                                        |
| sympy_expand               | 484 ms                                                       | 565 ms: 1.17x slower                                                         |
| json_loads                 | 24.4 us                                                      | 28.7 us: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                       |
| async_generators           | 390 ms                                                       | 466 ms: 1.19x slower                                                         |
| django_template            | 38.2 ms                                                      | 45.6 ms: 1.19x slower                                                        |
| meteor_contest             | 128 ms                                                       | 153 ms: 1.20x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.65 ms: 1.20x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 119 ms: 1.21x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 5.63 us: 1.21x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 71.2 ms: 1.22x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.31 ms: 1.23x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.97 ms: 1.23x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.96 ms: 1.24x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.24x slower                                                         |
| richards                   | 45.7 ms                                                      | 57.6 ms: 1.26x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 88.5 ms: 1.28x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.2 ms: 1.29x slower                                                        |
| richards_super             | 51.3 ms                                                      | 66.8 ms: 1.30x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.23 ms: 1.33x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.68 ms: 1.35x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| fannkuch                   | 350 ms                                                       | 480 ms: 1.37x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 219 us: 1.45x slower                                                         |
| nbody                      | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.44 ms: 1.52x slower                                                        |
| coverage                   | 66.7 ms                                                      | 102 ms: 1.53x slower                                                         |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 48.9 ms: 10.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.26x