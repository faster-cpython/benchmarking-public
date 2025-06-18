# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.193x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 364 ms: 1.28x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                      |
| Geometric mean | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 607 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 263 ms: 1.64x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 616 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 645 ms: 1.08x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.47x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| nbody          | 88.0 ms                                                      | 135 ms: 1.54x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| regex_dna      | 239 ms                                                       | 249 ms: 1.04x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| regex_compile  | 144 ms                                                       | 176 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 37.1 us: 1.14x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 169 ms: 1.17x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.71 sec: 1.26x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 6.31 us: 1.35x slower                                                       |
| pickle_list          | 4.43 us                                                      | 6.14 us: 1.39x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 448 us: 1.41x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 295 us: 1.41x slower                                                        |
| unpickle             | 14.8 us                                                      | 21.1 us: 1.43x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 124 ms: 1.44x slower                                                        |
| json_loads           | 24.4 us                                                      | 35.6 us: 1.46x slower                                                       |
| pickle               | 10.5 us                                                      | 15.7 us: 1.49x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 88.3 ms: 1.51x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 15.5 ms: 1.52x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.35x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                       |
| python_startup         | 11.6 ms                                                      | 21.2 ms: 1.83x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 51.9 ms: 1.36x slower                                                       |
| mako            | 10.0 ms                                                      | 19.7 ms: 1.97x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.63x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 607 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 263 ms: 1.64x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.81 sec: 1.42x faster                                                      |
| gc_traversal               | 3.48 ms                                                      | 3.02 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 616 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 645 ms: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| generators                 | 37.4 ms                                                      | 35.9 ms: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 377 ms: 1.03x faster                                                        |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                        |
| deepcopy                   | 368 us                                                       | 374 us: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.9 ms: 1.04x slower                                                       |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.04x slower                                                        |
| float                      | 76.6 ms                                                      | 80.0 ms: 1.04x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 38.9 us: 1.06x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 56.4 ns: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 24.5 ms: 1.07x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 20.3 ms: 1.07x slower                                                       |
| comprehensions             | 21.9 us                                                      | 23.6 us: 1.08x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 3.08 us: 1.11x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.38 sec: 1.11x slower                                                      |
| asyncio_tcp                | 378 ms                                                       | 425 ms: 1.12x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 37.1 us: 1.14x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 27.8 ms: 1.16x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 169 ms: 1.17x slower                                                        |
| pyflate                    | 439 ms                                                       | 522 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 198 ms: 1.22x slower                                                        |
| regex_compile              | 144 ms                                                       | 176 ms: 1.22x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.17 us: 1.24x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 4.04 ms: 1.25x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.71 sec: 1.26x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 7.53 ms: 1.26x slower                                                       |
| chaos                      | 64.0 ms                                                      | 81.5 ms: 1.27x slower                                                       |
| 2to3                       | 285 ms                                                       | 364 ms: 1.28x slower                                                        |
| sympy_str                  | 302 ms                                                       | 387 ms: 1.28x slower                                                        |
| logging_format             | 7.48 us                                                      | 9.59 us: 1.28x slower                                                       |
| logging_simple             | 6.71 us                                                      | 8.62 us: 1.28x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.06 ms: 1.29x slower                                                       |
| raytrace                   | 298 ms                                                       | 389 ms: 1.31x slower                                                        |
| json                       | 5.12 ms                                                      | 6.76 ms: 1.32x slower                                                       |
| scimark_sor                | 109 ms                                                       | 147 ms: 1.35x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 6.31 us: 1.35x slower                                                       |
| django_template            | 38.2 ms                                                      | 51.9 ms: 1.36x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 123 ms: 1.37x slower                                                        |
| sympy_expand               | 484 ms                                                       | 664 ms: 1.37x slower                                                        |
| async_generators           | 390 ms                                                       | 536 ms: 1.37x slower                                                        |
| pickle_list                | 4.43 us                                                      | 6.14 us: 1.39x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 448 us: 1.41x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 295 us: 1.41x slower                                                        |
| unpickle                   | 14.8 us                                                      | 21.1 us: 1.43x slower                                                       |
| richards                   | 45.7 ms                                                      | 65.8 ms: 1.44x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 142 ms: 1.44x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 124 ms: 1.44x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 117 ms: 1.45x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 100 ms: 1.46x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                       |
| json_loads                 | 24.4 us                                                      | 35.6 us: 1.46x slower                                                       |
| scimark_fft                | 301 ms                                                       | 445 ms: 1.48x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.20 sec: 1.49x slower                                                      |
| pickle                     | 10.5 us                                                      | 15.7 us: 1.49x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.48 sec: 1.50x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 138 ms: 1.51x slower                                                        |
| richards_super             | 51.3 ms                                                      | 77.6 ms: 1.51x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 88.3 ms: 1.51x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 15.5 ms: 1.52x slower                                                       |
| nbody                      | 88.0 ms                                                      | 135 ms: 1.54x slower                                                        |
| fannkuch                   | 350 ms                                                       | 544 ms: 1.55x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.50 ms: 1.58x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 257 us: 1.69x slower                                                        |
| telco                      | 6.96 ms                                                      | 12.0 ms: 1.72x slower                                                       |
| python_startup             | 11.6 ms                                                      | 21.2 ms: 1.83x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 7.78 ms: 1.85x slower                                                       |
| mako                       | 10.0 ms                                                      | 19.7 ms: 1.97x slower                                                       |
| coverage                   | 66.7 ms                                                      | 135 ms: 2.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 780 ns: 8.27x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 61.7 ms: 12.96x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.27x slower                                                                |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.193x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.38x