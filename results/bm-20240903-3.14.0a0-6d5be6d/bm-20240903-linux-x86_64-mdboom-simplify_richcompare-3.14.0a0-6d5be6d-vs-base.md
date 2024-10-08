# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x slower
- HPT reliability: 57.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 257 ms: 1.00x slower                                                  |
| html5lib       | 64.1 ms                                                               | 61.8 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io  | 935 ms                                                                | 928 ms: 1.01x faster                                                  |
| asyncio_tcp    | 484 ms                                                                | 482 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (11): async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines, async_generators, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                | 187 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.76 ms: 1.02x faster                                                 |
| regex_v8       | 26.2 ms                                                               | 26.8 ms: 1.02x slower                                                 |
| regex_compile  | 127 ms                                                                | 130 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 157 ms                                                                | 154 ms: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                               | 28.6 us: 1.01x faster                                                 |
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                                | 302 us: 1.01x slower                                                  |
| unpickle_pure_python | 212 us                                                                | 216 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, tomli_loads, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.13 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                 |
| django_template | 33.9 ms                                                               | 33.5 ms: 1.01x faster                                                 |
| genshi_text     | 21.9 ms                                                               | 23.0 ms: 1.05x slower                                                 |
| genshi_xml      | 49.0 ms                                                               | 51.5 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib                 | 64.1 ms                                                               | 61.8 ms: 1.04x faster                                                 |
| xml_etree_parse          | 157 ms                                                                | 154 ms: 1.02x faster                                                  |
| json                     | 5.38 ms                                                               | 5.27 ms: 1.02x faster                                                 |
| regex_effbot             | 3.83 ms                                                               | 3.76 ms: 1.02x faster                                                 |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                 |
| mako                     | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                 |
| crypto_pyaes             | 73.4 ms                                                               | 72.4 ms: 1.01x faster                                                 |
| deepcopy_memo            | 30.2 us                                                               | 29.8 us: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.13 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                 |
| django_template          | 33.9 ms                                                               | 33.5 ms: 1.01x faster                                                 |
| coverage                 | 85.8 ms                                                               | 84.9 ms: 1.01x faster                                                 |
| json_loads               | 28.9 us                                                               | 28.6 us: 1.01x faster                                                 |
| json_dumps               | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| logging_silent           | 103 ns                                                                | 102 ns: 1.01x faster                                                  |
| nqueens                  | 81.0 ms                                                               | 80.4 ms: 1.01x faster                                                 |
| async_tree_io            | 935 ms                                                                | 928 ms: 1.01x faster                                                  |
| richards_super           | 52.1 ms                                                               | 51.7 ms: 1.01x faster                                                 |
| pidigits                 | 188 ms                                                                | 187 ms: 1.01x faster                                                  |
| richards                 | 46.2 ms                                                               | 46.0 ms: 1.00x faster                                                 |
| asyncio_tcp              | 484 ms                                                                | 482 ms: 1.00x faster                                                  |
| hexiom                   | 6.21 ms                                                               | 6.19 ms: 1.00x faster                                                 |
| sqlglot_optimize         | 53.5 ms                                                               | 53.4 ms: 1.00x faster                                                 |
| meteor_contest           | 106 ms                                                                | 106 ms: 1.00x slower                                                  |
| 2to3                     | 256 ms                                                                | 257 ms: 1.00x slower                                                  |
| chaos                    | 58.5 ms                                                               | 58.7 ms: 1.00x slower                                                 |
| scimark_sor              | 126 ms                                                                | 126 ms: 1.00x slower                                                  |
| fannkuch                 | 405 ms                                                                | 407 ms: 1.00x slower                                                  |
| mdp                      | 2.56 sec                                                              | 2.57 sec: 1.00x slower                                                |
| sqlglot_transpile        | 1.58 ms                                                               | 1.58 ms: 1.00x slower                                                 |
| bench_thread_pool        | 783 us                                                                | 787 us: 1.01x slower                                                  |
| deepcopy_reduce          | 2.73 us                                                               | 2.75 us: 1.01x slower                                                 |
| deepcopy                 | 262 us                                                                | 264 us: 1.01x slower                                                  |
| sympy_str                | 268 ms                                                                | 270 ms: 1.01x slower                                                  |
| deltablue                | 3.17 ms                                                               | 3.20 ms: 1.01x slower                                                 |
| pickle_pure_python       | 300 us                                                                | 302 us: 1.01x slower                                                  |
| sympy_expand             | 455 ms                                                                | 459 ms: 1.01x slower                                                  |
| sympy_sum                | 147 ms                                                                | 149 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 67.4 ms                                                               | 68.2 ms: 1.01x slower                                                 |
| go                       | 118 ms                                                                | 119 ms: 1.01x slower                                                  |
| pathlib                  | 16.0 ms                                                               | 16.2 ms: 1.01x slower                                                 |
| pyflate                  | 471 ms                                                                | 478 ms: 1.01x slower                                                  |
| gc_traversal             | 3.73 ms                                                               | 3.78 ms: 1.01x slower                                                 |
| unpickle_pure_python     | 212 us                                                                | 216 us: 1.02x slower                                                  |
| raytrace                 | 260 ms                                                                | 264 ms: 1.02x slower                                                  |
| regex_v8                 | 26.2 ms                                                               | 26.8 ms: 1.02x slower                                                 |
| regex_compile            | 127 ms                                                                | 130 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 4.63 ms                                                               | 4.77 ms: 1.03x slower                                                 |
| typing_runtime_protocols | 158 us                                                                | 165 us: 1.05x slower                                                  |
| genshi_text              | 21.9 ms                                                               | 23.0 ms: 1.05x slower                                                 |
| genshi_xml               | 49.0 ms                                                               | 51.5 ms: 1.05x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (37): async_tree_none, async_tree_io_tg, xml_etree_iterparse, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, bpe_tokeniser, logging_simple, async_tree_cpu_io_mixed, thrift, async_tree_cpu_io_mixed_tg, coroutines, docutils, pylint, async_generators, telco, sqlglot_normalize, tomli_loads, pycparser, float, xml_etree_process, xml_etree_generate, pprint_safe_repr, bench_mp_pool, sympy_integrate, asyncio_tcp_ssl, regex_dna, generators, scimark_lu, nbody, asyncio_websockets, sqlglot_parse, pprint_pformat, tornado_http, logging_format, scimark_fft, spectral_norm

# HPT report

- Reliability score: 57.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x