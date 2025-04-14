# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                      | 231 ms: 1.04x slower                                                           |
| docutils       | 1.65 sec                                                                    | 1.71 sec: 1.04x slower                                                         |
| html5lib       | 39.7 ms                                                                     | 41.2 ms: 1.04x slower                                                          |
| sphinx         | 642 ms                                                                      | 670 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 341 ms                                                                      | 350 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 337 ms                                                                      | 355 ms: 1.05x slower                                                           |
| async_tree_none_tg         | 176 ms                                                                      | 186 ms: 1.06x slower                                                           |
| async_generators           | 223 ms                                                                      | 236 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 214 ms                                                                      | 228 ms: 1.07x slower                                                           |
| async_tree_io              | 416 ms                                                                      | 444 ms: 1.07x slower                                                           |
| async_tree_none            | 187 ms                                                                      | 199 ms: 1.07x slower                                                           |
| async_tree_memoization     | 218 ms                                                                      | 234 ms: 1.08x slower                                                           |
| coroutines                 | 13.2 ms                                                                     | 14.4 ms: 1.09x slower                                                          |
| async_tree_io_tg           | 403 ms                                                                      | 444 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 153 ms                                                                      | 151 ms: 1.01x faster                                                           |
| nbody          | 71.7 ms                                                                     | 78.4 ms: 1.09x slower                                                          |
| float          | 45.4 ms                                                                     | 51.5 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.46 ms                                                                     | 1.49 ms: 1.02x slower                                                          |
| regex_dna      | 114 ms                                                                      | 118 ms: 1.04x slower                                                           |
| regex_v8       | 14.4 ms                                                                     | 15.2 ms: 1.06x slower                                                          |
| regex_compile  | 85.2 ms                                                                     | 92.9 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.7 ms                                                                     | 91.2 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 62.6 ms                                                                     | 65.7 ms: 1.05x slower                                                          |
| json_dumps           | 6.75 ms                                                                     | 7.11 ms: 1.05x slower                                                          |
| xml_etree_generate   | 56.6 ms                                                                     | 61.2 ms: 1.08x slower                                                          |
| pickle_pure_python   | 224 us                                                                      | 244 us: 1.09x slower                                                           |
| xml_etree_process    | 39.8 ms                                                                     | 44.2 ms: 1.11x slower                                                          |
| tomli_loads          | 1.41 sec                                                                    | 1.62 sec: 1.15x slower                                                         |
| unpickle_pure_python | 147 us                                                                      | 170 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.8 ms                                                                     | 25.2 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 16.2 ms                                                                     | 17.6 ms: 1.09x slower                                                          |
| django_template | 24.8 ms                                                                     | 27.3 ms: 1.10x slower                                                          |
| genshi_xml      | 35.5 ms                                                                     | 39.5 ms: 1.11x slower                                                          |
| mako            | 6.81 ms                                                                     | 8.26 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.13x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse            | 92.7 ms                                                                     | 91.2 ms: 1.02x faster                                                          |
| pidigits                   | 153 ms                                                                      | 151 ms: 1.01x faster                                                           |
| generators                 | 19.4 ms                                                                     | 19.5 ms: 1.01x slower                                                          |
| coverage                   | 48.1 ms                                                                     | 48.3 ms: 1.01x slower                                                          |
| bench_mp_pool              | 84.9 ms                                                                     | 85.5 ms: 1.01x slower                                                          |
| dulwich_log                | 41.7 ms                                                                     | 42.1 ms: 1.01x slower                                                          |
| python_startup             | 24.8 ms                                                                     | 25.2 ms: 1.02x slower                                                          |
| pathlib                    | 29.5 ms                                                                     | 30.0 ms: 1.02x slower                                                          |
| regex_effbot               | 1.46 ms                                                                     | 1.49 ms: 1.02x slower                                                          |
| gc_traversal               | 1.97 ms                                                                     | 2.02 ms: 1.02x slower                                                          |
| many_optionals             | 432 us                                                                      | 441 us: 1.02x slower                                                           |
| sqlite_synth               | 1.56 us                                                                     | 1.60 us: 1.02x slower                                                          |
| pylint                     | 197 ms                                                                      | 202 ms: 1.03x slower                                                           |
| json                       | 3.00 ms                                                                     | 3.08 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                      | 350 ms: 1.03x slower                                                           |
| k_core                     | 1.69 sec                                                                    | 1.75 sec: 1.03x slower                                                         |
| 2to3                       | 223 ms                                                                      | 231 ms: 1.04x slower                                                           |
| regex_dna                  | 114 ms                                                                      | 118 ms: 1.04x slower                                                           |
| docutils                   | 1.65 sec                                                                    | 1.71 sec: 1.04x slower                                                         |
| subparsers                 | 16.3 ms                                                                     | 16.9 ms: 1.04x slower                                                          |
| html5lib                   | 39.7 ms                                                                     | 41.2 ms: 1.04x slower                                                          |
| shortest_path              | 349 ms                                                                      | 362 ms: 1.04x slower                                                           |
| sympy_integrate            | 13.2 ms                                                                     | 13.8 ms: 1.04x slower                                                          |
| connected_components       | 320 ms                                                                      | 334 ms: 1.04x slower                                                           |
| sphinx                     | 642 ms                                                                      | 670 ms: 1.04x slower                                                           |
| bench_thread_pool          | 831 us                                                                      | 869 us: 1.05x slower                                                           |
| sympy_str                  | 173 ms                                                                      | 182 ms: 1.05x slower                                                           |
| sympy_expand               | 297 ms                                                                      | 311 ms: 1.05x slower                                                           |
| mdp                        | 1.54 sec                                                                    | 1.62 sec: 1.05x slower                                                         |
| xml_etree_iterparse        | 62.6 ms                                                                     | 65.7 ms: 1.05x slower                                                          |
| meteor_contest             | 74.9 ms                                                                     | 78.7 ms: 1.05x slower                                                          |
| sympy_sum                  | 88.2 ms                                                                     | 92.8 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.76 ms                                                                     | 2.91 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 337 ms                                                                      | 355 ms: 1.05x slower                                                           |
| json_dumps                 | 6.75 ms                                                                     | 7.11 ms: 1.05x slower                                                          |
| telco                      | 4.74 ms                                                                     | 5.01 ms: 1.06x slower                                                          |
| async_tree_none_tg         | 176 ms                                                                      | 186 ms: 1.06x slower                                                           |
| regex_v8                   | 14.4 ms                                                                     | 15.2 ms: 1.06x slower                                                          |
| async_generators           | 223 ms                                                                      | 236 ms: 1.06x slower                                                           |
| sqlglot_transpile          | 1.10 ms                                                                     | 1.17 ms: 1.06x slower                                                          |
| pycparser                  | 739 ms                                                                      | 786 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 214 ms                                                                      | 228 ms: 1.07x slower                                                           |
| async_tree_io              | 416 ms                                                                      | 444 ms: 1.07x slower                                                           |
| async_tree_none            | 187 ms                                                                      | 199 ms: 1.07x slower                                                           |
| sqlglot_normalize          | 190 ms                                                                      | 203 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 34.7 ms                                                                     | 37.2 ms: 1.07x slower                                                          |
| bpe_tokeniser              | 2.88 sec                                                                    | 3.09 sec: 1.07x slower                                                         |
| async_tree_memoization     | 218 ms                                                                      | 234 ms: 1.08x slower                                                           |
| sqlglot_parse              | 885 us                                                                      | 954 us: 1.08x slower                                                           |
| logging_format             | 6.88 us                                                                     | 7.43 us: 1.08x slower                                                          |
| deepcopy                   | 183 us                                                                      | 198 us: 1.08x slower                                                           |
| xml_etree_generate         | 56.6 ms                                                                     | 61.2 ms: 1.08x slower                                                          |
| thrift                     | 498 us                                                                      | 539 us: 1.08x slower                                                           |
| logging_simple             | 6.42 us                                                                     | 6.95 us: 1.08x slower                                                          |
| scimark_fft                | 194 ms                                                                      | 210 ms: 1.08x slower                                                           |
| genshi_text                | 16.2 ms                                                                     | 17.6 ms: 1.09x slower                                                          |
| scimark_sor                | 85.8 ms                                                                     | 93.3 ms: 1.09x slower                                                          |
| deltablue                  | 2.19 ms                                                                     | 2.39 ms: 1.09x slower                                                          |
| coroutines                 | 13.2 ms                                                                     | 14.4 ms: 1.09x slower                                                          |
| scimark_monte_carlo        | 46.3 ms                                                                     | 50.5 ms: 1.09x slower                                                          |
| regex_compile              | 85.2 ms                                                                     | 92.9 ms: 1.09x slower                                                          |
| pickle_pure_python         | 224 us                                                                      | 244 us: 1.09x slower                                                           |
| spectral_norm              | 61.0 ms                                                                     | 66.7 ms: 1.09x slower                                                          |
| nbody                      | 71.7 ms                                                                     | 78.4 ms: 1.09x slower                                                          |
| chaos                      | 41.8 ms                                                                     | 45.9 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 105 us                                                                      | 115 us: 1.10x slower                                                           |
| django_template            | 24.8 ms                                                                     | 27.3 ms: 1.10x slower                                                          |
| async_tree_io_tg           | 403 ms                                                                      | 444 ms: 1.10x slower                                                           |
| deepcopy_reduce            | 1.90 us                                                                     | 2.09 us: 1.10x slower                                                          |
| pyflate                    | 310 ms                                                                      | 344 ms: 1.11x slower                                                           |
| xml_etree_process          | 39.8 ms                                                                     | 44.2 ms: 1.11x slower                                                          |
| genshi_xml                 | 35.5 ms                                                                     | 39.5 ms: 1.11x slower                                                          |
| pprint_safe_repr           | 534 ms                                                                      | 596 ms: 1.12x slower                                                           |
| pprint_pformat             | 1.08 sec                                                                    | 1.20 sec: 1.12x slower                                                         |
| richards_super             | 33.8 ms                                                                     | 37.8 ms: 1.12x slower                                                          |
| go                         | 84.5 ms                                                                     | 94.8 ms: 1.12x slower                                                          |
| deepcopy_memo              | 20.0 us                                                                     | 22.4 us: 1.12x slower                                                          |
| richards                   | 29.7 ms                                                                     | 33.4 ms: 1.12x slower                                                          |
| nqueens                    | 63.4 ms                                                                     | 71.8 ms: 1.13x slower                                                          |
| hexiom                     | 4.19 ms                                                                     | 4.75 ms: 1.13x slower                                                          |
| crypto_pyaes               | 49.9 ms                                                                     | 56.6 ms: 1.13x slower                                                          |
| float                      | 45.4 ms                                                                     | 51.5 ms: 1.13x slower                                                          |
| tomli_loads                | 1.41 sec                                                                    | 1.62 sec: 1.15x slower                                                         |
| comprehensions             | 11.3 us                                                                     | 13.0 us: 1.15x slower                                                          |
| scimark_lu                 | 64.2 ms                                                                     | 73.9 ms: 1.15x slower                                                          |
| unpickle_pure_python       | 147 us                                                                      | 170 us: 1.15x slower                                                           |
| fannkuch                   | 273 ms                                                                      | 317 ms: 1.16x slower                                                           |
| logging_silent             | 58.2 ns                                                                     | 69.6 ns: 1.20x slower                                                          |
| mako                       | 6.81 ms                                                                     | 8.26 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.07x slower                                                                   |

Benchmark hidden because not significant (5): asyncio_websockets, json_loads, raytrace, python_startup_no_site, create_gc_cycles

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown