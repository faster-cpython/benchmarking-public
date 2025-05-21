# Results vs. base

- fork: brandtbucher
- ref: cached_attributes
- machine: linux-x86_64
- commit hash: 0e20c44
- commit date: 2025-05-21
- overall geometric mean: 1.003x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed          | 508 ms                                                                | 489 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 473 ms                                                                | 456 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 401 ms                                                                | 387 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 500 ms                                                                | 483 ms: 1.04x faster                                                     |
| coroutines                       | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                    |
| async_tree_eager_memoization_tg  | 279 ms                                                                | 276 ms: 1.01x faster                                                     |
| async_generators                 | 426 ms                                                                | 428 ms: 1.00x slower                                                     |
| Geometric mean                   | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_eager_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_eager_io_tg, async_tree_eager, asyncio_websockets, async_tree_eager_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 187 ms: 1.02x faster                                                     |
| nbody          | 92.5 ms                                                               | 92.9 ms: 1.00x slower                                                    |
| float          | 63.3 ms                                                               | 64.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                    |
| regex_effbot   | 3.12 ms                                                               | 3.08 ms: 1.01x faster                                                    |
| regex_dna      | 202 ms                                                                | 203 ms: 1.00x slower                                                     |
| regex_compile  | 128 ms                                                                | 129 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                              | 1.88 sec: 1.02x faster                                                   |
| pickle_pure_python   | 328 us                                                                | 322 us: 1.02x faster                                                     |
| xml_etree_parse      | 140 ms                                                                | 139 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 98.3 ms                                                               | 97.4 ms: 1.01x faster                                                    |
| unpickle_pure_python | 205 us                                                                | 203 us: 1.01x faster                                                     |
| json_loads           | 30.0 us                                                               | 29.8 us: 1.00x faster                                                    |
| json_dumps           | 11.0 ms                                                               | 11.0 ms: 1.01x slower                                                    |
| xml_etree_generate   | 80.0 ms                                                               | 80.6 ms: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                               | 6.94 ms: 1.00x faster                                                    |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                    |
| genshi_xml      | 49.0 ms                                                               | 49.8 ms: 1.02x slower                                                    |
| django_template | 31.9 ms                                                               | 32.5 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| spectral_norm                    | 103 ms                                                                | 97.9 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed          | 508 ms                                                                | 489 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 473 ms                                                                | 456 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 401 ms                                                                | 387 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 500 ms                                                                | 483 ms: 1.04x faster                                                     |
| richards                         | 34.3 ms                                                               | 33.3 ms: 1.03x faster                                                    |
| deepcopy_reduce                  | 2.79 us                                                               | 2.71 us: 1.03x faster                                                    |
| connected_components             | 458 ms                                                                | 446 ms: 1.03x faster                                                     |
| pprint_pformat                   | 1.70 sec                                                              | 1.66 sec: 1.02x faster                                                   |
| pidigits                         | 191 ms                                                                | 187 ms: 1.02x faster                                                     |
| tomli_loads                      | 1.91 sec                                                              | 1.88 sec: 1.02x faster                                                   |
| pickle_pure_python               | 328 us                                                                | 322 us: 1.02x faster                                                     |
| coroutines                       | 24.7 ms                                                               | 24.2 ms: 1.02x faster                                                    |
| regex_v8                         | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                    |
| typing_runtime_protocols         | 176 us                                                                | 173 us: 1.02x faster                                                     |
| pathlib                          | 17.4 ms                                                               | 17.1 ms: 1.02x faster                                                    |
| logging_simple                   | 6.39 us                                                               | 6.28 us: 1.02x faster                                                    |
| shortest_path                    | 497 ms                                                                | 488 ms: 1.02x faster                                                     |
| scimark_monte_carlo              | 68.2 ms                                                               | 67.2 ms: 1.01x faster                                                    |
| xml_etree_parse                  | 140 ms                                                                | 139 ms: 1.01x faster                                                     |
| scimark_fft                      | 337 ms                                                                | 332 ms: 1.01x faster                                                     |
| dulwich_log                      | 62.0 ms                                                               | 61.2 ms: 1.01x faster                                                    |
| deepcopy_memo                    | 30.3 us                                                               | 29.9 us: 1.01x faster                                                    |
| comprehensions                   | 18.2 us                                                               | 18.0 us: 1.01x faster                                                    |
| regex_effbot                     | 3.12 ms                                                               | 3.08 ms: 1.01x faster                                                    |
| go                               | 127 ms                                                                | 125 ms: 1.01x faster                                                     |
| async_tree_eager_memoization_tg  | 279 ms                                                                | 276 ms: 1.01x faster                                                     |
| mako                             | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                    |
| deltablue                        | 3.10 ms                                                               | 3.08 ms: 1.01x faster                                                    |
| xml_etree_iterparse              | 98.3 ms                                                               | 97.4 ms: 1.01x faster                                                    |
| unpickle_pure_python             | 205 us                                                                | 203 us: 1.01x faster                                                     |
| logging_format                   | 7.14 us                                                               | 7.08 us: 1.01x faster                                                    |
| sympy_expand                     | 475 ms                                                                | 472 ms: 1.01x faster                                                     |
| gc_traversal                     | 4.97 ms                                                               | 4.93 ms: 1.01x faster                                                    |
| logging_silent                   | 472 ns                                                                | 469 ns: 1.01x faster                                                     |
| json_loads                       | 30.0 us                                                               | 29.8 us: 1.00x faster                                                    |
| sympy_integrate                  | 19.5 ms                                                               | 19.4 ms: 1.00x faster                                                    |
| create_gc_cycles                 | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                                    |
| python_startup_no_site           | 6.96 ms                                                               | 6.94 ms: 1.00x faster                                                    |
| python_startup                   | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                    |
| regex_dna                        | 202 ms                                                                | 203 ms: 1.00x slower                                                     |
| regex_compile                    | 128 ms                                                                | 129 ms: 1.00x slower                                                     |
| sqlglot_v2_optimize              | 52.9 ms                                                               | 53.1 ms: 1.00x slower                                                    |
| nbody                            | 92.5 ms                                                               | 92.9 ms: 1.00x slower                                                    |
| async_generators                 | 426 ms                                                                | 428 ms: 1.00x slower                                                     |
| hexiom                           | 6.57 ms                                                               | 6.60 ms: 1.00x slower                                                    |
| meteor_contest                   | 109 ms                                                                | 110 ms: 1.01x slower                                                     |
| json_dumps                       | 11.0 ms                                                               | 11.0 ms: 1.01x slower                                                    |
| xml_etree_generate               | 80.0 ms                                                               | 80.6 ms: 1.01x slower                                                    |
| coverage                         | 424 ms                                                                | 427 ms: 1.01x slower                                                     |
| fannkuch                         | 414 ms                                                                | 420 ms: 1.01x slower                                                     |
| float                            | 63.3 ms                                                               | 64.2 ms: 1.01x slower                                                    |
| genshi_xml                       | 49.0 ms                                                               | 49.8 ms: 1.02x slower                                                    |
| sqlite_synth                     | 2.76 us                                                               | 2.80 us: 1.02x slower                                                    |
| json                             | 5.28 ms                                                               | 5.37 ms: 1.02x slower                                                    |
| django_template                  | 31.9 ms                                                               | 32.5 ms: 1.02x slower                                                    |
| telco                            | 7.62 ms                                                               | 7.85 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult          | 4.94 ms                                                               | 5.16 ms: 1.04x slower                                                    |
| generators                       | 29.5 ms                                                               | 30.8 ms: 1.05x slower                                                    |
| pyflate                          | 422 ms                                                                | 448 ms: 1.06x slower                                                     |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (43): async_tree_io_tg, async_tree_eager_tg, async_tree_memoization_tg, pycparser, async_tree_none, async_tree_memoization, xml_etree_process, crypto_pyaes, async_tree_none_tg, many_optionals, scimark_sor, k_core, async_tree_io, sympy_sum, sphinx, sympy_str, sqlglot_v2_parse, thrift, dask, 2to3, async_tree_eager_io_tg, bench_mp_pool, docutils, async_tree_eager, asyncio_websockets, chaos, pylint, sqlglot_v2_transpile, bpe_tokeniser, nqueens, genshi_text, richards_super, subparsers, bench_thread_pool, deepcopy, mdp, raytrace, async_tree_eager_io, sqlglot_v2_normalize, scimark_lu, pprint_safe_repr, html5lib, async_tree_eager_memoization

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x