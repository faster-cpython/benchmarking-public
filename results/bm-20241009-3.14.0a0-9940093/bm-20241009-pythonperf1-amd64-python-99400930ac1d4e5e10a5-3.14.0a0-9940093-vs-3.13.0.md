# Results vs. 3.13.0

- fork: python
- ref: 99400930ac1d4e5e10a5
- machine: windows-amd64
- commit hash: 9940093
- commit date: 2024-10-09
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 268 ms: 1.07x faster                                                       |
| async_tree_none            | 223 ms                                                      | 219 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 404 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 593 ms: 1.16x slower                                                       |
| async_tree_io              | 521 ms                                                      | 603 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_tcp, async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 48.1 ms                                                     | 56.5 ms: 1.17x slower                                                      |
| nbody          | 64.5 ms                                                     | 85.6 ms: 1.33x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 16.2 ms: 1.11x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.7 us: 1.03x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.82 us: 1.03x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 19.0 us: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.0 ms: 1.06x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.17 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.41 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 220 us: 1.20x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 159 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 7.19 ms: 1.15x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 38.3 ms: 1.17x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                      |
| django_template | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 528 us: 16.44x faster                                                      |
| deepcopy                   | 223 us                                                      | 193 us: 1.15x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 268 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| async_tree_none            | 223 ms                                                      | 219 ms: 1.02x faster                                                       |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.01x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.6 us: 1.01x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.99 us: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.4 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 69.2 ms: 1.01x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.90 ms: 1.01x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 94.1 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.64 us: 1.03x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.7 us: 1.03x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.82 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 404 ms: 1.04x slower                                                       |
| coverage                   | 46.7 ms                                                     | 48.7 ms: 1.04x slower                                                      |
| 2to3                       | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| pickle_dict                | 18.0 us                                                     | 19.0 us: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 91.5 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.0 ms: 1.06x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.17 us: 1.06x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 78.1 ms: 1.08x slower                                                      |
| go                         | 84.6 ms                                                     | 91.7 ms: 1.08x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                      |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 44.2 ms: 1.09x slower                                                      |
| sympy_expand               | 285 ms                                                      | 312 ms: 1.10x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                     |
| regex_v8                   | 14.7 ms                                                     | 16.2 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 59.4 ms: 1.11x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.41 ms: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 928 us: 1.12x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.13x slower                                                       |
| logging_format             | 6.15 us                                                     | 7.02 us: 1.14x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 37.9 ms: 1.15x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.19 ms: 1.15x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 593 ms: 1.16x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.62 us: 1.16x slower                                                      |
| async_tree_io              | 521 ms                                                      | 603 ms: 1.16x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.72 ms: 1.16x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 200 ms: 1.17x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 38.3 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 575 ms: 1.17x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 50.1 ms: 1.17x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                      |
| float                      | 48.1 ms                                                     | 56.5 ms: 1.17x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 65.5 ms: 1.18x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.18 sec: 1.19x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 220 us: 1.20x slower                                                       |
| chaos                      | 37.9 ms                                                     | 45.5 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.15 ms: 1.21x slower                                                      |
| pyflate                    | 275 ms                                                      | 332 ms: 1.21x slower                                                       |
| django_template            | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 65.3 ms: 1.21x slower                                                      |
| fannkuch                   | 245 ms                                                      | 297 ms: 1.21x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| hexiom                     | 3.69 ms                                                     | 4.52 ms: 1.22x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 936 us: 1.23x slower                                                       |
| scimark_fft                | 174 ms                                                      | 215 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.33 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.4 ms: 1.25x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 159 us: 1.25x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 74.6 ms: 1.26x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 65.4 ns: 1.28x slower                                                      |
| raytrace                   | 156 ms                                                      | 201 ms: 1.29x slower                                                       |
| richards                   | 26.0 ms                                                     | 33.7 ms: 1.29x slower                                                      |
| richards_super             | 29.3 ms                                                     | 38.1 ms: 1.30x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 94.8 ms: 1.32x slower                                                      |
| nbody                      | 64.5 ms                                                     | 85.6 ms: 1.33x slower                                                      |
| json                       | 2.98 ms                                                     | 4.52 ms: 1.51x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (12): pycparser, async_tree_memoization, python_startup, python_startup_no_site, unpack_sequence, asyncio_tcp, bench_thread_pool, regex_dna, pidigits, pickle_list, async_tree_none_tg, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown