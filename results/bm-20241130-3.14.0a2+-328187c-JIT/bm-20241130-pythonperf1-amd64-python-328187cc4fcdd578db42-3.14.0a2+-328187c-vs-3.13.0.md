# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.018x faster
- HPT reliability: 92.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.80 sec: 1.15x slower                                                      |
| sphinx         | 633 ms                                                      | 694 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                        |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 410 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 414 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 575 ms: 1.11x slower                                                        |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                        |
| async_generators           | 223 ms                                                      | 266 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 50.8 ms: 1.35x faster                                                       |
| float          | 49.9 ms                                                     | 47.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.41 ms: 1.12x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.5 ms                                                     | 85.2 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 52.5 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 95.3 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.6 ms: 1.03x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.45 ms: 1.09x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 207 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.4 ms: 1.09x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.4 ms: 1.04x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.19 ms: 1.22x faster                                                       |
| django_template | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 43.9 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 546 us: 16.11x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.1 us: 1.44x faster                                                       |
| nbody                      | 68.4 ms                                                     | 50.8 ms: 1.35x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                                        |
| mako                       | 6.35 ms                                                     | 5.19 ms: 1.22x faster                                                       |
| deepcopy                   | 226 us                                                      | 189 us: 1.19x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.4 ms: 1.18x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 55.4 ms: 1.13x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.1 ms: 1.13x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 40.5 ms: 1.12x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.41 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.85 us: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.23 ms: 1.10x faster                                                       |
| scimark_fft                | 172 ms                                                      | 157 ms: 1.10x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 74.1 ms: 1.09x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.40 ms: 1.09x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.4 ms: 1.09x faster                                                       |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 2.71 sec: 1.07x faster                                                      |
| json                       | 3.19 ms                                                     | 2.98 ms: 1.07x faster                                                       |
| connected_components       | 332 ms                                                      | 314 ms: 1.06x faster                                                        |
| gc_traversal               | 1.97 ms                                                     | 1.86 ms: 1.06x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 82.1 ms: 1.05x faster                                                       |
| float                      | 49.9 ms                                                     | 47.7 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 494 ms                                                      | 472 ms: 1.05x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.4 ms: 1.04x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 958 ms: 1.04x faster                                                        |
| shortest_path              | 362 ms                                                      | 349 ms: 1.04x faster                                                        |
| xml_etree_generate         | 54.0 ms                                                     | 52.5 ms: 1.03x faster                                                       |
| meteor_contest             | 73.5 ms                                                     | 72.2 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| dulwich_log                | 40.8 ms                                                     | 40.2 ms: 1.02x faster                                                       |
| scimark_lu                 | 53.0 ms                                                     | 52.2 ms: 1.02x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                                        |
| fannkuch                   | 253 ms                                                      | 257 ms: 1.01x slower                                                        |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.6 ms                                                     | 95.3 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.6 ms: 1.03x slower                                                       |
| go                         | 87.0 ms                                                     | 89.6 ms: 1.03x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.14 us: 1.03x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.6 ms: 1.05x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.32 ms: 1.05x slower                                                       |
| pycparser                  | 683 ms                                                      | 715 ms: 1.05x slower                                                        |
| chaos                      | 38.5 ms                                                     | 40.4 ms: 1.05x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.61 us: 1.06x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 85.2 ms: 1.06x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 58.0 ns: 1.06x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 410 ms: 1.07x slower                                                        |
| sympy_expand               | 291 ms                                                      | 312 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                       |
| sympy_str                  | 169 ms                                                      | 182 ms: 1.08x slower                                                        |
| sympy_sum                  | 86.9 ms                                                     | 94.7 ms: 1.09x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.45 ms: 1.09x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 207 us: 1.09x slower                                                        |
| sphinx                     | 633 ms                                                      | 694 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 414 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 575 ms: 1.11x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 13.9 ms: 1.12x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.55 sec: 1.12x slower                                                      |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                        |
| sqlglot_parse              | 771 us                                                      | 871 us: 1.13x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.7 us: 1.14x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.80 sec: 1.15x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 65.4 ms: 1.15x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.6 ms: 1.16x slower                                                       |
| k_core                     | 1.74 sec                                                    | 2.02 sec: 1.16x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 38.3 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                       |
| richards                   | 27.3 ms                                                     | 32.4 ms: 1.19x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 266 ms: 1.19x slower                                                        |
| richards_super             | 30.9 ms                                                     | 36.8 ms: 1.19x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 211 ms: 1.21x slower                                                        |
| deltablue                  | 1.92 ms                                                     | 2.33 ms: 1.22x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 43.9 ms: 1.24x slower                                                       |
| raytrace                   | 160 ms                                                      | 205 ms: 1.28x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 5.03 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, pylint, async_tree_none_tg, json_loads, asyncio_websockets, async_tree_memoization, html5lib, pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 92.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown