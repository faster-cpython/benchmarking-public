# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-amd64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 223 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.2 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 526 ms: 1.24x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 82.0 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.27 us: 1.01x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.7 us: 1.02x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.7 ms: 1.04x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.04 us: 1.05x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.9 us: 1.05x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.19 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.6 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 213 us: 1.16x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 148 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.7 ms: 1.09x slower                                                      |
| mako            | 6.24 ms                                                     | 7.03 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                                      |
| django_template | 21.8 ms                                                     | 25.1 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.52x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 526 ms: 1.24x faster                                                       |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.05x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.9 us: 1.04x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 802 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| unpack_sequence            | 40.0 ns                                                     | 39.3 ns: 1.02x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.0 ms: 1.01x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 68.8 ms: 1.01x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.27 us: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.54 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.89 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| go                         | 84.6 ms                                                     | 85.9 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.02x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.7 us: 1.02x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| 2to3                       | 217 ms                                                      | 223 ms: 1.03x slower                                                       |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.7 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.1 ms: 1.04x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| unpickle                   | 8.63 us                                                     | 9.04 us: 1.05x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 18.9 us: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| meteor_contest             | 72.3 ms                                                     | 77.4 ms: 1.07x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 890 us: 1.07x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.19 ms: 1.07x slower                                                      |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.07x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 43.5 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.6 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                      |
| sympy_expand               | 285 ms                                                      | 310 ms: 1.09x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 35.7 ms: 1.09x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 42.2 ms: 1.09x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.73 us: 1.09x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.29 us: 1.10x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 565 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 546 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.03 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| regex_compile              | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.6 ms: 1.15x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.1 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 213 us: 1.16x slower                                                       |
| float                      | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 885 us: 1.16x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 64.7 ms: 1.17x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 148 us: 1.17x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 50.2 ms: 1.17x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.75 ms: 1.18x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 63.7 ms: 1.18x slower                                                      |
| pyflate                    | 275 ms                                                      | 328 ms: 1.19x slower                                                       |
| scimark_fft                | 174 ms                                                      | 209 ms: 1.20x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.43 ms: 1.20x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 71.5 ms: 1.21x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 62.3 ns: 1.22x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.23x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.0 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.5 ms: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.24x slower                                                      |
| fannkuch                   | 245 ms                                                      | 305 ms: 1.25x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 91.3 ms: 1.27x slower                                                      |
| nbody                      | 64.5 ms                                                     | 82.0 ms: 1.27x slower                                                      |
| raytrace                   | 156 ms                                                      | 201 ms: 1.29x slower                                                       |
| json                       | 2.98 ms                                                     | 4.33 ms: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (9): pycparser, asyncio_tcp_ssl, async_tree_none_tg, tornado_http, python_startup_no_site, regex_v8, async_tree_cpu_io_mixed, pickle_list, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown