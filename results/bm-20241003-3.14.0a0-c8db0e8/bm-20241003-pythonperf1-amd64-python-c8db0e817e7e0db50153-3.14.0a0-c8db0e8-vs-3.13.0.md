# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-amd64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 43.0 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.50 sec: 1.09x faster                                                     |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.9 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 87.6 ms: 1.36x slower                                                      |
| Geometric mean | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 93.0 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.52 us: 1.10x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.5 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 218 us: 1.19x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 155 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (3): json_loads, pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| mako            | 6.24 ms                                                     | 7.23 ms: 1.16x slower                                                      |
| django_template | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 527 us: 16.47x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.23x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.50 sec: 1.09x faster                                                     |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.01x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.5 us: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| pickle_dict                | 18.0 us                                                     | 18.3 us: 1.02x slower                                                      |
| python_startup             | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.9 ms: 1.03x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.64 us: 1.03x slower                                                      |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 72.5 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.4 ms: 1.05x slower                                                      |
| 2to3                       | 217 ms                                                      | 228 ms: 1.05x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                                      |
| go                         | 84.6 ms                                                     | 88.9 ms: 1.05x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 884 us: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 400 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 42.8 ns: 1.07x slower                                                      |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 43.7 ms: 1.08x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.52 sec: 1.10x slower                                                     |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.10x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 79.5 ms: 1.10x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.52 us: 1.10x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.84 us: 1.11x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.8 ms: 1.11x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 43.0 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 59.5 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 554 ms: 1.13x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.47 us: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.14 sec: 1.15x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.23 ms: 1.16x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 93.0 ms: 1.16x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 65.5 ms: 1.18x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.8 ms: 1.18x slower                                                      |
| float                      | 48.1 ms                                                     | 56.9 ms: 1.18x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 50.9 ms: 1.19x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.19x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 218 us: 1.19x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| pyflate                    | 275 ms                                                      | 329 ms: 1.19x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 908 us: 1.19x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.3 us: 1.20x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.84 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 155 us: 1.22x slower                                                       |
| scimark_fft                | 174 ms                                                      | 214 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.31 ms: 1.24x slower                                                      |
| fannkuch                   | 245 ms                                                      | 307 ms: 1.25x slower                                                       |
| richards                   | 26.0 ms                                                     | 32.6 ms: 1.25x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.8 ms: 1.25x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.63 ms: 1.25x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 67.9 ms: 1.26x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 74.9 ms: 1.26x slower                                                      |
| raytrace                   | 156 ms                                                      | 198 ms: 1.27x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.3 ms: 1.27x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 65.9 ns: 1.29x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 96.2 ms: 1.34x slower                                                      |
| nbody                      | 64.5 ms                                                     | 87.6 ms: 1.36x slower                                                      |
| json                       | 2.98 ms                                                     | 4.15 ms: 1.39x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (9): async_tree_none_tg, json_loads, pycparser, bench_thread_pool, pickle_list, tornado_http, async_tree_cpu_io_mixed, pickle, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown