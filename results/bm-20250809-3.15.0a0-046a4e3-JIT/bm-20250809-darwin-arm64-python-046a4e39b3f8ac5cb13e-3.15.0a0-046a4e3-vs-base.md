# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.013x faster
- HPT reliability: 65.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                                                                        | 1.45 sec: 1.01x slower                                                                                              |
| html5lib       | 33.0 ms                                                                                                         | 33.5 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_io          | 382 ms                                                                                                          | 377 ms: 1.01x faster                                                                                                |
| async_tree_eager       | 65.1 ms                                                                                                         | 64.4 ms: 1.01x faster                                                                                               |
| async_tree_memoization | 197 ms                                                                                                          | 195 ms: 1.01x faster                                                                                                |
| coroutines             | 16.4 ms                                                                                                         | 16.6 ms: 1.01x slower                                                                                               |
| async_generators       | 279 ms                                                                                                          | 285 ms: 1.02x slower                                                                                                |
| Geometric mean         | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (16): asyncio_tcp, async_tree_none, asyncio_tcp_ssl, async_tree_none_tg, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_io_tg, async_tree_eager_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 81.3 ms                                                                                                         | 72.4 ms: 1.12x faster                                                                                               |
| pidigits       | 284 ms                                                                                                          | 285 ms: 1.00x slower                                                                                                |
| float          | 50.6 ms                                                                                                         | 51.1 ms: 1.01x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.15 ms                                                                                                         | 2.13 ms: 1.01x faster                                                                                               |
| regex_compile  | 73.1 ms                                                                                                         | 72.7 ms: 1.01x faster                                                                                               |
| regex_dna      | 138 ms                                                                                                          | 138 ms: 1.00x slower                                                                                                |
| regex_v8       | 15.3 ms                                                                                                         | 15.5 ms: 1.01x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 158 us                                                                                                          | 128 us: 1.23x faster                                                                                                |
| tomli_loads          | 1.44 sec                                                                                                        | 1.24 sec: 1.16x faster                                                                                              |
| xml_etree_process    | 39.7 ms                                                                                                         | 34.6 ms: 1.15x faster                                                                                               |
| xml_etree_generate   | 55.6 ms                                                                                                         | 49.3 ms: 1.13x faster                                                                                               |
| pickle_pure_python   | 219 us                                                                                                          | 209 us: 1.04x faster                                                                                                |
| xml_etree_parse      | 101 ms                                                                                                          | 100 ms: 1.01x faster                                                                                                |
| pickle_list          | 3.04 us                                                                                                         | 3.05 us: 1.01x slower                                                                                               |
| unpickle             | 9.01 us                                                                                                         | 9.07 us: 1.01x slower                                                                                               |
| json_dumps           | 5.77 ms                                                                                                         | 5.81 ms: 1.01x slower                                                                                               |
| pickle_dict          | 17.6 us                                                                                                         | 17.8 us: 1.01x slower                                                                                               |
| pickle               | 7.61 us                                                                                                         | 7.70 us: 1.01x slower                                                                                               |
| json_loads           | 17.1 us                                                                                                         | 17.5 us: 1.02x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 17.6 ms                                                                                                         | 18.0 ms: 1.02x slower                                                                                               |
| python_startup_no_site | 13.3 ms                                                                                                         | 13.6 ms: 1.02x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.95 ms                                                                                                         | 6.53 ms: 1.22x faster                                                                                               |
| django_template | 23.0 ms                                                                                                         | 23.1 ms: 1.00x slower                                                                                               |
| genshi_xml      | 32.7 ms                                                                                                         | 33.0 ms: 1.01x slower                                                                                               |
| genshi_text     | 15.2 ms                                                                                                         | 15.4 ms: 1.02x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.04x faster                                                                                                        |

All benchmarks:
===============

| Benchmark               | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python    | 158 us                                                                                                          | 128 us: 1.23x faster                                                                                                |
| mako                    | 7.95 ms                                                                                                         | 6.53 ms: 1.22x faster                                                                                               |
| pprint_pformat          | 1.10 sec                                                                                                        | 901 ms: 1.22x faster                                                                                                |
| pprint_safe_repr        | 540 ms                                                                                                          | 448 ms: 1.20x faster                                                                                                |
| fannkuch                | 293 ms                                                                                                          | 249 ms: 1.18x faster                                                                                                |
| tomli_loads             | 1.44 sec                                                                                                        | 1.24 sec: 1.16x faster                                                                                              |
| xml_etree_process       | 39.7 ms                                                                                                         | 34.6 ms: 1.15x faster                                                                                               |
| xml_etree_generate      | 55.6 ms                                                                                                         | 49.3 ms: 1.13x faster                                                                                               |
| nbody                   | 81.3 ms                                                                                                         | 72.4 ms: 1.12x faster                                                                                               |
| bpe_tokeniser           | 3.19 sec                                                                                                        | 2.93 sec: 1.09x faster                                                                                              |
| crypto_pyaes            | 52.7 ms                                                                                                         | 49.7 ms: 1.06x faster                                                                                               |
| pyflate                 | 306 ms                                                                                                          | 289 ms: 1.06x faster                                                                                                |
| sqlglot_v2_parse        | 829 us                                                                                                          | 789 us: 1.05x faster                                                                                                |
| pickle_pure_python      | 219 us                                                                                                          | 209 us: 1.04x faster                                                                                                |
| sqlite_synth            | 1.64 us                                                                                                         | 1.58 us: 1.03x faster                                                                                               |
| meteor_contest          | 74.0 ms                                                                                                         | 71.7 ms: 1.03x faster                                                                                               |
| sqlglot_v2_transpile    | 1.00 ms                                                                                                         | 973 us: 1.03x faster                                                                                                |
| comprehensions          | 11.7 us                                                                                                         | 11.4 us: 1.03x faster                                                                                               |
| telco                   | 4.58 ms                                                                                                         | 4.47 ms: 1.03x faster                                                                                               |
| xml_etree_parse         | 101 ms                                                                                                          | 100 ms: 1.01x faster                                                                                                |
| async_tree_io           | 382 ms                                                                                                          | 377 ms: 1.01x faster                                                                                                |
| async_tree_eager        | 65.1 ms                                                                                                         | 64.4 ms: 1.01x faster                                                                                               |
| async_tree_memoization  | 197 ms                                                                                                          | 195 ms: 1.01x faster                                                                                                |
| bench_thread_pool       | 502 us                                                                                                          | 498 us: 1.01x faster                                                                                                |
| richards_super          | 37.8 ms                                                                                                         | 37.5 ms: 1.01x faster                                                                                               |
| regex_effbot            | 2.15 ms                                                                                                         | 2.13 ms: 1.01x faster                                                                                               |
| regex_compile           | 73.1 ms                                                                                                         | 72.7 ms: 1.01x faster                                                                                               |
| sympy_sum               | 77.2 ms                                                                                                         | 76.9 ms: 1.00x faster                                                                                               |
| deepcopy_memo           | 21.7 us                                                                                                         | 21.6 us: 1.00x faster                                                                                               |
| chaos                   | 39.3 ms                                                                                                         | 39.2 ms: 1.00x faster                                                                                               |
| raytrace                | 178 ms                                                                                                          | 177 ms: 1.00x faster                                                                                                |
| hexiom                  | 4.64 ms                                                                                                         | 4.65 ms: 1.00x slower                                                                                               |
| regex_dna               | 138 ms                                                                                                          | 138 ms: 1.00x slower                                                                                                |
| django_template         | 23.0 ms                                                                                                         | 23.1 ms: 1.00x slower                                                                                               |
| generators              | 24.3 ms                                                                                                         | 24.4 ms: 1.00x slower                                                                                               |
| pidigits                | 284 ms                                                                                                          | 285 ms: 1.00x slower                                                                                                |
| logging_simple          | 3.36 us                                                                                                         | 3.37 us: 1.00x slower                                                                                               |
| sympy_expand            | 247 ms                                                                                                          | 248 ms: 1.00x slower                                                                                                |
| sqlglot_v2_optimize     | 33.7 ms                                                                                                         | 33.9 ms: 1.01x slower                                                                                               |
| deepcopy_reduce         | 1.77 us                                                                                                         | 1.78 us: 1.01x slower                                                                                               |
| pickle_list             | 3.04 us                                                                                                         | 3.05 us: 1.01x slower                                                                                               |
| sympy_str               | 146 ms                                                                                                          | 147 ms: 1.01x slower                                                                                                |
| logging_format          | 3.63 us                                                                                                         | 3.65 us: 1.01x slower                                                                                               |
| many_optionals          | 593 us                                                                                                          | 598 us: 1.01x slower                                                                                                |
| unpickle                | 9.01 us                                                                                                         | 9.07 us: 1.01x slower                                                                                               |
| scimark_monte_carlo     | 45.3 ms                                                                                                         | 45.6 ms: 1.01x slower                                                                                               |
| json_dumps              | 5.77 ms                                                                                                         | 5.81 ms: 1.01x slower                                                                                               |
| genshi_xml              | 32.7 ms                                                                                                         | 33.0 ms: 1.01x slower                                                                                               |
| sympy_integrate         | 10.8 ms                                                                                                         | 10.9 ms: 1.01x slower                                                                                               |
| float                   | 50.6 ms                                                                                                         | 51.1 ms: 1.01x slower                                                                                               |
| regex_v8                | 15.3 ms                                                                                                         | 15.5 ms: 1.01x slower                                                                                               |
| pickle_dict             | 17.6 us                                                                                                         | 17.8 us: 1.01x slower                                                                                               |
| docutils                | 1.44 sec                                                                                                        | 1.45 sec: 1.01x slower                                                                                              |
| pickle                  | 7.61 us                                                                                                         | 7.70 us: 1.01x slower                                                                                               |
| pycparser               | 694 ms                                                                                                          | 703 ms: 1.01x slower                                                                                                |
| nqueens                 | 61.4 ms                                                                                                         | 62.2 ms: 1.01x slower                                                                                               |
| coroutines              | 16.4 ms                                                                                                         | 16.6 ms: 1.01x slower                                                                                               |
| go                      | 86.1 ms                                                                                                         | 87.4 ms: 1.01x slower                                                                                               |
| dulwich_log             | 25.0 ms                                                                                                         | 25.4 ms: 1.01x slower                                                                                               |
| genshi_text             | 15.2 ms                                                                                                         | 15.4 ms: 1.02x slower                                                                                               |
| scimark_lu              | 75.9 ms                                                                                                         | 77.1 ms: 1.02x slower                                                                                               |
| html5lib                | 33.0 ms                                                                                                         | 33.5 ms: 1.02x slower                                                                                               |
| async_generators        | 279 ms                                                                                                          | 285 ms: 1.02x slower                                                                                                |
| json_loads              | 17.1 us                                                                                                         | 17.5 us: 1.02x slower                                                                                               |
| spectral_norm           | 62.8 ms                                                                                                         | 64.3 ms: 1.02x slower                                                                                               |
| python_startup          | 17.6 ms                                                                                                         | 18.0 ms: 1.02x slower                                                                                               |
| python_startup_no_site  | 13.3 ms                                                                                                         | 13.6 ms: 1.02x slower                                                                                               |
| json                    | 2.99 ms                                                                                                         | 3.07 ms: 1.03x slower                                                                                               |
| scimark_fft             | 188 ms                                                                                                          | 194 ms: 1.03x slower                                                                                                |
| coverage                | 46.4 ms                                                                                                         | 48.0 ms: 1.03x slower                                                                                               |
| shortest_path           | 336 ms                                                                                                          | 350 ms: 1.04x slower                                                                                                |
| deltablue               | 2.44 ms                                                                                                         | 2.55 ms: 1.04x slower                                                                                               |
| k_core                  | 1.53 sec                                                                                                        | 1.60 sec: 1.05x slower                                                                                              |
| connected_components    | 306 ms                                                                                                          | 322 ms: 1.05x slower                                                                                                |
| pathlib                 | 24.2 ms                                                                                                         | 25.8 ms: 1.07x slower                                                                                               |
| scimark_sparse_mat_mult | 3.14 ms                                                                                                         | 3.42 ms: 1.09x slower                                                                                               |
| unpack_sequence         | 38.8 ns                                                                                                         | 46.7 ns: 1.20x slower                                                                                               |
| Geometric mean          | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (34): asyncio_tcp, async_tree_none, asyncio_tcp_ssl, async_tree_none_tg, gc_traversal, async_tree_eager_tg, create_gc_cycles, xml_etree_iterparse, typing_runtime_protocols, sqlglot_v2_normalize, async_tree_cpu_io_mixed, deepcopy, async_tree_eager_cpu_io_mixed, async_tree_io_tg, 2to3, async_tree_eager_memoization, asyncio_websockets, logging_silent, async_tree_cpu_io_mixed_tg, richards, async_tree_memoization_tg, sphinx, async_tree_eager_io, mdp, scimark_sor, unpickle_list, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, subparsers, async_tree_eager_io_tg, dask, pylint, thrift, bench_mp_pool

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 65.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x