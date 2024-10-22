# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 220 ms: 1.02x slower                                                      |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                    |
| html5lib       | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 83.5 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 462 ms: 1.42x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                      |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 571 ms: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                              |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                      |
| float          | 48.1 ms                                                     | 54.2 ms: 1.13x slower                                                     |
| nbody          | 64.5 ms                                                     | 82.1 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                       | 1.13x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                     |
| regex_v8       | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                                     |
| regex_dna      | 114 ms                                                      | 114 ms: 1.01x faster                                                      |
| regex_compile  | 80.1 ms                                                     | 89.2 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.15 us: 1.03x faster                                                     |
| xml_etree_parse      | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                     |
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.5 ms: 1.04x slower                                                     |
| pickle_dict          | 18.0 us                                                     | 19.2 us: 1.06x slower                                                     |
| json_dumps           | 5.76 ms                                                     | 6.14 ms: 1.07x slower                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                     |
| unpickle             | 8.63 us                                                     | 9.50 us: 1.10x slower                                                     |
| xml_etree_process    | 36.5 ms                                                     | 40.3 ms: 1.10x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 207 us: 1.13x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.55 sec: 1.14x slower                                                    |
| unpickle_pure_python | 127 us                                                      | 147 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                              |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                     |
| python_startup_no_site | 17.8 ms                                                     | 17.3 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.84 ms: 1.10x slower                                                     |
| genshi_xml      | 32.8 ms                                                     | 36.7 ms: 1.12x slower                                                     |
| django_template | 21.8 ms                                                     | 24.4 ms: 1.12x slower                                                     |
| genshi_text     | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 512 us: 16.94x faster                                                     |
| asyncio_tcp                | 654 ms                                                      | 462 ms: 1.42x faster                                                      |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 83.5 ms: 1.11x faster                                                     |
| pathlib                    | 81.2 ms                                                     | 74.2 ms: 1.09x faster                                                     |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.2 us: 1.08x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                     |
| python_startup             | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                     |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 67.4 ms: 1.03x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 807 us: 1.03x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.15 us: 1.03x faster                                                     |
| python_startup_no_site     | 17.8 ms                                                     | 17.3 ms: 1.03x faster                                                     |
| regex_v8                   | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                                     |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                     |
| xml_etree_parse            | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                     |
| regex_dna                  | 114 ms                                                      | 114 ms: 1.01x faster                                                      |
| mdp                        | 1.38 sec                                                    | 1.40 sec: 1.01x slower                                                    |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                     |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.01x slower                                                     |
| 2to3                       | 217 ms                                                      | 220 ms: 1.02x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.1 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.5 ms: 1.04x slower                                                     |
| html5lib                   | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                     |
| telco                      | 4.85 ms                                                     | 5.04 ms: 1.04x slower                                                     |
| dulwich_log                | 40.4 ms                                                     | 42.1 ms: 1.04x slower                                                     |
| sympy_str                  | 166 ms                                                      | 175 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                                     |
| pickle_dict                | 18.0 us                                                     | 19.2 us: 1.06x slower                                                     |
| json_dumps                 | 5.76 ms                                                     | 6.14 ms: 1.07x slower                                                     |
| sympy_expand               | 285 ms                                                      | 304 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                    |
| create_gc_cycles           | 829 us                                                      | 888 us: 1.07x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                     |
| unpack_sequence            | 40.0 ns                                                     | 43.2 ns: 1.08x slower                                                     |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.1 ms: 1.08x slower                                                     |
| logging_format             | 6.15 us                                                     | 6.67 us: 1.08x slower                                                     |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.09x slower                                                     |
| logging_simple             | 5.72 us                                                     | 6.24 us: 1.09x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 36.1 ms: 1.09x slower                                                     |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 571 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.84 ms: 1.10x slower                                                     |
| pprint_safe_repr           | 493 ms                                                      | 541 ms: 1.10x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.50 us: 1.10x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 40.3 ms: 1.10x slower                                                     |
| crypto_pyaes               | 42.8 ms                                                     | 47.2 ms: 1.10x slower                                                     |
| spectral_norm              | 59.2 ms                                                     | 65.3 ms: 1.10x slower                                                     |
| scimark_lu                 | 54.0 ms                                                     | 59.9 ms: 1.11x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 89.2 ms: 1.11x slower                                                     |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                    |
| genshi_xml                 | 32.8 ms                                                     | 36.7 ms: 1.12x slower                                                     |
| django_template            | 21.8 ms                                                     | 24.4 ms: 1.12x slower                                                     |
| comprehensions             | 10.2 us                                                     | 11.5 us: 1.12x slower                                                     |
| float                      | 48.1 ms                                                     | 54.2 ms: 1.13x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                     |
| pickle_pure_python         | 183 us                                                      | 207 us: 1.13x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.9 ms: 1.13x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                     |
| scimark_fft                | 174 ms                                                      | 199 ms: 1.14x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.55 sec: 1.14x slower                                                    |
| sqlglot_parse              | 761 us                                                      | 868 us: 1.14x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.67 ms: 1.14x slower                                                     |
| sqlglot_transpile          | 952 us                                                      | 1.09 ms: 1.14x slower                                                     |
| pyflate                    | 275 ms                                                      | 316 ms: 1.15x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 63.7 ms: 1.15x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 147 us: 1.16x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.33 ms: 1.17x slower                                                     |
| raytrace                   | 156 ms                                                      | 184 ms: 1.18x slower                                                      |
| fannkuch                   | 245 ms                                                      | 289 ms: 1.18x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.23 ms: 1.19x slower                                                     |
| scimark_sor                | 72.0 ms                                                     | 86.1 ms: 1.20x slower                                                     |
| richards_super             | 29.3 ms                                                     | 35.5 ms: 1.21x slower                                                     |
| logging_silent             | 51.0 ns                                                     | 61.7 ns: 1.21x slower                                                     |
| richards                   | 26.0 ms                                                     | 31.5 ms: 1.21x slower                                                     |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.1 ms: 1.22x slower                                                     |
| nbody                      | 64.5 ms                                                     | 82.1 ms: 1.27x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                              |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, pycparser, coverage, go, unpickle_list, pickle_list, json, async_tree_cpu_io_mixed, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown