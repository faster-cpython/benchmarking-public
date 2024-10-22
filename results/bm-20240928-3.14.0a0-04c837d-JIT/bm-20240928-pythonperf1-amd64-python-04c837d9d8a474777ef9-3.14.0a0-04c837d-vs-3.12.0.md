# Results vs. 3.12.0

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.15x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 283 ms: 1.30x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.18 sec: 1.32x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 106 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 292 ms: 1.26x faster                                                       |
| async_tree_none            | 291 ms                                                      | 237 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 234 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 639 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 297 ms: 1.14x faster                                                       |
| async_tree_io              | 731 ms                                                      | 647 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 449 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| float          | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 111 ms: 1.27x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| pickle               | 7.43 us                                                     | 8.42 us: 1.13x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 64.6 ms: 1.16x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 75.4 ms: 1.16x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 109 ms: 1.17x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.41 us: 1.21x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 47.1 ms: 1.25x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 7.32 ms: 1.29x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 256 us: 1.31x slower                                                       |
| unpickle             | 8.18 us                                                     | 11.9 us: 1.45x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.7 us: 1.49x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 204 us: 1.53x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.05 ms: 1.17x faster                                                      |
| django_template | 22.9 ms                                                     | 32.6 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                      | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.28x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 292 ms: 1.26x faster                                                       |
| async_tree_none            | 291 ms                                                      | 237 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 234 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 639 ms: 1.21x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.05 ms: 1.17x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 297 ms: 1.14x faster                                                       |
| async_tree_io              | 731 ms                                                      | 647 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 449 ms: 1.12x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.8 ms: 1.12x faster                                                      |
| deepcopy                   | 238 us                                                      | 214 us: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| comprehensions             | 14.1 us                                                     | 13.2 us: 1.07x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.02x faster                                                       |
| float                      | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.78 us: 1.01x slower                                                      |
| pathlib                    | 80.5 ms                                                     | 82.0 ms: 1.02x slower                                                      |
| pyflate                    | 295 ms                                                      | 301 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 83.8 ms: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.25 us: 1.08x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 933 us: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 49.2 ms: 1.11x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 83.1 ms: 1.11x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| chaos                      | 43.3 ms                                                     | 48.9 ms: 1.13x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.42 us: 1.13x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.85 ms: 1.14x slower                                                      |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 64.6 ms: 1.16x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 75.4 ms: 1.16x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.81 us: 1.16x slower                                                      |
| generators                 | 22.5 ms                                                     | 26.2 ms: 1.16x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 569 ms: 1.17x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 109 ms: 1.17x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.1 ms: 1.17x slower                                                      |
| logging_simple             | 6.28 us                                                     | 7.36 us: 1.17x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 106 ms: 1.19x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.24 sec: 1.19x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 612 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.8 ms: 1.20x slower                                                      |
| pycparser                  | 699 ms                                                      | 837 ms: 1.20x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 75.6 ms: 1.20x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.41 us: 1.21x slower                                                      |
| json                       | 3.05 ms                                                     | 3.68 ms: 1.21x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.22x slower                                                      |
| python_startup             | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.68 sec: 1.23x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 47.1 ms: 1.25x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.19 ms: 1.26x slower                                                      |
| go                         | 91.6 ms                                                     | 116 ms: 1.26x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 111 ms: 1.27x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 239 ms: 1.28x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 118 ms: 1.28x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.32 ms: 1.29x slower                                                      |
| 2to3                       | 218 ms                                                      | 283 ms: 1.30x slower                                                       |
| sympy_str                  | 175 ms                                                      | 227 ms: 1.30x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 256 us: 1.31x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.18 sec: 1.32x slower                                                     |
| raytrace                   | 192 ms                                                      | 253 ms: 1.32x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 1.06 ms: 1.32x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.37 ms: 1.34x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.01 ms: 1.35x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 17.5 ms: 1.35x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 19.6 ms: 1.37x slower                                                      |
| sympy_expand               | 284 ms                                                      | 390 ms: 1.37x slower                                                       |
| richards_super             | 32.1 ms                                                     | 44.2 ms: 1.38x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 131 us: 1.38x slower                                                       |
| async_generators           | 239 ms                                                      | 336 ms: 1.40x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 85.0 ns: 1.41x slower                                                      |
| django_template            | 22.9 ms                                                     | 32.6 ms: 1.42x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 84.0 ms: 1.43x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 50.0 ms: 1.45x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.9 us: 1.45x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.95 ms: 1.45x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.24 ms: 1.47x slower                                                      |
| coverage                   | 40.8 ms                                                     | 60.8 ms: 1.49x slower                                                      |
| json_loads                 | 13.9 us                                                     | 20.7 us: 1.49x slower                                                      |
| richards                   | 28.4 ms                                                     | 42.4 ms: 1.49x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 204 us: 1.53x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 61.0 ns: 1.63x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.15x slower                                                               |
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown