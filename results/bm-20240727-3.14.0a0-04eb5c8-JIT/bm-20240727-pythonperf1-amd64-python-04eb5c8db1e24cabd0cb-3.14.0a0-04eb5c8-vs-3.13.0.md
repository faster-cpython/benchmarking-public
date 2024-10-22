# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.03x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.88 sec: 1.20x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.6 ms: 1.08x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 96.3 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 536 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.50 sec: 1.09x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.06x faster                                                       |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| async_tree_io              | 521 ms                                                      | 539 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 536 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 51.1 ms: 1.26x faster                                                      |
| float          | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| regex_dna      | 114 ms                                                      | 125 ms: 1.09x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.31 sec: 1.04x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 52.4 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.8 us: 1.03x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.08 ms: 1.06x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 135 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.19 ms: 1.20x faster                                                      |
| django_template | 21.8 ms                                                     | 26.2 ms: 1.20x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 46.7 ms: 1.43x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 523 us: 16.60x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 16.3 us: 1.34x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 46.8 ms: 1.26x faster                                                      |
| nbody                      | 64.5 ms                                                     | 51.1 ms: 1.26x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 536 ms: 1.22x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.19 ms: 1.20x faster                                                      |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                                       |
| scimark_fft                | 174 ms                                                      | 150 ms: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.09 ms: 1.12x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.50 sec: 1.09x faster                                                     |
| pyflate                    | 275 ms                                                      | 256 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.07x faster                                                      |
| float                      | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| fannkuch                   | 245 ms                                                      | 229 ms: 1.07x faster                                                       |
| pycparser                  | 758 ms                                                      | 709 ms: 1.07x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 40.6 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 38.2 ms: 1.05x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.31 sec: 1.04x faster                                                     |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 493 ms                                                      | 478 ms: 1.03x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.72 ms: 1.03x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 52.4 ms: 1.02x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| comprehensions             | 10.2 us                                                     | 10.5 us: 1.03x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.60 ms: 1.03x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.8 us: 1.03x slower                                                      |
| async_tree_io              | 521 ms                                                      | 539 ms: 1.03x slower                                                       |
| coverage                   | 46.7 ms                                                     | 48.4 ms: 1.04x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 96.3 ms: 1.04x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| pathlib                    | 81.2 ms                                                     | 84.7 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 536 ms: 1.05x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 42.4 ms: 1.05x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 73.2 ms: 1.05x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| json                       | 2.98 ms                                                     | 3.14 ms: 1.05x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.08 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 135 us: 1.06x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.13 us: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                      |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 41.6 ms: 1.08x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.69 us: 1.09x slower                                                      |
| regex_dna                  | 114 ms                                                      | 125 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 835 us: 1.10x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 62.1 ms: 1.12x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.55 sec: 1.12x slower                                                     |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 935 us: 1.13x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.08 ms: 1.13x slower                                                      |
| sympy_str                  | 166 ms                                                      | 189 ms: 1.14x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 98.7 ms: 1.14x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 37.8 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| sympy_expand               | 285 ms                                                      | 329 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 201 ms: 1.17x slower                                                       |
| richards                   | 26.0 ms                                                     | 30.9 ms: 1.19x slower                                                      |
| go                         | 84.6 ms                                                     | 101 ms: 1.19x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 14.7 ms: 1.20x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.88 sec: 1.20x slower                                                     |
| richards_super             | 29.3 ms                                                     | 35.1 ms: 1.20x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 120 us: 1.20x slower                                                       |
| django_template            | 21.8 ms                                                     | 26.2 ms: 1.20x slower                                                      |
| pylint                     | 211 ms                                                      | 255 ms: 1.21x slower                                                       |
| raytrace                   | 156 ms                                                      | 192 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.34 ms: 1.26x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 90.5 ms: 1.26x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 18.9 ms: 1.27x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.74 ms: 1.28x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 75.9 ms: 1.40x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 46.7 ms: 1.43x slower                                                      |
| bench_thread_pool          | 828 us                                                      | 3.06 ms: 3.69x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (5): async_tree_memoization, xml_etree_parse, pprint_pformat, pickle_pure_python, meteor_contest
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown