# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.054x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.74 sec: 1.79x slower                                                     |
| html5lib       | 38.2 ms                                                     | 41.5 ms: 1.09x slower                                                      |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 141 ms: 2.13x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 323 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 189 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 346 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 305 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 134 ms: 1.09x faster                                                       |
| nbody          | 66.3 ms                                                     | 80.1 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 94.1 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 57.2 ms: 1.06x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 5.94 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.9 us: 1.05x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 62.3 ms: 1.17x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.20x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.7 ms: 1.22x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 232 us: 1.25x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.60 sec: 1.90x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.0 ms: 1.18x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.6 ms: 1.29x slower                                                      |
| django_template | 20.3 ms                                                     | 27.2 ms: 1.34x slower                                                      |
| mako            | 6.56 ms                                                     | 10.1 ms: 1.53x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.33x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 556 us: 15.23x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.7 ms: 2.54x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 141 ms: 2.13x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.19 ms: 1.65x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 323 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 189 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 346 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.08 sec: 1.32x faster                                                     |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 305 ms: 1.25x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 995 us: 1.23x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.34 us: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| float                      | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                      |
| pidigits                   | 146 ms                                                      | 134 ms: 1.09x faster                                                       |
| deepcopy                   | 223 us                                                      | 205 us: 1.09x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 77.6 ms: 1.09x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 21.4 us: 1.08x faster                                                      |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.2 ms: 1.06x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.94 ms: 1.04x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.76 ms: 1.02x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 720 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                      |
| json_loads                 | 15.1 us                                                     | 15.9 us: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.16 us: 1.07x slower                                                      |
| go                         | 84.7 ms                                                     | 91.3 ms: 1.08x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 41.5 ms: 1.09x slower                                                      |
| pyflate                    | 283 ms                                                      | 311 ms: 1.10x slower                                                       |
| sympy_expand               | 286 ms                                                      | 315 ms: 1.10x slower                                                       |
| sympy_str                  | 167 ms                                                      | 185 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 95.2 ms: 1.12x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 61.2 ns: 1.12x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 71.1 ms: 1.12x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 86.6 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 65.0 ms: 1.15x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.09 us: 1.15x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.67 us: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 62.3 ms: 1.17x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 94.1 ms: 1.17x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 40.0 ms: 1.18x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 573 ms: 1.18x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 85.5 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.09 ms: 1.19x slower                                                      |
| fannkuch                   | 252 ms                                                      | 302 ms: 1.20x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.20x slower                                                       |
| nbody                      | 66.3 ms                                                     | 80.1 ms: 1.21x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.67 ms: 1.22x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 55.7 ms: 1.22x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.2 ms: 1.22x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.7 ms: 1.22x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.5 ms: 1.23x slower                                                      |
| scimark_fft                | 175 ms                                                      | 216 ms: 1.24x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.8 ms: 1.25x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 232 us: 1.25x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 131 us: 1.27x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 71.6 ms: 1.28x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 19.6 ms: 1.29x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.44 ms: 1.29x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.07 ms: 1.33x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.2 ms: 1.34x slower                                                      |
| richards                   | 26.3 ms                                                     | 35.4 ms: 1.35x slower                                                      |
| raytrace                   | 153 ms                                                      | 208 ms: 1.36x slower                                                       |
| richards_super             | 29.8 ms                                                     | 41.1 ms: 1.38x slower                                                      |
| coverage                   | 45.3 ms                                                     | 67.3 ms: 1.48x slower                                                      |
| mako                       | 6.56 ms                                                     | 10.1 ms: 1.53x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.61 sec: 1.53x slower                                                     |
| many_optionals             | 361 us                                                      | 610 us: 1.69x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.69 sec: 1.73x slower                                                     |
| shortest_path              | 355 ms                                                      | 625 ms: 1.76x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.74 sec: 1.79x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.33 sec: 1.85x slower                                                     |
| connected_components       | 320 ms                                                      | 597 ms: 1.87x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.60 sec: 1.90x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 34.3 ms: 3.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): pylint, regex_dna
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown