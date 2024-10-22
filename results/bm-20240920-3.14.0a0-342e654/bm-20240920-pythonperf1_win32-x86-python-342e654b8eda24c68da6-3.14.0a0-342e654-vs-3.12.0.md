# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 256 ms: 1.09x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.6 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.0 ms: 1.40x faster                                                          |
| float          | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_dna      | 127 ms                                                          | 128 ms: 1.00x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 177 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| tomli_loads          | 2.20 sec                                                        | 1.92 sec: 1.14x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 261 us: 1.10x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.2 ms: 1.08x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.91 us: 1.01x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.34 us: 1.01x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.45 ms: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.84 us: 1.01x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.09 ms: 1.23x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                          |
| deepcopy                   | 360 us                                                          | 243 us: 1.48x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.2 ms: 1.47x faster                                                          |
| nbody                      | 127 ms                                                          | 91.0 ms: 1.40x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 45.4 ns: 1.38x faster                                                          |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.8 ms: 1.37x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 69.2 ms: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| logging_silent             | 101 ns                                                          | 76.1 ns: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 98.2 ms: 1.32x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.73 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.26 ms: 1.30x faster                                                          |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                          |
| raytrace                   | 308 ms                                                          | 243 ms: 1.27x faster                                                           |
| go                         | 137 ms                                                          | 109 ms: 1.26x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.1 ms: 1.26x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.06 ms: 1.26x faster                                                          |
| float                      | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 75.6 ms: 1.24x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.09 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.02 us: 1.22x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.74 us: 1.19x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 177 us: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                           |
| pyflate                    | 424 ms                                                          | 357 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.7 ms: 1.17x faster                                                          |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.8 ms: 1.16x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.1 ms: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 51.1 ms: 1.14x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.92 sec: 1.14x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.14x faster                                                          |
| pycparser                  | 978 ms                                                          | 880 ms: 1.11x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.2 ms: 1.10x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.6 ms: 1.10x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 261 us: 1.10x faster                                                           |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.10x faster                                                           |
| 2to3                       | 280 ms                                                          | 256 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 80.1 ms: 1.08x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 49.2 ms: 1.08x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.9 ms: 1.08x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| fannkuch                   | 354 ms                                                          | 330 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.41 sec: 1.06x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 687 ms: 1.05x faster                                                           |
| async_generators           | 313 ms                                                          | 300 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 386 ms: 1.03x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| richards                   | 41.3 ms                                                         | 40.6 ms: 1.02x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.4 ms: 1.01x faster                                                          |
| richards_super             | 46.5 ms                                                         | 45.9 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.91 us: 1.01x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.34 us: 1.01x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.00x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.45 ms: 1.01x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.84 us: 1.01x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.34 ms: 1.04x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.3 ms: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 739 us: 1.13x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.53 ms: 1.18x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.32x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown