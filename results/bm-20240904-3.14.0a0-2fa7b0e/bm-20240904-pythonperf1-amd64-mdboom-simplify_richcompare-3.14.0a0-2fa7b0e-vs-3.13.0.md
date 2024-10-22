# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 522 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 567 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 56.7 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 88.1 ms: 1.37x slower                                                      |
| Geometric mean | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.5 ms: 1.01x faster                                                      |
| regex_dna      | 114 ms                                                      | 115 ms: 1.01x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.6 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.6 ms: 1.08x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 212 us: 1.16x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 155 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 7.04 ms: 1.13x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| django_template | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.72x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 522 ms: 1.25x faster                                                       |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.7 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.5 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.56 ms: 1.00x slower                                                      |
| regex_dna                  | 114 ms                                                      | 115 ms: 1.01x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 70.3 ms: 1.01x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| coverage                   | 46.7 ms                                                     | 48.4 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.0 ms: 1.04x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| go                         | 84.6 ms                                                     | 88.6 ms: 1.05x slower                                                      |
| 2to3                       | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 42.4 ms: 1.05x slower                                                      |
| json                       | 2.98 ms                                                     | 3.14 ms: 1.05x slower                                                      |
| sympy_expand               | 285 ms                                                      | 303 ms: 1.06x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.06x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.16 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 57.6 ms: 1.08x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.7 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.09x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.8 ms: 1.09x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.51 sec: 1.09x slower                                                     |
| logging_format             | 6.15 us                                                     | 6.79 us: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 567 ms: 1.11x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 917 us: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 577 ms: 1.11x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.37 us: 1.11x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.04 ms: 1.13x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.13x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 563 ms: 1.14x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 91.6 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.69 ms: 1.15x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 64.1 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.15x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 212 us: 1.16x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                     |
| crypto_pyaes               | 42.8 ms                                                     | 49.8 ms: 1.16x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.2 ms: 1.17x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 63.1 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 892 us: 1.17x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                                      |
| float                      | 48.1 ms                                                     | 56.7 ms: 1.18x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.1 us: 1.18x slower                                                      |
| pyflate                    | 275 ms                                                      | 326 ms: 1.19x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                      |
| scimark_fft                | 174 ms                                                      | 211 ms: 1.21x slower                                                       |
| raytrace                   | 156 ms                                                      | 190 ms: 1.22x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 155 us: 1.22x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.56 ms: 1.24x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.3 ms: 1.24x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 73.9 ms: 1.25x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.7 ms: 1.25x slower                                                      |
| fannkuch                   | 245 ms                                                      | 307 ms: 1.25x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 64.4 ns: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.9 ms: 1.26x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 92.7 ms: 1.29x slower                                                      |
| nbody                      | 64.5 ms                                                     | 88.1 ms: 1.37x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (9): async_tree_memoization, asyncio_tcp_ssl, bench_thread_pool, python_startup, async_tree_none_tg, xml_etree_parse, tornado_http, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown