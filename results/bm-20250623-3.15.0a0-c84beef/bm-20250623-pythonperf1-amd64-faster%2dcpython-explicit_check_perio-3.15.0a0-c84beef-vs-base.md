# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.020x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                     | 226 ms: 1.01x slower                                                                 |
| docutils       | 1.62 sec                                                                   | 1.65 sec: 1.02x slower                                                               |
| html5lib       | 39.0 ms                                                                    | 40.7 ms: 1.04x slower                                                                |
| sphinx         | 638 ms                                                                     | 655 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                 | 14.6 ms                                                                    | 14.4 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 351 ms: 1.02x slower                                                                 |
| async_tree_memoization_tg  | 215 ms                                                                     | 226 ms: 1.05x slower                                                                 |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 345 ms: 1.05x slower                                                                 |
| async_tree_io_tg           | 394 ms                                                                     | 418 ms: 1.06x slower                                                                 |
| async_tree_io              | 399 ms                                                                     | 424 ms: 1.06x slower                                                                 |
| async_tree_none_tg         | 171 ms                                                                     | 183 ms: 1.07x slower                                                                 |
| async_tree_memoization     | 208 ms                                                                     | 228 ms: 1.09x slower                                                                 |
| async_tree_none            | 171 ms                                                                     | 188 ms: 1.09x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.04x slower                                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 67.3 ms                                                                    | 65.2 ms: 1.03x faster                                                                |
| pidigits       | 146 ms                                                                     | 146 ms: 1.01x slower                                                                 |
| float          | 45.1 ms                                                                    | 46.1 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                    | 14.0 ms: 1.03x faster                                                                |
| regex_dna      | 122 ms                                                                     | 121 ms: 1.01x faster                                                                 |
| regex_effbot   | 1.57 ms                                                                    | 1.59 ms: 1.01x slower                                                                |
| regex_compile  | 81.1 ms                                                                    | 84.1 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 64.6 ms                                                                    | 63.1 ms: 1.02x faster                                                                |
| tomli_loads          | 1.42 sec                                                                   | 1.41 sec: 1.01x faster                                                               |
| xml_etree_generate   | 56.8 ms                                                                    | 56.4 ms: 1.01x faster                                                                |
| json_loads           | 14.3 us                                                                    | 14.4 us: 1.01x slower                                                                |
| pickle_pure_python   | 215 us                                                                     | 222 us: 1.03x slower                                                                 |
| unpickle_pure_python | 137 us                                                                     | 142 us: 1.04x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.86 ms                                                                    | 6.78 ms: 1.01x faster                                                                |
| django_template | 24.7 ms                                                                    | 25.1 ms: 1.02x slower                                                                |
| genshi_text     | 15.5 ms                                                                    | 16.5 ms: 1.06x slower                                                                |
| genshi_xml      | 34.2 ms                                                                    | 37.5 ms: 1.09x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.04x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| scimark_sor                | 79.7 ms                                                                    | 75.2 ms: 1.06x faster                                                                |
| spectral_norm              | 64.7 ms                                                                    | 62.1 ms: 1.04x faster                                                                |
| gc_traversal               | 2.22 ms                                                                    | 2.14 ms: 1.03x faster                                                                |
| nbody                      | 67.3 ms                                                                    | 65.2 ms: 1.03x faster                                                                |
| regex_v8                   | 14.3 ms                                                                    | 14.0 ms: 1.03x faster                                                                |
| xml_etree_iterparse        | 64.6 ms                                                                    | 63.1 ms: 1.02x faster                                                                |
| fannkuch                   | 264 ms                                                                     | 259 ms: 1.02x faster                                                                 |
| logging_silent             | 328 ns                                                                     | 323 ns: 1.02x faster                                                                 |
| coroutines                 | 14.6 ms                                                                    | 14.4 ms: 1.01x faster                                                                |
| chaos                      | 41.5 ms                                                                    | 41.0 ms: 1.01x faster                                                                |
| mako                       | 6.86 ms                                                                    | 6.78 ms: 1.01x faster                                                                |
| pathlib                    | 32.0 ms                                                                    | 31.6 ms: 1.01x faster                                                                |
| tomli_loads                | 1.42 sec                                                                   | 1.41 sec: 1.01x faster                                                               |
| xml_etree_generate         | 56.8 ms                                                                    | 56.4 ms: 1.01x faster                                                                |
| regex_dna                  | 122 ms                                                                     | 121 ms: 1.01x faster                                                                 |
| pidigits                   | 146 ms                                                                     | 146 ms: 1.01x slower                                                                 |
| bpe_tokeniser              | 3.00 sec                                                                   | 3.03 sec: 1.01x slower                                                               |
| deltablue                  | 2.22 ms                                                                    | 2.24 ms: 1.01x slower                                                                |
| go                         | 78.6 ms                                                                    | 79.3 ms: 1.01x slower                                                                |
| json_loads                 | 14.3 us                                                                    | 14.4 us: 1.01x slower                                                                |
| 2to3                       | 223 ms                                                                     | 226 ms: 1.01x slower                                                                 |
| shortest_path              | 361 ms                                                                     | 365 ms: 1.01x slower                                                                 |
| regex_effbot               | 1.57 ms                                                                    | 1.59 ms: 1.01x slower                                                                |
| thrift                     | 490 us                                                                     | 495 us: 1.01x slower                                                                 |
| hexiom                     | 4.18 ms                                                                    | 4.25 ms: 1.02x slower                                                                |
| json                       | 2.96 ms                                                                    | 3.01 ms: 1.02x slower                                                                |
| sqlglot_v2_parse           | 845 us                                                                     | 859 us: 1.02x slower                                                                 |
| django_template            | 24.7 ms                                                                    | 25.1 ms: 1.02x slower                                                                |
| typing_runtime_protocols   | 105 us                                                                     | 107 us: 1.02x slower                                                                 |
| scimark_lu                 | 59.1 ms                                                                    | 60.1 ms: 1.02x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                                    | 41.5 ms: 1.02x slower                                                                |
| coverage                   | 48.7 ms                                                                    | 49.7 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 351 ms: 1.02x slower                                                                 |
| docutils                   | 1.62 sec                                                                   | 1.65 sec: 1.02x slower                                                               |
| float                      | 45.1 ms                                                                    | 46.1 ms: 1.02x slower                                                                |
| pycparser                  | 720 ms                                                                     | 739 ms: 1.03x slower                                                                 |
| richards                   | 27.8 ms                                                                    | 28.5 ms: 1.03x slower                                                                |
| sphinx                     | 638 ms                                                                     | 655 ms: 1.03x slower                                                                 |
| meteor_contest             | 73.0 ms                                                                    | 74.9 ms: 1.03x slower                                                                |
| telco                      | 4.48 ms                                                                    | 4.60 ms: 1.03x slower                                                                |
| subparsers                 | 17.1 ms                                                                    | 17.5 ms: 1.03x slower                                                                |
| logging_simple             | 6.44 us                                                                    | 6.62 us: 1.03x slower                                                                |
| deepcopy_memo              | 18.4 us                                                                    | 18.9 us: 1.03x slower                                                                |
| dulwich_log                | 41.1 ms                                                                    | 42.3 ms: 1.03x slower                                                                |
| raytrace                   | 183 ms                                                                     | 189 ms: 1.03x slower                                                                 |
| sqlglot_v2_transpile       | 1.03 ms                                                                    | 1.07 ms: 1.03x slower                                                                |
| sympy_integrate            | 12.5 ms                                                                    | 12.9 ms: 1.03x slower                                                                |
| richards_super             | 31.6 ms                                                                    | 32.6 ms: 1.03x slower                                                                |
| sympy_sum                  | 88.0 ms                                                                    | 90.8 ms: 1.03x slower                                                                |
| pickle_pure_python         | 215 us                                                                     | 222 us: 1.03x slower                                                                 |
| many_optionals             | 437 us                                                                     | 452 us: 1.03x slower                                                                 |
| regex_compile              | 81.1 ms                                                                    | 84.1 ms: 1.04x slower                                                                |
| logging_format             | 6.88 us                                                                    | 7.14 us: 1.04x slower                                                                |
| nqueens                    | 62.2 ms                                                                    | 64.7 ms: 1.04x slower                                                                |
| sqlglot_v2_normalize       | 70.2 ms                                                                    | 73.1 ms: 1.04x slower                                                                |
| unpickle_pure_python       | 137 us                                                                     | 142 us: 1.04x slower                                                                 |
| deepcopy_reduce            | 1.83 us                                                                    | 1.90 us: 1.04x slower                                                                |
| comprehensions             | 10.6 us                                                                    | 11.0 us: 1.04x slower                                                                |
| html5lib                   | 39.0 ms                                                                    | 40.7 ms: 1.04x slower                                                                |
| sympy_expand               | 289 ms                                                                     | 302 ms: 1.04x slower                                                                 |
| mdp                        | 800 ms                                                                     | 835 ms: 1.04x slower                                                                 |
| sqlglot_v2_optimize        | 33.6 ms                                                                    | 35.2 ms: 1.05x slower                                                                |
| sympy_str                  | 168 ms                                                                     | 176 ms: 1.05x slower                                                                 |
| async_tree_memoization_tg  | 215 ms                                                                     | 226 ms: 1.05x slower                                                                 |
| crypto_pyaes               | 47.4 ms                                                                    | 49.8 ms: 1.05x slower                                                                |
| deepcopy                   | 169 us                                                                     | 178 us: 1.05x slower                                                                 |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 345 ms: 1.05x slower                                                                 |
| generators                 | 19.3 ms                                                                    | 20.5 ms: 1.06x slower                                                                |
| async_tree_io_tg           | 394 ms                                                                     | 418 ms: 1.06x slower                                                                 |
| genshi_text                | 15.5 ms                                                                    | 16.5 ms: 1.06x slower                                                                |
| async_tree_io              | 399 ms                                                                     | 424 ms: 1.06x slower                                                                 |
| pprint_safe_repr           | 532 ms                                                                     | 566 ms: 1.06x slower                                                                 |
| async_tree_none_tg         | 171 ms                                                                     | 183 ms: 1.07x slower                                                                 |
| pprint_pformat             | 1.09 sec                                                                   | 1.17 sec: 1.08x slower                                                               |
| async_tree_memoization     | 208 ms                                                                     | 228 ms: 1.09x slower                                                                 |
| async_tree_none            | 171 ms                                                                     | 188 ms: 1.09x slower                                                                 |
| genshi_xml                 | 34.2 ms                                                                    | 37.5 ms: 1.09x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (15): python_startup, pyflate, xml_etree_process, scimark_fft, create_gc_cycles, xml_etree_parse, json_dumps, asyncio_websockets, scimark_sparse_mat_mult, async_generators, sqlite_synth, k_core, connected_components, python_startup_no_site, pylint

- Geometric mean (including insignificant results): 1.020x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown