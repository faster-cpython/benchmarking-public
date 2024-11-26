# Results vs. base

- fork: faster-cpython
- ref: more_robust_immortal
- machine: darwin-arm64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 160 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_tg | 41.9 ms                                                               | 41.7 ms: 1.01x faster                                                           |
| async_generators    | 277 ms                                                                | 276 ms: 1.00x faster                                                            |
| async_tree_io       | 592 ms                                                                | 593 ms: 1.00x slower                                                            |
| async_tree_eager    | 59.5 ms                                                               | 59.7 ms: 1.00x slower                                                           |
| coroutines          | 16.3 ms                                                               | 16.6 ms: 1.02x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (16): asyncio_tcp, asyncio_tcp_ssl, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_memoization, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                | 283 ms: 1.00x slower                                                            |
| float          | 48.3 ms                                                               | 48.9 ms: 1.01x slower                                                           |
| nbody          | 59.7 ms                                                               | 65.4 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 67.6 ms                                                               | 67.8 ms: 1.00x slower                                                           |
| regex_dna      | 146 ms                                                                | 148 ms: 1.01x slower                                                            |
| regex_effbot   | 2.59 ms                                                               | 2.63 ms: 1.02x slower                                                           |
| regex_v8       | 16.4 ms                                                               | 16.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 6.26 ms                                                               | 6.22 ms: 1.01x faster                                                           |
| pickle_dict          | 18.2 us                                                               | 18.1 us: 1.01x faster                                                           |
| xml_etree_process    | 37.7 ms                                                               | 37.4 ms: 1.01x faster                                                           |
| unpickle_list        | 2.97 us                                                               | 2.96 us: 1.01x faster                                                           |
| xml_etree_generate   | 52.3 ms                                                               | 52.1 ms: 1.00x faster                                                           |
| unpickle_pure_python | 141 us                                                                | 142 us: 1.00x slower                                                            |
| pickle               | 7.31 us                                                               | 7.33 us: 1.00x slower                                                           |
| pickle_pure_python   | 182 us                                                                | 184 us: 1.01x slower                                                            |
| tomli_loads          | 1.48 sec                                                              | 1.49 sec: 1.01x slower                                                          |
| xml_etree_parse      | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| pickle_list          | 2.90 us                                                               | 2.96 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): unpickle, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 16.9 ms                                                               | 17.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 29.9 ms                                                               | 29.8 ms: 1.00x faster                                                           |
| mako           | 6.88 ms                                                               | 6.97 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20241009-darwin-arm64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| richards_super          | 35.0 ms                                                               | 34.4 ms: 1.02x faster                                                           |
| richards                | 31.7 ms                                                               | 31.2 ms: 1.02x faster                                                           |
| logging_simple          | 3.09 us                                                               | 3.05 us: 1.01x faster                                                           |
| unpack_sequence         | 26.7 ns                                                               | 26.4 ns: 1.01x faster                                                           |
| json_dumps              | 6.26 ms                                                               | 6.22 ms: 1.01x faster                                                           |
| logging_format          | 3.36 us                                                               | 3.34 us: 1.01x faster                                                           |
| async_tree_eager_tg     | 41.9 ms                                                               | 41.7 ms: 1.01x faster                                                           |
| deepcopy_memo           | 17.2 us                                                               | 17.1 us: 1.01x faster                                                           |
| pickle_dict             | 18.2 us                                                               | 18.1 us: 1.01x faster                                                           |
| xml_etree_process       | 37.7 ms                                                               | 37.4 ms: 1.01x faster                                                           |
| unpickle_list           | 2.97 us                                                               | 2.96 us: 1.01x faster                                                           |
| xml_etree_generate      | 52.3 ms                                                               | 52.1 ms: 1.00x faster                                                           |
| 2to3                    | 160 ms                                                                | 160 ms: 1.00x faster                                                            |
| genshi_xml              | 29.9 ms                                                               | 29.8 ms: 1.00x faster                                                           |
| thrift                  | 417 us                                                                | 416 us: 1.00x faster                                                            |
| meteor_contest          | 70.8 ms                                                               | 70.5 ms: 1.00x faster                                                           |
| comprehensions          | 11.1 us                                                               | 11.0 us: 1.00x faster                                                           |
| async_generators        | 277 ms                                                                | 276 ms: 1.00x faster                                                            |
| gc_traversal            | 2.49 ms                                                               | 2.49 ms: 1.00x faster                                                           |
| sqlglot_normalize       | 166 ms                                                                | 166 ms: 1.00x slower                                                            |
| pprint_safe_repr        | 456 ms                                                                | 457 ms: 1.00x slower                                                            |
| bpe_tokeniser           | 3.07 sec                                                              | 3.07 sec: 1.00x slower                                                          |
| async_tree_io           | 592 ms                                                                | 593 ms: 1.00x slower                                                            |
| pidigits                | 282 ms                                                                | 283 ms: 1.00x slower                                                            |
| unpickle_pure_python    | 141 us                                                                | 142 us: 1.00x slower                                                            |
| pickle                  | 7.31 us                                                               | 7.33 us: 1.00x slower                                                           |
| go                      | 81.4 ms                                                               | 81.6 ms: 1.00x slower                                                           |
| regex_compile           | 67.6 ms                                                               | 67.8 ms: 1.00x slower                                                           |
| async_tree_eager        | 59.5 ms                                                               | 59.7 ms: 1.00x slower                                                           |
| sympy_expand            | 225 ms                                                                | 226 ms: 1.01x slower                                                            |
| create_gc_cycles        | 913 us                                                                | 918 us: 1.01x slower                                                            |
| pyflate                 | 324 ms                                                                | 326 ms: 1.01x slower                                                            |
| sympy_sum               | 69.3 ms                                                               | 69.7 ms: 1.01x slower                                                           |
| sqlglot_transpile       | 891 us                                                                | 896 us: 1.01x slower                                                            |
| hexiom                  | 4.12 ms                                                               | 4.14 ms: 1.01x slower                                                           |
| deltablue               | 2.21 ms                                                               | 2.23 ms: 1.01x slower                                                           |
| pickle_pure_python      | 182 us                                                                | 184 us: 1.01x slower                                                            |
| scimark_sor             | 94.4 ms                                                               | 95.1 ms: 1.01x slower                                                           |
| sympy_str               | 133 ms                                                                | 134 ms: 1.01x slower                                                            |
| pprint_pformat          | 932 ms                                                                | 940 ms: 1.01x slower                                                            |
| crypto_pyaes            | 50.7 ms                                                               | 51.2 ms: 1.01x slower                                                           |
| python_startup          | 16.9 ms                                                               | 17.0 ms: 1.01x slower                                                           |
| regex_dna               | 146 ms                                                                | 148 ms: 1.01x slower                                                            |
| generators              | 20.1 ms                                                               | 20.3 ms: 1.01x slower                                                           |
| coverage                | 43.5 ms                                                               | 43.9 ms: 1.01x slower                                                           |
| spectral_norm           | 69.4 ms                                                               | 70.2 ms: 1.01x slower                                                           |
| float                   | 48.3 ms                                                               | 48.9 ms: 1.01x slower                                                           |
| tomli_loads             | 1.48 sec                                                              | 1.49 sec: 1.01x slower                                                          |
| scimark_sparse_mat_mult | 2.78 ms                                                               | 2.82 ms: 1.01x slower                                                           |
| xml_etree_parse         | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| sqlite_synth            | 1.50 us                                                               | 1.52 us: 1.01x slower                                                           |
| nqueens                 | 53.7 ms                                                               | 54.4 ms: 1.01x slower                                                           |
| pathlib                 | 21.7 ms                                                               | 21.9 ms: 1.01x slower                                                           |
| mako                    | 6.88 ms                                                               | 6.97 ms: 1.01x slower                                                           |
| scimark_lu              | 65.8 ms                                                               | 66.9 ms: 1.02x slower                                                           |
| regex_effbot            | 2.59 ms                                                               | 2.63 ms: 1.02x slower                                                           |
| raytrace                | 150 ms                                                                | 153 ms: 1.02x slower                                                            |
| regex_v8                | 16.4 ms                                                               | 16.7 ms: 1.02x slower                                                           |
| coroutines              | 16.3 ms                                                               | 16.6 ms: 1.02x slower                                                           |
| pickle_list             | 2.90 us                                                               | 2.96 us: 1.02x slower                                                           |
| chaos                   | 35.5 ms                                                               | 36.3 ms: 1.02x slower                                                           |
| telco                   | 4.47 ms                                                               | 4.64 ms: 1.04x slower                                                           |
| scimark_monte_carlo     | 42.7 ms                                                               | 44.4 ms: 1.04x slower                                                           |
| scimark_fft             | 183 ms                                                                | 191 ms: 1.04x slower                                                            |
| nbody                   | 59.7 ms                                                               | 65.4 ms: 1.10x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (40): asyncio_tcp, asyncio_tcp_ssl, typing_runtime_protocols, async_tree_io_tg, deepcopy_reduce, async_tree_none_tg, async_tree_memoization_tg, unpickle, sqlglot_optimize, django_template, async_tree_cpu_io_mixed_tg, bench_thread_pool, docutils, asyncio_websockets, async_tree_eager_io, dulwich_log, async_tree_eager_cpu_io_mixed_tg, fannkuch, json_loads, sympy_integrate, logging_silent, deepcopy, async_tree_cpu_io_mixed, pylint, async_tree_none, mdp, async_tree_eager_cpu_io_mixed, sqlglot_parse, async_tree_eager_memoization, genshi_text, async_tree_eager_io_tg, async_tree_memoization, async_tree_eager_memoization_tg, html5lib, xml_etree_iterparse, json, bench_mp_pool, pycparser, python_startup_no_site, tornado_http

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x