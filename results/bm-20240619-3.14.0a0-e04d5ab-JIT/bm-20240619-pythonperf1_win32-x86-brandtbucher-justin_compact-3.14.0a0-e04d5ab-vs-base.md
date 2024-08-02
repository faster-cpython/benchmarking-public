# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.00x faster
- HPT reliability: 70.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                         | 258 ms: 1.01x slower                                                           |
| docutils       | 1.91 sec                                                                       | 1.92 sec: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 463 ms                                                                         | 454 ms: 1.02x faster                                                           |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 54.2 ms                                                                        | 52.4 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                         | 118 ms: 1.05x faster                                                           |
| regex_compile  | 95.9 ms                                                                        | 94.3 ms: 1.02x faster                                                          |
| regex_v8       | 16.0 ms                                                                        | 15.7 ms: 1.01x faster                                                          |
| regex_effbot   | 2.00 ms                                                                        | 1.99 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 21.1 us                                                                        | 20.5 us: 1.03x faster                                                          |
| tomli_loads          | 1.50 sec                                                                       | 1.46 sec: 1.03x faster                                                         |
| pickle               | 8.25 us                                                                        | 8.14 us: 1.01x faster                                                          |
| xml_etree_generate   | 58.7 ms                                                                        | 58.4 ms: 1.01x faster                                                          |
| xml_etree_parse      | 103 ms                                                                         | 104 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 61.5 ms                                                                        | 62.0 ms: 1.01x slower                                                          |
| json_loads           | 21.1 us                                                                        | 21.4 us: 1.01x slower                                                          |
| unpickle_pure_python | 144 us                                                                         | 147 us: 1.02x slower                                                           |
| json_dumps           | 6.81 ms                                                                        | 6.97 ms: 1.02x slower                                                          |
| unpickle             | 10.5 us                                                                        | 10.8 us: 1.03x slower                                                          |
| pickle_list          | 3.90 us                                                                        | 4.05 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): unpickle_list, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 53.5 ms                                                                        | 48.5 ms: 1.10x faster                                                          |
| genshi_text     | 22.2 ms                                                                        | 21.2 ms: 1.05x faster                                                          |
| mako            | 5.42 ms                                                                        | 5.34 ms: 1.02x faster                                                          |
| django_template | 32.9 ms                                                                        | 32.8 ms: 1.00x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml                 | 53.5 ms                                                                        | 48.5 ms: 1.10x faster                                                          |
| hexiom                     | 4.65 ms                                                                        | 4.28 ms: 1.09x faster                                                          |
| asyncio_tcp                | 646 ms                                                                         | 608 ms: 1.06x faster                                                           |
| regex_dna                  | 124 ms                                                                         | 118 ms: 1.05x faster                                                           |
| genshi_text                | 22.2 ms                                                                        | 21.2 ms: 1.05x faster                                                          |
| mdp                        | 1.72 sec                                                                       | 1.64 sec: 1.04x faster                                                         |
| sqlite_synth               | 1.97 us                                                                        | 1.90 us: 1.04x faster                                                          |
| spectral_norm              | 49.9 ms                                                                        | 48.2 ms: 1.04x faster                                                          |
| nbody                      | 54.2 ms                                                                        | 52.4 ms: 1.03x faster                                                          |
| sqlglot_parse              | 951 us                                                                         | 921 us: 1.03x faster                                                           |
| deepcopy_memo              | 15.9 us                                                                        | 15.5 us: 1.03x faster                                                          |
| pickle_dict                | 21.1 us                                                                        | 20.5 us: 1.03x faster                                                          |
| tomli_loads                | 1.50 sec                                                                       | 1.46 sec: 1.03x faster                                                         |
| deepcopy                   | 240 us                                                                         | 234 us: 1.03x faster                                                           |
| sqlglot_transpile          | 1.21 ms                                                                        | 1.18 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 463 ms                                                                         | 454 ms: 1.02x faster                                                           |
| pycparser                  | 837 ms                                                                         | 823 ms: 1.02x faster                                                           |
| async_generators           | 304 ms                                                                         | 298 ms: 1.02x faster                                                           |
| regex_compile              | 95.9 ms                                                                        | 94.3 ms: 1.02x faster                                                          |
| go                         | 112 ms                                                                         | 111 ms: 1.02x faster                                                           |
| mako                       | 5.42 ms                                                                        | 5.34 ms: 1.02x faster                                                          |
| logging_simple             | 7.49 us                                                                        | 7.39 us: 1.01x faster                                                          |
| regex_v8                   | 16.0 ms                                                                        | 15.7 ms: 1.01x faster                                                          |
| pickle                     | 8.25 us                                                                        | 8.14 us: 1.01x faster                                                          |
| logging_format             | 8.16 us                                                                        | 8.05 us: 1.01x faster                                                          |
| sqlglot_optimize           | 43.5 ms                                                                        | 43.0 ms: 1.01x faster                                                          |
| sqlglot_normalize          | 235 ms                                                                         | 233 ms: 1.01x faster                                                           |
| telco                      | 5.72 ms                                                                        | 5.66 ms: 1.01x faster                                                          |
| nqueens                    | 71.8 ms                                                                        | 71.2 ms: 1.01x faster                                                          |
| logging_silent             | 57.7 ns                                                                        | 57.3 ns: 1.01x faster                                                          |
| generators                 | 27.8 ms                                                                        | 27.6 ms: 1.01x faster                                                          |
| xml_etree_generate         | 58.7 ms                                                                        | 58.4 ms: 1.01x faster                                                          |
| django_template            | 32.9 ms                                                                        | 32.8 ms: 1.00x faster                                                          |
| regex_effbot               | 2.00 ms                                                                        | 1.99 ms: 1.00x faster                                                          |
| docutils                   | 1.91 sec                                                                       | 1.92 sec: 1.00x slower                                                         |
| coverage                   | 51.0 ms                                                                        | 51.2 ms: 1.00x slower                                                          |
| sympy_sum                  | 109 ms                                                                         | 110 ms: 1.01x slower                                                           |
| sympy_integrate            | 16.0 ms                                                                        | 16.1 ms: 1.01x slower                                                          |
| richards_super             | 38.0 ms                                                                        | 38.2 ms: 1.01x slower                                                          |
| xml_etree_parse            | 103 ms                                                                         | 104 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 61.5 ms                                                                        | 62.0 ms: 1.01x slower                                                          |
| 2to3                       | 256 ms                                                                         | 258 ms: 1.01x slower                                                           |
| richards                   | 33.4 ms                                                                        | 33.7 ms: 1.01x slower                                                          |
| scimark_sor                | 95.9 ms                                                                        | 96.9 ms: 1.01x slower                                                          |
| json_loads                 | 21.1 us                                                                        | 21.4 us: 1.01x slower                                                          |
| sympy_expand               | 387 ms                                                                         | 391 ms: 1.01x slower                                                           |
| sympy_str                  | 216 ms                                                                         | 219 ms: 1.01x slower                                                           |
| raytrace                   | 229 ms                                                                         | 232 ms: 1.01x slower                                                           |
| bench_mp_pool              | 74.8 ms                                                                        | 75.9 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 143 us                                                                         | 146 us: 1.02x slower                                                           |
| pprint_safe_repr           | 562 ms                                                                         | 572 ms: 1.02x slower                                                           |
| thrift                     | 743 us                                                                         | 757 us: 1.02x slower                                                           |
| deepcopy_reduce            | 2.42 us                                                                        | 2.47 us: 1.02x slower                                                          |
| scimark_lu                 | 73.8 ms                                                                        | 75.2 ms: 1.02x slower                                                          |
| pprint_pformat             | 1.16 sec                                                                       | 1.18 sec: 1.02x slower                                                         |
| unpickle_pure_python       | 144 us                                                                         | 147 us: 1.02x slower                                                           |
| meteor_contest             | 72.6 ms                                                                        | 74.2 ms: 1.02x slower                                                          |
| json_dumps                 | 6.81 ms                                                                        | 6.97 ms: 1.02x slower                                                          |
| unpickle                   | 10.5 us                                                                        | 10.8 us: 1.03x slower                                                          |
| scimark_sparse_mat_mult    | 2.40 ms                                                                        | 2.48 ms: 1.03x slower                                                          |
| pickle_list                | 3.90 us                                                                        | 4.05 us: 1.04x slower                                                          |
| scimark_fft                | 165 ms                                                                         | 172 ms: 1.05x slower                                                           |
| fannkuch                   | 214 ms                                                                         | 228 ms: 1.07x slower                                                           |
| scimark_monte_carlo        | 39.6 ms                                                                        | 43.6 ms: 1.10x slower                                                          |
| json                       | 4.37 ms                                                                        | 4.84 ms: 1.11x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed, async_tree_io, gc_traversal, pyflate, unpickle_list, bench_thread_pool, coroutines, comprehensions, async_tree_none, pathlib, html5lib, tornado_http, pidigits, pickle_pure_python, deltablue, pylint, chaos, crypto_pyaes, xml_etree_process, float, python_startup, create_gc_cycles, async_tree_memoization, python_startup_no_site, asyncio_tcp_ssl, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 70.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown