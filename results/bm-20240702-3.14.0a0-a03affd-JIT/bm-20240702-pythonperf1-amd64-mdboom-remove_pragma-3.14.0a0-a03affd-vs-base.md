# Results vs. base

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.00x slower
- HPT reliability: 85.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.77 sec                                                                   | 1.79 sec: 1.01x slower                                              |
| html5lib       | 37.5 ms                                                                    | 39.6 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                        |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 46.5 ms                                                                    | 46.1 ms: 1.01x faster                                               |
| pidigits       | 150 ms                                                                     | 149 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 88.7 ms                                                                    | 90.2 ms: 1.02x slower                                               |
| regex_dna      | 120 ms                                                                     | 122 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                        |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 138 us                                                                     | 136 us: 1.02x faster                                                |
| xml_etree_generate   | 53.8 ms                                                                    | 53.4 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 61.0 ms                                                                    | 60.6 ms: 1.01x faster                                               |
| json_loads           | 14.1 us                                                                    | 14.3 us: 1.01x slower                                               |
| tomli_loads          | 1.27 sec                                                                   | 1.29 sec: 1.02x slower                                              |
| pickle_pure_python   | 178 us                                                                     | 182 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                        |

Benchmark hidden because not significant (3): json_dumps, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 19.1 ms                                                                    | 18.3 ms: 1.04x faster                                               |
| django_template | 26.7 ms                                                                    | 26.3 ms: 1.02x faster                                               |
| genshi_xml      | 46.2 ms                                                                    | 45.9 ms: 1.01x faster                                               |
| mako            | 5.12 ms                                                                    | 5.30 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|--------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coverage                 | 48.8 ms                                                                    | 46.2 ms: 1.06x faster                                               |
| genshi_text              | 19.1 ms                                                                    | 18.3 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult  | 2.16 ms                                                                    | 2.08 ms: 1.04x faster                                               |
| scimark_sor              | 94.5 ms                                                                    | 92.0 ms: 1.03x faster                                               |
| thrift                   | 538 us                                                                     | 524 us: 1.03x faster                                                |
| scimark_fft              | 151 ms                                                                     | 147 ms: 1.02x faster                                                |
| coroutines               | 14.6 ms                                                                    | 14.3 ms: 1.02x faster                                               |
| async_generators         | 276 ms                                                                     | 270 ms: 1.02x faster                                                |
| unpickle_pure_python     | 138 us                                                                     | 136 us: 1.02x faster                                                |
| django_template          | 26.7 ms                                                                    | 26.3 ms: 1.02x faster                                               |
| scimark_monte_carlo      | 39.2 ms                                                                    | 38.6 ms: 1.02x faster                                               |
| deltablue                | 2.36 ms                                                                    | 2.32 ms: 1.02x faster                                               |
| pyflate                  | 265 ms                                                                     | 261 ms: 1.02x faster                                                |
| chaos                    | 41.0 ms                                                                    | 40.5 ms: 1.01x faster                                               |
| json                     | 2.99 ms                                                                    | 2.96 ms: 1.01x faster                                               |
| float                    | 46.5 ms                                                                    | 46.1 ms: 1.01x faster                                               |
| xml_etree_generate       | 53.8 ms                                                                    | 53.4 ms: 1.01x faster                                               |
| xml_etree_iterparse      | 61.0 ms                                                                    | 60.6 ms: 1.01x faster                                               |
| genshi_xml               | 46.2 ms                                                                    | 45.9 ms: 1.01x faster                                               |
| crypto_pyaes             | 41.4 ms                                                                    | 41.1 ms: 1.01x faster                                               |
| mdp                      | 1.41 sec                                                                   | 1.40 sec: 1.01x faster                                              |
| pidigits                 | 150 ms                                                                     | 149 ms: 1.00x faster                                                |
| comprehensions           | 10.4 us                                                                    | 10.5 us: 1.00x slower                                               |
| richards                 | 30.5 ms                                                                    | 30.6 ms: 1.00x slower                                               |
| logging_simple           | 5.87 us                                                                    | 5.91 us: 1.01x slower                                               |
| hexiom                   | 4.66 ms                                                                    | 4.69 ms: 1.01x slower                                               |
| pprint_safe_repr         | 479 ms                                                                     | 482 ms: 1.01x slower                                                |
| typing_runtime_protocols | 113 us                                                                     | 114 us: 1.01x slower                                                |
| sqlglot_transpile        | 1.05 ms                                                                    | 1.06 ms: 1.01x slower                                               |
| json_loads               | 14.1 us                                                                    | 14.3 us: 1.01x slower                                               |
| sqlglot_normalize        | 194 ms                                                                     | 196 ms: 1.01x slower                                                |
| docutils                 | 1.77 sec                                                                   | 1.79 sec: 1.01x slower                                              |
| scimark_lu               | 75.6 ms                                                                    | 76.4 ms: 1.01x slower                                               |
| sympy_expand             | 313 ms                                                                     | 316 ms: 1.01x slower                                                |
| deepcopy                 | 179 us                                                                     | 181 us: 1.01x slower                                                |
| sqlglot_parse            | 818 us                                                                     | 827 us: 1.01x slower                                                |
| raytrace                 | 184 ms                                                                     | 186 ms: 1.01x slower                                                |
| richards_super           | 34.6 ms                                                                    | 35.0 ms: 1.01x slower                                               |
| sqlglot_optimize         | 36.1 ms                                                                    | 36.6 ms: 1.01x slower                                               |
| telco                    | 4.49 ms                                                                    | 4.56 ms: 1.02x slower                                               |
| sympy_str                | 180 ms                                                                     | 183 ms: 1.02x slower                                                |
| regex_compile            | 88.7 ms                                                                    | 90.2 ms: 1.02x slower                                               |
| regex_dna                | 120 ms                                                                     | 122 ms: 1.02x slower                                                |
| tomli_loads              | 1.27 sec                                                                   | 1.29 sec: 1.02x slower                                              |
| nqueens                  | 60.4 ms                                                                    | 61.7 ms: 1.02x slower                                               |
| pprint_pformat           | 978 ms                                                                     | 1.00 sec: 1.02x slower                                              |
| pickle_pure_python       | 178 us                                                                     | 182 us: 1.03x slower                                                |
| deepcopy_reduce          | 1.82 us                                                                    | 1.87 us: 1.03x slower                                               |
| mako                     | 5.12 ms                                                                    | 5.30 ms: 1.04x slower                                               |
| html5lib                 | 37.5 ms                                                                    | 39.6 ms: 1.06x slower                                               |
| pycparser                | 801 ms                                                                     | 862 ms: 1.08x slower                                                |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                        |

Benchmark hidden because not significant (36): asyncio_tcp_ssl, sympy_integrate, async_tree_cpu_io_mixed_tg, create_gc_cycles, deepcopy_memo, nbody, json_dumps, logging_silent, async_tree_cpu_io_mixed, fannkuch, async_tree_io, regex_effbot, generators, python_startup, xml_etree_process, spectral_norm, python_startup_no_site, logging_format, async_tree_memoization_tg, meteor_contest, 2to3, asyncio_tcp, go, pylint, gc_traversal, xml_etree_parse, pathlib, bench_mp_pool, async_tree_io_tg, sympy_sum, tornado_http, async_tree_none, async_tree_none_tg, async_tree_memoization, bench_thread_pool, regex_v8

# HPT report

- Reliability score: 85.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown