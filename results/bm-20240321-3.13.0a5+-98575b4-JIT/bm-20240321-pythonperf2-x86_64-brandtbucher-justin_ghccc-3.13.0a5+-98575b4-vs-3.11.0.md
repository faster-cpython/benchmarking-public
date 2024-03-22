# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.18x slower
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 331 ms: 1.15x slower                                                       |
| chameleon      | 7.92 ms                                                      | 7.32 ms: 1.08x faster                                                      |
| docutils       | 2.85 sec                                                     | 4.68 sec: 1.64x slower                                                     |
| html5lib       | 72.2 ms                                                      | 81.5 ms: 1.13x slower                                                      |
| tornado_http   | 124 ms                                                       | 128 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 753 ms                                                       | 3.26 sec: 4.33x slower                                                     |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 3.43 sec: 4.57x slower                                                     |
| async_tree_none            | 518 ms                                                       | 2.68 sec: 5.18x slower                                                     |
| async_tree_memoization     | 629 ms                                                       | 3.39 sec: 5.38x slower                                                     |
| async_tree_memoization_tg  | 600 ms                                                       | 3.49 sec: 5.82x slower                                                     |
| async_tree_none_tg         | 474 ms                                                       | 2.83 sec: 5.96x slower                                                     |
| async_tree_io              | 1.17 sec                                                     | 9.59 sec: 8.19x slower                                                     |
| async_tree_io_tg           | 1.15 sec                                                     | 10.1 sec: 8.73x slower                                                     |
| Geometric mean             | (ref)                                                        | 5.85x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                      | 83.6 ms: 1.11x faster                                                      |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                       |
| float          | 74.9 ms                                                      | 149 ms: 1.98x slower                                                       |
| Geometric mean | (ref)                                                        | 1.23x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 144 ms: 1.08x faster                                                       |
| regex_effbot   | 3.34 ms                                                      | 3.48 ms: 1.04x slower                                                      |
| regex_v8       | 24.4 ms                                                      | 25.8 ms: 1.06x slower                                                      |
| regex_dna      | 227 ms                                                       | 247 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.7 ms: 1.24x faster                                                      |
| json_loads           | 28.9 us                                                      | 24.9 us: 1.16x faster                                                      |
| tomli_loads          | 2.25 sec                                                     | 2.08 sec: 1.08x faster                                                     |
| unpickle_pure_python | 238 us                                                       | 226 us: 1.06x faster                                                       |
| pickle_pure_python   | 316 us                                                       | 313 us: 1.01x faster                                                       |
| pickle_dict          | 32.3 us                                                      | 33.6 us: 1.04x slower                                                      |
| pickle               | 9.89 us                                                      | 10.9 us: 1.10x slower                                                      |
| unpickle             | 13.3 us                                                      | 15.3 us: 1.15x slower                                                      |
| pickle_list          | 3.94 us                                                      | 4.55 us: 1.16x slower                                                      |
| xml_etree_process    | 55.9 ms                                                      | 68.4 ms: 1.22x slower                                                      |
| xml_etree_generate   | 79.7 ms                                                      | 98.6 ms: 1.24x slower                                                      |
| xml_etree_parse      | 155 ms                                                       | 202 ms: 1.31x slower                                                       |
| xml_etree_iterparse  | 107 ms                                                       | 162 ms: 1.52x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 14.5 ms: 1.35x slower                                                      |
| python_startup_no_site | 7.73 ms                                                      | 12.6 ms: 1.62x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.30 ms: 1.18x faster                                                      |
| django_template | 39.3 ms                                                      | 39.8 ms: 1.01x slower                                                      |
| genshi_text     | 25.5 ms                                                      | 29.1 ms: 1.14x slower                                                      |
| genshi_xml      | 57.1 ms                                                      | 68.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 119 us: 4.46x faster                                                       |
| asyncio_tcp                | 747 ms                                                       | 368 ms: 2.03x faster                                                       |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.94x faster                                                     |
| generators                 | 54.6 ms                                                      | 33.0 ms: 1.66x faster                                                      |
| comprehensions             | 25.1 us                                                      | 18.8 us: 1.33x faster                                                      |
| json_dumps                 | 13.3 ms                                                      | 10.7 ms: 1.24x faster                                                      |
| coroutines                 | 27.8 ms                                                      | 22.4 ms: 1.24x faster                                                      |
| mako                       | 11.0 ms                                                      | 9.30 ms: 1.18x faster                                                      |
| chaos                      | 74.9 ms                                                      | 63.4 ms: 1.18x faster                                                      |
| sympy_sum                  | 186 ms                                                       | 160 ms: 1.16x faster                                                       |
| json_loads                 | 28.9 us                                                      | 24.9 us: 1.16x faster                                                      |
| fannkuch                   | 416 ms                                                       | 359 ms: 1.16x faster                                                       |
| crypto_pyaes               | 83.3 ms                                                      | 72.2 ms: 1.15x faster                                                      |
| spectral_norm              | 95.1 ms                                                      | 82.8 ms: 1.15x faster                                                      |
| sympy_str                  | 337 ms                                                       | 303 ms: 1.11x faster                                                       |
| nbody                      | 92.9 ms                                                      | 83.6 ms: 1.11x faster                                                      |
| richards_super             | 63.6 ms                                                      | 57.9 ms: 1.10x faster                                                      |
| logging_simple             | 7.24 us                                                      | 6.60 us: 1.10x faster                                                      |
| regex_compile              | 156 ms                                                       | 144 ms: 1.08x faster                                                       |
| chameleon                  | 7.92 ms                                                      | 7.32 ms: 1.08x faster                                                      |
| tomli_loads                | 2.25 sec                                                     | 2.08 sec: 1.08x faster                                                     |
| bench_thread_pool          | 1.00 ms                                                      | 938 us: 1.07x faster                                                       |
| sympy_expand               | 553 ms                                                       | 521 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 238 us                                                       | 226 us: 1.06x faster                                                       |
| logging_format             | 7.71 us                                                      | 7.30 us: 1.06x faster                                                      |
| sympy_integrate            | 25.8 ms                                                      | 24.5 ms: 1.05x faster                                                      |
| nqueens                    | 103 ms                                                       | 98.2 ms: 1.04x faster                                                      |
| mdp                        | 2.77 sec                                                     | 2.65 sec: 1.04x faster                                                     |
| thrift                     | 931 us                                                       | 893 us: 1.04x faster                                                       |
| gc_traversal               | 4.15 ms                                                      | 3.99 ms: 1.04x faster                                                      |
| raytrace                   | 309 ms                                                       | 301 ms: 1.03x faster                                                       |
| hexiom                     | 6.98 ms                                                      | 6.80 ms: 1.03x faster                                                      |
| json                       | 5.58 ms                                                      | 5.45 ms: 1.02x faster                                                      |
| logging_silent             | 100 ns                                                       | 98.0 ns: 1.02x faster                                                      |
| pickle_pure_python         | 316 us                                                       | 313 us: 1.01x faster                                                       |
| meteor_contest             | 131 ms                                                       | 130 ms: 1.01x faster                                                       |
| deepcopy_memo              | 37.5 us                                                      | 37.8 us: 1.01x slower                                                      |
| django_template            | 39.3 ms                                                      | 39.8 ms: 1.01x slower                                                      |
| pprint_pformat             | 1.67 sec                                                     | 1.69 sec: 1.01x slower                                                     |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.01x slower                                                      |
| create_gc_cycles           | 1.58 ms                                                      | 1.60 ms: 1.02x slower                                                      |
| deltablue                  | 3.97 ms                                                      | 4.04 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.51 ms                                                      | 1.55 ms: 1.02x slower                                                      |
| dulwich_log                | 67.4 ms                                                      | 69.0 ms: 1.02x slower                                                      |
| tornado_http               | 124 ms                                                       | 128 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 805 ms                                                       | 827 ms: 1.03x slower                                                       |
| richards                   | 49.7 ms                                                      | 51.2 ms: 1.03x slower                                                      |
| pidigits                   | 251 ms                                                       | 261 ms: 1.04x slower                                                       |
| pickle_dict                | 32.3 us                                                      | 33.6 us: 1.04x slower                                                      |
| scimark_fft                | 281 ms                                                       | 292 ms: 1.04x slower                                                       |
| regex_effbot               | 3.34 ms                                                      | 3.48 ms: 1.04x slower                                                      |
| regex_v8                   | 24.4 ms                                                      | 25.8 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.91 ms                                                      | 2.03 ms: 1.06x slower                                                      |
| sqlite_synth               | 2.52 us                                                      | 2.69 us: 1.07x slower                                                      |
| regex_dna                  | 227 ms                                                       | 247 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 59.0 ms                                                      | 64.3 ms: 1.09x slower                                                      |
| pickle                     | 9.89 us                                                      | 10.9 us: 1.10x slower                                                      |
| scimark_lu                 | 114 ms                                                       | 126 ms: 1.11x slower                                                       |
| go                         | 158 ms                                                       | 175 ms: 1.11x slower                                                       |
| pyflate                    | 449 ms                                                       | 501 ms: 1.11x slower                                                       |
| html5lib                   | 72.2 ms                                                      | 81.5 ms: 1.13x slower                                                      |
| mypy2                      | 762 ms                                                       | 867 ms: 1.14x slower                                                       |
| genshi_text                | 25.5 ms                                                      | 29.1 ms: 1.14x slower                                                      |
| unpickle                   | 13.3 us                                                      | 15.3 us: 1.15x slower                                                      |
| 2to3                       | 287 ms                                                       | 331 ms: 1.15x slower                                                       |
| pickle_list                | 3.94 us                                                      | 4.55 us: 1.16x slower                                                      |
| gunicorn                   | 966 us                                                       | 1.12 ms: 1.16x slower                                                      |
| telco                      | 6.81 ms                                                      | 8.00 ms: 1.18x slower                                                      |
| aiohttp                    | 986 us                                                       | 1.16 ms: 1.18x slower                                                      |
| genshi_xml                 | 57.1 ms                                                      | 68.1 ms: 1.19x slower                                                      |
| xml_etree_process          | 55.9 ms                                                      | 68.4 ms: 1.22x slower                                                      |
| xml_etree_generate         | 79.7 ms                                                      | 98.6 ms: 1.24x slower                                                      |
| coverage                   | 66.1 ms                                                      | 83.0 ms: 1.26x slower                                                      |
| pycparser                  | 1.31 sec                                                     | 1.65 sec: 1.26x slower                                                     |
| xml_etree_parse            | 155 ms                                                       | 202 ms: 1.31x slower                                                       |
| python_startup             | 10.7 ms                                                      | 14.5 ms: 1.35x slower                                                      |
| scimark_sor                | 110 ms                                                       | 151 ms: 1.37x slower                                                       |
| async_generators           | 322 ms                                                       | 474 ms: 1.48x slower                                                       |
| xml_etree_iterparse        | 107 ms                                                       | 162 ms: 1.52x slower                                                       |
| python_startup_no_site     | 7.73 ms                                                      | 12.6 ms: 1.62x slower                                                      |
| pylint                     | 514 ms                                                       | 835 ms: 1.62x slower                                                       |
| docutils                   | 2.85 sec                                                     | 4.68 sec: 1.64x slower                                                     |
| dask                       | 410 ms                                                       | 708 ms: 1.73x slower                                                       |
| float                      | 74.9 ms                                                      | 149 ms: 1.98x slower                                                       |
| unpack_sequence            | 45.7 ns                                                      | 118 ns: 2.59x slower                                                       |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 3.26 sec: 4.33x slower                                                     |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 3.43 sec: 4.57x slower                                                     |
| async_tree_none            | 518 ms                                                       | 2.68 sec: 5.18x slower                                                     |
| async_tree_memoization     | 629 ms                                                       | 3.39 sec: 5.38x slower                                                     |
| async_tree_memoization_tg  | 600 ms                                                       | 3.49 sec: 5.82x slower                                                     |
| async_tree_none_tg         | 474 ms                                                       | 2.83 sec: 5.96x slower                                                     |
| async_tree_io              | 1.17 sec                                                     | 9.59 sec: 8.19x slower                                                     |
| async_tree_io_tg           | 1.15 sec                                                     | 10.1 sec: 8.73x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                               |

Benchmark hidden because not significant (8): unpickle_list, scimark_monte_carlo, asyncio_websockets, scimark_sparse_mat_mult, sqlglot_normalize, deepcopy_reduce, deepcopy, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.59% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.13x