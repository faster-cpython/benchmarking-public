# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.006x slower
- HPT reliability: 98.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 314 ms                                                                                                                | 322 ms: 1.02x slower                                                                                                      |
| docutils       | 3.09 sec                                                                                                              | 3.17 sec: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 661 ms                                                                                                                | 635 ms: 1.04x faster                                                                                                      |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                                | 631 ms: 1.04x faster                                                                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| coroutines                 | 23.1 ms                                                                                                               | 23.2 ms: 1.00x slower                                                                                                     |
| async_tree_none_tg         | 298 ms                                                                                                                | 300 ms: 1.01x slower                                                                                                      |
| async_tree_memoization_tg  | 364 ms                                                                                                                | 367 ms: 1.01x slower                                                                                                      |
| asyncio_tcp                | 371 ms                                                                                                                | 374 ms: 1.01x slower                                                                                                      |
| async_tree_io              | 688 ms                                                                                                                | 699 ms: 1.02x slower                                                                                                      |
| async_tree_memoization     | 358 ms                                                                                                                | 363 ms: 1.02x slower                                                                                                      |
| async_tree_none            | 305 ms                                                                                                                | 312 ms: 1.02x slower                                                                                                      |
| async_generators           | 449 ms                                                                                                                | 472 ms: 1.05x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 81.8 ms                                                                                                               | 75.3 ms: 1.09x faster                                                                                                     |
| pidigits       | 254 ms                                                                                                                | 253 ms: 1.00x faster                                                                                                      |
| nbody          | 99.2 ms                                                                                                               | 109 ms: 1.10x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 27.2 ms                                                                                                               | 26.0 ms: 1.05x faster                                                                                                     |
| regex_dna      | 239 ms                                                                                                                | 239 ms: 1.00x faster                                                                                                      |
| regex_compile  | 153 ms                                                                                                                | 156 ms: 1.02x slower                                                                                                      |
| regex_effbot   | 3.24 ms                                                                                                               | 3.34 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 73.8 ms                                                                                                               | 71.5 ms: 1.03x faster                                                                                                     |
| tomli_loads          | 2.34 sec                                                                                                              | 2.27 sec: 1.03x faster                                                                                                    |
| xml_etree_parse      | 168 ms                                                                                                                | 164 ms: 1.03x faster                                                                                                      |
| xml_etree_generate   | 108 ms                                                                                                                | 106 ms: 1.02x faster                                                                                                      |
| json_loads           | 29.2 us                                                                                                               | 29.4 us: 1.00x slower                                                                                                     |
| pickle_dict          | 35.4 us                                                                                                               | 35.5 us: 1.00x slower                                                                                                     |
| pickle               | 14.8 us                                                                                                               | 14.9 us: 1.01x slower                                                                                                     |
| unpickle_pure_python | 241 us                                                                                                                | 244 us: 1.01x slower                                                                                                      |
| xml_etree_iterparse  | 114 ms                                                                                                                | 116 ms: 1.02x slower                                                                                                      |
| unpickle_list        | 5.50 us                                                                                                               | 5.59 us: 1.02x slower                                                                                                     |
| pickle_pure_python   | 380 us                                                                                                                | 391 us: 1.03x slower                                                                                                      |
| unpickle             | 18.0 us                                                                                                               | 18.6 us: 1.03x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 16.4 ms                                                                                                               | 16.4 ms: 1.00x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                                                                               | 12.9 ms: 1.02x faster                                                                                                     |
| django_template | 42.5 ms                                                                                                               | 43.2 ms: 1.02x slower                                                                                                     |
| genshi_text     | 27.5 ms                                                                                                               | 28.1 ms: 1.02x slower                                                                                                     |
| genshi_xml      | 59.8 ms                                                                                                               | 61.2 ms: 1.02x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                   | 52.3 ms                                                                                                               | 41.2 ms: 1.27x faster                                                                                                     |
| richards_super             | 59.4 ms                                                                                                               | 48.5 ms: 1.22x faster                                                                                                     |
| float                      | 81.8 ms                                                                                                               | 75.3 ms: 1.09x faster                                                                                                     |
| regex_v8                   | 27.2 ms                                                                                                               | 26.0 ms: 1.05x faster                                                                                                     |
| deltablue                  | 3.47 ms                                                                                                               | 3.34 ms: 1.04x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 661 ms                                                                                                                | 635 ms: 1.04x faster                                                                                                      |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                                | 631 ms: 1.04x faster                                                                                                      |
| k_core                     | 2.17 sec                                                                                                              | 2.10 sec: 1.04x faster                                                                                                    |
| xml_etree_process          | 73.8 ms                                                                                                               | 71.5 ms: 1.03x faster                                                                                                     |
| tomli_loads                | 2.34 sec                                                                                                              | 2.27 sec: 1.03x faster                                                                                                    |
| pprint_pformat             | 2.15 sec                                                                                                              | 2.10 sec: 1.03x faster                                                                                                    |
| xml_etree_parse            | 168 ms                                                                                                                | 164 ms: 1.03x faster                                                                                                      |
| create_gc_cycles           | 3.00 ms                                                                                                               | 2.94 ms: 1.02x faster                                                                                                     |
| mako                       | 13.2 ms                                                                                                               | 12.9 ms: 1.02x faster                                                                                                     |
| xml_etree_generate         | 108 ms                                                                                                                | 106 ms: 1.02x faster                                                                                                      |
| scimark_sparse_mat_mult    | 6.53 ms                                                                                                               | 6.40 ms: 1.02x faster                                                                                                     |
| gc_traversal               | 5.73 ms                                                                                                               | 5.62 ms: 1.02x faster                                                                                                     |
| coverage                   | 101 ms                                                                                                                | 99.8 ms: 1.02x faster                                                                                                     |
| connected_components       | 433 ms                                                                                                                | 427 ms: 1.01x faster                                                                                                      |
| sqlite_synth               | 3.40 us                                                                                                               | 3.36 us: 1.01x faster                                                                                                     |
| scimark_fft                | 386 ms                                                                                                                | 383 ms: 1.01x faster                                                                                                      |
| logging_silent             | 689 ns                                                                                                                | 685 ns: 1.01x faster                                                                                                      |
| shortest_path              | 462 ms                                                                                                                | 460 ms: 1.01x faster                                                                                                      |
| pidigits                   | 254 ms                                                                                                                | 253 ms: 1.00x faster                                                                                                      |
| regex_dna                  | 239 ms                                                                                                                | 239 ms: 1.00x faster                                                                                                      |
| python_startup             | 16.4 ms                                                                                                               | 16.4 ms: 1.00x slower                                                                                                     |
| mdp                        | 1.56 sec                                                                                                              | 1.56 sec: 1.00x slower                                                                                                    |
| json_loads                 | 29.2 us                                                                                                               | 29.4 us: 1.00x slower                                                                                                     |
| pickle_dict                | 35.4 us                                                                                                               | 35.5 us: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| coroutines                 | 23.1 ms                                                                                                               | 23.2 ms: 1.00x slower                                                                                                     |
| async_tree_none_tg         | 298 ms                                                                                                                | 300 ms: 1.01x slower                                                                                                      |
| logging_format             | 8.27 us                                                                                                               | 8.33 us: 1.01x slower                                                                                                     |
| pickle                     | 14.8 us                                                                                                               | 14.9 us: 1.01x slower                                                                                                     |
| async_tree_memoization_tg  | 364 ms                                                                                                                | 367 ms: 1.01x slower                                                                                                      |
| pyflate                    | 467 ms                                                                                                                | 471 ms: 1.01x slower                                                                                                      |
| asyncio_tcp                | 371 ms                                                                                                                | 374 ms: 1.01x slower                                                                                                      |
| unpickle_pure_python       | 241 us                                                                                                                | 244 us: 1.01x slower                                                                                                      |
| bpe_tokeniser              | 5.62 sec                                                                                                              | 5.69 sec: 1.01x slower                                                                                                    |
| meteor_contest             | 140 ms                                                                                                                | 142 ms: 1.01x slower                                                                                                      |
| deepcopy_reduce            | 3.53 us                                                                                                               | 3.58 us: 1.01x slower                                                                                                     |
| raytrace                   | 335 ms                                                                                                                | 339 ms: 1.01x slower                                                                                                      |
| sqlglot_v2_normalize       | 135 ms                                                                                                                | 137 ms: 1.01x slower                                                                                                      |
| pathlib                    | 19.8 ms                                                                                                               | 20.1 ms: 1.01x slower                                                                                                     |
| async_tree_io              | 688 ms                                                                                                                | 699 ms: 1.02x slower                                                                                                      |
| async_tree_memoization     | 358 ms                                                                                                                | 363 ms: 1.02x slower                                                                                                      |
| xml_etree_iterparse        | 114 ms                                                                                                                | 116 ms: 1.02x slower                                                                                                      |
| sympy_sum                  | 168 ms                                                                                                                | 171 ms: 1.02x slower                                                                                                      |
| pylint                     | 349 ms                                                                                                                | 355 ms: 1.02x slower                                                                                                      |
| telco                      | 9.52 ms                                                                                                               | 9.68 ms: 1.02x slower                                                                                                     |
| unpickle_list              | 5.50 us                                                                                                               | 5.59 us: 1.02x slower                                                                                                     |
| bench_thread_pool          | 1.04 ms                                                                                                               | 1.06 ms: 1.02x slower                                                                                                     |
| django_template            | 42.5 ms                                                                                                               | 43.2 ms: 1.02x slower                                                                                                     |
| regex_compile              | 153 ms                                                                                                                | 156 ms: 1.02x slower                                                                                                      |
| genshi_text                | 27.5 ms                                                                                                               | 28.1 ms: 1.02x slower                                                                                                     |
| sympy_str                  | 330 ms                                                                                                                | 337 ms: 1.02x slower                                                                                                      |
| typing_runtime_protocols   | 208 us                                                                                                                | 213 us: 1.02x slower                                                                                                      |
| logging_simple             | 7.41 us                                                                                                               | 7.58 us: 1.02x slower                                                                                                     |
| docutils                   | 3.09 sec                                                                                                              | 3.17 sec: 1.02x slower                                                                                                    |
| 2to3                       | 314 ms                                                                                                                | 322 ms: 1.02x slower                                                                                                      |
| async_tree_none            | 305 ms                                                                                                                | 312 ms: 1.02x slower                                                                                                      |
| genshi_xml                 | 59.8 ms                                                                                                               | 61.2 ms: 1.02x slower                                                                                                     |
| nqueens                    | 108 ms                                                                                                                | 111 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_optimize        | 67.0 ms                                                                                                               | 68.8 ms: 1.03x slower                                                                                                     |
| deepcopy                   | 320 us                                                                                                                | 328 us: 1.03x slower                                                                                                      |
| many_optionals             | 1.13 ms                                                                                                               | 1.16 ms: 1.03x slower                                                                                                     |
| sqlglot_v2_transpile       | 1.91 ms                                                                                                               | 1.96 ms: 1.03x slower                                                                                                     |
| pickle_pure_python         | 380 us                                                                                                                | 391 us: 1.03x slower                                                                                                      |
| sympy_integrate            | 23.6 ms                                                                                                               | 24.3 ms: 1.03x slower                                                                                                     |
| regex_effbot               | 3.24 ms                                                                                                               | 3.34 ms: 1.03x slower                                                                                                     |
| unpickle                   | 18.0 us                                                                                                               | 18.6 us: 1.03x slower                                                                                                     |
| scimark_lu                 | 116 ms                                                                                                                | 120 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_parse           | 1.49 ms                                                                                                               | 1.54 ms: 1.03x slower                                                                                                     |
| sympy_expand               | 571 ms                                                                                                                | 592 ms: 1.04x slower                                                                                                      |
| chaos                      | 71.0 ms                                                                                                               | 73.6 ms: 1.04x slower                                                                                                     |
| crypto_pyaes               | 87.9 ms                                                                                                               | 91.2 ms: 1.04x slower                                                                                                     |
| deepcopy_memo              | 31.5 us                                                                                                               | 32.9 us: 1.04x slower                                                                                                     |
| async_generators           | 449 ms                                                                                                                | 472 ms: 1.05x slower                                                                                                      |
| scimark_sor                | 119 ms                                                                                                                | 126 ms: 1.06x slower                                                                                                      |
| hexiom                     | 6.54 ms                                                                                                               | 6.94 ms: 1.06x slower                                                                                                     |
| unpack_sequence            | 56.6 ns                                                                                                               | 60.4 ns: 1.07x slower                                                                                                     |
| spectral_norm              | 111 ms                                                                                                                | 118 ms: 1.07x slower                                                                                                      |
| generators                 | 32.4 ms                                                                                                               | 34.9 ms: 1.08x slower                                                                                                     |
| fannkuch                   | 444 ms                                                                                                                | 486 ms: 1.10x slower                                                                                                      |
| nbody                      | 99.2 ms                                                                                                               | 109 ms: 1.10x slower                                                                                                      |
| go                         | 129 ms                                                                                                                | 143 ms: 1.11x slower                                                                                                      |
| comprehensions             | 18.9 us                                                                                                               | 21.2 us: 1.12x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (16): pprint_safe_repr, pycparser, dulwich_log, asyncio_websockets, thrift, python_startup_no_site, json, djangocms, json_dumps, pickle_list, subparsers, html5lib, async_tree_io_tg, sphinx, scimark_monte_carlo, bench_mp_pool

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x