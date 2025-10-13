# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.061x faster
- HPT reliability: 70.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.2 ms: 1.12x faster                                                      |
| nbody          | 66.3 ms                                                     | 67.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 135 us: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.2 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.91x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.1 ms: 2.58x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| mdp                        | 1.43 sec                                                    | 790 ms: 1.81x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| deepcopy                   | 223 us                                                      | 164 us: 1.37x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.34x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.4 us: 1.32x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.20 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                      |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                      |
| float                      | 50.8 ms                                                     | 45.2 ms: 1.12x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                      |
| go                         | 84.7 ms                                                     | 76.8 ms: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| pylint                     | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.5 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| sympy_expand               | 286 ms                                                      | 281 ms: 1.02x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| scimark_fft                | 175 ms                                                      | 174 ms: 1.01x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.3 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.1 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 490 ms: 1.01x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 77.1 ms: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| mako                       | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| nbody                      | 66.3 ms                                                     | 67.4 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 56.1 ns: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.96 us: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.03x slower                                                     |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                     |
| bench_thread_pool          | 810 us                                                      | 839 us: 1.04x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.7 ms: 1.04x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.42 us: 1.04x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 135 us: 1.04x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 66.6 ms: 1.05x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.05x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.3 ms: 1.05x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 48.3 ms: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.2 ms: 1.08x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.14 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.09x slower                                                      |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 63.4 ms: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 565 us: 1.56x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.4 ms: 2.90x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (10): pycparser, regex_compile, sympy_str, shortest_path, pyflate, sympy_sum, pidigits, sphinx, 2to3, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 70.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown