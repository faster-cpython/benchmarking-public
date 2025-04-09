# Results vs. base

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: windows-amd64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                                      | 220 ms: 1.01x slower                                                               |
| docutils       | 1.63 sec                                                                    | 1.64 sec: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 328 ms                                                                      | 331 ms: 1.01x slower                                                               |
| async_tree_io_tg           | 392 ms                                                                      | 399 ms: 1.02x slower                                                               |
| async_tree_memoization_tg  | 208 ms                                                                      | 212 ms: 1.02x slower                                                               |
| async_tree_memoization     | 202 ms                                                                      | 207 ms: 1.02x slower                                                               |
| async_tree_cpu_io_mixed_tg | 335 ms                                                                      | 343 ms: 1.02x slower                                                               |
| async_tree_none_tg         | 169 ms                                                                      | 173 ms: 1.03x slower                                                               |
| async_tree_none            | 178 ms                                                                      | 183 ms: 1.03x slower                                                               |
| coroutines                 | 13.4 ms                                                                     | 13.9 ms: 1.04x slower                                                              |
| async_generators           | 221 ms                                                                      | 233 ms: 1.05x slower                                                               |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 68.2 ms                                                                     | 65.5 ms: 1.04x faster                                                              |
| pidigits       | 149 ms                                                                      | 150 ms: 1.00x slower                                                               |
| float          | 43.0 ms                                                                     | 43.5 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 115 ms                                                                      | 114 ms: 1.01x faster                                                               |
| regex_v8       | 13.6 ms                                                                     | 13.7 ms: 1.00x slower                                                              |
| regex_effbot   | 1.41 ms                                                                     | 1.42 ms: 1.01x slower                                                              |
| regex_compile  | 79.5 ms                                                                     | 80.5 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 57.0 ms                                                                     | 55.4 ms: 1.03x faster                                                              |
| json_loads           | 15.0 us                                                                     | 15.2 us: 1.02x slower                                                              |
| pickle_pure_python   | 211 us                                                                      | 215 us: 1.02x slower                                                               |
| unpickle_pure_python | 132 us                                                                      | 137 us: 1.03x slower                                                               |
| json_dumps           | 6.55 ms                                                                     | 6.80 ms: 1.04x slower                                                              |
| tomli_loads          | 1.33 sec                                                                    | 1.43 sec: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                       |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.68 ms                                                                     | 6.81 ms: 1.02x slower                                                              |
| django_template | 24.0 ms                                                                     | 24.7 ms: 1.03x slower                                                              |
| genshi_text     | 15.3 ms                                                                     | 15.8 ms: 1.03x slower                                                              |
| genshi_xml      | 34.2 ms                                                                     | 35.4 ms: 1.04x slower                                                              |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                      | 68.2 ms                                                                     | 65.5 ms: 1.04x faster                                                              |
| logging_silent             | 57.7 ns                                                                     | 55.9 ns: 1.03x faster                                                              |
| xml_etree_generate         | 57.0 ms                                                                     | 55.4 ms: 1.03x faster                                                              |
| dulwich_log                | 41.7 ms                                                                     | 40.6 ms: 1.03x faster                                                              |
| generators                 | 19.7 ms                                                                     | 19.4 ms: 1.01x faster                                                              |
| richards                   | 28.1 ms                                                                     | 27.7 ms: 1.01x faster                                                              |
| logging_format             | 6.74 us                                                                     | 6.64 us: 1.01x faster                                                              |
| regex_dna                  | 115 ms                                                                      | 114 ms: 1.01x faster                                                               |
| richards_super             | 32.0 ms                                                                     | 31.6 ms: 1.01x faster                                                              |
| spectral_norm              | 59.3 ms                                                                     | 58.6 ms: 1.01x faster                                                              |
| sympy_expand               | 298 ms                                                                      | 295 ms: 1.01x faster                                                               |
| go                         | 79.3 ms                                                                     | 78.5 ms: 1.01x faster                                                              |
| many_optionals             | 429 us                                                                      | 424 us: 1.01x faster                                                               |
| subparsers                 | 15.8 ms                                                                     | 15.7 ms: 1.01x faster                                                              |
| sympy_str                  | 173 ms                                                                      | 172 ms: 1.01x faster                                                               |
| docutils                   | 1.63 sec                                                                    | 1.64 sec: 1.00x slower                                                             |
| pidigits                   | 149 ms                                                                      | 150 ms: 1.00x slower                                                               |
| regex_v8                   | 13.6 ms                                                                     | 13.7 ms: 1.00x slower                                                              |
| regex_effbot               | 1.41 ms                                                                     | 1.42 ms: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                                      | 220 ms: 1.01x slower                                                               |
| chaos                      | 38.1 ms                                                                     | 38.4 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed    | 328 ms                                                                      | 331 ms: 1.01x slower                                                               |
| deepcopy_memo              | 18.1 us                                                                     | 18.3 us: 1.01x slower                                                              |
| bench_mp_pool              | 86.3 ms                                                                     | 87.1 ms: 1.01x slower                                                              |
| deepcopy_reduce            | 1.82 us                                                                     | 1.84 us: 1.01x slower                                                              |
| float                      | 43.0 ms                                                                     | 43.5 ms: 1.01x slower                                                              |
| regex_compile              | 79.5 ms                                                                     | 80.5 ms: 1.01x slower                                                              |
| shortest_path              | 353 ms                                                                      | 357 ms: 1.01x slower                                                               |
| scimark_sor                | 74.7 ms                                                                     | 75.8 ms: 1.01x slower                                                              |
| pprint_pformat             | 1.01 sec                                                                    | 1.03 sec: 1.01x slower                                                             |
| telco                      | 4.70 ms                                                                     | 4.77 ms: 1.01x slower                                                              |
| scimark_fft                | 172 ms                                                                      | 175 ms: 1.02x slower                                                               |
| scimark_monte_carlo        | 39.6 ms                                                                     | 40.2 ms: 1.02x slower                                                              |
| connected_components       | 322 ms                                                                      | 327 ms: 1.02x slower                                                               |
| json_loads                 | 15.0 us                                                                     | 15.2 us: 1.02x slower                                                              |
| deepcopy                   | 171 us                                                                      | 174 us: 1.02x slower                                                               |
| async_tree_io_tg           | 392 ms                                                                      | 399 ms: 1.02x slower                                                               |
| pickle_pure_python         | 211 us                                                                      | 215 us: 1.02x slower                                                               |
| mako                       | 6.68 ms                                                                     | 6.81 ms: 1.02x slower                                                              |
| sqlglot_v2_parse           | 811 us                                                                      | 828 us: 1.02x slower                                                               |
| nqueens                    | 60.5 ms                                                                     | 61.8 ms: 1.02x slower                                                              |
| async_tree_memoization_tg  | 208 ms                                                                      | 212 ms: 1.02x slower                                                               |
| pycparser                  | 700 ms                                                                      | 715 ms: 1.02x slower                                                               |
| async_tree_memoization     | 202 ms                                                                      | 207 ms: 1.02x slower                                                               |
| sqlglot_v2_normalize       | 71.3 ms                                                                     | 72.9 ms: 1.02x slower                                                              |
| async_tree_cpu_io_mixed_tg | 335 ms                                                                      | 343 ms: 1.02x slower                                                               |
| sqlglot_v2_transpile       | 1.01 ms                                                                     | 1.03 ms: 1.02x slower                                                              |
| async_tree_none_tg         | 169 ms                                                                      | 173 ms: 1.03x slower                                                               |
| django_template            | 24.0 ms                                                                     | 24.7 ms: 1.03x slower                                                              |
| sqlglot_v2_optimize        | 34.1 ms                                                                     | 35.0 ms: 1.03x slower                                                              |
| mdp                        | 777 ms                                                                      | 798 ms: 1.03x slower                                                               |
| deltablue                  | 2.11 ms                                                                     | 2.16 ms: 1.03x slower                                                              |
| async_tree_none            | 178 ms                                                                      | 183 ms: 1.03x slower                                                               |
| scimark_sparse_mat_mult    | 2.48 ms                                                                     | 2.55 ms: 1.03x slower                                                              |
| pprint_safe_repr           | 492 ms                                                                      | 506 ms: 1.03x slower                                                               |
| fannkuch                   | 248 ms                                                                      | 256 ms: 1.03x slower                                                               |
| genshi_text                | 15.3 ms                                                                     | 15.8 ms: 1.03x slower                                                              |
| unpickle_pure_python       | 132 us                                                                      | 137 us: 1.03x slower                                                               |
| pyflate                    | 286 ms                                                                      | 296 ms: 1.03x slower                                                               |
| genshi_xml                 | 34.2 ms                                                                     | 35.4 ms: 1.04x slower                                                              |
| json                       | 3.13 ms                                                                     | 3.25 ms: 1.04x slower                                                              |
| json_dumps                 | 6.55 ms                                                                     | 6.80 ms: 1.04x slower                                                              |
| coroutines                 | 13.4 ms                                                                     | 13.9 ms: 1.04x slower                                                              |
| bpe_tokeniser              | 2.82 sec                                                                    | 2.94 sec: 1.04x slower                                                             |
| scimark_lu                 | 60.2 ms                                                                     | 62.7 ms: 1.04x slower                                                              |
| raytrace                   | 171 ms                                                                      | 179 ms: 1.04x slower                                                               |
| coverage                   | 49.8 ms                                                                     | 52.0 ms: 1.04x slower                                                              |
| comprehensions             | 11.1 us                                                                     | 11.7 us: 1.05x slower                                                              |
| hexiom                     | 3.94 ms                                                                     | 4.14 ms: 1.05x slower                                                              |
| crypto_pyaes               | 46.4 ms                                                                     | 48.8 ms: 1.05x slower                                                              |
| async_generators           | 221 ms                                                                      | 233 ms: 1.05x slower                                                               |
| tomli_loads                | 1.33 sec                                                                    | 1.43 sec: 1.08x slower                                                             |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (21): bench_thread_pool, xml_etree_iterparse, asyncio_websockets, xml_etree_parse, create_gc_cycles, sphinx, html5lib, sympy_integrate, xml_etree_process, logging_simple, sqlite_synth, typing_runtime_protocols, meteor_contest, python_startup_no_site, sympy_sum, python_startup, k_core, pathlib, gc_traversal, async_tree_io, pylint

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown