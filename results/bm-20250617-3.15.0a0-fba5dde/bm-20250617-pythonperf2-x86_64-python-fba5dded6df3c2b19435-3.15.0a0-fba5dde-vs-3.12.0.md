# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.128x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.09 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 688 ms: 1.51x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 703 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 364 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 305 ms: 1.48x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 298 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 655 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 661 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 81.8 ms: 1.07x slower                                                       |
| nbody          | 88.0 ms                                                      | 99.2 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                       |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.34 sec: 1.08x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 35.4 us: 1.09x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 241 us: 1.15x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.50 us: 1.18x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 380 us: 1.19x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.2 us: 1.20x slower                                                       |
| unpickle             | 14.8 us                                                      | 18.0 us: 1.22x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 108 ms: 1.25x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 73.8 ms: 1.26x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.91 us: 1.33x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| pickle               | 10.5 us                                                      | 14.8 us: 1.41x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.5 ms: 1.11x slower                                                       |
| mako            | 10.0 ms                                                      | 13.2 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.56 sec: 1.65x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 688 ms: 1.51x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 703 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 364 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 305 ms: 1.48x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 298 ms: 1.44x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 31.5 us: 1.17x faster                                                       |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.9 us: 1.16x faster                                                       |
| generators                 | 37.4 ms                                                      | 32.4 ms: 1.16x faster                                                       |
| deepcopy                   | 368 us                                                       | 320 us: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 655 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 661 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 63.9 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                       |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 23.1 ms: 1.01x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.04x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.53 us: 1.05x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.8 ms: 1.05x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 56.6 ns: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 467 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| float                      | 76.6 ms                                                      | 81.8 ms: 1.07x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.47 ms: 1.07x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.09 sec: 1.08x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.34 sec: 1.08x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.34 sec: 1.08x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 35.4 us: 1.09x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                       |
| sympy_str                  | 302 ms                                                       | 330 ms: 1.09x slower                                                        |
| meteor_contest             | 128 ms                                                       | 140 ms: 1.09x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 87.9 ms: 1.09x slower                                                       |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.10x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.54 ms: 1.10x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.04 ms: 1.10x slower                                                       |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 76.0 ms: 1.10x slower                                                       |
| logging_simple             | 6.71 us                                                      | 7.41 us: 1.10x slower                                                       |
| logging_format             | 7.48 us                                                      | 8.27 us: 1.10x slower                                                       |
| chaos                      | 64.0 ms                                                      | 71.0 ms: 1.11x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.5 ms: 1.11x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                                        |
| raytrace                   | 298 ms                                                       | 335 ms: 1.12x slower                                                        |
| nbody                      | 88.0 ms                                                      | 99.2 ms: 1.13x slower                                                       |
| richards                   | 45.7 ms                                                      | 52.3 ms: 1.14x slower                                                       |
| async_generators           | 390 ms                                                       | 449 ms: 1.15x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 241 us: 1.15x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                       |
| richards_super             | 51.3 ms                                                      | 59.4 ms: 1.16x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| json                       | 5.12 ms                                                      | 6.02 ms: 1.18x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.18x slower                                                        |
| sympy_expand               | 484 ms                                                       | 571 ms: 1.18x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.50 us: 1.18x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 380 us: 1.19x slower                                                        |
| json_loads                 | 24.4 us                                                      | 29.2 us: 1.20x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 108 ms: 1.20x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 111 ms: 1.21x slower                                                        |
| unpickle                   | 14.8 us                                                      | 18.0 us: 1.22x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 3.40 us: 1.22x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 108 ms: 1.25x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 73.8 ms: 1.26x slower                                                       |
| fannkuch                   | 350 ms                                                       | 444 ms: 1.27x slower                                                        |
| scimark_fft                | 301 ms                                                       | 386 ms: 1.28x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.15 sec: 1.30x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.06 sec: 1.31x slower                                                      |
| mako                       | 10.0 ms                                                      | 13.2 ms: 1.32x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.91 us: 1.33x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.52 ms: 1.37x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 208 us: 1.37x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| pickle                     | 10.5 us                                                      | 14.8 us: 1.41x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| coverage                   | 66.7 ms                                                      | 101 ms: 1.52x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.53 ms: 1.55x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.73 ms: 1.65x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 3.00 ms: 1.89x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 689 ns: 7.30x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.46 sec: 305.57x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.12x