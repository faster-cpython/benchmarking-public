# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 266 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 567 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 56.7 ms: 1.14x slower                                                      |
| nbody          | 68.4 ms                                                     | 88.1 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.5 ms: 1.48x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.6 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.3 ms: 1.12x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 212 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.0 ms: 1.04x slower                                                      |
| django_template | 22.4 ms                                                     | 24.7 ms: 1.11x slower                                                      |
| mako            | 6.35 ms                                                     | 7.04 ms: 1.11x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 519 us: 16.94x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.5 ms: 1.48x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 917 us: 1.37x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.56 ms: 1.26x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 70.3 ms: 1.23x faster                                                      |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.7 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 266 ms: 1.04x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| go                         | 87.0 ms                                                     | 88.6 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| 2to3                       | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 90.0 ms: 1.04x slower                                                      |
| sympy_expand               | 291 ms                                                      | 303 ms: 1.04x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.4 ms: 1.04x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 37.0 ms: 1.04x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.4 ms: 1.06x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.07x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.6 ms: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.37 us: 1.07x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.8 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                       |
| telco                      | 4.79 ms                                                     | 5.16 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| sqlglot_optimize           | 32.9 ms                                                     | 35.7 ms: 1.08x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.79 us: 1.09x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.51 sec: 1.09x slower                                                     |
| async_tree_io_tg           | 518 ms                                                      | 567 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.69 ms: 1.09x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 49.8 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 192 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.10x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.7 ms: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| mako                       | 6.35 ms                                                     | 7.04 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 41.3 ms: 1.12x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 212 us: 1.12x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.13x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| float                      | 49.9 ms                                                     | 56.7 ms: 1.14x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 563 ms: 1.14x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.2 ms: 1.15x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| pyflate                    | 283 ms                                                      | 326 ms: 1.15x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.15 sec: 1.15x slower                                                     |
| sqlglot_parse              | 771 us                                                      | 892 us: 1.16x slower                                                       |
| pycparser                  | 683 ms                                                      | 791 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.56 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 73.9 ms: 1.18x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 64.4 ns: 1.18x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.3 ms: 1.18x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.1 us: 1.18x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                      |
| raytrace                   | 160 ms                                                      | 190 ms: 1.19x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.7 ms: 1.19x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 63.1 ms: 1.19x slower                                                      |
| fannkuch                   | 253 ms                                                      | 307 ms: 1.21x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 92.7 ms: 1.22x slower                                                      |
| scimark_fft                | 172 ms                                                      | 211 ms: 1.23x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 50.9 ms: 1.25x slower                                                      |
| nbody                      | 68.4 ms                                                     | 88.1 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (7): bench_thread_pool, json, async_tree_none_tg, python_startup_no_site, xml_etree_parse, regex_dna, tornado_http
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.026x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown