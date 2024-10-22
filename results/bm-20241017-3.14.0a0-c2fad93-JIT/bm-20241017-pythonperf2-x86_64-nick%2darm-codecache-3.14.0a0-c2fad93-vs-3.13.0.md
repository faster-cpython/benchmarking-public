# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.08x slower
- HPT reliability: 61.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 316 ms: 1.09x slower                                                 |
| docutils       | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                               |
| html5lib       | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                        | 1.06x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 375 ms: 1.23x faster                                                 |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                 |
| async_tree_memoization     | 452 ms                                                       | 411 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 564 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                                 |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.01x faster                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                               |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                         |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 80.3 ms: 1.10x faster                                                |
| float          | 81.9 ms                                                      | 78.1 ms: 1.05x faster                                                |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                |
| regex_dna      | 244 ms                                                       | 247 ms: 1.01x slower                                                 |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                 |
| regex_effbot   | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                               |
| pickle_list          | 4.59 us                                                      | 4.25 us: 1.08x faster                                                |
| xml_etree_generate   | 85.3 ms                                                      | 79.4 ms: 1.08x faster                                                |
| xml_etree_process    | 60.9 ms                                                      | 56.6 ms: 1.07x faster                                                |
| pickle_dict          | 32.1 us                                                      | 30.2 us: 1.06x faster                                                |
| json_dumps           | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                                |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| json_loads           | 24.0 us                                                      | 23.9 us: 1.00x faster                                                |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                 |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.02x slower                                                 |
| unpickle_list        | 4.62 us                                                      | 4.75 us: 1.03x slower                                                |
| unpickle             | 15.1 us                                                      | 15.7 us: 1.04x slower                                                |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                                |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                |
| genshi_text     | 26.6 ms                                                      | 28.9 ms: 1.09x slower                                                |
| django_template | 38.9 ms                                                      | 42.5 ms: 1.09x slower                                                |
| genshi_xml      | 57.3 ms                                                      | 64.8 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.1 us: 1.40x faster                                                |
| deepcopy                   | 397 us                                                       | 302 us: 1.32x faster                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 375 ms: 1.23x faster                                                 |
| scimark_sor                | 126 ms                                                       | 106 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                |
| richards                   | 52.7 ms                                                      | 45.0 ms: 1.17x faster                                                |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.15x faster                                                 |
| mako                       | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                |
| scimark_fft                | 314 ms                                                       | 278 ms: 1.13x faster                                                 |
| richards_super             | 59.8 ms                                                      | 53.3 ms: 1.12x faster                                                |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                 |
| telco                      | 8.58 ms                                                      | 7.76 ms: 1.11x faster                                                |
| tomli_loads                | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                               |
| async_tree_memoization     | 452 ms                                                       | 411 ms: 1.10x faster                                                 |
| nbody                      | 88.0 ms                                                      | 80.3 ms: 1.10x faster                                                |
| pyflate                    | 492 ms                                                       | 450 ms: 1.09x faster                                                 |
| logging_silent             | 97.7 ns                                                      | 90.2 ns: 1.08x faster                                                |
| spectral_norm              | 97.4 ms                                                      | 90.2 ms: 1.08x faster                                                |
| pickle_list                | 4.59 us                                                      | 4.25 us: 1.08x faster                                                |
| xml_etree_generate         | 85.3 ms                                                      | 79.4 ms: 1.08x faster                                                |
| xml_etree_process          | 60.9 ms                                                      | 56.6 ms: 1.07x faster                                                |
| bpe_tokeniser              | 5.10 sec                                                     | 4.79 sec: 1.06x faster                                               |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 564 ms: 1.06x faster                                                 |
| pickle_dict                | 32.1 us                                                      | 30.2 us: 1.06x faster                                                |
| go                         | 160 ms                                                       | 152 ms: 1.06x faster                                                 |
| deltablue                  | 3.41 ms                                                      | 3.24 ms: 1.05x faster                                                |
| float                      | 81.9 ms                                                      | 78.1 ms: 1.05x faster                                                |
| json_dumps                 | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.13 ms: 1.04x faster                                                |
| coverage                   | 81.1 ms                                                      | 78.4 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                                 |
| sqlite_synth               | 2.79 us                                                      | 2.71 us: 1.03x faster                                                |
| crypto_pyaes               | 72.8 ms                                                      | 71.1 ms: 1.02x faster                                                |
| pprint_safe_repr           | 812 ms                                                       | 794 ms: 1.02x faster                                                 |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                               |
| json                       | 5.22 ms                                                      | 5.17 ms: 1.01x faster                                                |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                 |
| scimark_lu                 | 97.8 ms                                                      | 97.0 ms: 1.01x faster                                                |
| html5lib                   | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.01x faster                                                |
| json_loads                 | 24.0 us                                                      | 23.9 us: 1.00x faster                                                |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                               |
| python_startup_no_site     | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                                |
| dulwich_log                | 65.5 ms                                                      | 65.9 ms: 1.01x slower                                                |
| fannkuch                   | 365 ms                                                       | 367 ms: 1.01x slower                                                 |
| thrift                     | 877 us                                                       | 883 us: 1.01x slower                                                 |
| regex_dna                  | 244 ms                                                       | 247 ms: 1.01x slower                                                 |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                 |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                 |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.02x slower                                                 |
| unpickle_list              | 4.62 us                                                      | 4.75 us: 1.03x slower                                                |
| regex_effbot               | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                |
| logging_format             | 7.07 us                                                      | 7.28 us: 1.03x slower                                                |
| unpickle                   | 15.1 us                                                      | 15.7 us: 1.04x slower                                                |
| mdp                        | 2.52 sec                                                     | 2.62 sec: 1.04x slower                                               |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                 |
| sympy_expand               | 505 ms                                                       | 526 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 174 us                                                       | 181 us: 1.04x slower                                                 |
| logging_simple             | 6.40 us                                                      | 6.71 us: 1.05x slower                                                |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.3 ms: 1.05x slower                                                |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                 |
| bench_thread_pool          | 901 us                                                       | 968 us: 1.07x slower                                                 |
| sympy_str                  | 296 ms                                                       | 320 ms: 1.08x slower                                                 |
| genshi_text                | 26.6 ms                                                      | 28.9 ms: 1.09x slower                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                |
| 2to3                       | 291 ms                                                       | 316 ms: 1.09x slower                                                 |
| django_template            | 38.9 ms                                                      | 42.5 ms: 1.09x slower                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                |
| chaos                      | 61.7 ms                                                      | 68.4 ms: 1.11x slower                                                |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                |
| raytrace                   | 289 ms                                                       | 324 ms: 1.12x slower                                                 |
| hexiom                     | 6.33 ms                                                      | 7.13 ms: 1.13x slower                                                |
| comprehensions             | 17.3 us                                                      | 19.4 us: 1.13x slower                                                |
| genshi_xml                 | 57.3 ms                                                      | 64.8 ms: 1.13x slower                                                |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                 |
| sqlglot_normalize          | 118 ms                                                       | 135 ms: 1.14x slower                                                 |
| docutils                   | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                               |
| sqlglot_optimize           | 59.7 ms                                                      | 69.3 ms: 1.16x slower                                                |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                 |
| sympy_integrate            | 23.3 ms                                                      | 27.3 ms: 1.17x slower                                                |
| generators                 | 33.5 ms                                                      | 39.8 ms: 1.19x slower                                                |
| pylint                     | 346 ms                                                       | 418 ms: 1.21x slower                                                 |
| gc_traversal               | 4.11 ms                                                      | 5.17 ms: 1.26x slower                                                |
| unpack_sequence            | 56.8 ns                                                      | 88.6 ns: 1.56x slower                                                |
| create_gc_cycles           | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                |
| bench_mp_pool              | 4.65 ms                                                      | 2.97 sec: 638.52x slower                                             |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                         |

Benchmark hidden because not significant (5): async_tree_io, pycparser, asyncio_websockets, xml_etree_parse, async_tree_io_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx

# HPT report

- Reliability score: 61.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x