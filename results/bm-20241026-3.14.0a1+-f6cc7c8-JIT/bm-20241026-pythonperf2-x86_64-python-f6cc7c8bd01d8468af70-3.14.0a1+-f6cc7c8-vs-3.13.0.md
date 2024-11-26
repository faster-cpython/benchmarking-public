# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.009x slower
- HPT reliability: 71.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 382 ms: 1.20x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 402 ms: 1.11x faster                                                         |
| async_tree_none            | 370 ms                                                       | 334 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 573 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 558 ms: 1.03x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 333 ms: 1.03x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 836 ms: 1.02x slower                                                         |
| async_generators           | 364 ms                                                       | 379 ms: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.8 ms: 1.10x faster                                                        |
| float          | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 240 ms: 1.01x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 25.1 ms: 1.01x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                        |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.07 sec: 1.17x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 80.9 ms: 1.05x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.01x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 221 us: 1.02x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 336 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup         | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.49 ms: 1.09x faster                                                        |
| genshi_text     | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                        |
| django_template | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                        |
| genshi_xml      | 58.0 ms                                                      | 67.9 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 31.2 us: 1.25x faster                                                        |
| richards_super             | 60.2 ms                                                      | 49.3 ms: 1.22x faster                                                        |
| deepcopy                   | 388 us                                                       | 319 us: 1.22x faster                                                         |
| richards                   | 52.5 ms                                                      | 43.7 ms: 1.20x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 382 ms: 1.20x faster                                                         |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.07 sec: 1.17x faster                                                       |
| telco                      | 8.77 ms                                                      | 7.81 ms: 1.12x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 402 ms: 1.11x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 3.14 us: 1.11x faster                                                        |
| async_tree_none            | 370 ms                                                       | 334 ms: 1.11x faster                                                         |
| nbody                      | 92.1 ms                                                      | 83.8 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                        |
| pyflate                    | 493 ms                                                       | 450 ms: 1.09x faster                                                         |
| go                         | 167 ms                                                       | 153 ms: 1.09x faster                                                         |
| json                       | 5.62 ms                                                      | 5.15 ms: 1.09x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.49 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.83 sec: 1.05x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 80.9 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 795 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 93.6 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 573 ms: 1.04x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 63.2 ms: 1.04x faster                                                        |
| logging_silent             | 97.5 ns                                                      | 94.2 ns: 1.03x faster                                                        |
| fannkuch                   | 384 ms                                                       | 372 ms: 1.03x faster                                                         |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                        |
| coverage                   | 84.5 ms                                                      | 82.1 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 558 ms: 1.03x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 333 ms: 1.03x faster                                                         |
| scimark_fft                | 298 ms                                                       | 290 ms: 1.03x faster                                                         |
| deltablue                  | 3.38 ms                                                      | 3.30 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| float                      | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 100 ms: 1.01x slower                                                         |
| regex_dna                  | 238 ms                                                       | 240 ms: 1.01x slower                                                         |
| regex_v8                   | 24.9 ms                                                      | 25.1 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup             | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.02x slower                                                       |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.4 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 836 ms: 1.02x slower                                                         |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 221 us: 1.02x slower                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                        |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.02x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.13 us: 1.03x slower                                                        |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                         |
| bench_thread_pool          | 929 us                                                       | 954 us: 1.03x slower                                                         |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| mdp                        | 2.53 sec                                                     | 2.62 sec: 1.04x slower                                                       |
| async_generators           | 364 ms                                                       | 379 ms: 1.04x slower                                                         |
| pickle_pure_python         | 322 us                                                       | 336 us: 1.05x slower                                                         |
| logging_simple             | 6.28 us                                                      | 6.57 us: 1.05x slower                                                        |
| sympy_expand               | 506 ms                                                       | 535 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 176 us                                                       | 187 us: 1.07x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.7 ms: 1.07x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.87 ms: 1.08x slower                                                        |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                         |
| sympy_str                  | 297 ms                                                       | 323 ms: 1.09x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.09x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.18 ms: 1.11x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                        |
| comprehensions             | 17.3 us                                                      | 19.4 us: 1.12x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 104 ms: 1.13x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 135 ms: 1.13x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 168 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| django_template            | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                        |
| chaos                      | 60.6 ms                                                      | 69.2 ms: 1.14x slower                                                        |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| generators                 | 33.9 ms                                                      | 38.8 ms: 1.14x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.15x slower                                                         |
| raytrace                   | 267 ms                                                       | 310 ms: 1.16x slower                                                         |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 67.9 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 68.9 ms: 1.17x slower                                                        |
| pylint                     | 345 ms                                                       | 423 ms: 1.23x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 5.52 ms: 1.23x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 2.79 sec: 579.67x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (4): thrift, scimark_sparse_mat_mult, xml_etree_parse, async_tree_io
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.009x slower
# HPT report

- Reliability score: 71.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x