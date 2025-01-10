# Results vs. base

- fork: iritkatriel
- ref: cmq
- machine: linux-x86_64
- commit hash: 82b084a
- commit date: 2025-01-09
- overall geometric mean: 1.002x faster
- HPT reliability: 57.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                       |
| docutils       | 2.60 sec                                                               | 2.61 sec: 1.00x slower                                     |
| html5lib       | 61.8 ms                                                                | 61.3 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 24.6 ms                                                                | 23.1 ms: 1.07x faster                                      |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 472 ms: 1.00x slower                                       |
| async_generators           | 419 ms                                                                 | 426 ms: 1.02x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                | 25.7 ms: 1.02x faster                                      |
| regex_effbot   | 3.44 ms                                                                | 3.41 ms: 1.01x faster                                      |
| regex_dna      | 215 ms                                                                 | 216 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                 | 216 us: 1.01x faster                                       |
| json_loads           | 26.7 us                                                                | 26.6 us: 1.00x faster                                      |
| xml_etree_process    | 59.3 ms                                                                | 59.6 ms: 1.00x slower                                      |
| xml_etree_generate   | 84.8 ms                                                                | 85.6 ms: 1.01x slower                                      |
| tomli_loads          | 1.92 sec                                                               | 1.95 sec: 1.02x slower                                     |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (4): pickle_pure_python, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                      |
| genshi_text     | 21.8 ms                                                                | 22.1 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250109-linux-x86_64-iritkatriel-cmq-3.14.0a3+-82b084a |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| spectral_norm              | 103 ms                                                                 | 90.5 ms: 1.14x faster                                      |
| coroutines                 | 24.6 ms                                                                | 23.1 ms: 1.07x faster                                      |
| chaos                      | 60.8 ms                                                                | 58.0 ms: 1.05x faster                                      |
| pathlib                    | 16.4 ms                                                                | 15.9 ms: 1.03x faster                                      |
| crypto_pyaes               | 72.8 ms                                                                | 70.8 ms: 1.03x faster                                      |
| scimark_monte_carlo        | 67.9 ms                                                                | 66.1 ms: 1.03x faster                                      |
| pprint_safe_repr           | 741 ms                                                                 | 722 ms: 1.03x faster                                       |
| pprint_pformat             | 1.52 sec                                                               | 1.48 sec: 1.02x faster                                     |
| scimark_fft                | 343 ms                                                                 | 335 ms: 1.02x faster                                       |
| bpe_tokeniser              | 4.64 sec                                                               | 4.56 sec: 1.02x faster                                     |
| fannkuch                   | 406 ms                                                                 | 399 ms: 1.02x faster                                       |
| regex_v8                   | 26.1 ms                                                                | 25.7 ms: 1.02x faster                                      |
| logging_format             | 6.30 us                                                                | 6.20 us: 1.02x faster                                      |
| sqlite_synth               | 2.84 us                                                                | 2.80 us: 1.01x faster                                      |
| typing_runtime_protocols   | 163 us                                                                 | 161 us: 1.01x faster                                       |
| html5lib                   | 61.8 ms                                                                | 61.3 ms: 1.01x faster                                      |
| unpickle_pure_python       | 217 us                                                                 | 216 us: 1.01x faster                                       |
| regex_effbot               | 3.44 ms                                                                | 3.41 ms: 1.01x faster                                      |
| deepcopy                   | 260 us                                                                 | 258 us: 1.01x faster                                       |
| mdp                        | 2.50 sec                                                               | 2.49 sec: 1.01x faster                                     |
| json_loads                 | 26.7 us                                                                | 26.6 us: 1.00x faster                                      |
| dulwich_log                | 63.8 ms                                                                | 63.5 ms: 1.00x faster                                      |
| hexiom                     | 6.20 ms                                                                | 6.17 ms: 1.00x faster                                      |
| scimark_sor                | 121 ms                                                                 | 120 ms: 1.00x faster                                       |
| many_optionals             | 945 us                                                                 | 942 us: 1.00x faster                                       |
| pidigits                   | 189 ms                                                                 | 189 ms: 1.00x faster                                       |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.4 ms: 1.00x faster                                      |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                      |
| regex_dna                  | 215 ms                                                                 | 216 ms: 1.00x slower                                       |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 472 ms: 1.00x slower                                       |
| python_startup_no_site     | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                      |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                       |
| docutils                   | 2.60 sec                                                               | 2.61 sec: 1.00x slower                                     |
| go                         | 116 ms                                                                 | 117 ms: 1.00x slower                                       |
| xml_etree_process          | 59.3 ms                                                                | 59.6 ms: 1.00x slower                                      |
| sqlalchemy_declarative     | 128 ms                                                                 | 129 ms: 1.00x slower                                       |
| bench_thread_pool          | 858 us                                                                 | 862 us: 1.00x slower                                       |
| richards_super             | 50.6 ms                                                                | 50.8 ms: 1.01x slower                                      |
| sqlglot_optimize           | 52.4 ms                                                                | 52.7 ms: 1.01x slower                                      |
| deepcopy_memo              | 30.4 us                                                                | 30.6 us: 1.01x slower                                      |
| create_gc_cycles           | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                      |
| xml_etree_generate         | 84.8 ms                                                                | 85.6 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult    | 4.51 ms                                                                | 4.56 ms: 1.01x slower                                      |
| sqlglot_normalize          | 103 ms                                                                 | 104 ms: 1.01x slower                                       |
| sqlglot_transpile          | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                      |
| django_template            | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                      |
| meteor_contest             | 106 ms                                                                 | 108 ms: 1.01x slower                                       |
| generators                 | 27.2 ms                                                                | 27.6 ms: 1.02x slower                                      |
| genshi_text                | 21.8 ms                                                                | 22.1 ms: 1.02x slower                                      |
| sqlglot_parse              | 1.25 ms                                                                | 1.27 ms: 1.02x slower                                      |
| async_generators           | 419 ms                                                                 | 426 ms: 1.02x slower                                       |
| tomli_loads                | 1.92 sec                                                               | 1.95 sec: 1.02x slower                                     |
| logging_silent             | 105 ns                                                                 | 107 ns: 1.02x slower                                       |
| deepcopy_reduce            | 2.64 us                                                                | 2.70 us: 1.02x slower                                      |
| scimark_lu                 | 113 ms                                                                 | 115 ms: 1.02x slower                                       |
| comprehensions             | 16.4 us                                                                | 16.9 us: 1.03x slower                                      |
| gc_traversal               | 4.75 ms                                                                | 4.92 ms: 1.04x slower                                      |
| nqueens                    | 78.9 ms                                                                | 81.8 ms: 1.04x slower                                      |
| pyflate                    | 443 ms                                                                 | 470 ms: 1.06x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (37): async_tree_none_tg, pycparser, connected_components, bench_mp_pool, sympy_expand, subparsers, pickle_pure_python, async_tree_memoization, float, async_tree_none, sympy_sum, regex_compile, coverage, nbody, async_tree_memoization_tg, json_dumps, raytrace, genshi_xml, mako, sympy_integrate, xml_etree_iterparse, sympy_str, xml_etree_parse, logging_simple, async_tree_io_tg, pylint, sphinx, shortest_path, asyncio_websockets, thrift, richards, json, deltablue, async_tree_cpu_io_mixed, telco, k_core, async_tree_io

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 57.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x