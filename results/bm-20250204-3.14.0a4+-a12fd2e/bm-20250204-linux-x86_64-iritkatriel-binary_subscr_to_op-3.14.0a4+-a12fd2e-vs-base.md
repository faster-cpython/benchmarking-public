# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: a12fd2e
- commit date: 2025-02-04
- overall geometric mean: 1.000x slower
- HPT reliability: 78.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.00x faster                                                       |
| docutils       | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 60.5 ms                                                                | 59.7 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 478 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 488 ms: 1.02x faster                                                       |
| async_generators           | 388 ms                                                                 | 381 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                      |
| async_tree_memoization_tg  | 318 ms                                                                 | 314 ms: 1.01x faster                                                       |
| async_tree_memoization     | 322 ms                                                                 | 324 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.29 ms                                                                | 3.14 ms: 1.05x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                      |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.00x slower                                                       |
| regex_dna      | 204 ms                                                                 | 208 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.2 ms                                                                | 96.3 ms: 1.01x faster                                                      |
| json_dumps           | 11.7 ms                                                                | 11.7 ms: 1.00x faster                                                      |
| pickle_pure_python   | 318 us                                                                 | 317 us: 1.00x faster                                                       |
| unpickle_pure_python | 216 us                                                                 | 216 us: 1.00x slower                                                       |
| json_loads           | 28.6 us                                                                | 28.9 us: 1.01x slower                                                      |
| xml_etree_generate   | 83.1 ms                                                                | 84.0 ms: 1.01x slower                                                      |
| xml_etree_process    | 58.2 ms                                                                | 59.1 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 48.7 ms                                                                | 48.2 ms: 1.01x faster                                                      |
| genshi_text     | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                      |
| mako            | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                      |
| django_template | 31.5 ms                                                                | 31.8 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot               | 3.29 ms                                                                | 3.14 ms: 1.05x faster                                                      |
| pycparser                  | 1.17 sec                                                               | 1.13 sec: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 478 ms: 1.02x faster                                                       |
| regex_v8                   | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 488 ms: 1.02x faster                                                       |
| scimark_fft                | 346 ms                                                                 | 339 ms: 1.02x faster                                                       |
| async_generators           | 388 ms                                                                 | 381 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                      |
| gc_traversal               | 5.02 ms                                                                | 4.95 ms: 1.02x faster                                                      |
| html5lib                   | 60.5 ms                                                                | 59.7 ms: 1.01x faster                                                      |
| generators                 | 28.0 ms                                                                | 27.6 ms: 1.01x faster                                                      |
| async_tree_memoization_tg  | 318 ms                                                                 | 314 ms: 1.01x faster                                                       |
| json                       | 5.19 ms                                                                | 5.13 ms: 1.01x faster                                                      |
| crypto_pyaes               | 70.9 ms                                                                | 70.2 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                                | 66.8 ms: 1.01x faster                                                      |
| genshi_xml                 | 48.7 ms                                                                | 48.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 97.2 ms                                                                | 96.3 ms: 1.01x faster                                                      |
| sqlite_synth               | 2.78 us                                                                | 2.75 us: 1.01x faster                                                      |
| genshi_text                | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                      |
| bpe_tokeniser              | 4.42 sec                                                               | 4.39 sec: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.01x faster                                                       |
| scimark_lu                 | 116 ms                                                                 | 115 ms: 1.01x faster                                                       |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                      |
| mdp                        | 2.46 sec                                                               | 2.45 sec: 1.00x faster                                                     |
| 2to3                       | 251 ms                                                                 | 250 ms: 1.00x faster                                                       |
| json_dumps                 | 11.7 ms                                                                | 11.7 ms: 1.00x faster                                                      |
| pickle_pure_python         | 318 us                                                                 | 317 us: 1.00x faster                                                       |
| docutils                   | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| bench_thread_pool          | 855 us                                                                 | 857 us: 1.00x slower                                                       |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| unpickle_pure_python       | 216 us                                                                 | 216 us: 1.00x slower                                                       |
| regex_compile              | 125 ms                                                                 | 126 ms: 1.00x slower                                                       |
| many_optionals             | 926 us                                                                 | 929 us: 1.00x slower                                                       |
| sqlglot_optimize           | 51.7 ms                                                                | 51.9 ms: 1.00x slower                                                      |
| sympy_integrate            | 19.5 ms                                                                | 19.6 ms: 1.00x slower                                                      |
| chaos                      | 58.1 ms                                                                | 58.4 ms: 1.01x slower                                                      |
| async_tree_memoization     | 322 ms                                                                 | 324 ms: 1.01x slower                                                       |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                       |
| sympy_expand               | 447 ms                                                                 | 450 ms: 1.01x slower                                                       |
| richards_super             | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                      |
| nqueens                    | 79.9 ms                                                                | 80.6 ms: 1.01x slower                                                      |
| django_template            | 31.5 ms                                                                | 31.8 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.54 ms                                                                | 1.56 ms: 1.01x slower                                                      |
| fannkuch                   | 403 ms                                                                 | 407 ms: 1.01x slower                                                       |
| sympy_sum                  | 145 ms                                                                 | 146 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 156 us                                                                 | 157 us: 1.01x slower                                                       |
| json_loads                 | 28.6 us                                                                | 28.9 us: 1.01x slower                                                      |
| deepcopy                   | 254 us                                                                 | 256 us: 1.01x slower                                                       |
| subparsers                 | 20.3 ms                                                                | 20.5 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.24 ms                                                                | 1.26 ms: 1.01x slower                                                      |
| xml_etree_generate         | 83.1 ms                                                                | 84.0 ms: 1.01x slower                                                      |
| meteor_contest             | 104 ms                                                                 | 106 ms: 1.01x slower                                                       |
| logging_format             | 6.04 us                                                                | 6.12 us: 1.01x slower                                                      |
| logging_simple             | 5.42 us                                                                | 5.49 us: 1.01x slower                                                      |
| raytrace                   | 269 ms                                                                 | 273 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.2 ms                                                                | 59.1 ms: 1.02x slower                                                      |
| go                         | 115 ms                                                                 | 117 ms: 1.02x slower                                                       |
| deepcopy_memo              | 30.1 us                                                                | 30.7 us: 1.02x slower                                                      |
| hexiom                     | 6.21 ms                                                                | 6.33 ms: 1.02x slower                                                      |
| regex_dna                  | 204 ms                                                                 | 208 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.45 sec                                                               | 1.48 sec: 1.02x slower                                                     |
| pprint_safe_repr           | 703 ms                                                                 | 723 ms: 1.03x slower                                                       |
| logging_silent             | 105 ns                                                                 | 109 ns: 1.03x slower                                                       |
| deepcopy_reduce            | 2.63 us                                                                | 2.73 us: 1.04x slower                                                      |
| pyflate                    | 443 ms                                                                 | 465 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (29): async_tree_io_tg, k_core, float, async_tree_none, telco, sphinx, connected_components, shortest_path, coverage, bench_mp_pool, scimark_sparse_mat_mult, comprehensions, async_tree_io, xml_etree_parse, pylint, deltablue, tomli_loads, create_gc_cycles, asyncio_websockets, sqlalchemy_declarative, thrift, richards, dulwich_log, spectral_norm, sympy_str, nbody, sqlglot_normalize, async_tree_none_tg, pathlib

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 78.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x