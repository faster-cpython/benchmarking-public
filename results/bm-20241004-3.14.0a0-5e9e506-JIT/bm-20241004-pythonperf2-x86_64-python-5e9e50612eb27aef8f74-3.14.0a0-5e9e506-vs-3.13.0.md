# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.001x slower
- HPT reliability: 55.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 318 ms: 1.09x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.27 sec: 1.17x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                       |
| sphinx         | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                      |
| tornado_http   | 119 ms                                                       | 124 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 326 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 566 ms: 1.05x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 81.0 ms: 1.14x faster                                                       |
| float          | 81.6 ms                                                      | 77.5 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                       |
| regex_compile  | 143 ms                                                       | 149 ms: 1.04x slower                                                        |
| regex_dna      | 238 ms                                                       | 253 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                      |
| xml_etree_generate   | 85.2 ms                                                      | 79.8 ms: 1.07x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 57.1 ms: 1.06x faster                                                       |
| json_loads           | 24.7 us                                                      | 23.5 us: 1.05x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 219 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 334 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.1 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.20 ms: 1.12x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 28.2 ms: 1.04x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 62.3 ms: 1.07x slower                                                       |
| django_template | 38.9 ms                                                      | 44.9 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 27.3 us: 1.43x faster                                                       |
| deepcopy                   | 388 us                                                       | 300 us: 1.29x faster                                                        |
| scimark_sor                | 125 ms                                                       | 102 ms: 1.22x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 3.00 us: 1.16x faster                                                       |
| telco                      | 8.77 ms                                                      | 7.63 ms: 1.15x faster                                                       |
| richards_super             | 60.2 ms                                                      | 52.5 ms: 1.15x faster                                                       |
| nbody                      | 92.1 ms                                                      | 81.0 ms: 1.14x faster                                                       |
| async_tree_none            | 370 ms                                                       | 326 ms: 1.14x faster                                                        |
| richards                   | 52.5 ms                                                      | 46.5 ms: 1.13x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.20 ms: 1.12x faster                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                      |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                        |
| pyflate                    | 493 ms                                                       | 450 ms: 1.09x faster                                                        |
| go                         | 167 ms                                                       | 153 ms: 1.09x faster                                                        |
| json                       | 5.62 ms                                                      | 5.16 ms: 1.09x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 90.6 ms: 1.08x faster                                                       |
| coverage                   | 84.5 ms                                                      | 78.8 ms: 1.07x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 780 ms: 1.07x faster                                                        |
| logging_silent             | 97.5 ns                                                      | 91.1 ns: 1.07x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 79.8 ms: 1.07x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 57.1 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.61 sec: 1.06x faster                                                      |
| fannkuch                   | 384 ms                                                       | 364 ms: 1.06x faster                                                        |
| scimark_fft                | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.83 sec: 1.05x faster                                                      |
| json_loads                 | 24.7 us                                                      | 23.5 us: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 566 ms: 1.05x faster                                                        |
| float                      | 81.6 ms                                                      | 77.5 ms: 1.05x faster                                                       |
| deltablue                  | 3.38 ms                                                      | 3.23 ms: 1.05x faster                                                       |
| python_startup             | 15.6 ms                                                      | 15.1 ms: 1.04x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 71.2 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.15 ms: 1.01x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.27 sec: 1.01x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 219 us: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 179 us: 1.02x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.03x slower                                                      |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.03x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 28.2 ms: 1.04x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 334 us: 1.04x slower                                                        |
| regex_compile              | 143 ms                                                       | 149 ms: 1.04x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 969 us: 1.04x slower                                                        |
| tornado_http               | 119 ms                                                       | 124 ms: 1.04x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.80 ms: 1.06x slower                                                       |
| sympy_expand               | 506 ms                                                       | 536 ms: 1.06x slower                                                        |
| regex_dna                  | 238 ms                                                       | 253 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.1 ms: 1.06x slower                                                       |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 62.3 ms: 1.07x slower                                                       |
| logging_format             | 6.95 us                                                      | 7.46 us: 1.07x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.76 us: 1.08x slower                                                       |
| chaos                      | 60.6 ms                                                      | 65.7 ms: 1.08x slower                                                       |
| 2to3                       | 293 ms                                                       | 318 ms: 1.09x slower                                                        |
| sympy_str                  | 297 ms                                                       | 326 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.10x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 7.12 ms: 1.10x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.10x slower                                                        |
| comprehensions             | 17.3 us                                                      | 19.3 us: 1.11x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 134 ms: 1.13x slower                                                        |
| generators                 | 33.9 ms                                                      | 38.8 ms: 1.15x slower                                                       |
| sphinx                     | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                      |
| django_template            | 38.9 ms                                                      | 44.9 ms: 1.16x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 179 ms: 1.16x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.27 sec: 1.17x slower                                                      |
| sympy_integrate            | 23.4 ms                                                      | 27.8 ms: 1.19x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| gc_traversal               | 4.48 ms                                                      | 5.43 ms: 1.21x slower                                                       |
| pylint                     | 345 ms                                                       | 425 ms: 1.23x slower                                                        |
| raytrace                   | 267 ms                                                       | 331 ms: 1.24x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 2.25 sec: 467.55x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                |

Benchmark hidden because not significant (6): thrift, scimark_lu, pidigits, regex_effbot, async_tree_io_tg, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 55.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x