# Results vs. base

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 216 ms                                                                                                               | 212 ms: 1.02x faster                                                                                                     |
| docutils       | 1.59 sec                                                                                                             | 1.60 sec: 1.01x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 385 ms                                                                                                               | 376 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 202 ms                                                                                                               | 198 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 167 ms                                                                                                               | 164 ms: 1.02x faster                                                                                                     |
| coroutines                 | 14.4 ms                                                                                                              | 14.6 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 329 ms                                                                                                               | 334 ms: 1.02x slower                                                                                                     |
| async_tree_memoization_tg  | 206 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                                                               | 340 ms: 1.02x slower                                                                                                     |
| async_generators           | 230 ms                                                                                                               | 236 ms: 1.02x slower                                                                                                     |
| asyncio_websockets         | 157 ms                                                                                                               | 162 ms: 1.03x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.24 sec                                                                                                             | 1.40 sec: 1.12x slower                                                                                                   |
| asyncio_tcp                | 372 ms                                                                                                               | 489 ms: 1.31x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (2): async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 67.4 ms                                                                                                              | 54.5 ms: 1.24x faster                                                                                                    |
| float          | 45.2 ms                                                                                                              | 43.8 ms: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.09x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 80.4 ms                                                                                                              | 75.9 ms: 1.06x faster                                                                                                    |
| regex_v8       | 13.8 ms                                                                                                              | 13.6 ms: 1.02x faster                                                                                                    |
| regex_dna      | 117 ms                                                                                                               | 118 ms: 1.00x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                                                                             | 1.09 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python | 135 us                                                                                                               | 107 us: 1.27x faster                                                                                                     |
| xml_etree_generate   | 56.7 ms                                                                                                              | 49.2 ms: 1.15x faster                                                                                                    |
| xml_etree_process    | 39.2 ms                                                                                                              | 34.8 ms: 1.13x faster                                                                                                    |
| pickle_pure_python   | 214 us                                                                                                               | 194 us: 1.10x faster                                                                                                     |
| pickle_dict          | 20.5 us                                                                                                              | 19.1 us: 1.08x faster                                                                                                    |
| pickle               | 7.95 us                                                                                                              | 7.67 us: 1.04x faster                                                                                                    |
| json_loads           | 14.4 us                                                                                                              | 13.9 us: 1.03x faster                                                                                                    |
| unpickle_list        | 2.83 us                                                                                                              | 2.75 us: 1.03x faster                                                                                                    |
| xml_etree_iterparse  | 63.9 ms                                                                                                              | 62.7 ms: 1.02x faster                                                                                                    |
| pickle_list          | 3.29 us                                                                                                              | 3.22 us: 1.02x faster                                                                                                    |
| unpickle             | 8.54 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.3 ms                                                                                                              | 25.1 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.67 ms                                                                                                              | 5.28 ms: 1.26x faster                                                                                                    |
| genshi_text     | 15.6 ms                                                                                                              | 15.5 ms: 1.01x faster                                                                                                    |
| django_template | 23.8 ms                                                                                                              | 24.2 ms: 1.02x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm              | 66.6 ms                                                                                                              | 43.0 ms: 1.55x faster                                                                                                    |
| fannkuch                   | 277 ms                                                                                                               | 213 ms: 1.30x faster                                                                                                     |
| scimark_fft                | 174 ms                                                                                                               | 134 ms: 1.30x faster                                                                                                     |
| deepcopy_memo              | 17.4 us                                                                                                              | 13.5 us: 1.29x faster                                                                                                    |
| tomli_loads                | 1.39 sec                                                                                                             | 1.09 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python       | 135 us                                                                                                               | 107 us: 1.27x faster                                                                                                     |
| mako                       | 6.67 ms                                                                                                              | 5.28 ms: 1.26x faster                                                                                                    |
| nbody                      | 67.4 ms                                                                                                              | 54.5 ms: 1.24x faster                                                                                                    |
| pprint_pformat             | 1.00 sec                                                                                                             | 834 ms: 1.20x faster                                                                                                     |
| pprint_safe_repr           | 490 ms                                                                                                               | 411 ms: 1.19x faster                                                                                                     |
| bpe_tokeniser              | 2.97 sec                                                                                                             | 2.51 sec: 1.18x faster                                                                                                   |
| xml_etree_generate         | 56.7 ms                                                                                                              | 49.2 ms: 1.15x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.49 ms                                                                                                              | 2.19 ms: 1.14x faster                                                                                                    |
| pyflate                    | 283 ms                                                                                                               | 250 ms: 1.13x faster                                                                                                     |
| xml_etree_process          | 39.2 ms                                                                                                              | 34.8 ms: 1.13x faster                                                                                                    |
| sqlglot_v2_parse           | 827 us                                                                                                               | 749 us: 1.10x faster                                                                                                     |
| pickle_pure_python         | 214 us                                                                                                               | 194 us: 1.10x faster                                                                                                     |
| crypto_pyaes               | 48.3 ms                                                                                                              | 44.4 ms: 1.09x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                              | 950 us: 1.08x faster                                                                                                     |
| telco                      | 4.20 ms                                                                                                              | 3.90 ms: 1.08x faster                                                                                                    |
| pickle_dict                | 20.5 us                                                                                                              | 19.1 us: 1.08x faster                                                                                                    |
| nqueens                    | 63.4 ms                                                                                                              | 59.4 ms: 1.07x faster                                                                                                    |
| regex_compile              | 80.4 ms                                                                                                              | 75.9 ms: 1.06x faster                                                                                                    |
| deltablue                  | 2.26 ms                                                                                                              | 2.14 ms: 1.06x faster                                                                                                    |
| comprehensions             | 11.1 us                                                                                                              | 10.5 us: 1.06x faster                                                                                                    |
| k_core                     | 1.66 sec                                                                                                             | 1.58 sec: 1.05x faster                                                                                                   |
| richards_super             | 31.3 ms                                                                                                              | 30.0 ms: 1.04x faster                                                                                                    |
| richards                   | 27.7 ms                                                                                                              | 26.6 ms: 1.04x faster                                                                                                    |
| deepcopy_reduce            | 1.79 us                                                                                                              | 1.72 us: 1.04x faster                                                                                                    |
| pickle                     | 7.95 us                                                                                                              | 7.67 us: 1.04x faster                                                                                                    |
| logging_format             | 6.42 us                                                                                                              | 6.20 us: 1.04x faster                                                                                                    |
| hexiom                     | 4.14 ms                                                                                                              | 4.00 ms: 1.04x faster                                                                                                    |
| logging_simple             | 5.96 us                                                                                                              | 5.77 us: 1.03x faster                                                                                                    |
| float                      | 45.2 ms                                                                                                              | 43.8 ms: 1.03x faster                                                                                                    |
| deepcopy                   | 164 us                                                                                                               | 159 us: 1.03x faster                                                                                                     |
| json_loads                 | 14.4 us                                                                                                              | 13.9 us: 1.03x faster                                                                                                    |
| go                         | 76.8 ms                                                                                                              | 74.6 ms: 1.03x faster                                                                                                    |
| unpickle_list              | 2.83 us                                                                                                              | 2.75 us: 1.03x faster                                                                                                    |
| logging_silent             | 56.1 ns                                                                                                              | 54.7 ns: 1.03x faster                                                                                                    |
| raytrace                   | 176 ms                                                                                                               | 172 ms: 1.02x faster                                                                                                     |
| connected_components       | 326 ms                                                                                                               | 319 ms: 1.02x faster                                                                                                     |
| async_tree_io_tg           | 385 ms                                                                                                               | 376 ms: 1.02x faster                                                                                                     |
| shortest_path              | 354 ms                                                                                                               | 347 ms: 1.02x faster                                                                                                     |
| xml_etree_iterparse        | 63.9 ms                                                                                                              | 62.7 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 202 ms                                                                                                               | 198 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 167 ms                                                                                                               | 164 ms: 1.02x faster                                                                                                     |
| pickle_list                | 3.29 us                                                                                                              | 3.22 us: 1.02x faster                                                                                                    |
| 2to3                       | 216 ms                                                                                                               | 212 ms: 1.02x faster                                                                                                     |
| regex_v8                   | 13.8 ms                                                                                                              | 13.6 ms: 1.02x faster                                                                                                    |
| sqlite_synth               | 1.55 us                                                                                                              | 1.53 us: 1.02x faster                                                                                                    |
| scimark_sor                | 77.1 ms                                                                                                              | 76.0 ms: 1.02x faster                                                                                                    |
| dulwich_log                | 38.5 ms                                                                                                              | 38.0 ms: 1.01x faster                                                                                                    |
| scimark_monte_carlo        | 41.1 ms                                                                                                              | 40.6 ms: 1.01x faster                                                                                                    |
| json                       | 2.93 ms                                                                                                              | 2.89 ms: 1.01x faster                                                                                                    |
| mdp                        | 790 ms                                                                                                               | 781 ms: 1.01x faster                                                                                                     |
| sympy_sum                  | 85.2 ms                                                                                                              | 84.4 ms: 1.01x faster                                                                                                    |
| python_startup             | 25.3 ms                                                                                                              | 25.1 ms: 1.01x faster                                                                                                    |
| unpickle                   | 8.54 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| meteor_contest             | 72.3 ms                                                                                                              | 71.8 ms: 1.01x faster                                                                                                    |
| sqlglot_v2_optimize        | 34.1 ms                                                                                                              | 33.8 ms: 1.01x faster                                                                                                    |
| sqlglot_v2_normalize       | 70.0 ms                                                                                                              | 69.5 ms: 1.01x faster                                                                                                    |
| genshi_text                | 15.6 ms                                                                                                              | 15.5 ms: 1.01x faster                                                                                                    |
| regex_dna                  | 117 ms                                                                                                               | 118 ms: 1.00x slower                                                                                                     |
| coroutines                 | 14.4 ms                                                                                                              | 14.6 ms: 1.01x slower                                                                                                    |
| docutils                   | 1.59 sec                                                                                                             | 1.60 sec: 1.01x slower                                                                                                   |
| sympy_integrate            | 12.2 ms                                                                                                              | 12.4 ms: 1.01x slower                                                                                                    |
| django_template            | 23.8 ms                                                                                                              | 24.2 ms: 1.02x slower                                                                                                    |
| sympy_expand               | 281 ms                                                                                                               | 285 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 329 ms                                                                                                               | 334 ms: 1.02x slower                                                                                                     |
| coverage                   | 49.4 ms                                                                                                              | 50.3 ms: 1.02x slower                                                                                                    |
| async_tree_memoization_tg  | 206 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                                                               | 340 ms: 1.02x slower                                                                                                     |
| pycparser                  | 687 ms                                                                                                               | 703 ms: 1.02x slower                                                                                                     |
| async_generators           | 230 ms                                                                                                               | 236 ms: 1.02x slower                                                                                                     |
| typing_runtime_protocols   | 102 us                                                                                                               | 105 us: 1.03x slower                                                                                                     |
| asyncio_websockets         | 157 ms                                                                                                               | 162 ms: 1.03x slower                                                                                                     |
| scimark_lu                 | 58.7 ms                                                                                                              | 62.2 ms: 1.06x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.24 sec                                                                                                             | 1.40 sec: 1.12x slower                                                                                                   |
| asyncio_tcp                | 372 ms                                                                                                               | 489 ms: 1.31x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (23): chaos, subparsers, bench_thread_pool, async_tree_none, pathlib, genshi_xml, sympy_str, thrift, bench_mp_pool, unpack_sequence, pidigits, create_gc_cycles, html5lib, regex_effbot, json_dumps, pylint, generators, sphinx, async_tree_io, xml_etree_parse, python_startup_no_site, gc_traversal, many_optionals

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown