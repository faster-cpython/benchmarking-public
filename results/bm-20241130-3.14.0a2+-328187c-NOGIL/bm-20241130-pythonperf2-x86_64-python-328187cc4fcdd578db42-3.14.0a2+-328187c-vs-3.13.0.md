# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.242x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 401 ms: 1.37x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.27 sec: 1.17x slower                                                       |
| html5lib       | 72.9 ms                                                      | 101 ms: 1.38x slower                                                         |
| sphinx         | 1.11 sec                                                     | 1.29 sec: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 380 ms: 1.04x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 468 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 369 ms: 1.08x slower                                                         |
| async_tree_none            | 370 ms                                                       | 400 ms: 1.08x slower                                                         |
| async_tree_io              | 832 ms                                                       | 902 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 629 ms: 1.10x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 666 ms: 1.12x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 500 ms: 1.12x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 25.2 ms: 1.17x slower                                                        |
| async_generators           | 364 ms                                                       | 556 ms: 1.53x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| nbody          | 92.1 ms                                                      | 141 ms: 1.53x slower                                                         |
| float          | 81.6 ms                                                      | 133 ms: 1.63x slower                                                         |
| Geometric mean | (ref)                                                        | 1.35x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.32 ms: 1.06x faster                                                        |
| regex_dna      | 238 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 27.7 ms: 1.11x slower                                                        |
| regex_compile  | 143 ms                                                       | 198 ms: 1.39x slower                                                         |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                         |
| json_loads           | 24.7 us                                                      | 27.9 us: 1.13x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.98 sec: 1.22x slower                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 104 ms: 1.23x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 14.8 ms: 1.37x slower                                                        |
| xml_etree_process    | 60.7 ms                                                      | 83.5 ms: 1.38x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 348 us: 1.61x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 538 us: 1.67x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 20.0 ms: 1.28x slower                                                        |
| python_startup_no_site | 8.93 ms                                                      | 12.2 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 72.5 ms: 1.25x slower                                                        |
| genshi_text     | 27.2 ms                                                      | 37.7 ms: 1.39x slower                                                        |
| django_template | 38.9 ms                                                      | 55.9 ms: 1.44x slower                                                        |
| mako            | 10.3 ms                                                      | 21.0 ms: 2.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.50x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.48 ms                                                      | 3.82 ms: 1.17x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.32 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| deepcopy                   | 388 us                                                       | 371 us: 1.05x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 380 ms: 1.04x faster                                                         |
| pidigits                   | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                         |
| json                       | 5.62 ms                                                      | 5.74 ms: 1.02x slower                                                        |
| regex_dna                  | 238 ms                                                       | 243 ms: 1.02x slower                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 468 ms: 1.02x slower                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.71 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                         |
| pathlib                    | 17.4 ms                                                      | 18.3 ms: 1.05x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 369 ms: 1.08x slower                                                         |
| async_tree_none            | 370 ms                                                       | 400 ms: 1.08x slower                                                         |
| async_tree_io              | 832 ms                                                       | 902 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 629 ms: 1.10x slower                                                         |
| deepcopy_memo              | 38.9 us                                                      | 42.6 us: 1.10x slower                                                        |
| telco                      | 8.77 ms                                                      | 9.63 ms: 1.10x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 27.7 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 666 ms: 1.12x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 500 ms: 1.12x slower                                                         |
| json_loads                 | 24.7 us                                                      | 27.9 us: 1.13x slower                                                        |
| shortest_path              | 477 ms                                                       | 546 ms: 1.14x slower                                                         |
| connected_components       | 443 ms                                                       | 510 ms: 1.15x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.29 sec: 1.16x slower                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 4.06 us: 1.16x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.27 sec: 1.17x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 25.2 ms: 1.17x slower                                                        |
| k_core                     | 2.18 sec                                                     | 2.56 sec: 1.17x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 6.04 sec: 1.19x slower                                                       |
| pylint                     | 345 ms                                                       | 412 ms: 1.20x slower                                                         |
| spectral_norm              | 97.4 ms                                                      | 117 ms: 1.20x slower                                                         |
| mdp                        | 2.53 sec                                                     | 3.03 sec: 1.20x slower                                                       |
| generators                 | 33.9 ms                                                      | 41.1 ms: 1.21x slower                                                        |
| scimark_fft                | 298 ms                                                       | 362 ms: 1.21x slower                                                         |
| meteor_contest             | 130 ms                                                       | 159 ms: 1.22x slower                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.98 sec: 1.22x slower                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 104 ms: 1.23x slower                                                         |
| coverage                   | 84.5 ms                                                      | 105 ms: 1.24x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 72.5 ms: 1.25x slower                                                        |
| python_startup             | 15.6 ms                                                      | 20.0 ms: 1.28x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.65 sec: 1.29x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 119 ms: 1.29x slower                                                         |
| dulwich_log                | 65.5 ms                                                      | 86.1 ms: 1.31x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 30.9 ms: 1.32x slower                                                        |
| sqlalchemy_imperative      | 18.1 ms                                                      | 24.1 ms: 1.33x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 234 us: 1.34x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 159 ms: 1.34x slower                                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 78.8 ms: 1.34x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 12.2 ms: 1.36x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 14.8 ms: 1.37x slower                                                        |
| 2to3                       | 293 ms                                                       | 401 ms: 1.37x slower                                                         |
| xml_etree_process          | 60.7 ms                                                      | 83.5 ms: 1.38x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.80 ms: 1.38x slower                                                        |
| html5lib                   | 72.9 ms                                                      | 101 ms: 1.38x slower                                                         |
| pprint_safe_repr           | 835 ms                                                       | 1.15 sec: 1.38x slower                                                       |
| regex_compile              | 143 ms                                                       | 198 ms: 1.39x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 37.7 ms: 1.39x slower                                                        |
| sympy_str                  | 297 ms                                                       | 414 ms: 1.40x slower                                                         |
| fannkuch                   | 384 ms                                                       | 538 ms: 1.40x slower                                                         |
| thrift                     | 918 us                                                       | 1.28 ms: 1.40x slower                                                        |
| pprint_pformat             | 1.70 sec                                                     | 2.39 sec: 1.41x slower                                                       |
| django_template            | 38.9 ms                                                      | 55.9 ms: 1.44x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 217 ms: 1.46x slower                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 108 ms: 1.46x slower                                                         |
| pyflate                    | 493 ms                                                       | 728 ms: 1.48x slower                                                         |
| sympy_expand               | 506 ms                                                       | 758 ms: 1.50x slower                                                         |
| richards                   | 52.5 ms                                                      | 79.3 ms: 1.51x slower                                                        |
| async_generators           | 364 ms                                                       | 556 ms: 1.53x slower                                                         |
| nbody                      | 92.1 ms                                                      | 141 ms: 1.53x slower                                                         |
| richards_super             | 60.2 ms                                                      | 92.7 ms: 1.54x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 247 ms: 1.61x slower                                                         |
| unpickle_pure_python       | 216 us                                                       | 348 us: 1.61x slower                                                         |
| float                      | 81.6 ms                                                      | 133 ms: 1.63x slower                                                         |
| go                         | 167 ms                                                       | 276 ms: 1.65x slower                                                         |
| logging_format             | 6.95 us                                                      | 11.5 us: 1.65x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 10.7 ms: 1.65x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 1.55 ms: 1.67x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 538 us: 1.67x slower                                                         |
| logging_simple             | 6.28 us                                                      | 10.5 us: 1.68x slower                                                        |
| comprehensions             | 17.3 us                                                      | 29.2 us: 1.69x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 174 ms: 1.79x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 3.18 ms: 1.81x slower                                                        |
| scimark_sor                | 125 ms                                                       | 229 ms: 1.83x slower                                                         |
| chaos                      | 60.6 ms                                                      | 111 ms: 1.84x slower                                                         |
| logging_silent             | 97.5 ns                                                      | 181 ns: 1.85x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 124 ms: 1.90x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 2.66 ms: 1.95x slower                                                        |
| mako                       | 10.3 ms                                                      | 21.0 ms: 2.04x slower                                                        |
| raytrace                   | 267 ms                                                       | 565 ms: 2.11x slower                                                         |
| deltablue                  | 3.38 ms                                                      | 7.92 ms: 2.34x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 54.6 ms: 11.33x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.36x slower                                                                 |
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.242x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: 1.21x