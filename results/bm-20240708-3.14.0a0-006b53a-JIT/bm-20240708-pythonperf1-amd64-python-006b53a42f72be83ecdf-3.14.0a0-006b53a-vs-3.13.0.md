# Results vs. 3.13.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.02x faster
- HPT reliability: 91.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 232 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 83.8 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 243 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.41 sec: 1.16x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 185 ms: 1.11x faster                                                       |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 381 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 383 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 53.4 ms: 1.21x faster                                                      |
| float          | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_dna      | 114 ms                                                      | 122 ms: 1.06x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.1 ms: 1.10x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 89.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| pickle_pure_python   | 183 us                                                      | 174 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 52.2 ms: 1.02x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.79 ms: 1.01x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 130 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.0 ms: 1.05x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.17 ms: 1.21x faster                                                      |
| django_template | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 46.9 ms: 1.43x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 513 us: 16.92x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.5 us: 1.41x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.41x faster                                                       |
| spectral_norm              | 59.2 ms                                                     | 44.5 ms: 1.33x faster                                                      |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                       |
| nbody                      | 64.5 ms                                                     | 53.4 ms: 1.21x faster                                                      |
| mako                       | 6.24 ms                                                     | 5.17 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 243 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.41 sec: 1.16x faster                                                     |
| scimark_fft                | 174 ms                                                      | 150 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.76 us: 1.15x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 185 ms: 1.11x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| tornado_http               | 92.8 ms                                                     | 83.8 ms: 1.11x faster                                                      |
| fannkuch                   | 245 ms                                                      | 222 ms: 1.10x faster                                                       |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.49 ms: 1.08x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 75.5 ms: 1.08x faster                                                      |
| pyflate                    | 275 ms                                                      | 256 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.6 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.18 ms: 1.07x faster                                                      |
| float                      | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 40.2 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 464 ms: 1.06x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.0 ms: 1.05x faster                                                      |
| pickle_pure_python         | 183 us                                                      | 174 us: 1.05x faster                                                       |
| pprint_pformat             | 991 ms                                                      | 950 ms: 1.04x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 797 us: 1.04x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 52.2 ms: 1.02x faster                                                      |
| logging_simple             | 5.72 us                                                     | 5.63 us: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 381 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| logging_format             | 6.15 us                                                     | 6.08 us: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 69.2 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.5 ms: 1.00x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.79 ms: 1.01x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 73.2 ms: 1.01x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 383 ms: 1.02x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.8 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 130 us: 1.03x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 800 us: 1.05x slower                                                       |
| regex_dna                  | 114 ms                                                      | 122 ms: 1.06x slower                                                       |
| 2to3                       | 217 ms                                                      | 232 ms: 1.07x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 92.6 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.5 ms: 1.07x slower                                                      |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.03 ms: 1.08x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 898 us: 1.08x slower                                                       |
| sympy_expand               | 285 ms                                                      | 310 ms: 1.09x slower                                                       |
| pylint                     | 211 ms                                                      | 229 ms: 1.09x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 60.5 ms: 1.09x slower                                                      |
| go                         | 84.6 ms                                                     | 93.0 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 188 ms: 1.10x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 16.1 ms: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.10x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 56.5 ns: 1.11x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 89.1 ms: 1.11x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.13x slower                                                      |
| raytrace                   | 156 ms                                                      | 176 ms: 1.13x slower                                                       |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.14x slower                                                       |
| richards                   | 26.0 ms                                                     | 29.8 ms: 1.15x slower                                                      |
| richards_super             | 29.3 ms                                                     | 33.6 ms: 1.15x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 86.5 ms: 1.20x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                      |
| generators                 | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.61 ms: 1.25x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 74.6 ms: 1.38x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 46.9 ms: 1.43x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (8): pidigits, comprehensions, gc_traversal, html5lib, async_tree_io, async_tree_io_tg, json, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 91.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown