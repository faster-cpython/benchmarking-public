# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.01x slower
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.5 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 211 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 92.3 ms: 1.06x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 6.99 us: 1.06x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.88 us: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.11x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.27 us: 1.13x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 211 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.37x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.61 sec: 1.30x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.6 ms: 1.08x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 83.5 ms: 1.07x faster                                                      |
| pickle                     | 7.43 us                                                     | 6.99 us: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 813 us: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 66.2 ms: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 87.8 ms: 1.04x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 469 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                      |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.31 us: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| raytrace                   | 192 ms                                                      | 195 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.0 ms: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.88 us: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.90 us: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.0 ms: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 92.3 ms: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.5 ms: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.9 ms: 1.07x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.8 ns: 1.07x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                     |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.79 ms: 1.09x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.6 ms: 1.10x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 326 ms: 1.11x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.11x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.57 ms: 1.12x slower                                                      |
| scimark_fft                | 184 ms                                                      | 206 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 905 us: 1.13x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 42.2 ns: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.27 us: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.7 ms: 1.14x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.2 ms: 1.15x slower                                                      |
| nbody                      | 71.9 ms                                                     | 83.3 ms: 1.16x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 874 us: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.8 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| pycparser                  | 699 ms                                                      | 826 ms: 1.18x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 93.9 ms: 1.19x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.01 ms: 1.21x slower                                                      |
| fannkuch                   | 247 ms                                                      | 302 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): gc_traversal, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.19% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown