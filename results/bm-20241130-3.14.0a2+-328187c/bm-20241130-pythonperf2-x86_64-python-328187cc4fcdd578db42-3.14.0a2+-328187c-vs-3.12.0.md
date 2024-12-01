# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.002x faster
- HPT reliability: 61.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.39x faster                                                         |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 839 ms: 1.25x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 840 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 82.9 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 336 us: 1.06x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                 |

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
| django_template | 38.2 ms                                                      | 37.8 ms: 1.01x faster                                                        |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.39x faster                                                         |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 839 ms: 1.25x faster                                                         |
| deepcopy                   | 368 us                                                       | 294 us: 1.25x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 840 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.4 ms: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.10x faster                                                        |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.2 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.24 us: 1.03x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.2 ms: 1.03x faster                                                        |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 930 us: 1.02x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 96.9 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.8 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.02x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 91.7 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.04x slower                                                         |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.9 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 315 ms: 1.05x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.5 ms: 1.05x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.28 ms: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 336 us: 1.06x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| float                      | 76.6 ms                                                      | 82.9 ms: 1.08x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 100 ms: 1.09x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.54 ms: 1.09x slower                                                        |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.10x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| richards                   | 45.7 ms                                                      | 51.8 ms: 1.13x slower                                                        |
| richards_super             | 51.3 ms                                                      | 58.2 ms: 1.13x slower                                                        |
| pyflate                    | 439 ms                                                       | 499 ms: 1.14x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.79 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                         |
| async_generators           | 390 ms                                                       | 452 ms: 1.16x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.12 ms: 1.17x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 78.5 ms: 1.18x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.20 ms: 1.78x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.95 ms: 1.85x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.40 sec: 293.13x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                 |

Benchmark hidden because not significant (2): regex_dna, nbody
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 61.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x