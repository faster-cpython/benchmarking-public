# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x faster
- HPT reliability: 95.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.04 sec                                                                | 3.01 sec: 1.01x faster                                                  |
| tornado_http   | 132 ms                                                                  | 126 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.23 sec                                                                | 2.20 sec: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 728 ms                                                                  | 739 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 721 ms                                                                  | 732 ms: 1.02x slower                                                    |
| async_tree_memoization     | 556 ms                                                                  | 568 ms: 1.02x slower                                                    |
| async_tree_none            | 423 ms                                                                  | 437 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (8): async_generators, async_tree_io, coroutines, async_tree_io_tg, asyncio_tcp, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 111 ms                                                                  | 109 ms: 1.02x faster                                                    |
| float          | 91.9 ms                                                                 | 92.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                  | 127 ms: 1.01x slower                                                    |
| regex_effbot   | 4.84 ms                                                                 | 4.94 ms: 1.02x slower                                                   |
| regex_dna      | 245 ms                                                                  | 254 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads    | 2.64 sec                                                                | 2.63 sec: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (8): json_dumps, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, pickle_pure_python, json_loads, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                                 | 8.80 ms: 1.02x faster                                                   |
| python_startup         | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.6 ms                                                                 | 41.7 ms: 1.02x faster                                                   |
| mako            | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tornado_http               | 132 ms                                                                  | 126 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                                 | 1.23 ms: 1.03x faster                                                   |
| sympy_sum                  | 147 ms                                                                  | 143 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 926 ms                                                                  | 905 ms: 1.02x faster                                                    |
| django_template            | 42.6 ms                                                                 | 41.7 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.90 sec                                                                | 1.87 sec: 1.02x faster                                                  |
| nbody                      | 111 ms                                                                  | 109 ms: 1.02x faster                                                    |
| deepcopy                   | 335 us                                                                  | 329 us: 1.02x faster                                                    |
| sqlglot_transpile          | 1.76 ms                                                                 | 1.73 ms: 1.02x faster                                                   |
| sympy_integrate            | 21.1 ms                                                                 | 20.8 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.43 ms                                                                 | 1.41 ms: 1.02x faster                                                   |
| python_startup_no_site     | 8.94 ms                                                                 | 8.80 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 3.54 us                                                                 | 3.48 us: 1.02x faster                                                   |
| go                         | 138 ms                                                                  | 136 ms: 1.02x faster                                                    |
| logging_format             | 7.80 us                                                                 | 7.69 us: 1.01x faster                                                   |
| nqueens                    | 100 ms                                                                  | 98.9 ms: 1.01x faster                                                   |
| docutils                   | 3.04 sec                                                                | 3.01 sec: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 2.23 sec                                                                | 2.20 sec: 1.01x faster                                                  |
| scimark_fft                | 444 ms                                                                  | 440 ms: 1.01x faster                                                    |
| raytrace                   | 306 ms                                                                  | 303 ms: 1.01x faster                                                    |
| mdp                        | 3.38 sec                                                                | 3.35 sec: 1.01x faster                                                  |
| python_startup             | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| generators                 | 34.9 ms                                                                 | 34.6 ms: 1.01x faster                                                   |
| tomli_loads                | 2.64 sec                                                                | 2.63 sec: 1.00x faster                                                  |
| richards_super             | 58.8 ms                                                                 | 59.2 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                                | 5.94 sec: 1.01x slower                                                  |
| float                      | 91.9 ms                                                                 | 92.6 ms: 1.01x slower                                                   |
| telco                      | 9.97 ms                                                                 | 10.1 ms: 1.01x slower                                                   |
| mako                       | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| regex_compile              | 125 ms                                                                  | 127 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed    | 728 ms                                                                  | 739 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 721 ms                                                                  | 732 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 193 us                                                                  | 197 us: 1.02x slower                                                    |
| regex_effbot               | 4.84 ms                                                                 | 4.94 ms: 1.02x slower                                                   |
| async_tree_memoization     | 556 ms                                                                  | 568 ms: 1.02x slower                                                    |
| pyflate                    | 566 ms                                                                  | 582 ms: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                                  | 115 ms: 1.03x slower                                                    |
| async_tree_none            | 423 ms                                                                  | 437 ms: 1.03x slower                                                    |
| regex_dna                  | 245 ms                                                                  | 254 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (50): genshi_xml, logging_simple, json_dumps, 2to3, pylint, json, sqlglot_normalize, logging_silent, scimark_sparse_mat_mult, chaos, deltablue, fannkuch, sympy_str, async_generators, create_gc_cycles, async_tree_io, sympy_expand, genshi_text, coroutines, thrift, unpickle_pure_python, xml_etree_generate, async_tree_io_tg, xml_etree_iterparse, gc_traversal, html5lib, sqlglot_optimize, scimark_lu, pidigits, pathlib, pickle_pure_python, json_loads, bench_mp_pool, asyncio_tcp, comprehensions, asyncio_websockets, richards, coverage, regex_v8, async_tree_memoization_tg, xml_etree_parse, scimark_sor, spectral_norm, async_tree_none_tg, deepcopy_memo, hexiom, pycparser, crypto_pyaes, xml_etree_process, scimark_monte_carlo

# HPT report

- Reliability score: 95.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x