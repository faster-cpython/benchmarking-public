# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 230 ms: 1.06x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 536 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 402 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 569 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 58.6 ms: 1.22x slower                                                      |
| nbody          | 64.5 ms                                                     | 87.8 ms: 1.36x slower                                                      |
| Geometric mean | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 15.9 ms: 1.08x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 92.4 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.32 ms: 1.10x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 214 us: 1.17x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 155 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.4 ms: 1.01x slower                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| mako            | 6.24 ms                                                     | 7.12 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.2 ms: 1.16x slower                                                      |
| django_template | 21.8 ms                                                     | 25.5 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 521 us: 16.66x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 536 ms: 1.22x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 211 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.2 us: 1.03x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.6 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 69.0 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| python_startup             | 22.2 ms                                                     | 22.4 ms: 1.01x slower                                                      |
| json                       | 2.98 ms                                                     | 3.03 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 39.7 ms: 1.03x slower                                                      |
| go                         | 84.6 ms                                                     | 88.1 ms: 1.04x slower                                                      |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| 2to3                       | 217 ms                                                      | 230 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.9 ms: 1.06x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.9 ms: 1.07x slower                                                      |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| sympy_expand               | 285 ms                                                      | 305 ms: 1.07x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.20 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 402 ms: 1.07x slower                                                       |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.9 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.09x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.32 ms: 1.10x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 79.5 ms: 1.10x slower                                                      |
| pycparser                  | 758 ms                                                      | 839 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.6 ms: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 919 us: 1.11x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 569 ms: 1.11x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.85 us: 1.11x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.12x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.48 us: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 194 ms: 1.13x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.12 ms: 1.14x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 49.3 ms: 1.15x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 92.4 ms: 1.15x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 569 ms: 1.15x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 17.2 ms: 1.16x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                     |
| nqueens                    | 55.5 ms                                                     | 64.7 ms: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 214 us: 1.17x slower                                                       |
| django_template            | 21.8 ms                                                     | 25.5 ms: 1.17x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.4 ms: 1.17x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.1 us: 1.18x slower                                                      |
| pyflate                    | 275 ms                                                      | 327 ms: 1.19x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.19x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 910 us: 1.20x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 65.3 ms: 1.21x slower                                                      |
| float                      | 48.1 ms                                                     | 58.6 ms: 1.22x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 72.2 ms: 1.22x slower                                                      |
| fannkuch                   | 245 ms                                                      | 300 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.23x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.52 ms: 1.23x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 155 us: 1.23x slower                                                       |
| scimark_fft                | 174 ms                                                      | 214 ms: 1.23x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.92 ms: 1.25x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.5 ms: 1.25x slower                                                      |
| raytrace                   | 156 ms                                                      | 198 ms: 1.27x slower                                                       |
| richards_super             | 29.3 ms                                                     | 37.2 ms: 1.27x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 64.8 ns: 1.27x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.6 ms: 1.28x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 93.8 ms: 1.30x slower                                                      |
| nbody                      | 64.5 ms                                                     | 87.8 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (6): async_tree_memoization, asyncio_tcp_ssl, bench_thread_pool, async_tree_none_tg, tornado_http, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown