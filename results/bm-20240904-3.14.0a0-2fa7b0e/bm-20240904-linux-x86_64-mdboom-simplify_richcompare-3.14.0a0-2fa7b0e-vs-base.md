# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.004x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tornado_http   | 90.1 ms                                                               | 90.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines              | 23.1 ms                                                               | 22.7 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| asyncio_websockets      | 557 ms                                                                | 559 ms: 1.00x slower                                                  |
| async_tree_io           | 930 ms                                                                | 937 ms: 1.01x slower                                                  |
| async_generators        | 437 ms                                                                | 445 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 556 ms                                                                | 567 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, asyncio_tcp, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| nbody          | 84.1 ms                                                               | 86.0 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.77 ms: 1.01x faster                                                 |
| regex_v8       | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| regex_dna      | 220 ms                                                                | 222 ms: 1.01x slower                                                  |
| regex_compile  | 128 ms                                                                | 131 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 210 us: 1.01x faster                                                  |
| tomli_loads          | 2.09 sec                                                              | 2.10 sec: 1.01x slower                                                |
| xml_etree_process    | 58.7 ms                                                               | 59.4 ms: 1.01x slower                                                 |
| xml_etree_generate   | 84.6 ms                                                               | 86.0 ms: 1.02x slower                                                 |
| xml_etree_iterparse  | 104 ms                                                                | 106 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (4): json_dumps, pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                                 |
| django_template | 33.7 ms                                                               | 34.0 ms: 1.01x slower                                                 |
| genshi_xml      | 49.5 ms                                                               | 50.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| spectral_norm            | 114 ms                                                                | 108 ms: 1.05x faster                                                  |
| deepcopy_reduce          | 2.72 us                                                               | 2.65 us: 1.02x faster                                                 |
| coroutines               | 23.1 ms                                                               | 22.7 ms: 1.02x faster                                                 |
| unpickle_pure_python     | 213 us                                                                | 210 us: 1.01x faster                                                  |
| pycparser                | 1.20 sec                                                              | 1.18 sec: 1.01x faster                                                |
| regex_effbot             | 3.81 ms                                                               | 3.77 ms: 1.01x faster                                                 |
| telco                    | 8.42 ms                                                               | 8.34 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| nqueens                  | 81.3 ms                                                               | 80.7 ms: 1.01x faster                                                 |
| richards                 | 46.0 ms                                                               | 45.7 ms: 1.01x faster                                                 |
| pathlib                  | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                 |
| fannkuch                 | 406 ms                                                                | 403 ms: 1.01x faster                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| pyflate                  | 474 ms                                                                | 471 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| regex_v8                 | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| mako                     | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                                 |
| pidigits                 | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| gc_traversal             | 3.72 ms                                                               | 3.72 ms: 1.00x slower                                                 |
| sqlglot_optimize         | 53.6 ms                                                               | 53.8 ms: 1.00x slower                                                 |
| sympy_integrate          | 19.5 ms                                                               | 19.6 ms: 1.00x slower                                                 |
| asyncio_websockets       | 557 ms                                                                | 559 ms: 1.00x slower                                                  |
| chaos                    | 58.4 ms                                                               | 58.7 ms: 1.00x slower                                                 |
| scimark_sor              | 125 ms                                                                | 126 ms: 1.01x slower                                                  |
| tomli_loads              | 2.09 sec                                                              | 2.10 sec: 1.01x slower                                                |
| create_gc_cycles         | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult  | 4.71 ms                                                               | 4.74 ms: 1.01x slower                                                 |
| async_tree_io            | 930 ms                                                                | 937 ms: 1.01x slower                                                  |
| go                       | 118 ms                                                                | 119 ms: 1.01x slower                                                  |
| tornado_http             | 90.1 ms                                                               | 90.7 ms: 1.01x slower                                                 |
| bench_thread_pool        | 780 us                                                                | 787 us: 1.01x slower                                                  |
| sympy_sum                | 147 ms                                                                | 148 ms: 1.01x slower                                                  |
| comprehensions           | 16.6 us                                                               | 16.7 us: 1.01x slower                                                 |
| sympy_str                | 267 ms                                                                | 270 ms: 1.01x slower                                                  |
| django_template          | 33.7 ms                                                               | 34.0 ms: 1.01x slower                                                 |
| meteor_contest           | 107 ms                                                                | 108 ms: 1.01x slower                                                  |
| regex_dna                | 220 ms                                                                | 222 ms: 1.01x slower                                                  |
| xml_etree_process        | 58.7 ms                                                               | 59.4 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 108 ms                                                                | 109 ms: 1.01x slower                                                  |
| sympy_expand             | 455 ms                                                                | 461 ms: 1.01x slower                                                  |
| pprint_pformat           | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                                |
| crypto_pyaes             | 72.6 ms                                                               | 73.6 ms: 1.01x slower                                                 |
| hexiom                   | 6.20 ms                                                               | 6.29 ms: 1.01x slower                                                 |
| bpe_tokeniser            | 4.78 sec                                                              | 4.86 sec: 1.02x slower                                                |
| xml_etree_generate       | 84.6 ms                                                               | 86.0 ms: 1.02x slower                                                 |
| raytrace                 | 259 ms                                                                | 263 ms: 1.02x slower                                                  |
| pprint_safe_repr         | 704 ms                                                                | 717 ms: 1.02x slower                                                  |
| async_generators         | 437 ms                                                                | 445 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed  | 556 ms                                                                | 567 ms: 1.02x slower                                                  |
| typing_runtime_protocols | 158 us                                                                | 161 us: 1.02x slower                                                  |
| scimark_fft              | 353 ms                                                                | 360 ms: 1.02x slower                                                  |
| regex_compile            | 128 ms                                                                | 131 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 104 ms                                                                | 106 ms: 1.02x slower                                                  |
| nbody                    | 84.1 ms                                                               | 86.0 ms: 1.02x slower                                                 |
| deepcopy_memo            | 29.7 us                                                               | 30.3 us: 1.02x slower                                                 |
| scimark_lu               | 113 ms                                                                | 115 ms: 1.02x slower                                                  |
| genshi_xml               | 49.5 ms                                                               | 50.9 ms: 1.03x slower                                                 |
| scimark_monte_carlo      | 66.5 ms                                                               | 68.7 ms: 1.03x slower                                                 |
| logging_silent           | 97.9 ns                                                               | 101 ns: 1.04x slower                                                  |
| mdp                      | 2.52 sec                                                              | 2.64 sec: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (28): deepcopy, json_dumps, sqlglot_transpile, async_tree_memoization, docutils, thrift, json, float, 2to3, logging_simple, generators, bench_mp_pool, pickle_pure_python, asyncio_tcp, richards_super, deltablue, xml_etree_parse, async_tree_memoization_tg, json_loads, pylint, logging_format, coverage, html5lib, genshi_text, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x