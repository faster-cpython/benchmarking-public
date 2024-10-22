# Results vs. 3.13.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 8110f98
- commit date: 2024-07-19
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 222 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.66 sec: 1.05x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 91.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 522 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 247 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                       |
| async_tree_io              | 521 ms                                                      | 538 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 535 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.0 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 75.5 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 83.3 ms: 1.04x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                      | 127 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.95 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.2 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.5 ms: 1.08x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 199 us: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 145 us: 1.14x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                                      |
| django_template | 21.8 ms                                                     | 24.3 ms: 1.12x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.6 ms: 1.15x slower                                                      |
| mako            | 6.24 ms                                                     | 7.54 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 529 us: 16.40x faster                                                      |
| deepcopy                   | 223 us                                                      | 178 us: 1.26x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 522 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 247 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.3 us: 1.07x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 67.4 ms: 1.03x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 91.4 ms: 1.02x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.6 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.4 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.40 sec: 1.01x slower                                                     |
| sympy_expand               | 285 ms                                                      | 288 ms: 1.01x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| sympy_str                  | 166 ms                                                      | 169 ms: 1.01x slower                                                       |
| 2to3                       | 217 ms                                                      | 222 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 5.95 ms: 1.03x slower                                                      |
| async_tree_io              | 521 ms                                                      | 538 ms: 1.03x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 83.3 ms: 1.04x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 535 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 34.6 ms: 1.05x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.66 sec: 1.05x slower                                                     |
| go                         | 84.6 ms                                                     | 89.2 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.2 ms: 1.06x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 76.8 ms: 1.06x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 890 us: 1.07x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.5 ms: 1.08x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 185 ms: 1.08x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.66 us: 1.08x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.20 us: 1.08x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 199 us: 1.08x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 534 ms: 1.08x slower                                                       |
| richards_super             | 29.3 ms                                                     | 32.0 ms: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 78.9 ms: 1.10x slower                                                      |
| richards                   | 26.0 ms                                                     | 28.5 ms: 1.10x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.09 sec: 1.10x slower                                                     |
| pyflate                    | 275 ms                                                      | 302 ms: 1.10x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 61.2 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| raytrace                   | 156 ms                                                      | 173 ms: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.9 ms: 1.11x slower                                                      |
| regex_dna                  | 114 ms                                                      | 127 ms: 1.11x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.3 ms: 1.12x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.08 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.13 ms: 1.12x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.5 us: 1.13x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 66.7 ms: 1.13x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 861 us: 1.13x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.08 ms: 1.13x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 145 us: 1.14x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 37.6 ms: 1.15x slower                                                      |
| fannkuch                   | 245 ms                                                      | 282 ms: 1.15x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 62.2 ms: 1.15x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 49.5 ms: 1.16x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 46.6 ms: 1.16x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| float                      | 48.1 ms                                                     | 56.0 ms: 1.16x slower                                                      |
| scimark_fft                | 174 ms                                                      | 204 ms: 1.17x slower                                                       |
| nbody                      | 64.5 ms                                                     | 75.5 ms: 1.17x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 60.6 ns: 1.19x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.54 ms: 1.21x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.86 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (12): asyncio_tcp_ssl, bench_thread_pool, async_tree_cpu_io_mixed, html5lib, pycparser, python_startup_no_site, pylint, gc_traversal, regex_effbot, sympy_sum, xml_etree_parse, json
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown