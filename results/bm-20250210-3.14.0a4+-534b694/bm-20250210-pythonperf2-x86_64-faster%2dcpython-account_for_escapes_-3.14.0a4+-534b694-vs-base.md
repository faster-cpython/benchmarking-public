# Results vs. base

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 534b694
- commit date: 2025-02-10
- overall geometric mean: 1.002x slower
- HPT reliability: 63.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| html5lib       | 67.5 ms                                                                      | 68.0 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                                       | 278 ms: 1.03x faster                                                                   |
| async_tree_none            | 295 ms                                                                       | 290 ms: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 515 ms                                                                       | 508 ms: 1.01x faster                                                                   |
| async_tree_memoization_tg  | 342 ms                                                                       | 338 ms: 1.01x faster                                                                   |
| async_tree_io              | 657 ms                                                                       | 649 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                                       | 521 ms: 1.01x faster                                                                   |
| async_tree_memoization     | 357 ms                                                                       | 354 ms: 1.01x faster                                                                   |
| coroutines                 | 21.1 ms                                                                      | 21.1 ms: 1.00x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                       | 90.8 ms: 1.11x faster                                                                  |
| pidigits       | 254 ms                                                                       | 255 ms: 1.00x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| regex_effbot   | 3.12 ms                                                                      | 3.15 ms: 1.01x slower                                                                  |
| regex_dna      | 237 ms                                                                       | 242 ms: 1.02x slower                                                                   |
| regex_v8       | 25.6 ms                                                                      | 26.6 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_generate   | 84.3 ms                                                                      | 83.7 ms: 1.01x faster                                                                  |
| xml_etree_iterparse  | 95.4 ms                                                                      | 94.8 ms: 1.01x faster                                                                  |
| xml_etree_process    | 59.6 ms                                                                      | 60.0 ms: 1.01x slower                                                                  |
| pickle_pure_python   | 327 us                                                                       | 330 us: 1.01x slower                                                                   |
| tomli_loads          | 2.06 sec                                                                     | 2.08 sec: 1.01x slower                                                                 |
| json_dumps           | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                                  |
| unpickle_pure_python | 207 us                                                                       | 212 us: 1.03x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                                      | 35.8 ms: 1.02x slower                                                                  |
| genshi_text     | 23.4 ms                                                                      | 23.9 ms: 1.02x slower                                                                  |
| mako            | 10.6 ms                                                                      | 11.0 ms: 1.04x slower                                                                  |
| genshi_xml      | 52.2 ms                                                                      | 55.4 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.03x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody                      | 101 ms                                                                       | 90.8 ms: 1.11x faster                                                                  |
| scimark_sparse_mat_mult    | 4.86 ms                                                                      | 4.56 ms: 1.06x faster                                                                  |
| pyflate                    | 445 ms                                                                       | 426 ms: 1.04x faster                                                                   |
| async_tree_none_tg         | 285 ms                                                                       | 278 ms: 1.03x faster                                                                   |
| scimark_sor                | 110 ms                                                                       | 108 ms: 1.03x faster                                                                   |
| telco                      | 7.95 ms                                                                      | 7.76 ms: 1.02x faster                                                                  |
| scimark_fft                | 313 ms                                                                       | 306 ms: 1.02x faster                                                                   |
| thrift                     | 858 us                                                                       | 841 us: 1.02x faster                                                                   |
| async_tree_none            | 295 ms                                                                       | 290 ms: 1.02x faster                                                                   |
| spectral_norm              | 85.1 ms                                                                      | 83.7 ms: 1.02x faster                                                                  |
| deepcopy_memo              | 29.5 us                                                                      | 29.1 us: 1.01x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 515 ms                                                                       | 508 ms: 1.01x faster                                                                   |
| pycparser                  | 1.24 sec                                                                     | 1.23 sec: 1.01x faster                                                                 |
| scimark_lu                 | 95.7 ms                                                                      | 94.5 ms: 1.01x faster                                                                  |
| async_tree_memoization_tg  | 342 ms                                                                       | 338 ms: 1.01x faster                                                                   |
| async_tree_io              | 657 ms                                                                       | 649 ms: 1.01x faster                                                                   |
| meteor_contest             | 125 ms                                                                       | 123 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                                       | 521 ms: 1.01x faster                                                                   |
| logging_silent             | 97.7 ns                                                                      | 96.9 ns: 1.01x faster                                                                  |
| richards                   | 45.8 ms                                                                      | 45.4 ms: 1.01x faster                                                                  |
| async_tree_memoization     | 357 ms                                                                       | 354 ms: 1.01x faster                                                                   |
| xml_etree_generate         | 84.3 ms                                                                      | 83.7 ms: 1.01x faster                                                                  |
| xml_etree_iterparse        | 95.4 ms                                                                      | 94.8 ms: 1.01x faster                                                                  |
| sqlalchemy_declarative     | 143 ms                                                                       | 142 ms: 1.01x faster                                                                   |
| sqlalchemy_imperative      | 17.8 ms                                                                      | 17.7 ms: 1.01x faster                                                                  |
| pprint_pformat             | 1.61 sec                                                                     | 1.60 sec: 1.00x faster                                                                 |
| sympy_integrate            | 23.1 ms                                                                      | 23.0 ms: 1.00x faster                                                                  |
| pathlib                    | 16.3 ms                                                                      | 16.3 ms: 1.00x faster                                                                  |
| bpe_tokeniser              | 4.56 sec                                                                     | 4.55 sec: 1.00x faster                                                                 |
| coroutines                 | 21.1 ms                                                                      | 21.1 ms: 1.00x slower                                                                  |
| connected_components       | 414 ms                                                                       | 416 ms: 1.00x slower                                                                   |
| pidigits                   | 254 ms                                                                       | 255 ms: 1.00x slower                                                                   |
| dulwich_log                | 66.6 ms                                                                      | 67.0 ms: 1.01x slower                                                                  |
| xml_etree_process          | 59.6 ms                                                                      | 60.0 ms: 1.01x slower                                                                  |
| shortest_path              | 443 ms                                                                       | 446 ms: 1.01x slower                                                                   |
| sympy_str                  | 287 ms                                                                       | 290 ms: 1.01x slower                                                                   |
| html5lib                   | 67.5 ms                                                                      | 68.0 ms: 1.01x slower                                                                  |
| pickle_pure_python         | 327 us                                                                       | 330 us: 1.01x slower                                                                   |
| fannkuch                   | 362 ms                                                                       | 365 ms: 1.01x slower                                                                   |
| regex_compile              | 134 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| regex_effbot               | 3.12 ms                                                                      | 3.15 ms: 1.01x slower                                                                  |
| sqlglot_optimize           | 56.8 ms                                                                      | 57.3 ms: 1.01x slower                                                                  |
| coverage                   | 78.0 ms                                                                      | 78.8 ms: 1.01x slower                                                                  |
| subparsers                 | 22.6 ms                                                                      | 22.8 ms: 1.01x slower                                                                  |
| 2to3                       | 281 ms                                                                       | 283 ms: 1.01x slower                                                                   |
| logging_simple             | 6.19 us                                                                      | 6.26 us: 1.01x slower                                                                  |
| many_optionals             | 995 us                                                                       | 1.01 ms: 1.01x slower                                                                  |
| deepcopy_reduce            | 2.89 us                                                                      | 2.92 us: 1.01x slower                                                                  |
| sympy_expand               | 488 ms                                                                       | 494 ms: 1.01x slower                                                                   |
| tomli_loads                | 2.06 sec                                                                     | 2.08 sec: 1.01x slower                                                                 |
| typing_runtime_protocols   | 167 us                                                                       | 169 us: 1.01x slower                                                                   |
| sqlglot_normalize          | 115 ms                                                                       | 116 ms: 1.01x slower                                                                   |
| create_gc_cycles           | 2.73 ms                                                                      | 2.77 ms: 1.02x slower                                                                  |
| hexiom                     | 6.07 ms                                                                      | 6.16 ms: 1.02x slower                                                                  |
| json_dumps                 | 11.5 ms                                                                      | 11.7 ms: 1.02x slower                                                                  |
| django_template            | 35.2 ms                                                                      | 35.8 ms: 1.02x slower                                                                  |
| sqlglot_transpile          | 1.72 ms                                                                      | 1.75 ms: 1.02x slower                                                                  |
| genshi_text                | 23.4 ms                                                                      | 23.9 ms: 1.02x slower                                                                  |
| logging_format             | 6.78 us                                                                      | 6.93 us: 1.02x slower                                                                  |
| sqlglot_parse              | 1.33 ms                                                                      | 1.36 ms: 1.02x slower                                                                  |
| regex_dna                  | 237 ms                                                                       | 242 ms: 1.02x slower                                                                   |
| unpickle_pure_python       | 207 us                                                                       | 212 us: 1.03x slower                                                                   |
| nqueens                    | 87.1 ms                                                                      | 89.6 ms: 1.03x slower                                                                  |
| crypto_pyaes               | 71.7 ms                                                                      | 73.9 ms: 1.03x slower                                                                  |
| mako                       | 10.6 ms                                                                      | 11.0 ms: 1.04x slower                                                                  |
| regex_v8                   | 25.6 ms                                                                      | 26.6 ms: 1.04x slower                                                                  |
| scimark_monte_carlo        | 60.8 ms                                                                      | 63.3 ms: 1.04x slower                                                                  |
| generators                 | 28.0 ms                                                                      | 29.3 ms: 1.04x slower                                                                  |
| genshi_xml                 | 52.2 ms                                                                      | 55.4 ms: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (27): pylint, pprint_safe_repr, chaos, richards_super, k_core, xml_etree_parse, raytrace, gc_traversal, async_tree_io_tg, deepcopy, sqlite_synth, python_startup, docutils, deltablue, go, python_startup_no_site, mdp, asyncio_websockets, json, sympy_sum, json_loads, comprehensions, async_generators, sphinx, float, bench_thread_pool, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 63.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x