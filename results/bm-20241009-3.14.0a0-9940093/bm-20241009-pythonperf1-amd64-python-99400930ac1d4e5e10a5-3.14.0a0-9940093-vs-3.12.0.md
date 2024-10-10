# Results vs. 3.12.0

- fork: python
- ref: 99400930ac1d4e5e10a5
- machine: windows-amd64
- commit hash: 9940093
- commit date: 2024-10-09
- overall geometric mean: 1.04x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 94.1 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 268 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 593 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 404 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.6 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.92 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                      |
| unpickle             | 8.18 us                                                     | 9.17 us: 1.12x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.41 ms: 1.13x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 42.5 ms: 1.13x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.13x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.19 ms: 1.01x slower                                                      |
| django_template | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 268 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 593 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                       |
| deepcopy                   | 238 us                                                      | 193 us: 1.23x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.72 sec: 1.22x faster                                                     |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 404 ms: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                      |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.10x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.6 us: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.1 ms: 1.02x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.53 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.0 ms: 1.01x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.19 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 50.1 ms: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.92 us: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                     |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                      |
| raytrace                   | 192 ms                                                      | 201 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.02 us: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.1 ms: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.5 ms: 1.05x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 94.1 ms: 1.05x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.05x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.62 us: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.72 ms: 1.06x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.9 ns: 1.07x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| pycparser                  | 699 ms                                                      | 749 ms: 1.07x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.33 ms: 1.08x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 65.4 ns: 1.08x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.9 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.52 ms: 1.10x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.3 ms: 1.11x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 74.6 ms: 1.11x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.17 us: 1.12x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 575 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.15 ms: 1.12x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.41 ms: 1.13x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.5 ms: 1.13x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.13x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.18 sec: 1.13x slower                                                     |
| pyflate                    | 295 ms                                                      | 332 ms: 1.13x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.4 ms: 1.15x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 936 us: 1.16x slower                                                       |
| scimark_fft                | 184 ms                                                      | 215 ms: 1.16x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.7 ms: 1.19x slower                                                      |
| richards_super             | 32.1 ms                                                     | 38.1 ms: 1.19x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.90 ms: 1.19x slower                                                      |
| nbody                      | 71.9 ms                                                     | 85.6 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                       |
| fannkuch                   | 247 ms                                                      | 297 ms: 1.20x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 94.8 ms: 1.20x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 928 us: 1.23x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 652 ms: 1.34x slower                                                       |
| json                       | 3.05 ms                                                     | 4.52 ms: 1.48x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): float, dulwich_log, pathlib, bench_mp_pool, sympy_sum, go
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241009-3.14.0a0-9940093/bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown