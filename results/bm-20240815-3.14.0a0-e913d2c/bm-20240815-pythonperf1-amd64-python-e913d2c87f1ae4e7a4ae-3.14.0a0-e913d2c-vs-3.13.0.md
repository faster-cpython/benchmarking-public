# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-amd64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 231 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.51 sec: 1.08x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 547 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 56.4 ms: 1.17x slower                                                      |
| nbody          | 64.5 ms                                                     | 82.3 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.5 ms: 1.12x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.6 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.22 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.8 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 211 us: 1.15x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 148 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.4 ms: 1.11x slower                                                      |
| mako            | 6.24 ms                                                     | 7.03 ms: 1.13x slower                                                      |
| django_template | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.5 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 530 us: 16.38x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.51 sec: 1.08x faster                                                     |
| deepcopy_memo              | 21.8 us                                                     | 20.4 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 78.3 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 68.8 ms: 1.01x faster                                                      |
| python_startup             | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.00x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.6 ms: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.4 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.06x slower                                                       |
| 2to3                       | 217 ms                                                      | 231 ms: 1.07x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 92.3 ms: 1.07x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 547 ms: 1.07x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 77.2 ms: 1.07x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 43.4 ms: 1.07x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.49 sec: 1.07x slower                                                     |
| json_dumps                 | 5.76 ms                                                     | 6.22 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| sympy_str                  | 166 ms                                                      | 180 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 57.8 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.72 us: 1.09x slower                                                      |
| sympy_expand               | 285 ms                                                      | 312 ms: 1.09x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 909 us: 1.10x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.29 us: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 36.4 ms: 1.11x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| pprint_safe_repr           | 493 ms                                                      | 549 ms: 1.11x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 47.8 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 16.5 ms: 1.12x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.03 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                                       |
| django_template            | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 67.6 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.68 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.7 ms: 1.15x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 211 us: 1.15x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.14 sec: 1.15x slower                                                     |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| go                         | 84.6 ms                                                     | 98.5 ms: 1.16x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 888 us: 1.17x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 148 us: 1.17x slower                                                       |
| pycparser                  | 758 ms                                                      | 888 ms: 1.17x slower                                                       |
| float                      | 48.1 ms                                                     | 56.4 ms: 1.17x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.5 ms: 1.17x slower                                                      |
| pyflate                    | 275 ms                                                      | 324 ms: 1.18x slower                                                       |
| scimark_fft                | 174 ms                                                      | 205 ms: 1.18x slower                                                       |
| fannkuch                   | 245 ms                                                      | 294 ms: 1.20x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.46 ms: 1.21x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 65.5 ms: 1.21x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.27 ms: 1.22x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.24x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.3 ms: 1.24x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.3 ms: 1.25x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.7 ns: 1.25x slower                                                      |
| raytrace                   | 156 ms                                                      | 195 ms: 1.25x slower                                                       |
| nbody                      | 64.5 ms                                                     | 82.3 ms: 1.28x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 92.2 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, bench_thread_pool, json, tornado_http, python_startup_no_site, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown