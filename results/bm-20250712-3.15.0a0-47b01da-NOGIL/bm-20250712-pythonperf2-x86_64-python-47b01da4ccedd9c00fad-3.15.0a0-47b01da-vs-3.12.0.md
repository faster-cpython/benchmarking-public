# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.063x slower
- HPT reliability: 98.15%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 538 ms: 1.96x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 569 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 237 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 302 ms: 1.79x faster                                                        |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 473 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 130 ms: 1.48x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 22.7 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 36.2 us: 1.11x slower                                                       |
| unpickle             | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 237 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 97.7 ms: 1.13x slower                                                       |
| json_loads           | 24.4 us                                                      | 28.2 us: 1.16x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 369 us: 1.16x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.20 us: 1.17x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.51 us: 1.18x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 12.1 ms: 1.18x slower                                                       |
| pickle               | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.7 ms: 1.69x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.52x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 44.3 ms: 1.16x slower                                                       |
| mako            | 10.0 ms                                                      | 17.5 ms: 1.75x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.43x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 538 ms: 1.96x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 569 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 237 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 302 ms: 1.79x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.46 sec: 1.76x faster                                                      |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.24 ms: 1.55x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 473 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                       |
| generators                 | 37.4 ms                                                      | 31.5 ms: 1.19x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| deepcopy                   | 368 us                                                       | 325 us: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                                       |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| float                      | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                       |
| go                         | 150 ms                                                       | 140 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.60 us: 1.07x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 34.5 us: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 61.6 ms: 1.06x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 22.7 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| asyncio_tcp                | 378 ms                                                       | 386 ms: 1.02x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.89 us: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| logging_format             | 7.48 us                                                      | 7.70 us: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.7 ms: 1.04x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.53 us: 1.05x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 55.9 ns: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.5 ns: 1.05x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.3 ms: 1.06x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 475 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.56 ms: 1.09x slower                                                       |
| sympy_str                  | 302 ms                                                       | 329 ms: 1.09x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 882 ms: 1.09x slower                                                        |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.82 sec: 1.10x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 36.2 us: 1.11x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.66 ms: 1.12x slower                                                       |
| 2to3                       | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 103 ms: 1.13x slower                                                        |
| unpickle                   | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 237 us: 1.13x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 97.7 ms: 1.13x slower                                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 79.3 ms: 1.15x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.72 ms: 1.15x slower                                                       |
| sympy_expand               | 484 ms                                                       | 561 ms: 1.16x slower                                                        |
| json_loads                 | 24.4 us                                                      | 28.2 us: 1.16x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 369 us: 1.16x slower                                                        |
| django_template            | 38.2 ms                                                      | 44.3 ms: 1.16x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 93.7 ms: 1.17x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.20 us: 1.17x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.87 sec: 1.18x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 5.51 us: 1.18x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 12.1 ms: 1.18x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| scimark_fft                | 301 ms                                                       | 358 ms: 1.19x slower                                                        |
| async_generators           | 390 ms                                                       | 465 ms: 1.19x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 118 ms: 1.20x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 108 ms: 1.20x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| richards                   | 45.7 ms                                                      | 56.6 ms: 1.24x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                       |
| richards_super             | 51.3 ms                                                      | 64.6 ms: 1.26x slower                                                       |
| fannkuch                   | 350 ms                                                       | 450 ms: 1.29x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 207 us: 1.37x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.91 ms: 1.41x slower                                                       |
| nbody                      | 88.0 ms                                                      | 130 ms: 1.48x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.41 ms: 1.49x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.7 ms: 1.69x slower                                                       |
| coverage                   | 66.7 ms                                                      | 117 ms: 1.75x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.5 ms: 1.75x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 56.9 ms: 11.94x slower                                                      |
| telco                      | 6.96 ms                                                      | 175 ms: 25.09x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.063x slower

# HPT report

- Reliability score: 98.15% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.35x