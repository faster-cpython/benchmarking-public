# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: linux-aarch64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 361 ms                                                                  | 353 ms: 1.02x faster                                                  |
| chameleon      | 9.28 ms                                                                 | 9.09 ms: 1.02x faster                                                 |
| html5lib       | 71.4 ms                                                                 | 70.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 116 ms                                                                  | 113 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                          |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 172 ms                                                                  | 165 ms: 1.04x faster                                                  |
| regex_v8       | 30.5 ms                                                                 | 30.1 ms: 1.02x faster                                                 |
| regex_dna      | 254 ms                                                                  | 251 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                                  | 110 ms: 1.03x faster                                                  |
| unpickle_pure_python | 278 us                                                                  | 272 us: 1.02x faster                                                  |
| unpickle_list        | 6.41 us                                                                 | 6.35 us: 1.01x faster                                                 |
| tomli_loads          | 2.63 sec                                                                | 2.62 sec: 1.01x faster                                                |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                          |

Benchmark hidden because not significant (10): xml_etree_iterparse, pickle_dict, pickle, json_dumps, unpickle, xml_etree_process, json_loads, pickle_list, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 35.3 ms                                                                 | 33.2 ms: 1.06x faster                                                 |
| genshi_xml      | 83.8 ms                                                                 | 80.0 ms: 1.05x faster                                                 |
| django_template | 51.5 ms                                                                 | 49.3 ms: 1.05x faster                                                 |
| mako            | 12.9 ms                                                                 | 12.6 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                                   | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text              | 35.3 ms                                                                 | 33.2 ms: 1.06x faster                                                 |
| fannkuch                 | 460 ms                                                                  | 437 ms: 1.05x faster                                                  |
| genshi_xml               | 83.8 ms                                                                 | 80.0 ms: 1.05x faster                                                 |
| crypto_pyaes             | 90.7 ms                                                                 | 86.7 ms: 1.05x faster                                                 |
| hexiom                   | 9.07 ms                                                                 | 8.67 ms: 1.05x faster                                                 |
| django_template          | 51.5 ms                                                                 | 49.3 ms: 1.05x faster                                                 |
| regex_compile            | 172 ms                                                                  | 165 ms: 1.04x faster                                                  |
| nqueens                  | 119 ms                                                                  | 114 ms: 1.04x faster                                                  |
| richards                 | 54.7 ms                                                                 | 52.7 ms: 1.04x faster                                                 |
| chaos                    | 88.8 ms                                                                 | 85.6 ms: 1.04x faster                                                 |
| telco                    | 10.3 ms                                                                 | 9.90 ms: 1.04x faster                                                 |
| pprint_pformat           | 2.30 sec                                                                | 2.22 sec: 1.04x faster                                                |
| dulwich_log              | 71.9 ms                                                                 | 69.5 ms: 1.04x faster                                                 |
| pyflate                  | 633 ms                                                                  | 613 ms: 1.03x faster                                                  |
| sympy_str                | 323 ms                                                                  | 313 ms: 1.03x faster                                                  |
| logging_silent           | 140 ns                                                                  | 136 ns: 1.03x faster                                                  |
| scimark_monte_carlo      | 92.8 ms                                                                 | 90.0 ms: 1.03x faster                                                 |
| pprint_safe_repr         | 1.10 sec                                                                | 1.07 sec: 1.03x faster                                                |
| deepcopy_memo            | 50.0 us                                                                 | 48.7 us: 1.03x faster                                                 |
| xml_etree_generate       | 113 ms                                                                  | 110 ms: 1.03x faster                                                  |
| nbody                    | 116 ms                                                                  | 113 ms: 1.03x faster                                                  |
| deepcopy_reduce          | 4.72 us                                                                 | 4.61 us: 1.03x faster                                                 |
| spectral_norm            | 147 ms                                                                  | 143 ms: 1.02x faster                                                  |
| unpickle_pure_python     | 278 us                                                                  | 272 us: 1.02x faster                                                  |
| deepcopy                 | 503 us                                                                  | 492 us: 1.02x faster                                                  |
| mako                     | 12.9 ms                                                                 | 12.6 ms: 1.02x faster                                                 |
| typing_runtime_protocols | 208 us                                                                  | 204 us: 1.02x faster                                                  |
| scimark_fft              | 461 ms                                                                  | 451 ms: 1.02x faster                                                  |
| 2to3                     | 361 ms                                                                  | 353 ms: 1.02x faster                                                  |
| go                       | 179 ms                                                                  | 176 ms: 1.02x faster                                                  |
| sqlglot_optimize         | 70.3 ms                                                                 | 68.9 ms: 1.02x faster                                                 |
| chameleon                | 9.28 ms                                                                 | 9.09 ms: 1.02x faster                                                 |
| richards_super           | 61.4 ms                                                                 | 60.2 ms: 1.02x faster                                                 |
| json                     | 5.72 ms                                                                 | 5.62 ms: 1.02x faster                                                 |
| sympy_expand             | 541 ms                                                                  | 532 ms: 1.02x faster                                                  |
| scimark_lu               | 183 ms                                                                  | 179 ms: 1.02x faster                                                  |
| regex_v8                 | 30.5 ms                                                                 | 30.1 ms: 1.02x faster                                                 |
| sympy_integrate          | 26.0 ms                                                                 | 25.6 ms: 1.02x faster                                                 |
| html5lib                 | 71.4 ms                                                                 | 70.4 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.60 ms                                                                 | 1.58 ms: 1.01x faster                                                 |
| regex_dna                | 254 ms                                                                  | 251 ms: 1.01x faster                                                  |
| raytrace                 | 324 ms                                                                  | 321 ms: 1.01x faster                                                  |
| unpickle_list            | 6.41 us                                                                 | 6.35 us: 1.01x faster                                                 |
| bench_thread_pool        | 1.33 ms                                                                 | 1.32 ms: 1.01x faster                                                 |
| tomli_loads              | 2.63 sec                                                                | 2.62 sec: 1.01x faster                                                |
| scimark_sparse_mat_mult  | 6.91 ms                                                                 | 6.87 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl          | 2.26 sec                                                                | 2.29 sec: 1.01x slower                                                |
| asyncio_tcp              | 617 ms                                                                  | 629 ms: 1.02x slower                                                  |
| bench_mp_pool            | 8.11 ms                                                                 | 8.28 ms: 1.02x slower                                                 |
| gc_traversal             | 5.10 ms                                                                 | 5.27 ms: 1.03x slower                                                 |
| Geometric mean           | (ref)                                                                   | 1.01x faster                                                          |

Benchmark hidden because not significant (48): sympy_sum, create_gc_cycles, async_tree_io_tg, async_tree_none, xml_etree_iterparse, logging_simple, sqlglot_normalize, logging_format, async_tree_memoization, pycparser, pickle_dict, deltablue, pickle, json_dumps, docutils, async_tree_none_tg, unpickle, async_tree_memoization_tg, xml_etree_process, comprehensions, sqlite_synth, float, meteor_contest, generators, regex_effbot, pidigits, tornado_http, async_generators, json_loads, mdp, async_tree_io, sqlglot_transpile, python_startup, scimark_sor, asyncio_websockets, thrift, pathlib, python_startup_no_site, pylint, pickle_list, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, dask, coverage, pickle_pure_python, coroutines, xml_etree_parse, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x