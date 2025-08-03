# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.080x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.97 sec: 1.94x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 731 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 141 ms: 2.13x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 335 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 155 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.4 ms: 1.09x faster                                                      |
| pidigits       | 146 ms                                                      | 142 ms: 1.03x faster                                                       |
| nbody          | 66.3 ms                                                     | 82.2 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| regex_dna      | 115 ms                                                      | 112 ms: 1.02x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 94.4 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.5 ms: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.8 us: 1.05x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.72 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 63.1 ms: 1.18x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.2 ms: 1.21x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 242 us: 1.30x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.77 sec: 2.02x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.3 ms: 1.19x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.7 ms: 1.29x slower                                                      |
| django_template | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                      |
| mako            | 6.56 ms                                                     | 9.71 ms: 1.48x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.32x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 577 us: 14.66x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.30x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 141 ms: 2.13x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.22 ms: 1.61x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 335 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 155 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.18 sec: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.05 ms: 1.17x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.36 us: 1.17x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 20.9 us: 1.11x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                       |
| deepcopy                   | 223 us                                                      | 203 us: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 46.4 ms: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.15 ms: 1.05x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 80.7 ms: 1.04x faster                                                      |
| pidigits                   | 146 ms                                                      | 142 ms: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.5 ms: 1.02x faster                                                      |
| json_loads                 | 15.1 us                                                     | 15.8 us: 1.05x slower                                                      |
| pycparser                  | 695 ms                                                      | 731 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.13 us: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.9 ms: 1.07x slower                                                      |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.72 ms: 1.08x slower                                                      |
| go                         | 84.7 ms                                                     | 92.9 ms: 1.10x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.34 ms: 1.10x slower                                                      |
| python_startup             | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| sympy_expand               | 286 ms                                                      | 322 ms: 1.13x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.1 ns: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.2 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 328 ms: 1.16x slower                                                       |
| sympy_str                  | 167 ms                                                      | 193 ms: 1.16x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.72 us: 1.16x slower                                                      |
| fannkuch                   | 252 ms                                                      | 294 ms: 1.17x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 74.2 ms: 1.17x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 94.4 ms: 1.17x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.23 us: 1.17x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 567 ms: 1.17x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 89.8 ms: 1.18x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.1 ms: 1.18x slower                                                      |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                       |
| sphinx                     | 617 ms                                                      | 731 ms: 1.18x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 40.3 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 102 ms: 1.20x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 68.2 ms: 1.20x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.5 us: 1.20x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.2 ms: 1.21x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.67 ms: 1.22x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.2 ms: 1.22x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.20 ms: 1.23x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 89.1 ms: 1.24x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.9 ms: 1.24x slower                                                      |
| nbody                      | 66.3 ms                                                     | 82.2 ms: 1.24x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 56.8 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 51.5 ms: 1.26x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 19.7 ms: 1.29x slower                                                      |
| scimark_fft                | 175 ms                                                      | 227 ms: 1.30x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 242 us: 1.30x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.48 ms: 1.31x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 74.6 ms: 1.33x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                      |
| richards                   | 26.3 ms                                                     | 35.5 ms: 1.35x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.10 ms: 1.35x slower                                                      |
| raytrace                   | 153 ms                                                      | 211 ms: 1.38x slower                                                       |
| richards_super             | 29.8 ms                                                     | 41.3 ms: 1.39x slower                                                      |
| coverage                   | 45.3 ms                                                     | 66.3 ms: 1.46x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.71 ms: 1.48x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.72 sec: 1.60x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.72 sec: 1.76x slower                                                     |
| many_optionals             | 361 us                                                      | 656 us: 1.82x slower                                                       |
| shortest_path              | 355 ms                                                      | 673 ms: 1.89x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.97 sec: 1.94x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.59 sec: 1.95x slower                                                     |
| connected_components       | 320 ms                                                      | 636 ms: 1.99x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.77 sec: 2.02x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 36.4 ms: 3.35x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.080x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown