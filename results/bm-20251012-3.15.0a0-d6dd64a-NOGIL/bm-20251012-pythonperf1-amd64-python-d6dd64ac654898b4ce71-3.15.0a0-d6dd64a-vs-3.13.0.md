# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.034x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.86 sec: 1.86x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                      |
| sphinx         | 617 ms                                                      | 675 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.17x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 318 ms: 1.56x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 323 ms: 1.18x faster                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.2 ms: 1.13x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 78.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 89.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.3 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.04 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.1 us: 1.06x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 146 us: 1.12x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 60.6 ms: 1.13x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.19x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.28 sec: 1.66x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                      |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| mako            | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 557 us: 15.20x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.9 ms: 2.61x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.17x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.22 ms: 1.61x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 318 ms: 1.56x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.05 sec: 1.36x faster                                                     |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.26x faster                                                      |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.02 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 323 ms: 1.18x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.38 us: 1.15x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 74.5 ms: 1.13x faster                                                      |
| float                      | 50.8 ms                                                     | 45.2 ms: 1.13x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.3 ms: 1.03x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.04 ms: 1.03x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.99 us: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.00x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.7 ms: 1.01x slower                                                      |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 296 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 80.9 ms: 1.06x slower                                                      |
| go                         | 84.7 ms                                                     | 90.0 ms: 1.06x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.1 us: 1.06x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 67.7 ms: 1.07x slower                                                      |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 309 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.09x slower                                                       |
| sphinx                     | 617 ms                                                      | 675 ms: 1.09x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.8 ns: 1.10x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 533 ms: 1.10x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 93.9 ms: 1.10x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 89.2 ms: 1.11x slower                                                      |
| generators                 | 19.0 ms                                                     | 21.0 ms: 1.11x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.90 ms: 1.11x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 146 us: 1.12x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.97 us: 1.13x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.7 us: 1.13x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.54 us: 1.13x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 60.6 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 64.4 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.40 ms: 1.15x slower                                                      |
| nbody                      | 66.3 ms                                                     | 78.2 ms: 1.18x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.4 ms: 1.19x slower                                                      |
| fannkuch                   | 252 ms                                                      | 300 ms: 1.19x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.19x slower                                                       |
| richards                   | 26.3 ms                                                     | 31.4 ms: 1.20x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.9 ms: 1.20x slower                                                      |
| chaos                      | 37.9 ms                                                     | 45.6 ms: 1.20x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.32 ms: 1.22x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 127 us: 1.23x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 56.3 ms: 1.24x slower                                                      |
| richards_super             | 29.8 ms                                                     | 36.8 ms: 1.24x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.02 ms: 1.25x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 71.0 ms: 1.26x slower                                                      |
| raytrace                   | 153 ms                                                      | 206 ms: 1.34x slower                                                       |
| coverage                   | 45.3 ms                                                     | 68.2 ms: 1.51x slower                                                      |
| mako                       | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.67 sec: 1.57x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.59 sec: 1.63x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.28 sec: 1.66x slower                                                     |
| many_optionals             | 361 us                                                      | 619 us: 1.71x slower                                                       |
| shortest_path              | 355 ms                                                      | 651 ms: 1.83x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.86 sec: 1.86x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.45 sec: 1.90x slower                                                     |
| connected_components       | 320 ms                                                      | 618 ms: 1.93x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 35.0 ms: 3.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): pylint, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown