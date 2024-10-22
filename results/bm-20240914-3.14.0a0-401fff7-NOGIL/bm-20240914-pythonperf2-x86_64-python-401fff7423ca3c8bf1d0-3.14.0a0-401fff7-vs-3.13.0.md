# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.39x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 424 ms: 1.46x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.37 sec: 1.20x slower                                                      |
| html5lib       | 71.9 ms                                                      | 105 ms: 1.46x slower                                                        |
| tornado_http   | 120 ms                                                       | 166 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 382 ms                                                       | 379 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 467 ms: 1.01x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 364 ms: 1.07x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 878 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 625 ms: 1.09x slower                                                        |
| async_tree_io              | 847 ms                                                       | 928 ms: 1.10x slower                                                        |
| async_tree_none            | 372 ms                                                       | 411 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 673 ms: 1.12x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 511 ms: 1.13x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.80 sec: 1.14x slower                                                      |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 27.8 ms: 1.29x slower                                                       |
| async_generators           | 359 ms                                                       | 489 ms: 1.36x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 249 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 142 ms: 1.73x slower                                                        |
| nbody          | 88.0 ms                                                      | 191 ms: 2.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.55x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 250 ms: 1.03x slower                                                        |
| regex_v8       | 26.2 ms                                                      | 28.0 ms: 1.07x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| regex_compile  | 144 ms                                                       | 224 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 139 ms: 1.04x faster                                                        |
| pickle               | 10.5 us                                                      | 10.4 us: 1.02x faster                                                       |
| pickle_list          | 4.59 us                                                      | 4.53 us: 1.01x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 32.6 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 107 ms: 1.07x slower                                                        |
| unpickle_list        | 4.62 us                                                      | 5.31 us: 1.15x slower                                                       |
| unpickle             | 15.1 us                                                      | 17.4 us: 1.15x slower                                                       |
| json_loads           | 24.0 us                                                      | 28.8 us: 1.20x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 13.9 ms: 1.27x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 113 ms: 1.33x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.33 sec: 1.38x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 91.6 ms: 1.50x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 583 us: 1.83x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 399 us: 1.86x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.23x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.5 ms: 1.31x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 82.4 ms: 1.44x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 42.3 ms: 1.59x slower                                                       |
| django_template | 38.9 ms                                                      | 66.4 ms: 1.71x slower                                                       |
| mako            | 10.4 ms                                                      | 21.4 ms: 2.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.68x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 3.04 ms: 1.35x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.67 ms: 1.05x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 139 ms: 1.04x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.02x faster                                                       |
| pidigits                   | 253 ms                                                       | 249 ms: 1.01x faster                                                        |
| pickle_list                | 4.59 us                                                      | 4.53 us: 1.01x faster                                                       |
| asyncio_websockets         | 382 ms                                                       | 379 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 467 ms: 1.01x slower                                                        |
| pickle_dict                | 32.1 us                                                      | 32.6 us: 1.02x slower                                                       |
| regex_dna                  | 244 ms                                                       | 250 ms: 1.03x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.79 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 107 ms: 1.07x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 28.0 ms: 1.07x slower                                                       |
| async_tree_none_tg         | 340 ms                                                       | 364 ms: 1.07x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.61 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 819 ms                                                       | 878 ms: 1.07x slower                                                        |
| sqlite_synth               | 2.79 us                                                      | 3.00 us: 1.08x slower                                                       |
| deepcopy                   | 397 us                                                       | 430 us: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 625 ms: 1.09x slower                                                        |
| async_tree_io              | 847 ms                                                       | 928 ms: 1.10x slower                                                        |
| async_tree_none            | 372 ms                                                       | 411 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 673 ms: 1.12x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.6 ms: 1.12x slower                                                       |
| async_tree_memoization     | 452 ms                                                       | 511 ms: 1.13x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.80 sec: 1.14x slower                                                      |
| unpickle_list              | 4.62 us                                                      | 5.31 us: 1.15x slower                                                       |
| unpickle                   | 15.1 us                                                      | 17.4 us: 1.15x slower                                                       |
| json                       | 5.22 ms                                                      | 6.03 ms: 1.15x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.37 sec: 1.20x slower                                                      |
| json_loads                 | 24.0 us                                                      | 28.8 us: 1.20x slower                                                       |
| telco                      | 8.58 ms                                                      | 10.4 ms: 1.22x slower                                                       |
| generators                 | 33.5 ms                                                      | 41.4 ms: 1.24x slower                                                       |
| deepcopy_memo              | 39.5 us                                                      | 49.2 us: 1.25x slower                                                       |
| pylint                     | 346 ms                                                       | 433 ms: 1.25x slower                                                        |
| json_dumps                 | 11.0 ms                                                      | 13.9 ms: 1.27x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 27.8 ms: 1.29x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.25 sec: 1.29x slower                                                      |
| bpe_tokeniser              | 5.10 sec                                                     | 6.61 sec: 1.30x slower                                                      |
| scimark_fft                | 314 ms                                                       | 407 ms: 1.30x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 4.61 us: 1.30x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.63 ms: 1.31x slower                                                       |
| python_startup             | 13.3 ms                                                      | 17.5 ms: 1.31x slower                                                       |
| meteor_contest             | 128 ms                                                       | 169 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| coverage                   | 81.1 ms                                                      | 108 ms: 1.33x slower                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 113 ms: 1.33x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.70 sec: 1.35x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 89.1 ms: 1.36x slower                                                       |
| async_generators           | 359 ms                                                       | 489 ms: 1.36x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 32.2 ms: 1.38x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 3.33 sec: 1.38x slower                                                      |
| tornado_http               | 120 ms                                                       | 166 ms: 1.39x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 82.4 ms: 1.44x slower                                                       |
| 2to3                       | 291 ms                                                       | 424 ms: 1.46x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 105 ms: 1.46x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 129 ms: 1.47x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 91.6 ms: 1.50x slower                                                       |
| sympy_str                  | 296 ms                                                       | 446 ms: 1.51x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 263 us: 1.51x slower                                                        |
| richards                   | 52.7 ms                                                      | 79.9 ms: 1.52x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 180 ms: 1.52x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 91.1 ms: 1.53x slower                                                       |
| pyflate                    | 492 ms                                                       | 760 ms: 1.55x slower                                                        |
| thrift                     | 877 us                                                       | 1.36 ms: 1.55x slower                                                       |
| regex_compile              | 144 ms                                                       | 224 ms: 1.55x slower                                                        |
| fannkuch                   | 365 ms                                                       | 575 ms: 1.58x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 42.3 ms: 1.59x slower                                                       |
| sympy_expand               | 505 ms                                                       | 811 ms: 1.61x slower                                                        |
| richards_super             | 59.8 ms                                                      | 96.3 ms: 1.61x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 118 ms: 1.62x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 160 ms: 1.64x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 1.37 sec: 1.68x slower                                                      |
| comprehensions             | 17.3 us                                                      | 29.1 us: 1.69x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 260 ms: 1.69x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.81 sec: 1.70x slower                                                      |
| django_template            | 38.9 ms                                                      | 66.4 ms: 1.71x slower                                                       |
| float                      | 81.9 ms                                                      | 142 ms: 1.73x slower                                                        |
| go                         | 160 ms                                                       | 285 ms: 1.78x slower                                                        |
| logging_format             | 7.07 us                                                      | 12.6 us: 1.78x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 11.4 ms: 1.80x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 177 ns: 1.81x slower                                                        |
| logging_simple             | 6.40 us                                                      | 11.6 us: 1.82x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 583 us: 1.83x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 399 us: 1.86x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.35 ms: 1.88x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 1.70 ms: 1.89x slower                                                       |
| scimark_sor                | 126 ms                                                       | 244 ms: 1.94x slower                                                        |
| chaos                      | 61.7 ms                                                      | 122 ms: 1.97x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 133 ms: 2.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 21.4 ms: 2.05x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 2.84 ms: 2.06x slower                                                       |
| raytrace                   | 289 ms                                                       | 596 ms: 2.06x slower                                                        |
| nbody                      | 88.0 ms                                                      | 191 ms: 2.17x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 131 ns: 2.30x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 228 ms: 2.33x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.16 ms: 2.39x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.39x slower                                                                |
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.16x