# Results vs. base

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.013x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                            | 310 ms: 1.03x slower                                                                                                  |
| docutils       | 2.97 sec                                                                                                          | 3.12 sec: 1.05x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization | 459 ms                                                                                                            | 466 ms: 1.02x slower                                                                                                  |
| async_tree_io          | 866 ms                                                                                                            | 883 ms: 1.02x slower                                                                                                  |
| async_tree_none        | 381 ms                                                                                                            | 392 ms: 1.03x slower                                                                                                  |
| async_generators       | 453 ms                                                                                                            | 478 ms: 1.06x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (9): asyncio_websockets, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 85.6 ms                                                                                                           | 82.5 ms: 1.04x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                                                            | 216 ms: 1.04x faster                                                                                                  |
| regex_effbot   | 3.83 ms                                                                                                           | 3.77 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 265 us                                                                                                            | 251 us: 1.06x faster                                                                                                  |
| tomli_loads          | 2.44 sec                                                                                                          | 2.32 sec: 1.05x faster                                                                                                |
| xml_etree_parse      | 180 ms                                                                                                            | 177 ms: 1.02x faster                                                                                                  |
| xml_etree_iterparse  | 142 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| json_dumps           | 13.5 ms                                                                                                           | 13.8 ms: 1.02x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (9): xml_etree_process, xml_etree_generate, unpickle_list, pickle, pickle_list, json_loads, pickle_pure_python, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 8.54 ms                                                                                                           | 8.69 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.7 ms                                                                                                           | 12.9 ms: 1.07x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json | results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 2.17 sec                                                                                                          | 1.27 sec: 1.71x faster                                                                                                |
| richards                 | 53.2 ms                                                                                                           | 44.3 ms: 1.20x faster                                                                                                 |
| richards_super           | 59.0 ms                                                                                                           | 50.8 ms: 1.16x faster                                                                                                 |
| mako                     | 13.7 ms                                                                                                           | 12.9 ms: 1.07x faster                                                                                                 |
| spectral_norm            | 123 ms                                                                                                            | 116 ms: 1.06x faster                                                                                                  |
| unpickle_pure_python     | 265 us                                                                                                            | 251 us: 1.06x faster                                                                                                  |
| tomli_loads              | 2.44 sec                                                                                                          | 2.32 sec: 1.05x faster                                                                                                |
| deltablue                | 3.99 ms                                                                                                           | 3.83 ms: 1.04x faster                                                                                                 |
| scimark_fft              | 424 ms                                                                                                            | 408 ms: 1.04x faster                                                                                                  |
| float                    | 85.6 ms                                                                                                           | 82.5 ms: 1.04x faster                                                                                                 |
| regex_dna                | 223 ms                                                                                                            | 216 ms: 1.04x faster                                                                                                  |
| bpe_tokeniser            | 5.51 sec                                                                                                          | 5.37 sec: 1.03x faster                                                                                                |
| xml_etree_parse          | 180 ms                                                                                                            | 177 ms: 1.02x faster                                                                                                  |
| regex_effbot             | 3.83 ms                                                                                                           | 3.77 ms: 1.02x faster                                                                                                 |
| deepcopy                 | 325 us                                                                                                            | 321 us: 1.01x faster                                                                                                  |
| deepcopy_reduce          | 3.56 us                                                                                                           | 3.52 us: 1.01x faster                                                                                                 |
| coverage                 | 102 ms                                                                                                            | 103 ms: 1.01x slower                                                                                                  |
| connected_components     | 557 ms                                                                                                            | 561 ms: 1.01x slower                                                                                                  |
| xml_etree_iterparse      | 142 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| python_startup           | 15.0 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| logging_simple           | 6.86 us                                                                                                           | 6.95 us: 1.01x slower                                                                                                 |
| async_tree_memoization   | 459 ms                                                                                                            | 466 ms: 1.02x slower                                                                                                  |
| python_startup_no_site   | 8.54 ms                                                                                                           | 8.69 ms: 1.02x slower                                                                                                 |
| async_tree_io            | 866 ms                                                                                                            | 883 ms: 1.02x slower                                                                                                  |
| shortest_path            | 581 ms                                                                                                            | 593 ms: 1.02x slower                                                                                                  |
| k_core                   | 2.82 sec                                                                                                          | 2.88 sec: 1.02x slower                                                                                                |
| json_dumps               | 13.5 ms                                                                                                           | 13.8 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_normalize     | 125 ms                                                                                                            | 128 ms: 1.02x slower                                                                                                  |
| 2to3                     | 301 ms                                                                                                            | 310 ms: 1.03x slower                                                                                                  |
| async_tree_none          | 381 ms                                                                                                            | 392 ms: 1.03x slower                                                                                                  |
| sqlglot_v2_optimize      | 60.6 ms                                                                                                           | 62.6 ms: 1.03x slower                                                                                                 |
| sympy_expand             | 476 ms                                                                                                            | 494 ms: 1.04x slower                                                                                                  |
| pylint                   | 316 ms                                                                                                            | 328 ms: 1.04x slower                                                                                                  |
| many_optionals           | 924 us                                                                                                            | 964 us: 1.04x slower                                                                                                  |
| sympy_integrate          | 19.9 ms                                                                                                           | 20.8 ms: 1.04x slower                                                                                                 |
| dulwich_log              | 51.3 ms                                                                                                           | 53.7 ms: 1.05x slower                                                                                                 |
| pyflate                  | 527 ms                                                                                                            | 553 ms: 1.05x slower                                                                                                  |
| docutils                 | 2.97 sec                                                                                                          | 3.12 sec: 1.05x slower                                                                                                |
| sqlglot_v2_transpile     | 1.75 ms                                                                                                           | 1.84 ms: 1.05x slower                                                                                                 |
| create_gc_cycles         | 3.76 ms                                                                                                           | 3.96 ms: 1.05x slower                                                                                                 |
| async_generators         | 453 ms                                                                                                            | 478 ms: 1.06x slower                                                                                                  |
| typing_runtime_protocols | 194 us                                                                                                            | 205 us: 1.06x slower                                                                                                  |
| sqlglot_v2_parse         | 1.42 ms                                                                                                           | 1.51 ms: 1.06x slower                                                                                                 |
| pycparser                | 1.25 sec                                                                                                          | 1.33 sec: 1.07x slower                                                                                                |
| scimark_monte_carlo      | 78.8 ms                                                                                                           | 84.3 ms: 1.07x slower                                                                                                 |
| comprehensions           | 19.8 us                                                                                                           | 21.5 us: 1.09x slower                                                                                                 |
| hexiom                   | 6.81 ms                                                                                                           | 7.44 ms: 1.09x slower                                                                                                 |
| crypto_pyaes             | 83.6 ms                                                                                                           | 91.5 ms: 1.09x slower                                                                                                 |
| go                       | 126 ms                                                                                                            | 154 ms: 1.22x slower                                                                                                  |
| pprint_pformat           | 1.82 sec                                                                                                          | 2.29 sec: 1.26x slower                                                                                                |
| pprint_safe_repr         | 894 ms                                                                                                            | 1.13 sec: 1.26x slower                                                                                                |
| unpack_sequence          | 51.1 ns                                                                                                           | 71.4 ns: 1.40x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (51): scimark_lu, regex_v8, regex_compile, xml_etree_process, xml_etree_generate, genshi_text, subparsers, json, logging_silent, unpickle_list, deepcopy_memo, mdp, scimark_sparse_mat_mult, fannkuch, asyncio_websockets, async_tree_cpu_io_mixed, pickle, pidigits, pickle_list, djangocms, asyncio_tcp, django_template, logging_format, json_loads, gc_traversal, sqlite_synth, pickle_pure_python, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_none_tg, raytrace, bench_thread_pool, async_tree_memoization_tg, telco, scimark_sor, pickle_dict, sphinx, sympy_str, unpickle, async_tree_io_tg, sympy_sum, pathlib, thrift, meteor_contest, chaos, genshi_xml, nbody, generators, coroutines, html5lib, nqueens

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x