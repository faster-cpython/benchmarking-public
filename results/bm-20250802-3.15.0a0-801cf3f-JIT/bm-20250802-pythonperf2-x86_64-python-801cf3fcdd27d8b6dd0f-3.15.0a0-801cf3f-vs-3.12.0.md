# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.035x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 627 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                        |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.9 ms: 1.20x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 98.1 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 195 us: 1.08x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 34.2 us: 1.05x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.99 us: 1.07x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.00 us: 1.13x slower                                                       |
| pickle               | 10.5 us                                                      | 12.7 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.8 ms: 1.10x faster                                                       |
| mako            | 10.0 ms                                                      | 9.79 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 627 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                        |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                        |
| deepcopy                   | 368 us                                                       | 276 us: 1.33x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.4 us: 1.29x faster                                                       |
| richards                   | 45.7 ms                                                      | 35.6 ms: 1.29x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| richards_super             | 51.3 ms                                                      | 41.2 ms: 1.25x faster                                                       |
| float                      | 76.6 ms                                                      | 63.9 ms: 1.20x faster                                                       |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.50 us: 1.15x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.91 us: 1.13x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.2 ms: 1.13x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.88 ms: 1.12x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 729 ms: 1.11x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.8 ms: 1.10x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.7 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.0 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 195 us: 1.08x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.2 ms: 1.08x faster                                                       |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                        |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 50.9 ns: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.3 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| pyflate                    | 439 ms                                                       | 423 ms: 1.04x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 56.6 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.79 ms: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.79 us: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                        |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 93.3 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.32 ms: 1.04x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 987 us: 1.04x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.20 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.2 us: 1.05x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.99 us: 1.07x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                       |
| nbody                      | 88.0 ms                                                      | 98.1 ms: 1.11x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.00 us: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                        |
| async_generators           | 390 ms                                                       | 448 ms: 1.15x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.7 ms: 1.20x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.7 us: 1.21x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.28 ms: 1.81x slower                                                       |
| telco                      | 6.96 ms                                                      | 158 ms: 22.68x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.38 sec: 290.54x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, pycparser, logging_silent
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x