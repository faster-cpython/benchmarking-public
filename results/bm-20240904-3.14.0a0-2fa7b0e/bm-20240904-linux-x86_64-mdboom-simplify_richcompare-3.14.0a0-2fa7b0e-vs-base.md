# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x faster
- HPT reliability: 90.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 257 ms: 1.00x faster                                                  |
| docutils       | 2.68 sec                                                              | 2.66 sec: 1.01x faster                                                |
| html5lib       | 61.7 ms                                                               | 63.5 ms: 1.03x slower                                                 |
| tornado_http   | 90.3 ms                                                               | 90.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines              | 23.5 ms                                                               | 22.7 ms: 1.04x faster                                                 |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                |
| async_tree_io           | 931 ms                                                                | 937 ms: 1.01x slower                                                  |
| asyncio_tcp             | 475 ms                                                                | 479 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 560 ms                                                                | 567 ms: 1.01x slower                                                  |
| async_tree_none_tg      | 309 ms                                                                | 313 ms: 1.01x slower                                                  |
| async_generators        | 436 ms                                                                | 445 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                               | 77.5 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.77 ms: 1.02x faster                                                 |
| regex_v8       | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| regex_compile  | 130 ms                                                                | 131 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 210 us: 1.03x faster                                                  |
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| pickle_pure_python   | 302 us                                                                | 301 us: 1.00x faster                                                  |
| xml_etree_process    | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                 |
| xml_etree_generate   | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.12 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.5 ms                                                               | 11.2 ms: 1.02x faster                                                 |
| genshi_text    | 22.6 ms                                                               | 23.1 ms: 1.02x slower                                                 |
| genshi_xml     | 49.3 ms                                                               | 50.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| spectral_norm            | 114 ms                                                                | 108 ms: 1.05x faster                                                  |
| deepcopy_reduce          | 2.78 us                                                               | 2.65 us: 1.05x faster                                                 |
| coroutines               | 23.5 ms                                                               | 22.7 ms: 1.04x faster                                                 |
| richards_super           | 53.5 ms                                                               | 51.8 ms: 1.03x faster                                                 |
| unpickle_pure_python     | 217 us                                                                | 210 us: 1.03x faster                                                  |
| richards                 | 46.9 ms                                                               | 45.7 ms: 1.03x faster                                                 |
| mako                     | 11.5 ms                                                               | 11.2 ms: 1.02x faster                                                 |
| logging_silent           | 104 ns                                                                | 101 ns: 1.02x faster                                                  |
| pyflate                  | 480 ms                                                                | 471 ms: 1.02x faster                                                  |
| regex_effbot             | 3.83 ms                                                               | 3.77 ms: 1.02x faster                                                 |
| deepcopy                 | 265 us                                                                | 260 us: 1.02x faster                                                  |
| float                    | 78.7 ms                                                               | 77.5 ms: 1.02x faster                                                 |
| deepcopy_memo            | 30.7 us                                                               | 30.3 us: 1.01x faster                                                 |
| pprint_pformat           | 1.49 sec                                                              | 1.47 sec: 1.01x faster                                                |
| json                     | 5.37 ms                                                               | 5.32 ms: 1.01x faster                                                 |
| pprint_safe_repr         | 724 ms                                                                | 717 ms: 1.01x faster                                                  |
| pathlib                  | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                 |
| meteor_contest           | 109 ms                                                                | 108 ms: 1.01x faster                                                  |
| deltablue                | 3.23 ms                                                               | 3.21 ms: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| generators               | 27.9 ms                                                               | 27.7 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult  | 4.77 ms                                                               | 4.74 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.12 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| json_dumps               | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| docutils                 | 2.68 sec                                                              | 2.66 sec: 1.01x faster                                                |
| sqlglot_parse            | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                                 |
| go                       | 119 ms                                                                | 119 ms: 1.01x faster                                                  |
| scimark_sor              | 127 ms                                                                | 126 ms: 1.01x faster                                                  |
| hexiom                   | 6.32 ms                                                               | 6.29 ms: 1.01x faster                                                 |
| fannkuch                 | 405 ms                                                                | 403 ms: 1.00x faster                                                  |
| sqlglot_transpile        | 1.59 ms                                                               | 1.58 ms: 1.00x faster                                                 |
| regex_v8                 | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| sympy_integrate          | 19.7 ms                                                               | 19.6 ms: 1.00x faster                                                 |
| pickle_pure_python       | 302 us                                                                | 301 us: 1.00x faster                                                  |
| scimark_fft              | 361 ms                                                                | 360 ms: 1.00x faster                                                  |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x faster                                                 |
| 2to3                     | 257 ms                                                                | 257 ms: 1.00x faster                                                  |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x faster                                                  |
| crypto_pyaes             | 73.3 ms                                                               | 73.6 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                |
| bench_thread_pool        | 783 us                                                                | 787 us: 1.00x slower                                                  |
| regex_compile            | 130 ms                                                                | 131 ms: 1.00x slower                                                  |
| tornado_http             | 90.3 ms                                                               | 90.7 ms: 1.01x slower                                                 |
| async_tree_io            | 931 ms                                                                | 937 ms: 1.01x slower                                                  |
| bpe_tokeniser            | 4.82 sec                                                              | 4.86 sec: 1.01x slower                                                |
| sympy_sum                | 147 ms                                                                | 148 ms: 1.01x slower                                                  |
| xml_etree_process        | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                 |
| asyncio_tcp              | 475 ms                                                                | 479 ms: 1.01x slower                                                  |
| xml_etree_generate       | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed  | 560 ms                                                                | 567 ms: 1.01x slower                                                  |
| sqlglot_normalize        | 108 ms                                                                | 109 ms: 1.01x slower                                                  |
| async_tree_none_tg       | 309 ms                                                                | 313 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 159 us                                                                | 161 us: 1.01x slower                                                  |
| nqueens                  | 79.6 ms                                                               | 80.7 ms: 1.01x slower                                                 |
| scimark_monte_carlo      | 67.5 ms                                                               | 68.7 ms: 1.02x slower                                                 |
| async_generators         | 436 ms                                                                | 445 ms: 1.02x slower                                                  |
| genshi_text              | 22.6 ms                                                               | 23.1 ms: 1.02x slower                                                 |
| html5lib                 | 61.7 ms                                                               | 63.5 ms: 1.03x slower                                                 |
| genshi_xml               | 49.3 ms                                                               | 50.9 ms: 1.03x slower                                                 |
| mdp                      | 2.52 sec                                                              | 2.64 sec: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (29): xml_etree_parse, telco, thrift, comprehensions, chaos, tomli_loads, nbody, regex_dna, coverage, bench_mp_pool, gc_traversal, json_loads, django_template, sqlglot_optimize, raytrace, logging_simple, sympy_str, pycparser, asyncio_websockets, pylint, logging_format, sympy_expand, async_tree_none, async_tree_memoization_tg, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, scimark_lu

# HPT report

- Reliability score: 90.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x