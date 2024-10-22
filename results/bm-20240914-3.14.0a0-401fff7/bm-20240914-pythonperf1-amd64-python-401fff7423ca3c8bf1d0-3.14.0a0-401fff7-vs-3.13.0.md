# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.6 ms: 1.05x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 83.5 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 263 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 83.3 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 15.2 ms: 1.04x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 6.99 us: 1.05x faster                                                      |
| unpickle_list        | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.27 us: 1.07x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.0 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.5 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 216 us: 1.18x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.63 sec: 1.20x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 157 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.82 ms: 1.09x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 36.8 ms: 1.12x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| django_template | 21.8 ms                                                     | 26.0 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 513 us: 16.92x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 83.5 ms: 1.11x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 74.6 ms: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 66.2 ms: 1.05x faster                                                      |
| pickle                     | 7.34 us                                                     | 6.99 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.04x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.0 us: 1.04x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 263 ms: 1.03x faster                                                       |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.63 us: 1.02x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.8 ms: 1.02x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.01 ms: 1.03x slower                                                      |
| 2to3                       | 217 ms                                                      | 225 ms: 1.04x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.2 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.7 ms: 1.04x slower                                                      |
| go                         | 84.6 ms                                                     | 87.8 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.3 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.6 ms: 1.05x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 874 us: 1.05x slower                                                       |
| unpack_sequence            | 40.0 ns                                                     | 42.2 ns: 1.05x slower                                                      |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.27 us: 1.07x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| meteor_contest             | 72.3 ms                                                     | 78.0 ms: 1.08x slower                                                      |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                      |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| pycparser                  | 758 ms                                                      | 826 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.82 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.31 us: 1.10x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.5 ms: 1.10x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.53 sec: 1.10x slower                                                     |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 59.0 ms: 1.11x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 47.9 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 551 ms: 1.12x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.90 us: 1.12x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.8 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.5 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.13 sec: 1.14x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.15x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 64.5 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.0 ms: 1.16x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 62.9 ms: 1.16x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 216 us: 1.18x slower                                                       |
| pyflate                    | 275 ms                                                      | 326 ms: 1.18x slower                                                       |
| scimark_fft                | 174 ms                                                      | 206 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.18x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.2 us: 1.19x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 905 us: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.79 ms: 1.19x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.0 ms: 1.19x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.63 sec: 1.20x slower                                                     |
| deltablue                  | 1.86 ms                                                     | 2.29 ms: 1.23x slower                                                      |
| fannkuch                   | 245 ms                                                      | 302 ms: 1.24x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.57 ms: 1.24x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 157 us: 1.24x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 73.6 ms: 1.24x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.4 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.2 ms: 1.25x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.7 ms: 1.25x slower                                                      |
| raytrace                   | 156 ms                                                      | 195 ms: 1.25x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 64.8 ns: 1.27x slower                                                      |
| nbody                      | 64.5 ms                                                     | 83.3 ms: 1.29x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 93.9 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (11): bench_thread_pool, asyncio_tcp_ssl, async_tree_none_tg, python_startup, pickle_list, async_tree_cpu_io_mixed, json, xml_etree_parse, python_startup_no_site, json_loads, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown