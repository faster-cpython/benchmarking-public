# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.015x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 579 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 82.8 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.7 ms: 1.37x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                      |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 90.9 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.25 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.1 ms: 1.07x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 40.5 ms: 1.09x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 210 us: 1.11x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| mako            | 6.35 ms                                                     | 6.90 ms: 1.09x slower                                                      |
| django_template | 22.4 ms                                                     | 24.3 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 514 us: 17.13x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 917 us: 1.37x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.7 ms: 1.37x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.56 ms: 1.26x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 70.6 ms: 1.22x faster                                                      |
| deepcopy                   | 226 us                                                      | 186 us: 1.22x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.0 us: 1.16x faster                                                      |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.03x faster                                                       |
| go                         | 87.0 ms                                                     | 85.1 ms: 1.02x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 89.6 ms: 1.03x slower                                                      |
| 2to3                       | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.5 ms: 1.04x slower                                                      |
| sympy_expand               | 291 ms                                                      | 303 ms: 1.04x slower                                                       |
| sympy_str                  | 169 ms                                                      | 176 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 66.0 ms: 1.05x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.25 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 78.5 ms: 1.07x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 48.5 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.1 ms: 1.07x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.63 ms: 1.07x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.45 us: 1.08x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| mako                       | 6.35 ms                                                     | 6.90 ms: 1.09x slower                                                      |
| django_template            | 22.4 ms                                                     | 24.3 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 40.5 ms: 1.09x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.91 us: 1.10x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.30 ms: 1.11x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 210 us: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 579 ms: 1.11x slower                                                       |
| chaos                      | 38.5 ms                                                     | 42.8 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 551 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| float                      | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.37 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 63.8 ms: 1.13x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| regex_compile              | 80.5 ms                                                     | 90.9 ms: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| fannkuch                   | 253 ms                                                      | 288 ms: 1.14x slower                                                       |
| scimark_fft                | 172 ms                                                      | 197 ms: 1.15x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 886 us: 1.15x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 61.2 ms: 1.16x slower                                                      |
| raytrace                   | 160 ms                                                      | 185 ms: 1.16x slower                                                       |
| richards                   | 27.3 ms                                                     | 31.8 ms: 1.16x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 63.7 ns: 1.17x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.0 ms: 1.17x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 89.4 ms: 1.17x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.26 ms: 1.18x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| nbody                      | 68.4 ms                                                     | 82.8 ms: 1.21x slower                                                      |
| pycparser                  | 683 ms                                                      | 833 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): json, bench_thread_pool, tornado_http, python_startup_no_site, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown