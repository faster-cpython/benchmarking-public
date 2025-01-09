# Results vs. base

- fork: iritkatriel
- ref: cmq
- machine: linux-x86_64
- commit hash: 708575f
- commit date: 2025-01-08
- overall geometric mean: 1.002x slower
- HPT reliability: 70.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 24.6 ms                                                                | 23.6 ms: 1.04x faster                                      |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 486 ms: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 467 ms: 1.01x faster                                       |
| async_tree_memoization_tg  | 308 ms                                                                 | 311 ms: 1.01x slower                                       |
| async_generators           | 419 ms                                                                 | 424 ms: 1.01x slower                                       |
| async_tree_io_tg           | 587 ms                                                                 | 595 ms: 1.01x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (5): async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                       |
| nbody          | 93.5 ms                                                                | 94.4 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                | 25.3 ms: 1.03x faster                                      |
| regex_dna      | 215 ms                                                                 | 214 ms: 1.01x faster                                       |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 59.3 ms                                                                | 58.6 ms: 1.01x faster                                      |
| xml_etree_generate   | 84.8 ms                                                                | 84.3 ms: 1.01x faster                                      |
| pickle_pure_python   | 320 us                                                                 | 319 us: 1.00x faster                                       |
| unpickle_pure_python | 217 us                                                                 | 217 us: 1.00x faster                                       |
| json_loads           | 26.7 us                                                                | 26.9 us: 1.01x slower                                      |
| tomli_loads          | 1.92 sec                                                               | 1.99 sec: 1.04x slower                                     |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (3): json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                      |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.5 ms                                                                | 11.1 ms: 1.03x faster                                      |
| genshi_xml      | 49.7 ms                                                                | 49.2 ms: 1.01x faster                                      |
| genshi_text     | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                      |
| django_template | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250108-linux-x86_64-python-004f9fd1f22643100aa8-3.14.0a3+-004f9fd | bm-20250108-linux-x86_64-iritkatriel-cmq-3.14.0a3+-708575f |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 24.6 ms                                                                | 23.6 ms: 1.04x faster                                      |
| pycparser                  | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                     |
| regex_v8                   | 26.1 ms                                                                | 25.3 ms: 1.03x faster                                      |
| pathlib                    | 16.4 ms                                                                | 15.9 ms: 1.03x faster                                      |
| chaos                      | 60.8 ms                                                                | 58.9 ms: 1.03x faster                                      |
| mako                       | 11.5 ms                                                                | 11.1 ms: 1.03x faster                                      |
| crypto_pyaes               | 72.8 ms                                                                | 71.0 ms: 1.02x faster                                      |
| pprint_safe_repr           | 741 ms                                                                 | 726 ms: 1.02x faster                                       |
| pprint_pformat             | 1.52 sec                                                               | 1.49 sec: 1.02x faster                                     |
| fannkuch                   | 406 ms                                                                 | 399 ms: 1.02x faster                                       |
| bpe_tokeniser              | 4.64 sec                                                               | 4.57 sec: 1.01x faster                                     |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 486 ms: 1.01x faster                                       |
| sqlite_synth               | 2.84 us                                                                | 2.80 us: 1.01x faster                                      |
| scimark_monte_carlo        | 67.9 ms                                                                | 67.0 ms: 1.01x faster                                      |
| xml_etree_process          | 59.3 ms                                                                | 58.6 ms: 1.01x faster                                      |
| genshi_xml                 | 49.7 ms                                                                | 49.2 ms: 1.01x faster                                      |
| dulwich_log                | 63.8 ms                                                                | 63.2 ms: 1.01x faster                                      |
| subparsers                 | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                      |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 467 ms: 1.01x faster                                       |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.01x faster                                       |
| logging_format             | 6.30 us                                                                | 6.25 us: 1.01x faster                                      |
| regex_dna                  | 215 ms                                                                 | 214 ms: 1.01x faster                                       |
| go                         | 116 ms                                                                 | 116 ms: 1.01x faster                                       |
| xml_etree_generate         | 84.8 ms                                                                | 84.3 ms: 1.01x faster                                      |
| deltablue                  | 3.24 ms                                                                | 3.23 ms: 1.01x faster                                      |
| meteor_contest             | 106 ms                                                                 | 106 ms: 1.00x faster                                       |
| pickle_pure_python         | 320 us                                                                 | 319 us: 1.00x faster                                       |
| unpickle_pure_python       | 217 us                                                                 | 217 us: 1.00x faster                                       |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                      |
| pidigits                   | 189 ms                                                                 | 189 ms: 1.00x faster                                       |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                      |
| gc_traversal               | 4.75 ms                                                                | 4.76 ms: 1.00x slower                                      |
| raytrace                   | 273 ms                                                                 | 274 ms: 1.00x slower                                       |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                      |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                      |
| sqlglot_optimize           | 52.4 ms                                                                | 52.6 ms: 1.00x slower                                      |
| richards_super             | 50.6 ms                                                                | 50.8 ms: 1.00x slower                                      |
| thrift                     | 770 us                                                                 | 774 us: 1.01x slower                                       |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.01x slower                                       |
| bench_thread_pool          | 858 us                                                                 | 864 us: 1.01x slower                                       |
| json_loads                 | 26.7 us                                                                | 26.9 us: 1.01x slower                                      |
| sqlalchemy_declarative     | 128 ms                                                                 | 129 ms: 1.01x slower                                       |
| nqueens                    | 78.9 ms                                                                | 79.5 ms: 1.01x slower                                      |
| regex_compile              | 127 ms                                                                 | 128 ms: 1.01x slower                                       |
| async_tree_memoization_tg  | 308 ms                                                                 | 311 ms: 1.01x slower                                       |
| sqlglot_normalize          | 103 ms                                                                 | 104 ms: 1.01x slower                                       |
| nbody                      | 93.5 ms                                                                | 94.4 ms: 1.01x slower                                      |
| async_generators           | 419 ms                                                                 | 424 ms: 1.01x slower                                       |
| async_tree_io_tg           | 587 ms                                                                 | 595 ms: 1.01x slower                                       |
| comprehensions             | 16.4 us                                                                | 16.6 us: 1.01x slower                                      |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.7 ms: 1.02x slower                                      |
| scimark_sor                | 121 ms                                                                 | 123 ms: 1.02x slower                                       |
| generators                 | 27.2 ms                                                                | 27.7 ms: 1.02x slower                                      |
| genshi_text                | 21.8 ms                                                                | 22.2 ms: 1.02x slower                                      |
| django_template            | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                      |
| sqlglot_transpile          | 1.56 ms                                                                | 1.59 ms: 1.02x slower                                      |
| mdp                        | 2.50 sec                                                               | 2.55 sec: 1.02x slower                                     |
| json                       | 4.87 ms                                                                | 4.97 ms: 1.02x slower                                      |
| sqlglot_parse              | 1.25 ms                                                                | 1.28 ms: 1.02x slower                                      |
| scimark_lu                 | 113 ms                                                                 | 115 ms: 1.02x slower                                       |
| scimark_fft                | 343 ms                                                                 | 351 ms: 1.02x slower                                       |
| pyflate                    | 443 ms                                                                 | 454 ms: 1.02x slower                                       |
| typing_runtime_protocols   | 163 us                                                                 | 168 us: 1.03x slower                                       |
| deepcopy                   | 260 us                                                                 | 268 us: 1.03x slower                                       |
| deepcopy_memo              | 30.4 us                                                                | 31.4 us: 1.03x slower                                      |
| scimark_sparse_mat_mult    | 4.51 ms                                                                | 4.68 ms: 1.04x slower                                      |
| deepcopy_reduce            | 2.64 us                                                                | 2.75 us: 1.04x slower                                      |
| tomli_loads                | 1.92 sec                                                               | 1.99 sec: 1.04x slower                                     |
| spectral_norm              | 103 ms                                                                 | 109 ms: 1.05x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (27): sympy_str, json_dumps, logging_silent, sympy_expand, shortest_path, float, async_tree_memoization, html5lib, bench_mp_pool, many_optionals, xml_etree_iterparse, k_core, pylint, connected_components, docutils, coverage, xml_etree_parse, asyncio_websockets, richards, logging_simple, async_tree_none_tg, sphinx, regex_effbot, hexiom, telco, async_tree_none, async_tree_io

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 70.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x