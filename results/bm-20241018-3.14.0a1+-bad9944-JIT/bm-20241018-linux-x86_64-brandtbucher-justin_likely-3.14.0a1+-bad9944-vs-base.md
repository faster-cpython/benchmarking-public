# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                |
| html5lib       | 64.6 ms                                                                | 64.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): 2to3, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 561 ms                                                                 | 556 ms: 1.01x faster                                                  |
| async_generators           | 455 ms                                                                 | 454 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.80 sec                                                               | 1.80 sec: 1.00x slower                                                |
| async_tree_io_tg           | 967 ms                                                                 | 971 ms: 1.00x slower                                                  |
| asyncio_tcp                | 494 ms                                                                 | 499 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, coroutines, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| float          | 75.6 ms                                                                | 76.0 ms: 1.01x slower                                                 |
| nbody          | 83.0 ms                                                                | 84.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                 | 143 ms: 1.01x slower                                                  |
| regex_effbot   | 3.64 ms                                                                | 3.68 ms: 1.01x slower                                                 |
| regex_v8       | 24.2 ms                                                                | 24.7 ms: 1.02x slower                                                 |
| regex_dna      | 210 ms                                                                 | 216 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                                | 34.8 us: 1.02x faster                                                 |
| json_loads           | 26.7 us                                                                | 26.5 us: 1.01x faster                                                 |
| xml_etree_generate   | 78.2 ms                                                                | 78.8 ms: 1.01x slower                                                 |
| unpickle_pure_python | 217 us                                                                 | 218 us: 1.01x slower                                                  |
| xml_etree_process    | 55.0 ms                                                                | 55.5 ms: 1.01x slower                                                 |
| unpickle             | 14.2 us                                                                | 14.3 us: 1.01x slower                                                 |
| json_dumps           | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                                 |
| tomli_loads          | 1.89 sec                                                               | 1.93 sec: 1.02x slower                                                |
| unpickle_list        | 5.29 us                                                                | 5.53 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_iterparse, pickle, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                                | 7.09 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.9 ms                                                                | 25.2 ms: 1.03x faster                                                 |
| django_template | 36.2 ms                                                                | 36.7 ms: 1.01x slower                                                 |
| genshi_xml      | 60.8 ms                                                                | 61.9 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 4.84 ms                                                                | 4.52 ms: 1.07x faster                                                 |
| genshi_text                | 25.9 ms                                                                | 25.2 ms: 1.03x faster                                                 |
| unpack_sequence            | 111 ns                                                                 | 108 ns: 1.02x faster                                                  |
| scimark_sor                | 120 ms                                                                 | 118 ms: 1.02x faster                                                  |
| pickle_dict                | 35.5 us                                                                | 34.8 us: 1.02x faster                                                 |
| logging_format             | 6.19 us                                                                | 6.11 us: 1.01x faster                                                 |
| richards_super             | 47.7 ms                                                                | 47.2 ms: 1.01x faster                                                 |
| html5lib                   | 64.6 ms                                                                | 64.0 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                 | 556 ms: 1.01x faster                                                  |
| deltablue                  | 3.29 ms                                                                | 3.27 ms: 1.01x faster                                                 |
| generators                 | 35.4 ms                                                                | 35.2 ms: 1.01x faster                                                 |
| json_loads                 | 26.7 us                                                                | 26.5 us: 1.01x faster                                                 |
| scimark_lu                 | 113 ms                                                                 | 113 ms: 1.01x faster                                                  |
| logging_silent             | 99.3 ns                                                                | 98.8 ns: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| go                         | 135 ms                                                                 | 134 ms: 1.00x faster                                                  |
| async_generators           | 455 ms                                                                 | 454 ms: 1.00x faster                                                  |
| dulwich_log                | 66.9 ms                                                                | 66.7 ms: 1.00x faster                                                 |
| create_gc_cycles           | 2.68 ms                                                                | 2.68 ms: 1.00x faster                                                 |
| python_startup_no_site     | 7.09 ms                                                                | 7.09 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl            | 1.80 sec                                                               | 1.80 sec: 1.00x slower                                                |
| hexiom                     | 7.05 ms                                                                | 7.07 ms: 1.00x slower                                                 |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.00x slower                                                  |
| async_tree_io_tg           | 967 ms                                                                 | 971 ms: 1.00x slower                                                  |
| docutils                   | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                |
| sympy_str                  | 302 ms                                                                 | 303 ms: 1.01x slower                                                  |
| chaos                      | 59.1 ms                                                                | 59.4 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 60.2 ms                                                                | 60.6 ms: 1.01x slower                                                 |
| float                      | 75.6 ms                                                                | 76.0 ms: 1.01x slower                                                 |
| xml_etree_generate         | 78.2 ms                                                                | 78.8 ms: 1.01x slower                                                 |
| regex_compile              | 142 ms                                                                 | 143 ms: 1.01x slower                                                  |
| deepcopy                   | 272 us                                                                 | 274 us: 1.01x slower                                                  |
| asyncio_tcp                | 494 ms                                                                 | 499 ms: 1.01x slower                                                  |
| sympy_integrate            | 23.4 ms                                                                | 23.6 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 217 us                                                                 | 218 us: 1.01x slower                                                  |
| coverage                   | 83.7 ms                                                                | 84.6 ms: 1.01x slower                                                 |
| xml_etree_process          | 55.0 ms                                                                | 55.5 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.33 ms                                                                | 1.34 ms: 1.01x slower                                                 |
| regex_effbot               | 3.64 ms                                                                | 3.68 ms: 1.01x slower                                                 |
| unpickle                   | 14.2 us                                                                | 14.3 us: 1.01x slower                                                 |
| sympy_expand               | 499 ms                                                                 | 505 ms: 1.01x slower                                                  |
| django_template            | 36.2 ms                                                                | 36.7 ms: 1.01x slower                                                 |
| scimark_fft                | 318 ms                                                                 | 323 ms: 1.02x slower                                                  |
| genshi_xml                 | 60.8 ms                                                                | 61.9 ms: 1.02x slower                                                 |
| nbody                      | 83.0 ms                                                                | 84.5 ms: 1.02x slower                                                 |
| pathlib                    | 15.9 ms                                                                | 16.2 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 729 ms                                                                 | 742 ms: 1.02x slower                                                  |
| regex_v8                   | 24.2 ms                                                                | 24.7 ms: 1.02x slower                                                 |
| json_dumps                 | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                                 |
| tomli_loads                | 1.89 sec                                                               | 1.93 sec: 1.02x slower                                                |
| pycparser                  | 1.15 sec                                                               | 1.17 sec: 1.02x slower                                                |
| nqueens                    | 86.7 ms                                                                | 88.6 ms: 1.02x slower                                                 |
| comprehensions             | 16.9 us                                                                | 17.4 us: 1.03x slower                                                 |
| regex_dna                  | 210 ms                                                                 | 216 ms: 1.03x slower                                                  |
| unpickle_list              | 5.29 us                                                                | 5.53 us: 1.05x slower                                                 |
| pprint_pformat             | 1.48 sec                                                               | 1.56 sec: 1.05x slower                                                |
| scimark_sparse_mat_mult    | 4.59 ms                                                                | 4.90 ms: 1.07x slower                                                 |
| mdp                        | 2.54 sec                                                               | 2.75 sec: 1.08x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (40): mako, json, async_tree_cpu_io_mixed, raytrace, pickle_pure_python, sqlite_synth, thrift, logging_simple, bench_mp_pool, async_tree_none, scimark_monte_carlo, bench_thread_pool, pyflate, spectral_norm, bpe_tokeniser, tornado_http, pylint, python_startup, 2to3, xml_etree_iterparse, sympy_sum, pickle, asyncio_websockets, coroutines, pickle_list, sqlglot_normalize, deepcopy_reduce, async_tree_memoization_tg, richards, crypto_pyaes, sqlglot_transpile, telco, sphinx, xml_etree_parse, async_tree_io, typing_runtime_protocols, deepcopy_memo, async_tree_none_tg, async_tree_memoization, fannkuch

# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x