# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.014x faster
- HPT reliability: 87.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 324 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.11x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 813 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| async_generators           | 364 ms                                                       | 392 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.6 ms: 1.10x faster                                                       |
| float          | 81.6 ms                                                      | 75.5 ms: 1.08x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 252 ms: 1.06x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.75 ms: 1.07x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 26.6 ms: 1.07x slower                                                       |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                      |
| xml_etree_generate   | 85.2 ms                                                      | 78.4 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| json_loads           | 24.7 us                                                      | 24.0 us: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 97.5 ms: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 330 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                       |
| django_template | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 63.6 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.87 ms: 1.42x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 28.2 us: 1.38x faster                                                       |
| deepcopy                   | 388 us                                                       | 300 us: 1.29x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.18x faster                                                       |
| richards                   | 52.5 ms                                                      | 44.7 ms: 1.18x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 82.9 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| scimark_sor                | 125 ms                                                       | 107 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| richards_super             | 60.2 ms                                                      | 51.8 ms: 1.16x faster                                                       |
| telco                      | 8.77 ms                                                      | 7.61 ms: 1.15x faster                                                       |
| async_tree_none            | 370 ms                                                       | 324 ms: 1.14x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                      |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 755 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                        |
| nbody                      | 92.1 ms                                                      | 83.6 ms: 1.10x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 78.4 ms: 1.09x faster                                                       |
| go                         | 167 ms                                                       | 154 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| float                      | 81.6 ms                                                      | 75.5 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.58 sec: 1.08x faster                                                      |
| fannkuch                   | 384 ms                                                       | 359 ms: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                                       |
| scimark_fft                | 298 ms                                                       | 280 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.80 sec: 1.06x faster                                                      |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.21 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.30 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 71.1 ms: 1.03x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 94.4 ms: 1.03x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.0 us: 1.03x faster                                                       |
| pyflate                    | 493 ms                                                       | 478 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 97.5 ms: 1.02x faster                                                       |
| async_tree_io              | 832 ms                                                       | 813 ms: 1.02x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                       |
| thrift                     | 918 us                                                       | 899 us: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| coverage                   | 84.5 ms                                                      | 84.0 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 952 us: 1.02x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 330 us: 1.03x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.26 us: 1.04x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.2 ms: 1.05x slower                                                       |
| sympy_expand               | 506 ms                                                       | 532 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 185 us: 1.05x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.62 us: 1.06x slower                                                       |
| regex_dna                  | 238 ms                                                       | 252 ms: 1.06x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.75 ms: 1.07x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 26.6 ms: 1.07x slower                                                       |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| django_template            | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                       |
| async_generators           | 364 ms                                                       | 392 ms: 1.08x slower                                                        |
| sympy_str                  | 297 ms                                                       | 322 ms: 1.08x slower                                                        |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 101 ms: 1.09x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.08 ms: 1.09x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 63.6 ms: 1.10x slower                                                       |
| chaos                      | 60.6 ms                                                      | 67.3 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.54 ms: 1.13x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                        |
| generators                 | 33.9 ms                                                      | 38.4 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 135 ms: 1.13x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                      |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| raytrace                   | 267 ms                                                       | 320 ms: 1.20x slower                                                        |
| pylint                     | 345 ms                                                       | 419 ms: 1.21x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 1.87 sec: 388.31x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (2): logging_silent, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 87.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x