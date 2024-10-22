# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 525 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                       |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_tree_io              | 521 ms                                                      | 613 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 57.2 ms: 1.19x slower                                                      |
| nbody          | 64.5 ms                                                     | 84.6 ms: 1.31x slower                                                      |
| Geometric mean | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| pickle               | 7.34 us                                                     | 7.44 us: 1.01x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.78 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.3 ms: 1.05x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 19.0 us: 1.05x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.21 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.4 ms: 1.10x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.64 us: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 213 us: 1.16x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 150 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| django_template | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 515 us: 16.85x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 525 ms: 1.24x faster                                                       |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.3 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                       |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 67.8 ms: 1.03x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| unpack_sequence            | 40.0 ns                                                     | 40.3 ns: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| pickle                     | 7.34 us                                                     | 7.44 us: 1.01x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.02x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.78 us: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| go                         | 84.6 ms                                                     | 86.9 ms: 1.03x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.6 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| 2to3                       | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.3 ms: 1.05x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 19.0 us: 1.05x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.12 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.06x slower                                                       |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| json                       | 2.98 ms                                                     | 3.16 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                                      |
| sympy_expand               | 285 ms                                                      | 307 ms: 1.08x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.21 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| logging_format             | 6.15 us                                                     | 6.64 us: 1.08x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 902 us: 1.09x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.23 us: 1.09x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 44.1 ms: 1.09x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 79.0 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.2 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 58.4 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 190 ms: 1.11x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 549 ms: 1.12x slower                                                       |
| unpickle                   | 8.63 us                                                     | 9.64 us: 1.12x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 47.8 ms: 1.12x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.0 ms: 1.14x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 213 us: 1.16x slower                                                       |
| pyflate                    | 275 ms                                                      | 321 ms: 1.16x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 69.0 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 892 us: 1.17x slower                                                       |
| async_tree_io              | 521 ms                                                      | 613 ms: 1.18x slower                                                       |
| scimark_fft                | 174 ms                                                      | 205 ms: 1.18x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 150 us: 1.18x slower                                                       |
| float                      | 48.1 ms                                                     | 57.2 ms: 1.19x slower                                                      |
| fannkuch                   | 245 ms                                                      | 291 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.79 ms: 1.19x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 64.7 ms: 1.20x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.50 ms: 1.22x slower                                                      |
| raytrace                   | 156 ms                                                      | 191 ms: 1.22x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 62.5 ns: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.1 ms: 1.23x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.1 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.4 ms: 1.25x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 91.5 ms: 1.27x slower                                                      |
| nbody                      | 64.5 ms                                                     | 84.6 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_cpu_io_mixed, bench_thread_pool, json_loads, gc_traversal, python_startup, tornado_http, pycparser, pickle_list, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown