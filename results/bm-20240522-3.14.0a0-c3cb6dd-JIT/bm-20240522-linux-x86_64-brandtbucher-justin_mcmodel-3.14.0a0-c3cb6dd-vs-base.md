# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: c3cb6dd
- commit date: 2024-05-22
- overall geometric mean: 1.01x faster
- HPT reliability: 99.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 275 ms: 1.02x faster                                                  |
| chameleon      | 7.05 ms                                                               | 7.14 ms: 1.01x slower                                                 |
| docutils       | 2.95 sec                                                              | 2.90 sec: 1.02x faster                                                |
| html5lib       | 66.6 ms                                                               | 66.3 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 80.8 ms                                                               | 79.3 ms: 1.02x faster                                                 |
| float          | 72.9 ms                                                               | 72.2 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.3 ms                                                               | 23.7 ms: 1.11x faster                                                 |
| regex_effbot   | 3.92 ms                                                               | 3.68 ms: 1.07x faster                                                 |
| regex_dna      | 236 ms                                                                | 225 ms: 1.05x faster                                                  |
| regex_compile  | 138 ms                                                                | 135 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 5.37 us                                                               | 5.10 us: 1.05x faster                                                 |
| pickle_dict          | 36.1 us                                                               | 34.8 us: 1.04x faster                                                 |
| pickle_list          | 5.26 us                                                               | 5.10 us: 1.03x faster                                                 |
| unpickle             | 15.5 us                                                               | 15.0 us: 1.03x faster                                                 |
| json_loads           | 28.8 us                                                               | 28.5 us: 1.01x faster                                                 |
| xml_etree_generate   | 82.2 ms                                                               | 82.5 ms: 1.00x slower                                                 |
| json_dumps           | 10.2 ms                                                               | 10.3 ms: 1.01x slower                                                 |
| xml_etree_parse      | 149 ms                                                                | 151 ms: 1.01x slower                                                  |
| pickle               | 11.9 us                                                               | 12.2 us: 1.03x slower                                                 |
| unpickle_pure_python | 221 us                                                                | 227 us: 1.03x slower                                                  |
| tomli_loads          | 1.96 sec                                                              | 2.01 sec: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 58.3 ms                                                               | 54.3 ms: 1.07x faster                                                 |
| genshi_text     | 24.6 ms                                                               | 24.0 ms: 1.02x faster                                                 |
| django_template | 36.3 ms                                                               | 36.0 ms: 1.01x faster                                                 |
| mako            | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8                | 26.3 ms                                                               | 23.7 ms: 1.11x faster                                                 |
| genshi_xml              | 58.3 ms                                                               | 54.3 ms: 1.07x faster                                                 |
| regex_effbot            | 3.92 ms                                                               | 3.68 ms: 1.07x faster                                                 |
| unpickle_list           | 5.37 us                                                               | 5.10 us: 1.05x faster                                                 |
| pycparser               | 1.21 sec                                                              | 1.15 sec: 1.05x faster                                                |
| regex_dna               | 236 ms                                                                | 225 ms: 1.05x faster                                                  |
| pyflate                 | 457 ms                                                                | 439 ms: 1.04x faster                                                  |
| pickle_dict             | 36.1 us                                                               | 34.8 us: 1.04x faster                                                 |
| pickle_list             | 5.26 us                                                               | 5.10 us: 1.03x faster                                                 |
| unpickle                | 15.5 us                                                               | 15.0 us: 1.03x faster                                                 |
| nqueens                 | 87.4 ms                                                               | 85.1 ms: 1.03x faster                                                 |
| regex_compile           | 138 ms                                                                | 135 ms: 1.03x faster                                                  |
| genshi_text             | 24.6 ms                                                               | 24.0 ms: 1.02x faster                                                 |
| go                      | 148 ms                                                                | 145 ms: 1.02x faster                                                  |
| sqlglot_transpile       | 1.63 ms                                                               | 1.59 ms: 1.02x faster                                                 |
| sqlglot_parse           | 1.29 ms                                                               | 1.27 ms: 1.02x faster                                                 |
| nbody                   | 80.8 ms                                                               | 79.3 ms: 1.02x faster                                                 |
| docutils                | 2.95 sec                                                              | 2.90 sec: 1.02x faster                                                |
| sympy_sum               | 171 ms                                                                | 168 ms: 1.02x faster                                                  |
| 2to3                    | 280 ms                                                                | 275 ms: 1.02x faster                                                  |
| richards                | 40.9 ms                                                               | 40.2 ms: 1.02x faster                                                 |
| sqlglot_optimize        | 56.7 ms                                                               | 55.8 ms: 1.02x faster                                                 |
| richards_super          | 47.5 ms                                                               | 46.8 ms: 1.02x faster                                                 |
| deepcopy_reduce         | 3.33 us                                                               | 3.29 us: 1.01x faster                                                 |
| telco                   | 8.24 ms                                                               | 8.13 ms: 1.01x faster                                                 |
| hexiom                  | 6.61 ms                                                               | 6.52 ms: 1.01x faster                                                 |
| gc_traversal            | 3.80 ms                                                               | 3.75 ms: 1.01x faster                                                 |
| sympy_str               | 301 ms                                                                | 297 ms: 1.01x faster                                                  |
| json                    | 5.22 ms                                                               | 5.16 ms: 1.01x faster                                                 |
| sympy_integrate         | 22.4 ms                                                               | 22.2 ms: 1.01x faster                                                 |
| generators              | 30.6 ms                                                               | 30.2 ms: 1.01x faster                                                 |
| sympy_expand            | 509 ms                                                                | 503 ms: 1.01x faster                                                  |
| comprehensions          | 16.6 us                                                               | 16.4 us: 1.01x faster                                                 |
| json_loads              | 28.8 us                                                               | 28.5 us: 1.01x faster                                                 |
| float                   | 72.9 ms                                                               | 72.2 ms: 1.01x faster                                                 |
| thrift                  | 816 us                                                                | 808 us: 1.01x faster                                                  |
| scimark_sor             | 138 ms                                                                | 136 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 113 ms                                                                | 112 ms: 1.01x faster                                                  |
| deepcopy_memo           | 37.8 us                                                               | 37.5 us: 1.01x faster                                                 |
| django_template         | 36.3 ms                                                               | 36.0 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl         | 1.86 sec                                                              | 1.85 sec: 1.00x faster                                                |
| html5lib                | 66.6 ms                                                               | 66.3 ms: 1.00x faster                                                 |
| bench_thread_pool       | 863 us                                                                | 859 us: 1.00x faster                                                  |
| coroutines              | 23.9 ms                                                               | 24.0 ms: 1.00x slower                                                 |
| create_gc_cycles        | 1.79 ms                                                               | 1.79 ms: 1.00x slower                                                 |
| meteor_contest          | 107 ms                                                                | 108 ms: 1.00x slower                                                  |
| dulwich_log             | 68.7 ms                                                               | 68.9 ms: 1.00x slower                                                 |
| xml_etree_generate      | 82.2 ms                                                               | 82.5 ms: 1.00x slower                                                 |
| crypto_pyaes            | 67.8 ms                                                               | 68.2 ms: 1.01x slower                                                 |
| mako                    | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                 |
| json_dumps              | 10.2 ms                                                               | 10.3 ms: 1.01x slower                                                 |
| coverage                | 92.5 ms                                                               | 93.3 ms: 1.01x slower                                                 |
| xml_etree_parse         | 149 ms                                                                | 151 ms: 1.01x slower                                                  |
| sqlite_synth            | 2.85 us                                                               | 2.89 us: 1.01x slower                                                 |
| chameleon               | 7.05 ms                                                               | 7.14 ms: 1.01x slower                                                 |
| logging_simple          | 5.66 us                                                               | 5.74 us: 1.01x slower                                                 |
| logging_silent          | 107 ns                                                                | 109 ns: 1.02x slower                                                  |
| scimark_fft             | 313 ms                                                                | 319 ms: 1.02x slower                                                  |
| async_generators        | 461 ms                                                                | 471 ms: 1.02x slower                                                  |
| asyncio_tcp             | 508 ms                                                                | 519 ms: 1.02x slower                                                  |
| fannkuch                | 355 ms                                                                | 363 ms: 1.02x slower                                                  |
| pickle                  | 11.9 us                                                               | 12.2 us: 1.03x slower                                                 |
| unpickle_pure_python    | 221 us                                                                | 227 us: 1.03x slower                                                  |
| tomli_loads             | 1.96 sec                                                              | 2.01 sec: 1.03x slower                                                |
| logging_format          | 6.28 us                                                               | 6.47 us: 1.03x slower                                                 |
| spectral_norm           | 101 ms                                                                | 105 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult | 4.43 ms                                                               | 4.66 ms: 1.05x slower                                                 |
| mdp                     | 2.58 sec                                                              | 2.76 sec: 1.07x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (30): async_tree_io, deepcopy, pprint_safe_repr, pylint, async_tree_memoization_tg, raytrace, pprint_pformat, dask, xml_etree_iterparse, async_tree_none_tg, async_tree_none, async_tree_io_tg, asyncio_websockets, bench_mp_pool, pathlib, python_startup, python_startup_no_site, pidigits, xml_etree_process, async_tree_cpu_io_mixed_tg, tornado_http, async_tree_cpu_io_mixed, deltablue, typing_runtime_protocols, pickle_pure_python, async_tree_memoization, chaos, scimark_monte_carlo, scimark_lu, flaskblogging

# HPT report

- Reliability score: 99.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x