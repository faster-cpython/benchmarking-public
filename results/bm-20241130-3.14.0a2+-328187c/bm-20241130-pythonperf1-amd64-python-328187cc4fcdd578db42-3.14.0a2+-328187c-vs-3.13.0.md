# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 223 ms: 1.01x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.9 ms: 1.05x slower                                                       |
| sphinx         | 633 ms                                                      | 673 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                        |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.06x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 301 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 406 ms: 1.06x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 419 ms: 1.11x slower                                                        |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.11x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 582 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 56.6 ms: 1.13x slower                                                       |
| nbody          | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.44 ms: 1.09x faster                                                       |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 94.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.5 ms: 1.06x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 58.2 ms: 1.08x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 7.08 ms: 1.20x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 227 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.4 ms: 1.04x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                       |
| django_template | 22.4 ms                                                     | 25.3 ms: 1.13x slower                                                       |
| mako            | 6.35 ms                                                     | 7.53 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 540 us: 16.30x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                       |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                        |
| pylint                     | 211 ms                                                      | 190 ms: 1.11x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 21.3 us: 1.10x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.44 ms: 1.09x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 74.5 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                       |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.06x faster                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 81.7 ms: 1.06x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 301 ms: 1.06x faster                                                        |
| gc_traversal               | 1.97 ms                                                     | 1.87 ms: 1.05x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 809 us: 1.05x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.4 ms: 1.04x faster                                                       |
| shortest_path              | 362 ms                                                      | 358 ms: 1.01x faster                                                        |
| 2to3                       | 221 ms                                                      | 223 ms: 1.01x slower                                                        |
| xml_etree_parse            | 93.6 ms                                                     | 94.8 ms: 1.01x slower                                                       |
| telco                      | 4.79 ms                                                     | 4.88 ms: 1.02x slower                                                       |
| go                         | 87.0 ms                                                     | 89.7 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.7 ms: 1.03x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.32 ms: 1.05x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.9 ms: 1.05x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.0 ms: 1.05x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 77.5 ms: 1.05x slower                                                       |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                        |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.5 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 406 ms: 1.06x slower                                                        |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                        |
| sphinx                     | 633 ms                                                      | 673 ms: 1.06x slower                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 3.10 sec: 1.06x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.38 us: 1.07x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.72 us: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 58.2 ms: 1.08x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 49.1 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                       |
| pycparser                  | 683 ms                                                      | 741 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.09x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 419 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 36.6 ms: 1.11x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.11x slower                                                        |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 582 ms: 1.12x slower                                                        |
| pprint_safe_repr           | 494 ms                                                      | 556 ms: 1.13x slower                                                        |
| django_template            | 22.4 ms                                                     | 25.3 ms: 1.13x slower                                                       |
| float                      | 49.9 ms                                                     | 56.6 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.80 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 200 ms: 1.15x slower                                                        |
| chaos                      | 38.5 ms                                                     | 44.3 ms: 1.15x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.3 ms: 1.15x slower                                                       |
| fannkuch                   | 253 ms                                                      | 292 ms: 1.15x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                       |
| pyflate                    | 283 ms                                                      | 327 ms: 1.15x slower                                                        |
| spectral_norm              | 62.8 ms                                                     | 72.7 ms: 1.16x slower                                                       |
| nbody                      | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 4.58 ms: 1.18x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.5 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.18x slower                                                       |
| mako                       | 6.35 ms                                                     | 7.53 ms: 1.19x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.2 us: 1.19x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 919 us: 1.19x slower                                                        |
| scimark_fft                | 172 ms                                                      | 206 ms: 1.19x slower                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.8 ms: 1.19x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 63.4 ms: 1.20x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 7.08 ms: 1.20x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 227 us: 1.20x slower                                                        |
| richards                   | 27.3 ms                                                     | 32.8 ms: 1.20x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 91.6 ms: 1.20x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.31 ms: 1.20x slower                                                       |
| raytrace                   | 160 ms                                                      | 194 ms: 1.21x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.11 sec: 1.22x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 67.4 ns: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (9): json_loads, connected_components, async_tree_none_tg, coverage, async_tree_memoization, regex_dna, pidigits, json, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown