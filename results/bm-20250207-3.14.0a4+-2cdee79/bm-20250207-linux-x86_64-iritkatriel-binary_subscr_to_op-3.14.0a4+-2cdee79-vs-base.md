# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 2cdee79
- commit date: 2025-02-07
- overall geometric mean: 1.000x faster
- HPT reliability: 91.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 252 ms: 1.01x faster                                                       |
| docutils       | 2.57 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 61.7 ms                                                                | 61.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 259 ms                                                                 | 256 ms: 1.01x faster                                                       |
| async_generators           | 387 ms                                                                 | 384 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 493 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 501 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (6): async_tree_none, asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.1 ms                                                                | 91.9 ms: 1.04x faster                                                      |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                | 24.3 ms: 1.04x faster                                                      |
| regex_dna      | 217 ms                                                                 | 215 ms: 1.01x faster                                                       |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 83.6 ms                                                                | 83.2 ms: 1.01x faster                                                      |
| xml_etree_process    | 58.4 ms                                                                | 58.1 ms: 1.00x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 218 us: 1.00x faster                                                       |
| xml_etree_iterparse  | 96.2 ms                                                                | 97.1 ms: 1.01x slower                                                      |
| json_loads           | 28.4 us                                                                | 28.7 us: 1.01x slower                                                      |
| json_dumps           | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): tomli_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.02 ms: 1.00x slower                                                      |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| genshi_xml      | 47.4 ms                                                                | 48.0 ms: 1.01x slower                                                      |
| django_template | 31.7 ms                                                                | 32.2 ms: 1.01x slower                                                      |
| mako            | 11.2 ms                                                                | 11.3 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent             | 112 ns                                                                 | 106 ns: 1.05x faster                                                       |
| deltablue                  | 3.32 ms                                                                | 3.17 ms: 1.05x faster                                                      |
| regex_v8                   | 25.2 ms                                                                | 24.3 ms: 1.04x faster                                                      |
| nbody                      | 95.1 ms                                                                | 91.9 ms: 1.04x faster                                                      |
| richards                   | 45.5 ms                                                                | 44.6 ms: 1.02x faster                                                      |
| telco                      | 7.95 ms                                                                | 7.81 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 16.5 ms                                                                | 16.2 ms: 1.02x faster                                                      |
| richards_super             | 51.9 ms                                                                | 51.2 ms: 1.01x faster                                                      |
| scimark_fft                | 342 ms                                                                 | 337 ms: 1.01x faster                                                       |
| comprehensions             | 16.4 us                                                                | 16.2 us: 1.01x faster                                                      |
| raytrace                   | 275 ms                                                                 | 271 ms: 1.01x faster                                                       |
| coroutines                 | 23.4 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| shortest_path              | 477 ms                                                                 | 472 ms: 1.01x faster                                                       |
| async_tree_none_tg         | 259 ms                                                                 | 256 ms: 1.01x faster                                                       |
| genshi_text                | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| meteor_contest             | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| sqlglot_parse              | 1.26 ms                                                                | 1.25 ms: 1.01x faster                                                      |
| generators                 | 27.9 ms                                                                | 27.6 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 2.69 us                                                                | 2.66 us: 1.01x faster                                                      |
| pathlib                    | 15.8 ms                                                                | 15.6 ms: 1.01x faster                                                      |
| async_generators           | 387 ms                                                                 | 384 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 4.46 sec                                                               | 4.42 sec: 1.01x faster                                                     |
| regex_dna                  | 217 ms                                                                 | 215 ms: 1.01x faster                                                       |
| go                         | 119 ms                                                                 | 118 ms: 1.01x faster                                                       |
| 2to3                       | 254 ms                                                                 | 252 ms: 1.01x faster                                                       |
| deepcopy                   | 261 us                                                                 | 259 us: 1.01x faster                                                       |
| html5lib                   | 61.7 ms                                                                | 61.2 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.57 ms                                                                | 1.55 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 52.2 ms                                                                | 51.8 ms: 1.01x faster                                                      |
| bench_mp_pool              | 81.1 ms                                                                | 80.5 ms: 1.01x faster                                                      |
| mdp                        | 2.49 sec                                                               | 2.47 sec: 1.01x faster                                                     |
| xml_etree_generate         | 83.6 ms                                                                | 83.2 ms: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                                | 58.1 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 218 us: 1.00x faster                                                       |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x faster                                                       |
| docutils                   | 2.57 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                       |
| python_startup_no_site     | 7.02 ms                                                                | 7.02 ms: 1.00x slower                                                      |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| pprint_pformat             | 1.48 sec                                                               | 1.48 sec: 1.00x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                      |
| sympy_sum                  | 146 ms                                                                 | 146 ms: 1.00x slower                                                       |
| sympy_integrate            | 19.6 ms                                                                | 19.7 ms: 1.00x slower                                                      |
| bench_thread_pool          | 856 us                                                                 | 860 us: 1.01x slower                                                       |
| many_optionals             | 923 us                                                                 | 930 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 96.2 ms                                                                | 97.1 ms: 1.01x slower                                                      |
| regex_compile              | 126 ms                                                                 | 127 ms: 1.01x slower                                                       |
| crypto_pyaes               | 70.1 ms                                                                | 70.8 ms: 1.01x slower                                                      |
| json_loads                 | 28.4 us                                                                | 28.7 us: 1.01x slower                                                      |
| spectral_norm              | 94.8 ms                                                                | 96.0 ms: 1.01x slower                                                      |
| genshi_xml                 | 47.4 ms                                                                | 48.0 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                                | 32.2 ms: 1.01x slower                                                      |
| json_dumps                 | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| logging_format             | 5.98 us                                                                | 6.07 us: 1.01x slower                                                      |
| logging_simple             | 5.42 us                                                                | 5.50 us: 1.01x slower                                                      |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.02x slower                                                      |
| fannkuch                   | 397 ms                                                                 | 405 ms: 1.02x slower                                                       |
| pyflate                    | 437 ms                                                                 | 446 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                 | 493 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 501 ms: 1.03x slower                                                       |
| scimark_lu                 | 113 ms                                                                 | 117 ms: 1.03x slower                                                       |
| coverage                   | 89.5 ms                                                                | 92.4 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 4.64 ms                                                                | 4.81 ms: 1.04x slower                                                      |
| gc_traversal               | 4.61 ms                                                                | 4.80 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (32): k_core, connected_components, sympy_expand, json, async_tree_none, asyncio_websockets, sphinx, pycparser, sqlglot_normalize, deepcopy_memo, sqlite_synth, pylint, tomli_loads, pickle_pure_python, async_tree_io, hexiom, float, sympy_str, thrift, async_tree_memoization, regex_effbot, pprint_safe_repr, chaos, subparsers, nqueens, dulwich_log, async_tree_io_tg, typing_runtime_protocols, async_tree_memoization_tg, scimark_monte_carlo, scimark_sor, xml_etree_parse

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 91.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x