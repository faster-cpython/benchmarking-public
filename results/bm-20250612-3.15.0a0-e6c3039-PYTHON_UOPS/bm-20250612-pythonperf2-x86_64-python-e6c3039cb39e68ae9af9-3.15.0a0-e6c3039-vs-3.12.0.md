# Results vs. 3.12.0

- fork: python
- ref: e6c3039cb39e68ae9af9
- machine: linux-x86_64
- commit hash: e6c3039
- commit date: 2025-06-12
- overall geometric mean: 1.112x slower
- HPT reliability: 98.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 321 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 666 ms: 1.56x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 676 ms: 1.56x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 356 ms: 1.53x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 357 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 291 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 307 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 530 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 531 ms: 1.31x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.46x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 260 ms: 1.02x faster                                                        |
| float          | 76.6 ms                                                      | 105 ms: 1.38x slower                                                        |
| nbody          | 88.0 ms                                                      | 187 ms: 2.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.42x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 221 ms: 1.08x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.77 ms: 1.06x slower                                                       |
| regex_compile  | 144 ms                                                       | 160 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 107 ms: 1.24x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 75.0 ms: 1.28x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 410 us: 1.29x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 3.17 sec: 1.47x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 382 us: 1.82x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.23x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                       |
| mako            | 10.0 ms                                                      | 16.8 ms: 1.68x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.26x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.46 sec: 1.76x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 666 ms: 1.56x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 676 ms: 1.56x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 356 ms: 1.53x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 357 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 291 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 307 ms: 1.47x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.4 us: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 530 ms: 1.32x faster                                                        |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 531 ms: 1.31x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                       |
| regex_dna                  | 239 ms                                                       | 221 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 61.8 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.5 ms: 1.06x faster                                                       |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.26 us: 1.03x faster                                                       |
| pidigits                   | 265 ms                                                       | 260 ms: 1.02x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.02x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| json                       | 5.12 ms                                                      | 5.29 ms: 1.03x slower                                                       |
| sympy_str                  | 302 ms                                                       | 314 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 107 ms: 1.04x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.77 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 3.04 us: 1.09x slower                                                       |
| regex_compile              | 144 ms                                                       | 160 ms: 1.11x slower                                                        |
| raytrace                   | 298 ms                                                       | 334 ms: 1.12x slower                                                        |
| sympy_expand               | 484 ms                                                       | 543 ms: 1.12x slower                                                        |
| 2to3                       | 285 ms                                                       | 321 ms: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 104 ms: 1.15x slower                                                        |
| async_generators           | 390 ms                                                       | 460 ms: 1.18x slower                                                        |
| richards                   | 45.7 ms                                                      | 54.2 ms: 1.19x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.47 sec: 1.19x slower                                                      |
| richards_super             | 51.3 ms                                                      | 61.1 ms: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 80.5 ms: 1.21x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 107 ms: 1.24x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 87.7 ms: 1.27x slower                                                       |
| meteor_contest             | 128 ms                                                       | 164 ms: 1.28x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 75.0 ms: 1.28x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 410 us: 1.29x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.18 ms: 1.32x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 202 us: 1.33x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 108 ms: 1.34x slower                                                        |
| float                      | 76.6 ms                                                      | 105 ms: 1.38x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.3 us: 1.38x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.40 sec: 1.45x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.18 sec: 1.47x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 3.17 sec: 1.47x slower                                                      |
| go                         | 150 ms                                                       | 220 ms: 1.47x slower                                                        |
| pyflate                    | 439 ms                                                       | 650 ms: 1.48x slower                                                        |
| scimark_fft                | 301 ms                                                       | 493 ms: 1.64x slower                                                        |
| mako                       | 10.0 ms                                                      | 16.8 ms: 1.68x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 10.4 ms: 1.75x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 382 us: 1.82x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 5.92 ms: 1.83x slower                                                       |
| fannkuch                   | 350 ms                                                       | 644 ms: 1.84x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.70 ms: 1.93x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 8.32 ms: 1.98x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 191 ms: 2.09x slower                                                        |
| nbody                      | 88.0 ms                                                      | 187 ms: 2.13x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 504 ns: 5.34x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, sympy_sum, asyncio_websockets, chaos
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250612-3.15.0a0-e6c3039-PYTHON_UOPS/bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x slower

# HPT report

- Reliability score: 98.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x