# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.003x slower
- HPT reliability: 70.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 297 ms: 1.02x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.11 sec: 1.11x slower                                                       |
| html5lib       | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.19 sec: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                         |
| async_tree_none            | 370 ms                                                       | 335 ms: 1.10x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                         |
| async_tree_io              | 832 ms                                                       | 851 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 842 ms: 1.02x slower                                                         |
| async_generators           | 364 ms                                                       | 473 ms: 1.30x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.20 ms: 1.10x faster                                                        |
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                                         |
| regex_dna      | 238 ms                                                       | 239 ms: 1.00x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 201 us: 1.07x faster                                                         |
| xml_etree_process    | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 82.2 ms: 1.04x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 336 us: 1.05x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.45 ms: 1.09x faster                                                        |
| django_template | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                        |
| genshi_text     | 27.2 ms                                                      | 28.5 ms: 1.05x slower                                                        |
| genshi_xml      | 58.0 ms                                                      | 62.6 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.0 us: 1.34x faster                                                        |
| richards_super             | 60.2 ms                                                      | 48.3 ms: 1.25x faster                                                        |
| deepcopy                   | 388 us                                                       | 312 us: 1.25x faster                                                         |
| richards                   | 52.5 ms                                                      | 44.2 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                         |
| scimark_sor                | 125 ms                                                       | 106 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 3.04 us: 1.15x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.65 ms: 1.15x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                                       |
| async_tree_none            | 370 ms                                                       | 335 ms: 1.10x faster                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.20 ms: 1.10x faster                                                        |
| connected_components       | 443 ms                                                       | 404 ms: 1.10x faster                                                         |
| mako                       | 10.3 ms                                                      | 9.45 ms: 1.09x faster                                                        |
| shortest_path              | 477 ms                                                       | 438 ms: 1.09x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                         |
| coverage                   | 84.5 ms                                                      | 78.6 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 201 us: 1.07x faster                                                         |
| json                       | 5.62 ms                                                      | 5.28 ms: 1.06x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.5 ms: 1.06x faster                                                        |
| go                         | 167 ms                                                       | 158 ms: 1.06x faster                                                         |
| xml_etree_process          | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                                        |
| nbody                      | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.24 ms: 1.05x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 93.6 ms: 1.04x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 82.2 ms: 1.04x faster                                                        |
| thrift                     | 918 us                                                       | 890 us: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.94 sec: 1.03x faster                                                       |
| logging_silent             | 97.5 ns                                                      | 94.8 ns: 1.03x faster                                                        |
| pyflate                    | 493 ms                                                       | 480 ms: 1.03x faster                                                         |
| html5lib                   | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 95.3 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 820 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                         |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                                         |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| python_startup_no_site     | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| regex_dna                  | 238 ms                                                       | 239 ms: 1.00x slower                                                         |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.01x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| 2to3                       | 293 ms                                                       | 297 ms: 1.02x slower                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.5 ms: 1.02x slower                                                        |
| async_tree_io              | 832 ms                                                       | 851 ms: 1.02x slower                                                         |
| regex_v8                   | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 842 ms: 1.02x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                        |
| python_startup             | 15.6 ms                                                      | 16.0 ms: 1.03x slower                                                        |
| django_template            | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.61 sec: 1.03x slower                                                       |
| scimark_fft                | 298 ms                                                       | 308 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.0 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.27 us: 1.04x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 336 us: 1.05x slower                                                         |
| sympy_expand               | 506 ms                                                       | 531 ms: 1.05x slower                                                         |
| sympy_str                  | 297 ms                                                       | 311 ms: 1.05x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 28.5 ms: 1.05x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.61 us: 1.05x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 981 us: 1.06x slower                                                         |
| sympy_integrate            | 23.4 ms                                                      | 24.7 ms: 1.06x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 163 ms: 1.06x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.19 sec: 1.07x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 62.6 ms: 1.08x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 99.8 ms: 1.08x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.89 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 64.2 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.10x slower                                                        |
| chaos                      | 60.6 ms                                                      | 66.8 ms: 1.10x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.11 sec: 1.11x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 7.18 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                        |
| comprehensions             | 17.3 us                                                      | 19.8 us: 1.15x slower                                                        |
| generators                 | 33.9 ms                                                      | 39.0 ms: 1.15x slower                                                        |
| k_core                     | 2.18 sec                                                     | 2.58 sec: 1.18x slower                                                       |
| raytrace                   | 267 ms                                                       | 326 ms: 1.22x slower                                                         |
| async_generators           | 364 ms                                                       | 473 ms: 1.30x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 6.26 ms: 1.40x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 1.09 sec: 226.23x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (7): pylint, async_tree_none_tg, crypto_pyaes, pycparser, float, dulwich_log, fannkuch
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 70.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x