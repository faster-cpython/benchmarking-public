# Results vs. base

- fork: mdboom
- ref: fast_tuple_dealloc
- machine: linux-x86_64
- commit hash: 661a2b8
- commit date: 2025-04-15
- overall geometric mean: 1.014x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 262 ms: 1.05x slower                                                 |
| docutils       | 2.58 sec                                                               | 3.21 sec: 1.25x slower                                               |
| Geometric mean | (ref)                                                                  | 1.07x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization     | 308 ms                                                                 | 310 ms: 1.00x slower                                                 |
| async_generators           | 396 ms                                                                 | 401 ms: 1.01x slower                                                 |
| coroutines                 | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed    | 482 ms                                                                 | 493 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 490 ms: 1.02x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 94.0 ms                                                                | 94.6 ms: 1.01x slower                                                |
| float          | 67.6 ms                                                                | 69.1 ms: 1.02x slower                                                |
| pidigits       | 194 ms                                                                 | 198 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                                |
| regex_dna      | 200 ms                                                                 | 203 ms: 1.01x slower                                                 |
| regex_compile  | 125 ms                                                                 | 127 ms: 1.02x slower                                                 |
| regex_effbot   | 3.06 ms                                                                | 3.15 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 59.4 ms                                                                | 58.6 ms: 1.01x faster                                                |
| json_loads           | 29.8 us                                                                | 29.5 us: 1.01x faster                                                |
| xml_etree_generate   | 84.9 ms                                                                | 84.4 ms: 1.01x faster                                                |
| tomli_loads          | 1.97 sec                                                               | 1.98 sec: 1.00x slower                                               |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                 |
| pickle_pure_python   | 314 us                                                                 | 319 us: 1.02x slower                                                 |
| json_dumps           | 11.4 ms                                                                | 12.1 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                                |
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                |
| genshi_text     | 20.9 ms                                                                | 21.0 ms: 1.00x slower                                                |
| genshi_xml      | 48.9 ms                                                                | 49.8 ms: 1.02x slower                                                |
| mako            | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| many_optionals             | 934 us                                                                 | 921 us: 1.01x faster                                                 |
| xml_etree_process          | 59.4 ms                                                                | 58.6 ms: 1.01x faster                                                |
| shortest_path              | 499 ms                                                                 | 492 ms: 1.01x faster                                                 |
| json_loads                 | 29.8 us                                                                | 29.5 us: 1.01x faster                                                |
| generators                 | 29.8 ms                                                                | 29.5 ms: 1.01x faster                                                |
| regex_v8                   | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                                |
| pprint_pformat             | 1.48 sec                                                               | 1.46 sec: 1.01x faster                                               |
| django_template            | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                |
| xml_etree_generate         | 84.9 ms                                                                | 84.4 ms: 1.01x faster                                                |
| logging_silent             | 98.4 ns                                                                | 98.2 ns: 1.00x faster                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.48 ms: 1.00x slower                                                |
| dulwich_log                | 59.5 ms                                                                | 59.7 ms: 1.00x slower                                                |
| deepcopy                   | 253 us                                                                 | 254 us: 1.00x slower                                                 |
| hexiom                     | 6.29 ms                                                                | 6.32 ms: 1.00x slower                                                |
| tomli_loads                | 1.97 sec                                                               | 1.98 sec: 1.00x slower                                               |
| async_tree_memoization     | 308 ms                                                                 | 310 ms: 1.00x slower                                                 |
| genshi_text                | 20.9 ms                                                                | 21.0 ms: 1.00x slower                                                |
| python_startup_no_site     | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                                |
| comprehensions             | 16.6 us                                                                | 16.7 us: 1.01x slower                                                |
| nbody                      | 94.0 ms                                                                | 94.6 ms: 1.01x slower                                                |
| crypto_pyaes               | 73.4 ms                                                                | 73.9 ms: 1.01x slower                                                |
| meteor_contest             | 106 ms                                                                 | 107 ms: 1.01x slower                                                 |
| pyflate                    | 444 ms                                                                 | 447 ms: 1.01x slower                                                 |
| nqueens                    | 80.6 ms                                                                | 81.1 ms: 1.01x slower                                                |
| python_startup             | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                |
| raytrace                   | 262 ms                                                                 | 264 ms: 1.01x slower                                                 |
| scimark_fft                | 354 ms                                                                 | 358 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 216 us                                                                 | 218 us: 1.01x slower                                                 |
| scimark_lu                 | 117 ms                                                                 | 119 ms: 1.01x slower                                                 |
| sqlglot_v2_transpile       | 1.54 ms                                                                | 1.56 ms: 1.01x slower                                                |
| bench_thread_pool          | 883 us                                                                 | 892 us: 1.01x slower                                                 |
| deltablue                  | 3.34 ms                                                                | 3.37 ms: 1.01x slower                                                |
| bench_mp_pool              | 81.3 ms                                                                | 82.1 ms: 1.01x slower                                                |
| async_generators           | 396 ms                                                                 | 401 ms: 1.01x slower                                                 |
| logging_simple             | 5.54 us                                                                | 5.60 us: 1.01x slower                                                |
| regex_dna                  | 200 ms                                                                 | 203 ms: 1.01x slower                                                 |
| coverage                   | 87.3 ms                                                                | 88.4 ms: 1.01x slower                                                |
| richards                   | 43.0 ms                                                                | 43.6 ms: 1.01x slower                                                |
| scimark_sor                | 117 ms                                                                 | 119 ms: 1.01x slower                                                 |
| sympy_integrate            | 19.0 ms                                                                | 19.3 ms: 1.01x slower                                                |
| sqlglot_v2_optimize        | 52.0 ms                                                                | 52.7 ms: 1.01x slower                                                |
| deepcopy_reduce            | 2.65 us                                                                | 2.69 us: 1.02x slower                                                |
| pickle_pure_python         | 314 us                                                                 | 319 us: 1.02x slower                                                 |
| regex_compile              | 125 ms                                                                 | 127 ms: 1.02x slower                                                 |
| telco                      | 7.72 ms                                                                | 7.86 ms: 1.02x slower                                                |
| sqlglot_v2_parse           | 1.22 ms                                                                | 1.25 ms: 1.02x slower                                                |
| coroutines                 | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                |
| genshi_xml                 | 48.9 ms                                                                | 49.8 ms: 1.02x slower                                                |
| sqlalchemy_imperative      | 16.7 ms                                                                | 17.1 ms: 1.02x slower                                                |
| float                      | 67.6 ms                                                                | 69.1 ms: 1.02x slower                                                |
| pidigits                   | 194 ms                                                                 | 198 ms: 1.02x slower                                                 |
| sympy_str                  | 265 ms                                                                 | 271 ms: 1.02x slower                                                 |
| go                         | 111 ms                                                                 | 114 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed    | 482 ms                                                                 | 493 ms: 1.02x slower                                                 |
| logging_format             | 6.10 us                                                                | 6.25 us: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 478 ms                                                                 | 490 ms: 1.02x slower                                                 |
| sympy_sum                  | 147 ms                                                                 | 151 ms: 1.03x slower                                                 |
| sympy_expand               | 451 ms                                                                 | 463 ms: 1.03x slower                                                 |
| mako                       | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                                |
| bpe_tokeniser              | 4.57 sec                                                               | 4.70 sec: 1.03x slower                                               |
| spectral_norm              | 103 ms                                                                 | 106 ms: 1.03x slower                                                 |
| regex_effbot               | 3.06 ms                                                                | 3.15 ms: 1.03x slower                                                |
| sqlglot_v2_normalize       | 105 ms                                                                 | 108 ms: 1.03x slower                                                 |
| fannkuch                   | 412 ms                                                                 | 425 ms: 1.03x slower                                                 |
| mdp                        | 1.21 sec                                                               | 1.25 sec: 1.03x slower                                               |
| scimark_monte_carlo        | 65.8 ms                                                                | 68.2 ms: 1.04x slower                                                |
| sqlalchemy_declarative     | 132 ms                                                                 | 137 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 163 us                                                                 | 169 us: 1.04x slower                                                 |
| pycparser                  | 1.11 sec                                                               | 1.15 sec: 1.04x slower                                               |
| deepcopy_memo              | 28.5 us                                                                | 29.7 us: 1.04x slower                                                |
| scimark_sparse_mat_mult    | 4.65 ms                                                                | 4.86 ms: 1.04x slower                                                |
| 2to3                       | 249 ms                                                                 | 262 ms: 1.05x slower                                                 |
| json_dumps                 | 11.4 ms                                                                | 12.1 ms: 1.06x slower                                                |
| gc_traversal               | 4.62 ms                                                                | 5.11 ms: 1.11x slower                                                |
| docutils                   | 2.58 sec                                                               | 3.21 sec: 1.25x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (20): xml_etree_parse, xml_etree_iterparse, pprint_safe_repr, html5lib, richards_super, asyncio_websockets, subparsers, async_tree_io, pathlib, chaos, async_tree_io_tg, connected_components, async_tree_none, sqlite_synth, pylint, k_core, json, async_tree_none_tg, sphinx, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x