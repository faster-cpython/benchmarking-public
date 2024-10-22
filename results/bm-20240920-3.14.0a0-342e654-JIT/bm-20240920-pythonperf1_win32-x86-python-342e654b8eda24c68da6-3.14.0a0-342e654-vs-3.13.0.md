# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.10x faster
- HPT reliability: 98.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.97 sec: 1.08x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 100 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 607 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 472 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 468 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.16x slower                                                          |
| async_generators           | 274 ms                                                          | 335 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 50.5 ms: 1.62x faster                                                          |
| float          | 57.8 ms                                                         | 43.5 ms: 1.33x faster                                                          |
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 102 ms: 1.02x faster                                                           |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.97 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 62.6 ms                                                         | 53.5 ms: 1.17x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 39.7 ms: 1.13x faster                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| unpickle_list        | 3.09 us                                                         | 2.78 us: 1.11x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 60.9 ms: 1.07x faster                                                          |
| pickle               | 8.42 us                                                         | 7.93 us: 1.06x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 103 ms: 1.06x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.31 us: 1.03x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.02x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 163 us: 1.01x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 242 us: 1.02x slower                                                           |
| json_loads           | 21.0 us                                                         | 21.4 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.47 ms: 1.33x faster                                                          |
| django_template | 32.7 ms                                                         | 34.0 ms: 1.04x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 24.1 ms: 1.07x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 53.8 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 790 us: 12.85x faster                                                          |
| coverage                   | 333 ms                                                          | 53.8 ms: 6.19x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.72x faster                                                          |
| nbody                      | 81.9 ms                                                         | 50.5 ms: 1.62x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 46.6 ms: 1.53x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 607 ms: 1.39x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 68.0 ms: 1.35x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.47 ms: 1.33x faster                                                          |
| float                      | 57.8 ms                                                         | 43.5 ms: 1.33x faster                                                          |
| deepcopy                   | 307 us                                                          | 233 us: 1.31x faster                                                           |
| fannkuch                   | 293 ms                                                          | 237 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.36 ms: 1.23x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 48.4 ms: 1.20x faster                                                          |
| deltablue                  | 2.41 ms                                                         | 2.02 ms: 1.19x faster                                                          |
| scimark_fft                | 206 ms                                                          | 175 ms: 1.18x faster                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 53.5 ms: 1.17x faster                                                          |
| pyflate                    | 326 ms                                                          | 282 ms: 1.16x faster                                                           |
| xml_etree_process          | 45.0 ms                                                         | 39.7 ms: 1.13x faster                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| deepcopy_reduce            | 2.85 us                                                         | 2.53 us: 1.13x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| unpickle_list              | 3.09 us                                                         | 2.78 us: 1.11x faster                                                          |
| async_tree_none            | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.00 ms: 1.11x faster                                                          |
| comprehensions             | 12.7 us                                                         | 11.6 us: 1.10x faster                                                          |
| go                         | 111 ms                                                          | 102 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 83.1 ms: 1.08x faster                                                          |
| pprint_safe_repr           | 644 ms                                                          | 598 ms: 1.08x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 71.8 ms: 1.07x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 60.9 ms: 1.07x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.93 us: 1.06x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 103 ms: 1.06x faster                                                           |
| scimark_lu                 | 63.5 ms                                                         | 60.0 ms: 1.06x faster                                                          |
| richards_super             | 38.0 ms                                                         | 35.9 ms: 1.06x faster                                                          |
| pycparser                  | 869 ms                                                          | 825 ms: 1.05x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 472 ms: 1.05x faster                                                           |
| tornado_http               | 104 ms                                                          | 100 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.25 sec: 1.04x faster                                                         |
| unpack_sequence            | 42.9 ns                                                         | 41.4 ns: 1.04x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.90 us: 1.03x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 59.7 ns: 1.03x faster                                                          |
| richards                   | 33.8 ms                                                         | 32.8 ms: 1.03x faster                                                          |
| logging_format             | 8.57 us                                                         | 8.34 us: 1.03x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.31 us: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| logging_simple             | 7.87 us                                                         | 7.72 us: 1.02x faster                                                          |
| dulwich_log                | 49.7 ms                                                         | 48.8 ms: 1.02x faster                                                          |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.02x faster                                                          |
| pidigits                   | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| regex_compile              | 103 ms                                                          | 102 ms: 1.02x faster                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 1.04 ms: 1.01x faster                                                          |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.00x faster                                                          |
| mdp                        | 1.67 sec                                                        | 1.69 sec: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 468 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 163 us: 1.01x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 76.2 ms: 1.01x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 242 us: 1.02x slower                                                           |
| 2to3                       | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| json_loads                 | 21.0 us                                                         | 21.4 us: 1.02x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 521 ms: 1.02x slower                                                           |
| sympy_str                  | 215 ms                                                          | 220 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| django_template            | 32.7 ms                                                         | 34.0 ms: 1.04x slower                                                          |
| chaos                      | 51.2 ms                                                         | 53.3 ms: 1.04x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 745 us: 1.04x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 4.86 ms: 1.05x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 113 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 231 ms: 1.05x slower                                                           |
| sympy_expand               | 375 ms                                                          | 394 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 146 us: 1.07x slower                                                           |
| genshi_text                | 22.4 ms                                                         | 24.1 ms: 1.07x slower                                                          |
| generators                 | 22.1 ms                                                         | 23.8 ms: 1.08x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.97 sec: 1.08x slower                                                         |
| sqlglot_optimize           | 42.5 ms                                                         | 46.0 ms: 1.08x slower                                                          |
| genshi_xml                 | 49.5 ms                                                         | 53.8 ms: 1.09x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.97 ms: 1.09x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 16.7 ms: 1.10x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.1 ms: 1.16x slower                                                          |
| raytrace                   | 205 ms                                                          | 244 ms: 1.19x slower                                                           |
| pylint                     | 225 ms                                                          | 268 ms: 1.19x slower                                                           |
| async_generators           | 274 ms                                                          | 335 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, json, bench_mp_pool, scimark_monte_carlo, python_startup_no_site, async_tree_io
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 98.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown