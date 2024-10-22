# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-x86_64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.09x slower
- HPT reliability: 68.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 315 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| html5lib       | 71.9 ms                                                      | 69.9 ms: 1.03x faster                                                        |
| tornado_http   | 120 ms                                                       | 123 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 378 ms: 1.22x faster                                                         |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.10x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.00x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                         |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 819 ms                                                       | 873 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.9 ms: 1.08x faster                                                        |
| float          | 81.9 ms                                                      | 79.8 ms: 1.03x faster                                                        |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.6 ms: 1.06x faster                                                        |
| regex_dna      | 244 ms                                                       | 243 ms: 1.00x faster                                                         |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.44 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 57.9 ms: 1.05x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 81.9 ms: 1.04x faster                                                        |
| unpickle             | 15.1 us                                                      | 15.3 us: 1.01x slower                                                        |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.02x slower                                                        |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.03x slower                                                        |
| xml_etree_parse      | 145 ms                                                       | 149 ms: 1.03x slower                                                         |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                         |
| unpickle_list        | 4.62 us                                                      | 4.78 us: 1.03x slower                                                        |
| pickle_list          | 4.59 us                                                      | 4.76 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                         |
| pickle_dict          | 32.1 us                                                      | 34.0 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 13.3 ms                                                      | 15.0 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.46 ms: 1.10x faster                                                        |
| genshi_text     | 26.6 ms                                                      | 28.0 ms: 1.05x slower                                                        |
| genshi_xml      | 57.3 ms                                                      | 62.6 ms: 1.09x slower                                                        |
| django_template | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 308 us: 1.29x faster                                                         |
| deepcopy_memo              | 39.5 us                                                      | 31.3 us: 1.26x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 378 ms: 1.22x faster                                                         |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                                         |
| richards                   | 52.7 ms                                                      | 44.8 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.05 us: 1.16x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                       |
| richards_super             | 59.8 ms                                                      | 53.0 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                         |
| scimark_fft                | 314 ms                                                       | 282 ms: 1.11x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.11x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.46 ms: 1.10x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.10x faster                                                         |
| telco                      | 8.58 ms                                                      | 7.90 ms: 1.09x faster                                                        |
| pyflate                    | 492 ms                                                       | 453 ms: 1.09x faster                                                         |
| bpe_tokeniser              | 5.10 sec                                                     | 4.72 sec: 1.08x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.9 ms: 1.08x faster                                                        |
| logging_silent             | 97.7 ns                                                      | 91.4 ns: 1.07x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 24.6 ms: 1.06x faster                                                        |
| go                         | 160 ms                                                       | 151 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.05x faster                                                         |
| xml_etree_process          | 60.9 ms                                                      | 57.9 ms: 1.05x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 93.1 ms: 1.05x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 81.9 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                         |
| deltablue                  | 3.41 ms                                                      | 3.30 ms: 1.03x faster                                                        |
| json                       | 5.22 ms                                                      | 5.07 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.71 us: 1.03x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 69.9 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.1 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 790 ms: 1.03x faster                                                         |
| float                      | 81.9 ms                                                      | 79.8 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| crypto_pyaes               | 72.8 ms                                                      | 71.5 ms: 1.02x faster                                                        |
| coverage                   | 81.1 ms                                                      | 80.2 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                         |
| regex_dna                  | 244 ms                                                       | 243 ms: 1.00x faster                                                         |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| unpickle                   | 15.1 us                                                      | 15.3 us: 1.01x slower                                                        |
| thrift                     | 877 us                                                       | 887 us: 1.01x slower                                                         |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                         |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| fannkuch                   | 365 ms                                                       | 371 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.37 ms: 1.02x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.23 us: 1.02x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.44 ms: 1.02x slower                                                        |
| tornado_http               | 120 ms                                                       | 123 ms: 1.02x slower                                                         |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.02x slower                                                        |
| json_dumps                 | 11.0 ms                                                      | 11.2 ms: 1.03x slower                                                        |
| xml_etree_parse            | 145 ms                                                       | 149 ms: 1.03x slower                                                         |
| pycparser                  | 1.26 sec                                                     | 1.29 sec: 1.03x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                         |
| logging_simple             | 6.40 us                                                      | 6.59 us: 1.03x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 4.78 us: 1.03x slower                                                        |
| pickle_list                | 4.59 us                                                      | 4.76 us: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                         |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                         |
| mdp                        | 2.52 sec                                                     | 2.64 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 183 us: 1.05x slower                                                         |
| genshi_text                | 26.6 ms                                                      | 28.0 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.2 ms: 1.05x slower                                                        |
| sympy_expand               | 505 ms                                                       | 532 ms: 1.05x slower                                                         |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                         |
| pickle_dict                | 32.1 us                                                      | 34.0 us: 1.06x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 959 us: 1.06x slower                                                         |
| async_tree_io_tg           | 819 ms                                                       | 873 ms: 1.07x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                        |
| sympy_str                  | 296 ms                                                       | 318 ms: 1.08x slower                                                         |
| 2to3                       | 291 ms                                                       | 315 ms: 1.08x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 62.6 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 7.06 ms: 1.11x slower                                                        |
| django_template            | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 132 ms: 1.12x slower                                                         |
| chaos                      | 61.7 ms                                                      | 69.1 ms: 1.12x slower                                                        |
| python_startup             | 13.3 ms                                                      | 15.0 ms: 1.12x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                                         |
| raytrace                   | 289 ms                                                       | 327 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| generators                 | 33.5 ms                                                      | 38.6 ms: 1.15x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 69.5 ms: 1.17x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 27.2 ms: 1.17x slower                                                        |
| pylint                     | 346 ms                                                       | 424 ms: 1.23x slower                                                         |
| gc_traversal               | 4.11 ms                                                      | 5.49 ms: 1.33x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 91.0 ns: 1.60x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 3.28 sec: 705.11x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (5): pickle, asyncio_tcp_ssl, async_tree_io, xml_etree_iterparse, dulwich_log
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx

# HPT report

- Reliability score: 68.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x