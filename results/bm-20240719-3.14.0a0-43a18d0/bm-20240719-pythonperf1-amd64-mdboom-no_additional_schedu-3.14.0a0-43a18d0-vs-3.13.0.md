# Results vs. 3.13.0

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 43a18d0
- commit date: 2024-07-19
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 91.8 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 517 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 246 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 538 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.7 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 77.8 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.7 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 89.7 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 94.2 ms: 1.01x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.13 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.3 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.57 sec: 1.16x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 213 us: 1.16x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 152 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.9 ms: 1.10x slower                                                      |
| django_template | 21.8 ms                                                     | 24.1 ms: 1.11x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.6 ms: 1.12x slower                                                      |
| mako            | 6.24 ms                                                     | 7.52 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 533 us: 16.27x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 517 ms: 1.26x faster                                                       |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 246 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                      |
| coverage                   | 46.7 ms                                                     | 44.9 ms: 1.04x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 800 us: 1.03x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 67.6 ms: 1.03x faster                                                      |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 91.8 ms: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.7 us: 1.00x faster                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.7 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 94.2 ms: 1.01x slower                                                      |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| json_loads                 | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| sympy_sum                  | 86.4 ms                                                     | 88.2 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| 2to3                       | 217 ms                                                      | 226 ms: 1.04x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| sympy_str                  | 166 ms                                                      | 173 ms: 1.04x slower                                                       |
| json                       | 2.98 ms                                                     | 3.11 ms: 1.04x slower                                                      |
| sympy_expand               | 285 ms                                                      | 298 ms: 1.04x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 75.5 ms: 1.04x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 538 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.1 ms: 1.06x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.13 ms: 1.06x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| create_gc_cycles           | 829 us                                                      | 897 us: 1.08x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.67 us: 1.08x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.23 us: 1.09x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 187 ms: 1.09x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 58.3 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                       |
| pycparser                  | 758 ms                                                      | 830 ms: 1.10x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 35.9 ms: 1.10x slower                                                      |
| go                         | 84.6 ms                                                     | 93.0 ms: 1.10x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 61.2 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| django_template            | 21.8 ms                                                     | 24.1 ms: 1.11x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.6 ms: 1.12x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 89.7 ms: 1.12x slower                                                      |
| raytrace                   | 156 ms                                                      | 176 ms: 1.12x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 557 ms: 1.13x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| pyflate                    | 275 ms                                                      | 313 ms: 1.13x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.3 ms: 1.14x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.14 ms: 1.15x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.57 sec: 1.16x slower                                                     |
| scimark_sor                | 72.0 ms                                                     | 83.2 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 213 us: 1.16x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 891 us: 1.17x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.34 ms: 1.18x slower                                                      |
| float                      | 48.1 ms                                                     | 56.7 ms: 1.18x slower                                                      |
| richards                   | 26.0 ms                                                     | 30.8 ms: 1.18x slower                                                      |
| fannkuch                   | 245 ms                                                      | 290 ms: 1.18x slower                                                       |
| richards_super             | 29.3 ms                                                     | 34.8 ms: 1.19x slower                                                      |
| scimark_fft                | 174 ms                                                      | 207 ms: 1.19x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 51.2 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 152 us: 1.20x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.52 ms: 1.21x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.6 ms: 1.21x slower                                                      |
| nbody                      | 64.5 ms                                                     | 77.8 ms: 1.21x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.84 ms: 1.21x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 72.0 ms: 1.22x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 62.7 ns: 1.23x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 67.2 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, pylint, gc_traversal, python_startup_no_site, telco, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown