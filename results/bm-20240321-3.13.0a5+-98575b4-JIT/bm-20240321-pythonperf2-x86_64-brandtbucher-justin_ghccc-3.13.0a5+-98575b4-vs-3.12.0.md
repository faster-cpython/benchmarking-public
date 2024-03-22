# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.26x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 331 ms: 1.16x slower                                                       |
| chameleon      | 7.23 ms                                                      | 7.32 ms: 1.01x slower                                                      |
| docutils       | 2.87 sec                                                     | 4.68 sec: 1.63x slower                                                     |
| tornado_http   | 121 ms                                                       | 128 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.19x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 696 ms                                                       | 3.26 sec: 4.68x slower                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 3.43 sec: 4.92x slower                                                     |
| async_tree_none            | 452 ms                                                       | 2.68 sec: 5.94x slower                                                     |
| async_tree_memoization     | 544 ms                                                       | 3.39 sec: 6.22x slower                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 3.49 sec: 6.46x slower                                                     |
| async_tree_none_tg         | 431 ms                                                       | 2.83 sec: 6.57x slower                                                     |
| async_tree_io              | 1.04 sec                                                     | 9.59 sec: 9.20x slower                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 10.1 sec: 9.56x slower                                                     |
| Geometric mean             | (ref)                                                        | 6.50x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                      |
| pidigits       | 265 ms                                                       | 261 ms: 1.02x faster                                                       |
| float          | 76.6 ms                                                      | 149 ms: 1.94x slower                                                       |
| Geometric mean | (ref)                                                        | 1.22x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                      |
| regex_dna      | 239 ms                                                       | 247 ms: 1.04x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                     |
| unpickle_list        | 4.66 us                                                      | 4.58 us: 1.02x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                      |
| pickle_list          | 4.43 us                                                      | 4.55 us: 1.03x slower                                                      |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.03x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 33.6 us: 1.03x slower                                                      |
| pickle               | 10.5 us                                                      | 10.9 us: 1.03x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 226 us: 1.08x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 98.6 ms: 1.14x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 68.4 ms: 1.17x slower                                                      |
| xml_etree_parse      | 144 ms                                                       | 202 ms: 1.41x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 162 ms: 1.57x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 14.5 ms: 1.24x slower                                                      |
| python_startup_no_site | 8.64 ms                                                      | 12.6 ms: 1.45x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.34x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.30 ms: 1.08x faster                                                      |
| django_template | 38.2 ms                                                      | 39.8 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 119 us: 1.27x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                      |
| generators                 | 37.4 ms                                                      | 33.0 ms: 1.13x faster                                                      |
| crypto_pyaes               | 80.3 ms                                                      | 72.2 ms: 1.11x faster                                                      |
| spectral_norm              | 91.6 ms                                                      | 82.8 ms: 1.11x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.30 ms: 1.08x faster                                                      |
| nbody                      | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.05 ms: 1.04x faster                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.69 us: 1.03x faster                                                      |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.02x faster                                                      |
| logging_format             | 7.48 us                                                      | 7.30 us: 1.02x faster                                                      |
| unpickle_list              | 4.66 us                                                      | 4.58 us: 1.02x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                      |
| pidigits                   | 265 ms                                                       | 261 ms: 1.02x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 160 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                       |
| chaos                      | 64.0 ms                                                      | 63.4 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.39 us: 1.01x slower                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 69.6 ms: 1.01x slower                                                      |
| raytrace                   | 298 ms                                                       | 301 ms: 1.01x slower                                                       |
| chameleon                  | 7.23 ms                                                      | 7.32 ms: 1.01x slower                                                      |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                     |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 827 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.02x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 24.5 ms: 1.03x slower                                                      |
| pickle_list                | 4.43 us                                                      | 4.55 us: 1.03x slower                                                      |
| deepcopy_memo              | 36.8 us                                                      | 37.8 us: 1.03x slower                                                      |
| unpickle                   | 14.8 us                                                      | 15.3 us: 1.03x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 33.6 us: 1.03x slower                                                      |
| pickle                     | 10.5 us                                                      | 10.9 us: 1.03x slower                                                      |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                     |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.04x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                      |
| django_template            | 38.2 ms                                                      | 39.8 ms: 1.04x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                       |
| tornado_http               | 121 ms                                                       | 128 ms: 1.05x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 69.0 ms: 1.06x slower                                                      |
| deepcopy                   | 368 us                                                       | 391 us: 1.06x slower                                                       |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 226 us: 1.08x slower                                                       |
| sympy_expand               | 484 ms                                                       | 521 ms: 1.08x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 98.2 ms: 1.09x slower                                                      |
| gunicorn                   | 1.00 ms                                                      | 1.12 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 64.3 ms: 1.12x slower                                                      |
| richards                   | 45.7 ms                                                      | 51.2 ms: 1.12x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.55 ms: 1.12x slower                                                      |
| richards_super             | 51.3 ms                                                      | 57.9 ms: 1.13x slower                                                      |
| aiohttp                    | 1.02 ms                                                      | 1.16 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 2.03 ms: 1.14x slower                                                      |
| pyflate                    | 439 ms                                                       | 501 ms: 1.14x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.80 ms: 1.14x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 98.6 ms: 1.14x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 3.99 ms: 1.15x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.00 ms: 1.15x slower                                                      |
| 2to3                       | 285 ms                                                       | 331 ms: 1.16x slower                                                       |
| go                         | 150 ms                                                       | 175 ms: 1.17x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 68.4 ms: 1.17x slower                                                      |
| async_generators           | 390 ms                                                       | 474 ms: 1.22x slower                                                       |
| python_startup             | 11.6 ms                                                      | 14.5 ms: 1.24x slower                                                      |
| coverage                   | 66.7 ms                                                      | 83.0 ms: 1.24x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 4.04 ms: 1.25x slower                                                      |
| scimark_lu                 | 98.8 ms                                                      | 126 ms: 1.28x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.65 sec: 1.34x slower                                                     |
| scimark_sor                | 109 ms                                                       | 151 ms: 1.38x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 202 ms: 1.41x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 12.6 ms: 1.45x slower                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 162 ms: 1.57x slower                                                       |
| docutils                   | 2.87 sec                                                     | 4.68 sec: 1.63x slower                                                     |
| dask                       | 392 ms                                                       | 708 ms: 1.81x slower                                                       |
| float                      | 76.6 ms                                                      | 149 ms: 1.94x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 118 ns: 2.22x slower                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 3.26 sec: 4.68x slower                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 3.43 sec: 4.92x slower                                                     |
| async_tree_none            | 452 ms                                                       | 2.68 sec: 5.94x slower                                                     |
| async_tree_memoization     | 544 ms                                                       | 3.39 sec: 6.22x slower                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 3.49 sec: 6.46x slower                                                     |
| async_tree_none_tg         | 431 ms                                                       | 2.83 sec: 6.57x slower                                                     |
| async_tree_io              | 1.04 sec                                                     | 9.59 sec: 9.20x slower                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 10.1 sec: 9.56x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.26x slower                                                               |

Benchmark hidden because not significant (7): bench_thread_pool, regex_compile, sympy_str, asyncio_websockets, bench_mp_pool, create_gc_cycles, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.01x