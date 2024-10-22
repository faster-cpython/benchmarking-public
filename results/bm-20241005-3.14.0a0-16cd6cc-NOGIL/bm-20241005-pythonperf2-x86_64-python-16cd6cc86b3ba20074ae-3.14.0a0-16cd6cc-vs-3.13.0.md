# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.41x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 421 ms: 1.45x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| html5lib       | 71.9 ms                                                      | 105 ms: 1.46x slower                                                        |
| tornado_http   | 120 ms                                                       | 166 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 382 ms                                                       | 377 ms: 1.02x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 475 ms: 1.03x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 882 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 371 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 636 ms: 1.11x slower                                                        |
| async_tree_io              | 847 ms                                                       | 939 ms: 1.11x slower                                                        |
| async_tree_none            | 372 ms                                                       | 422 ms: 1.13x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 681 ms: 1.13x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 519 ms: 1.15x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.83 sec: 1.16x slower                                                      |
| asyncio_tcp                | 380 ms                                                       | 455 ms: 1.20x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 26.9 ms: 1.25x slower                                                       |
| async_generators           | 359 ms                                                       | 479 ms: 1.33x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 141 ms: 1.72x slower                                                        |
| nbody          | 88.0 ms                                                      | 193 ms: 2.19x slower                                                        |
| Geometric mean | (ref)                                                        | 1.55x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 246 ms: 1.01x slower                                                        |
| regex_v8       | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                       |
| regex_compile  | 144 ms                                                       | 223 ms: 1.54x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle               | 10.5 us                                                      | 9.98 us: 1.06x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 138 ms: 1.05x faster                                                        |
| pickle_list          | 4.59 us                                                      | 4.40 us: 1.04x faster                                                       |
| pickle_dict          | 32.1 us                                                      | 30.9 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 108 ms: 1.08x slower                                                        |
| unpickle_list        | 4.62 us                                                      | 5.22 us: 1.13x slower                                                       |
| unpickle             | 15.1 us                                                      | 17.1 us: 1.13x slower                                                       |
| json_loads           | 24.0 us                                                      | 29.5 us: 1.23x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 13.7 ms: 1.25x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 111 ms: 1.30x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.31 sec: 1.38x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 89.3 ms: 1.47x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 579 us: 1.82x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 399 us: 1.86x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.4 ms: 1.31x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 81.0 ms: 1.41x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 42.0 ms: 1.58x slower                                                       |
| django_template | 38.9 ms                                                      | 65.4 ms: 1.68x slower                                                       |
| mako            | 10.4 ms                                                      | 21.3 ms: 2.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.66x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 3.19 ms: 1.29x faster                                                       |
| pickle                     | 10.5 us                                                      | 9.98 us: 1.06x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 138 ms: 1.05x faster                                                        |
| pickle_list                | 4.59 us                                                      | 4.40 us: 1.04x faster                                                       |
| pickle_dict                | 32.1 us                                                      | 30.9 us: 1.04x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.72 ms: 1.03x faster                                                       |
| asyncio_websockets         | 382 ms                                                       | 377 ms: 1.02x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_dna                  | 244 ms                                                       | 246 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 475 ms: 1.03x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                                       |
| deepcopy                   | 397 us                                                       | 423 us: 1.07x slower                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.98 us: 1.07x slower                                                       |
| async_tree_io_tg           | 819 ms                                                       | 882 ms: 1.08x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 108 ms: 1.08x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                       |
| async_tree_none_tg         | 340 ms                                                       | 371 ms: 1.09x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.2 ms: 1.10x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 636 ms: 1.11x slower                                                        |
| async_tree_io              | 847 ms                                                       | 939 ms: 1.11x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 5.22 us: 1.13x slower                                                       |
| unpickle                   | 15.1 us                                                      | 17.1 us: 1.13x slower                                                       |
| async_tree_none            | 372 ms                                                       | 422 ms: 1.13x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 681 ms: 1.13x slower                                                        |
| json                       | 5.22 ms                                                      | 5.94 ms: 1.14x slower                                                       |
| async_tree_memoization     | 452 ms                                                       | 519 ms: 1.15x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.83 sec: 1.16x slower                                                      |
| telco                      | 8.58 ms                                                      | 10.2 ms: 1.19x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 455 ms: 1.20x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| scimark_fft                | 314 ms                                                       | 384 ms: 1.22x slower                                                        |
| json_loads                 | 24.0 us                                                      | 29.5 us: 1.23x slower                                                       |
| pylint                     | 346 ms                                                       | 430 ms: 1.24x slower                                                        |
| deepcopy_memo              | 39.5 us                                                      | 49.0 us: 1.24x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 26.9 ms: 1.25x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 13.7 ms: 1.25x slower                                                       |
| generators                 | 33.5 ms                                                      | 42.1 ms: 1.26x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.19 sec: 1.26x slower                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.48 ms: 1.28x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.52 sec: 1.28x slower                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 4.55 us: 1.29x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 111 ms: 1.30x slower                                                        |
| coverage                   | 81.1 ms                                                      | 105 ms: 1.30x slower                                                        |
| python_startup             | 13.3 ms                                                      | 17.4 ms: 1.31x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| meteor_contest             | 128 ms                                                       | 171 ms: 1.33x slower                                                        |
| async_generators           | 359 ms                                                       | 479 ms: 1.33x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.70 sec: 1.35x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 89.2 ms: 1.36x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 3.31 sec: 1.38x slower                                                      |
| tornado_http               | 120 ms                                                       | 166 ms: 1.39x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 32.4 ms: 1.39x slower                                                       |
| genshi_xml                 | 57.3 ms                                                      | 81.0 ms: 1.41x slower                                                       |
| 2to3                       | 291 ms                                                       | 421 ms: 1.45x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 128 ms: 1.45x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 105 ms: 1.46x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 89.3 ms: 1.47x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 258 us: 1.48x slower                                                        |
| sympy_str                  | 296 ms                                                       | 445 ms: 1.50x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 90.1 ms: 1.51x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 179 ms: 1.51x slower                                                        |
| pyflate                    | 492 ms                                                       | 754 ms: 1.53x slower                                                        |
| thrift                     | 877 us                                                       | 1.34 ms: 1.53x slower                                                       |
| regex_compile              | 144 ms                                                       | 223 ms: 1.54x slower                                                        |
| richards                   | 52.7 ms                                                      | 81.6 ms: 1.55x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 42.0 ms: 1.58x slower                                                       |
| sympy_expand               | 505 ms                                                       | 805 ms: 1.60x slower                                                        |
| fannkuch                   | 365 ms                                                       | 583 ms: 1.60x slower                                                        |
| richards_super             | 59.8 ms                                                      | 97.8 ms: 1.64x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 119 ms: 1.64x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 161 ms: 1.65x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 1.35 sec: 1.66x slower                                                      |
| sympy_sum                  | 154 ms                                                       | 259 ms: 1.68x slower                                                        |
| django_template            | 38.9 ms                                                      | 65.4 ms: 1.68x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.79 sec: 1.69x slower                                                      |
| comprehensions             | 17.3 us                                                      | 29.5 us: 1.71x slower                                                       |
| float                      | 81.9 ms                                                      | 141 ms: 1.72x slower                                                        |
| logging_format             | 7.07 us                                                      | 12.4 us: 1.75x slower                                                       |
| logging_simple             | 6.40 us                                                      | 11.3 us: 1.77x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 11.4 ms: 1.80x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 579 us: 1.82x slower                                                        |
| go                         | 160 ms                                                       | 292 ms: 1.82x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 1.65 ms: 1.83x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 181 ns: 1.86x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 399 us: 1.86x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.34 ms: 1.87x slower                                                       |
| chaos                      | 61.7 ms                                                      | 121 ms: 1.96x slower                                                        |
| scimark_sor                | 126 ms                                                       | 247 ms: 1.97x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 130 ms: 2.00x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.82 ms: 2.04x slower                                                       |
| mako                       | 10.4 ms                                                      | 21.3 ms: 2.04x slower                                                       |
| raytrace                   | 289 ms                                                       | 596 ms: 2.06x slower                                                        |
| nbody                      | 88.0 ms                                                      | 193 ms: 2.19x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 216 ms: 2.21x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.13 ms: 2.38x slower                                                       |
| unpack_sequence            | 56.8 ns                                                      | 136 ns: 2.39x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 34.0 ms: 7.31x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.41x slower                                                                |
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.17x