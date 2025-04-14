# Results vs. 3.13.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.05x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.7 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 343 ms: 1.36x faster                                                         |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 356 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 283 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 515 ms: 1.13x faster                                                         |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.5 ms: 1.15x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 104 ms: 1.17x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.10 ms: 1.19x faster                                                        |
| regex_dna      | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 56.1 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 79.8 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 204 us: 1.06x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 337 us: 1.04x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| mako           | 10.4 ms                                                      | 9.66 ms: 1.07x faster                                                        |
| genshi_xml     | 57.1 ms                                                      | 56.0 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 343 ms: 1.36x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.0 us: 1.33x faster                                                        |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 356 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.88 us: 1.23x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 283 ms: 1.22x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.10 ms: 1.19x faster                                                        |
| pyflate                    | 503 ms                                                       | 425 ms: 1.18x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                        |
| richards                   | 52.9 ms                                                      | 44.9 ms: 1.18x faster                                                        |
| richards_super             | 59.6 ms                                                      | 50.8 ms: 1.17x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 83.9 ms: 1.16x faster                                                        |
| float                      | 81.3 ms                                                      | 70.5 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.76 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 515 ms: 1.13x faster                                                         |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.59 sec: 1.11x faster                                                       |
| go                         | 162 ms                                                       | 148 ms: 1.10x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 56.1 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.7 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 79.8 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.1 ms: 1.08x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 321 ms: 1.08x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.66 ms: 1.07x faster                                                        |
| scimark_fft                | 328 ms                                                       | 306 ms: 1.07x faster                                                         |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| connected_components       | 432 ms                                                       | 404 ms: 1.07x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 204 us: 1.06x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| regex_dna                  | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| shortest_path              | 460 ms                                                       | 437 ms: 1.05x faster                                                         |
| thrift                     | 901 us                                                       | 857 us: 1.05x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 803 ms: 1.05x faster                                                         |
| json                       | 5.69 ms                                                      | 5.43 ms: 1.05x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                        |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.78 us: 1.04x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.02x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 56.0 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 96.8 ns: 1.01x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.38 ms: 1.01x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 67.6 ms: 1.01x faster                                                        |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.77 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                         |
| logging_format             | 6.94 us                                                      | 6.90 us: 1.01x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.6 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 59.9 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.84 ms: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 100 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.73 ms: 1.02x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.60 sec: 1.02x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 966 us: 1.03x slower                                                         |
| chaos                      | 60.2 ms                                                      | 62.0 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                         |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.03x slower                                                         |
| deltablue                  | 3.42 ms                                                      | 3.53 ms: 1.03x slower                                                        |
| coverage                   | 80.0 ms                                                      | 82.8 ms: 1.04x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 337 us: 1.04x slower                                                         |
| fannkuch                   | 363 ms                                                       | 381 ms: 1.05x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 77.4 ms: 1.06x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 7.14 ms: 1.09x slower                                                        |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 100.0 ms: 1.10x slower                                                       |
| raytrace                   | 273 ms                                                       | 302 ms: 1.11x slower                                                         |
| comprehensions             | 17.0 us                                                      | 19.4 us: 1.14x slower                                                        |
| nbody                      | 89.3 ms                                                      | 104 ms: 1.17x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.3 ms: 1.34x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.50 ms: 1.37x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.55 sec: 303.12x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (7): sphinx, sympy_expand, sympy_str, asyncio_websockets, sympy_sum, logging_simple, django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x