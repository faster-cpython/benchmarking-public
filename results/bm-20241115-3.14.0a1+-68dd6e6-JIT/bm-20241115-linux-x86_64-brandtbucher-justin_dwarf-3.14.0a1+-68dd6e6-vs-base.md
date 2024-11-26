# Results vs. base

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 68dd6e6
- commit date: 2024-11-15
- overall geometric mean: 1.004x faster
- HPT reliability: 99.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 282 ms: 1.01x slower                                                 |
| html5lib       | 67.0 ms                                                                | 67.6 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.7 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 581 ms                                                                 | 566 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 553 ms: 1.02x faster                                                 |
| async_generators           | 456 ms                                                                 | 458 ms: 1.00x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                 |
| nbody          | 82.3 ms                                                                | 83.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.58 ms: 1.05x faster                                                |
| regex_dna      | 216 ms                                                                 | 210 ms: 1.03x faster                                                 |
| regex_v8       | 24.6 ms                                                                | 25.3 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads        | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                               |
| json_dumps         | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                |
| json_loads         | 26.8 us                                                                | 26.5 us: 1.01x faster                                                |
| pickle_pure_python | 321 us                                                                 | 318 us: 1.01x faster                                                 |
| xml_etree_generate | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                                |
| Geometric mean     | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (4): xml_etree_process, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.13 ms: 1.00x faster                                                |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.3 ms                                                                | 33.7 ms: 1.02x faster                                                |
| genshi_xml      | 59.9 ms                                                                | 59.0 ms: 1.02x faster                                                |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                                |
| genshi_text     | 25.1 ms                                                                | 24.8 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot               | 3.77 ms                                                                | 3.58 ms: 1.05x faster                                                |
| richards_super             | 47.1 ms                                                                | 44.9 ms: 1.05x faster                                                |
| logging_silent             | 102 ns                                                                 | 97.3 ns: 1.05x faster                                                |
| pprint_pformat             | 1.51 sec                                                               | 1.45 sec: 1.04x faster                                               |
| spectral_norm              | 115 ms                                                                 | 111 ms: 1.03x faster                                                 |
| raytrace                   | 283 ms                                                                 | 274 ms: 1.03x faster                                                 |
| regex_dna                  | 216 ms                                                                 | 210 ms: 1.03x faster                                                 |
| tomli_loads                | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                               |
| coroutines                 | 23.2 ms                                                                | 22.7 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 581 ms                                                                 | 566 ms: 1.03x faster                                                 |
| richards                   | 40.7 ms                                                                | 39.8 ms: 1.02x faster                                                |
| typing_runtime_protocols   | 170 us                                                                 | 166 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 553 ms: 1.02x faster                                                 |
| generators                 | 36.6 ms                                                                | 35.9 ms: 1.02x faster                                                |
| json_dumps                 | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                |
| logging_format             | 6.17 us                                                                | 6.06 us: 1.02x faster                                                |
| pprint_safe_repr           | 724 ms                                                                 | 711 ms: 1.02x faster                                                 |
| mdp                        | 2.62 sec                                                               | 2.57 sec: 1.02x faster                                               |
| django_template            | 34.3 ms                                                                | 33.7 ms: 1.02x faster                                                |
| genshi_xml                 | 59.9 ms                                                                | 59.0 ms: 1.02x faster                                                |
| logging_simple             | 5.56 us                                                                | 5.48 us: 1.02x faster                                                |
| fannkuch                   | 389 ms                                                                 | 383 ms: 1.02x faster                                                 |
| mako                       | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                                |
| deltablue                  | 3.31 ms                                                                | 3.28 ms: 1.01x faster                                                |
| json_loads                 | 26.8 us                                                                | 26.5 us: 1.01x faster                                                |
| genshi_text                | 25.1 ms                                                                | 24.8 ms: 1.01x faster                                                |
| subparsers                 | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                |
| pickle_pure_python         | 321 us                                                                 | 318 us: 1.01x faster                                                 |
| meteor_contest             | 109 ms                                                                 | 108 ms: 1.01x faster                                                 |
| xml_etree_generate         | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 64.8 ms                                                                | 64.3 ms: 1.01x faster                                                |
| sqlite_synth               | 2.80 us                                                                | 2.79 us: 1.01x faster                                                |
| sympy_expand               | 509 ms                                                                 | 506 ms: 1.01x faster                                                 |
| create_gc_cycles           | 2.71 ms                                                                | 2.70 ms: 1.00x faster                                                |
| bpe_tokeniser              | 4.53 sec                                                               | 4.51 sec: 1.00x faster                                               |
| go                         | 133 ms                                                                 | 133 ms: 1.00x faster                                                 |
| shortest_path              | 482 ms                                                                 | 481 ms: 1.00x faster                                                 |
| connected_components       | 437 ms                                                                 | 436 ms: 1.00x faster                                                 |
| gc_traversal               | 4.74 ms                                                                | 4.73 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                 |
| python_startup_no_site     | 7.14 ms                                                                | 7.13 ms: 1.00x faster                                                |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| comprehensions             | 17.5 us                                                                | 17.6 us: 1.00x slower                                                |
| sqlglot_optimize           | 60.3 ms                                                                | 60.5 ms: 1.00x slower                                                |
| async_generators           | 456 ms                                                                 | 458 ms: 1.00x slower                                                 |
| bench_mp_pool              | 84.8 ms                                                                | 85.2 ms: 1.01x slower                                                |
| 2to3                       | 280 ms                                                                 | 282 ms: 1.01x slower                                                 |
| scimark_fft                | 318 ms                                                                 | 320 ms: 1.01x slower                                                 |
| dulwich_log                | 67.7 ms                                                                | 68.2 ms: 1.01x slower                                                |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                 |
| html5lib                   | 67.0 ms                                                                | 67.6 ms: 1.01x slower                                                |
| nqueens                    | 87.9 ms                                                                | 88.7 ms: 1.01x slower                                                |
| nbody                      | 82.3 ms                                                                | 83.2 ms: 1.01x slower                                                |
| sqlglot_normalize          | 114 ms                                                                 | 116 ms: 1.01x slower                                                 |
| scimark_lu                 | 113 ms                                                                 | 115 ms: 1.01x slower                                                 |
| pyflate                    | 449 ms                                                                 | 455 ms: 1.01x slower                                                 |
| pathlib                    | 16.1 ms                                                                | 16.3 ms: 1.02x slower                                                |
| thrift                     | 779 us                                                                 | 795 us: 1.02x slower                                                 |
| deepcopy_reduce            | 2.66 us                                                                | 2.72 us: 1.02x slower                                                |
| regex_v8                   | 24.6 ms                                                                | 25.3 ms: 1.03x slower                                                |
| pycparser                  | 1.16 sec                                                               | 1.20 sec: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.86 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (35): sqlalchemy_imperative, async_tree_memoization, async_tree_io, async_tree_none, coverage, chaos, telco, k_core, async_tree_none_tg, sphinx, deepcopy_memo, float, sympy_str, json, async_tree_io_tg, sqlglot_transpile, many_optionals, xml_etree_process, unpickle_pure_python, sqlalchemy_declarative, asyncio_websockets, bench_thread_pool, xml_etree_parse, xml_etree_iterparse, docutils, async_tree_memoization_tg, sqlglot_parse, sympy_sum, sympy_integrate, deepcopy, hexiom, djangocms, regex_compile, crypto_pyaes, pylint

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x