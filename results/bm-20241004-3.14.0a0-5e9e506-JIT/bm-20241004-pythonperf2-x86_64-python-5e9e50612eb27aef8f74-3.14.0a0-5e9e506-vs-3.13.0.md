# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.08x slower
- HPT reliability: 56.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 318 ms: 1.09x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.27 sec: 1.16x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 124 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 326 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 417 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 566 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| async_tree_io_tg           | 819 ms                                                       | 833 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.0 ms: 1.09x faster                                                       |
| float          | 81.9 ms                                                      | 77.5 ms: 1.06x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.02x faster                                                       |
| regex_compile  | 144 ms                                                       | 149 ms: 1.03x slower                                                        |
| regex_dna      | 244 ms                                                       | 253 ms: 1.04x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                                      |
| xml_etree_generate   | 85.3 ms                                                      | 79.8 ms: 1.07x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 57.1 ms: 1.07x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.31 us: 1.06x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 30.7 us: 1.05x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| json_loads           | 24.0 us                                                      | 23.5 us: 1.02x faster                                                       |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| unpickle_list        | 4.62 us                                                      | 4.66 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 219 us: 1.02x slower                                                        |
| unpickle             | 15.1 us                                                      | 15.7 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| python_startup         | 13.3 ms                                                      | 15.1 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.20 ms: 1.13x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 62.3 ms: 1.09x slower                                                       |
| django_template | 38.9 ms                                                      | 44.9 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 27.3 us: 1.45x faster                                                       |
| deepcopy                   | 397 us                                                       | 300 us: 1.32x faster                                                        |
| scimark_sor                | 126 ms                                                       | 102 ms: 1.23x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 326 ms: 1.14x faster                                                        |
| richards_super             | 59.8 ms                                                      | 52.5 ms: 1.14x faster                                                       |
| richards                   | 52.7 ms                                                      | 46.5 ms: 1.13x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.20 ms: 1.13x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.63 ms: 1.13x faster                                                       |
| scimark_fft                | 314 ms                                                       | 283 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.18 sec: 1.10x faster                                                      |
| pyflate                    | 492 ms                                                       | 450 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                        |
| nbody                      | 88.0 ms                                                      | 81.0 ms: 1.09x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 417 ms: 1.08x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 90.6 ms: 1.08x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 91.1 ns: 1.07x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 79.8 ms: 1.07x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 57.1 ms: 1.07x faster                                                       |
| pickle_list                | 4.59 us                                                      | 4.31 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 566 ms: 1.06x faster                                                        |
| float                      | 81.9 ms                                                      | 77.5 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.83 sec: 1.06x faster                                                      |
| deltablue                  | 3.41 ms                                                      | 3.23 ms: 1.05x faster                                                       |
| go                         | 160 ms                                                       | 153 ms: 1.05x faster                                                        |
| pickle_dict                | 32.1 us                                                      | 30.7 us: 1.05x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 780 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.15 ms: 1.03x faster                                                       |
| coverage                   | 81.1 ms                                                      | 78.8 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                      |
| sqlite_synth               | 2.79 us                                                      | 2.72 us: 1.02x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.2 ms: 1.02x faster                                                       |
| json_loads                 | 24.0 us                                                      | 23.5 us: 1.02x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| json                       | 5.22 ms                                                      | 5.16 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 97.2 ms: 1.01x faster                                                       |
| html5lib                   | 71.9 ms                                                      | 71.5 ms: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                      |
| unpickle_list              | 4.62 us                                                      | 4.66 us: 1.01x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 833 ms: 1.02x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 219 us: 1.02x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                                      |
| typing_runtime_protocols   | 174 us                                                       | 179 us: 1.03x slower                                                        |
| regex_compile              | 144 ms                                                       | 149 ms: 1.03x slower                                                        |
| unpickle                   | 15.1 us                                                      | 15.7 us: 1.03x slower                                                       |
| tornado_http               | 120 ms                                                       | 124 ms: 1.04x slower                                                        |
| regex_dna                  | 244 ms                                                       | 253 ms: 1.04x slower                                                        |
| thrift                     | 877 us                                                       | 910 us: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                        |
| logging_format             | 7.07 us                                                      | 7.46 us: 1.06x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.76 us: 1.06x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                                       |
| sympy_expand               | 505 ms                                                       | 536 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.1 ms: 1.06x slower                                                       |
| chaos                      | 61.7 ms                                                      | 65.7 ms: 1.07x slower                                                       |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 969 us: 1.08x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 62.3 ms: 1.09x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                       |
| 2to3                       | 291 ms                                                       | 318 ms: 1.09x slower                                                        |
| sympy_str                  | 296 ms                                                       | 326 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                       |
| comprehensions             | 17.3 us                                                      | 19.3 us: 1.12x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 7.12 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 134 ms: 1.13x slower                                                        |
| python_startup             | 13.3 ms                                                      | 15.1 ms: 1.13x slower                                                       |
| raytrace                   | 289 ms                                                       | 331 ms: 1.15x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.15x slower                                                        |
| django_template            | 38.9 ms                                                      | 44.9 ms: 1.16x slower                                                       |
| generators                 | 33.5 ms                                                      | 38.8 ms: 1.16x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 179 ms: 1.16x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.27 sec: 1.16x slower                                                      |
| sqlglot_optimize           | 59.7 ms                                                      | 70.2 ms: 1.18x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 27.8 ms: 1.19x slower                                                       |
| pylint                     | 346 ms                                                       | 425 ms: 1.23x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 5.43 ms: 1.32x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 87.5 ns: 1.54x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 2.25 sec: 483.94x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (4): async_tree_io, fannkuch, asyncio_websockets, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 56.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x