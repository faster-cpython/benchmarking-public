# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.43x faster                                                        |
| async_tree_none            | 376 ms                                                       | 267 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_io              | 843 ms                                                       | 612 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 619 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 424 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.2 ms: 1.14x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.50 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.2 ms: 1.07x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.3 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.05x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.68 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| django_template | 36.4 ms                                                      | 36.1 ms: 1.01x faster                                                       |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 2.00x faster                                                      |
| deepcopy                   | 392 us                                                       | 268 us: 1.47x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.43x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.2 us: 1.42x faster                                                       |
| async_tree_none            | 376 ms                                                       | 267 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                        |
| go                         | 162 ms                                                       | 116 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 612 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 619 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                      |
| pyflate                    | 503 ms                                                       | 412 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.19x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.1 ms: 1.17x faster                                                       |
| richards_super             | 59.6 ms                                                      | 50.9 ms: 1.17x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.3 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.4 ms: 1.14x faster                                                       |
| float                      | 81.3 ms                                                      | 71.2 ms: 1.14x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.52 sec: 1.13x faster                                                      |
| spectral_norm              | 97.0 ms                                                      | 86.3 ms: 1.12x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.86 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 754 ms: 1.12x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.65 sec: 1.09x faster                                                      |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                        |
| thrift                     | 901 us                                                       | 826 us: 1.09x faster                                                        |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.2 ms: 1.08x faster                                                       |
| async_generators           | 457 ms                                                       | 424 ms: 1.08x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.17 ms: 1.08x faster                                                       |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 21.9 ms: 1.07x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.2 ms: 1.07x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.4 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.02 us: 1.06x faster                                                       |
| sympy_expand               | 509 ms                                                       | 481 ms: 1.06x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.1 us: 1.06x faster                                                       |
| json                       | 5.69 ms                                                      | 5.39 ms: 1.06x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| sympy_str                  | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.62 us: 1.05x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.50 ms: 1.05x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.05x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 93.9 ns: 1.04x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                      |
| python_startup_no_site     | 8.96 ms                                                      | 8.68 ms: 1.03x faster                                                       |
| chaos                      | 60.2 ms                                                      | 58.4 ms: 1.03x faster                                                       |
| coverage                   | 80.0 ms                                                      | 77.7 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                        |
| connected_components       | 432 ms                                                       | 424 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 166 us: 1.02x faster                                                        |
| shortest_path              | 460 ms                                                       | 453 ms: 1.02x faster                                                        |
| fannkuch                   | 363 ms                                                       | 360 ms: 1.01x faster                                                        |
| django_template            | 36.4 ms                                                      | 36.1 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.75 ms: 1.00x faster                                                       |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.01x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 91.8 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| raytrace                   | 273 ms                                                       | 278 ms: 1.02x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 961 us: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 76.2 ms: 1.04x slower                                                       |
| nbody                      | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.3 us: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                       |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.11x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.25 ms: 1.32x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 24.6 ms: 1.41x slower                                                       |
| telco                      | 8.79 ms                                                      | 160 ms: 18.16x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 2.38 sec: 465.11x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): json_dumps, djangocms
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x