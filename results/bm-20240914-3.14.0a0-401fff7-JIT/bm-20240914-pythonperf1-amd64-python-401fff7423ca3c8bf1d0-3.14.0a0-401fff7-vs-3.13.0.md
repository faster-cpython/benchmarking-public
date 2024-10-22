# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.00x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 239 ms: 1.10x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.1 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 87.4 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 463 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.39 sec: 1.18x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.4 ms: 1.30x faster                                                      |
| float          | 48.1 ms                                                     | 44.5 ms: 1.08x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 94.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.3 ms                                                     | 49.0 ms: 1.09x faster                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| xml_etree_process    | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                      |
| pickle_list          | 2.89 us                                                     | 2.78 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 17.9 us: 1.01x faster                                                      |
| pickle               | 7.34 us                                                     | 7.38 us: 1.01x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.87 us: 1.05x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 196 us: 1.07x slower                                                       |
| unpickle             | 8.63 us                                                     | 9.27 us: 1.07x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 145 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.6 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| django_template | 21.8 ms                                                     | 26.2 ms: 1.20x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 45.7 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.52x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 14.8 us: 1.47x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 463 ms: 1.41x faster                                                       |
| spectral_norm              | 59.2 ms                                                     | 43.3 ms: 1.37x faster                                                      |
| nbody                      | 64.5 ms                                                     | 49.4 ms: 1.30x faster                                                      |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                       |
| scimark_sor                | 72.0 ms                                                     | 60.7 ms: 1.19x faster                                                      |
| mako                       | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.39 sec: 1.18x faster                                                     |
| scimark_fft                | 174 ms                                                      | 149 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 38.6 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.13 ms: 1.10x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 49.0 ms: 1.09x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 74.8 ms: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| float                      | 48.1 ms                                                     | 44.5 ms: 1.08x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 87.4 ms: 1.06x faster                                                      |
| pycparser                  | 758 ms                                                      | 715 ms: 1.06x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.05x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                       |
| pyflate                    | 275 ms                                                      | 265 ms: 1.04x faster                                                       |
| pickle_list                | 2.89 us                                                     | 2.78 us: 1.04x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| deltablue                  | 1.86 ms                                                     | 1.82 ms: 1.02x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 809 us: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| json                       | 2.98 ms                                                     | 2.95 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pickle_dict                | 18.0 us                                                     | 17.9 us: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.55 ms: 1.00x faster                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.00x slower                                                       |
| pickle                     | 7.34 us                                                     | 7.38 us: 1.01x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 54.4 ms: 1.01x slower                                                      |
| fannkuch                   | 245 ms                                                      | 248 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 503 ms: 1.02x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 71.7 ms: 1.03x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.1 ms: 1.03x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| meteor_contest             | 72.3 ms                                                     | 74.9 ms: 1.04x slower                                                      |
| comprehensions             | 10.2 us                                                     | 10.7 us: 1.04x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.03 sec: 1.04x slower                                                     |
| logging_format             | 6.15 us                                                     | 6.45 us: 1.05x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.3 ms: 1.05x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.87 us: 1.05x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.0 ms: 1.06x slower                                                      |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.06 us: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 42.7 ms: 1.06x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 196 us: 1.07x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 59.6 ms: 1.07x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.27 us: 1.07x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 901 us: 1.09x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.1 ms: 1.09x slower                                                      |
| go                         | 84.6 ms                                                     | 92.2 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| 2to3                       | 217 ms                                                      | 239 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 57.2 ns: 1.12x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 97.9 ms: 1.13x slower                                                      |
| sympy_str                  | 166 ms                                                      | 189 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 145 us: 1.14x slower                                                       |
| sympy_expand               | 285 ms                                                      | 330 ms: 1.16x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 199 ms: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 886 us: 1.16x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 94.2 ms: 1.18x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.2 ms: 1.20x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 39.7 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.8 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| pylint                     | 211 ms                                                      | 263 ms: 1.25x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                      |
| raytrace                   | 156 ms                                                      | 202 ms: 1.29x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.89 ms: 1.33x slower                                                      |
| richards_super             | 29.3 ms                                                     | 39.1 ms: 1.33x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 45.7 ms: 1.39x slower                                                      |
| richards                   | 26.0 ms                                                     | 36.5 ms: 1.40x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 56.9 ns: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, sqlite_synth, json_loads, python_startup_no_site
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown