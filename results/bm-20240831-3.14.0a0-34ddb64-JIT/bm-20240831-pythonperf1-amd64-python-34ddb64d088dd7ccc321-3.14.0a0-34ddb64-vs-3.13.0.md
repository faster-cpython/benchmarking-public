# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 243 ms: 1.12x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.94 sec: 1.23x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.8 ms: 1.11x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 99.1 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 530 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.09x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 559 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 586 ms: 1.13x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.0 ms: 1.29x faster                                                      |
| float          | 48.1 ms                                                     | 45.3 ms: 1.06x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 95.6 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.7 ms: 1.01x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 195 us: 1.06x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 145 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| django_template | 21.8 ms                                                     | 26.8 ms: 1.23x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 19.7 ms: 1.33x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 46.3 ms: 1.41x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.71x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.0 us: 1.45x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 44.1 ms: 1.34x faster                                                      |
| nbody                      | 64.5 ms                                                     | 50.0 ms: 1.29x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 530 ms: 1.23x faster                                                       |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                       |
| scimark_sor                | 72.0 ms                                                     | 60.5 ms: 1.19x faster                                                      |
| mako                       | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| scimark_fft                | 174 ms                                                      | 149 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 38.2 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.09x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.18 ms: 1.07x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| float                      | 48.1 ms                                                     | 45.3 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.58 ms: 1.06x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                      |
| pyflate                    | 275 ms                                                      | 262 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 79.1 ms: 1.03x faster                                                      |
| fannkuch                   | 245 ms                                                      | 239 ms: 1.03x faster                                                       |
| deltablue                  | 1.86 ms                                                     | 1.82 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                      |
| json                       | 2.98 ms                                                     | 2.93 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.7 ms: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.58 ms: 1.02x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.6 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 507 ms: 1.03x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 74.6 ms: 1.03x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                                      |
| comprehensions             | 10.2 us                                                     | 10.8 us: 1.05x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.46 sec: 1.05x slower                                                     |
| pprint_pformat             | 991 ms                                                      | 1.05 sec: 1.06x slower                                                     |
| logging_simple             | 5.72 us                                                     | 6.05 us: 1.06x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 195 us: 1.06x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.56 us: 1.07x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 99.1 ms: 1.07x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 74.4 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 43.5 ms: 1.08x slower                                                      |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| go                         | 84.6 ms                                                     | 92.0 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 559 ms: 1.09x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 44.0 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 61.4 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.11x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.8 ms: 1.11x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| 2to3                       | 217 ms                                                      | 243 ms: 1.12x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                                      |
| async_tree_io              | 521 ms                                                      | 586 ms: 1.13x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 933 us: 1.13x slower                                                       |
| sympy_str                  | 166 ms                                                      | 190 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 145 us: 1.15x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 99.3 ms: 1.15x slower                                                      |
| sympy_expand               | 285 ms                                                      | 329 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 901 us: 1.18x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 203 ms: 1.19x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 95.6 ms: 1.19x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 40.0 ms: 1.21x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 15.0 ms: 1.22x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.17 ms: 1.23x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.8 ms: 1.23x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.94 sec: 1.23x slower                                                     |
| raytrace                   | 156 ms                                                      | 198 ms: 1.26x slower                                                       |
| pylint                     | 211 ms                                                      | 269 ms: 1.28x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.87 ms: 1.32x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 19.7 ms: 1.33x slower                                                      |
| richards_super             | 29.3 ms                                                     | 39.3 ms: 1.34x slower                                                      |
| richards                   | 26.0 ms                                                     | 36.0 ms: 1.38x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 46.3 ms: 1.41x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, pycparser, bench_thread_pool, json_loads, scimark_lu, regex_effbot, json_dumps, python_startup
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown