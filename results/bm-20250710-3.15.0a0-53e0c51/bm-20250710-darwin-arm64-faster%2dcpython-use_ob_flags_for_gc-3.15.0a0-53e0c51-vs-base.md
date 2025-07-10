# Results vs. base

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: darwin-arm64
- commit hash: 53e0c51
- commit date: 2025-07-10
- overall geometric mean: 1.006x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                              | 1.52 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager              | 75.8 ms                                                               | 73.5 ms: 1.03x faster                                                          |
| async_tree_eager_io_tg        | 404 ms                                                                | 394 ms: 1.02x faster                                                           |
| async_tree_eager_io           | 396 ms                                                                | 389 ms: 1.02x faster                                                           |
| async_tree_memoization_tg     | 208 ms                                                                | 205 ms: 1.01x faster                                                           |
| async_tree_io                 | 409 ms                                                                | 404 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg    | 423 ms                                                                | 421 ms: 1.01x faster                                                           |
| async_generators              | 278 ms                                                                | 278 ms: 1.00x slower                                                           |
| async_tree_memoization        | 214 ms                                                                | 214 ms: 1.00x slower                                                           |
| async_tree_eager_cpu_io_mixed | 366 ms                                                                | 368 ms: 1.01x slower                                                           |
| async_tree_eager_memoization  | 149 ms                                                                | 150 ms: 1.01x slower                                                           |
| async_tree_none               | 178 ms                                                                | 180 ms: 1.01x slower                                                           |
| coroutines                    | 18.9 ms                                                               | 19.1 ms: 1.01x slower                                                          |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                                   |

Benchmark hidden because not significant (7): async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 284 ms                                                                | 286 ms: 1.01x slower                                                           |
| float          | 56.7 ms                                                               | 59.9 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.38 ms                                                               | 2.36 ms: 1.01x faster                                                          |
| regex_dna      | 143 ms                                                                | 144 ms: 1.01x slower                                                           |
| regex_compile  | 81.1 ms                                                               | 82.2 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                                | 98.7 ms: 1.06x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                               | 73.5 ms: 1.01x faster                                                          |
| xml_etree_generate   | 58.6 ms                                                               | 58.9 ms: 1.00x slower                                                          |
| pickle_pure_python   | 242 us                                                                | 243 us: 1.01x slower                                                           |
| json_loads           | 16.6 us                                                               | 16.7 us: 1.01x slower                                                          |
| xml_etree_process    | 43.5 ms                                                               | 43.9 ms: 1.01x slower                                                          |
| tomli_loads          | 1.42 sec                                                              | 1.45 sec: 1.02x slower                                                         |
| json_dumps           | 6.83 ms                                                               | 6.94 ms: 1.02x slower                                                          |
| unpickle_pure_python | 176 us                                                                | 182 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 17.5 ms                                                               | 16.7 ms: 1.04x faster                                                          |
| python_startup_no_site | 13.0 ms                                                               | 12.4 ms: 1.04x faster                                                          |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                          |
| mako            | 9.03 ms                                                               | 9.16 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| create_gc_cycles              | 1.37 ms                                                               | 1.27 ms: 1.08x faster                                                          |
| xml_etree_parse               | 104 ms                                                                | 98.7 ms: 1.06x faster                                                          |
| python_startup                | 17.5 ms                                                               | 16.7 ms: 1.04x faster                                                          |
| python_startup_no_site        | 13.0 ms                                                               | 12.4 ms: 1.04x faster                                                          |
| async_tree_eager              | 75.8 ms                                                               | 73.5 ms: 1.03x faster                                                          |
| gc_traversal                  | 3.19 ms                                                               | 3.11 ms: 1.02x faster                                                          |
| async_tree_eager_io_tg        | 404 ms                                                                | 394 ms: 1.02x faster                                                           |
| logging_silent                | 79.4 ns                                                               | 77.7 ns: 1.02x faster                                                          |
| logging_format                | 4.22 us                                                               | 4.14 us: 1.02x faster                                                          |
| logging_simple                | 3.92 us                                                               | 3.84 us: 1.02x faster                                                          |
| async_tree_eager_io           | 396 ms                                                                | 389 ms: 1.02x faster                                                           |
| async_tree_memoization_tg     | 208 ms                                                                | 205 ms: 1.01x faster                                                           |
| xml_etree_iterparse           | 74.5 ms                                                               | 73.5 ms: 1.01x faster                                                          |
| async_tree_io                 | 409 ms                                                                | 404 ms: 1.01x faster                                                           |
| subparsers                    | 15.0 ms                                                               | 14.9 ms: 1.01x faster                                                          |
| docutils                      | 1.53 sec                                                              | 1.52 sec: 1.01x faster                                                         |
| regex_effbot                  | 2.38 ms                                                               | 2.36 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg    | 423 ms                                                                | 421 ms: 1.01x faster                                                           |
| many_optionals                | 503 us                                                                | 500 us: 1.01x faster                                                           |
| async_generators              | 278 ms                                                                | 278 ms: 1.00x slower                                                           |
| async_tree_memoization        | 214 ms                                                                | 214 ms: 1.00x slower                                                           |
| deepcopy                      | 176 us                                                                | 177 us: 1.00x slower                                                           |
| xml_etree_generate            | 58.6 ms                                                               | 58.9 ms: 1.00x slower                                                          |
| pickle_pure_python            | 242 us                                                                | 243 us: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed | 366 ms                                                                | 368 ms: 1.01x slower                                                           |
| deepcopy_reduce               | 1.89 us                                                               | 1.90 us: 1.01x slower                                                          |
| go                            | 99.4 ms                                                               | 100 ms: 1.01x slower                                                           |
| coverage                      | 49.3 ms                                                               | 49.6 ms: 1.01x slower                                                          |
| json_loads                    | 16.6 us                                                               | 16.7 us: 1.01x slower                                                          |
| pidigits                      | 284 ms                                                                | 286 ms: 1.01x slower                                                           |
| scimark_monte_carlo           | 53.1 ms                                                               | 53.5 ms: 1.01x slower                                                          |
| shortest_path                 | 328 ms                                                                | 331 ms: 1.01x slower                                                           |
| regex_dna                     | 143 ms                                                                | 144 ms: 1.01x slower                                                           |
| connected_components          | 304 ms                                                                | 307 ms: 1.01x slower                                                           |
| django_template               | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                          |
| xml_etree_process             | 43.5 ms                                                               | 43.9 ms: 1.01x slower                                                          |
| async_tree_eager_memoization  | 149 ms                                                                | 150 ms: 1.01x slower                                                           |
| pyflate                       | 335 ms                                                                | 338 ms: 1.01x slower                                                           |
| async_tree_none               | 178 ms                                                                | 180 ms: 1.01x slower                                                           |
| thrift                        | 473 us                                                                | 478 us: 1.01x slower                                                           |
| comprehensions                | 13.2 us                                                               | 13.3 us: 1.01x slower                                                          |
| pprint_pformat                | 1.19 sec                                                              | 1.21 sec: 1.01x slower                                                         |
| meteor_contest                | 74.0 ms                                                               | 74.9 ms: 1.01x slower                                                          |
| pprint_safe_repr              | 586 ms                                                                | 594 ms: 1.01x slower                                                           |
| regex_compile                 | 81.1 ms                                                               | 82.2 ms: 1.01x slower                                                          |
| coroutines                    | 18.9 ms                                                               | 19.1 ms: 1.01x slower                                                          |
| mako                          | 9.03 ms                                                               | 9.16 ms: 1.01x slower                                                          |
| tomli_loads                   | 1.42 sec                                                              | 1.45 sec: 1.02x slower                                                         |
| bpe_tokeniser                 | 3.23 sec                                                              | 3.28 sec: 1.02x slower                                                         |
| nqueens                       | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                          |
| json_dumps                    | 6.83 ms                                                               | 6.94 ms: 1.02x slower                                                          |
| generators                    | 31.4 ms                                                               | 31.9 ms: 1.02x slower                                                          |
| scimark_fft                   | 202 ms                                                                | 205 ms: 1.02x slower                                                           |
| sqlite_synth                  | 1.63 us                                                               | 1.65 us: 1.02x slower                                                          |
| pathlib                       | 22.9 ms                                                               | 23.3 ms: 1.02x slower                                                          |
| json                          | 2.93 ms                                                               | 2.98 ms: 1.02x slower                                                          |
| richards_super                | 42.6 ms                                                               | 43.4 ms: 1.02x slower                                                          |
| sqlglot_v2_optimize           | 36.3 ms                                                               | 37.0 ms: 1.02x slower                                                          |
| spectral_norm                 | 71.8 ms                                                               | 73.3 ms: 1.02x slower                                                          |
| mdp                           | 819 ms                                                                | 836 ms: 1.02x slower                                                           |
| sympy_integrate               | 11.2 ms                                                               | 11.5 ms: 1.02x slower                                                          |
| sympy_expand                  | 262 ms                                                                | 267 ms: 1.02x slower                                                           |
| raytrace                      | 211 ms                                                                | 215 ms: 1.02x slower                                                           |
| scimark_sor                   | 90.0 ms                                                               | 92.2 ms: 1.02x slower                                                          |
| sympy_sum                     | 80.3 ms                                                               | 82.3 ms: 1.02x slower                                                          |
| sympy_str                     | 154 ms                                                                | 158 ms: 1.03x slower                                                           |
| typing_runtime_protocols      | 104 us                                                                | 107 us: 1.03x slower                                                           |
| telco                         | 4.76 ms                                                               | 4.89 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult       | 3.21 ms                                                               | 3.31 ms: 1.03x slower                                                          |
| deltablue                     | 2.73 ms                                                               | 2.81 ms: 1.03x slower                                                          |
| chaos                         | 46.0 ms                                                               | 47.6 ms: 1.03x slower                                                          |
| unpickle_pure_python          | 176 us                                                                | 182 us: 1.03x slower                                                           |
| sqlglot_v2_normalize          | 75.6 ms                                                               | 78.4 ms: 1.04x slower                                                          |
| sqlglot_v2_transpile          | 1.12 ms                                                               | 1.18 ms: 1.05x slower                                                          |
| float                         | 56.7 ms                                                               | 59.9 ms: 1.06x slower                                                          |
| sqlglot_v2_parse              | 940 us                                                                | 999 us: 1.06x slower                                                           |
| dulwich_log                   | 27.4 ms                                                               | 29.7 ms: 1.08x slower                                                          |
| fannkuch                      | 290 ms                                                                | 327 ms: 1.13x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.01x slower                                                                   |

Benchmark hidden because not significant (23): pylint, richards, scimark_lu, crypto_pyaes, regex_v8, hexiom, dask, async_tree_eager_memoization_tg, genshi_text, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, 2to3, deepcopy_memo, async_tree_cpu_io_mixed, async_tree_none_tg, html5lib, k_core, genshi_xml, nbody, sphinx, async_tree_io_tg, pycparser, async_tree_eager_tg

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x