# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.06x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 239 ms: 1.09x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.39 ms: 1.08x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 87.2 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.32x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 410 ms: 1.19x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 290 ms: 1.17x faster                                                       |
| async_tree_io              | 731 ms                                                      | 627 ms: 1.17x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 81.2 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 111 ms: 1.27x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.26 us: 1.02x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.82 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.4 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.72 us: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.02 us: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 167 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.7 ms: 1.03x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.54 ms: 1.06x slower                                                      |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.37 sec: 1.53x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.32x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 221 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 390 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 410 ms: 1.19x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 290 ms: 1.17x faster                                                       |
| async_tree_io              | 731 ms                                                      | 627 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 87.2 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.26 us: 1.02x faster                                                      |
| raytrace                   | 192 ms                                                      | 188 ms: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 68.1 ms: 1.02x faster                                                      |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.64 us: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.25 us: 1.00x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.82 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 16.7 ms: 1.03x slower                                                      |
| comprehensions             | 14.1 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.4 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.5 ms: 1.04x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.7 ms: 1.06x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.0 ms: 1.06x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 79.0 ms: 1.06x slower                                                      |
| async_generators           | 239 ms                                                      | 254 ms: 1.06x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.54 ms: 1.06x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.72 us: 1.07x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.02 us: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.26 us: 1.08x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 52.3 ms: 1.08x slower                                                      |
| chameleon                  | 4.98 ms                                                     | 5.39 ms: 1.08x slower                                                      |
| 2to3                       | 218 ms                                                      | 239 ms: 1.09x slower                                                       |
| coverage                   | 40.8 ms                                                     | 44.8 ms: 1.10x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                      |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.11x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                       |
| deepcopy                   | 238 us                                                      | 266 us: 1.12x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.17 sec: 1.12x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 577 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 38.9 ms: 1.13x slower                                                      |
| sympy_str                  | 175 ms                                                      | 197 ms: 1.13x slower                                                       |
| nbody                      | 71.9 ms                                                     | 81.2 ms: 1.13x slower                                                      |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.14x slower                                                       |
| go                         | 91.6 ms                                                     | 104 ms: 1.14x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 71.7 ms: 1.14x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.57 sec: 1.14x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.14x slower                                                      |
| pyflate                    | 295 ms                                                      | 339 ms: 1.15x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 927 us: 1.15x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 93.2 ms: 1.18x slower                                                      |
| sympy_expand               | 284 ms                                                      | 337 ms: 1.19x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.9 ms: 1.19x slower                                                      |
| pycparser                  | 699 ms                                                      | 831 ms: 1.19x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 80.8 ms: 1.21x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.04 ms: 1.22x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 926 us: 1.23x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.70 ms: 1.25x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 119 us: 1.25x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 167 us: 1.26x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 111 ms: 1.27x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 77.4 ns: 1.28x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.29 ms: 1.29x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 31.2 us: 1.31x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.76 ms: 1.40x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 83.1 ms: 1.41x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (5): bench_thread_pool, xml_etree_parse, asyncio_tcp, pickle_dict, regex_effbot
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown