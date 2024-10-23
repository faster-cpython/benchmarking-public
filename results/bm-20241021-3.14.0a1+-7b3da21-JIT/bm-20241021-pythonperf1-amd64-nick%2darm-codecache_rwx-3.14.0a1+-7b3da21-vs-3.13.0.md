# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-amd64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.01x slower
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 234 ms: 1.08x slower                                                     |
| docutils       | 1.57 sec                                                    | 1.81 sec: 1.15x slower                                                   |
| tornado_http   | 92.8 ms                                                     | 98.5 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                       | 1.07x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                     |
| async_tree_none            | 223 ms                                                      | 219 ms: 1.02x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.02x slower                                                     |
| async_tree_memoization     | 271 ms                                                      | 283 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                     |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.09x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                    |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                     |
| async_tree_io_tg           | 512 ms                                                      | 632 ms: 1.23x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                                    |
| pidigits       | 148 ms                                                      | 148 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                       | 1.07x faster                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                                     |
| regex_v8       | 14.7 ms                                                     | 15.0 ms: 1.03x slower                                                    |
| regex_compile  | 80.1 ms                                                     | 82.6 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                       | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                   |
| xml_etree_generate   | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                    |
| xml_etree_process    | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                    |
| json_loads           | 14.3 us                                                     | 14.4 us: 1.01x slower                                                    |
| xml_etree_parse      | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.4 ms: 1.02x slower                                                    |
| pickle_pure_python   | 183 us                                                      | 197 us: 1.07x slower                                                     |
| json_dumps           | 5.76 ms                                                     | 6.20 ms: 1.08x slower                                                    |
| unpickle_pure_python | 127 us                                                      | 141 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                    |
| python_startup         | 22.2 ms                                                     | 24.2 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.09 ms: 1.23x faster                                                    |
| django_template | 21.8 ms                                                     | 26.6 ms: 1.22x slower                                                    |
| genshi_xml      | 32.8 ms                                                     | 40.3 ms: 1.23x slower                                                    |
| genshi_text     | 14.9 ms                                                     | 18.5 ms: 1.25x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 531 us: 16.34x faster                                                    |
| deepcopy_memo              | 21.8 us                                                     | 16.2 us: 1.35x faster                                                    |
| mako                       | 6.24 ms                                                     | 5.09 ms: 1.23x faster                                                    |
| nbody                      | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                                    |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                                     |
| fannkuch                   | 245 ms                                                      | 213 ms: 1.15x faster                                                     |
| scimark_sor                | 72.0 ms                                                     | 63.1 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 40.3 ms                                                     | 35.8 ms: 1.13x faster                                                    |
| scimark_fft                | 174 ms                                                      | 156 ms: 1.12x faster                                                     |
| pprint_safe_repr           | 493 ms                                                      | 442 ms: 1.12x faster                                                     |
| spectral_norm              | 59.2 ms                                                     | 53.2 ms: 1.11x faster                                                    |
| pprint_pformat             | 991 ms                                                      | 900 ms: 1.10x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                    |
| crypto_pyaes               | 42.8 ms                                                     | 39.7 ms: 1.08x faster                                                    |
| telco                      | 4.85 ms                                                     | 4.51 ms: 1.07x faster                                                    |
| pycparser                  | 758 ms                                                      | 707 ms: 1.07x faster                                                     |
| tomli_loads                | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                   |
| xml_etree_generate         | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                    |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.24 ms: 1.05x faster                                                    |
| xml_etree_process          | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                    |
| meteor_contest             | 72.3 ms                                                     | 70.0 ms: 1.03x faster                                                    |
| go                         | 84.6 ms                                                     | 82.4 ms: 1.03x faster                                                    |
| async_tree_none            | 223 ms                                                      | 219 ms: 1.02x faster                                                     |
| scimark_lu                 | 54.0 ms                                                     | 53.3 ms: 1.01x faster                                                    |
| json                       | 2.98 ms                                                     | 2.95 ms: 1.01x faster                                                    |
| pidigits                   | 148 ms                                                      | 148 ms: 1.00x faster                                                     |
| json_loads                 | 14.3 us                                                     | 14.4 us: 1.01x slower                                                    |
| xml_etree_parse            | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                    |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.4 ms: 1.02x slower                                                    |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.02x slower                                                     |
| python_startup_no_site     | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                    |
| regex_v8                   | 14.7 ms                                                     | 15.0 ms: 1.03x slower                                                    |
| regex_compile              | 80.1 ms                                                     | 82.6 ms: 1.03x slower                                                    |
| async_tree_memoization     | 271 ms                                                      | 283 ms: 1.04x slower                                                     |
| chaos                      | 37.9 ms                                                     | 39.7 ms: 1.05x slower                                                    |
| coverage                   | 46.7 ms                                                     | 49.5 ms: 1.06x slower                                                    |
| logging_simple             | 5.72 us                                                     | 6.08 us: 1.06x slower                                                    |
| tornado_http               | 92.8 ms                                                     | 98.5 ms: 1.06x slower                                                    |
| mdp                        | 1.38 sec                                                    | 1.48 sec: 1.07x slower                                                   |
| comprehensions             | 10.2 us                                                     | 10.9 us: 1.07x slower                                                    |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                     |
| logging_silent             | 51.0 ns                                                     | 54.5 ns: 1.07x slower                                                    |
| logging_format             | 6.15 us                                                     | 6.58 us: 1.07x slower                                                    |
| pickle_pure_python         | 183 us                                                      | 197 us: 1.07x slower                                                     |
| json_dumps                 | 5.76 ms                                                     | 6.20 ms: 1.08x slower                                                    |
| 2to3                       | 217 ms                                                      | 234 ms: 1.08x slower                                                     |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                                     |
| sympy_str                  | 166 ms                                                      | 180 ms: 1.08x slower                                                     |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.09x slower                                                     |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                    |
| python_startup             | 22.2 ms                                                     | 24.2 ms: 1.09x slower                                                    |
| sympy_sum                  | 86.4 ms                                                     | 95.5 ms: 1.11x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                    |
| unpickle_pure_python       | 127 us                                                      | 141 us: 1.11x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 858 us: 1.13x slower                                                     |
| nqueens                    | 55.5 ms                                                     | 62.7 ms: 1.13x slower                                                    |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.15x slower                                                     |
| docutils                   | 1.57 sec                                                    | 1.81 sec: 1.15x slower                                                   |
| hexiom                     | 3.69 ms                                                     | 4.25 ms: 1.15x slower                                                    |
| sqlglot_optimize           | 33.1 ms                                                     | 38.8 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 171 ms                                                      | 202 ms: 1.18x slower                                                     |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                                    |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 14.8 ms: 1.21x slower                                                    |
| deltablue                  | 1.86 ms                                                     | 2.27 ms: 1.22x slower                                                    |
| django_template            | 21.8 ms                                                     | 26.6 ms: 1.22x slower                                                    |
| pylint                     | 211 ms                                                      | 258 ms: 1.22x slower                                                     |
| genshi_xml                 | 32.8 ms                                                     | 40.3 ms: 1.23x slower                                                    |
| richards                   | 26.0 ms                                                     | 32.0 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 512 ms                                                      | 632 ms: 1.23x slower                                                     |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.23x slower                                                    |
| genshi_text                | 14.9 ms                                                     | 18.5 ms: 1.25x slower                                                    |
| bench_mp_pool              | 69.6 ms                                                     | 87.2 ms: 1.25x slower                                                    |
| gc_traversal               | 1.55 ms                                                     | 1.95 ms: 1.26x slower                                                    |
| raytrace                   | 156 ms                                                      | 206 ms: 1.32x slower                                                     |
| create_gc_cycles           | 829 us                                                      | 1.41 ms: 1.70x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (8): regex_effbot, async_tree_cpu_io_mixed, float, dulwich_log, pathlib, pyflate, html5lib, bench_thread_pool
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: sphinx

# HPT report

- Reliability score: 98.48% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown