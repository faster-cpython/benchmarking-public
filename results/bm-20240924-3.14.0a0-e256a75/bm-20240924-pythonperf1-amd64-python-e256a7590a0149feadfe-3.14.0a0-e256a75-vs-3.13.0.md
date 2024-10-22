# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 222 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.5 ms: 1.05x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 83.1 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 471 ms: 1.39x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.48 sec: 1.11x faster                                                     |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 388 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 553 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.2 ms: 1.15x slower                                                      |
| nbody          | 64.5 ms                                                     | 83.2 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.04 us: 1.04x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| unpickle_list        | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.9 ms: 1.03x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.8 us: 1.03x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.39 us: 1.09x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.35 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 212 us: 1.15x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.4 ms: 1.08x slower                                                      |
| mako            | 6.24 ms                                                     | 6.81 ms: 1.09x slower                                                      |
| django_template | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.0 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 523 us: 16.60x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 471 ms: 1.39x faster                                                       |
| deepcopy                   | 223 us                                                      | 193 us: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 83.1 ms: 1.12x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.48 sec: 1.11x faster                                                     |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 75.9 ms: 1.07x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 66.0 ms: 1.06x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.8 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.04 us: 1.04x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 802 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| unpack_sequence            | 40.0 ns                                                     | 40.3 ns: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.63 us: 1.02x slower                                                      |
| 2to3                       | 217 ms                                                      | 222 ms: 1.02x slower                                                       |
| go                         | 84.6 ms                                                     | 86.6 ms: 1.02x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.9 ms: 1.03x slower                                                      |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| json_loads                 | 14.3 us                                                     | 14.8 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 388 ms: 1.04x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.7 ms: 1.04x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| html5lib                   | 38.6 ms                                                     | 40.5 ms: 1.05x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.09 ms: 1.05x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.3 ms: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.8 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 176 ms: 1.06x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 884 us: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                                      |
| sympy_expand               | 285 ms                                                      | 306 ms: 1.07x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 553 ms: 1.08x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 35.4 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.08x slower                                                     |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                       |
| unpickle                   | 8.63 us                                                     | 9.39 us: 1.09x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.6 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.81 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.09x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 542 ms: 1.10x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.35 ms: 1.10x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.35 us: 1.11x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.85 us: 1.11x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 47.8 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.7 ms: 1.13x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.66 ms: 1.14x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                      |
| float                      | 48.1 ms                                                     | 55.2 ms: 1.15x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.0 ms: 1.15x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 212 us: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 62.5 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.16x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 888 us: 1.17x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| pyflate                    | 275 ms                                                      | 322 ms: 1.17x slower                                                       |
| scimark_fft                | 174 ms                                                      | 204 ms: 1.17x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.18x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 69.8 ms: 1.18x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 65.5 ms: 1.18x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.39 ms: 1.19x slower                                                      |
| raytrace                   | 156 ms                                                      | 189 ms: 1.21x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.0 ms: 1.22x slower                                                      |
| fannkuch                   | 245 ms                                                      | 299 ms: 1.22x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.3 ms: 1.24x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.4 ms: 1.24x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.8 ns: 1.25x slower                                                      |
| nbody                      | 64.5 ms                                                     | 83.2 ms: 1.29x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 93.1 ms: 1.29x slower                                                      |
| json                       | 2.98 ms                                                     | 4.50 ms: 1.51x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, pycparser, async_tree_cpu_io_mixed, regex_v8, python_startup, pickle_list, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown