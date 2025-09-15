# Results vs. 3.12.0

- fork: savannahostrowski
- ref: poptimize
- machine: linux-x86_64
- commit hash: c6edbf9
- commit date: 2025-09-15
- overall geometric mean: 1.035x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 96.6 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 192 us: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 79.7 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.0 ms: 1.04x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 324 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.0 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.85 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.08x faster                                                       |
| mako            | 10.0 ms                                                      | 9.62 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.1 us: 1.41x faster                                                       |
| deepcopy                   | 368 us                                                       | 262 us: 1.41x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| go                         | 150 ms                                                       | 120 ms: 1.25x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.44 us: 1.16x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 79.6 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.86 us: 1.14x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                      |
| float                      | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.5 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.2 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| pyflate                    | 439 ms                                                       | 397 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 734 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 192 us: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.7 ms: 1.08x faster                                                       |
| chaos                      | 64.0 ms                                                      | 59.2 ms: 1.08x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.08x faster                                                       |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                        |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                                       |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 56.0 ms: 1.04x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 77.1 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.62 ms: 1.04x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.3 ms: 1.03x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 91.9 ns: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.5 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.18 ms: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.90 ms: 1.01x faster                                                       |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 324 us: 1.02x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.85 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 93.3 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.07x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.0 us: 1.07x slower                                                       |
| fannkuch                   | 350 ms                                                       | 380 ms: 1.09x slower                                                        |
| nbody                      | 88.0 ms                                                      | 96.6 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.12x slower                                                        |
| async_generators           | 390 ms                                                       | 445 ms: 1.14x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.87 ms: 1.16x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.95 ms: 1.86x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.68 ms: 1.92x slower                                                       |
| telco                      | 6.96 ms                                                      | 160 ms: 22.95x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250915-3.15.0a0-c6edbf9-JIT/bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x