# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 620 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 279 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 502 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.9 ms: 1.13x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 91.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 224 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.99 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 97.0 ms: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 204 us: 1.03x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                       |
| unpickle             | 14.8 us                                                      | 14.6 us: 1.01x faster                                                       |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.12 us: 1.10x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 620 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 279 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 502 ms: 1.39x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.1 us: 1.36x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.2 us: 1.35x faster                                                       |
| deepcopy                   | 368 us                                                       | 274 us: 1.34x faster                                                        |
| generators                 | 37.4 ms                                                      | 27.9 ms: 1.34x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 42.1 ns: 1.26x faster                                                       |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.54 us: 1.14x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                       |
| float                      | 76.6 ms                                                      | 67.9 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.98 us: 1.12x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.4 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                       |
| chaos                      | 64.0 ms                                                      | 58.8 ms: 1.09x faster                                                       |
| raytrace                   | 298 ms                                                       | 274 ms: 1.09x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.99 sec: 1.08x faster                                                      |
| pyflate                    | 439 ms                                                       | 406 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.07x faster                                                      |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 756 ms: 1.07x faster                                                        |
| regex_dna                  | 239 ms                                                       | 224 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.8 ms: 1.06x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 75.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.0 ms: 1.06x faster                                                       |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.5 ms: 1.06x faster                                                       |
| sympy_str                  | 302 ms                                                       | 285 ms: 1.06x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.0 ms: 1.05x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.7 ns: 1.03x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.79 ms: 1.03x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.5 ms: 1.03x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.15 ms: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 204 us: 1.03x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.7 ms: 1.01x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                       |
| unpickle                   | 14.8 us                                                      | 14.6 us: 1.01x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 489 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 973 us: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 92.2 ms: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                        |
| scimark_fft                | 301 ms                                                       | 311 ms: 1.03x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.87 us: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| nbody                      | 88.0 ms                                                      | 91.8 ms: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| async_generators           | 390 ms                                                       | 422 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.57 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.09x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.12 us: 1.10x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.92 ms: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 83.6 ms: 1.25x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.74 ms: 1.94x slower                                                       |
| telco                      | 6.96 ms                                                      | 159 ms: 22.89x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.27 sec: 266.97x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (3): docutils, pickle_dict, pycparser
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x