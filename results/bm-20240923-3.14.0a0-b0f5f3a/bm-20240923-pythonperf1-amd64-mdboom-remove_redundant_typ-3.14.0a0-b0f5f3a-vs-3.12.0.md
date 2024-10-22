# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.01x slower
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.2 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 81.8 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.6 ms: 1.01x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.3 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.07 us: 1.09x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.34 us: 1.14x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.30x faster                                                     |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.14x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 84.2 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| go                         | 91.6 ms                                                     | 86.6 ms: 1.06x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 66.3 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.6 ms: 1.02x faster                                                      |
| float                      | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.6 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.00x slower                                                      |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.8 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.60 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.3 ms: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.46 us: 1.03x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 69.0 ms: 1.03x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 61.3 ms: 1.04x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.0 ns: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.8 ms: 1.04x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 734 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.06x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 543 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.42 ms: 1.08x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.07 us: 1.09x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.09x slower                                                      |
| pyflate                    | 295 ms                                                      | 322 ms: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.6 ms: 1.11x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 895 us: 1.11x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.0 ms: 1.13x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.3 ms: 1.13x slower                                                      |
| nbody                      | 71.9 ms                                                     | 81.8 ms: 1.14x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.34 us: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 92.2 ms: 1.17x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 883 us: 1.17x slower                                                       |
| fannkuch                   | 247 ms                                                      | 293 ms: 1.19x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.05 ms: 1.22x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 46.4 ns: 1.24x slower                                                      |
| json                       | 3.05 ms                                                     | 4.39 ms: 1.44x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown