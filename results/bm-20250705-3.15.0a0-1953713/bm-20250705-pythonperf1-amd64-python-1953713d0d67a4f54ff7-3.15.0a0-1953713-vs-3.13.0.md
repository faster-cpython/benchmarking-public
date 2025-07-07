# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.058x faster
- HPT reliability: 98.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| sphinx         | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 64.3 ms: 1.03x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 80.2 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.41 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.7 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| mako            | 6.56 ms                                                     | 6.85 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 493 us: 17.16x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                       |
| mdp                        | 1.43 sec                                                    | 817 ms: 1.75x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 77.7 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.54 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                      |
| nbody                      | 66.3 ms                                                     | 64.3 ms: 1.03x faster                                                      |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 80.2 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 63.9 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.6 ms: 1.01x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 77.4 ms: 1.02x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.5 ns: 1.02x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 73.2 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 493 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| scimark_fft                | 175 ms                                                      | 180 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| pyflate                    | 283 ms                                                      | 292 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.03x slower                                                     |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.04x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.41 ms: 1.04x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.85 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 847 us: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 48.2 ms: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.7 ms: 1.07x slower                                                      |
| fannkuch                   | 252 ms                                                      | 270 ms: 1.07x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.16 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.26 us: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.71 us: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.5 ms: 1.10x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.7 ms: 1.12x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.2 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                       |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 429 us: 1.19x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (9): pylint, genshi_xml, sqlite_synth, typing_runtime_protocols, sympy_expand, scimark_monte_carlo, k_core, html5lib, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 98.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown