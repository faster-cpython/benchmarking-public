# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 529 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 401 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 579 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 82.8 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 15.7 ms: 1.07x slower                                                      |
| regex_dna      | 114 ms                                                      | 123 ms: 1.08x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.9 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.25 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.5 ms: 1.11x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 210 us: 1.15x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.1 ms: 1.10x slower                                                      |
| mako            | 6.24 ms                                                     | 6.90 ms: 1.11x slower                                                      |
| django_template | 21.8 ms                                                     | 24.3 ms: 1.12x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.9 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 514 us: 16.90x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 529 ms: 1.24x faster                                                       |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.0 us: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| go                         | 84.6 ms                                                     | 85.1 ms: 1.01x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 70.6 ms: 1.01x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.2 ms: 1.02x slower                                                      |
| json                       | 2.98 ms                                                     | 3.07 ms: 1.03x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.6 ms: 1.04x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.7 ms: 1.04x slower                                                      |
| 2to3                       | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 42.5 ms: 1.05x slower                                                      |
| sympy_str                  | 166 ms                                                      | 176 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| sympy_expand               | 285 ms                                                      | 303 ms: 1.06x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.7 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 401 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| regex_dna                  | 114 ms                                                      | 123 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.9 ms: 1.08x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| json_dumps                 | 5.76 ms                                                     | 6.25 ms: 1.09x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.5 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.30 ms: 1.09x slower                                                      |
| pycparser                  | 758 ms                                                      | 833 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 36.1 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.90 ms: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 917 us: 1.11x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.5 ms: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 579 ms: 1.11x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 66.0 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                       |
| django_template            | 21.8 ms                                                     | 24.3 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 551 ms: 1.12x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.91 us: 1.12x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.45 us: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.63 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.8 ms: 1.13x slower                                                      |
| scimark_fft                | 174 ms                                                      | 197 ms: 1.13x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 61.2 ms: 1.13x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 48.5 ms: 1.13x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 90.9 ms: 1.13x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.9 ms: 1.13x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 210 us: 1.15x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 886 us: 1.16x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.17x slower                                                      |
| pyflate                    | 275 ms                                                      | 321 ms: 1.17x slower                                                       |
| fannkuch                   | 245 ms                                                      | 288 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.18x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.37 ms: 1.18x slower                                                      |
| raytrace                   | 156 ms                                                      | 185 ms: 1.19x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.0 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 31.8 ms: 1.22x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.0 ms: 1.23x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 89.4 ms: 1.24x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.7 ns: 1.25x slower                                                      |
| nbody                      | 64.5 ms                                                     | 82.8 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (8): async_tree_none_tg, bench_thread_pool, gc_traversal, tornado_http, python_startup, async_tree_cpu_io_mixed, asyncio_tcp_ssl, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown