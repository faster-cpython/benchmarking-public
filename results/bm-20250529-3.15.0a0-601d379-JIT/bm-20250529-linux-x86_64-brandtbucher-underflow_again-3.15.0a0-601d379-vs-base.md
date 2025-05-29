# Results vs. base

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: 601d379
- commit date: 2025-05-29
- overall geometric mean: 1.011x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 261 ms: 1.01x slower                                                   |
| docutils       | 2.63 sec                                                              | 2.70 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 643 ms                                                                | 629 ms: 1.02x faster                                                   |
| async_generators           | 426 ms                                                                | 429 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 247 ms                                                                | 250 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                | 490 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 488 ms                                                                | 498 ms: 1.02x slower                                                   |
| coroutines                 | 25.2 ms                                                               | 25.9 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (5): async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.10 ms                                                               | 3.37 ms: 1.09x slower                                                  |
| regex_v8       | 21.9 ms                                                               | 24.2 ms: 1.11x slower                                                  |
| regex_dna      | 187 ms                                                                | 208 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 81.9 ms                                                               | 79.9 ms: 1.02x faster                                                  |
| xml_etree_process    | 56.8 ms                                                               | 55.6 ms: 1.02x faster                                                  |
| json_dumps           | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 97.5 ms                                                               | 98.4 ms: 1.01x slower                                                  |
| unpickle_pure_python | 199 us                                                                | 202 us: 1.02x slower                                                   |
| json_loads           | 29.9 us                                                               | 30.7 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (3): pickle_pure_python, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                  |
| python_startup_no_site | 6.93 ms                                                               | 6.96 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.7 ms                                                               | 32.4 ms: 1.01x faster                                                  |
| genshi_xml      | 49.7 ms                                                               | 50.2 ms: 1.01x slower                                                  |
| genshi_text     | 21.5 ms                                                               | 21.7 ms: 1.01x slower                                                  |
| mako            | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.98 ms                                                               | 4.82 ms: 1.03x faster                                                  |
| fannkuch                   | 419 ms                                                                | 407 ms: 1.03x faster                                                   |
| xml_etree_generate         | 81.9 ms                                                               | 79.9 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 643 ms                                                                | 629 ms: 1.02x faster                                                   |
| generators                 | 31.0 ms                                                               | 30.3 ms: 1.02x faster                                                  |
| xml_etree_process          | 56.8 ms                                                               | 55.6 ms: 1.02x faster                                                  |
| scimark_fft                | 335 ms                                                                | 328 ms: 1.02x faster                                                   |
| connected_components       | 458 ms                                                                | 451 ms: 1.02x faster                                                   |
| shortest_path              | 496 ms                                                                | 489 ms: 1.02x faster                                                   |
| gc_traversal               | 5.10 ms                                                               | 5.02 ms: 1.02x faster                                                  |
| crypto_pyaes               | 76.3 ms                                                               | 75.5 ms: 1.01x faster                                                  |
| django_template            | 32.7 ms                                                               | 32.4 ms: 1.01x faster                                                  |
| json_dumps                 | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                  |
| scimark_sor                | 120 ms                                                                | 120 ms: 1.01x faster                                                   |
| deepcopy                   | 258 us                                                                | 257 us: 1.00x faster                                                   |
| spectral_norm              | 100 ms                                                                | 99.8 ms: 1.00x faster                                                  |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                  |
| dulwich_log                | 61.5 ms                                                               | 61.6 ms: 1.00x slower                                                  |
| python_startup_no_site     | 6.93 ms                                                               | 6.96 ms: 1.00x slower                                                  |
| mdp                        | 1.24 sec                                                              | 1.25 sec: 1.00x slower                                                 |
| sqlglot_v2_optimize        | 52.6 ms                                                               | 52.8 ms: 1.00x slower                                                  |
| hexiom                     | 6.40 ms                                                               | 6.42 ms: 1.00x slower                                                  |
| comprehensions             | 16.9 us                                                               | 17.0 us: 1.00x slower                                                  |
| bench_thread_pool          | 893 us                                                                | 897 us: 1.00x slower                                                   |
| bpe_tokeniser              | 4.40 sec                                                              | 4.42 sec: 1.01x slower                                                 |
| deltablue                  | 3.06 ms                                                               | 3.08 ms: 1.01x slower                                                  |
| 2to3                       | 260 ms                                                                | 261 ms: 1.01x slower                                                   |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                                  |
| logging_simple             | 6.15 us                                                               | 6.19 us: 1.01x slower                                                  |
| bench_mp_pool              | 92.8 ms                                                               | 93.5 ms: 1.01x slower                                                  |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.59 ms: 1.01x slower                                                  |
| async_generators           | 426 ms                                                                | 429 ms: 1.01x slower                                                   |
| genshi_xml                 | 49.7 ms                                                               | 50.2 ms: 1.01x slower                                                  |
| genshi_text                | 21.5 ms                                                               | 21.7 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 97.5 ms                                                               | 98.4 ms: 1.01x slower                                                  |
| sympy_expand               | 462 ms                                                                | 466 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 247 ms                                                                | 250 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 2.70 us                                                               | 2.73 us: 1.01x slower                                                  |
| json                       | 5.33 ms                                                               | 5.40 ms: 1.01x slower                                                  |
| sqlglot_v2_normalize       | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| scimark_lu                 | 119 ms                                                                | 120 ms: 1.01x slower                                                   |
| meteor_contest             | 104 ms                                                                | 106 ms: 1.01x slower                                                   |
| mako                       | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.28 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 168 us                                                                | 171 us: 1.02x slower                                                   |
| sympy_str                  | 269 ms                                                                | 273 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                | 490 ms: 1.02x slower                                                   |
| sympy_sum                  | 149 ms                                                                | 152 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 199 us                                                                | 202 us: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 488 ms                                                                | 498 ms: 1.02x slower                                                   |
| json_loads                 | 29.9 us                                                               | 30.7 us: 1.02x slower                                                  |
| docutils                   | 2.63 sec                                                              | 2.70 sec: 1.03x slower                                                 |
| deepcopy_memo              | 29.3 us                                                               | 30.1 us: 1.03x slower                                                  |
| pprint_safe_repr           | 835 ns                                                                | 857 ns: 1.03x slower                                                   |
| coverage                   | 421 ms                                                                | 432 ms: 1.03x slower                                                   |
| coroutines                 | 25.2 ms                                                               | 25.9 ms: 1.03x slower                                                  |
| raytrace                   | 270 ms                                                                | 278 ms: 1.03x slower                                                   |
| nqueens                    | 81.8 ms                                                               | 84.3 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.42 us                                                               | 1.47 us: 1.03x slower                                                  |
| telco                      | 7.65 ms                                                               | 7.93 ms: 1.04x slower                                                  |
| chaos                      | 61.3 ms                                                               | 63.9 ms: 1.04x slower                                                  |
| pycparser                  | 1.11 sec                                                              | 1.17 sec: 1.06x slower                                                 |
| scimark_monte_carlo        | 66.4 ms                                                               | 70.3 ms: 1.06x slower                                                  |
| pyflate                    | 409 ms                                                                | 441 ms: 1.08x slower                                                   |
| regex_effbot               | 3.10 ms                                                               | 3.37 ms: 1.09x slower                                                  |
| regex_v8                   | 21.9 ms                                                               | 24.2 ms: 1.11x slower                                                  |
| regex_dna                  | 187 ms                                                                | 208 ms: 1.12x slower                                                   |
| go                         | 121 ms                                                                | 141 ms: 1.16x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (25): pickle_pure_python, many_optionals, tomli_loads, async_tree_memoization_tg, subparsers, logging_format, create_gc_cycles, asyncio_websockets, thrift, pathlib, pidigits, logging_silent, nbody, sqlite_synth, async_tree_memoization, pylint, k_core, xml_etree_parse, richards, float, html5lib, async_tree_io, async_tree_none, richards_super, sphinx
Ignored benchmarks (9) of results/bm-20250528-3.15.0a0-9fbd66a-JIT/bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x