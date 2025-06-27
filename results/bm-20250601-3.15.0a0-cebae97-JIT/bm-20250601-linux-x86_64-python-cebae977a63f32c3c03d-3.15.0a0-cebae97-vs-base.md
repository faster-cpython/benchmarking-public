# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.374x faster
- HPT reliability: 81.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                                                          | 260 ms: 1.02x slower                                                                                                |
| docutils       | 2.57 sec                                                                                                        | 2.64 sec: 1.03x slower                                                                                              |
| sphinx         | 996 ms                                                                                                          | 1.02 sec: 1.02x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 253 ms                                                                                                          | 248 ms: 1.02x faster                                                                                                |
| async_tree_memoization_tg  | 317 ms                                                                                                          | 311 ms: 1.02x faster                                                                                                |
| async_tree_cpu_io_mixed    | 495 ms                                                                                                          | 490 ms: 1.01x faster                                                                                                |
| async_tree_memoization     | 313 ms                                                                                                          | 311 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                                                          | 483 ms: 1.01x faster                                                                                                |
| coroutines                 | 25.1 ms                                                                                                         | 25.6 ms: 1.02x slower                                                                                               |
| async_generators           | 412 ms                                                                                                          | 428 ms: 1.04x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (4): async_tree_none, asyncio_websockets, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 71.5 ms                                                                                                         | 63.7 ms: 1.12x faster                                                                                               |
| nbody          | 103 ms                                                                                                          | 93.1 ms: 1.10x faster                                                                                               |
| pidigits       | 188 ms                                                                                                          | 187 ms: 1.01x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.08x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 22.1 ms                                                                                                         | 23.1 ms: 1.04x slower                                                                                               |
| regex_effbot   | 3.07 ms                                                                                                         | 3.29 ms: 1.07x slower                                                                                               |
| regex_dna      | 182 ms                                                                                                          | 197 ms: 1.08x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                                                          | 199 us: 1.09x faster                                                                                                |
| tomli_loads          | 2.04 sec                                                                                                        | 1.89 sec: 1.08x faster                                                                                              |
| xml_etree_process    | 60.0 ms                                                                                                         | 56.3 ms: 1.07x faster                                                                                               |
| xml_etree_generate   | 85.1 ms                                                                                                         | 80.5 ms: 1.06x faster                                                                                               |
| xml_etree_iterparse  | 98.5 ms                                                                                                         | 97.1 ms: 1.01x faster                                                                                               |
| xml_etree_parse      | 141 ms                                                                                                          | 139 ms: 1.01x faster                                                                                                |
| json_dumps           | 11.3 ms                                                                                                         | 11.2 ms: 1.01x faster                                                                                               |
| json_loads           | 28.0 us                                                                                                         | 28.3 us: 1.01x slower                                                                                               |
| pickle_pure_python   | 318 us                                                                                                          | 323 us: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.1 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 6.90 ms                                                                                                         | 6.94 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.5 ms                                                                                                         | 10.7 ms: 1.08x faster                                                                                               |
| django_template | 32.6 ms                                                                                                         | 32.3 ms: 1.01x faster                                                                                               |
| genshi_xml      | 48.9 ms                                                                                                         | 50.0 ms: 1.02x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 1.60 sec                                                                                                        | 1.45 us: 1103648.79x faster                                                                                         |
| pprint_safe_repr           | 785 ms                                                                                                          | 837 ns: 937654.05x faster                                                                                           |
| richards                   | 43.0 ms                                                                                                         | 33.5 ms: 1.28x faster                                                                                               |
| richards_super             | 48.9 ms                                                                                                         | 39.2 ms: 1.25x faster                                                                                               |
| scimark_fft                | 379 ms                                                                                                          | 330 ms: 1.15x faster                                                                                                |
| float                      | 71.5 ms                                                                                                         | 63.7 ms: 1.12x faster                                                                                               |
| deltablue                  | 3.47 ms                                                                                                         | 3.09 ms: 1.12x faster                                                                                               |
| nbody                      | 103 ms                                                                                                          | 93.1 ms: 1.10x faster                                                                                               |
| unpickle_pure_python       | 216 us                                                                                                          | 199 us: 1.09x faster                                                                                                |
| spectral_norm              | 109 ms                                                                                                          | 101 ms: 1.08x faster                                                                                                |
| tomli_loads                | 2.04 sec                                                                                                        | 1.89 sec: 1.08x faster                                                                                              |
| pyflate                    | 443 ms                                                                                                          | 412 ms: 1.08x faster                                                                                                |
| mako                       | 11.5 ms                                                                                                         | 10.7 ms: 1.08x faster                                                                                               |
| xml_etree_process          | 60.0 ms                                                                                                         | 56.3 ms: 1.07x faster                                                                                               |
| xml_etree_generate         | 85.1 ms                                                                                                         | 80.5 ms: 1.06x faster                                                                                               |
| connected_components       | 472 ms                                                                                                          | 450 ms: 1.05x faster                                                                                                |
| shortest_path              | 509 ms                                                                                                          | 489 ms: 1.04x faster                                                                                                |
| bpe_tokeniser              | 4.50 sec                                                                                                        | 4.39 sec: 1.03x faster                                                                                              |
| coverage                   | 89.2 ms                                                                                                         | 87.0 ms: 1.02x faster                                                                                               |
| scimark_sparse_mat_mult    | 5.01 ms                                                                                                         | 4.90 ms: 1.02x faster                                                                                               |
| telco                      | 7.89 ms                                                                                                         | 7.72 ms: 1.02x faster                                                                                               |
| async_tree_none_tg         | 253 ms                                                                                                          | 248 ms: 1.02x faster                                                                                                |
| pathlib                    | 17.3 ms                                                                                                         | 17.0 ms: 1.02x faster                                                                                               |
| async_tree_memoization_tg  | 317 ms                                                                                                          | 311 ms: 1.02x faster                                                                                                |
| sqlite_synth               | 2.86 us                                                                                                         | 2.81 us: 1.01x faster                                                                                               |
| scimark_monte_carlo        | 68.1 ms                                                                                                         | 67.2 ms: 1.01x faster                                                                                               |
| xml_etree_iterparse        | 98.5 ms                                                                                                         | 97.1 ms: 1.01x faster                                                                                               |
| xml_etree_parse            | 141 ms                                                                                                          | 139 ms: 1.01x faster                                                                                                |
| json_dumps                 | 11.3 ms                                                                                                         | 11.2 ms: 1.01x faster                                                                                               |
| fannkuch                   | 413 ms                                                                                                          | 409 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed    | 495 ms                                                                                                          | 490 ms: 1.01x faster                                                                                                |
| django_template            | 32.6 ms                                                                                                         | 32.3 ms: 1.01x faster                                                                                               |
| async_tree_memoization     | 313 ms                                                                                                          | 311 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                                                          | 483 ms: 1.01x faster                                                                                                |
| logging_silent             | 475 ns                                                                                                          | 472 ns: 1.01x faster                                                                                                |
| pidigits                   | 188 ms                                                                                                          | 187 ms: 1.01x faster                                                                                                |
| gc_traversal               | 5.06 ms                                                                                                         | 5.08 ms: 1.00x slower                                                                                               |
| python_startup             | 12.1 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site     | 6.90 ms                                                                                                         | 6.94 ms: 1.01x slower                                                                                               |
| sympy_sum                  | 148 ms                                                                                                          | 149 ms: 1.01x slower                                                                                                |
| deepcopy                   | 254 us                                                                                                          | 255 us: 1.01x slower                                                                                                |
| sqlglot_v2_optimize        | 52.0 ms                                                                                                         | 52.3 ms: 1.01x slower                                                                                               |
| subparsers                 | 23.2 ms                                                                                                         | 23.4 ms: 1.01x slower                                                                                               |
| json                       | 5.18 ms                                                                                                         | 5.22 ms: 1.01x slower                                                                                               |
| sqlglot_v2_parse           | 1.25 ms                                                                                                         | 1.26 ms: 1.01x slower                                                                                               |
| scimark_lu                 | 117 ms                                                                                                          | 118 ms: 1.01x slower                                                                                                |
| json_loads                 | 28.0 us                                                                                                         | 28.3 us: 1.01x slower                                                                                               |
| deepcopy_memo              | 29.3 us                                                                                                         | 29.6 us: 1.01x slower                                                                                               |
| create_gc_cycles           | 2.56 ms                                                                                                         | 2.59 ms: 1.01x slower                                                                                               |
| mdp                        | 1.23 sec                                                                                                        | 1.24 sec: 1.01x slower                                                                                              |
| nqueens                    | 81.7 ms                                                                                                         | 82.7 ms: 1.01x slower                                                                                               |
| sqlglot_v2_transpile       | 1.56 ms                                                                                                         | 1.58 ms: 1.01x slower                                                                                               |
| dulwich_log                | 58.9 ms                                                                                                         | 59.7 ms: 1.01x slower                                                                                               |
| sympy_str                  | 266 ms                                                                                                          | 270 ms: 1.01x slower                                                                                                |
| pickle_pure_python         | 318 us                                                                                                          | 323 us: 1.01x slower                                                                                                |
| typing_runtime_protocols   | 167 us                                                                                                          | 169 us: 1.01x slower                                                                                                |
| meteor_contest             | 105 ms                                                                                                          | 106 ms: 1.02x slower                                                                                                |
| djangocms                  | 21.7 us                                                                                                         | 22.1 us: 1.02x slower                                                                                               |
| sphinx                     | 996 ms                                                                                                          | 1.02 sec: 1.02x slower                                                                                              |
| coroutines                 | 25.1 ms                                                                                                         | 25.6 ms: 1.02x slower                                                                                               |
| genshi_xml                 | 48.9 ms                                                                                                         | 50.0 ms: 1.02x slower                                                                                               |
| sympy_expand               | 453 ms                                                                                                          | 463 ms: 1.02x slower                                                                                                |
| generators                 | 29.9 ms                                                                                                         | 30.6 ms: 1.02x slower                                                                                               |
| sympy_integrate            | 19.0 ms                                                                                                         | 19.4 ms: 1.02x slower                                                                                               |
| many_optionals             | 958 us                                                                                                          | 981 us: 1.02x slower                                                                                                |
| 2to3                       | 254 ms                                                                                                          | 260 ms: 1.02x slower                                                                                                |
| chaos                      | 60.4 ms                                                                                                         | 62.1 ms: 1.03x slower                                                                                               |
| docutils                   | 2.57 sec                                                                                                        | 2.64 sec: 1.03x slower                                                                                              |
| raytrace                   | 270 ms                                                                                                          | 277 ms: 1.03x slower                                                                                                |
| deepcopy_reduce            | 2.63 us                                                                                                         | 2.71 us: 1.03x slower                                                                                               |
| scimark_sor                | 118 ms                                                                                                          | 121 ms: 1.03x slower                                                                                                |
| async_generators           | 412 ms                                                                                                          | 428 ms: 1.04x slower                                                                                                |
| comprehensions             | 16.4 us                                                                                                         | 17.0 us: 1.04x slower                                                                                               |
| regex_v8                   | 22.1 ms                                                                                                         | 23.1 ms: 1.04x slower                                                                                               |
| hexiom                     | 6.07 ms                                                                                                         | 6.45 ms: 1.06x slower                                                                                               |
| regex_effbot               | 3.07 ms                                                                                                         | 3.29 ms: 1.07x slower                                                                                               |
| regex_dna                  | 182 ms                                                                                                          | 197 ms: 1.08x slower                                                                                                |
| go                         | 111 ms                                                                                                          | 123 ms: 1.11x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.36x faster                                                                                                        |

Benchmark hidden because not significant (14): async_tree_none, thrift, asyncio_websockets, genshi_text, crypto_pyaes, logging_simple, logging_format, async_tree_io_tg, async_tree_io, sqlglot_v2_normalize, html5lib, k_core, pycparser, pylint
Ignored benchmarks (1) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: regex_compile

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 81.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x