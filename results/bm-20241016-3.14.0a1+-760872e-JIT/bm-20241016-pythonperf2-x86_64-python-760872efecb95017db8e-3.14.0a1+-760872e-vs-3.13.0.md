# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-x86_64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.003x slower
- HPT reliability: 64.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 315 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| html5lib       | 72.9 ms                                                      | 69.9 ms: 1.04x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                         |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                        |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                                         |
| async_generators           | 364 ms                                                       | 380 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 873 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 81.9 ms: 1.12x faster                                                        |
| float          | 81.6 ms                                                      | 79.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.44 ms: 1.02x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 24.6 ms: 1.01x faster                                                        |
| regex_dna      | 238 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.13 sec: 1.15x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 57.9 ms: 1.05x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 81.9 ms: 1.04x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.01x faster                                                        |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 330 us: 1.03x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.03x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.0 ms: 1.04x faster                                                        |
| python_startup_no_site | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.46 ms: 1.09x faster                                                        |
| genshi_text     | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                                        |
| genshi_xml      | 58.0 ms                                                      | 62.6 ms: 1.08x slower                                                        |
| django_template | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 308 us: 1.26x faster                                                         |
| deepcopy_memo              | 38.9 us                                                      | 31.3 us: 1.24x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                         |
| scimark_sor                | 125 ms                                                       | 103 ms: 1.21x faster                                                         |
| richards                   | 52.5 ms                                                      | 44.8 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 3.05 us: 1.15x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.15x faster                                                       |
| richards_super             | 60.2 ms                                                      | 53.0 ms: 1.14x faster                                                        |
| nbody                      | 92.1 ms                                                      | 81.9 ms: 1.12x faster                                                        |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                         |
| telco                      | 8.77 ms                                                      | 7.90 ms: 1.11x faster                                                        |
| json                       | 5.62 ms                                                      | 5.07 ms: 1.11x faster                                                        |
| go                         | 167 ms                                                       | 151 ms: 1.11x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.46 ms: 1.09x faster                                                        |
| pyflate                    | 493 ms                                                       | 453 ms: 1.09x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.72 sec: 1.08x faster                                                       |
| logging_silent             | 97.5 ns                                                      | 91.4 ns: 1.07x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                         |
| scimark_fft                | 298 ms                                                       | 282 ms: 1.06x faster                                                         |
| pprint_safe_repr           | 835 ms                                                       | 790 ms: 1.06x faster                                                         |
| coverage                   | 84.5 ms                                                      | 80.2 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 57.9 ms: 1.05x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 93.1 ms: 1.05x faster                                                        |
| python_startup             | 15.6 ms                                                      | 15.0 ms: 1.04x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 69.9 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 81.9 ms: 1.04x faster                                                        |
| fannkuch                   | 384 ms                                                       | 371 ms: 1.04x faster                                                         |
| thrift                     | 918 us                                                       | 887 us: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 71.5 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 95.1 ms: 1.02x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.30 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| float                      | 81.6 ms                                                      | 79.8 ms: 1.02x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.44 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                         |
| regex_v8                   | 24.9 ms                                                      | 24.6 ms: 1.01x faster                                                        |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                         |
| regex_dna                  | 238 ms                                                       | 243 ms: 1.02x slower                                                         |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.02x slower                                                         |
| pickle_pure_python         | 322 us                                                       | 330 us: 1.03x slower                                                         |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                                        |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                         |
| bench_thread_pool          | 929 us                                                       | 959 us: 1.03x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.37 ms: 1.04x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.23 us: 1.04x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                         |
| mdp                        | 2.53 sec                                                     | 2.64 sec: 1.04x slower                                                       |
| async_generators           | 364 ms                                                       | 380 ms: 1.04x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.2 ms: 1.05x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.59 us: 1.05x slower                                                        |
| sympy_expand               | 506 ms                                                       | 532 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 873 ms: 1.06x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                        |
| sympy_str                  | 297 ms                                                       | 318 ms: 1.07x slower                                                         |
| 2to3                       | 293 ms                                                       | 315 ms: 1.08x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 62.6 ms: 1.08x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.87 ms: 1.08x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.06 ms: 1.09x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.10x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.10x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                                         |
| django_template            | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| generators                 | 33.9 ms                                                      | 38.6 ms: 1.14x slower                                                        |
| chaos                      | 60.6 ms                                                      | 69.1 ms: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 27.2 ms: 1.16x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 69.5 ms: 1.19x slower                                                        |
| raytrace                   | 267 ms                                                       | 327 ms: 1.22x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 5.49 ms: 1.22x slower                                                        |
| pylint                     | 345 ms                                                       | 424 ms: 1.23x slower                                                         |
| bench_mp_pool              | 4.82 ms                                                      | 3.28 sec: 681.22x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (3): pidigits, xml_etree_iterparse, dulwich_log
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 64.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x