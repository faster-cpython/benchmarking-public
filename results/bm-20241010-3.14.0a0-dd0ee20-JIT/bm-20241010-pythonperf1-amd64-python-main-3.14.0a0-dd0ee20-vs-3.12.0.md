# Results vs. 3.12.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: dd0ee20
- commit date: 2024-10-10
- overall geometric mean: 1.14x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 283 ms: 1.30x slower                                       |
| docutils       | 1.66 sec                                                    | 2.17 sec: 1.31x slower                                     |
| tornado_http   | 89.5 ms                                                     | 106 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                       | 1.26x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                       |
| async_tree_none_tg         | 285 ms                                                      | 231 ms: 1.23x faster                                       |
| async_tree_none            | 291 ms                                                      | 238 ms: 1.23x faster                                       |
| async_tree_io_tg           | 771 ms                                                      | 633 ms: 1.22x faster                                       |
| async_tree_io              | 731 ms                                                      | 639 ms: 1.14x faster                                       |
| async_tree_memoization     | 339 ms                                                      | 298 ms: 1.14x faster                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 442 ms: 1.14x faster                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                       |
| Geometric mean             | (ref)                                                       | 1.18x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 48.1 ms: 1.49x faster                                      |
| float          | 56.8 ms                                                     | 54.6 ms: 1.04x faster                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                       |
| regex_effbot   | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                      |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                      |
| regex_compile  | 87.5 ms                                                     | 107 ms: 1.22x slower                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                     |
| unpickle_list        | 2.75 us                                                     | 3.07 us: 1.12x slower                                      |
| pickle               | 7.43 us                                                     | 8.55 us: 1.15x slower                                      |
| xml_etree_generate   | 55.8 ms                                                     | 64.6 ms: 1.16x slower                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 76.0 ms: 1.17x slower                                      |
| xml_etree_parse      | 93.0 ms                                                     | 109 ms: 1.17x slower                                       |
| xml_etree_process    | 37.7 ms                                                     | 46.7 ms: 1.24x slower                                      |
| pickle_dict          | 18.4 us                                                     | 22.9 us: 1.24x slower                                      |
| pickle_list          | 2.83 us                                                     | 3.56 us: 1.26x slower                                      |
| pickle_pure_python   | 195 us                                                      | 251 us: 1.29x slower                                       |
| json_dumps           | 5.70 ms                                                     | 7.69 ms: 1.35x slower                                      |
| unpickle             | 8.18 us                                                     | 11.4 us: 1.39x slower                                      |
| json_loads           | 13.9 us                                                     | 21.2 us: 1.52x slower                                      |
| unpickle_pure_python | 133 us                                                      | 207 us: 1.55x slower                                       |
| Geometric mean       | (ref)                                                       | 1.26x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                      |
| python_startup         | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.17 ms: 1.15x faster                                      |
| django_template | 22.9 ms                                                     | 32.7 ms: 1.43x slower                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody                      | 71.9 ms                                                     | 48.1 ms: 1.49x faster                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.57 sec: 1.34x faster                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.27x faster                                      |
| async_tree_none_tg         | 285 ms                                                      | 231 ms: 1.23x faster                                       |
| async_tree_none            | 291 ms                                                      | 238 ms: 1.23x faster                                       |
| async_tree_io_tg           | 771 ms                                                      | 633 ms: 1.22x faster                                       |
| mako                       | 7.09 ms                                                     | 6.17 ms: 1.15x faster                                      |
| async_tree_io              | 731 ms                                                      | 639 ms: 1.14x faster                                       |
| async_tree_memoization     | 339 ms                                                      | 298 ms: 1.14x faster                                       |
| spectral_norm              | 66.9 ms                                                     | 58.8 ms: 1.14x faster                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 442 ms: 1.14x faster                                       |
| deepcopy                   | 238 us                                                      | 214 us: 1.11x faster                                       |
| comprehensions             | 14.1 us                                                     | 12.8 us: 1.10x faster                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.43 ms: 1.05x faster                                      |
| float                      | 56.8 ms                                                     | 54.6 ms: 1.04x faster                                      |
| scimark_fft                | 184 ms                                                      | 179 ms: 1.03x faster                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.0 ms: 1.01x slower                                      |
| pathlib                    | 80.5 ms                                                     | 82.0 ms: 1.02x slower                                      |
| pprint_safe_repr           | 513 ms                                                      | 523 ms: 1.02x slower                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                     |
| scimark_sor                | 78.8 ms                                                     | 80.7 ms: 1.02x slower                                      |
| pyflate                    | 295 ms                                                      | 309 ms: 1.05x slower                                       |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                      |
| meteor_contest             | 74.6 ms                                                     | 80.0 ms: 1.07x slower                                      |
| dulwich_log                | 44.3 ms                                                     | 47.6 ms: 1.07x slower                                      |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                     |
| deepcopy_reduce            | 2.09 us                                                     | 2.27 us: 1.08x slower                                      |
| bench_thread_pool          | 857 us                                                      | 930 us: 1.09x slower                                       |
| chaos                      | 43.3 ms                                                     | 47.7 ms: 1.10x slower                                      |
| fannkuch                   | 247 ms                                                      | 274 ms: 1.11x slower                                       |
| unpickle_list              | 2.75 us                                                     | 3.07 us: 1.12x slower                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                      |
| logging_format             | 6.72 us                                                     | 7.64 us: 1.14x slower                                      |
| logging_simple             | 6.28 us                                                     | 7.14 us: 1.14x slower                                      |
| regex_effbot               | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                      |
| pickle                     | 7.43 us                                                     | 8.55 us: 1.15x slower                                      |
| generators                 | 22.5 ms                                                     | 26.0 ms: 1.15x slower                                      |
| asyncio_tcp                | 487 ms                                                      | 563 ms: 1.15x slower                                       |
| xml_etree_generate         | 55.8 ms                                                     | 64.6 ms: 1.16x slower                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 76.0 ms: 1.17x slower                                      |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                      |
| xml_etree_parse            | 93.0 ms                                                     | 109 ms: 1.17x slower                                       |
| logging_silent             | 60.5 ns                                                     | 71.4 ns: 1.18x slower                                      |
| tornado_http               | 89.5 ms                                                     | 106 ms: 1.18x slower                                       |
| pycparser                  | 699 ms                                                      | 833 ms: 1.19x slower                                       |
| nqueens                    | 62.8 ms                                                     | 75.2 ms: 1.20x slower                                      |
| bench_mp_pool              | 69.2 ms                                                     | 83.6 ms: 1.21x slower                                      |
| mdp                        | 1.37 sec                                                    | 1.67 sec: 1.22x slower                                     |
| regex_compile              | 87.5 ms                                                     | 107 ms: 1.22x slower                                       |
| go                         | 91.6 ms                                                     | 112 ms: 1.22x slower                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                      |
| xml_etree_process          | 37.7 ms                                                     | 46.7 ms: 1.24x slower                                      |
| json                       | 3.05 ms                                                     | 3.78 ms: 1.24x slower                                      |
| python_startup             | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                      |
| pickle_dict                | 18.4 us                                                     | 22.9 us: 1.24x slower                                      |
| pickle_list                | 2.83 us                                                     | 3.56 us: 1.26x slower                                      |
| raytrace                   | 192 ms                                                      | 245 ms: 1.27x slower                                       |
| telco                      | 4.13 ms                                                     | 5.30 ms: 1.28x slower                                      |
| pickle_pure_python         | 195 us                                                      | 251 us: 1.29x slower                                       |
| sympy_sum                  | 91.5 ms                                                     | 118 ms: 1.29x slower                                       |
| sympy_str                  | 175 ms                                                      | 226 ms: 1.29x slower                                       |
| sqlglot_parse              | 804 us                                                      | 1.04 ms: 1.30x slower                                      |
| 2to3                       | 218 ms                                                      | 283 ms: 1.30x slower                                       |
| sqlglot_normalize          | 187 ms                                                      | 244 ms: 1.30x slower                                       |
| docutils                   | 1.66 sec                                                    | 2.17 sec: 1.31x slower                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.35 ms: 1.33x slower                                      |
| sympy_integrate            | 13.0 ms                                                     | 17.3 ms: 1.34x slower                                      |
| json_dumps                 | 5.70 ms                                                     | 7.69 ms: 1.35x slower                                      |
| sympy_expand               | 284 ms                                                      | 389 ms: 1.37x slower                                       |
| richards_super             | 32.1 ms                                                     | 44.4 ms: 1.38x slower                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 132 us: 1.39x slower                                       |
| unpickle                   | 8.18 us                                                     | 11.4 us: 1.39x slower                                      |
| coroutines                 | 14.3 ms                                                     | 19.9 ms: 1.39x slower                                      |
| scimark_lu                 | 58.9 ms                                                     | 82.8 ms: 1.41x slower                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 49.1 ms: 1.42x slower                                      |
| django_template            | 22.9 ms                                                     | 32.7 ms: 1.43x slower                                      |
| hexiom                     | 4.10 ms                                                     | 5.85 ms: 1.43x slower                                      |
| create_gc_cycles           | 752 us                                                      | 1.08 ms: 1.43x slower                                      |
| richards                   | 28.4 ms                                                     | 41.0 ms: 1.45x slower                                      |
| coverage                   | 40.8 ms                                                     | 59.6 ms: 1.46x slower                                      |
| async_generators           | 239 ms                                                      | 351 ms: 1.47x slower                                       |
| json_loads                 | 13.9 us                                                     | 21.2 us: 1.52x slower                                      |
| unpickle_pure_python       | 133 us                                                      | 207 us: 1.55x slower                                       |
| unpack_sequence            | 37.5 ns                                                     | 58.7 ns: 1.57x slower                                      |
| gc_traversal               | 1.52 ms                                                     | 2.52 ms: 1.66x slower                                      |
| Geometric mean             | (ref)                                                       | 1.14x slower                                               |

Benchmark hidden because not significant (1): sqlite_synth
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241010-3.14.0a0-dd0ee20-JIT/bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown