# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.071x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.89 sec: 1.89x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 671 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 136 ms: 2.20x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 370 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 222 ms: 1.27x faster                                                       |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                       |
| async_tree_none            | 219 ms                                                      | 214 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 374 ms: 1.02x faster                                                       |
| async_generators           | 223 ms                                                      | 257 ms: 1.16x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 83.9 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.62 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.7 ms                                                     | 93.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.65 ms: 1.07x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 154 us: 1.18x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 63.5 ms: 1.19x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 232 us: 1.25x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.66 sec: 1.94x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 41.7 ms: 1.23x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 20.0 ms: 1.31x slower                                                      |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| mako            | 6.56 ms                                                     | 9.81 ms: 1.50x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.35x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 576 us: 14.69x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 136 ms: 2.20x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.22 ms: 1.61x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 370 ms: 1.34x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.13 sec: 1.27x faster                                                     |
| async_tree_memoization_tg  | 281 ms                                                      | 222 ms: 1.27x faster                                                       |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.05 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                       |
| deepcopy                   | 223 us                                                      | 201 us: 1.11x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 79.5 ms: 1.06x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.62 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                      |
| async_tree_none            | 219 ms                                                      | 214 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 374 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 729 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                      |
| pylint                     | 205 ms                                                      | 216 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.16 us: 1.07x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.65 ms: 1.07x slower                                                      |
| sphinx                     | 617 ms                                                      | 671 ms: 1.09x slower                                                       |
| go                         | 84.7 ms                                                     | 92.4 ms: 1.09x slower                                                      |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 86.2 ms: 1.13x slower                                                      |
| sympy_expand               | 286 ms                                                      | 323 ms: 1.13x slower                                                       |
| sympy_str                  | 167 ms                                                      | 190 ms: 1.14x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.3 ns: 1.14x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.54 ms: 1.14x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 97.4 ms: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.1 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.16x slower                                                      |
| async_generators           | 223 ms                                                      | 257 ms: 1.16x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 93.3 ms: 1.16x slower                                                      |
| fannkuch                   | 252 ms                                                      | 291 ms: 1.16x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 65.7 ms: 1.16x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 73.8 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 564 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 154 us: 1.18x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.56 ms: 1.19x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.5 ms: 1.19x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.35 us: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.10 ms: 1.19x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.8 ms: 1.19x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.89 us: 1.19x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.7 ms: 1.19x slower                                                      |
| scimark_fft                | 175 ms                                                      | 211 ms: 1.21x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.3 ms: 1.22x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 55.8 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.9 ms: 1.23x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 41.7 ms: 1.23x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 128 us: 1.24x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 232 us: 1.25x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.2 ms: 1.27x slower                                                      |
| nbody                      | 66.3 ms                                                     | 83.9 ms: 1.27x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.42 ms: 1.28x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 71.9 ms: 1.28x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 20.0 ms: 1.31x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.08 ms: 1.33x slower                                                      |
| many_optionals             | 361 us                                                      | 481 us: 1.33x slower                                                       |
| richards_super             | 29.8 ms                                                     | 40.0 ms: 1.34x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| raytrace                   | 153 ms                                                      | 210 ms: 1.37x slower                                                       |
| coverage                   | 45.3 ms                                                     | 67.1 ms: 1.48x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.81 ms: 1.50x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.70 sec: 1.59x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 18.8 ms: 1.73x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.71 sec: 1.75x slower                                                     |
| shortest_path              | 355 ms                                                      | 642 ms: 1.81x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.89 sec: 1.89x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.48 sec: 1.91x slower                                                     |
| connected_components       | 320 ms                                                      | 620 ms: 1.94x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.66 sec: 1.94x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.071x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown