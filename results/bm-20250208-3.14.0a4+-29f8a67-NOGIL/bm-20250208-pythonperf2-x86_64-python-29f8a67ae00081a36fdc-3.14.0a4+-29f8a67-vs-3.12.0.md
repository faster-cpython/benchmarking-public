# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.057x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 335 ms: 1.17x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 580 ms: 1.82x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 496 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 534 ms: 1.30x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 73.3 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 90.1 ms: 1.14x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.05x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 36.7 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 97.1 ms: 1.13x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 238 us: 1.13x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 5.44 us: 1.17x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 379 us: 1.19x slower                                                         |
| pickle               | 10.5 us                                                      | 12.5 us: 1.19x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.30 us: 1.20x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 69.8 ms: 1.20x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| json_loads           | 24.4 us                                                      | 32.1 us: 1.32x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| python_startup         | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.2 ms: 1.19x slower                                                        |
| mako            | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 580 ms: 1.82x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.06 ms: 1.69x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 496 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 534 ms: 1.30x faster                                                         |
| generators                 | 37.4 ms                                                      | 31.7 ms: 1.18x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 90.1 ms: 1.14x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| deepcopy                   | 368 us                                                       | 332 us: 1.11x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.9 us: 1.10x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.57 us: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| float                      | 76.6 ms                                                      | 73.3 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 36.3 us: 1.01x faster                                                        |
| go                         | 150 ms                                                       | 148 ms: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.8 ms: 1.06x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.56 us: 1.06x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.92 us: 1.06x slower                                                        |
| logging_simple             | 6.71 us                                                      | 7.11 us: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                         |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 69.9 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 172 ms: 1.08x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 872 ms: 1.08x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.78 sec: 1.08x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 127 ms: 1.10x slower                                                         |
| chaos                      | 64.0 ms                                                      | 70.7 ms: 1.10x slower                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.7 ms: 1.11x slower                                                        |
| pyflate                    | 439 ms                                                       | 486 ms: 1.11x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.84 sec: 1.11x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                       |
| sympy_str                  | 302 ms                                                       | 337 ms: 1.12x slower                                                         |
| asyncio_tcp                | 378 ms                                                       | 425 ms: 1.12x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 36.7 us: 1.13x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 97.1 ms: 1.13x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.1 ms: 1.13x slower                                                        |
| scimark_fft                | 301 ms                                                       | 341 ms: 1.13x slower                                                         |
| raytrace                   | 298 ms                                                       | 338 ms: 1.13x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 238 us: 1.13x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 65.3 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 2.04 ms: 1.15x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.3 ms: 1.16x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.44 us: 1.17x slower                                                        |
| sympy_expand               | 484 ms                                                       | 565 ms: 1.17x slower                                                         |
| 2to3                       | 285 ms                                                       | 335 ms: 1.17x slower                                                         |
| json                       | 5.12 ms                                                      | 6.03 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 117 ms: 1.18x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 63.0 ns: 1.18x slower                                                        |
| django_template            | 38.2 ms                                                      | 45.2 ms: 1.19x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 379 us: 1.19x slower                                                         |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.19x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.64 ms: 1.19x slower                                                        |
| async_generators           | 390 ms                                                       | 467 ms: 1.20x slower                                                         |
| pickle_list                | 4.43 us                                                      | 5.30 us: 1.20x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 69.8 ms: 1.20x slower                                                        |
| meteor_contest             | 128 ms                                                       | 154 ms: 1.20x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 83.0 ms: 1.20x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.23 ms: 1.21x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.22x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.96 ms: 1.23x slower                                                        |
| richards                   | 45.7 ms                                                      | 58.0 ms: 1.27x slower                                                        |
| richards_super             | 51.3 ms                                                      | 66.5 ms: 1.30x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.09 ms: 1.31x slower                                                        |
| json_loads                 | 24.4 us                                                      | 32.1 us: 1.32x slower                                                        |
| fannkuch                   | 350 ms                                                       | 468 ms: 1.34x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.77 ms: 1.37x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.52 ms: 1.40x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 217 us: 1.43x slower                                                         |
| nbody                      | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.46 ms: 1.53x slower                                                        |
| coverage                   | 66.7 ms                                                      | 104 ms: 1.56x slower                                                         |
| python_startup             | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 49.0 ms: 10.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                 |
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.27x