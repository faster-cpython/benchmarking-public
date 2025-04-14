# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: ffcb0ed
- commit date: 2025-03-26
- overall geometric mean: 1.007x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.00x slower                                                 |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                               |
| html5lib       | 63.2 ms                                                                | 63.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                                 | 262 ms: 1.01x faster                                                 |
| async_generators           | 418 ms                                                                 | 419 ms: 1.00x slower                                                 |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 485 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 501 ms: 1.02x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (7): async_tree_io, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                                |
| float          | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| regex_v8       | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                                |
| regex_dna      | 217 ms                                                                 | 225 ms: 1.04x slower                                                 |
| regex_effbot   | 3.16 ms                                                                | 3.39 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process   | 57.1 ms                                                                | 56.4 ms: 1.01x faster                                                |
| xml_etree_generate  | 80.8 ms                                                                | 80.4 ms: 1.01x faster                                                |
| pickle_pure_python  | 325 us                                                                 | 327 us: 1.01x slower                                                 |
| xml_etree_iterparse | 97.6 ms                                                                | 98.6 ms: 1.01x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (5): json_loads, tomli_loads, unpickle_pure_python, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| python_startup_no_site | 8.19 ms                                                                | 8.20 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                |
| django_template | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| crypto_pyaes               | 78.3 ms                                                                | 76.5 ms: 1.02x faster                                                |
| spectral_norm              | 97.1 ms                                                                | 95.2 ms: 1.02x faster                                                |
| generators                 | 29.2 ms                                                                | 28.7 ms: 1.02x faster                                                |
| scimark_fft                | 312 ms                                                                 | 307 ms: 1.02x faster                                                 |
| async_tree_none            | 266 ms                                                                 | 262 ms: 1.01x faster                                                 |
| xml_etree_process          | 57.1 ms                                                                | 56.4 ms: 1.01x faster                                                |
| pathlib                    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                |
| raytrace                   | 269 ms                                                                 | 266 ms: 1.01x faster                                                 |
| scimark_lu                 | 118 ms                                                                 | 116 ms: 1.01x faster                                                 |
| nbody                      | 89.4 ms                                                                | 88.4 ms: 1.01x faster                                                |
| shortest_path              | 494 ms                                                                 | 490 ms: 1.01x faster                                                 |
| gc_traversal               | 5.05 ms                                                                | 5.01 ms: 1.01x faster                                                |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                |
| hexiom                     | 6.86 ms                                                                | 6.82 ms: 1.01x faster                                                |
| xml_etree_generate         | 80.8 ms                                                                | 80.4 ms: 1.01x faster                                                |
| scimark_sor                | 119 ms                                                                 | 118 ms: 1.00x faster                                                 |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| python_startup_no_site     | 8.19 ms                                                                | 8.20 ms: 1.00x slower                                                |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                                |
| async_generators           | 418 ms                                                                 | 419 ms: 1.00x slower                                                 |
| 2to3                       | 263 ms                                                                 | 264 ms: 1.00x slower                                                 |
| docutils                   | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                               |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.63 ms: 1.00x slower                                                |
| bench_thread_pool          | 882 us                                                                 | 886 us: 1.00x slower                                                 |
| subparsers                 | 21.0 ms                                                                | 21.1 ms: 1.01x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| deepcopy                   | 260 us                                                                 | 262 us: 1.01x slower                                                 |
| pickle_pure_python         | 325 us                                                                 | 327 us: 1.01x slower                                                 |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.5 ms: 1.01x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                 |
| sympy_integrate            | 20.0 ms                                                                | 20.2 ms: 1.01x slower                                                |
| html5lib                   | 63.2 ms                                                                | 63.7 ms: 1.01x slower                                                |
| sympy_str                  | 274 ms                                                                 | 277 ms: 1.01x slower                                                 |
| bpe_tokeniser              | 4.57 sec                                                               | 4.62 sec: 1.01x slower                                               |
| deepcopy_memo              | 29.0 us                                                                | 29.3 us: 1.01x slower                                                |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.6 ms: 1.01x slower                                                |
| regex_v8                   | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                                |
| django_template            | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 485 ms: 1.01x slower                                                 |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.01x slower                                                 |
| go                         | 128 ms                                                                 | 130 ms: 1.01x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                                 | 134 ms: 1.01x slower                                                 |
| float                      | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                                |
| pprint_safe_repr           | 756 ms                                                                 | 768 ms: 1.01x slower                                                 |
| nqueens                    | 84.9 ms                                                                | 86.1 ms: 1.01x slower                                                |
| many_optionals             | 970 us                                                                 | 985 us: 1.01x slower                                                 |
| sympy_sum                  | 152 ms                                                                 | 154 ms: 1.02x slower                                                 |
| logging_simple             | 5.59 us                                                                | 5.67 us: 1.02x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 501 ms: 1.02x slower                                                 |
| comprehensions             | 19.0 us                                                                | 19.4 us: 1.02x slower                                                |
| pprint_pformat             | 1.55 sec                                                               | 1.58 sec: 1.02x slower                                               |
| pyflate                    | 432 ms                                                                 | 441 ms: 1.02x slower                                                 |
| connected_components       | 454 ms                                                                 | 464 ms: 1.02x slower                                                 |
| mdp                        | 2.48 sec                                                               | 2.54 sec: 1.02x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.74 us: 1.03x slower                                                |
| regex_dna                  | 217 ms                                                                 | 225 ms: 1.04x slower                                                 |
| pycparser                  | 1.13 sec                                                               | 1.19 sec: 1.06x slower                                               |
| regex_effbot               | 3.16 ms                                                                | 3.39 ms: 1.07x slower                                                |
| richards_super             | 41.1 ms                                                                | 47.2 ms: 1.15x slower                                                |
| richards                   | 35.8 ms                                                                | 41.6 ms: 1.16x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (33): async_tree_io, async_tree_memoization, async_tree_io_tg, json_loads, tomli_loads, json, asyncio_websockets, async_tree_memoization_tg, bench_mp_pool, sqlite_synth, logging_silent, async_tree_none_tg, coroutines, pidigits, unpickle_pure_python, telco, chaos, dulwich_log, deltablue, sympy_expand, coverage, typing_runtime_protocols, k_core, json_dumps, genshi_text, genshi_xml, logging_format, pylint, xml_etree_parse, fannkuch, scimark_monte_carlo, thrift, sphinx

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x