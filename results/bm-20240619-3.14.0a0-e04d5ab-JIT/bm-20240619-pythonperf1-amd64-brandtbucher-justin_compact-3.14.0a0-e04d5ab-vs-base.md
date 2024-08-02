# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.00x slower
- HPT reliability: 98.88%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 228 ms                                                                     | 230 ms: 1.01x slower                                                       |
| docutils       | 1.73 sec                                                                   | 1.74 sec: 1.01x slower                                                     |
| html5lib       | 35.5 ms                                                                    | 35.7 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 589 ms                                                                     | 598 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 43.7 ms                                                                    | 44.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 86.4 ms                                                                    | 82.4 ms: 1.05x faster                                                      |
| regex_dna      | 118 ms                                                                     | 120 ms: 1.01x slower                                                       |
| regex_effbot   | 1.57 ms                                                                    | 1.60 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list         | 2.94 us                                                                    | 2.83 us: 1.04x faster                                                      |
| pickle              | 7.45 us                                                                    | 7.27 us: 1.02x faster                                                      |
| pickle_dict         | 18.2 us                                                                    | 17.8 us: 1.02x faster                                                      |
| unpickle_list       | 2.83 us                                                                    | 2.78 us: 1.02x faster                                                      |
| tomli_loads         | 1.19 sec                                                                   | 1.19 sec: 1.01x faster                                                     |
| json_loads          | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                      |
| xml_etree_process   | 35.6 ms                                                                    | 35.9 ms: 1.01x slower                                                      |
| xml_etree_generate  | 50.8 ms                                                                    | 51.4 ms: 1.01x slower                                                      |
| xml_etree_parse     | 92.6 ms                                                                    | 94.1 ms: 1.02x slower                                                      |
| xml_etree_iterparse | 59.9 ms                                                                    | 61.0 ms: 1.02x slower                                                      |
| json_dumps          | 5.55 ms                                                                    | 5.68 ms: 1.02x slower                                                      |
| unpickle            | 8.64 us                                                                    | 8.86 us: 1.03x slower                                                      |
| Geometric mean      | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                                    | 18.2 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 42.8 ms                                                                    | 39.4 ms: 1.09x faster                                                      |
| genshi_text    | 17.2 ms                                                                    | 16.2 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                               |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| hexiom                   | 4.60 ms                                                                    | 4.13 ms: 1.11x faster                                                      |
| genshi_xml               | 42.8 ms                                                                    | 39.4 ms: 1.09x faster                                                      |
| genshi_text              | 17.2 ms                                                                    | 16.2 ms: 1.07x faster                                                      |
| deepcopy                 | 175 us                                                                     | 166 us: 1.05x faster                                                       |
| nqueens                  | 60.5 ms                                                                    | 57.6 ms: 1.05x faster                                                      |
| regex_compile            | 86.4 ms                                                                    | 82.4 ms: 1.05x faster                                                      |
| pickle_list              | 2.94 us                                                                    | 2.83 us: 1.04x faster                                                      |
| coroutines               | 13.1 ms                                                                    | 12.7 ms: 1.03x faster                                                      |
| async_generators         | 252 ms                                                                     | 246 ms: 1.02x faster                                                       |
| pickle                   | 7.45 us                                                                    | 7.27 us: 1.02x faster                                                      |
| logging_format           | 6.04 us                                                                    | 5.91 us: 1.02x faster                                                      |
| go                       | 89.3 ms                                                                    | 87.4 ms: 1.02x faster                                                      |
| pickle_dict              | 18.2 us                                                                    | 17.8 us: 1.02x faster                                                      |
| bench_thread_pool        | 765 us                                                                     | 751 us: 1.02x faster                                                       |
| sqlglot_transpile        | 998 us                                                                     | 980 us: 1.02x faster                                                       |
| unpickle_list            | 2.83 us                                                                    | 2.78 us: 1.02x faster                                                      |
| pyflate                  | 257 ms                                                                     | 254 ms: 1.01x faster                                                       |
| deepcopy_reduce          | 1.72 us                                                                    | 1.70 us: 1.01x faster                                                      |
| raytrace                 | 171 ms                                                                     | 170 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 109 us                                                                     | 108 us: 1.01x faster                                                       |
| chaos                    | 38.6 ms                                                                    | 38.2 ms: 1.01x faster                                                      |
| logging_simple           | 5.52 us                                                                    | 5.48 us: 1.01x faster                                                      |
| tomli_loads              | 1.19 sec                                                                   | 1.19 sec: 1.01x faster                                                     |
| pathlib                  | 75.5 ms                                                                    | 75.1 ms: 1.01x faster                                                      |
| sympy_expand             | 301 ms                                                                     | 300 ms: 1.00x faster                                                       |
| html5lib                 | 35.5 ms                                                                    | 35.7 ms: 1.00x slower                                                      |
| docutils                 | 1.73 sec                                                                   | 1.74 sec: 1.01x slower                                                     |
| json_loads               | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                      |
| 2to3                     | 228 ms                                                                     | 230 ms: 1.01x slower                                                       |
| xml_etree_process        | 35.6 ms                                                                    | 35.9 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 458 ms                                                                     | 462 ms: 1.01x slower                                                       |
| python_startup_no_site   | 18.1 ms                                                                    | 18.2 ms: 1.01x slower                                                      |
| float                    | 43.7 ms                                                                    | 44.2 ms: 1.01x slower                                                      |
| bench_mp_pool            | 69.8 ms                                                                    | 70.6 ms: 1.01x slower                                                      |
| thrift                   | 490 us                                                                     | 495 us: 1.01x slower                                                       |
| xml_etree_generate       | 50.8 ms                                                                    | 51.4 ms: 1.01x slower                                                      |
| sqlglot_parse            | 771 us                                                                     | 781 us: 1.01x slower                                                       |
| regex_dna                | 118 ms                                                                     | 120 ms: 1.01x slower                                                       |
| pprint_pformat           | 942 ms                                                                     | 956 ms: 1.01x slower                                                       |
| telco                    | 4.50 ms                                                                    | 4.57 ms: 1.02x slower                                                      |
| async_tree_io_tg         | 589 ms                                                                     | 598 ms: 1.02x slower                                                       |
| deltablue                | 2.09 ms                                                                    | 2.13 ms: 1.02x slower                                                      |
| comprehensions           | 10.1 us                                                                    | 10.3 us: 1.02x slower                                                      |
| xml_etree_parse          | 92.6 ms                                                                    | 94.1 ms: 1.02x slower                                                      |
| richards_super           | 34.2 ms                                                                    | 34.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 59.9 ms                                                                    | 61.0 ms: 1.02x slower                                                      |
| regex_effbot             | 1.57 ms                                                                    | 1.60 ms: 1.02x slower                                                      |
| richards                 | 30.4 ms                                                                    | 31.0 ms: 1.02x slower                                                      |
| fannkuch                 | 215 ms                                                                     | 219 ms: 1.02x slower                                                       |
| json_dumps               | 5.55 ms                                                                    | 5.68 ms: 1.02x slower                                                      |
| coverage                 | 44.5 ms                                                                    | 45.6 ms: 1.03x slower                                                      |
| mdp                      | 1.35 sec                                                                   | 1.39 sec: 1.03x slower                                                     |
| unpickle                 | 8.64 us                                                                    | 8.86 us: 1.03x slower                                                      |
| scimark_monte_carlo      | 37.0 ms                                                                    | 38.0 ms: 1.03x slower                                                      |
| scimark_fft              | 147 ms                                                                     | 151 ms: 1.03x slower                                                       |
| sqlite_synth             | 1.60 us                                                                    | 1.65 us: 1.03x slower                                                      |
| generators               | 20.0 ms                                                                    | 20.7 ms: 1.03x slower                                                      |
| scimark_sor              | 80.2 ms                                                                    | 83.3 ms: 1.04x slower                                                      |
| json                     | 2.96 ms                                                                    | 3.08 ms: 1.04x slower                                                      |
| spectral_norm            | 44.6 ms                                                                    | 46.7 ms: 1.05x slower                                                      |
| asyncio_tcp_ssl          | 1.42 sec                                                                   | 1.51 sec: 1.06x slower                                                     |
| scimark_lu               | 67.7 ms                                                                    | 72.3 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult  | 2.06 ms                                                                    | 2.21 ms: 1.07x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (29): nbody, deepcopy_memo, pylint, async_tree_io, gc_traversal, sympy_str, django_template, mako, tornado_http, crypto_pyaes, async_tree_none, logging_silent, pickle_pure_python, meteor_contest, sqlglot_optimize, sympy_integrate, python_startup, async_tree_memoization, sympy_sum, pidigits, create_gc_cycles, async_tree_none_tg, pycparser, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, unpickle_pure_python, regex_v8

# HPT report

- Reliability score: 98.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown