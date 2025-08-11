# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.057x slower
- HPT reliability: 97.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 316 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 531 ms: 1.98x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 561 ms: 1.86x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 295 ms: 1.83x faster                                                        |
| async_tree_none            | 452 ms                                                       | 263 ms: 1.72x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 468 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 496 ms: 1.40x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 22.8 ms: 1.04x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 86.1 ms: 1.19x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 35.1 us: 1.08x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.33 sec: 1.08x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.96 us: 1.12x slower                                                       |
| unpickle             | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 97.5 ms: 1.13x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 364 us: 1.14x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 241 us: 1.15x slower                                                        |
| pickle               | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 69.7 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                                       |
| mako            | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 531 ms: 1.98x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 561 ms: 1.86x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 295 ms: 1.83x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.77x faster                                                      |
| async_tree_none            | 452 ms                                                       | 263 ms: 1.72x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.24 ms: 1.55x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 468 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 496 ms: 1.40x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 86.1 ms: 1.19x faster                                                       |
| deepcopy                   | 368 us                                                       | 319 us: 1.15x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                       |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| float                      | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.61 us: 1.06x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 34.8 us: 1.06x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 61.8 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 22.8 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.60 us: 1.02x slower                                                       |
| logging_simple             | 6.71 us                                                      | 6.82 us: 1.02x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 386 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.6 ns: 1.02x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 54.7 ns: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 3.50 us: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.1 ms: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                       |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.1 us: 1.08x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.33 sec: 1.08x slower                                                      |
| sympy_str                  | 302 ms                                                       | 327 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 477 ms: 1.09x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.57 ms: 1.10x slower                                                       |
| 2to3                       | 285 ms                                                       | 316 ms: 1.11x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.96 us: 1.12x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 906 ms: 1.12x slower                                                        |
| raytrace                   | 298 ms                                                       | 335 ms: 1.12x slower                                                        |
| django_template            | 38.2 ms                                                      | 42.9 ms: 1.12x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 97.5 ms: 1.13x slower                                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.88 sec: 1.14x slower                                                      |
| sympy_expand               | 484 ms                                                       | 554 ms: 1.14x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 364 us: 1.14x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.70 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 241 us: 1.15x slower                                                        |
| scimark_fft                | 301 ms                                                       | 348 ms: 1.15x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.0 ms: 1.16x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 80.2 ms: 1.16x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.17x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.89 sec: 1.19x slower                                                      |
| json_loads                 | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 69.7 ms: 1.19x slower                                                       |
| async_generators           | 390 ms                                                       | 468 ms: 1.20x slower                                                        |
| richards                   | 45.7 ms                                                      | 55.4 ms: 1.21x slower                                                       |
| richards_super             | 51.3 ms                                                      | 63.6 ms: 1.24x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 114 ms: 1.24x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                       |
| fannkuch                   | 350 ms                                                       | 475 ms: 1.36x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 206 us: 1.36x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.83 ms: 1.39x slower                                                       |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.41 ms: 1.49x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                       |
| mako                       | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                       |
| coverage                   | 66.7 ms                                                      | 119 ms: 1.78x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 57.7 ms: 12.11x slower                                                      |
| telco                      | 6.96 ms                                                      | 174 ms: 24.94x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (1): docutils
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 97.70% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.36x