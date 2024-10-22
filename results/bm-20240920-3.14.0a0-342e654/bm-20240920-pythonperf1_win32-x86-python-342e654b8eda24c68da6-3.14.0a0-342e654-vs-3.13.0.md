# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 256 ms: 1.01x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.1 ms: 1.02x faster                                                          |
| tornado_http   | 104 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 644 ms: 1.31x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 460 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| async_generators           | 274 ms                                                          | 300 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.16x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.0 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| regex_compile  | 103 ms                                                          | 110 ms: 1.07x slower                                                           |
| regex_dna      | 117 ms                                                          | 128 ms: 1.09x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.42 us                                                         | 7.84 us: 1.07x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.91 us: 1.06x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.2 us: 1.03x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.34 us: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 21.5 us: 1.02x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 49.2 ms: 1.09x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 261 us: 1.10x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.5 ms: 1.02x faster                                                          |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| mako            | 7.31 ms                                                         | 8.09 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 742 us: 13.67x faster                                                          |
| coverage                   | 333 ms                                                          | 51.3 ms: 6.49x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 644 ms: 1.31x faster                                                           |
| deepcopy                   | 307 us                                                          | 243 us: 1.26x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.9 us: 1.20x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.53 us: 1.13x faster                                                          |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                           |
| tornado_http               | 104 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 83.2 ms: 1.08x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.84 us: 1.07x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 2.91 us: 1.06x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.2 us: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 47.1 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| go                         | 111 ms                                                          | 109 ms: 1.02x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.53 ms: 1.02x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 48.5 ms: 1.02x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.34 us: 1.02x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 460 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 75.6 ms: 1.01x slower                                                          |
| 2to3                       | 253 ms                                                          | 256 ms: 1.01x slower                                                           |
| pycparser                  | 869 ms                                                          | 880 ms: 1.01x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 219 ms: 1.02x slower                                                           |
| django_template            | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.02 us: 1.02x slower                                                          |
| logging_format             | 8.57 us                                                         | 8.74 us: 1.02x slower                                                          |
| json_loads                 | 21.0 us                                                         | 21.5 us: 1.02x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 59.8 ms: 1.03x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 51.1 ms: 1.03x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| sympy_expand               | 375 ms                                                          | 386 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 1.09 ms: 1.03x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 739 us: 1.04x slower                                                           |
| meteor_contest             | 77.0 ms                                                         | 80.1 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 234 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 144 us: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.06 ms: 1.05x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 232 ms: 1.06x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 45.4 ns: 1.06x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.9 ms: 1.06x slower                                                          |
| float                      | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 75.8 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 687 ms: 1.07x slower                                                           |
| regex_compile              | 103 ms                                                          | 110 ms: 1.07x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 98.2 ms: 1.07x slower                                                          |
| chaos                      | 51.2 ms                                                         | 55.1 ms: 1.08x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.82 sec: 1.09x slower                                                         |
| pprint_pformat             | 1.30 sec                                                        | 1.41 sec: 1.09x slower                                                         |
| scimark_lu                 | 63.5 ms                                                         | 69.2 ms: 1.09x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 49.2 ms: 1.09x slower                                                          |
| regex_dna                  | 117 ms                                                          | 128 ms: 1.09x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 261 us: 1.10x slower                                                           |
| comprehensions             | 12.7 us                                                         | 14.0 us: 1.10x slower                                                          |
| async_generators           | 274 ms                                                          | 300 ms: 1.10x slower                                                           |
| pyflate                    | 326 ms                                                          | 357 ms: 1.10x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.09 ms: 1.11x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| nbody                      | 81.9 ms                                                         | 91.0 ms: 1.11x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 56.7 ms: 1.13x slower                                                          |
| fannkuch                   | 293 ms                                                          | 330 ms: 1.13x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.26 ms: 1.13x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.73 ms: 1.13x slower                                                          |
| scimark_fft                | 206 ms                                                          | 236 ms: 1.14x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.16x slower                                                          |
| raytrace                   | 205 ms                                                          | 243 ms: 1.18x slower                                                           |
| generators                 | 22.1 ms                                                         | 26.2 ms: 1.19x slower                                                          |
| richards                   | 33.8 ms                                                         | 40.6 ms: 1.20x slower                                                          |
| richards_super             | 38.0 ms                                                         | 45.9 ms: 1.21x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 76.1 ns: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (10): bench_thread_pool, xml_etree_parse, sympy_sum, bench_mp_pool, genshi_text, sqlite_synth, python_startup, json_dumps, async_tree_io, json
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown