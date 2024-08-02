# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                                                     | 311 ms: 1.07x slower                                                                                                   |
| chameleon      | 7.47 ms                                                                                                    | 7.90 ms: 1.06x slower                                                                                                  |
| docutils       | 2.83 sec                                                                                                   | 2.93 sec: 1.04x slower                                                                                                 |
| tornado_http   | 119 ms                                                                                                     | 124 ms: 1.04x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.05x slower                                                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 1.07 sec                                                                                                   | 1.09 sec: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 706 ms                                                                                                     | 725 ms: 1.03x slower                                                                                                   |
| async_tree_io_tg           | 1.08 sec                                                                                                   | 1.11 sec: 1.03x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 690 ms                                                                                                     | 711 ms: 1.03x slower                                                                                                   |
| async_tree_memoization     | 542 ms                                                                                                     | 561 ms: 1.03x slower                                                                                                   |
| async_tree_none_tg         | 435 ms                                                                                                     | 453 ms: 1.04x slower                                                                                                   |
| async_tree_none            | 429 ms                                                                                                     | 447 ms: 1.04x slower                                                                                                   |
| async_tree_memoization_tg  | 556 ms                                                                                                     | 586 ms: 1.05x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                      | 1.04x slower                                                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                                                                     | 267 ms: 1.01x slower                                                                                                   |
| float          | 80.9 ms                                                                                                    | 92.5 ms: 1.14x slower                                                                                                  |
| nbody          | 83.9 ms                                                                                                    | 112 ms: 1.34x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.16x slower                                                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                                                                    | 3.51 ms: 1.03x faster                                                                                                  |
| regex_v8       | 25.2 ms                                                                                                    | 24.9 ms: 1.01x faster                                                                                                  |
| regex_dna      | 241 ms                                                                                                     | 249 ms: 1.04x slower                                                                                                   |
| regex_compile  | 143 ms                                                                                                     | 172 ms: 1.20x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.04x slower                                                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| pickle_dict          | 32.6 us                                                                                                    | 31.8 us: 1.03x faster                                                                                                  |
| pickle_list          | 4.34 us                                                                                                    | 4.27 us: 1.02x faster                                                                                                  |
| unpickle_list        | 4.62 us                                                                                                    | 4.56 us: 1.01x faster                                                                                                  |
| json_loads           | 25.5 us                                                                                                    | 25.3 us: 1.01x faster                                                                                                  |
| unpickle             | 15.1 us                                                                                                    | 15.2 us: 1.01x slower                                                                                                  |
| pickle_pure_python   | 308 us                                                                                                     | 312 us: 1.01x slower                                                                                                   |
| json_dumps           | 10.5 ms                                                                                                    | 10.7 ms: 1.02x slower                                                                                                  |
| unpickle_pure_python | 225 us                                                                                                     | 231 us: 1.03x slower                                                                                                   |
| xml_etree_parse      | 151 ms                                                                                                     | 157 ms: 1.04x slower                                                                                                   |
| xml_etree_process    | 57.6 ms                                                                                                    | 60.9 ms: 1.06x slower                                                                                                  |
| xml_etree_generate   | 84.0 ms                                                                                                    | 90.1 ms: 1.07x slower                                                                                                  |
| xml_etree_iterparse  | 108 ms                                                                                                     | 117 ms: 1.09x slower                                                                                                   |
| tomli_loads          | 2.16 sec                                                                                                   | 2.61 sec: 1.21x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                      | 1.03x slower                                                                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                                                    | 12.9 ms: 1.00x slower                                                                                                  |
| python_startup_no_site | 11.3 ms                                                                                                    | 11.3 ms: 1.00x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                      | 1.00x slower                                                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                                                                    | 13.6 ms: 1.35x slower                                                                                                  |

All benchmarks:
===============

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 3.94 ms                                                                                                    | 3.76 ms: 1.05x faster                                                                                                  |
| regex_effbot               | 3.63 ms                                                                                                    | 3.51 ms: 1.03x faster                                                                                                  |
| pickle_dict                | 32.6 us                                                                                                    | 31.8 us: 1.03x faster                                                                                                  |
| pickle_list                | 4.34 us                                                                                                    | 4.27 us: 1.02x faster                                                                                                  |
| unpickle_list              | 4.62 us                                                                                                    | 4.56 us: 1.01x faster                                                                                                  |
| regex_v8                   | 25.2 ms                                                                                                    | 24.9 ms: 1.01x faster                                                                                                  |
| richards                   | 52.1 ms                                                                                                    | 51.6 ms: 1.01x faster                                                                                                  |
| json_loads                 | 25.5 us                                                                                                    | 25.3 us: 1.01x faster                                                                                                  |
| coverage                   | 79.1 ms                                                                                                    | 78.8 ms: 1.00x faster                                                                                                  |
| python_startup             | 12.9 ms                                                                                                    | 12.9 ms: 1.00x slower                                                                                                  |
| python_startup_no_site     | 11.3 ms                                                                                                    | 11.3 ms: 1.00x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.57 sec                                                                                                   | 1.59 sec: 1.01x slower                                                                                                 |
| unpickle                   | 15.1 us                                                                                                    | 15.2 us: 1.01x slower                                                                                                  |
| asyncio_websockets         | 384 ms                                                                                                     | 387 ms: 1.01x slower                                                                                                   |
| pidigits                   | 265 ms                                                                                                     | 267 ms: 1.01x slower                                                                                                   |
| pathlib                    | 19.1 ms                                                                                                    | 19.3 ms: 1.01x slower                                                                                                  |
| asyncio_tcp                | 368 ms                                                                                                     | 373 ms: 1.01x slower                                                                                                   |
| pickle_pure_python         | 308 us                                                                                                     | 312 us: 1.01x slower                                                                                                   |
| deepcopy                   | 362 us                                                                                                     | 366 us: 1.01x slower                                                                                                   |
| json_dumps                 | 10.5 ms                                                                                                    | 10.7 ms: 1.02x slower                                                                                                  |
| pycparser                  | 1.31 sec                                                                                                   | 1.33 sec: 1.02x slower                                                                                                 |
| scimark_sor                | 146 ms                                                                                                     | 149 ms: 1.02x slower                                                                                                   |
| coroutines                 | 22.2 ms                                                                                                    | 22.6 ms: 1.02x slower                                                                                                  |
| mdp                        | 2.59 sec                                                                                                   | 2.63 sec: 1.02x slower                                                                                                 |
| json                       | 5.20 ms                                                                                                    | 5.30 ms: 1.02x slower                                                                                                  |
| async_generators           | 370 ms                                                                                                     | 377 ms: 1.02x slower                                                                                                   |
| generators                 | 34.2 ms                                                                                                    | 35.0 ms: 1.02x slower                                                                                                  |
| logging_silent             | 96.5 ns                                                                                                    | 98.7 ns: 1.02x slower                                                                                                  |
| deepcopy_reduce            | 3.27 us                                                                                                    | 3.35 us: 1.02x slower                                                                                                  |
| async_tree_io              | 1.07 sec                                                                                                   | 1.09 sec: 1.02x slower                                                                                                 |
| unpickle_pure_python       | 225 us                                                                                                     | 231 us: 1.03x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 706 ms                                                                                                     | 725 ms: 1.03x slower                                                                                                   |
| deepcopy_memo              | 37.6 us                                                                                                    | 38.6 us: 1.03x slower                                                                                                  |
| async_tree_io_tg           | 1.08 sec                                                                                                   | 1.11 sec: 1.03x slower                                                                                                 |
| logging_format             | 7.20 us                                                                                                    | 7.40 us: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 690 ms                                                                                                     | 711 ms: 1.03x slower                                                                                                   |
| sqlite_synth               | 2.74 us                                                                                                    | 2.83 us: 1.03x slower                                                                                                  |
| async_tree_memoization     | 542 ms                                                                                                     | 561 ms: 1.03x slower                                                                                                   |
| go                         | 173 ms                                                                                                     | 179 ms: 1.04x slower                                                                                                   |
| bench_thread_pool          | 951 us                                                                                                     | 985 us: 1.04x slower                                                                                                   |
| regex_dna                  | 241 ms                                                                                                     | 249 ms: 1.04x slower                                                                                                   |
| telco                      | 8.17 ms                                                                                                    | 8.47 ms: 1.04x slower                                                                                                  |
| docutils                   | 2.83 sec                                                                                                   | 2.93 sec: 1.04x slower                                                                                                 |
| create_gc_cycles           | 1.55 ms                                                                                                    | 1.61 ms: 1.04x slower                                                                                                  |
| async_tree_none_tg         | 435 ms                                                                                                     | 453 ms: 1.04x slower                                                                                                   |
| tornado_http               | 119 ms                                                                                                     | 124 ms: 1.04x slower                                                                                                   |
| xml_etree_parse            | 151 ms                                                                                                     | 157 ms: 1.04x slower                                                                                                   |
| async_tree_none            | 429 ms                                                                                                     | 447 ms: 1.04x slower                                                                                                   |
| bench_mp_pool              | 4.54 ms                                                                                                    | 4.75 ms: 1.05x slower                                                                                                  |
| async_tree_memoization_tg  | 556 ms                                                                                                     | 586 ms: 1.05x slower                                                                                                   |
| sqlglot_transpile          | 1.80 ms                                                                                                    | 1.90 ms: 1.05x slower                                                                                                  |
| logging_simple             | 6.44 us                                                                                                    | 6.80 us: 1.06x slower                                                                                                  |
| chameleon                  | 7.47 ms                                                                                                    | 7.90 ms: 1.06x slower                                                                                                  |
| xml_etree_process          | 57.6 ms                                                                                                    | 60.9 ms: 1.06x slower                                                                                                  |
| typing_runtime_protocols   | 126 us                                                                                                     | 133 us: 1.06x slower                                                                                                   |
| scimark_lu                 | 98.6 ms                                                                                                    | 105 ms: 1.06x slower                                                                                                   |
| sqlglot_parse              | 1.39 ms                                                                                                    | 1.49 ms: 1.07x slower                                                                                                  |
| 2to3                       | 292 ms                                                                                                     | 311 ms: 1.07x slower                                                                                                   |
| xml_etree_generate         | 84.0 ms                                                                                                    | 90.1 ms: 1.07x slower                                                                                                  |
| sqlglot_normalize          | 115 ms                                                                                                     | 124 ms: 1.07x slower                                                                                                   |
| dulwich_log                | 66.9 ms                                                                                                    | 72.0 ms: 1.08x slower                                                                                                  |
| meteor_contest             | 127 ms                                                                                                     | 137 ms: 1.08x slower                                                                                                   |
| sympy_integrate            | 23.0 ms                                                                                                    | 24.9 ms: 1.08x slower                                                                                                  |
| pyflate                    | 513 ms                                                                                                     | 557 ms: 1.08x slower                                                                                                   |
| sqlglot_optimize           | 58.1 ms                                                                                                    | 63.2 ms: 1.09x slower                                                                                                  |
| xml_etree_iterparse        | 108 ms                                                                                                     | 117 ms: 1.09x slower                                                                                                   |
| sympy_expand               | 488 ms                                                                                                     | 535 ms: 1.10x slower                                                                                                   |
| raytrace                   | 271 ms                                                                                                     | 299 ms: 1.10x slower                                                                                                   |
| sympy_sum                  | 150 ms                                                                                                     | 167 ms: 1.11x slower                                                                                                   |
| pprint_safe_repr           | 792 ms                                                                                                     | 880 ms: 1.11x slower                                                                                                   |
| sympy_str                  | 289 ms                                                                                                     | 322 ms: 1.12x slower                                                                                                   |
| pprint_pformat             | 1.62 sec                                                                                                   | 1.81 sec: 1.12x slower                                                                                                 |
| crypto_pyaes               | 71.7 ms                                                                                                    | 80.6 ms: 1.12x slower                                                                                                  |
| float                      | 80.9 ms                                                                                                    | 92.5 ms: 1.14x slower                                                                                                  |
| nqueens                    | 89.5 ms                                                                                                    | 105 ms: 1.17x slower                                                                                                   |
| chaos                      | 61.9 ms                                                                                                    | 73.3 ms: 1.18x slower                                                                                                  |
| regex_compile              | 143 ms                                                                                                     | 172 ms: 1.20x slower                                                                                                   |
| tomli_loads                | 2.16 sec                                                                                                   | 2.61 sec: 1.21x slower                                                                                                 |
| fannkuch                   | 374 ms                                                                                                     | 453 ms: 1.21x slower                                                                                                   |
| scimark_monte_carlo        | 67.9 ms                                                                                                    | 87.4 ms: 1.29x slower                                                                                                  |
| nbody                      | 83.9 ms                                                                                                    | 112 ms: 1.34x slower                                                                                                   |
| scimark_fft                | 301 ms                                                                                                     | 407 ms: 1.35x slower                                                                                                   |
| mako                       | 10.1 ms                                                                                                    | 13.6 ms: 1.35x slower                                                                                                  |
| deltablue                  | 3.61 ms                                                                                                    | 4.98 ms: 1.38x slower                                                                                                  |
| comprehensions             | 16.6 us                                                                                                    | 23.3 us: 1.40x slower                                                                                                  |
| hexiom                     | 6.35 ms                                                                                                    | 9.10 ms: 1.43x slower                                                                                                  |
| scimark_sparse_mat_mult    | 4.19 ms                                                                                                    | 6.01 ms: 1.44x slower                                                                                                  |
| spectral_norm              | 92.3 ms                                                                                                    | 144 ms: 1.56x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                      | 1.08x slower                                                                                                           |

Benchmark hidden because not significant (3): pickle, richards_super, mypy2
Ignored benchmarks (9) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x