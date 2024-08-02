# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.05x faster
- HPT reliability: 98.78%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 244 ms: 1.12x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.14 ms: 1.03x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 85.3 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                       |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.2 ms: 1.41x faster                                                      |
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 170 us: 1.15x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.12x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| pickle               | 7.43 us                                                     | 7.08 us: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.96 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.90 ms: 1.45x faster                                                      |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.37 sec: 1.53x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 46.1 ms: 1.45x faster                                                      |
| mako                       | 7.09 ms                                                     | 4.90 ms: 1.45x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.2 ms: 1.41x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                       |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.20x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.4 ms: 1.17x faster                                                      |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 170 us: 1.15x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.15x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.3 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 935 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.12x faster                                                     |
| fannkuch                   | 247 ms                                                      | 221 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 461 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.5 ns: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.15 us: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.76 us: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.1 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.08 us: 1.05x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 85.3 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 826 us: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.0 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                                      |
| richards_super             | 32.1 ms                                                     | 32.3 ms: 1.01x slower                                                      |
| deepcopy                   | 238 us                                                      | 240 us: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.4 ms: 1.01x slower                                                      |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.7 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.15 us: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 721 ms: 1.03x slower                                                       |
| chameleon                  | 4.98 ms                                                     | 5.14 ms: 1.03x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 81.5 ms: 1.03x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.05x slower                                                     |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 73.8 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.96 us: 1.09x slower                                                      |
| coverage                   | 40.8 ms                                                     | 45.3 ms: 1.11x slower                                                      |
| 2to3                       | 218 ms                                                      | 244 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.62 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.67 ms: 1.14x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 911 us: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (5): asyncio_tcp, regex_compile, sqlglot_parse, pickle_list, regex_v8
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.78% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown