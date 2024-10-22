# Results vs. 3.13.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 39fa464
- commit date: 2024-07-19
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 91.5 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 525 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 243 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 187 ms: 1.10x faster                                                       |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 252 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 380 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.74 sec: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 64.5 ms                                                     | 68.8 ms: 1.07x slower                                                      |
| float          | 48.1 ms                                                     | 54.0 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 80.1 ms                                                     | 83.8 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.87 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.6 ms: 1.02x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 55.2 ms: 1.03x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.0 ms: 1.04x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 134 us: 1.06x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.46 sec: 1.07x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 198 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 34.0 ms: 1.04x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 15.6 ms: 1.05x slower                                                      |
| django_template | 21.8 ms                                                     | 23.0 ms: 1.05x slower                                                      |
| mako            | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 507 us: 17.10x faster                                                      |
| deepcopy                   | 223 us                                                      | 174 us: 1.28x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 525 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 243 ms: 1.19x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 18.9 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.13x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 187 ms: 1.10x faster                                                       |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 252 ms: 1.08x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 791 us: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 67.8 ms: 1.03x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.74 ms: 1.02x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 380 ms: 1.02x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 91.5 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.5 ms: 1.01x faster                                                      |
| sympy_sum                  | 86.4 ms                                                     | 87.5 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 73.4 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 5.87 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 33.7 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.6 ms: 1.02x slower                                                      |
| sympy_expand               | 285 ms                                                      | 292 ms: 1.02x slower                                                       |
| sympy_str                  | 166 ms                                                      | 171 ms: 1.03x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.03x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 55.2 ms: 1.03x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 56.0 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 34.0 ms: 1.04x slower                                                      |
| logging_simple             | 5.72 us                                                     | 5.95 us: 1.04x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.40 us: 1.04x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.0 ms: 1.04x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 83.8 ms: 1.05x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 179 ms: 1.05x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 1.95 ms: 1.05x slower                                                      |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 15.6 ms: 1.05x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| go                         | 84.6 ms                                                     | 88.7 ms: 1.05x slower                                                      |
| raytrace                   | 156 ms                                                      | 164 ms: 1.05x slower                                                       |
| django_template            | 21.8 ms                                                     | 23.0 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 134 us: 1.06x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| pyflate                    | 275 ms                                                      | 293 ms: 1.06x slower                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.74 sec: 1.06x slower                                                     |
| hexiom                     | 3.69 ms                                                     | 3.93 ms: 1.06x slower                                                      |
| nbody                      | 64.5 ms                                                     | 68.8 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 107 us: 1.07x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 45.9 ms: 1.07x slower                                                      |
| scimark_fft                | 174 ms                                                      | 187 ms: 1.07x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.46 sec: 1.07x slower                                                     |
| comprehensions             | 10.2 us                                                     | 11.0 us: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.52 ms: 1.08x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 198 us: 1.08x slower                                                       |
| richards                   | 26.0 ms                                                     | 28.3 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 535 ms: 1.09x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.08 sec: 1.09x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 830 us: 1.09x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.04 ms: 1.09x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 905 us: 1.09x slower                                                       |
| richards_super             | 29.3 ms                                                     | 32.0 ms: 1.09x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 78.9 ms: 1.10x slower                                                      |
| fannkuch                   | 245 ms                                                      | 269 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 44.2 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.88 ms: 1.10x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 65.4 ms: 1.10x slower                                                      |
| float                      | 48.1 ms                                                     | 54.0 ms: 1.12x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 58.2 ns: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (13): pycparser, pylint, xml_etree_parse, gc_traversal, mdp, json, 2to3, generators, html5lib, python_startup_no_site, async_tree_io, async_tree_io_tg, regex_v8
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown