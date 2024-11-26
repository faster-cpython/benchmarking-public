# Results vs. base

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.114x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                              | 389 ms: 1.32x slower                                                                                                    |
| docutils       | 3.01 sec                                                                                                            | 3.70 sec: 1.23x slower                                                                                                  |
| html5lib       | 65.3 ms                                                                                                             | 72.7 ms: 1.11x slower                                                                                                   |
| sphinx         | 1.19 sec                                                                                                            | 1.47 sec: 1.24x slower                                                                                                  |
| tornado_http   | 125 ms                                                                                                              | 148 ms: 1.18x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.22x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.25 sec                                                                                                            | 1.24 sec: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                                              | 755 ms: 1.03x slower                                                                                                    |
| async_tree_memoization     | 578 ms                                                                                                              | 597 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 743 ms                                                                                                              | 769 ms: 1.03x slower                                                                                                    |
| async_tree_io              | 1.13 sec                                                                                                            | 1.18 sec: 1.04x slower                                                                                                  |
| async_tree_none            | 445 ms                                                                                                              | 468 ms: 1.05x slower                                                                                                    |
| async_tree_memoization_tg  | 528 ms                                                                                                              | 565 ms: 1.07x slower                                                                                                    |
| async_tree_none_tg         | 438 ms                                                                                                              | 471 ms: 1.08x slower                                                                                                    |
| async_generators           | 477 ms                                                                                                              | 519 ms: 1.09x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.04x slower                                                                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 117 ms                                                                                                              | 114 ms: 1.03x faster                                                                                                    |
| float          | 95.1 ms                                                                                                             | 96.8 ms: 1.02x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 31.9 ms                                                                                                             | 30.9 ms: 1.03x faster                                                                                                   |
| regex_dna      | 253 ms                                                                                                              | 250 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 4.96 ms                                                                                                             | 5.27 ms: 1.06x slower                                                                                                   |
| regex_compile  | 125 ms                                                                                                              | 175 ms: 1.40x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                                                                              | 112 ms: 1.01x faster                                                                                                    |
| json_loads           | 31.3 us                                                                                                             | 31.5 us: 1.01x slower                                                                                                   |
| tomli_loads          | 2.63 sec                                                                                                            | 2.68 sec: 1.02x slower                                                                                                  |
| xml_etree_iterparse  | 147 ms                                                                                                              | 150 ms: 1.02x slower                                                                                                    |
| unpickle_pure_python | 257 us                                                                                                              | 268 us: 1.04x slower                                                                                                    |
| pickle_pure_python   | 371 us                                                                                                              | 391 us: 1.05x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.67 ms                                                                                                             | 8.79 ms: 1.01x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.6 ms                                                                                                             | 13.2 ms: 1.03x faster                                                                                                   |
| genshi_text     | 27.6 ms                                                                                                             | 34.1 ms: 1.24x slower                                                                                                   |
| django_template | 41.9 ms                                                                                                             | 53.0 ms: 1.27x slower                                                                                                   |
| genshi_xml      | 60.1 ms                                                                                                             | 82.8 ms: 1.38x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.20x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.94 sec                                                                                                            | 1.47 sec: 3.36x faster                                                                                                  |
| scimark_sor                | 160 ms                                                                                                              | 155 ms: 1.03x faster                                                                                                    |
| regex_v8                   | 31.9 ms                                                                                                             | 30.9 ms: 1.03x faster                                                                                                   |
| mako                       | 13.6 ms                                                                                                             | 13.2 ms: 1.03x faster                                                                                                   |
| nbody                      | 117 ms                                                                                                              | 114 ms: 1.03x faster                                                                                                    |
| xml_etree_generate         | 113 ms                                                                                                              | 112 ms: 1.01x faster                                                                                                    |
| async_tree_io_tg           | 1.25 sec                                                                                                            | 1.24 sec: 1.01x faster                                                                                                  |
| regex_dna                  | 253 ms                                                                                                              | 250 ms: 1.01x faster                                                                                                    |
| json_loads                 | 31.3 us                                                                                                             | 31.5 us: 1.01x slower                                                                                                   |
| python_startup_no_site     | 8.67 ms                                                                                                             | 8.79 ms: 1.01x slower                                                                                                   |
| coverage                   | 97.2 ms                                                                                                             | 98.9 ms: 1.02x slower                                                                                                   |
| float                      | 95.1 ms                                                                                                             | 96.8 ms: 1.02x slower                                                                                                   |
| tomli_loads                | 2.63 sec                                                                                                            | 2.68 sec: 1.02x slower                                                                                                  |
| logging_silent             | 132 ns                                                                                                              | 135 ns: 1.02x slower                                                                                                    |
| deepcopy_memo              | 38.4 us                                                                                                             | 39.3 us: 1.02x slower                                                                                                   |
| xml_etree_iterparse        | 147 ms                                                                                                              | 150 ms: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                                              | 755 ms: 1.03x slower                                                                                                    |
| bpe_tokeniser              | 5.79 sec                                                                                                            | 5.97 sec: 1.03x slower                                                                                                  |
| thrift                     | 945 us                                                                                                              | 976 us: 1.03x slower                                                                                                    |
| async_tree_memoization     | 578 ms                                                                                                              | 597 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 743 ms                                                                                                              | 769 ms: 1.03x slower                                                                                                    |
| async_tree_io              | 1.13 sec                                                                                                            | 1.18 sec: 1.04x slower                                                                                                  |
| unpickle_pure_python       | 257 us                                                                                                              | 268 us: 1.04x slower                                                                                                    |
| mdp                        | 3.35 sec                                                                                                            | 3.51 sec: 1.05x slower                                                                                                  |
| json                       | 5.46 ms                                                                                                             | 5.74 ms: 1.05x slower                                                                                                   |
| scimark_fft                | 438 ms                                                                                                              | 461 ms: 1.05x slower                                                                                                    |
| pickle_pure_python         | 371 us                                                                                                              | 391 us: 1.05x slower                                                                                                    |
| async_tree_none            | 445 ms                                                                                                              | 468 ms: 1.05x slower                                                                                                    |
| regex_effbot               | 4.96 ms                                                                                                             | 5.27 ms: 1.06x slower                                                                                                   |
| scimark_monte_carlo        | 83.3 ms                                                                                                             | 88.7 ms: 1.06x slower                                                                                                   |
| async_tree_memoization_tg  | 528 ms                                                                                                              | 565 ms: 1.07x slower                                                                                                    |
| bench_thread_pool          | 1.28 ms                                                                                                             | 1.37 ms: 1.07x slower                                                                                                   |
| async_tree_none_tg         | 438 ms                                                                                                              | 471 ms: 1.08x slower                                                                                                    |
| spectral_norm              | 144 ms                                                                                                              | 155 ms: 1.08x slower                                                                                                    |
| fannkuch                   | 468 ms                                                                                                              | 505 ms: 1.08x slower                                                                                                    |
| logging_format             | 7.62 us                                                                                                             | 8.25 us: 1.08x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.57 ms                                                                                                             | 7.14 ms: 1.09x slower                                                                                                   |
| crypto_pyaes               | 82.7 ms                                                                                                             | 89.9 ms: 1.09x slower                                                                                                   |
| async_generators           | 477 ms                                                                                                              | 519 ms: 1.09x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                              | 124 ms: 1.09x slower                                                                                                    |
| pyflate                    | 585 ms                                                                                                              | 643 ms: 1.10x slower                                                                                                    |
| logging_simple             | 6.91 us                                                                                                             | 7.62 us: 1.10x slower                                                                                                   |
| html5lib                   | 65.3 ms                                                                                                             | 72.7 ms: 1.11x slower                                                                                                   |
| deepcopy_reduce            | 3.54 us                                                                                                             | 3.95 us: 1.11x slower                                                                                                   |
| raytrace                   | 310 ms                                                                                                              | 347 ms: 1.12x slower                                                                                                    |
| typing_runtime_protocols   | 194 us                                                                                                              | 219 us: 1.13x slower                                                                                                    |
| scimark_lu                 | 135 ms                                                                                                              | 152 ms: 1.13x slower                                                                                                    |
| deepcopy                   | 336 us                                                                                                              | 383 us: 1.14x slower                                                                                                    |
| deltablue                  | 3.94 ms                                                                                                             | 4.54 ms: 1.15x slower                                                                                                   |
| richards_super             | 60.0 ms                                                                                                             | 70.5 ms: 1.17x slower                                                                                                   |
| tornado_http               | 125 ms                                                                                                              | 148 ms: 1.18x slower                                                                                                    |
| richards                   | 53.9 ms                                                                                                             | 64.9 ms: 1.20x slower                                                                                                   |
| comprehensions             | 20.8 us                                                                                                             | 25.3 us: 1.22x slower                                                                                                   |
| sqlglot_parse              | 1.41 ms                                                                                                             | 1.72 ms: 1.22x slower                                                                                                   |
| sqlalchemy_imperative      | 15.4 ms                                                                                                             | 18.8 ms: 1.22x slower                                                                                                   |
| chaos                      | 70.3 ms                                                                                                             | 86.1 ms: 1.22x slower                                                                                                   |
| pycparser                  | 1.24 sec                                                                                                            | 1.51 sec: 1.22x slower                                                                                                  |
| docutils                   | 3.01 sec                                                                                                            | 3.70 sec: 1.23x slower                                                                                                  |
| sqlglot_normalize          | 128 ms                                                                                                              | 157 ms: 1.23x slower                                                                                                    |
| genshi_text                | 27.6 ms                                                                                                             | 34.1 ms: 1.24x slower                                                                                                   |
| sphinx                     | 1.19 sec                                                                                                            | 1.47 sec: 1.24x slower                                                                                                  |
| sqlglot_transpile          | 1.74 ms                                                                                                             | 2.19 ms: 1.26x slower                                                                                                   |
| django_template            | 41.9 ms                                                                                                             | 53.0 ms: 1.27x slower                                                                                                   |
| pprint_safe_repr           | 939 ms                                                                                                              | 1.19 sec: 1.27x slower                                                                                                  |
| nqueens                    | 98.9 ms                                                                                                             | 126 ms: 1.28x slower                                                                                                    |
| pprint_pformat             | 1.92 sec                                                                                                            | 2.51 sec: 1.30x slower                                                                                                  |
| sympy_expand               | 459 ms                                                                                                              | 600 ms: 1.31x slower                                                                                                    |
| 2to3                       | 294 ms                                                                                                              | 389 ms: 1.32x slower                                                                                                    |
| sqlglot_optimize           | 62.0 ms                                                                                                             | 83.4 ms: 1.35x slower                                                                                                   |
| go                         | 137 ms                                                                                                              | 185 ms: 1.35x slower                                                                                                    |
| sqlalchemy_declarative     | 140 ms                                                                                                              | 190 ms: 1.35x slower                                                                                                    |
| sympy_str                  | 264 ms                                                                                                              | 362 ms: 1.37x slower                                                                                                    |
| genshi_xml                 | 60.1 ms                                                                                                             | 82.8 ms: 1.38x slower                                                                                                   |
| pylint                     | 352 ms                                                                                                              | 489 ms: 1.39x slower                                                                                                    |
| dulwich_log                | 58.7 ms                                                                                                             | 81.8 ms: 1.39x slower                                                                                                   |
| regex_compile              | 125 ms                                                                                                              | 175 ms: 1.40x slower                                                                                                    |
| sympy_integrate            | 21.2 ms                                                                                                             | 29.9 ms: 1.41x slower                                                                                                   |
| hexiom                     | 7.11 ms                                                                                                             | 10.5 ms: 1.47x slower                                                                                                   |
| sympy_sum                  | 142 ms                                                                                                              | 222 ms: 1.56x slower                                                                                                    |
| generators                 | 34.8 ms                                                                                                             | 58.8 ms: 1.69x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                               | 1.11x slower                                                                                                            |

Benchmark hidden because not significant (11): pidigits, xml_etree_parse, python_startup, pathlib, telco, gc_traversal, asyncio_websockets, json_dumps, xml_etree_process, coroutines, create_gc_cycles

- Geometric mean (including insignificant results): 1.114x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.07x