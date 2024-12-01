# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.010x slower
- HPT reliability: 84.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 297 ms: 1.04x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                         |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 842 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 851 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 201 us: 1.04x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 336 us: 1.06x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.45 ms: 1.06x faster                                                        |
| django_template | 38.2 ms                                                      | 39.9 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                         |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 842 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 851 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                         |
| deepcopy                   | 368 us                                                       | 312 us: 1.18x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.8 us: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                                         |
| richards_super             | 51.3 ms                                                      | 48.3 ms: 1.06x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.45 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 82.2 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 201 us: 1.04x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.2 ms: 1.03x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                        |
| scimark_sor                | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.02x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.0 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.5 ms: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 163 ms: 1.00x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 94.8 ns: 1.00x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 820 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 93.6 ms: 1.02x slower                                                        |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                         |
| sympy_str                  | 302 ms                                                       | 311 ms: 1.03x slower                                                         |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 981 us: 1.03x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 24.7 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                        |
| 2to3                       | 285 ms                                                       | 297 ms: 1.04x slower                                                         |
| generators                 | 37.4 ms                                                      | 39.0 ms: 1.04x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.8 ms: 1.04x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.9 ms: 1.04x slower                                                        |
| go                         | 150 ms                                                       | 158 ms: 1.05x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 336 us: 1.06x slower                                                         |
| float                      | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.91 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.09x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                        |
| raytrace                   | 298 ms                                                       | 326 ms: 1.09x slower                                                         |
| pyflate                    | 439 ms                                                       | 480 ms: 1.09x slower                                                         |
| sympy_expand               | 484 ms                                                       | 531 ms: 1.10x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.65 ms: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 99.8 ms: 1.11x slower                                                        |
| fannkuch                   | 350 ms                                                       | 389 ms: 1.11x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 64.2 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.6 ms: 1.18x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.18 ms: 1.21x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                         |
| async_generators           | 390 ms                                                       | 473 ms: 1.21x slower                                                         |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.26 ms: 1.80x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.09 sec: 228.79x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (6): nbody, tomli_loads, asyncio_websockets, deltablue, dulwich_log, pprint_pformat
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 84.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x