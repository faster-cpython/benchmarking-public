# Results vs. base

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: f366df0
- commit date: 2025-01-29
- overall geometric mean: 1.002x faster
- HPT reliability: 98.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.59 sec                                                               | 2.58 sec: 1.00x faster                                                 |
| html5lib       | 61.8 ms                                                                | 60.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg       | 624 ms                                                                 | 609 ms: 1.03x faster                                                   |
| coroutines             | 24.0 ms                                                                | 23.6 ms: 1.01x faster                                                  |
| async_tree_memoization | 324 ms                                                                 | 321 ms: 1.01x faster                                                   |
| async_generators       | 380 ms                                                                 | 384 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.3 ms                                                                | 70.9 ms: 1.02x faster                                                  |
| nbody          | 94.3 ms                                                                | 93.2 ms: 1.01x faster                                                  |
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                 | 209 ms: 1.04x faster                                                   |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.00x faster                                                   |
| regex_effbot   | 3.27 ms                                                                | 3.34 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 323 us                                                                 | 318 us: 1.02x faster                                                   |
| json_dumps           | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                  |
| xml_etree_generate   | 83.6 ms                                                                | 83.9 ms: 1.00x slower                                                  |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                                   |
| json_loads           | 28.6 us                                                                | 28.8 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                                  |
| xml_etree_parse      | 138 ms                                                                 | 140 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.06 ms                                                                | 7.05 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                  |
| genshi_xml      | 48.2 ms                                                                | 49.1 ms: 1.02x slower                                                  |
| django_template | 31.3 ms                                                                | 32.0 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_monte_carlo     | 69.3 ms                                                                | 66.3 ms: 1.04x faster                                                  |
| regex_dna               | 218 ms                                                                 | 209 ms: 1.04x faster                                                   |
| crypto_pyaes            | 71.7 ms                                                                | 69.9 ms: 1.03x faster                                                  |
| scimark_fft             | 344 ms                                                                 | 335 ms: 1.03x faster                                                   |
| async_tree_io_tg        | 624 ms                                                                 | 609 ms: 1.03x faster                                                   |
| go                      | 119 ms                                                                 | 117 ms: 1.02x faster                                                   |
| float                   | 72.3 ms                                                                | 70.9 ms: 1.02x faster                                                  |
| html5lib                | 61.8 ms                                                                | 60.7 ms: 1.02x faster                                                  |
| meteor_contest          | 108 ms                                                                 | 106 ms: 1.02x faster                                                   |
| mako                    | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                  |
| scimark_sor             | 122 ms                                                                 | 120 ms: 1.02x faster                                                   |
| richards                | 44.9 ms                                                                | 44.2 ms: 1.02x faster                                                  |
| connected_components    | 441 ms                                                                 | 434 ms: 1.02x faster                                                   |
| pickle_pure_python      | 323 us                                                                 | 318 us: 1.02x faster                                                   |
| coroutines              | 24.0 ms                                                                | 23.6 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 4.68 ms                                                                | 4.62 ms: 1.01x faster                                                  |
| coverage                | 92.0 ms                                                                | 90.7 ms: 1.01x faster                                                  |
| pathlib                 | 16.0 ms                                                                | 15.8 ms: 1.01x faster                                                  |
| json_dumps              | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                  |
| nbody                   | 94.3 ms                                                                | 93.2 ms: 1.01x faster                                                  |
| scimark_lu              | 118 ms                                                                 | 116 ms: 1.01x faster                                                   |
| thrift                  | 767 us                                                                 | 759 us: 1.01x faster                                                   |
| logging_format          | 6.11 us                                                                | 6.04 us: 1.01x faster                                                  |
| fannkuch                | 404 ms                                                                 | 401 ms: 1.01x faster                                                   |
| generators              | 28.5 ms                                                                | 28.3 ms: 1.01x faster                                                  |
| async_tree_memoization  | 324 ms                                                                 | 321 ms: 1.01x faster                                                   |
| spectral_norm           | 96.6 ms                                                                | 95.9 ms: 1.01x faster                                                  |
| hexiom                  | 6.32 ms                                                                | 6.29 ms: 1.01x faster                                                  |
| regex_compile           | 126 ms                                                                 | 125 ms: 1.00x faster                                                   |
| many_optionals          | 937 us                                                                 | 933 us: 1.00x faster                                                   |
| mdp                     | 2.46 sec                                                               | 2.45 sec: 1.00x faster                                                 |
| docutils                | 2.59 sec                                                               | 2.58 sec: 1.00x faster                                                 |
| bench_thread_pool       | 860 us                                                                 | 858 us: 1.00x faster                                                   |
| python_startup          | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                  |
| python_startup_no_site  | 7.06 ms                                                                | 7.05 ms: 1.00x faster                                                  |
| create_gc_cycles        | 2.47 ms                                                                | 2.47 ms: 1.00x slower                                                  |
| nqueens                 | 80.3 ms                                                                | 80.5 ms: 1.00x slower                                                  |
| dulwich_log             | 63.7 ms                                                                | 63.9 ms: 1.00x slower                                                  |
| xml_etree_generate      | 83.6 ms                                                                | 83.9 ms: 1.00x slower                                                  |
| unpickle_pure_python    | 218 us                                                                 | 219 us: 1.00x slower                                                   |
| sqlglot_transpile       | 1.57 ms                                                                | 1.58 ms: 1.01x slower                                                  |
| sympy_expand            | 447 ms                                                                 | 449 ms: 1.01x slower                                                   |
| chaos                   | 58.7 ms                                                                | 59.0 ms: 1.01x slower                                                  |
| json_loads              | 28.6 us                                                                | 28.8 us: 1.01x slower                                                  |
| pidigits                | 186 ms                                                                 | 187 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 51.5 ms                                                                | 52.0 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 102 ms                                                                 | 103 ms: 1.01x slower                                                   |
| xml_etree_iterparse     | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                                  |
| async_generators        | 380 ms                                                                 | 384 ms: 1.01x slower                                                   |
| deepcopy_reduce         | 2.67 us                                                                | 2.71 us: 1.01x slower                                                  |
| subparsers              | 20.1 ms                                                                | 20.4 ms: 1.01x slower                                                  |
| deepcopy_memo           | 30.3 us                                                                | 30.8 us: 1.01x slower                                                  |
| gc_traversal            | 4.94 ms                                                                | 5.03 ms: 1.02x slower                                                  |
| deltablue               | 3.22 ms                                                                | 3.28 ms: 1.02x slower                                                  |
| genshi_xml              | 48.2 ms                                                                | 49.1 ms: 1.02x slower                                                  |
| xml_etree_parse         | 138 ms                                                                 | 140 ms: 1.02x slower                                                   |
| regex_effbot            | 3.27 ms                                                                | 3.34 ms: 1.02x slower                                                  |
| pprint_pformat          | 1.47 sec                                                               | 1.50 sec: 1.02x slower                                                 |
| django_template         | 31.3 ms                                                                | 32.0 ms: 1.02x slower                                                  |
| pprint_safe_repr        | 712 ms                                                                 | 731 ms: 1.03x slower                                                   |
| pycparser               | 1.13 sec                                                               | 1.17 sec: 1.03x slower                                                 |
| logging_silent          | 110 ns                                                                 | 113 ns: 1.03x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (34): sphinx, shortest_path, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, tomli_loads, bench_mp_pool, k_core, async_tree_none_tg, sqlglot_parse, genshi_text, raytrace, sqlalchemy_declarative, telco, 2to3, sympy_integrate, sqlalchemy_imperative, xml_etree_process, comprehensions, richards_super, typing_runtime_protocols, async_tree_io, pyflate, pylint, json, deepcopy, logging_simple, sympy_sum, asyncio_websockets, bpe_tokeniser, regex_v8, sqlite_synth, sympy_str, async_tree_none

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 98.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x