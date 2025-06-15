# Results vs. base

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.072x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                               | 288 ms: 1.03x faster                                                                                                     |
| html5lib       | 51.2 ms                                                                                                              | 51.9 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 243 ms                                                                                                               | 232 ms: 1.05x faster                                                                                                     |
| async_tree_none_tg         | 237 ms                                                                                                               | 228 ms: 1.04x faster                                                                                                     |
| async_tree_memoization     | 296 ms                                                                                                               | 285 ms: 1.04x faster                                                                                                     |
| async_tree_memoization_tg  | 294 ms                                                                                                               | 284 ms: 1.03x faster                                                                                                     |
| async_tree_io              | 547 ms                                                                                                               | 531 ms: 1.03x faster                                                                                                     |
| async_tree_io_tg           | 566 ms                                                                                                               | 551 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 442 ms                                                                                                               | 432 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 437 ms                                                                                                               | 430 ms: 1.02x faster                                                                                                     |
| coroutines                 | 26.1 ms                                                                                                              | 25.7 ms: 1.01x faster                                                                                                    |
| async_generators           | 341 ms                                                                                                               | 355 ms: 1.04x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.39 sec                                                                                                             | 1.51 sec: 1.09x slower                                                                                                   |
| asyncio_tcp                | 459 ms                                                                                                               | 569 ms: 1.24x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 107 ms                                                                                                               | 56.2 ms: 1.90x faster                                                                                                    |
| pidigits       | 147 ms                                                                                                               | 146 ms: 1.01x faster                                                                                                     |
| float          | 76.8 ms                                                                                                              | 78.7 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.23x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                                                               | 120 ms: 1.03x faster                                                                                                     |
| regex_v8       | 17.0 ms                                                                                                              | 16.6 ms: 1.03x faster                                                                                                    |
| regex_effbot   | 1.73 ms                                                                                                              | 1.74 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 279 us                                                                                                               | 157 us: 1.78x faster                                                                                                     |
| tomli_loads          | 2.08 sec                                                                                                             | 1.56 sec: 1.33x faster                                                                                                   |
| xml_etree_generate   | 91.2 ms                                                                                                              | 71.8 ms: 1.27x faster                                                                                                    |
| xml_etree_process    | 65.7 ms                                                                                                              | 52.1 ms: 1.26x faster                                                                                                    |
| pickle_pure_python   | 363 us                                                                                                               | 329 us: 1.10x faster                                                                                                     |
| xml_etree_iterparse  | 91.6 ms                                                                                                              | 87.8 ms: 1.04x faster                                                                                                    |
| xml_etree_parse      | 108 ms                                                                                                               | 105 ms: 1.03x faster                                                                                                     |
| unpickle_list        | 3.11 us                                                                                                              | 3.08 us: 1.01x faster                                                                                                    |
| pickle_list          | 3.86 us                                                                                                              | 3.93 us: 1.02x slower                                                                                                    |
| json_dumps           | 8.45 ms                                                                                                              | 8.63 ms: 1.02x slower                                                                                                    |
| json_loads           | 20.5 us                                                                                                              | 20.9 us: 1.02x slower                                                                                                    |
| unpickle             | 11.3 us                                                                                                              | 11.6 us: 1.02x slower                                                                                                    |
| pickle               | 9.60 us                                                                                                              | 9.86 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.11x faster                                                                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 27.0 ms                                                                                                              | 27.2 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.1 ms                                                                                                              | 7.25 ms: 1.80x faster                                                                                                    |
| genshi_xml      | 50.0 ms                                                                                                              | 50.7 ms: 1.01x slower                                                                                                    |
| genshi_text     | 24.3 ms                                                                                                              | 24.7 ms: 1.02x slower                                                                                                    |
| django_template | 37.3 ms                                                                                                              | 38.0 ms: 1.02x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.14x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json | results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 107 ms                                                                                                               | 56.2 ms: 1.90x faster                                                                                                    |
| mako                       | 13.1 ms                                                                                                              | 7.25 ms: 1.80x faster                                                                                                    |
| unpickle_pure_python       | 279 us                                                                                                               | 157 us: 1.78x faster                                                                                                     |
| scimark_sparse_mat_mult    | 4.41 ms                                                                                                              | 2.80 ms: 1.58x faster                                                                                                    |
| scimark_fft                | 277 ms                                                                                                               | 189 ms: 1.47x faster                                                                                                     |
| fannkuch                   | 413 ms                                                                                                               | 284 ms: 1.45x faster                                                                                                     |
| bpe_tokeniser              | 4.33 sec                                                                                                             | 3.06 sec: 1.41x faster                                                                                                   |
| tomli_loads                | 2.08 sec                                                                                                             | 1.56 sec: 1.33x faster                                                                                                   |
| crypto_pyaes               | 79.8 ms                                                                                                              | 62.0 ms: 1.29x faster                                                                                                    |
| pprint_pformat             | 1.76 sec                                                                                                             | 1.37 sec: 1.29x faster                                                                                                   |
| pprint_safe_repr           | 856 ms                                                                                                               | 670 ms: 1.28x faster                                                                                                     |
| xml_etree_generate         | 91.2 ms                                                                                                              | 71.8 ms: 1.27x faster                                                                                                    |
| xml_etree_process          | 65.7 ms                                                                                                              | 52.1 ms: 1.26x faster                                                                                                    |
| comprehensions             | 19.8 us                                                                                                              | 15.8 us: 1.26x faster                                                                                                    |
| telco                      | 6.26 ms                                                                                                              | 5.24 ms: 1.19x faster                                                                                                    |
| pyflate                    | 462 ms                                                                                                               | 387 ms: 1.19x faster                                                                                                     |
| sqlglot_v2_parse           | 1.35 ms                                                                                                              | 1.14 ms: 1.18x faster                                                                                                    |
| meteor_contest             | 93.2 ms                                                                                                              | 81.6 ms: 1.14x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.62 ms                                                                                                              | 1.42 ms: 1.14x faster                                                                                                    |
| pickle_pure_python         | 363 us                                                                                                               | 329 us: 1.10x faster                                                                                                     |
| connected_components       | 351 ms                                                                                                               | 324 ms: 1.08x faster                                                                                                     |
| k_core                     | 1.81 sec                                                                                                             | 1.68 sec: 1.08x faster                                                                                                   |
| unpack_sequence            | 83.6 ns                                                                                                              | 77.6 ns: 1.08x faster                                                                                                    |
| typing_runtime_protocols   | 155 us                                                                                                               | 144 us: 1.08x faster                                                                                                     |
| sqlite_synth               | 1.85 us                                                                                                              | 1.73 us: 1.07x faster                                                                                                    |
| pycparser                  | 988 ms                                                                                                               | 927 ms: 1.07x faster                                                                                                     |
| shortest_path              | 383 ms                                                                                                               | 365 ms: 1.05x faster                                                                                                     |
| async_tree_none            | 243 ms                                                                                                               | 232 ms: 1.05x faster                                                                                                     |
| nqueens                    | 94.5 ms                                                                                                              | 90.4 ms: 1.05x faster                                                                                                    |
| xml_etree_iterparse        | 91.6 ms                                                                                                              | 87.8 ms: 1.04x faster                                                                                                    |
| async_tree_none_tg         | 237 ms                                                                                                               | 228 ms: 1.04x faster                                                                                                     |
| async_tree_memoization     | 296 ms                                                                                                               | 285 ms: 1.04x faster                                                                                                     |
| sqlglot_v2_optimize        | 51.1 ms                                                                                                              | 49.2 ms: 1.04x faster                                                                                                    |
| regex_compile              | 124 ms                                                                                                               | 120 ms: 1.03x faster                                                                                                     |
| async_tree_memoization_tg  | 294 ms                                                                                                               | 284 ms: 1.03x faster                                                                                                     |
| async_tree_io              | 547 ms                                                                                                               | 531 ms: 1.03x faster                                                                                                     |
| 2to3                       | 296 ms                                                                                                               | 288 ms: 1.03x faster                                                                                                     |
| regex_v8                   | 17.0 ms                                                                                                              | 16.6 ms: 1.03x faster                                                                                                    |
| async_tree_io_tg           | 566 ms                                                                                                               | 551 ms: 1.03x faster                                                                                                     |
| gc_traversal               | 2.93 ms                                                                                                              | 2.85 ms: 1.03x faster                                                                                                    |
| xml_etree_parse            | 108 ms                                                                                                               | 105 ms: 1.03x faster                                                                                                     |
| sqlglot_v2_normalize       | 106 ms                                                                                                               | 104 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 442 ms                                                                                                               | 432 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 437 ms                                                                                                               | 430 ms: 1.02x faster                                                                                                     |
| coroutines                 | 26.1 ms                                                                                                              | 25.7 ms: 1.01x faster                                                                                                    |
| richards                   | 52.3 ms                                                                                                              | 51.7 ms: 1.01x faster                                                                                                    |
| sympy_sum                  | 116 ms                                                                                                               | 115 ms: 1.01x faster                                                                                                     |
| subparsers                 | 22.8 ms                                                                                                              | 22.6 ms: 1.01x faster                                                                                                    |
| unpickle_list              | 3.11 us                                                                                                              | 3.08 us: 1.01x faster                                                                                                    |
| pidigits                   | 147 ms                                                                                                               | 146 ms: 1.01x faster                                                                                                     |
| sympy_str                  | 234 ms                                                                                                               | 233 ms: 1.00x faster                                                                                                     |
| coverage                   | 471 ms                                                                                                               | 473 ms: 1.00x slower                                                                                                     |
| sympy_expand               | 402 ms                                                                                                               | 404 ms: 1.01x slower                                                                                                     |
| regex_effbot               | 1.73 ms                                                                                                              | 1.74 ms: 1.01x slower                                                                                                    |
| python_startup             | 27.0 ms                                                                                                              | 27.2 ms: 1.01x slower                                                                                                    |
| scimark_sor                | 133 ms                                                                                                               | 135 ms: 1.01x slower                                                                                                     |
| scimark_lu                 | 120 ms                                                                                                               | 122 ms: 1.01x slower                                                                                                     |
| html5lib                   | 51.2 ms                                                                                                              | 51.9 ms: 1.01x slower                                                                                                    |
| thrift                     | 103 ms                                                                                                               | 104 ms: 1.01x slower                                                                                                     |
| raytrace                   | 303 ms                                                                                                               | 307 ms: 1.01x slower                                                                                                     |
| genshi_xml                 | 50.0 ms                                                                                                              | 50.7 ms: 1.01x slower                                                                                                    |
| pathlib                    | 34.3 ms                                                                                                              | 34.8 ms: 1.01x slower                                                                                                    |
| logging_format             | 9.91 us                                                                                                              | 10.1 us: 1.01x slower                                                                                                    |
| sympy_integrate            | 16.7 ms                                                                                                              | 17.0 ms: 1.01x slower                                                                                                    |
| genshi_text                | 24.3 ms                                                                                                              | 24.7 ms: 1.02x slower                                                                                                    |
| deepcopy                   | 267 us                                                                                                               | 271 us: 1.02x slower                                                                                                     |
| pickle_list                | 3.86 us                                                                                                              | 3.93 us: 1.02x slower                                                                                                    |
| many_optionals             | 556 us                                                                                                               | 566 us: 1.02x slower                                                                                                     |
| django_template            | 37.3 ms                                                                                                              | 38.0 ms: 1.02x slower                                                                                                    |
| mdp                        | 1.17 sec                                                                                                             | 1.19 sec: 1.02x slower                                                                                                   |
| json_dumps                 | 8.45 ms                                                                                                              | 8.63 ms: 1.02x slower                                                                                                    |
| json_loads                 | 20.5 us                                                                                                              | 20.9 us: 1.02x slower                                                                                                    |
| unpickle                   | 11.3 us                                                                                                              | 11.6 us: 1.02x slower                                                                                                    |
| generators                 | 36.4 ms                                                                                                              | 37.3 ms: 1.02x slower                                                                                                    |
| create_gc_cycles           | 1.45 ms                                                                                                              | 1.48 ms: 1.02x slower                                                                                                    |
| float                      | 76.8 ms                                                                                                              | 78.7 ms: 1.03x slower                                                                                                    |
| go                         | 134 ms                                                                                                               | 137 ms: 1.03x slower                                                                                                     |
| pickle                     | 9.60 us                                                                                                              | 9.86 us: 1.03x slower                                                                                                    |
| spectral_norm              | 111 ms                                                                                                               | 115 ms: 1.04x slower                                                                                                     |
| async_generators           | 341 ms                                                                                                               | 355 ms: 1.04x slower                                                                                                     |
| deepcopy_memo              | 33.6 us                                                                                                              | 35.1 us: 1.04x slower                                                                                                    |
| deltablue                  | 4.38 ms                                                                                                              | 4.57 ms: 1.04x slower                                                                                                    |
| hexiom                     | 7.46 ms                                                                                                              | 7.80 ms: 1.05x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.39 sec                                                                                                             | 1.51 sec: 1.09x slower                                                                                                   |
| asyncio_tcp                | 459 ms                                                                                                               | 569 ms: 1.24x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (17): bench_thread_pool, asyncio_websockets, python_startup_no_site, json, richards_super, scimark_monte_carlo, deepcopy_reduce, pickle_dict, logging_silent, dulwich_log, logging_simple, regex_dna, sphinx, docutils, chaos, bench_mp_pool, pylint

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown