# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.251x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 401 ms: 1.40x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.27x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 369 ms: 1.17x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 902 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 468 ms: 1.15x faster                                                         |
| async_tree_none            | 452 ms                                                       | 400 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 629 ms: 1.11x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 500 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 666 ms: 1.05x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| nbody          | 88.0 ms                                                      | 141 ms: 1.61x slower                                                         |
| float          | 76.6 ms                                                      | 133 ms: 1.74x slower                                                         |
| Geometric mean | (ref)                                                        | 1.38x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 27.7 ms: 1.17x slower                                                        |
| regex_compile  | 144 ms                                                       | 198 ms: 1.37x slower                                                         |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| json_loads           | 24.4 us                                                      | 27.9 us: 1.15x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 104 ms: 1.21x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.98 sec: 1.38x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 83.5 ms: 1.43x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.8 ms: 1.45x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 348 us: 1.66x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 538 us: 1.69x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.30x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.2 ms: 1.41x slower                                                        |
| python_startup         | 11.6 ms                                                      | 20.0 ms: 1.72x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.56x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 55.9 ms: 1.46x slower                                                        |
| mako            | 10.0 ms                                                      | 21.0 ms: 2.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.76x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 369 ms: 1.17x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 902 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 468 ms: 1.15x faster                                                         |
| async_tree_none            | 452 ms                                                       | 400 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 629 ms: 1.11x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 500 ms: 1.09x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                        |
| pidigits                   | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 666 ms: 1.05x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 18.3 ms: 1.03x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                         |
| deepcopy                   | 368 us                                                       | 371 us: 1.01x slower                                                         |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.88 us: 1.04x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 25.2 ms: 1.10x slower                                                        |
| generators                 | 37.4 ms                                                      | 41.1 ms: 1.10x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.82 ms: 1.10x slower                                                        |
| json                       | 5.12 ms                                                      | 5.74 ms: 1.12x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.27 sec: 1.14x slower                                                       |
| json_loads                 | 24.4 us                                                      | 27.9 us: 1.15x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 42.6 us: 1.16x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.7 ms: 1.17x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.03 sec: 1.18x slower                                                       |
| scimark_fft                | 301 ms                                                       | 362 ms: 1.20x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 4.06 us: 1.20x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 104 ms: 1.21x slower                                                         |
| meteor_contest             | 128 ms                                                       | 159 ms: 1.24x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 117 ms: 1.27x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 24.1 ms: 1.28x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 30.9 ms: 1.29x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 86.1 ms: 1.32x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 119 ms: 1.33x slower                                                         |
| comprehensions             | 21.9 us                                                      | 29.2 us: 1.33x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.65 sec: 1.33x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 108 ms: 1.34x slower                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 217 ms: 1.36x slower                                                         |
| sympy_str                  | 302 ms                                                       | 414 ms: 1.37x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 78.8 ms: 1.37x slower                                                        |
| regex_compile              | 144 ms                                                       | 198 ms: 1.37x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 159 ms: 1.38x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.80 ms: 1.38x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.98 sec: 1.38x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.63 ms: 1.38x slower                                                        |
| 2to3                       | 285 ms                                                       | 401 ms: 1.40x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 12.2 ms: 1.41x slower                                                        |
| async_generators           | 390 ms                                                       | 556 ms: 1.42x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 1.15 sec: 1.43x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 83.5 ms: 1.43x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.39 sec: 1.45x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.8 ms: 1.45x slower                                                        |
| django_template            | 38.2 ms                                                      | 55.9 ms: 1.46x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 247 ms: 1.52x slower                                                         |
| logging_format             | 7.48 us                                                      | 11.5 us: 1.54x slower                                                        |
| fannkuch                   | 350 ms                                                       | 538 ms: 1.54x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 234 us: 1.55x slower                                                         |
| sympy_expand               | 484 ms                                                       | 758 ms: 1.57x slower                                                         |
| logging_simple             | 6.71 us                                                      | 10.5 us: 1.57x slower                                                        |
| coverage                   | 66.7 ms                                                      | 105 ms: 1.57x slower                                                         |
| nbody                      | 88.0 ms                                                      | 141 ms: 1.61x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.55 ms: 1.64x slower                                                        |
| pyflate                    | 439 ms                                                       | 728 ms: 1.66x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 348 us: 1.66x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 538 us: 1.69x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 2.71 ms: 1.70x slower                                                        |
| python_startup             | 11.6 ms                                                      | 20.0 ms: 1.72x slower                                                        |
| richards                   | 45.7 ms                                                      | 79.3 ms: 1.73x slower                                                        |
| float                      | 76.6 ms                                                      | 133 ms: 1.74x slower                                                         |
| chaos                      | 64.0 ms                                                      | 111 ms: 1.74x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 174 ms: 1.76x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 124 ms: 1.79x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 3.18 ms: 1.79x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 10.7 ms: 1.80x slower                                                        |
| richards_super             | 51.3 ms                                                      | 92.7 ms: 1.81x slower                                                        |
| go                         | 150 ms                                                       | 276 ms: 1.84x slower                                                         |
| raytrace                   | 298 ms                                                       | 565 ms: 1.90x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 181 ns: 1.91x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 2.66 ms: 1.93x slower                                                        |
| scimark_sor                | 109 ms                                                       | 229 ms: 2.10x slower                                                         |
| mako                       | 10.0 ms                                                      | 21.0 ms: 2.10x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 7.92 ms: 2.45x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 54.6 ms: 11.46x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.38x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.251x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.27x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: 1.24x