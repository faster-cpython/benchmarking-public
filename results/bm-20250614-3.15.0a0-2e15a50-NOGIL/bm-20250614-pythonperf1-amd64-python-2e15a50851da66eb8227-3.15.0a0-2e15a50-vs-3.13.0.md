# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.415x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.65x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 337 ms: 1.57x slower                                                       |
| docutils       | 1.53 sec                                                    | 4.15 sec: 2.71x slower                                                     |
| html5lib       | 38.2 ms                                                     | 63.8 ms: 1.67x slower                                                      |
| sphinx         | 617 ms                                                      | 1.26 sec: 2.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.95x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.11x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 310 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 551 ms: 1.11x slower                                                       |
| async_tree_io              | 513 ms                                                      | 580 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 457 ms: 1.19x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 243 ms: 1.22x slower                                                       |
| async_tree_none            | 219 ms                                                      | 273 ms: 1.24x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 332 ms: 1.25x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 480 ms: 1.26x slower                                                       |
| async_generators           | 223 ms                                                      | 407 ms: 1.83x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 32.8 ms: 2.62x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 140 ms: 1.04x faster                                                       |
| float          | 50.8 ms                                                     | 98.6 ms: 1.94x slower                                                      |
| nbody          | 66.3 ms                                                     | 176 ms: 2.66x slower                                                       |
| Geometric mean | (ref)                                                       | 1.70x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.82 ms: 1.07x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 160 ms: 1.98x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 112 ms: 1.22x slower                                                       |
| json_loads           | 15.1 us                                                     | 22.5 us: 1.49x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 9.45 ms: 1.53x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 93.0 ms: 1.54x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 107 ms: 2.00x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 78.8 ms: 2.16x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 455 us: 2.45x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 357 us: 2.74x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.02 sec: 3.66x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.97x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.5 ms: 1.13x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 66.0 ms: 1.95x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 33.4 ms: 2.20x slower                                                      |
| django_template | 20.3 ms                                                     | 45.3 ms: 2.23x slower                                                      |
| mako            | 6.56 ms                                                     | 16.4 ms: 2.50x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.21x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 836 us: 10.13x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.11x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 35.8 ms: 2.10x faster                                                      |
| regex_v8                   | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.79 ms: 1.10x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.13 ms: 1.09x faster                                                      |
| pidigits                   | 146 ms                                                      | 140 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.68 us: 1.06x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 89.5 ms: 1.06x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.82 ms: 1.07x slower                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 310 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 551 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.5 ms: 1.13x slower                                                      |
| async_tree_io              | 513 ms                                                      | 580 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 457 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 112 ms: 1.22x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 243 ms: 1.22x slower                                                       |
| async_tree_none            | 219 ms                                                      | 273 ms: 1.24x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 332 ms: 1.25x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 480 ms: 1.26x slower                                                       |
| json                       | 3.30 ms                                                     | 4.18 ms: 1.27x slower                                                      |
| pylint                     | 205 ms                                                      | 279 ms: 1.36x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 56.2 ms: 1.40x slower                                                      |
| deepcopy                   | 223 us                                                      | 332 us: 1.49x slower                                                       |
| json_loads                 | 15.1 us                                                     | 22.5 us: 1.49x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 9.45 ms: 1.53x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 93.0 ms: 1.54x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.25 ms: 1.54x slower                                                      |
| mdp                        | 1.43 sec                                                    | 2.23 sec: 1.56x slower                                                     |
| 2to3                       | 215 ms                                                      | 337 ms: 1.57x slower                                                       |
| telco                      | 4.85 ms                                                     | 7.95 ms: 1.64x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 119 ms: 1.66x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 142 ms: 1.67x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 63.8 ms: 1.67x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 3.41 us: 1.68x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 21.0 ms: 1.70x slower                                                      |
| sympy_expand               | 286 ms                                                      | 494 ms: 1.73x slower                                                       |
| sympy_str                  | 167 ms                                                      | 291 ms: 1.74x slower                                                       |
| many_optionals             | 361 us                                                      | 636 us: 1.76x slower                                                       |
| k_core                     | 1.70 sec                                                    | 3.02 sec: 1.78x slower                                                     |
| async_generators           | 223 ms                                                      | 407 ms: 1.83x slower                                                       |
| coverage                   | 45.3 ms                                                     | 83.7 ms: 1.85x slower                                                      |
| logging_format             | 6.18 us                                                     | 11.5 us: 1.87x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 43.2 us: 1.87x slower                                                      |
| logging_simple             | 5.77 us                                                     | 11.0 us: 1.91x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 198 us: 1.92x slower                                                       |
| float                      | 50.8 ms                                                     | 98.6 ms: 1.94x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 66.0 ms: 1.95x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 160 ms: 1.98x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 107 ms: 2.00x slower                                                       |
| sphinx                     | 617 ms                                                      | 1.26 sec: 2.04x slower                                                     |
| shortest_path              | 355 ms                                                      | 736 ms: 2.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 78.8 ms: 2.16x slower                                                      |
| connected_components       | 320 ms                                                      | 691 ms: 2.16x slower                                                       |
| pyflate                    | 283 ms                                                      | 617 ms: 2.18x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 33.4 ms: 2.20x slower                                                      |
| generators                 | 19.0 ms                                                     | 41.8 ms: 2.20x slower                                                      |
| django_template            | 20.3 ms                                                     | 45.3 ms: 2.23x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 126 ms: 2.25x slower                                                       |
| go                         | 84.7 ms                                                     | 191 ms: 2.26x slower                                                       |
| fannkuch                   | 252 ms                                                      | 581 ms: 2.31x slower                                                       |
| scimark_fft                | 175 ms                                                      | 412 ms: 2.36x slower                                                       |
| pycparser                  | 695 ms                                                      | 1.70 sec: 2.45x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 455 us: 2.45x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 6.39 ms: 2.45x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 187 ms: 2.45x slower                                                       |
| comprehensions             | 10.4 us                                                     | 25.4 us: 2.46x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 27.1 ms: 2.49x slower                                                      |
| mako                       | 6.56 ms                                                     | 16.4 ms: 2.50x slower                                                      |
| chaos                      | 37.9 ms                                                     | 95.4 ms: 2.52x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 118 ms: 2.58x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 107 ms: 2.62x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 166 ms: 2.62x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 32.8 ms: 2.62x slower                                                      |
| richards                   | 26.3 ms                                                     | 69.7 ms: 2.66x slower                                                      |
| nbody                      | 66.3 ms                                                     | 176 ms: 2.66x slower                                                       |
| richards_super             | 29.8 ms                                                     | 79.2 ms: 2.66x slower                                                      |
| raytrace                   | 153 ms                                                      | 409 ms: 2.67x slower                                                       |
| docutils                   | 1.53 sec                                                    | 4.15 sec: 2.71x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 357 us: 2.74x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 10.6 ms: 2.75x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 163 ms: 2.88x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 8.32 sec: 2.90x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 1.40 sec: 2.90x slower                                                     |
| deltablue                  | 1.89 ms                                                     | 5.89 ms: 3.12x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 5.02 sec: 3.66x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 4.05 sec: 4.14x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 583 ns: 10.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.75x slower                                                               |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.415x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.75x
- 95% likely to have a slowdown of 1.72x
- 99% likely to have a slowdown of 1.65x

# Memory
- memory change: unknown