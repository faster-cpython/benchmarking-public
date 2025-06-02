# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.374x faster
- HPT reliability: 90.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                                                          | 297 ms: 1.03x slower                                                                                                |
| docutils       | 2.84 sec                                                                                                        | 2.91 sec: 1.02x slower                                                                                              |
| html5lib       | 66.2 ms                                                                                                         | 65.4 ms: 1.01x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 598 ms                                                                                                          | 579 ms: 1.03x faster                                                                                                |
| async_tree_io_tg           | 696 ms                                                                                                          | 678 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed    | 607 ms                                                                                                          | 592 ms: 1.03x faster                                                                                                |
| coroutines                 | 28.1 ms                                                                                                         | 27.4 ms: 1.02x faster                                                                                               |
| async_tree_memoization_tg  | 352 ms                                                                                                          | 345 ms: 1.02x faster                                                                                                |
| async_tree_none_tg         | 279 ms                                                                                                          | 274 ms: 1.02x faster                                                                                                |
| async_tree_memoization     | 350 ms                                                                                                          | 345 ms: 1.01x faster                                                                                                |
| asyncio_tcp_ssl            | 1.82 sec                                                                                                        | 1.82 sec: 1.00x slower                                                                                              |
| asyncio_tcp                | 484 ms                                                                                                          | 491 ms: 1.02x slower                                                                                                |
| async_generators           | 416 ms                                                                                                          | 439 ms: 1.05x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (3): async_tree_none, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 109 ms                                                                                                          | 98.5 ms: 1.11x faster                                                                                               |
| float          | 75.1 ms                                                                                                         | 69.2 ms: 1.09x faster                                                                                               |
| pidigits       | 202 ms                                                                                                          | 206 ms: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.06x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                                                          | 201 ms: 1.01x faster                                                                                                |
| regex_v8       | 24.0 ms                                                                                                         | 24.9 ms: 1.03x slower                                                                                               |
| regex_effbot   | 3.00 ms                                                                                                         | 3.20 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 255 us                                                                                                          | 234 us: 1.09x faster                                                                                                |
| tomli_loads          | 2.25 sec                                                                                                        | 2.09 sec: 1.08x faster                                                                                              |
| xml_etree_process    | 73.6 ms                                                                                                         | 69.2 ms: 1.06x faster                                                                                               |
| xml_etree_generate   | 107 ms                                                                                                          | 102 ms: 1.05x faster                                                                                                |
| pickle_pure_python   | 380 us                                                                                                          | 372 us: 1.02x faster                                                                                                |
| pickle               | 15.0 us                                                                                                         | 14.9 us: 1.01x faster                                                                                               |
| json_loads           | 33.9 us                                                                                                         | 33.6 us: 1.01x faster                                                                                               |
| json_dumps           | 13.3 ms                                                                                                         | 13.4 ms: 1.01x slower                                                                                               |
| unpickle             | 18.9 us                                                                                                         | 19.1 us: 1.01x slower                                                                                               |
| pickle_list          | 5.85 us                                                                                                         | 6.01 us: 1.03x slower                                                                                               |
| pickle_dict          | 36.2 us                                                                                                         | 37.8 us: 1.04x slower                                                                                               |
| unpickle_list        | 5.59 us                                                                                                         | 5.86 us: 1.05x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.42 ms                                                                                                         | 7.40 ms: 1.00x faster                                                                                               |
| python_startup         | 13.2 ms                                                                                                         | 13.1 ms: 1.00x faster                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.7 ms                                                                                                         | 13.3 ms: 1.03x faster                                                                                               |
| django_template | 40.3 ms                                                                                                         | 39.9 ms: 1.01x faster                                                                                               |
| genshi_xml      | 57.5 ms                                                                                                         | 58.2 ms: 1.01x slower                                                                                               |
| genshi_text     | 25.0 ms                                                                                                         | 25.3 ms: 1.01x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.00x faster                                                                                                        |

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 2.01 sec                                                                                                        | 1.86 us: 1083218.98x faster                                                                                         |
| pprint_safe_repr           | 988 ms                                                                                                          | 1.12 us: 878737.26x faster                                                                                          |
| richards                   | 54.3 ms                                                                                                         | 39.6 ms: 1.37x faster                                                                                               |
| richards_super             | 61.5 ms                                                                                                         | 46.3 ms: 1.33x faster                                                                                               |
| scimark_fft                | 420 ms                                                                                                          | 353 ms: 1.19x faster                                                                                                |
| deltablue                  | 3.86 ms                                                                                                         | 3.37 ms: 1.14x faster                                                                                               |
| nbody                      | 109 ms                                                                                                          | 98.5 ms: 1.11x faster                                                                                               |
| unpickle_pure_python       | 255 us                                                                                                          | 234 us: 1.09x faster                                                                                                |
| float                      | 75.1 ms                                                                                                         | 69.2 ms: 1.09x faster                                                                                               |
| tomli_loads                | 2.25 sec                                                                                                        | 2.09 sec: 1.08x faster                                                                                              |
| scimark_monte_carlo        | 78.2 ms                                                                                                         | 73.1 ms: 1.07x faster                                                                                               |
| xml_etree_process          | 73.6 ms                                                                                                         | 69.2 ms: 1.06x faster                                                                                               |
| pyflate                    | 476 ms                                                                                                          | 450 ms: 1.06x faster                                                                                                |
| connected_components       | 487 ms                                                                                                          | 463 ms: 1.05x faster                                                                                                |
| shortest_path              | 529 ms                                                                                                          | 504 ms: 1.05x faster                                                                                                |
| xml_etree_generate         | 107 ms                                                                                                          | 102 ms: 1.05x faster                                                                                                |
| logging_silent             | 651 ns                                                                                                          | 623 ns: 1.05x faster                                                                                                |
| telco                      | 9.39 ms                                                                                                         | 9.04 ms: 1.04x faster                                                                                               |
| spectral_norm              | 113 ms                                                                                                          | 110 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 598 ms                                                                                                          | 579 ms: 1.03x faster                                                                                                |
| sqlite_synth               | 3.17 us                                                                                                         | 3.08 us: 1.03x faster                                                                                               |
| mako                       | 13.7 ms                                                                                                         | 13.3 ms: 1.03x faster                                                                                               |
| async_tree_io_tg           | 696 ms                                                                                                          | 678 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed    | 607 ms                                                                                                          | 592 ms: 1.03x faster                                                                                                |
| coroutines                 | 28.1 ms                                                                                                         | 27.4 ms: 1.02x faster                                                                                               |
| fannkuch                   | 491 ms                                                                                                          | 479 ms: 1.02x faster                                                                                                |
| bpe_tokeniser              | 5.25 sec                                                                                                        | 5.14 sec: 1.02x faster                                                                                              |
| async_tree_memoization_tg  | 352 ms                                                                                                          | 345 ms: 1.02x faster                                                                                                |
| pickle_pure_python         | 380 us                                                                                                          | 372 us: 1.02x faster                                                                                                |
| logging_format             | 8.58 us                                                                                                         | 8.43 us: 1.02x faster                                                                                               |
| async_tree_none_tg         | 279 ms                                                                                                          | 274 ms: 1.02x faster                                                                                                |
| json                       | 6.11 ms                                                                                                         | 6.01 ms: 1.02x faster                                                                                               |
| logging_simple             | 7.52 us                                                                                                         | 7.41 us: 1.02x faster                                                                                               |
| async_tree_memoization     | 350 ms                                                                                                          | 345 ms: 1.01x faster                                                                                                |
| crypto_pyaes               | 87.1 ms                                                                                                         | 85.8 ms: 1.01x faster                                                                                               |
| regex_dna                  | 204 ms                                                                                                          | 201 ms: 1.01x faster                                                                                                |
| html5lib                   | 66.2 ms                                                                                                         | 65.4 ms: 1.01x faster                                                                                               |
| django_template            | 40.3 ms                                                                                                         | 39.9 ms: 1.01x faster                                                                                               |
| gc_traversal               | 5.16 ms                                                                                                         | 5.11 ms: 1.01x faster                                                                                               |
| pickle                     | 15.0 us                                                                                                         | 14.9 us: 1.01x faster                                                                                               |
| json_loads                 | 33.9 us                                                                                                         | 33.6 us: 1.01x faster                                                                                               |
| meteor_contest             | 116 ms                                                                                                          | 115 ms: 1.01x faster                                                                                                |
| create_gc_cycles           | 2.63 ms                                                                                                         | 2.61 ms: 1.01x faster                                                                                               |
| python_startup_no_site     | 7.42 ms                                                                                                         | 7.40 ms: 1.00x faster                                                                                               |
| sqlglot_v2_optimize        | 62.0 ms                                                                                                         | 61.9 ms: 1.00x faster                                                                                               |
| python_startup             | 13.2 ms                                                                                                         | 13.1 ms: 1.00x faster                                                                                               |
| chaos                      | 69.9 ms                                                                                                         | 70.1 ms: 1.00x slower                                                                                               |
| sqlglot_v2_normalize       | 126 ms                                                                                                          | 127 ms: 1.00x slower                                                                                                |
| mdp                        | 1.47 sec                                                                                                        | 1.48 sec: 1.00x slower                                                                                              |
| asyncio_tcp_ssl            | 1.82 sec                                                                                                        | 1.82 sec: 1.00x slower                                                                                              |
| bench_mp_pool              | 104 ms                                                                                                          | 105 ms: 1.01x slower                                                                                                |
| json_dumps                 | 13.3 ms                                                                                                         | 13.4 ms: 1.01x slower                                                                                               |
| scimark_lu                 | 134 ms                                                                                                          | 135 ms: 1.01x slower                                                                                                |
| subparsers                 | 28.0 ms                                                                                                         | 28.2 ms: 1.01x slower                                                                                               |
| bench_thread_pool          | 957 us                                                                                                          | 965 us: 1.01x slower                                                                                                |
| pathlib                    | 18.2 ms                                                                                                         | 18.4 ms: 1.01x slower                                                                                               |
| sympy_sum                  | 166 ms                                                                                                          | 167 ms: 1.01x slower                                                                                                |
| unpickle                   | 18.9 us                                                                                                         | 19.1 us: 1.01x slower                                                                                               |
| raytrace                   | 319 ms                                                                                                          | 322 ms: 1.01x slower                                                                                                |
| genshi_xml                 | 57.5 ms                                                                                                         | 58.2 ms: 1.01x slower                                                                                               |
| genshi_text                | 25.0 ms                                                                                                         | 25.3 ms: 1.01x slower                                                                                               |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                         | 1.78 ms: 1.01x slower                                                                                               |
| asyncio_tcp                | 484 ms                                                                                                          | 491 ms: 1.02x slower                                                                                                |
| deepcopy                   | 310 us                                                                                                          | 315 us: 1.02x slower                                                                                                |
| pidigits                   | 202 ms                                                                                                          | 206 ms: 1.02x slower                                                                                                |
| sympy_str                  | 307 ms                                                                                                          | 314 ms: 1.02x slower                                                                                                |
| generators                 | 32.4 ms                                                                                                         | 33.1 ms: 1.02x slower                                                                                               |
| sqlglot_v2_parse           | 1.40 ms                                                                                                         | 1.43 ms: 1.02x slower                                                                                               |
| deepcopy_memo              | 34.0 us                                                                                                         | 34.8 us: 1.02x slower                                                                                               |
| deepcopy_reduce            | 3.30 us                                                                                                         | 3.38 us: 1.02x slower                                                                                               |
| sympy_integrate            | 20.9 ms                                                                                                         | 21.4 ms: 1.02x slower                                                                                               |
| docutils                   | 2.84 sec                                                                                                        | 2.91 sec: 1.02x slower                                                                                              |
| 2to3                       | 289 ms                                                                                                          | 297 ms: 1.03x slower                                                                                                |
| pickle_list                | 5.85 us                                                                                                         | 6.01 us: 1.03x slower                                                                                               |
| sympy_expand               | 534 ms                                                                                                          | 548 ms: 1.03x slower                                                                                                |
| coverage                   | 514 ms                                                                                                          | 529 ms: 1.03x slower                                                                                                |
| many_optionals             | 1.07 ms                                                                                                         | 1.10 ms: 1.03x slower                                                                                               |
| typing_runtime_protocols   | 195 us                                                                                                          | 201 us: 1.03x slower                                                                                                |
| nqueens                    | 99.3 ms                                                                                                         | 103 ms: 1.03x slower                                                                                                |
| dulwich_log                | 64.0 ms                                                                                                         | 66.1 ms: 1.03x slower                                                                                               |
| regex_v8                   | 24.0 ms                                                                                                         | 24.9 ms: 1.03x slower                                                                                               |
| pickle_dict                | 36.2 us                                                                                                         | 37.8 us: 1.04x slower                                                                                               |
| hexiom                     | 6.66 ms                                                                                                         | 6.94 ms: 1.04x slower                                                                                               |
| unpickle_list              | 5.59 us                                                                                                         | 5.86 us: 1.05x slower                                                                                               |
| async_generators           | 416 ms                                                                                                          | 439 ms: 1.05x slower                                                                                                |
| comprehensions             | 19.1 us                                                                                                         | 20.1 us: 1.06x slower                                                                                               |
| regex_effbot               | 3.00 ms                                                                                                         | 3.20 ms: 1.06x slower                                                                                               |
| go                         | 119 ms                                                                                                          | 130 ms: 1.09x slower                                                                                                |
| unpack_sequence            | 50.5 ns                                                                                                         | 75.6 ns: 1.50x slower                                                                                               |
| Geometric mean             | (ref)                                                                                                           | 1.32x faster                                                                                                        |

Benchmark hidden because not significant (12): async_tree_none, scimark_sparse_mat_mult, xml_etree_iterparse, k_core, asyncio_websockets, thrift, xml_etree_parse, async_tree_io, scimark_sor, pycparser, sphinx, pylint
Ignored benchmarks (1) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: regex_compile

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 90.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x