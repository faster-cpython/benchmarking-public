# Results vs. base

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: linux-aarch64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                  | 376 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 739 ms                                                                  | 725 ms: 1.02x faster                                                        |
| async_tree_memoization_tg  | 556 ms                                                                  | 550 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                                |

Benchmark hidden because not significant (11): async_tree_memoization, asyncio_tcp_ssl, async_tree_io, async_tree_none_tg, coroutines, asyncio_websockets, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_io_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 114 ms                                                                  | 111 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                                  | 186 ms: 1.02x faster                                                        |
| regex_effbot   | 4.91 ms                                                                 | 4.99 ms: 1.02x slower                                                       |
| regex_dna      | 245 ms                                                                  | 255 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle           | 19.8 us                                                                 | 19.3 us: 1.03x faster                                                       |
| unpickle_list      | 6.44 us                                                                 | 6.34 us: 1.02x faster                                                       |
| xml_etree_parse    | 189 ms                                                                  | 187 ms: 1.01x faster                                                        |
| pickle_pure_python | 388 us                                                                  | 384 us: 1.01x faster                                                        |
| xml_etree_generate | 111 ms                                                                  | 110 ms: 1.01x faster                                                        |
| json_dumps         | 13.5 ms                                                                 | 13.9 ms: 1.03x slower                                                       |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                                |

Benchmark hidden because not significant (8): xml_etree_iterparse, xml_etree_process, pickle_list, json_loads, pickle, unpickle_pure_python, tomli_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 51.2 ms                                                                 | 50.5 ms: 1.01x faster                                                       |
| mako            | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240910-arminc-aarch64-python-3597642ed57d184511ca-3.14.0a0-3597642 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| telco                      | 10.7 ms                                                                 | 10.3 ms: 1.04x faster                                                       |
| logging_format             | 8.27 us                                                                 | 8.00 us: 1.03x faster                                                       |
| sympy_sum                  | 215 ms                                                                  | 208 ms: 1.03x faster                                                        |
| nqueens                    | 127 ms                                                                  | 123 ms: 1.03x faster                                                        |
| nbody                      | 114 ms                                                                  | 111 ms: 1.03x faster                                                        |
| hexiom                     | 10.2 ms                                                                 | 9.91 ms: 1.03x faster                                                       |
| deepcopy                   | 411 us                                                                  | 400 us: 1.03x faster                                                        |
| unpickle                   | 19.8 us                                                                 | 19.3 us: 1.03x faster                                                       |
| sympy_str                  | 364 ms                                                                  | 355 ms: 1.02x faster                                                        |
| pyflate                    | 655 ms                                                                  | 641 ms: 1.02x faster                                                        |
| regex_compile              | 190 ms                                                                  | 186 ms: 1.02x faster                                                        |
| sympy_expand               | 612 ms                                                                  | 601 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 739 ms                                                                  | 725 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 1.25 sec                                                                | 1.23 sec: 1.02x faster                                                      |
| deepcopy_reduce            | 3.93 us                                                                 | 3.86 us: 1.02x faster                                                       |
| unpickle_list              | 6.44 us                                                                 | 6.34 us: 1.02x faster                                                       |
| dulwich_log                | 82.0 ms                                                                 | 80.7 ms: 1.02x faster                                                       |
| json                       | 5.70 ms                                                                 | 5.61 ms: 1.02x faster                                                       |
| django_template            | 51.2 ms                                                                 | 50.5 ms: 1.01x faster                                                       |
| pprint_pformat             | 2.61 sec                                                                | 2.57 sec: 1.01x faster                                                      |
| pycparser                  | 1.53 sec                                                                | 1.50 sec: 1.01x faster                                                      |
| xml_etree_parse            | 189 ms                                                                  | 187 ms: 1.01x faster                                                        |
| 2to3                       | 381 ms                                                                  | 376 ms: 1.01x faster                                                        |
| scimark_fft                | 460 ms                                                                  | 454 ms: 1.01x faster                                                        |
| fannkuch                   | 503 ms                                                                  | 497 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 151 ms                                                                  | 149 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 556 ms                                                                  | 550 ms: 1.01x faster                                                        |
| pickle_pure_python         | 388 us                                                                  | 384 us: 1.01x faster                                                        |
| scimark_sor                | 151 ms                                                                  | 149 ms: 1.01x faster                                                        |
| spectral_norm              | 147 ms                                                                  | 146 ms: 1.01x faster                                                        |
| mako                       | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                       |
| go                         | 186 ms                                                                  | 184 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.97 sec                                                                | 5.94 sec: 1.01x faster                                                      |
| xml_etree_generate         | 111 ms                                                                  | 110 ms: 1.01x faster                                                        |
| python_startup             | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                       |
| regex_effbot               | 4.91 ms                                                                 | 4.99 ms: 1.02x slower                                                       |
| unpack_sequence            | 146 ns                                                                  | 149 ns: 1.02x slower                                                        |
| json_dumps                 | 13.5 ms                                                                 | 13.9 ms: 1.03x slower                                                       |
| regex_dna                  | 245 ms                                                                  | 255 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                                   | 1.01x faster                                                                |

Benchmark hidden because not significant (58): xml_etree_iterparse, pathlib, typing_runtime_protocols, xml_etree_process, richards, html5lib, gc_traversal, scimark_sparse_mat_mult, async_tree_memoization, logging_simple, bench_thread_pool, pickle_list, sympy_integrate, json_loads, raytrace, deltablue, pickle, unpickle_pure_python, coverage, asyncio_tcp_ssl, async_tree_io, comprehensions, sqlglot_transpile, crypto_pyaes, sqlite_synth, tomli_loads, logging_silent, pickle_dict, pidigits, sqlglot_optimize, meteor_contest, docutils, richards_super, pylint, async_tree_none_tg, coroutines, float, mdp, python_startup_no_site, asyncio_websockets, bench_mp_pool, create_gc_cycles, genshi_xml, async_tree_none, genshi_text, sqlglot_parse, regex_v8, scimark_lu, scimark_monte_carlo, thrift, deepcopy_memo, async_tree_cpu_io_mixed, asyncio_tcp, chaos, async_tree_io_tg, async_generators, generators, tornado_http

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x