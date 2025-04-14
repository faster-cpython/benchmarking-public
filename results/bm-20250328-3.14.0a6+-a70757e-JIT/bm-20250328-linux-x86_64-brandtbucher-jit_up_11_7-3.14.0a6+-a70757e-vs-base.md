# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_7
- machine: linux-x86_64
- commit hash: a70757e
- commit date: 2025-03-28
- overall geometric mean: 1.001x slower
- HPT reliability: 54.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 264 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 472 ms: 1.02x faster                                                |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 489 ms: 1.01x faster                                                |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 65.3 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 211 ms: 1.03x faster                                                |
| regex_v8       | 23.5 ms                                                                | 22.9 ms: 1.02x faster                                               |
| regex_effbot   | 3.16 ms                                                                | 3.10 ms: 1.02x faster                                               |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.2 ms: 1.01x slower                                               |
| unpickle_pure_python | 214 us                                                                 | 216 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (6): json_loads, xml_etree_parse, xml_etree_generate, pickle_pure_python, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                               |
| django_template | 32.0 ms                                                                | 32.9 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.05 ms                                                                | 4.85 ms: 1.04x faster                                               |
| crypto_pyaes               | 78.3 ms                                                                | 75.5 ms: 1.04x faster                                               |
| regex_dna                  | 217 ms                                                                 | 211 ms: 1.03x faster                                                |
| regex_v8                   | 23.5 ms                                                                | 22.9 ms: 1.02x faster                                               |
| async_tree_none            | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| fannkuch                   | 423 ms                                                                 | 414 ms: 1.02x faster                                                |
| telco                      | 7.93 ms                                                                | 7.78 ms: 1.02x faster                                               |
| subparsers                 | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                               |
| regex_effbot               | 3.16 ms                                                                | 3.10 ms: 1.02x faster                                               |
| comprehensions             | 19.0 us                                                                | 18.7 us: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 472 ms: 1.02x faster                                                |
| raytrace                   | 269 ms                                                                 | 266 ms: 1.01x faster                                                |
| thrift                     | 783 us                                                                 | 775 us: 1.01x faster                                                |
| async_generators           | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| mako                       | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                               |
| chaos                      | 60.3 ms                                                                | 59.8 ms: 1.01x faster                                               |
| go                         | 128 ms                                                                 | 127 ms: 1.01x faster                                                |
| xml_etree_process          | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                               |
| pathlib                    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                               |
| pyflate                    | 432 ms                                                                 | 429 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 489 ms: 1.01x faster                                                |
| generators                 | 29.2 ms                                                                | 29.1 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                               |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.00x slower                                                |
| bpe_tokeniser              | 4.57 sec                                                               | 4.59 sec: 1.00x slower                                              |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x slower                                                |
| 2to3                       | 263 ms                                                                 | 264 ms: 1.00x slower                                                |
| dulwich_log                | 60.6 ms                                                                | 60.9 ms: 1.00x slower                                               |
| bench_thread_pool          | 882 us                                                                 | 886 us: 1.00x slower                                                |
| mdp                        | 2.48 sec                                                               | 2.49 sec: 1.01x slower                                              |
| float                      | 64.9 ms                                                                | 65.3 ms: 1.01x slower                                               |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.01x slower                                               |
| scimark_fft                | 312 ms                                                                 | 314 ms: 1.01x slower                                                |
| sympy_expand               | 475 ms                                                                 | 478 ms: 1.01x slower                                                |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                               |
| xml_etree_iterparse        | 97.6 ms                                                                | 98.2 ms: 1.01x slower                                               |
| many_optionals             | 970 us                                                                 | 978 us: 1.01x slower                                                |
| deltablue                  | 3.06 ms                                                                | 3.08 ms: 1.01x slower                                               |
| sqlglot_v2_optimize        | 54.1 ms                                                                | 54.6 ms: 1.01x slower                                               |
| sympy_str                  | 274 ms                                                                 | 277 ms: 1.01x slower                                                |
| unpickle_pure_python       | 214 us                                                                 | 216 us: 1.01x slower                                                |
| json                       | 5.29 ms                                                                | 5.35 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                                 | 119 ms: 1.01x slower                                                |
| sympy_integrate            | 20.0 ms                                                                | 20.3 ms: 1.01x slower                                               |
| sqlglot_v2_normalize       | 107 ms                                                                 | 109 ms: 1.01x slower                                                |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.63 ms: 1.01x slower                                               |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                |
| deepcopy                   | 260 us                                                                 | 264 us: 1.02x slower                                                |
| typing_runtime_protocols   | 167 us                                                                 | 170 us: 1.02x slower                                                |
| deepcopy_memo              | 29.0 us                                                                | 29.5 us: 1.02x slower                                               |
| sympy_sum                  | 152 ms                                                                 | 155 ms: 1.02x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                                 | 136 ms: 1.02x slower                                                |
| logging_silent             | 95.7 ns                                                                | 98.1 ns: 1.03x slower                                               |
| django_template            | 32.0 ms                                                                | 32.9 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.73 ms: 1.03x slower                                               |
| pprint_safe_repr           | 756 ms                                                                 | 777 ms: 1.03x slower                                                |
| deepcopy_reduce            | 2.66 us                                                                | 2.74 us: 1.03x slower                                               |
| richards                   | 35.8 ms                                                                | 36.8 ms: 1.03x slower                                               |
| hexiom                     | 6.86 ms                                                                | 7.11 ms: 1.04x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (34): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, nbody, json_loads, async_tree_none_tg, xml_etree_parse, logging_format, xml_etree_generate, shortest_path, k_core, docutils, asyncio_websockets, bench_mp_pool, spectral_norm, pickle_pure_python, genshi_xml, html5lib, create_gc_cycles, connected_components, json_dumps, pprint_pformat, richards_super, sqlite_synth, tomli_loads, logging_simple, sphinx, genshi_text, scimark_monte_carlo, pylint, coverage, nqueens, pycparser

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 54.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x