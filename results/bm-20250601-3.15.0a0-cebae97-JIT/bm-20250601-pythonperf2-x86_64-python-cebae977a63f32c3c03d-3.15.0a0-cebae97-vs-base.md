# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.347x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 311 ms                                                                                                                | 320 ms: 1.03x slower                                                                                                      |
| docutils       | 3.12 sec                                                                                                              | 3.17 sec: 1.02x slower                                                                                                    |
| html5lib       | 71.6 ms                                                                                                               | 70.9 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.62 sec                                                                                                              | 1.59 sec: 1.02x faster                                                                                                    |
| coroutines                 | 24.4 ms                                                                                                               | 23.9 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 689 ms                                                                                                                | 696 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 385 ms                                                                                                                | 389 ms: 1.01x slower                                                                                                      |
| async_tree_none_tg         | 297 ms                                                                                                                | 301 ms: 1.01x slower                                                                                                      |
| async_tree_memoization     | 358 ms                                                                                                                | 365 ms: 1.02x slower                                                                                                      |
| async_tree_none            | 307 ms                                                                                                                | 314 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 662 ms                                                                                                                | 680 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                                | 677 ms: 1.03x slower                                                                                                      |
| async_generators           | 444 ms                                                                                                                | 468 ms: 1.05x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 80.6 ms                                                                                                               | 72.7 ms: 1.11x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 254 ms: 1.00x slower                                                                                                      |
| nbody          | 101 ms                                                                                                                | 107 ms: 1.06x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.36 ms                                                                                                               | 3.32 ms: 1.01x faster                                                                                                     |
| regex_v8       | 27.5 ms                                                                                                               | 27.3 ms: 1.00x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|---------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process   | 72.6 ms                                                                                                               | 70.1 ms: 1.04x faster                                                                                                     |
| pickle_dict         | 36.4 us                                                                                                               | 35.3 us: 1.03x faster                                                                                                     |
| tomli_loads         | 2.38 sec                                                                                                              | 2.31 sec: 1.03x faster                                                                                                    |
| xml_etree_parse     | 168 ms                                                                                                                | 164 ms: 1.02x faster                                                                                                      |
| xml_etree_generate  | 107 ms                                                                                                                | 104 ms: 1.02x faster                                                                                                      |
| json_dumps          | 14.4 ms                                                                                                               | 14.2 ms: 1.02x faster                                                                                                     |
| xml_etree_iterparse | 117 ms                                                                                                                | 115 ms: 1.02x faster                                                                                                      |
| pickle_pure_python  | 378 us                                                                                                                | 380 us: 1.00x slower                                                                                                      |
| pickle_list         | 5.92 us                                                                                                               | 5.97 us: 1.01x slower                                                                                                     |
| unpickle            | 17.6 us                                                                                                               | 17.7 us: 1.01x slower                                                                                                     |
| json_loads          | 29.1 us                                                                                                               | 29.4 us: 1.01x slower                                                                                                     |
| unpickle_list       | 5.47 us                                                                                                               | 5.59 us: 1.02x slower                                                                                                     |
| Geometric mean      | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (2): pickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.40 ms                                                                                                               | 9.44 ms: 1.00x slower                                                                                                     |
| python_startup         | 16.4 ms                                                                                                               | 16.5 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.7 ms                                                                                                               | 13.5 ms: 1.02x faster                                                                                                     |
| django_template | 42.2 ms                                                                                                               | 42.4 ms: 1.01x slower                                                                                                     |
| genshi_xml      | 60.5 ms                                                                                                               | 63.0 ms: 1.04x slower                                                                                                     |
| genshi_text     | 27.7 ms                                                                                                               | 29.2 ms: 1.05x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 2.11 sec                                                                                                              | 1.83 us: 1154688.44x faster                                                                                               |
| pprint_safe_repr           | 1.03 sec                                                                                                              | 1.12 us: 923660.57x faster                                                                                                |
| richards                   | 53.9 ms                                                                                                               | 40.6 ms: 1.33x faster                                                                                                     |
| richards_super             | 60.8 ms                                                                                                               | 47.9 ms: 1.27x faster                                                                                                     |
| float                      | 80.6 ms                                                                                                               | 72.7 ms: 1.11x faster                                                                                                     |
| deltablue                  | 3.46 ms                                                                                                               | 3.20 ms: 1.08x faster                                                                                                     |
| k_core                     | 2.20 sec                                                                                                              | 2.11 sec: 1.04x faster                                                                                                    |
| xml_etree_process          | 72.6 ms                                                                                                               | 70.1 ms: 1.04x faster                                                                                                     |
| connected_components       | 433 ms                                                                                                                | 419 ms: 1.03x faster                                                                                                      |
| pickle_dict                | 36.4 us                                                                                                               | 35.3 us: 1.03x faster                                                                                                     |
| tomli_loads                | 2.38 sec                                                                                                              | 2.31 sec: 1.03x faster                                                                                                    |
| scimark_sparse_mat_mult    | 6.46 ms                                                                                                               | 6.30 ms: 1.02x faster                                                                                                     |
| xml_etree_parse            | 168 ms                                                                                                                | 164 ms: 1.02x faster                                                                                                      |
| xml_etree_generate         | 107 ms                                                                                                                | 104 ms: 1.02x faster                                                                                                      |
| scimark_lu                 | 123 ms                                                                                                                | 121 ms: 1.02x faster                                                                                                      |
| asyncio_tcp_ssl            | 1.62 sec                                                                                                              | 1.59 sec: 1.02x faster                                                                                                    |
| coroutines                 | 24.4 ms                                                                                                               | 23.9 ms: 1.02x faster                                                                                                     |
| shortest_path              | 460 ms                                                                                                                | 452 ms: 1.02x faster                                                                                                      |
| coverage                   | 98.2 ms                                                                                                               | 96.4 ms: 1.02x faster                                                                                                     |
| json_dumps                 | 14.4 ms                                                                                                               | 14.2 ms: 1.02x faster                                                                                                     |
| xml_etree_iterparse        | 117 ms                                                                                                                | 115 ms: 1.02x faster                                                                                                      |
| mako                       | 13.7 ms                                                                                                               | 13.5 ms: 1.02x faster                                                                                                     |
| pyflate                    | 469 ms                                                                                                                | 462 ms: 1.01x faster                                                                                                      |
| regex_effbot               | 3.36 ms                                                                                                               | 3.32 ms: 1.01x faster                                                                                                     |
| logging_silent             | 676 ns                                                                                                                | 668 ns: 1.01x faster                                                                                                      |
| sqlite_synth               | 3.40 us                                                                                                               | 3.36 us: 1.01x faster                                                                                                     |
| html5lib                   | 71.6 ms                                                                                                               | 70.9 ms: 1.01x faster                                                                                                     |
| scimark_sor                | 124 ms                                                                                                                | 123 ms: 1.01x faster                                                                                                      |
| deepcopy_memo              | 32.2 us                                                                                                               | 32.0 us: 1.01x faster                                                                                                     |
| regex_v8                   | 27.5 ms                                                                                                               | 27.3 ms: 1.00x faster                                                                                                     |
| pidigits                   | 253 ms                                                                                                                | 254 ms: 1.00x slower                                                                                                      |
| scimark_monte_carlo        | 76.1 ms                                                                                                               | 76.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site     | 9.40 ms                                                                                                               | 9.44 ms: 1.00x slower                                                                                                     |
| python_startup             | 16.4 ms                                                                                                               | 16.5 ms: 1.00x slower                                                                                                     |
| bpe_tokeniser              | 5.65 sec                                                                                                              | 5.68 sec: 1.00x slower                                                                                                    |
| pickle_pure_python         | 378 us                                                                                                                | 380 us: 1.00x slower                                                                                                      |
| sqlglot_v2_normalize       | 135 ms                                                                                                                | 136 ms: 1.00x slower                                                                                                      |
| deepcopy_reduce            | 3.52 us                                                                                                               | 3.54 us: 1.01x slower                                                                                                     |
| django_template            | 42.2 ms                                                                                                               | 42.4 ms: 1.01x slower                                                                                                     |
| djangocms                  | 65.8 us                                                                                                               | 66.3 us: 1.01x slower                                                                                                     |
| pickle_list                | 5.92 us                                                                                                               | 5.97 us: 1.01x slower                                                                                                     |
| gc_traversal               | 5.65 ms                                                                                                               | 5.70 ms: 1.01x slower                                                                                                     |
| unpickle                   | 17.6 us                                                                                                               | 17.7 us: 1.01x slower                                                                                                     |
| json                       | 5.93 ms                                                                                                               | 5.98 ms: 1.01x slower                                                                                                     |
| async_tree_io              | 689 ms                                                                                                                | 696 ms: 1.01x slower                                                                                                      |
| json_loads                 | 29.1 us                                                                                                               | 29.4 us: 1.01x slower                                                                                                     |
| asyncio_websockets         | 385 ms                                                                                                                | 389 ms: 1.01x slower                                                                                                      |
| many_optionals             | 1.14 ms                                                                                                               | 1.15 ms: 1.01x slower                                                                                                     |
| deepcopy                   | 317 us                                                                                                                | 320 us: 1.01x slower                                                                                                      |
| mdp                        | 1.55 sec                                                                                                              | 1.57 sec: 1.01x slower                                                                                                    |
| pathlib                    | 19.5 ms                                                                                                               | 19.8 ms: 1.01x slower                                                                                                     |
| async_tree_none_tg         | 297 ms                                                                                                                | 301 ms: 1.01x slower                                                                                                      |
| dulwich_log                | 63.1 ms                                                                                                               | 64.0 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_optimize        | 66.6 ms                                                                                                               | 67.6 ms: 1.01x slower                                                                                                     |
| bench_thread_pool          | 1.04 ms                                                                                                               | 1.05 ms: 1.02x slower                                                                                                     |
| subparsers                 | 28.2 ms                                                                                                               | 28.6 ms: 1.02x slower                                                                                                     |
| docutils                   | 3.12 sec                                                                                                              | 3.17 sec: 1.02x slower                                                                                                    |
| sympy_sum                  | 169 ms                                                                                                                | 172 ms: 1.02x slower                                                                                                      |
| sympy_str                  | 330 ms                                                                                                                | 336 ms: 1.02x slower                                                                                                      |
| async_tree_memoization     | 358 ms                                                                                                                | 365 ms: 1.02x slower                                                                                                      |
| async_tree_none            | 307 ms                                                                                                                | 314 ms: 1.02x slower                                                                                                      |
| thrift                     | 1.01 ms                                                                                                               | 1.04 ms: 1.02x slower                                                                                                     |
| unpickle_list              | 5.47 us                                                                                                               | 5.59 us: 1.02x slower                                                                                                     |
| logging_simple             | 7.55 us                                                                                                               | 7.73 us: 1.02x slower                                                                                                     |
| sympy_integrate            | 23.8 ms                                                                                                               | 24.3 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_parse           | 1.50 ms                                                                                                               | 1.53 ms: 1.02x slower                                                                                                     |
| raytrace                   | 331 ms                                                                                                                | 339 ms: 1.03x slower                                                                                                      |
| sympy_expand               | 571 ms                                                                                                                | 586 ms: 1.03x slower                                                                                                      |
| nqueens                    | 108 ms                                                                                                                | 111 ms: 1.03x slower                                                                                                      |
| chaos                      | 71.5 ms                                                                                                               | 73.4 ms: 1.03x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 662 ms                                                                                                                | 680 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_transpile       | 1.91 ms                                                                                                               | 1.97 ms: 1.03x slower                                                                                                     |
| typing_runtime_protocols   | 210 us                                                                                                                | 216 us: 1.03x slower                                                                                                      |
| 2to3                       | 311 ms                                                                                                                | 320 ms: 1.03x slower                                                                                                      |
| logging_format             | 8.33 us                                                                                                               | 8.59 us: 1.03x slower                                                                                                     |
| spectral_norm              | 114 ms                                                                                                                | 118 ms: 1.03x slower                                                                                                      |
| fannkuch                   | 463 ms                                                                                                                | 479 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 655 ms                                                                                                                | 677 ms: 1.03x slower                                                                                                      |
| scimark_fft                | 383 ms                                                                                                                | 397 ms: 1.04x slower                                                                                                      |
| genshi_xml                 | 60.5 ms                                                                                                               | 63.0 ms: 1.04x slower                                                                                                     |
| generators                 | 31.7 ms                                                                                                               | 33.0 ms: 1.04x slower                                                                                                     |
| meteor_contest             | 139 ms                                                                                                                | 146 ms: 1.05x slower                                                                                                      |
| async_generators           | 444 ms                                                                                                                | 468 ms: 1.05x slower                                                                                                      |
| genshi_text                | 27.7 ms                                                                                                               | 29.2 ms: 1.05x slower                                                                                                     |
| nbody                      | 101 ms                                                                                                                | 107 ms: 1.06x slower                                                                                                      |
| hexiom                     | 6.50 ms                                                                                                               | 6.93 ms: 1.07x slower                                                                                                     |
| crypto_pyaes               | 87.9 ms                                                                                                               | 93.9 ms: 1.07x slower                                                                                                     |
| go                         | 127 ms                                                                                                                | 141 ms: 1.11x slower                                                                                                      |
| comprehensions             | 18.6 us                                                                                                               | 21.1 us: 1.14x slower                                                                                                     |
| unpack_sequence            | 55.5 ns                                                                                                               | 63.1 ns: 1.14x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                 | 1.30x faster                                                                                                              |

Benchmark hidden because not significant (12): asyncio_tcp, pickle, regex_dna, unpickle_pure_python, pycparser, create_gc_cycles, telco, async_tree_io_tg, sphinx, async_tree_memoization_tg, pylint, bench_mp_pool
Ignored benchmarks (1) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: regex_compile

- Geometric mean (including insignificant results): 1.347x faster

# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x