# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.283x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 421 ms: 1.44x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| html5lib       | 72.9 ms                                                      | 105 ms: 1.44x slower                                                        |
| tornado_http   | 119 ms                                                       | 166 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 377 ms: 1.05x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 475 ms: 1.04x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 882 ms: 1.07x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 371 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 636 ms: 1.11x slower                                                        |
| async_tree_io              | 832 ms                                                       | 939 ms: 1.13x slower                                                        |
| async_tree_none            | 370 ms                                                       | 422 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 681 ms: 1.14x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 519 ms: 1.16x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 26.9 ms: 1.25x slower                                                       |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.6 ms                                                      | 141 ms: 1.73x slower                                                        |
| nbody          | 92.1 ms                                                      | 193 ms: 2.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.53x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 246 ms: 1.03x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 27.0 ms: 1.08x slower                                                       |
| regex_compile  | 143 ms                                                       | 223 ms: 1.56x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 108 ms: 1.08x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.5 us: 1.19x slower                                                       |
| json_dumps           | 10.8 ms                                                      | 13.7 ms: 1.27x slower                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 111 ms: 1.30x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 3.31 sec: 1.36x slower                                                      |
| xml_etree_process    | 60.7 ms                                                      | 89.3 ms: 1.47x slower                                                       |
| pickle_pure_python   | 322 us                                                       | 579 us: 1.80x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 399 us: 1.85x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.34x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 17.4 ms: 1.11x slower                                                       |
| python_startup_no_site | 8.93 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 81.0 ms: 1.40x slower                                                       |
| genshi_text     | 27.2 ms                                                      | 42.0 ms: 1.54x slower                                                       |
| django_template | 38.9 ms                                                      | 65.4 ms: 1.68x slower                                                       |
| mako            | 10.3 ms                                                      | 21.3 ms: 2.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.65x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.72 ms: 1.54x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 3.19 ms: 1.40x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 377 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_dna                  | 238 ms                                                       | 246 ms: 1.03x slower                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 475 ms: 1.04x slower                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                       |
| json                       | 5.62 ms                                                      | 5.94 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 823 ms                                                       | 882 ms: 1.07x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 108 ms: 1.08x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 27.0 ms: 1.08x slower                                                       |
| async_tree_none_tg         | 342 ms                                                       | 371 ms: 1.09x slower                                                        |
| deepcopy                   | 388 us                                                       | 423 us: 1.09x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.2 ms: 1.10x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 636 ms: 1.11x slower                                                        |
| python_startup             | 15.6 ms                                                      | 17.4 ms: 1.11x slower                                                       |
| async_tree_io              | 832 ms                                                       | 939 ms: 1.13x slower                                                        |
| async_tree_none            | 370 ms                                                       | 422 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 681 ms: 1.14x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 519 ms: 1.16x slower                                                        |
| telco                      | 8.77 ms                                                      | 10.2 ms: 1.17x slower                                                       |
| json_loads                 | 24.7 us                                                      | 29.5 us: 1.19x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| generators                 | 33.9 ms                                                      | 42.1 ms: 1.24x slower                                                       |
| coverage                   | 84.5 ms                                                      | 105 ms: 1.25x slower                                                        |
| pylint                     | 345 ms                                                       | 430 ms: 1.25x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 26.9 ms: 1.25x slower                                                       |
| deepcopy_memo              | 38.9 us                                                      | 49.0 us: 1.26x slower                                                       |
| mdp                        | 2.53 sec                                                     | 3.19 sec: 1.26x slower                                                      |
| json_dumps                 | 10.8 ms                                                      | 13.7 ms: 1.27x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 6.52 sec: 1.28x slower                                                      |
| scimark_fft                | 298 ms                                                       | 384 ms: 1.29x slower                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 111 ms: 1.30x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.48 ms: 1.30x slower                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 4.55 us: 1.30x slower                                                       |
| meteor_contest             | 130 ms                                                       | 171 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.70 sec: 1.33x slower                                                      |
| tomli_loads                | 2.43 sec                                                     | 3.31 sec: 1.36x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 89.2 ms: 1.36x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 32.4 ms: 1.38x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 128 ms: 1.39x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 81.0 ms: 1.40x slower                                                       |
| tornado_http               | 119 ms                                                       | 166 ms: 1.40x slower                                                        |
| 2to3                       | 293 ms                                                       | 421 ms: 1.44x slower                                                        |
| html5lib                   | 72.9 ms                                                      | 105 ms: 1.44x slower                                                        |
| thrift                     | 918 us                                                       | 1.34 ms: 1.46x slower                                                       |
| xml_etree_process          | 60.7 ms                                                      | 89.3 ms: 1.47x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 258 us: 1.47x slower                                                        |
| sympy_str                  | 297 ms                                                       | 445 ms: 1.50x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 179 ms: 1.51x slower                                                        |
| fannkuch                   | 384 ms                                                       | 583 ms: 1.52x slower                                                        |
| pyflate                    | 493 ms                                                       | 754 ms: 1.53x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 90.1 ms: 1.54x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 42.0 ms: 1.54x slower                                                       |
| richards                   | 52.5 ms                                                      | 81.6 ms: 1.55x slower                                                       |
| regex_compile              | 143 ms                                                       | 223 ms: 1.56x slower                                                        |
| sympy_expand               | 506 ms                                                       | 805 ms: 1.59x slower                                                        |
| pprint_safe_repr           | 835 ms                                                       | 1.35 sec: 1.61x slower                                                      |
| crypto_pyaes               | 73.5 ms                                                      | 119 ms: 1.62x slower                                                        |
| richards_super             | 60.2 ms                                                      | 97.8 ms: 1.62x slower                                                       |
| pprint_pformat             | 1.70 sec                                                     | 2.79 sec: 1.64x slower                                                      |
| spectral_norm              | 97.4 ms                                                      | 161 ms: 1.65x slower                                                        |
| django_template            | 38.9 ms                                                      | 65.4 ms: 1.68x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 259 ms: 1.68x slower                                                        |
| comprehensions             | 17.3 us                                                      | 29.5 us: 1.71x slower                                                       |
| float                      | 81.6 ms                                                      | 141 ms: 1.73x slower                                                        |
| go                         | 167 ms                                                       | 292 ms: 1.75x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 11.4 ms: 1.76x slower                                                       |
| bench_thread_pool          | 929 us                                                       | 1.65 ms: 1.77x slower                                                       |
| logging_format             | 6.95 us                                                      | 12.4 us: 1.78x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 579 us: 1.80x slower                                                        |
| logging_simple             | 6.28 us                                                      | 11.3 us: 1.80x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 399 us: 1.85x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 181 ns: 1.86x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 3.34 ms: 1.89x slower                                                       |
| scimark_sor                | 125 ms                                                       | 247 ms: 1.98x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 130 ms: 1.99x slower                                                        |
| chaos                      | 60.6 ms                                                      | 121 ms: 1.99x slower                                                        |
| mako                       | 10.3 ms                                                      | 21.3 ms: 2.06x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 2.82 ms: 2.07x slower                                                       |
| nbody                      | 92.1 ms                                                      | 193 ms: 2.09x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 216 ms: 2.22x slower                                                        |
| raytrace                   | 267 ms                                                       | 596 ms: 2.23x slower                                                        |
| deltablue                  | 3.38 ms                                                      | 8.13 ms: 2.40x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 34.0 ms: 7.06x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.43x slower                                                                |
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.283x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.05x