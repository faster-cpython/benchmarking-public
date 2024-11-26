# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 227 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.09x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 255 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 558 ms: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 572 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                      |
| nbody          | 68.4 ms                                                     | 80.9 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 94.7 ms: 1.01x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.1 ms: 1.07x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 58.5 ms: 1.08x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 210 us: 1.11x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 41.5 ms: 1.12x slower                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.0 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.92 ms: 1.09x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 522 us: 16.85x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 908 us: 1.39x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 68.5 ms: 1.26x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.56 ms: 1.26x faster                                                      |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 19.9 us: 1.17x faster                                                      |
| python_startup             | 25.4 ms                                                     | 22.0 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.09x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 255 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 816 us: 1.04x faster                                                       |
| go                         | 87.0 ms                                                     | 84.5 ms: 1.03x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 78.8 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 94.7 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| 2to3                       | 221 ms                                                      | 227 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.9 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                      |
| sympy_expand               | 291 ms                                                      | 305 ms: 1.05x slower                                                       |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 77.0 ms: 1.05x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.8 ms: 1.05x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.03 ms: 1.05x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 47.9 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 67.1 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.1 ms: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.38 us: 1.07x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 558 ms: 1.08x slower                                                       |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 58.5 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| pycparser                  | 683 ms                                                      | 744 ms: 1.09x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.82 us: 1.09x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.92 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.70 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 572 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 543 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 210 us: 1.11x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.32 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| chaos                      | 38.5 ms                                                     | 42.8 ms: 1.11x slower                                                      |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.12x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                     |
| xml_etree_process          | 37.0 ms                                                     | 41.5 ms: 1.12x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.56 sec: 1.13x slower                                                     |
| nqueens                    | 56.7 ms                                                     | 64.0 ms: 1.13x slower                                                      |
| float                      | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                     |
| regex_compile              | 80.5 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| fannkuch                   | 253 ms                                                      | 288 ms: 1.14x slower                                                       |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 884 us: 1.15x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.7 ns: 1.15x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 87.7 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                      |
| richards                   | 27.3 ms                                                     | 31.6 ms: 1.16x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.23 ms: 1.16x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.1 ms: 1.17x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 62.6 ms: 1.18x slower                                                      |
| nbody                      | 68.4 ms                                                     | 80.9 ms: 1.18x slower                                                      |
| raytrace                   | 160 ms                                                      | 191 ms: 1.19x slower                                                       |
| scimark_fft                | 172 ms                                                      | 207 ms: 1.20x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.2 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): json, python_startup_no_site, regex_effbot, tornado_http, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown