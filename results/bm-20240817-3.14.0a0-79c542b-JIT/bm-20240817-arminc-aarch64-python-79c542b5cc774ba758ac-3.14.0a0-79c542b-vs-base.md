# Results vs. base

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 302 ms                                                                                                            | 386 ms: 1.28x slower                                                                                                  |
| docutils       | 3.13 sec                                                                                                          | 4.04 sec: 1.29x slower                                                                                                |
| html5lib       | 66.4 ms                                                                                                           | 71.9 ms: 1.08x slower                                                                                                 |
| tornado_http   | 121 ms                                                                                                            | 140 ms: 1.16x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.20x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines              | 28.4 ms                                                                                                           | 29.1 ms: 1.02x slower                                                                                                 |
| asyncio_tcp_ssl         | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_tree_none_tg      | 400 ms                                                                                                            | 412 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed | 726 ms                                                                                                            | 751 ms: 1.03x slower                                                                                                  |
| async_tree_memoization  | 549 ms                                                                                                            | 580 ms: 1.06x slower                                                                                                  |
| async_generators        | 482 ms                                                                                                            | 511 ms: 1.06x slower                                                                                                  |
| asyncio_tcp             | 576 ms                                                                                                            | 614 ms: 1.07x slower                                                                                                  |
| async_tree_io           | 1.08 sec                                                                                                          | 1.15 sec: 1.07x slower                                                                                                |
| Geometric mean          | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 93.1 ms                                                                                                           | 88.3 ms: 1.05x faster                                                                                                 |
| nbody          | 111 ms                                                                                                            | 115 ms: 1.04x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                                                            | 246 ms: 1.03x faster                                                                                                  |
| regex_effbot   | 4.92 ms                                                                                                           | 4.81 ms: 1.02x faster                                                                                                 |
| regex_v8       | 30.7 ms                                                                                                           | 30.2 ms: 1.01x faster                                                                                                 |
| regex_compile  | 126 ms                                                                                                            | 188 ms: 1.48x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.55 sec                                                                                                          | 2.61 sec: 1.02x slower                                                                                                |
| unpickle_pure_python | 252 us                                                                                                            | 268 us: 1.06x slower                                                                                                  |
| pickle_pure_python   | 356 us                                                                                                            | 391 us: 1.10x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (6): json_loads, xml_etree_process, xml_etree_parse, json_dumps, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                                                           | 13.1 ms: 1.02x faster                                                                                                 |
| django_template | 42.9 ms                                                                                                           | 50.8 ms: 1.18x slower                                                                                                 |
| genshi_text     | 27.6 ms                                                                                                           | 34.3 ms: 1.24x slower                                                                                                 |
| genshi_xml      | 60.1 ms                                                                                                           | 82.0 ms: 1.36x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.18x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                    | 93.1 ms                                                                                                           | 88.3 ms: 1.05x faster                                                                                                 |
| regex_dna                | 254 ms                                                                                                            | 246 ms: 1.03x faster                                                                                                  |
| scimark_sor              | 154 ms                                                                                                            | 150 ms: 1.03x faster                                                                                                  |
| regex_effbot             | 4.92 ms                                                                                                           | 4.81 ms: 1.02x faster                                                                                                 |
| deepcopy_memo            | 37.5 us                                                                                                           | 36.8 us: 1.02x faster                                                                                                 |
| mako                     | 13.3 ms                                                                                                           | 13.1 ms: 1.02x faster                                                                                                 |
| regex_v8                 | 30.7 ms                                                                                                           | 30.2 ms: 1.01x faster                                                                                                 |
| telco                    | 10.3 ms                                                                                                           | 10.2 ms: 1.01x faster                                                                                                 |
| create_gc_cycles         | 2.29 ms                                                                                                           | 2.32 ms: 1.01x slower                                                                                                 |
| coroutines               | 28.4 ms                                                                                                           | 29.1 ms: 1.02x slower                                                                                                 |
| tomli_loads              | 2.55 sec                                                                                                          | 2.61 sec: 1.02x slower                                                                                                |
| scimark_fft              | 444 ms                                                                                                            | 454 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl          | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| mdp                      | 3.38 sec                                                                                                          | 3.47 sec: 1.03x slower                                                                                                |
| bpe_tokeniser            | 5.85 sec                                                                                                          | 6.02 sec: 1.03x slower                                                                                                |
| async_tree_none_tg       | 400 ms                                                                                                            | 412 ms: 1.03x slower                                                                                                  |
| logging_silent           | 130 ns                                                                                                            | 134 ns: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed  | 726 ms                                                                                                            | 751 ms: 1.03x slower                                                                                                  |
| thrift                   | 957 us                                                                                                            | 992 us: 1.04x slower                                                                                                  |
| spectral_norm            | 140 ms                                                                                                            | 146 ms: 1.04x slower                                                                                                  |
| pathlib                  | 21.1 ms                                                                                                           | 22.0 ms: 1.04x slower                                                                                                 |
| nbody                    | 111 ms                                                                                                            | 115 ms: 1.04x slower                                                                                                  |
| typing_runtime_protocols | 201 us                                                                                                            | 210 us: 1.05x slower                                                                                                  |
| async_tree_memoization   | 549 ms                                                                                                            | 580 ms: 1.06x slower                                                                                                  |
| bench_thread_pool        | 1.25 ms                                                                                                           | 1.32 ms: 1.06x slower                                                                                                 |
| async_generators         | 482 ms                                                                                                            | 511 ms: 1.06x slower                                                                                                  |
| gc_traversal             | 4.79 ms                                                                                                           | 5.08 ms: 1.06x slower                                                                                                 |
| logging_format           | 7.69 us                                                                                                           | 8.16 us: 1.06x slower                                                                                                 |
| unpickle_pure_python     | 252 us                                                                                                            | 268 us: 1.06x slower                                                                                                  |
| asyncio_tcp              | 576 ms                                                                                                            | 614 ms: 1.07x slower                                                                                                  |
| scimark_sparse_mat_mult  | 6.37 ms                                                                                                           | 6.80 ms: 1.07x slower                                                                                                 |
| async_tree_io            | 1.08 sec                                                                                                          | 1.15 sec: 1.07x slower                                                                                                |
| logging_simple           | 6.93 us                                                                                                           | 7.44 us: 1.07x slower                                                                                                 |
| crypto_pyaes             | 82.0 ms                                                                                                           | 88.2 ms: 1.08x slower                                                                                                 |
| meteor_contest           | 113 ms                                                                                                            | 122 ms: 1.08x slower                                                                                                  |
| bench_mp_pool            | 7.00 ms                                                                                                           | 7.56 ms: 1.08x slower                                                                                                 |
| html5lib                 | 66.4 ms                                                                                                           | 71.9 ms: 1.08x slower                                                                                                 |
| fannkuch                 | 460 ms                                                                                                            | 502 ms: 1.09x slower                                                                                                  |
| pickle_pure_python       | 356 us                                                                                                            | 391 us: 1.10x slower                                                                                                  |
| scimark_lu               | 134 ms                                                                                                            | 147 ms: 1.10x slower                                                                                                  |
| scimark_monte_carlo      | 81.8 ms                                                                                                           | 90.8 ms: 1.11x slower                                                                                                 |
| pyflate                  | 577 ms                                                                                                            | 643 ms: 1.11x slower                                                                                                  |
| raytrace                 | 294 ms                                                                                                            | 328 ms: 1.12x slower                                                                                                  |
| deltablue                | 3.77 ms                                                                                                           | 4.24 ms: 1.12x slower                                                                                                 |
| deepcopy_reduce          | 3.40 us                                                                                                           | 3.81 us: 1.12x slower                                                                                                 |
| tornado_http             | 121 ms                                                                                                            | 140 ms: 1.16x slower                                                                                                  |
| go                       | 159 ms                                                                                                            | 186 ms: 1.17x slower                                                                                                  |
| sqlglot_parse            | 1.43 ms                                                                                                           | 1.69 ms: 1.18x slower                                                                                                 |
| comprehensions           | 20.5 us                                                                                                           | 24.2 us: 1.18x slower                                                                                                 |
| sqlglot_normalize        | 127 ms                                                                                                            | 150 ms: 1.18x slower                                                                                                  |
| django_template          | 42.9 ms                                                                                                           | 50.8 ms: 1.18x slower                                                                                                 |
| deepcopy                 | 330 us                                                                                                            | 397 us: 1.20x slower                                                                                                  |
| pycparser                | 1.22 sec                                                                                                          | 1.49 sec: 1.22x slower                                                                                                |
| genshi_text              | 27.6 ms                                                                                                           | 34.3 ms: 1.24x slower                                                                                                 |
| nqueens                  | 98.8 ms                                                                                                           | 123 ms: 1.24x slower                                                                                                  |
| sqlglot_optimize         | 61.8 ms                                                                                                           | 78.4 ms: 1.27x slower                                                                                                 |
| 2to3                     | 302 ms                                                                                                            | 386 ms: 1.28x slower                                                                                                  |
| richards_super           | 58.4 ms                                                                                                           | 75.0 ms: 1.28x slower                                                                                                 |
| sqlglot_transpile        | 1.73 ms                                                                                                           | 2.22 ms: 1.28x slower                                                                                                 |
| docutils                 | 3.13 sec                                                                                                          | 4.04 sec: 1.29x slower                                                                                                |
| sympy_expand             | 464 ms                                                                                                            | 604 ms: 1.30x slower                                                                                                  |
| chaos                    | 67.7 ms                                                                                                           | 88.9 ms: 1.31x slower                                                                                                 |
| richards                 | 51.9 ms                                                                                                           | 68.4 ms: 1.32x slower                                                                                                 |
| pylint                   | 359 ms                                                                                                            | 477 ms: 1.33x slower                                                                                                  |
| genshi_xml               | 60.1 ms                                                                                                           | 82.0 ms: 1.36x slower                                                                                                 |
| sympy_integrate          | 21.1 ms                                                                                                           | 28.9 ms: 1.37x slower                                                                                                 |
| sympy_str                | 268 ms                                                                                                            | 370 ms: 1.38x slower                                                                                                  |
| pprint_safe_repr         | 942 ms                                                                                                            | 1.35 sec: 1.43x slower                                                                                                |
| hexiom                   | 6.98 ms                                                                                                           | 10.0 ms: 1.43x slower                                                                                                 |
| pprint_pformat           | 1.92 sec                                                                                                          | 2.79 sec: 1.45x slower                                                                                                |
| regex_compile            | 126 ms                                                                                                            | 188 ms: 1.48x slower                                                                                                  |
| sympy_sum                | 145 ms                                                                                                            | 218 ms: 1.50x slower                                                                                                  |
| generators               | 34.4 ms                                                                                                           | 57.2 ms: 1.66x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                             | 1.11x slower                                                                                                          |

Benchmark hidden because not significant (16): async_tree_io_tg, json_loads, async_tree_none, xml_etree_process, xml_etree_parse, json, async_tree_cpu_io_mixed_tg, asyncio_websockets, python_startup, json_dumps, pidigits, python_startup_no_site, coverage, xml_etree_generate, async_tree_memoization_tg, xml_etree_iterparse

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x