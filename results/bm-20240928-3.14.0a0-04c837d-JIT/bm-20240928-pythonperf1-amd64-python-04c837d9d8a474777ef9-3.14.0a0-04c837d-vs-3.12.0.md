# Results vs. 3.12.0

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.03x faster
- HPT reliability: 83.34%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 248 ms: 1.14x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 98.4 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 556 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 47.9 ms: 1.50x faster                                                      |
| float          | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 94.1 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.39 us: 1.01x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.02x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 201 us: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.77 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): pickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                      |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.0 us: 1.59x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 44.0 ms: 1.52x faster                                                      |
| nbody                      | 71.9 ms                                                     | 47.9 ms: 1.50x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 556 ms: 1.39x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.9 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                       |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.26x faster                                                       |
| float                      | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 38.7 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.71 sec: 1.22x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.86 ms: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.07x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 55.3 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.1 ns: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 826 us: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.48 us: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.08 us: 1.03x faster                                                      |
| fannkuch                   | 247 ms                                                      | 239 ms: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| generators                 | 22.5 ms                                                     | 22.3 ms: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.9 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.4 ms: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.39 us: 1.01x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.1 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 716 ms: 1.03x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 201 us: 1.03x slower                                                       |
| go                         | 91.6 ms                                                     | 94.1 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 72.9 ms: 1.05x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.36 ms: 1.06x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.1 ms: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                       |
| raytrace                   | 192 ms                                                      | 210 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.09x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 98.4 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 895 us: 1.11x slower                                                       |
| async_generators           | 239 ms                                                      | 267 ms: 1.11x slower                                                       |
| sympy_str                  | 175 ms                                                      | 195 ms: 1.11x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 545 ms: 1.12x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| 2to3                       | 218 ms                                                      | 248 ms: 1.14x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.57 sec: 1.14x slower                                                     |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.16x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.92 sec: 1.16x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 885 us: 1.18x slower                                                       |
| sympy_expand               | 284 ms                                                      | 334 ms: 1.18x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.3 ms: 1.18x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.77 us: 1.19x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.03 ms: 1.23x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 43.0 ms: 1.25x slower                                                      |
| richards_super             | 32.1 ms                                                     | 41.7 ms: 1.30x slower                                                      |
| richards                   | 28.4 ms                                                     | 38.7 ms: 1.36x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 56.8 ns: 1.51x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (6): json, pprint_pformat, pickle_list, pprint_safe_repr, gc_traversal, json_dumps
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown