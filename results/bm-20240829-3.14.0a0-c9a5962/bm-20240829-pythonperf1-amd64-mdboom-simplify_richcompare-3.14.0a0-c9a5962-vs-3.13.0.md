# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 230 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| html5lib       | 38.9 ms                                                     | 39.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 211 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 569 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.12x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.6 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.03x slower                                                       |
| float          | 49.9 ms                                                     | 58.6 ms: 1.17x slower                                                      |
| nbody          | 68.4 ms                                                     | 87.8 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.9 ms: 1.35x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 92.4 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.32 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 214 us: 1.13x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 42.3 ms: 1.14x slower                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.4 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 17.2 ms: 1.10x slower                                                      |
| mako            | 6.35 ms                                                     | 7.12 ms: 1.12x slower                                                      |
| django_template | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 521 us: 16.89x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 919 us: 1.37x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.9 ms: 1.35x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.57 ms: 1.26x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 69.0 ms: 1.25x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.4 ms: 1.13x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 21.2 us: 1.10x faster                                                      |
| async_tree_none            | 226 ms                                                      | 211 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                                      |
| json                       | 3.19 ms                                                     | 3.03 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.05x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 79.6 ms: 1.02x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| go                         | 87.0 ms                                                     | 88.1 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 39.7 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                                       |
| pidigits                   | 148 ms                                                      | 151 ms: 1.03x slower                                                       |
| 2to3                       | 221 ms                                                      | 230 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| sympy_expand               | 291 ms                                                      | 305 ms: 1.05x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.9 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.06x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.07x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.32 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                                      |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 79.5 ms: 1.08x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| crypto_pyaes               | 45.4 ms                                                     | 49.3 ms: 1.08x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.20 ms: 1.09x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| logging_simple             | 5.96 us                                                     | 6.48 us: 1.09x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.85 us: 1.09x slower                                                      |
| coverage                   | 45.6 ms                                                     | 49.9 ms: 1.10x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 569 ms: 1.10x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.2 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 194 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.6 ms: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| mako                       | 6.35 ms                                                     | 7.12 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 251 ms: 1.12x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 214 us: 1.13x slower                                                       |
| django_template            | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 64.7 ms: 1.14x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 42.3 ms: 1.14x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.6 ms: 1.15x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 92.4 ms: 1.15x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 72.2 ms: 1.15x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.15 sec: 1.15x slower                                                     |
| pprint_safe_repr           | 494 ms                                                      | 569 ms: 1.15x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.4 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 327 ms: 1.16x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.52 ms: 1.16x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| float                      | 49.9 ms                                                     | 58.6 ms: 1.17x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 910 us: 1.18x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.1 us: 1.18x slower                                                      |
| fannkuch                   | 253 ms                                                      | 300 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.19x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 64.8 ns: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.92 ms: 1.19x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.5 ms: 1.19x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                      |
| richards_super             | 30.9 ms                                                     | 37.2 ms: 1.20x slower                                                      |
| pycparser                  | 683 ms                                                      | 839 ms: 1.23x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 93.8 ms: 1.23x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 65.3 ms: 1.23x slower                                                      |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                                       |
| scimark_fft                | 172 ms                                                      | 214 ms: 1.24x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 51.6 ms: 1.26x slower                                                      |
| nbody                      | 68.4 ms                                                     | 87.8 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (5): bench_thread_pool, async_tree_none_tg, python_startup_no_site, tornado_http, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown