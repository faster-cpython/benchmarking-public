# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                     | 308 ms: 1.05x slower                                                                                                   |
| chameleon      | 7.26 ms                                                                                                    | 7.89 ms: 1.09x slower                                                                                                  |
| docutils       | 2.83 sec                                                                                                   | 2.94 sec: 1.04x slower                                                                                                 |
| tornado_http   | 118 ms                                                                                                     | 123 ms: 1.05x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.06x slower                                                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 701 ms                                                                                                     | 710 ms: 1.01x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 701 ms                                                                                                     | 713 ms: 1.02x slower                                                                                                   |
| async_tree_io              | 1.08 sec                                                                                                   | 1.10 sec: 1.02x slower                                                                                                 |
| async_tree_io_tg           | 1.07 sec                                                                                                   | 1.09 sec: 1.02x slower                                                                                                 |
| async_tree_memoization     | 547 ms                                                                                                     | 558 ms: 1.02x slower                                                                                                   |
| async_tree_none            | 435 ms                                                                                                     | 446 ms: 1.02x slower                                                                                                   |
| async_tree_none_tg         | 430 ms                                                                                                     | 442 ms: 1.03x slower                                                                                                   |
| async_tree_memoization_tg  | 545 ms                                                                                                     | 570 ms: 1.04x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                      | 1.02x slower                                                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 263 ms                                                                                                     | 265 ms: 1.01x slower                                                                                                   |
| float          | 78.0 ms                                                                                                    | 103 ms: 1.32x slower                                                                                                   |
| nbody          | 85.3 ms                                                                                                    | 125 ms: 1.47x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.25x slower                                                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                                                                    | 3.43 ms: 1.02x faster                                                                                                  |
| regex_dna      | 238 ms                                                                                                     | 240 ms: 1.01x slower                                                                                                   |
| regex_v8       | 26.0 ms                                                                                                    | 26.4 ms: 1.02x slower                                                                                                  |
| regex_compile  | 141 ms                                                                                                     | 170 ms: 1.21x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.05x slower                                                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                                                                    | 30.7 us: 1.06x faster                                                                                                  |
| pickle_list          | 4.49 us                                                                                                    | 4.32 us: 1.04x faster                                                                                                  |
| xml_etree_parse      | 150 ms                                                                                                     | 146 ms: 1.03x faster                                                                                                   |
| unpickle             | 15.4 us                                                                                                    | 15.1 us: 1.02x faster                                                                                                  |
| unpickle_list        | 4.82 us                                                                                                    | 4.74 us: 1.02x faster                                                                                                  |
| json_loads           | 25.0 us                                                                                                    | 25.1 us: 1.00x slower                                                                                                  |
| pickle_pure_python   | 307 us                                                                                                     | 311 us: 1.01x slower                                                                                                   |
| json_dumps           | 10.6 ms                                                                                                    | 10.8 ms: 1.03x slower                                                                                                  |
| xml_etree_process    | 58.7 ms                                                                                                    | 62.3 ms: 1.06x slower                                                                                                  |
| xml_etree_generate   | 85.6 ms                                                                                                    | 90.9 ms: 1.06x slower                                                                                                  |
| xml_etree_iterparse  | 107 ms                                                                                                     | 117 ms: 1.10x slower                                                                                                   |
| unpickle_pure_python | 213 us                                                                                                     | 245 us: 1.15x slower                                                                                                   |
| tomli_loads          | 2.23 sec                                                                                                   | 2.82 sec: 1.27x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                      | 1.03x slower                                                                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                                    | 12.5 ms: 1.00x faster                                                                                                  |
| python_startup_no_site | 11.0 ms                                                                                                    | 11.0 ms: 1.00x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                      | 1.00x faster                                                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| mako      | 10.3 ms                                                                                                    | 14.8 ms: 1.43x slower                                                                                                  |

All benchmarks:
===============

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| pickle_dict                | 32.5 us                                                                                                    | 30.7 us: 1.06x faster                                                                                                  |
| gc_traversal               | 3.94 ms                                                                                                    | 3.74 ms: 1.05x faster                                                                                                  |
| pickle_list                | 4.49 us                                                                                                    | 4.32 us: 1.04x faster                                                                                                  |
| xml_etree_parse            | 150 ms                                                                                                     | 146 ms: 1.03x faster                                                                                                   |
| unpickle                   | 15.4 us                                                                                                    | 15.1 us: 1.02x faster                                                                                                  |
| regex_effbot               | 3.50 ms                                                                                                    | 3.43 ms: 1.02x faster                                                                                                  |
| unpickle_list              | 4.82 us                                                                                                    | 4.74 us: 1.02x faster                                                                                                  |
| asyncio_websockets         | 395 ms                                                                                                     | 389 ms: 1.01x faster                                                                                                   |
| coverage                   | 82.9 ms                                                                                                    | 81.8 ms: 1.01x faster                                                                                                  |
| python_startup             | 12.6 ms                                                                                                    | 12.5 ms: 1.00x faster                                                                                                  |
| python_startup_no_site     | 11.0 ms                                                                                                    | 11.0 ms: 1.00x slower                                                                                                  |
| json_loads                 | 25.0 us                                                                                                    | 25.1 us: 1.00x slower                                                                                                  |
| pidigits                   | 263 ms                                                                                                     | 265 ms: 1.01x slower                                                                                                   |
| asyncio_tcp_ssl            | 1.57 sec                                                                                                   | 1.59 sec: 1.01x slower                                                                                                 |
| coroutines                 | 22.3 ms                                                                                                    | 22.5 ms: 1.01x slower                                                                                                  |
| logging_format             | 7.31 us                                                                                                    | 7.38 us: 1.01x slower                                                                                                  |
| regex_dna                  | 238 ms                                                                                                     | 240 ms: 1.01x slower                                                                                                   |
| richards_super             | 59.4 ms                                                                                                    | 60.0 ms: 1.01x slower                                                                                                  |
| sqlite_synth               | 2.77 us                                                                                                    | 2.80 us: 1.01x slower                                                                                                  |
| asyncio_tcp                | 371 ms                                                                                                     | 375 ms: 1.01x slower                                                                                                   |
| pathlib                    | 18.9 ms                                                                                                    | 19.1 ms: 1.01x slower                                                                                                  |
| async_generators           | 368 ms                                                                                                     | 372 ms: 1.01x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 701 ms                                                                                                     | 710 ms: 1.01x slower                                                                                                   |
| pickle_pure_python         | 307 us                                                                                                     | 311 us: 1.01x slower                                                                                                   |
| create_gc_cycles           | 1.57 ms                                                                                                    | 1.59 ms: 1.01x slower                                                                                                  |
| regex_v8                   | 26.0 ms                                                                                                    | 26.4 ms: 1.02x slower                                                                                                  |
| generators                 | 33.8 ms                                                                                                    | 34.3 ms: 1.02x slower                                                                                                  |
| json                       | 5.27 ms                                                                                                    | 5.35 ms: 1.02x slower                                                                                                  |
| richards                   | 53.7 ms                                                                                                    | 54.5 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 701 ms                                                                                                     | 713 ms: 1.02x slower                                                                                                   |
| async_tree_io              | 1.08 sec                                                                                                   | 1.10 sec: 1.02x slower                                                                                                 |
| scimark_sor                | 144 ms                                                                                                     | 147 ms: 1.02x slower                                                                                                   |
| async_tree_io_tg           | 1.07 sec                                                                                                   | 1.09 sec: 1.02x slower                                                                                                 |
| async_tree_memoization     | 547 ms                                                                                                     | 558 ms: 1.02x slower                                                                                                   |
| async_tree_none            | 435 ms                                                                                                     | 446 ms: 1.02x slower                                                                                                   |
| async_tree_none_tg         | 430 ms                                                                                                     | 442 ms: 1.03x slower                                                                                                   |
| json_dumps                 | 10.6 ms                                                                                                    | 10.8 ms: 1.03x slower                                                                                                  |
| logging_silent             | 96.0 ns                                                                                                    | 98.9 ns: 1.03x slower                                                                                                  |
| logging_simple             | 6.66 us                                                                                                    | 6.88 us: 1.03x slower                                                                                                  |
| deepcopy                   | 367 us                                                                                                     | 379 us: 1.03x slower                                                                                                   |
| pycparser                  | 1.32 sec                                                                                                   | 1.36 sec: 1.03x slower                                                                                                 |
| bench_mp_pool              | 4.57 ms                                                                                                    | 4.73 ms: 1.04x slower                                                                                                  |
| deepcopy_reduce            | 3.28 us                                                                                                    | 3.41 us: 1.04x slower                                                                                                  |
| docutils                   | 2.83 sec                                                                                                   | 2.94 sec: 1.04x slower                                                                                                 |
| async_tree_memoization_tg  | 545 ms                                                                                                     | 570 ms: 1.04x slower                                                                                                   |
| sqlglot_parse              | 1.39 ms                                                                                                    | 1.45 ms: 1.04x slower                                                                                                  |
| sqlglot_transpile          | 1.79 ms                                                                                                    | 1.87 ms: 1.05x slower                                                                                                  |
| 2to3                       | 294 ms                                                                                                     | 308 ms: 1.05x slower                                                                                                   |
| tornado_http               | 118 ms                                                                                                     | 123 ms: 1.05x slower                                                                                                   |
| mdp                        | 2.50 sec                                                                                                   | 2.64 sec: 1.05x slower                                                                                                 |
| dulwich_log                | 68.2 ms                                                                                                    | 72.1 ms: 1.06x slower                                                                                                  |
| xml_etree_process          | 58.7 ms                                                                                                    | 62.3 ms: 1.06x slower                                                                                                  |
| xml_etree_generate         | 85.6 ms                                                                                                    | 90.9 ms: 1.06x slower                                                                                                  |
| sympy_integrate            | 23.3 ms                                                                                                    | 24.8 ms: 1.06x slower                                                                                                  |
| scimark_lu                 | 97.8 ms                                                                                                    | 104 ms: 1.07x slower                                                                                                   |
| meteor_contest             | 130 ms                                                                                                     | 139 ms: 1.07x slower                                                                                                   |
| sqlglot_normalize          | 116 ms                                                                                                     | 124 ms: 1.07x slower                                                                                                   |
| sqlglot_optimize           | 59.0 ms                                                                                                    | 63.6 ms: 1.08x slower                                                                                                  |
| sympy_expand               | 494 ms                                                                                                     | 534 ms: 1.08x slower                                                                                                   |
| sympy_sum                  | 154 ms                                                                                                     | 166 ms: 1.08x slower                                                                                                   |
| go                         | 166 ms                                                                                                     | 180 ms: 1.09x slower                                                                                                   |
| deepcopy_memo              | 37.1 us                                                                                                    | 40.3 us: 1.09x slower                                                                                                  |
| chameleon                  | 7.26 ms                                                                                                    | 7.89 ms: 1.09x slower                                                                                                  |
| typing_runtime_protocols   | 113 us                                                                                                     | 124 us: 1.10x slower                                                                                                   |
| sympy_str                  | 294 ms                                                                                                     | 322 ms: 1.10x slower                                                                                                   |
| xml_etree_iterparse        | 107 ms                                                                                                     | 117 ms: 1.10x slower                                                                                                   |
| pprint_safe_repr           | 813 ms                                                                                                     | 921 ms: 1.13x slower                                                                                                   |
| pprint_pformat             | 1.66 sec                                                                                                   | 1.90 sec: 1.15x slower                                                                                                 |
| raytrace                   | 265 ms                                                                                                     | 305 ms: 1.15x slower                                                                                                   |
| unpickle_pure_python       | 213 us                                                                                                     | 245 us: 1.15x slower                                                                                                   |
| pyflate                    | 501 ms                                                                                                     | 582 ms: 1.16x slower                                                                                                   |
| nqueens                    | 89.1 ms                                                                                                    | 108 ms: 1.21x slower                                                                                                   |
| regex_compile              | 141 ms                                                                                                     | 170 ms: 1.21x slower                                                                                                   |
| crypto_pyaes               | 71.4 ms                                                                                                    | 86.6 ms: 1.21x slower                                                                                                  |
| fannkuch                   | 386 ms                                                                                                     | 481 ms: 1.24x slower                                                                                                   |
| tomli_loads                | 2.23 sec                                                                                                   | 2.82 sec: 1.27x slower                                                                                                 |
| chaos                      | 59.9 ms                                                                                                    | 77.4 ms: 1.29x slower                                                                                                  |
| scimark_monte_carlo        | 67.9 ms                                                                                                    | 88.7 ms: 1.31x slower                                                                                                  |
| float                      | 78.0 ms                                                                                                    | 103 ms: 1.32x slower                                                                                                   |
| scimark_fft                | 302 ms                                                                                                     | 429 ms: 1.42x slower                                                                                                   |
| mako                       | 10.3 ms                                                                                                    | 14.8 ms: 1.43x slower                                                                                                  |
| nbody                      | 85.3 ms                                                                                                    | 125 ms: 1.47x slower                                                                                                   |
| comprehensions             | 16.5 us                                                                                                    | 25.0 us: 1.51x slower                                                                                                  |
| hexiom                     | 6.46 ms                                                                                                    | 9.82 ms: 1.52x slower                                                                                                  |
| deltablue                  | 3.54 ms                                                                                                    | 5.40 ms: 1.53x slower                                                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                                                                    | 6.49 ms: 1.54x slower                                                                                                  |
| spectral_norm              | 92.3 ms                                                                                                    | 161 ms: 1.74x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                      | 1.09x slower                                                                                                           |

Benchmark hidden because not significant (4): pickle, telco, bench_thread_pool, mypy2
Ignored benchmarks (9) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x