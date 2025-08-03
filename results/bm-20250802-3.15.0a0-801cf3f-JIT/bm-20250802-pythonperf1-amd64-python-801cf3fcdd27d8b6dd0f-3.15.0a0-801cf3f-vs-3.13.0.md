# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.073x faster
- HPT reliability: 90.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.25x faster                                                       |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 349 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                      |
| nbody          | 66.3 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.9 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.13 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.35 ms: 1.23x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 16.99x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.5 ms: 2.31x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| mdp                        | 1.43 sec                                                    | 819 ms: 1.75x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.29x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.25x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.35 ms: 1.23x faster                                                      |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.21x faster                                                       |
| scimark_fft                | 175 ms                                                      | 149 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.25 ms: 1.16x faster                                                      |
| fannkuch                   | 252 ms                                                      | 220 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.27 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.13x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.13x faster                                                      |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 349 ms: 1.10x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 454 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                      |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 930 ms: 1.05x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 77.9 ms: 1.04x faster                                                      |
| pyflate                    | 283 ms                                                      | 275 ms: 1.03x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.65 sec: 1.03x faster                                                     |
| shortest_path              | 355 ms                                                      | 346 ms: 1.03x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 71.0 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.13 ms: 1.01x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 45.8 ms: 1.00x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 54.9 ns: 1.01x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 77.3 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.9 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                      |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.4 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.2 ms: 1.04x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.48 us: 1.05x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.07 us: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 861 us: 1.06x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.5 ms: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| hexiom                     | 3.84 ms                                                     | 4.17 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.0 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.7 ms: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.6 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                      |
| many_optionals             | 361 us                                                      | 588 us: 1.63x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.4 ms: 2.80x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (6): pylint, sqlite_synth, pycparser, regex_dna, connected_components, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 90.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown