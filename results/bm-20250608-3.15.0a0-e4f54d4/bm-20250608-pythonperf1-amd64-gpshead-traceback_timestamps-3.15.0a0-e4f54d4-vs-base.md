# Results vs. base

- fork: gpshead
- ref: traceback_timestamps
- machine: windows-amd64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.006x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                   | 1.62 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 402 ms                                                                     | 389 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 406 ms                                                                     | 392 ms: 1.03x faster                                                        |
| async_tree_memoization     | 212 ms                                                                     | 206 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 214 ms                                                                     | 208 ms: 1.03x faster                                                        |
| asyncio_websockets         | 162 ms                                                                     | 158 ms: 1.02x faster                                                        |
| coroutines                 | 14.2 ms                                                                    | 13.9 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 338 ms: 1.02x faster                                                        |
| async_tree_none            | 173 ms                                                                     | 170 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 173 ms                                                                     | 171 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 64.8 ms                                                                    | 62.8 ms: 1.03x faster                                                       |
| float          | 45.1 ms                                                                    | 44.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 14.5 ms                                                                    | 13.9 ms: 1.04x faster                                                       |
| regex_dna      | 120 ms                                                                     | 121 ms: 1.01x slower                                                        |
| regex_effbot   | 1.51 ms                                                                    | 1.53 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|---------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 57.0 ms                                                                    | 55.6 ms: 1.02x faster                                                       |
| tomli_loads         | 1.41 sec                                                                   | 1.39 sec: 1.01x faster                                                      |
| pickle_pure_python  | 214 us                                                                     | 212 us: 1.01x faster                                                        |
| xml_etree_iterparse | 65.5 ms                                                                    | 64.8 ms: 1.01x faster                                                       |
| Geometric mean      | (ref)                                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, unpickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 26.6 ms                                                                    | 26.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.79 ms                                                                    | 6.65 ms: 1.02x faster                                                       |
| django_template | 24.2 ms                                                                    | 24.0 ms: 1.01x faster                                                       |
| genshi_text     | 15.1 ms                                                                    | 15.4 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8                   | 14.5 ms                                                                    | 13.9 ms: 1.04x faster                                                       |
| async_tree_io              | 402 ms                                                                     | 389 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 406 ms                                                                     | 392 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 106 us                                                                     | 103 us: 1.03x faster                                                        |
| nbody                      | 64.8 ms                                                                    | 62.8 ms: 1.03x faster                                                       |
| telco                      | 4.71 ms                                                                    | 4.57 ms: 1.03x faster                                                       |
| async_tree_memoization     | 212 ms                                                                     | 206 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 214 ms                                                                     | 208 ms: 1.03x faster                                                        |
| coverage                   | 299 ms                                                                     | 291 ms: 1.03x faster                                                        |
| xml_etree_generate         | 57.0 ms                                                                    | 55.6 ms: 1.02x faster                                                       |
| float                      | 45.1 ms                                                                    | 44.0 ms: 1.02x faster                                                       |
| sympy_expand               | 292 ms                                                                     | 285 ms: 1.02x faster                                                        |
| asyncio_websockets         | 162 ms                                                                     | 158 ms: 1.02x faster                                                        |
| pycparser                  | 720 ms                                                                     | 704 ms: 1.02x faster                                                        |
| k_core                     | 1.72 sec                                                                   | 1.69 sec: 1.02x faster                                                      |
| sqlglot_v2_optimize        | 34.4 ms                                                                    | 33.7 ms: 1.02x faster                                                       |
| mako                       | 6.79 ms                                                                    | 6.65 ms: 1.02x faster                                                       |
| many_optionals             | 444 us                                                                     | 435 us: 1.02x faster                                                        |
| subparsers                 | 17.2 ms                                                                    | 16.8 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 3.01 sec                                                                   | 2.95 sec: 1.02x faster                                                      |
| coroutines                 | 14.2 ms                                                                    | 13.9 ms: 1.02x faster                                                       |
| comprehensions             | 11.1 us                                                                    | 10.9 us: 1.02x faster                                                       |
| scimark_lu                 | 58.6 ms                                                                    | 57.4 ms: 1.02x faster                                                       |
| sqlglot_v2_normalize       | 71.3 ms                                                                    | 70.0 ms: 1.02x faster                                                       |
| mdp                        | 815 ms                                                                     | 801 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 338 ms: 1.02x faster                                                        |
| async_tree_none            | 173 ms                                                                     | 170 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 173 ms                                                                     | 171 ms: 1.02x faster                                                        |
| generators                 | 19.8 ms                                                                    | 19.5 ms: 1.02x faster                                                       |
| tomli_loads                | 1.41 sec                                                                   | 1.39 sec: 1.01x faster                                                      |
| python_startup             | 26.6 ms                                                                    | 26.2 ms: 1.01x faster                                                       |
| pickle_pure_python         | 214 us                                                                     | 212 us: 1.01x faster                                                        |
| xml_etree_iterparse        | 65.5 ms                                                                    | 64.8 ms: 1.01x faster                                                       |
| django_template            | 24.2 ms                                                                    | 24.0 ms: 1.01x faster                                                       |
| sympy_str                  | 169 ms                                                                     | 168 ms: 1.01x faster                                                        |
| dulwich_log                | 41.3 ms                                                                    | 40.9 ms: 1.01x faster                                                       |
| sympy_sum                  | 88.1 ms                                                                    | 87.4 ms: 1.01x faster                                                       |
| docutils                   | 1.63 sec                                                                   | 1.62 sec: 1.01x faster                                                      |
| deepcopy                   | 172 us                                                                     | 171 us: 1.01x faster                                                        |
| deltablue                  | 2.24 ms                                                                    | 2.23 ms: 1.01x faster                                                       |
| sympy_integrate            | 12.4 ms                                                                    | 12.3 ms: 1.01x faster                                                       |
| crypto_pyaes               | 47.3 ms                                                                    | 47.6 ms: 1.01x slower                                                       |
| meteor_contest             | 72.9 ms                                                                    | 73.4 ms: 1.01x slower                                                       |
| regex_dna                  | 120 ms                                                                     | 121 ms: 1.01x slower                                                        |
| scimark_sor                | 74.5 ms                                                                    | 75.2 ms: 1.01x slower                                                       |
| fannkuch                   | 253 ms                                                                     | 256 ms: 1.01x slower                                                        |
| genshi_text                | 15.1 ms                                                                    | 15.4 ms: 1.02x slower                                                       |
| regex_effbot               | 1.51 ms                                                                    | 1.53 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.10 sec                                                                   | 1.12 sec: 1.02x slower                                                      |
| pprint_safe_repr           | 541 ms                                                                     | 554 ms: 1.02x slower                                                        |
| hexiom                     | 4.04 ms                                                                    | 4.14 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 40.4 ms                                                                    | 41.5 ms: 1.03x slower                                                       |
| logging_silent             | 315 ns                                                                     | 324 ns: 1.03x slower                                                        |
| sqlite_synth               | 1.59 us                                                                    | 1.64 us: 1.03x slower                                                       |
| scimark_fft                | 173 ms                                                                     | 178 ms: 1.03x slower                                                        |
| spectral_norm              | 57.5 ms                                                                    | 60.1 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (36): pylint, json, sphinx, pyflate, sqlglot_v2_transpile, connected_components, sqlglot_v2_parse, deepcopy_reduce, 2to3, chaos, xml_etree_process, logging_format, richards, python_startup_no_site, json_dumps, async_generators, logging_simple, shortest_path, unpickle_pure_python, xml_etree_parse, regex_compile, thrift, richards_super, deepcopy_memo, create_gc_cycles, async_tree_cpu_io_mixed, nqueens, go, pidigits, scimark_sparse_mat_mult, raytrace, json_loads, html5lib, genshi_xml, pathlib, gc_traversal

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown