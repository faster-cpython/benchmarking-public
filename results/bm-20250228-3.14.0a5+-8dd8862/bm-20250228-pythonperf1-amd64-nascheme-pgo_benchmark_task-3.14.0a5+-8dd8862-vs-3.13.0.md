# Results vs. 3.13.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-amd64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.010x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.5 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 218 ms: 1.02x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 72.8 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.9 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 226 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.8 ms: 1.06x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| django_template | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 506 us: 16.73x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.9 ms: 1.60x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.9 us: 1.16x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 58.5 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                       |
| async_generators           | 223 ms                                                      | 218 ms: 1.02x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.20 ms: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.58 ms: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.88 sec: 1.00x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| go                         | 84.7 ms                                                     | 86.6 ms: 1.02x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 86.2 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.03x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                       |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 75.0 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.4 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 855 us: 1.06x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 35.8 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                        |
| pycparser                  | 695 ms                                                      | 735 ms: 1.06x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.5 ms: 1.06x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.5 ms: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.9 ms: 1.06x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 34.9 ms: 1.07x slower                                                       |
| pyflate                    | 283 ms                                                      | 304 ms: 1.08x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 274 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.5 ms: 1.09x slower                                                       |
| nbody                      | 66.3 ms                                                     | 72.8 ms: 1.10x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.1 ms: 1.10x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 84.2 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.9 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.86 us: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.2 ms: 1.12x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 542 ms: 1.12x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 192 ms: 1.12x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.5 ms: 1.12x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.5 ms: 1.13x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.61 sec: 1.13x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.35 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.15x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 882 us: 1.15x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| many_optionals             | 361 us                                                      | 434 us: 1.20x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 226 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                       |
| raytrace                   | 153 ms                                                      | 192 ms: 1.25x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): pylint, connected_components, sqlite_synth, asyncio_websockets, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown