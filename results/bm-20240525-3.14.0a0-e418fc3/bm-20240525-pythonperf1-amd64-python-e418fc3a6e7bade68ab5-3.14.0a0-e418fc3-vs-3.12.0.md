# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 210 ms: 1.04x faster                                                       |
| chameleon      | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                                      |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| tornado_http   | 89.5 ms                                                     | 81.6 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_none            | 291 ms                                                      | 225 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 600 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.5 ms: 1.12x faster                                                      |
| nbody          | 71.9 ms                                                     | 68.7 ms: 1.05x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 76.7 ms: 1.14x faster                                                      |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 177 us: 1.10x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.23 us: 1.03x faster                                                      |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.02x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.8 ms: 1.01x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.77 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.85 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.73 us: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.41 ms: 1.11x faster                                                      |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_none            | 291 ms                                                      | 225 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| raytrace                   | 192 ms                                                      | 157 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 600 ms: 1.22x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 76.7 ms: 1.14x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.14x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                                      |
| float                      | 56.8 ms                                                     | 50.5 ms: 1.12x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.41 ms: 1.11x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 177 us: 1.10x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 81.6 ms: 1.10x faster                                                      |
| go                         | 91.6 ms                                                     | 83.5 ms: 1.10x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 83.6 ms: 1.09x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 57.4 ms: 1.09x faster                                                      |
| sympy_str                  | 175 ms                                                      | 160 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.80 us: 1.08x faster                                                      |
| deepcopy                   | 238 us                                                      | 220 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.81 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.26 us: 1.07x faster                                                      |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 802 us: 1.07x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.2 ms: 1.06x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 966 us: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 762 us: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 22.5 us: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 997 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.00 us: 1.05x faster                                                      |
| nbody                      | 71.9 ms                                                     | 68.7 ms: 1.05x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 66.2 ms: 1.05x faster                                                      |
| sympy_expand               | 284 ms                                                      | 272 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 492 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.5 ms: 1.04x faster                                                      |
| 2to3                       | 218 ms                                                      | 210 ms: 1.04x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.3 ms: 1.04x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 470 ms: 1.04x faster                                                       |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 64.7 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.23 us: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 78.7 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                      |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.8 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.1 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                      |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.77 ms: 1.01x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.85 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 99.8 us: 1.05x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.73 us: 1.07x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.3 ms: 1.13x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.70 ms: 1.14x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 916 us: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (3): pycparser, tomli_loads, scimark_sor
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown