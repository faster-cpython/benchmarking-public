# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.221x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 289 ms: 1.34x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.12 sec: 1.38x slower                                                     |
| html5lib       | 38.2 ms                                                     | 52.9 ms: 1.39x slower                                                      |
| sphinx         | 617 ms                                                      | 860 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.38x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 288 ms: 1.03x slower                                                       |
| async_tree_io              | 513 ms                                                      | 536 ms: 1.04x slower                                                       |
| async_tree_none            | 219 ms                                                      | 236 ms: 1.08x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 289 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 554 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 428 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 432 ms: 1.14x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 229 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 355 ms: 1.59x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 26.8 ms: 2.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.7 ms: 1.23x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| float          | 50.8 ms                                                     | 78.5 ms: 1.54x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.6 ms: 1.43x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 122 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 106 ms: 1.15x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 72.7 ms: 1.36x slower                                                      |
| json_loads           | 15.1 us                                                     | 20.8 us: 1.38x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.67 ms: 1.40x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 87.2 ms: 1.44x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 53.2 ms: 1.46x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 328 us: 1.77x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.36x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.13 ms: 1.09x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 51.5 ms: 1.52x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 25.5 ms: 1.68x slower                                                      |
| django_template | 20.3 ms                                                     | 38.7 ms: 1.91x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.52x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 714 us: 11.86x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 34.4 ms: 2.19x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.6 ms: 1.43x faster                                                      |
| nbody                      | 66.3 ms                                                     | 53.7 ms: 1.23x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.21 sec: 1.19x faster                                                     |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 288 ms: 1.03x slower                                                       |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.70 ms: 1.04x slower                                                      |
| async_tree_io              | 513 ms                                                      | 536 ms: 1.04x slower                                                       |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                       |
| async_tree_none            | 219 ms                                                      | 236 ms: 1.08x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.09 sec: 1.08x slower                                                     |
| telco                      | 4.85 ms                                                     | 5.27 ms: 1.09x slower                                                      |
| mako                       | 6.56 ms                                                     | 7.13 ms: 1.09x slower                                                      |
| async_tree_memoization     | 265 ms                                                      | 289 ms: 1.09x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.74 us: 1.09x slower                                                      |
| async_tree_io_tg           | 497 ms                                                      | 554 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 428 ms: 1.12x slower                                                       |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 432 ms: 1.14x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 229 ms: 1.14x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 106 ms: 1.15x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 83.0 ms: 1.15x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.47 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                       |
| deepcopy                   | 223 us                                                      | 273 us: 1.22x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 995 us: 1.23x slower                                                       |
| json                       | 3.30 ms                                                     | 4.07 ms: 1.23x slower                                                      |
| pylint                     | 205 ms                                                      | 254 ms: 1.23x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 105 ms: 1.25x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 52.1 ms: 1.30x slower                                                      |
| 2to3                       | 215 ms                                                      | 289 ms: 1.34x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 72.7 ms: 1.36x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 116 ms: 1.37x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 62.7 ms: 1.38x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 667 ms: 1.38x slower                                                       |
| json_loads                 | 15.1 us                                                     | 20.8 us: 1.38x slower                                                      |
| pyflate                    | 283 ms                                                      | 390 ms: 1.38x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 17.0 ms: 1.38x slower                                                      |
| docutils                   | 1.53 sec                                                    | 2.12 sec: 1.38x slower                                                     |
| html5lib                   | 38.2 ms                                                     | 52.9 ms: 1.39x slower                                                      |
| pycparser                  | 695 ms                                                      | 964 ms: 1.39x slower                                                       |
| coverage                   | 45.3 ms                                                     | 62.9 ms: 1.39x slower                                                      |
| sphinx                     | 617 ms                                                      | 860 ms: 1.39x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 8.67 ms: 1.40x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.37 sec: 1.40x slower                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 2.84 us: 1.40x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 145 us: 1.40x slower                                                       |
| sympy_str                  | 167 ms                                                      | 238 ms: 1.42x slower                                                       |
| sympy_expand               | 286 ms                                                      | 409 ms: 1.43x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 87.2 ms: 1.44x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 53.2 ms: 1.46x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 122 ms: 1.51x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 51.5 ms: 1.52x slower                                                      |
| comprehensions             | 10.4 us                                                     | 15.9 us: 1.53x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 3.02 ms: 1.54x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 35.6 us: 1.54x slower                                                      |
| float                      | 50.8 ms                                                     | 78.5 ms: 1.54x slower                                                      |
| many_optionals             | 361 us                                                      | 572 us: 1.58x slower                                                       |
| async_generators           | 223 ms                                                      | 355 ms: 1.59x slower                                                       |
| go                         | 84.7 ms                                                     | 137 ms: 1.62x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 91.2 ms: 1.62x slower                                                      |
| logging_format             | 6.18 us                                                     | 10.1 us: 1.64x slower                                                      |
| logging_simple             | 5.77 us                                                     | 9.56 us: 1.66x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 25.5 ms: 1.68x slower                                                      |
| chaos                      | 37.9 ms                                                     | 65.7 ms: 1.73x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 328 us: 1.77x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 137 ms: 1.79x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 115 ms: 1.81x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 74.6 ms: 1.83x slower                                                      |
| django_template            | 20.3 ms                                                     | 38.7 ms: 1.91x slower                                                      |
| raytrace                   | 153 ms                                                      | 307 ms: 2.00x slower                                                       |
| generators                 | 19.0 ms                                                     | 38.3 ms: 2.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 60.9 ms: 2.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 54.1 ms: 2.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 8.03 ms: 2.09x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 23.0 ms: 2.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 26.8 ms: 2.14x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 126 ms: 2.23x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.52 ms: 2.39x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 509 ns: 9.32x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.31x slower                                                               |

Benchmark hidden because not significant (1): k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.221x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: unknown