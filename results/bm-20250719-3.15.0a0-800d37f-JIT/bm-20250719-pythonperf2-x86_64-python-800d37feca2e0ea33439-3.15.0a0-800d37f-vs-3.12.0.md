# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.032x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.3 ms: 1.19x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 103 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.0 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 79.2 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 197 us: 1.06x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 55.6 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.9 us: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 35.0 us: 1.08x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.16 us: 1.11x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.04 us: 1.14x slower                                                       |
| pickle               | 10.5 us                                                      | 12.5 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.71 ms: 1.01x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.28 sec: 2.01x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| deepcopy                   | 368 us                                                       | 280 us: 1.32x faster                                                        |
| richards                   | 45.7 ms                                                      | 34.9 ms: 1.31x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.27x faster                                                       |
| richards_super             | 51.3 ms                                                      | 41.1 ms: 1.25x faster                                                       |
| float                      | 76.6 ms                                                      | 64.3 ms: 1.19x faster                                                       |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 80.6 ms: 1.14x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.61 us: 1.13x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 3.01 us: 1.12x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.91 ms: 1.11x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| dulwich_log                | 65.4 ms                                                      | 59.2 ms: 1.10x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.12 us: 1.10x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 737 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.2 ms: 1.09x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 49.1 ns: 1.08x faster                                                       |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| pyflate                    | 439 ms                                                       | 411 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 197 us: 1.06x faster                                                        |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.5 ms: 1.06x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 55.6 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.1 ms: 1.04x faster                                                       |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.0 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.7 ms: 1.02x faster                                                       |
| raytrace                   | 298 ms                                                       | 293 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 93.8 ns: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                        |
| unpickle                   | 14.8 us                                                      | 14.9 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.71 ms: 1.01x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 92.5 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.18 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.00 ms: 1.05x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 35.0 us: 1.08x slower                                                       |
| fannkuch                   | 350 ms                                                       | 380 ms: 1.09x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.16 us: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.04 us: 1.14x slower                                                       |
| nbody                      | 88.0 ms                                                      | 103 ms: 1.17x slower                                                        |
| async_generators           | 390 ms                                                       | 458 ms: 1.17x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.18x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.04 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 83.7 ms: 1.25x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.86 ms: 1.80x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                       |
| telco                      | 6.96 ms                                                      | 161 ms: 23.15x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.51 sec: 317.11x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (2): mako, regex_effbot
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x