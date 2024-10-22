# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.5 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 532 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 558 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 572 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 56.5 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 80.9 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.4 us: 1.00x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.5 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 210 us: 1.15x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 148 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.7 ms: 1.09x slower                                                      |
| mako            | 6.24 ms                                                     | 6.92 ms: 1.11x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                      |
| django_template | 21.8 ms                                                     | 24.9 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 522 us: 16.62x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 532 ms: 1.23x faster                                                       |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 19.9 us: 1.10x faster                                                      |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 78.8 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 68.5 ms: 1.02x faster                                                      |
| python_startup             | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.4 us: 1.00x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.03 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.9 ms: 1.04x slower                                                      |
| json                       | 2.98 ms                                                     | 3.10 ms: 1.04x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.7 ms: 1.04x slower                                                      |
| 2to3                       | 217 ms                                                      | 227 ms: 1.04x slower                                                       |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.5 ms: 1.05x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.8 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.06x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 77.0 ms: 1.07x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| sympy_expand               | 285 ms                                                      | 305 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                      |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 558 ms: 1.09x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 35.7 ms: 1.09x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 908 us: 1.10x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 58.5 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 572 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 543 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.82 us: 1.11x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.11x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.92 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 190 ms: 1.11x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.38 us: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 47.9 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| mdp                        | 1.38 sec                                                    | 1.56 sec: 1.13x slower                                                     |
| chaos                      | 37.9 ms                                                     | 42.8 ms: 1.13x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 67.1 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.9 ms: 1.15x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 210 us: 1.15x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.70 ms: 1.15x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 64.0 ms: 1.15x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 62.6 ms: 1.16x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.16x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 884 us: 1.16x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.32 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 148 us: 1.17x slower                                                       |
| pyflate                    | 275 ms                                                      | 323 ms: 1.17x slower                                                       |
| float                      | 48.1 ms                                                     | 56.5 ms: 1.18x slower                                                      |
| fannkuch                   | 245 ms                                                      | 288 ms: 1.18x slower                                                       |
| scimark_fft                | 174 ms                                                      | 207 ms: 1.19x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.23 ms: 1.20x slower                                                      |
| richards                   | 26.0 ms                                                     | 31.6 ms: 1.21x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 87.7 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.2 ms: 1.22x slower                                                      |
| raytrace                   | 156 ms                                                      | 191 ms: 1.22x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 62.7 ns: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.1 ms: 1.23x slower                                                      |
| nbody                      | 64.5 ms                                                     | 80.9 ms: 1.26x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, async_tree_none_tg, pycparser, bench_thread_pool, go, gc_traversal, tornado_http, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown