# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                     | 227 ms: 1.02x faster                                                       |
| html5lib       | 40.1 ms                                                                    | 40.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization | 264 ms                                                                     | 255 ms: 1.04x faster                                                       |
| async_tree_none        | 213 ms                                                                     | 208 ms: 1.02x faster                                                       |
| coroutines             | 14.3 ms                                                                    | 14.0 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_io, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.2 ms                                                                    | 80.9 ms: 1.10x faster                                                      |
| float          | 57.0 ms                                                                    | 56.5 ms: 1.01x faster                                                      |
| pidigits       | 150 ms                                                                     | 151 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                                    | 14.8 ms: 1.05x faster                                                      |
| regex_dna      | 124 ms                                                                     | 120 ms: 1.04x faster                                                       |
| regex_effbot   | 1.64 ms                                                                    | 1.58 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 155 us                                                                     | 148 us: 1.04x faster                                                       |
| tomli_loads          | 1.65 sec                                                                   | 1.58 sec: 1.04x faster                                                     |
| pickle_pure_python   | 217 us                                                                     | 210 us: 1.03x faster                                                       |
| xml_etree_generate   | 59.5 ms                                                                    | 58.5 ms: 1.02x faster                                                      |
| xml_etree_process    | 41.9 ms                                                                    | 41.5 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                                    | 22.0 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 7.17 ms                                                                    | 6.92 ms: 1.04x faster                                                      |
| genshi_xml     | 36.4 ms                                                                    | 35.7 ms: 1.02x faster                                                      |
| genshi_text    | 16.9 ms                                                                    | 17.0 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pycparser                | 824 ms                                                                     | 744 ms: 1.11x faster                                                       |
| nbody                    | 89.2 ms                                                                    | 80.9 ms: 1.10x faster                                                      |
| scimark_sor              | 95.7 ms                                                                    | 87.7 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 2.89 ms                                                                    | 2.70 ms: 1.07x faster                                                      |
| deepcopy_memo            | 21.3 us                                                                    | 19.9 us: 1.07x faster                                                      |
| scimark_monte_carlo      | 52.4 ms                                                                    | 49.2 ms: 1.06x faster                                                      |
| regex_v8                 | 15.6 ms                                                                    | 14.8 ms: 1.05x faster                                                      |
| fannkuch                 | 303 ms                                                                     | 288 ms: 1.05x faster                                                       |
| hexiom                   | 4.53 ms                                                                    | 4.32 ms: 1.05x faster                                                      |
| unpickle_pure_python     | 155 us                                                                     | 148 us: 1.04x faster                                                       |
| spectral_norm            | 69.9 ms                                                                    | 67.1 ms: 1.04x faster                                                      |
| tomli_loads              | 1.65 sec                                                                   | 1.58 sec: 1.04x faster                                                     |
| async_tree_memoization   | 264 ms                                                                     | 255 ms: 1.04x faster                                                       |
| go                       | 87.6 ms                                                                    | 84.5 ms: 1.04x faster                                                      |
| regex_dna                | 124 ms                                                                     | 120 ms: 1.04x faster                                                       |
| pprint_safe_repr         | 562 ms                                                                     | 543 ms: 1.04x faster                                                       |
| mako                     | 7.17 ms                                                                    | 6.92 ms: 1.04x faster                                                      |
| crypto_pyaes             | 49.6 ms                                                                    | 47.9 ms: 1.03x faster                                                      |
| regex_effbot             | 1.64 ms                                                                    | 1.58 ms: 1.03x faster                                                      |
| scimark_lu               | 64.6 ms                                                                    | 62.6 ms: 1.03x faster                                                      |
| sqlglot_parse            | 913 us                                                                     | 884 us: 1.03x faster                                                       |
| scimark_fft              | 214 ms                                                                     | 207 ms: 1.03x faster                                                       |
| deltablue                | 2.30 ms                                                                    | 2.23 ms: 1.03x faster                                                      |
| pprint_pformat           | 1.15 sec                                                                   | 1.12 sec: 1.03x faster                                                     |
| pickle_pure_python       | 217 us                                                                     | 210 us: 1.03x faster                                                       |
| chaos                    | 44.2 ms                                                                    | 42.8 ms: 1.03x faster                                                      |
| richards                 | 32.6 ms                                                                    | 31.6 ms: 1.03x faster                                                      |
| sqlglot_optimize         | 37.0 ms                                                                    | 35.9 ms: 1.03x faster                                                      |
| logging_silent           | 64.4 ns                                                                    | 62.7 ns: 1.03x faster                                                      |
| nqueens                  | 65.8 ms                                                                    | 64.0 ms: 1.03x faster                                                      |
| sqlglot_transpile        | 1.14 ms                                                                    | 1.11 ms: 1.03x faster                                                      |
| comprehensions           | 12.2 us                                                                    | 11.9 us: 1.03x faster                                                      |
| async_tree_none          | 213 ms                                                                     | 208 ms: 1.02x faster                                                       |
| sqlglot_normalize        | 195 ms                                                                     | 190 ms: 1.02x faster                                                       |
| telco                    | 5.14 ms                                                                    | 5.03 ms: 1.02x faster                                                      |
| sympy_expand             | 311 ms                                                                     | 305 ms: 1.02x faster                                                       |
| richards_super           | 36.9 ms                                                                    | 36.1 ms: 1.02x faster                                                      |
| coroutines               | 14.3 ms                                                                    | 14.0 ms: 1.02x faster                                                      |
| pyflate                  | 329 ms                                                                     | 323 ms: 1.02x faster                                                       |
| genshi_xml               | 36.4 ms                                                                    | 35.7 ms: 1.02x faster                                                      |
| xml_etree_generate       | 59.5 ms                                                                    | 58.5 ms: 1.02x faster                                                      |
| meteor_contest           | 78.3 ms                                                                    | 77.0 ms: 1.02x faster                                                      |
| deepcopy                 | 192 us                                                                     | 189 us: 1.02x faster                                                       |
| 2to3                     | 230 ms                                                                     | 227 ms: 1.02x faster                                                       |
| dulwich_log              | 43.5 ms                                                                    | 42.8 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 1.95 us                                                                    | 1.92 us: 1.01x faster                                                      |
| coverage                 | 49.4 ms                                                                    | 48.7 ms: 1.01x faster                                                      |
| sympy_sum                | 91.1 ms                                                                    | 89.9 ms: 1.01x faster                                                      |
| xml_etree_process        | 41.9 ms                                                                    | 41.5 ms: 1.01x faster                                                      |
| bench_mp_pool            | 69.2 ms                                                                    | 68.5 ms: 1.01x faster                                                      |
| sympy_str                | 178 ms                                                                     | 177 ms: 1.01x faster                                                       |
| float                    | 57.0 ms                                                                    | 56.5 ms: 1.01x faster                                                      |
| python_startup           | 22.2 ms                                                                    | 22.0 ms: 1.01x faster                                                      |
| sympy_integrate          | 13.3 ms                                                                    | 13.2 ms: 1.01x faster                                                      |
| pathlib                  | 79.2 ms                                                                    | 78.8 ms: 1.01x faster                                                      |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.00x slower                                                       |
| generators               | 20.7 ms                                                                    | 20.8 ms: 1.01x slower                                                      |
| logging_format           | 6.77 us                                                                    | 6.82 us: 1.01x slower                                                      |
| genshi_text              | 16.9 ms                                                                    | 17.0 ms: 1.01x slower                                                      |
| logging_simple           | 6.34 us                                                                    | 6.38 us: 1.01x slower                                                      |
| html5lib                 | 40.1 ms                                                                    | 40.5 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 110 us                                                                     | 111 us: 1.01x slower                                                       |
| raytrace                 | 189 ms                                                                     | 191 ms: 1.01x slower                                                       |
| mdp                      | 1.50 sec                                                                   | 1.56 sec: 1.04x slower                                                     |
| Geometric mean           | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (24): async_tree_none_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_io, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, create_gc_cycles, gc_traversal, bench_thread_pool, django_template, tornado_http, thrift, json_dumps, async_generators, pylint, regex_compile, docutils, json_loads, xml_etree_parse, async_tree_cpu_io_mixed, python_startup_no_site, xml_etree_iterparse, json

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown