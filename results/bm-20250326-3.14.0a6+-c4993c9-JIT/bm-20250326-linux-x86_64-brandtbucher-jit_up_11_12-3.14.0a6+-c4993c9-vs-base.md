# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: c4993c9
- commit date: 2025-03-26
- overall geometric mean: 1.005x slower
- HPT reliability: 84.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 263 ms: 1.00x slower                                                 |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                               |
| html5lib       | 63.2 ms                                                                | 62.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                                 | 261 ms: 1.02x faster                                                 |
| coroutines                 | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 476 ms: 1.01x faster                                                 |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.9 ms: 1.02x faster                                                |
| float          | 64.9 ms                                                                | 65.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| regex_v8       | 23.5 ms                                                                | 23.9 ms: 1.02x slower                                                |
| regex_dna      | 217 ms                                                                 | 228 ms: 1.05x slower                                                 |
| regex_effbot   | 3.16 ms                                                                | 3.54 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.87 sec                                                               | 1.84 sec: 1.01x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| xml_etree_generate   | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                                |
| pickle_pure_python   | 325 us                                                                 | 327 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.5 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                |
| python_startup_no_site | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                |
| genshi_text     | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                                |
| genshi_xml      | 49.8 ms                                                                | 50.4 ms: 1.01x slower                                                |
| django_template | 32.0 ms                                                                | 32.5 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.75 ms: 1.06x faster                                                |
| crypto_pyaes               | 78.3 ms                                                                | 75.9 ms: 1.03x faster                                                |
| spectral_norm              | 97.1 ms                                                                | 94.6 ms: 1.03x faster                                                |
| async_tree_none            | 266 ms                                                                 | 261 ms: 1.02x faster                                                 |
| coroutines                 | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                                |
| scimark_lu                 | 118 ms                                                                 | 116 ms: 1.02x faster                                                 |
| nbody                      | 89.4 ms                                                                | 87.9 ms: 1.02x faster                                                |
| generators                 | 29.2 ms                                                                | 28.8 ms: 1.01x faster                                                |
| tomli_loads                | 1.87 sec                                                               | 1.84 sec: 1.01x faster                                               |
| nqueens                    | 84.9 ms                                                                | 83.9 ms: 1.01x faster                                                |
| hexiom                     | 6.86 ms                                                                | 6.79 ms: 1.01x faster                                                |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                 |
| html5lib                   | 63.2 ms                                                                | 62.7 ms: 1.01x faster                                                |
| unpickle_pure_python       | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 476 ms: 1.01x faster                                                 |
| xml_etree_generate         | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                                |
| chaos                      | 60.3 ms                                                                | 60.0 ms: 1.01x faster                                                |
| async_generators           | 418 ms                                                                 | 415 ms: 1.01x faster                                                 |
| dulwich_log                | 60.6 ms                                                                | 60.4 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                                |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                |
| python_startup_no_site     | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                                |
| 2to3                       | 263 ms                                                                 | 263 ms: 1.00x slower                                                 |
| bench_thread_pool          | 882 us                                                                 | 884 us: 1.00x slower                                                 |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| many_optionals             | 970 us                                                                 | 975 us: 1.00x slower                                                 |
| pathlib                    | 16.8 ms                                                                | 16.8 ms: 1.00x slower                                                |
| sympy_integrate            | 20.0 ms                                                                | 20.2 ms: 1.01x slower                                                |
| go                         | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                 |
| logging_simple             | 5.59 us                                                                | 5.62 us: 1.01x slower                                                |
| pickle_pure_python         | 325 us                                                                 | 327 us: 1.01x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                                |
| fannkuch                   | 423 ms                                                                 | 426 ms: 1.01x slower                                                 |
| genshi_text                | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                |
| sympy_expand               | 475 ms                                                                 | 479 ms: 1.01x slower                                                 |
| float                      | 64.9 ms                                                                | 65.5 ms: 1.01x slower                                                |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.7 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.5 ms: 1.01x slower                                                |
| sympy_str                  | 274 ms                                                                 | 277 ms: 1.01x slower                                                 |
| docutils                   | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                               |
| bpe_tokeniser              | 4.57 sec                                                               | 4.62 sec: 1.01x slower                                               |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                               |
| genshi_xml                 | 49.8 ms                                                                | 50.4 ms: 1.01x slower                                                |
| sympy_sum                  | 152 ms                                                                 | 153 ms: 1.01x slower                                                 |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.31 ms: 1.01x slower                                                |
| django_template            | 32.0 ms                                                                | 32.5 ms: 1.01x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                                 | 135 ms: 1.01x slower                                                 |
| deepcopy_memo              | 29.0 us                                                                | 29.5 us: 1.02x slower                                                |
| regex_v8                   | 23.5 ms                                                                | 23.9 ms: 1.02x slower                                                |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.02x slower                                                 |
| deepcopy                   | 260 us                                                                 | 265 us: 1.02x slower                                                 |
| typing_runtime_protocols   | 167 us                                                                 | 170 us: 1.02x slower                                                 |
| connected_components       | 454 ms                                                                 | 464 ms: 1.02x slower                                                 |
| deepcopy_reduce            | 2.66 us                                                                | 2.73 us: 1.03x slower                                                |
| pprint_pformat             | 1.55 sec                                                               | 1.59 sec: 1.03x slower                                               |
| logging_silent             | 95.7 ns                                                                | 98.8 ns: 1.03x slower                                                |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.76 ms: 1.03x slower                                                |
| pyflate                    | 432 ms                                                                 | 451 ms: 1.04x slower                                                 |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                               |
| regex_dna                  | 217 ms                                                                 | 228 ms: 1.05x slower                                                 |
| richards_super             | 41.1 ms                                                                | 44.2 ms: 1.08x slower                                                |
| richards                   | 35.8 ms                                                                | 39.0 ms: 1.09x slower                                                |
| regex_effbot               | 3.16 ms                                                                | 3.54 ms: 1.12x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (30): async_tree_io, async_tree_memoization_tg, telco, async_tree_none_tg, json_loads, pprint_safe_repr, async_tree_io_tg, xml_etree_process, comprehensions, bench_mp_pool, scimark_monte_carlo, thrift, shortest_path, deltablue, asyncio_websockets, raytrace, pidigits, json_dumps, pylint, scimark_sor, scimark_fft, xml_etree_parse, json, subparsers, async_tree_cpu_io_mixed, logging_format, sqlite_synth, sphinx, k_core, coverage

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 84.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x