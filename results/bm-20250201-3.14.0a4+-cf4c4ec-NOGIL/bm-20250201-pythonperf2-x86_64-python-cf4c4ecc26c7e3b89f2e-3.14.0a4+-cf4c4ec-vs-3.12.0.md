# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.058x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 332 ms: 1.17x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 577 ms: 1.83x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 256 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 248 ms: 1.07x faster                                                         |
| float          | 76.6 ms                                                      | 74.5 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 128 ms: 1.46x slower                                                         |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| regex_compile  | 144 ms                                                       | 153 ms: 1.07x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.6 ms: 1.15x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.06x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 96.8 ms: 1.12x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 36.6 us: 1.13x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 236 us: 1.13x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 5.39 us: 1.16x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 370 us: 1.16x slower                                                         |
| pickle               | 10.5 us                                                      | 12.4 us: 1.18x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.42 us: 1.22x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.7 ms: 1.33x slower                                                        |
| json_loads           | 24.4 us                                                      | 32.9 us: 1.35x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                        |
| python_startup         | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.4 ms: 1.19x slower                                                        |
| mako            | 10.0 ms                                                      | 17.9 ms: 1.79x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.46x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 577 ms: 1.83x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.05 ms: 1.70x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 256 ms: 1.68x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 495 ms: 1.41x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                        |
| generators                 | 37.4 ms                                                      | 32.0 ms: 1.17x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 89.6 ms: 1.15x faster                                                        |
| deepcopy                   | 368 us                                                       | 327 us: 1.13x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.7 us: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.59 us: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 248 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| float                      | 76.6 ms                                                      | 74.5 ms: 1.03x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 379 ms: 1.02x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 36.3 us: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 55.7 ns: 1.05x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 99.6 ns: 1.06x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.06x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 69.0 ms: 1.06x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.56 us: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.07x slower                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 171 ms: 1.07x slower                                                         |
| logging_simple             | 6.71 us                                                      | 7.21 us: 1.07x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.76 sec: 1.08x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.08x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| logging_format             | 7.48 us                                                      | 8.07 us: 1.08x slower                                                        |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.5 ms: 1.09x slower                                                        |
| chaos                      | 64.0 ms                                                      | 70.2 ms: 1.10x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 896 ms: 1.11x slower                                                         |
| sympy_str                  | 302 ms                                                       | 337 ms: 1.12x slower                                                         |
| scimark_fft                | 301 ms                                                       | 337 ms: 1.12x slower                                                         |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.86 sec: 1.12x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 425 ms: 1.12x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 96.8 ms: 1.12x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 36.6 us: 1.13x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.9 ms: 1.13x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 236 us: 1.13x slower                                                         |
| raytrace                   | 298 ms                                                       | 337 ms: 1.13x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 2.03 ms: 1.14x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 65.7 ms: 1.14x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.39 us: 1.16x slower                                                        |
| sympy_expand               | 484 ms                                                       | 561 ms: 1.16x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 370 us: 1.16x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 93.6 ms: 1.16x slower                                                        |
| 2to3                       | 285 ms                                                       | 332 ms: 1.17x slower                                                         |
| pickle                     | 10.5 us                                                      | 12.4 us: 1.18x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.62 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                       |
| django_template            | 38.2 ms                                                      | 45.4 ms: 1.19x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                        |
| json                       | 5.12 ms                                                      | 6.15 ms: 1.20x slower                                                        |
| async_generators           | 390 ms                                                       | 470 ms: 1.20x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 119 ms: 1.20x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.19 ms: 1.21x slower                                                        |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 84.4 ms: 1.22x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.42 us: 1.22x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.23x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                        |
| richards                   | 45.7 ms                                                      | 59.2 ms: 1.29x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.47 ms: 1.30x slower                                                        |
| richards_super             | 51.3 ms                                                      | 67.2 ms: 1.31x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.12 ms: 1.31x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.7 ms: 1.33x slower                                                        |
| json_loads                 | 24.4 us                                                      | 32.9 us: 1.35x slower                                                        |
| fannkuch                   | 350 ms                                                       | 476 ms: 1.36x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.49 ms: 1.39x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 213 us: 1.41x slower                                                         |
| nbody                      | 88.0 ms                                                      | 128 ms: 1.46x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.46 ms: 1.54x slower                                                        |
| python_startup             | 11.6 ms                                                      | 18.7 ms: 1.61x slower                                                        |
| coverage                   | 66.7 ms                                                      | 108 ms: 1.62x slower                                                         |
| mako                       | 10.0 ms                                                      | 17.9 ms: 1.79x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 47.5 ms: 9.97x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                 |

Benchmark hidden because not significant (2): go, pycparser
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.25x