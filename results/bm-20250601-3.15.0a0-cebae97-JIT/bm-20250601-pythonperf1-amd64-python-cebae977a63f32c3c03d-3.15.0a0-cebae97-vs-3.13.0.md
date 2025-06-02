# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.001x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 286 ms: 1.33x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.06 sec: 1.35x slower                                                     |
| html5lib       | 38.2 ms                                                     | 51.3 ms: 1.34x slower                                                      |
| sphinx         | 617 ms                                                      | 841 ms: 1.36x slower                                                       |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| async_tree_io              | 513 ms                                                      | 536 ms: 1.04x slower                                                       |
| async_tree_none            | 219 ms                                                      | 230 ms: 1.05x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 282 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 538 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 424 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 426 ms: 1.12x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 228 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 353 ms: 1.58x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 25.1 ms: 2.01x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| float          | 50.8 ms                                                     | 78.8 ms: 1.55x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.4 ms: 1.46x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.78 ms: 1.05x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 112 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 103 ms: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 156 us: 1.20x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 70.0 ms: 1.31x slower                                                      |
| json_loads           | 15.1 us                                                     | 20.4 us: 1.35x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 50.8 ms: 1.39x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 85.0 ms: 1.40x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.78 ms: 1.42x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 319 us: 1.71x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.2 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.09 ms: 1.08x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 49.3 ms: 1.46x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 24.2 ms: 1.59x slower                                                      |
| django_template | 20.3 ms                                                     | 37.3 ms: 1.84x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.47x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat             | 977 ms                                                      | 1.56 us: 625512.75x faster                                                 |
| pprint_safe_repr           | 485 ms                                                      | 904 ns: 536283.65x faster                                                  |
| pathlib                    | 75.3 ms                                                     | 33.9 ms: 2.22x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.4 ms: 1.46x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.20 sec: 1.20x faster                                                     |
| nbody                      | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.67 sec: 1.02x faster                                                     |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| async_tree_io              | 513 ms                                                      | 536 ms: 1.04x slower                                                       |
| async_tree_none            | 219 ms                                                      | 230 ms: 1.05x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.78 ms: 1.05x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.05x slower                                                     |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.14 ms: 1.06x slower                                                      |
| async_tree_memoization     | 265 ms                                                      | 282 ms: 1.06x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.09 ms: 1.08x slower                                                      |
| async_tree_io_tg           | 497 ms                                                      | 538 ms: 1.08x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.72 us: 1.09x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 424 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.2 ms: 1.11x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 103 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 426 ms: 1.12x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| fannkuch                   | 252 ms                                                      | 286 ms: 1.14x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 228 ms: 1.14x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 82.1 ms: 1.14x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.43 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 156 us: 1.20x slower                                                       |
| pylint                     | 205 ms                                                      | 247 ms: 1.20x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 977 us: 1.21x slower                                                       |
| deepcopy                   | 223 us                                                      | 270 us: 1.21x slower                                                       |
| json                       | 3.30 ms                                                     | 4.06 ms: 1.23x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 104 ms: 1.23x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 52.0 ms: 1.30x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 70.0 ms: 1.31x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 113 ms: 1.33x slower                                                       |
| 2to3                       | 215 ms                                                      | 286 ms: 1.33x slower                                                       |
| pycparser                  | 695 ms                                                      | 932 ms: 1.34x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 51.3 ms: 1.34x slower                                                      |
| docutils                   | 1.53 sec                                                    | 2.06 sec: 1.35x slower                                                     |
| json_loads                 | 15.1 us                                                     | 20.4 us: 1.35x slower                                                      |
| pyflate                    | 283 ms                                                      | 383 ms: 1.35x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 16.7 ms: 1.35x slower                                                      |
| sphinx                     | 617 ms                                                      | 841 ms: 1.36x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 62.2 ms: 1.36x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.80 us: 1.38x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 112 ms: 1.39x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 50.8 ms: 1.39x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 144 us: 1.40x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.75 ms: 1.40x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 85.0 ms: 1.40x slower                                                      |
| sympy_str                  | 167 ms                                                      | 236 ms: 1.42x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 8.78 ms: 1.42x slower                                                      |
| sympy_expand               | 286 ms                                                      | 416 ms: 1.46x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 49.3 ms: 1.46x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 34.2 us: 1.48x slower                                                      |
| comprehensions             | 10.4 us                                                     | 15.5 us: 1.49x slower                                                      |
| float                      | 50.8 ms                                                     | 78.8 ms: 1.55x slower                                                      |
| many_optionals             | 361 us                                                      | 563 us: 1.56x slower                                                       |
| go                         | 84.7 ms                                                     | 133 ms: 1.57x slower                                                       |
| async_generators           | 223 ms                                                      | 353 ms: 1.58x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 24.2 ms: 1.59x slower                                                      |
| logging_format             | 6.18 us                                                     | 9.85 us: 1.59x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 90.5 ms: 1.61x slower                                                      |
| logging_simple             | 5.77 us                                                     | 9.39 us: 1.63x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 319 us: 1.71x slower                                                       |
| chaos                      | 37.9 ms                                                     | 65.0 ms: 1.72x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 131 ms: 1.72x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 73.8 ms: 1.81x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 116 ms: 1.82x slower                                                       |
| django_template            | 20.3 ms                                                     | 37.3 ms: 1.84x slower                                                      |
| generators                 | 19.0 ms                                                     | 36.5 ms: 1.92x slower                                                      |
| raytrace                   | 153 ms                                                      | 299 ms: 1.95x slower                                                       |
| richards                   | 26.3 ms                                                     | 51.2 ms: 1.95x slower                                                      |
| richards_super             | 29.8 ms                                                     | 58.1 ms: 1.95x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 7.72 ms: 2.01x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 25.1 ms: 2.01x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 22.6 ms: 2.08x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 120 ms: 2.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.29 ms: 2.27x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 497 ns: 9.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 479 ms: 10.58x slower                                                      |
| thrift                     | 8.47 ms                                                     | 98.9 ms: 11.69x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (4): connected_components, async_tree_memoization_tg, pidigits, scimark_sparse_mat_mult
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown