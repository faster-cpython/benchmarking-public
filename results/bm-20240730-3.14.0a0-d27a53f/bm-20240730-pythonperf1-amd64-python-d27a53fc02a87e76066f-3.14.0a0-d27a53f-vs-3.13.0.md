# Results vs. 3.13.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-amd64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| html5lib       | 38.6 ms                                                     | 43.1 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 538 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 551 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 59.7 ms: 1.24x slower                                                      |
| nbody          | 64.5 ms                                                     | 86.7 ms: 1.34x slower                                                      |
| Geometric mean | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 93.3 ms: 1.16x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 17.4 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.1 us: 1.02x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 215 us: 1.17x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.61 sec: 1.19x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 152 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.8 ms: 1.02x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 7.08 ms: 1.13x slower                                                      |
| django_template | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 38.1 ms: 1.16x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 529 us: 16.39x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 538 ms: 1.22x faster                                                       |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.9 us: 1.05x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 804 us: 1.03x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.8 ms: 1.02x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 47.2 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 95.0 ms: 1.02x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.98 ms: 1.03x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| json                       | 2.98 ms                                                     | 3.11 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.5 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.48 sec: 1.07x slower                                                     |
| meteor_contest             | 72.3 ms                                                     | 77.3 ms: 1.07x slower                                                      |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 551 ms: 1.08x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 893 us: 1.08x slower                                                       |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                                       |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.09x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                      |
| sympy_expand               | 285 ms                                                      | 311 ms: 1.09x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 44.1 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                      |
| pycparser                  | 758 ms                                                      | 833 ms: 1.10x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 61.6 ms: 1.11x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 36.7 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.85 us: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 43.1 ms: 1.12x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.44 us: 1.12x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.13x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.08 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| django_template            | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 571 ms: 1.16x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 38.1 ms: 1.16x slower                                                      |
| pyflate                    | 275 ms                                                      | 320 ms: 1.16x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 93.3 ms: 1.16x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.3 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.17x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.16 sec: 1.17x slower                                                     |
| pickle_pure_python         | 183 us                                                      | 215 us: 1.17x slower                                                       |
| go                         | 84.6 ms                                                     | 99.7 ms: 1.18x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 899 us: 1.18x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.1 us: 1.18x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.61 sec: 1.19x slower                                                     |
| regex_v8                   | 14.7 ms                                                     | 17.4 ms: 1.19x slower                                                      |
| fannkuch                   | 245 ms                                                      | 292 ms: 1.19x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 152 us: 1.20x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 64.9 ms: 1.20x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 51.5 ms: 1.20x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 71.3 ms: 1.20x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.49 ms: 1.22x slower                                                      |
| scimark_fft                | 174 ms                                                      | 213 ms: 1.22x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 62.8 ns: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.4 ms: 1.24x slower                                                      |
| float                      | 48.1 ms                                                     | 59.7 ms: 1.24x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.91 ms: 1.24x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.4 ms: 1.24x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 89.7 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.6 ms: 1.26x slower                                                      |
| raytrace                   | 156 ms                                                      | 197 ms: 1.26x slower                                                       |
| nbody                      | 64.5 ms                                                     | 86.7 ms: 1.34x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none, pathlib, gc_traversal, bench_mp_pool, async_tree_cpu_io_mixed, tornado_http, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown