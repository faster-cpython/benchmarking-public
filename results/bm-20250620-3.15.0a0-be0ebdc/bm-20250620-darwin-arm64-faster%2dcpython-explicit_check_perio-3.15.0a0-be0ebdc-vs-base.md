# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.004x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 188 ms: 1.01x slower                                                            |
| docutils       | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed       | 432 ms                                                                | 433 ms: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 369 ms: 1.00x slower                                                            |
| async_tree_memoization        | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| async_tree_eager              | 72.8 ms                                                               | 73.6 ms: 1.01x slower                                                           |
| async_tree_none               | 182 ms                                                                | 185 ms: 1.02x slower                                                            |
| async_tree_io_tg              | 405 ms                                                                | 413 ms: 1.02x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (13): async_generators, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, coroutines, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                                           |
| nbody          | 85.0 ms                                                               | 85.3 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| regex_v8       | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| regex_compile  | 81.0 ms                                                               | 82.0 ms: 1.01x slower                                                           |
| regex_effbot   | 2.34 ms                                                               | 2.40 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 73.9 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| xml_etree_generate   | 58.7 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| tomli_loads          | 1.45 sec                                                              | 1.46 sec: 1.01x slower                                                          |
| json_dumps           | 6.76 ms                                                               | 6.82 ms: 1.01x slower                                                           |
| json_loads           | 16.5 us                                                               | 16.7 us: 1.01x slower                                                           |
| xml_etree_process    | 43.3 ms                                                               | 43.8 ms: 1.01x slower                                                           |
| unpickle_pure_python | 178 us                                                                | 180 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.5 ms                                                               | 13.2 ms: 1.03x faster                                                           |
| python_startup         | 17.8 ms                                                               | 17.6 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| mako            | 9.03 ms                                                               | 9.10 ms: 1.01x slower                                                           |
| django_template | 25.0 ms                                                               | 25.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site        | 13.5 ms                                                               | 13.2 ms: 1.03x faster                                                           |
| python_startup                | 17.8 ms                                                               | 17.6 ms: 1.01x faster                                                           |
| nqueens                       | 70.4 ms                                                               | 69.8 ms: 1.01x faster                                                           |
| telco                         | 4.78 ms                                                               | 4.74 ms: 1.01x faster                                                           |
| float                         | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                                           |
| generators                    | 31.7 ms                                                               | 31.5 ms: 1.01x faster                                                           |
| deepcopy                      | 176 us                                                                | 175 us: 1.00x faster                                                            |
| meteor_contest                | 74.6 ms                                                               | 74.5 ms: 1.00x faster                                                           |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed       | 432 ms                                                                | 433 ms: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 369 ms: 1.00x slower                                                            |
| sympy_integrate               | 11.3 ms                                                               | 11.4 ms: 1.00x slower                                                           |
| richards                      | 37.3 ms                                                               | 37.4 ms: 1.00x slower                                                           |
| dulwich_log                   | 26.4 ms                                                               | 26.5 ms: 1.00x slower                                                           |
| nbody                         | 85.0 ms                                                               | 85.3 ms: 1.00x slower                                                           |
| richards_super                | 41.6 ms                                                               | 41.7 ms: 1.00x slower                                                           |
| genshi_text                   | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| coverage                      | 49.2 ms                                                               | 49.4 ms: 1.00x slower                                                           |
| scimark_fft                   | 202 ms                                                                | 203 ms: 1.00x slower                                                            |
| logging_silent                | 343 ns                                                                | 344 ns: 1.00x slower                                                            |
| crypto_pyaes                  | 60.8 ms                                                               | 61.1 ms: 1.01x slower                                                           |
| go                            | 99.0 ms                                                               | 99.5 ms: 1.01x slower                                                           |
| chaos                         | 47.0 ms                                                               | 47.2 ms: 1.01x slower                                                           |
| mdp                           | 826 ms                                                                | 831 ms: 1.01x slower                                                            |
| async_tree_memoization        | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| sympy_str                     | 155 ms                                                                | 156 ms: 1.01x slower                                                            |
| deepcopy_reduce               | 1.90 us                                                               | 1.91 us: 1.01x slower                                                           |
| xml_etree_iterparse           | 73.9 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| shortest_path                 | 328 ms                                                                | 330 ms: 1.01x slower                                                            |
| create_gc_cycles              | 1.35 ms                                                               | 1.36 ms: 1.01x slower                                                           |
| connected_components          | 303 ms                                                                | 305 ms: 1.01x slower                                                            |
| sympy_expand                  | 262 ms                                                                | 264 ms: 1.01x slower                                                            |
| pyflate                       | 331 ms                                                                | 333 ms: 1.01x slower                                                            |
| docutils                      | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| xml_etree_generate            | 58.7 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| sqlite_synth                  | 1.61 us                                                               | 1.63 us: 1.01x slower                                                           |
| spectral_norm                 | 72.0 ms                                                               | 72.6 ms: 1.01x slower                                                           |
| sqlglot_v2_parse              | 985 us                                                                | 992 us: 1.01x slower                                                            |
| tomli_loads                   | 1.45 sec                                                              | 1.46 sec: 1.01x slower                                                          |
| scimark_monte_carlo           | 52.6 ms                                                               | 53.0 ms: 1.01x slower                                                           |
| pprint_pformat                | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                                          |
| sqlglot_v2_transpile          | 1.17 ms                                                               | 1.18 ms: 1.01x slower                                                           |
| mako                          | 9.03 ms                                                               | 9.10 ms: 1.01x slower                                                           |
| hexiom                        | 5.10 ms                                                               | 5.14 ms: 1.01x slower                                                           |
| json_dumps                    | 6.76 ms                                                               | 6.82 ms: 1.01x slower                                                           |
| sqlglot_v2_optimize           | 36.4 ms                                                               | 36.8 ms: 1.01x slower                                                           |
| regex_v8                      | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| deepcopy_memo                 | 21.8 us                                                               | 22.1 us: 1.01x slower                                                           |
| 2to3                          | 186 ms                                                                | 188 ms: 1.01x slower                                                            |
| json_loads                    | 16.5 us                                                               | 16.7 us: 1.01x slower                                                           |
| xml_etree_process             | 43.3 ms                                                               | 43.8 ms: 1.01x slower                                                           |
| async_tree_eager              | 72.8 ms                                                               | 73.6 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult       | 3.19 ms                                                               | 3.22 ms: 1.01x slower                                                           |
| deltablue                     | 2.80 ms                                                               | 2.83 ms: 1.01x slower                                                           |
| many_optionals                | 494 us                                                                | 499 us: 1.01x slower                                                            |
| unpickle_pure_python          | 178 us                                                                | 180 us: 1.01x slower                                                            |
| regex_compile                 | 81.0 ms                                                               | 82.0 ms: 1.01x slower                                                           |
| sqlglot_v2_normalize          | 76.1 ms                                                               | 77.1 ms: 1.01x slower                                                           |
| bpe_tokeniser                 | 3.24 sec                                                              | 3.29 sec: 1.01x slower                                                          |
| pprint_safe_repr              | 621 ms                                                                | 630 ms: 1.01x slower                                                            |
| async_tree_none               | 182 ms                                                                | 185 ms: 1.02x slower                                                            |
| scimark_lu                    | 84.2 ms                                                               | 85.6 ms: 1.02x slower                                                           |
| django_template               | 25.0 ms                                                               | 25.5 ms: 1.02x slower                                                           |
| async_tree_io_tg              | 405 ms                                                                | 413 ms: 1.02x slower                                                            |
| logging_format                | 4.34 us                                                               | 4.43 us: 1.02x slower                                                           |
| regex_effbot                  | 2.34 ms                                                               | 2.40 ms: 1.02x slower                                                           |
| logging_simple                | 4.04 us                                                               | 4.14 us: 1.03x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (34): gc_traversal, async_generators, dask, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, coroutines, async_tree_cpu_io_mixed_tg, k_core, pidigits, asyncio_websockets, xml_etree_parse, scimark_sor, comprehensions, thrift, pickle_pure_python, fannkuch, raytrace, async_tree_memoization_tg, typing_runtime_protocols, async_tree_eager_memoization_tg, genshi_xml, json, sympy_sum, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_eager_io, html5lib, pycparser, subparsers, pathlib, async_tree_io, pylint, sphinx

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x